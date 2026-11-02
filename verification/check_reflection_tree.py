#!/usr/bin/env python3
"""Independent finite checks of the field-only leaf-loop parity construction."""
from __future__ import annotations
import argparse
import itertools
import json
import math
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import expm

def require(condition, message):
    """Keep scientific checks active under Python optimization."""
    if not condition:
        raise ValidationError(message)

class ValidationError(RuntimeError):
    """A required finite scientific comparison failed."""

def vertices(m):
    out = [()]
    for d in range(1, m + 1):
        out.extend((w for w in itertools.product(range(3), repeat=d) if all((w[i] != w[i + 1] for i in range(d - 1)))))
    return out

def move(v, j, m):
    if v and v[-1] == j:
        return (v[:-1], False)
    if len(v) < m:
        return (v + (j,), False)
    return (v, True)

def trajectory(w, bits, boundary_z):
    m = len(bits)
    v, a, phase, loops = ((), 0, 1, 0)
    for j in w:
        nxt, loop = move(v, j, m)
        if loop:
            loops += 1
            if boundary_z:
                phase *= (-1) ** a
        else:
            a ^= bits[max(len(v), len(nxt)) - 1]
        v = nxt
    return (v, a, phase, loops)

def exact_reflections(bits, boundary_z):
    vs = vertices(len(bits))
    vi = {v: i for i, v in enumerate(vs)}
    rs = []
    for j in range(3):
        r = np.zeros((2 * len(vs), 2 * len(vs)))
        for v in vs:
            for a in (0, 1):
                nxt, loop = move(v, j, len(bits))
                b = a if loop else a ^ bits[max(len(v), len(nxt)) - 1]
                z = (-1) ** a if loop and boundary_z else 1
                r[2 * vi[nxt] + b, 2 * vi[v] + a] = z
        require(np.array_equal(r, r.T), 'Required three-reflection comparison failed: np.array_equal(r, r.T)')
        require(np.array_equal(r @ r, np.eye(len(r))), 'Required three-reflection comparison failed: np.array_equal(r @ r, np.eye(len(r)))')
        rs.append(r)
    return rs

def field_matrix(bits, t, nmax, boundary_z):
    vs = vertices(len(bits))
    vi = {v: i for i, v in enumerate(vs)}
    words = [w for n in range(nmax + 1) for w in itertools.product(range(3), repeat=n)]
    a = np.zeros((2 * len(vs), len(words)))
    p, b = (np.zeros(len(vs)), np.zeros(len(vs)))
    for c, w in enumerate(words):
        v, answer, phase, k = trajectory(w, bits, boundary_z)
        n = len(w)
        prob = math.exp(-t) * (t / 3) ** n / math.factorial(n)
        a[2 * vi[v] + answer, c] = phase * math.sqrt(prob)
        p[vi[v]] += prob
        b[vi[v]] += prob * (-1) ** k
    return (a.T @ a, p, b)

def radial(t, m, nmax):
    step = np.zeros((m + 1, m + 1))
    step[0, 1] = 1
    for d in range(1, m):
        step[d, d - 1], step[d, d + 1] = (1 / 3, 2 / 3)
    step[m, m - 1], step[m, m] = (1 / 3, 2 / 3)
    signed = step.copy()
    signed[m, m] = -2 / 3
    e0 = np.eye(m + 1)[0]
    full_p = e0 @ expm(t * (step - np.eye(m + 1)))
    full_b = e0 @ expm(t * (signed - np.eye(m + 1)))
    p, b = (np.zeros(m + 1), np.zeros(m + 1))
    pv, bv = (e0.copy(), e0.copy())
    poisson = math.exp(-t)
    for n in range(nmax + 1):
        p += poisson * pv
        b += poisson * bv
        pv = pv @ step
        bv = bv @ signed
        poisson *= t / (n + 1)
    tail = 1 - math.exp(-t) * sum((t ** n / math.factorial(n) for n in range(nmax + 1)))
    return (p, b, full_p, full_b, tail)

def run(out):
    rows = []
    max_field_parity_error = 0.0
    max_blind_error = 0.0
    max_number_dephased_error = 0.0
    max_global_number_phase_identity_error = 0.0
    for m, t in ((1, 0.7), (2, 1.2)):
        nmax = 5
        all_bits = list(itertools.product((0, 1), repeat=m))
        base = {}
        blind_base = None
        for bits in all_bits:
            exact_reflections(bits, True)
            exact_reflections(bits, False)
            field, p, b = field_matrix(bits, t, nmax, True)
            parity = sum(bits) % 2
            if parity in base:
                max_field_parity_error = max(max_field_parity_error, float(np.max(np.abs(field - base[parity]))))
            else:
                base[parity] = field
            blind, _, _ = field_matrix(bits, t, nmax, False)
            if blind_base is None:
                blind_base = blind
            max_blind_error = max(max_blind_error, float(np.max(np.abs(blind - blind_base))))
        delta = base[0] - base[1]
        counts = np.concatenate([np.full(3 ** n, n) for n in range(nmax + 1)])
        number_mask = counts[:, None] == counts[None, :]
        max_number_dephased_error = max(max_number_dephased_error, float(np.max(np.abs(np.where(number_mask, delta, 0)))))
        number_sign = (-1.0) ** counts
        max_global_number_phase_identity_error = max(max_global_number_phase_identity_error, float(np.max(np.abs(base[1] - number_sign[:, None] * base[0] * number_sign[None, :]))))
        direct_d = float(np.abs(np.linalg.eigvalsh(delta)).sum() / 2)
        fibre_d = float(np.sqrt(np.maximum(p * p - b * b, 0)).sum())
        require(abs(direct_d - fibre_d) < 1e-10, 'Required three-reflection comparison failed: abs(direct_d - fibre_d) < 1e-10')
        vs = vertices(m)
        agg_p = np.array([sum((p[i] for i, v in enumerate(vs) if len(v) == d)) for d in range(m + 1)])
        agg_b = np.array([sum((b[i] for i, v in enumerate(vs) if len(v) == d)) for d in range(m + 1)])
        rp, rb, fullp, fullb, tail = radial(t, m, nmax)
        require(np.max(np.abs(agg_p - rp)) < 1e-12, 'Required three-reflection comparison failed: np.max(np.abs(agg_p - rp)) < 1e-12')
        require(np.max(np.abs(agg_b - rb)) < 1e-12, 'Required three-reflection comparison failed: np.max(np.abs(agg_b - rb)) < 1e-12')
        require(np.max(np.abs(fullp - rp)) <= tail + 1e-12, 'Required three-reflection comparison failed: np.max(np.abs(fullp - rp)) <= tail + 1e-12')
        require(np.max(np.abs(fullb - rb)) <= tail + 1e-12, 'Required three-reflection comparison failed: np.max(np.abs(fullb - rb)) <= tail + 1e-12')
        require(np.all(fullb >= -1e-12), 'Required three-reflection comparison failed: np.all(fullb >= -1e-12)')
        require(direct_d + 1e-12 >= sum(rp - rb), 'Required three-reflection comparison failed: direct_d + 1e-12 >= sum(rp - rb)')
        rows.append({'m': m, 't': t, 'maximum_count': nmax, 'word_states': len(field), 'retained_probability': float(p.sum()), 'poisson_tail': tail, 'full_matrix_half_trace_distance': direct_d, 'endpoint_fibre_half_trace_distance': fibre_d, 'feynman_kac_bound_full': float(1 - fullb.sum()), 'radial_distance_full': float(np.sqrt(np.maximum(fullp ** 2 - fullb ** 2, 0)).sum())})
    require(max_field_parity_error < 1e-12, 'Required three-reflection comparison failed: max_field_parity_error < 1e-12')
    require(max_blind_error < 1e-12, 'Required three-reflection comparison failed: max_blind_error < 1e-12')
    require(max_number_dephased_error < 1e-12, 'Required three-reflection comparison failed: max_number_dephased_error < 1e-12')
    require(max_global_number_phase_identity_error < 1e-12, 'Required three-reflection comparison failed: max_global_number_phase_identity_error < 1e-12')
    h0 = 1513 / 1936
    asymptotic = h0 * 4 / 5 * (1 - math.exp(-5 / 3))
    operational_signal = h0 * math.exp(-0.5) / math.sqrt(3)
    require(asymptotic > 0.5, 'Required three-reflection comparison failed: asymptotic > 0.5')
    require((1 + operational_signal) / 2 - 0.1 > 0.5, 'Required three-reflection comparison failed: (1 + operational_signal) / 2 - 0.1 > 0.5')
    theorem_checks = []
    for t in (48, 96, 192, 480):
        m = int(t // 48)
        _, _, fullp, fullb, _ = radial(t, m, 0)
        bound = float(1 - fullb.sum())
        require(bound >= asymptotic - 1e-12, 'Required three-reflection comparison failed: bound >= asymptotic - 1e-12')
        theorem_checks.append({'t': t, 'm': m, 'feynman_kac_distance_lower_bound': bound, 'exact_radial_fibre_distance': float(np.sqrt(np.maximum(fullp ** 2 - fullb ** 2, 0)).sum())})
    result = {'status': 'passed', 'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__, 'finite_word_checks': rows, 'maximum_same_parity_field_matrix_error': max_field_parity_error, 'maximum_original_identity_loop_field_difference': max_blind_error, 'maximum_total_number_dephased_field_difference': max_number_dephased_error, 'maximum_global_number_phase_identity_error': max_global_number_phase_identity_error, 'uniform_analytic_distance_lower_bound': asymptotic, 'operational_signal_lower_bound': operational_signal, 'operational_success_after_half_diamond_error_0_1': (1 + operational_signal) / 2 - 0.1, 'large_time_radial_checks': theorem_checks, 'scope': 'Finite numerical checks supplement, but do not prove, the analytical lower bound.'}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('reflection_triple_results.json'))
    args = parser.parse_args()
    run(args.output)
if __name__ == '__main__':
    main()
