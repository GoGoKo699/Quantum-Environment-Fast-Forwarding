"""Independent finite checks for quantum environment fast forwarding.

Run: python verification/audit_environment.py --output verification/audit_results.json

The checks compare independently constructed objects: finite collision states,
operator recurrences, exact simplex integrals, finite-bin field projections,
word-code measurements, and entangled-reference channel matrices. They do not
prove the asymptotic query lower bounds or certify novelty.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.stats import poisson


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PSI = np.array([1, 0], dtype=complex)
VALIDATION_COUNT = 0


class ValidationError(RuntimeError):
    """A required scientific comparison did not meet its declared tolerance."""


def require(condition, message):
    """Validate explicitly so python -O cannot disable the scientific checks."""
    global VALIDATION_COUNT
    VALIDATION_COUNT += 1
    if not condition:
        raise ValidationError(message)


def rotation(theta):
    return math.cos(theta) * I2 - 1j * math.sin(theta) * X


def trace_distance(a, b):
    difference = (a - b + (a - b).conj().T) / 2
    return float(np.abs(np.linalg.eigvalsh(difference)).sum() / 2)


def partial_system_trace(amplitudes):
    # amplitudes[field, system, reference]; preserve every field coherence.
    result = np.einsum("nsr,msq->nrmq", amplitudes, amplitudes.conj())
    size = amplitudes.shape[0] * amplitudes.shape[2]
    return result.reshape(size, size)


def f_ratio(z):
    if abs(z) < 1e-4:
        return 2 * sum((z**k / math.factorial(k + 2)).real for k in range(12))
    return float(2 * ((np.expm1(z) - z) / (z * z)).real)


def continuous_probability(t, theta):
    # Stable real part, including large t and correspondingly tiny theta.
    z = complex(-2 * t * math.sin(theta) ** 2, t * math.sin(2 * theta))
    return math.exp(-1) * f_ratio(z)


def exclusive_collision_state(bins, p, q, theta):
    """Build the entire finite system/two-bath state, without a kernel formula.

    Each bin has mutually exclusive vacuum, main, and observer events. The
    bath registers use the ordinary product of local zero/one photon bases.
    """
    require(p > 0 and q > 0 and p + q < 1, "Collision probabilities must satisfy p,q>0 and p+q<1")
    u = rotation(theta)
    operators = [math.sqrt(1 - p - q) * I2, math.sqrt(p) * u, math.sqrt(q) * Z]
    amplitudes = np.zeros((2**bins, 2**bins, 2), dtype=complex)
    for symbols in itertools.product(range(3), repeat=bins):
        vector = PSI.copy()
        main = observer = 0
        for k, symbol in enumerate(symbols):
            vector = operators[symbol] @ vector
            if symbol == 1:
                main |= 1 << k
            elif symbol == 2:
                observer |= 1 << k
        amplitudes[main, observer] += vector
    normalization = float(np.vdot(amplitudes, amplitudes).real)
    single = amplitudes[:, [1 << k for k in range(bins)], :]
    uniform_amplitude = single.sum(axis=1) / math.sqrt(bins)
    probability = float(np.vdot(uniform_amplitude, uniform_amplitude).real)
    one_photon = float(np.vdot(single, single).real)
    return probability, one_photon, normalization


def exclusive_collision_transfer(bins, p, q, theta):
    """Independently trace each main output and accumulate observer amplitudes.

    The two blocks represent zero emissions and the sum of all one-emission
    amplitudes. This is a Gram-matrix recurrence, not a density-matrix claim
    for the compressed two-block register.
    """
    a = 1 - p - q
    u = rotation(theta)
    no_main = np.zeros((4, 4), dtype=complex)
    no_main[:2, :2] = math.sqrt(a) * I2
    no_main[2:, 2:] = math.sqrt(a) * I2
    no_main[2:, :2] = math.sqrt(q) * Z
    main = np.zeros((4, 4), dtype=complex)
    main[:2, :2] = math.sqrt(p) * u
    main[2:, 2:] = math.sqrt(p) * u
    gram = np.zeros((4, 4), dtype=complex)
    gram[:2, :2] = np.outer(PSI, PSI.conj())
    for _ in range(bins):
        gram = no_main @ gram @ no_main.conj().T + main @ gram @ main.conj().T
    return float(np.trace(gram[2:, 2:]).real / bins)


def collision_checks():
    exact = []
    for bins, p, q, theta in [(3, .2, .1, .17), (5, .4, .08, .31), (6, .15, .12, .7)]:
        direct, count_one, norm = exclusive_collision_state(bins, p, q, theta)
        transfer = exclusive_collision_transfer(bins, p, q, theta)
        expected_count = bins * q * (1 - q) ** (bins - 1)
        require(abs(norm - 1) < 2e-13, f"Collision state normalization failed for {bins} bins")
        require(abs(direct - transfer) < 2e-13, f"Full state/transfer witness mismatch for {bins} bins")
        require(abs(count_one - expected_count) < 2e-13, f"Observer photon-count law failed for {bins} bins")
        exact.append(dict(bins=bins, p=p, q=q, theta=theta,
                          full_state_probability=direct, transfer_probability=transfer,
                          absolute_error=abs(direct - transfer),
                          observer_one_count=count_one,
                          dephased_time_probability=count_one / bins))

    convergence = []
    for t, grids in [(10., [128, 512, 2048, 8192]), (30., [512, 2048, 8192, 32768])]:
        theta = math.asin(2 * math.pi / t) / 2
        target = continuous_probability(t, theta)
        records = []
        for bins in grids:
            # Exact normalized projection onto at most one total event/bin.
            p = t / (bins + t + 1)
            q = 1 / (bins + t + 1)
            value = exclusive_collision_transfer(bins, p, q, theta)
            records.append(dict(bins=bins, probability=value, error=abs(value - target)))
        require(records[-1]["error"] < records[0]["error"], f"Collision refinement did not improve at t={t}")
        require(records[-1]["error"] < 2e-4, f"Collision continuum discrepancy exceeds 2e-4 at t={t}")
        convergence.append(dict(t=t, theta=theta, continuous_target=target, grids=records))
    return dict(full_collision_states=exact, continuous_limit=convergence)


def multiply_polynomials(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            exponent = tuple(i + j for i, j in zip(a, b))
            result[exponent] = result.get(exponent, Fraction(0)) + x * y
    return {e: c for e, c in result.items() if c}


def gap_polynomial(n, position):
    """Gap between ordered main times, with endpoints zero and one."""
    zero = (0,) * n
    if n == 0:
        return {zero: Fraction(1)}
    result = {}
    if position == n:
        result[zero] = Fraction(1)
    else:
        e = [0] * n
        e[position] = 1
        result[tuple(e)] = Fraction(1)
    if position > 0:
        e = [0] * n
        e[position - 1] = 1
        result[tuple(e)] = result.get(tuple(e), Fraction(0)) - 1
    return result


def integrate_ordered_simplex(poly, n):
    """Exact repeated polynomial integration over 0<s1<...<sn<1.

    Uses only rational arithmetic; no Dirichlet moment or claimed E_n formula.
    """
    if n == 0:
        return poly.get((), Fraction(0))
    current = poly
    for variable in range(n):
        new = {}
        for exponent, coefficient in current.items():
            powers = list(exponent)
            degree = powers[variable]
            powers[variable] = 0
            if variable + 1 < n:
                powers[variable + 1] += degree + 1
            key = tuple(powers)
            new[key] = new.get(key, Fraction(0)) + coefficient / (degree + 1)
        current = new
    return current.get((0,) * n, Fraction(0))


def continuous_pullback_exact(n):
    return [[math.factorial(n + 1) * integrate_ordered_simplex(
        multiply_polynomials(gap_polynomial(n, k), gap_polynomial(n, ell)), n)
        for ell in range(n + 1)] for k in range(n + 1)]


def bin_pullback_exact(n, bins):
    """Project explicit finite-bin word states onto a uniform observer mode.

    For each main-bin subset, sum its allowed observer-bin amplitudes. The
    integer gap Gram matrix is divided by the field-state normalization.
    """
    numerator = [[0] * (n + 1) for _ in range(n + 1)]
    for main_bins in itertools.combinations(range(bins), n):
        boundaries = (-1,) + main_bins + (bins,)
        gaps = [boundaries[k + 1] - boundaries[k] - 1 for k in range(n + 1)]
        for k in range(n + 1):
            for ell in range(n + 1):
                numerator[k][ell] += gaps[k] * gaps[ell]
    denominator = bins * math.comb(bins, n + 1)
    return [[Fraction(x, denominator) for x in row] for row in numerator]


def pullback_checks():
    continuous = []
    for n in range(8):
        actual = continuous_pullback_exact(n)
        expected = [[Fraction(1 + int(k == ell), n + 2)
                     for ell in range(n + 1)] for k in range(n + 1)]
        require(actual == expected, f"Exact simplex pullback mismatch for n={n}")
        matrix = np.array(actual, dtype=float)
        eigenvalues = np.linalg.eigvalsh(matrix)
        require(eigenvalues.min() > 0 and eigenvalues.max() <= 1 + 2e-14,
                f"Simplex pullback is not an effect for n={n}")
        uniform = np.ones(n + 1) / math.sqrt(n + 1)
        require(np.linalg.norm(matrix @ uniform - uniform) < 2e-14,
                f"Uniform-position eigenvector failed for n={n}")
        continuous.append(dict(main_photons=n, exact_entries_match=True,
                               min_eigenvalue=float(eigenvalues.min()),
                               max_eigenvalue=float(eigenvalues.max())))

    finite = []
    for n, bins in [(0, 4), (1, 8), (2, 12), (3, 12), (4, 16), (2, 32), (2, 128)]:
        actual = bin_pullback_exact(n, bins)
        expected = [[Fraction((bins + 1) * int(k == ell) + bins - n - 1,
                              bins * (n + 2))
                     for ell in range(n + 1)] for k in range(n + 1)]
        require(actual == expected, f"Exact finite-bin projection mismatch for n={n}, K={bins}")
        matrix = np.array(actual, dtype=float)
        target = np.array(continuous_pullback_exact(n), dtype=float)
        error = float(np.linalg.norm(matrix - target, 2))
        require(abs(error - (n / bins if n else 0)) < 2e-14,
                f"Finite-bin continuum distance failed for n={n}, K={bins}")
        finite.append(dict(main_photons=n, bins=bins, exact_entries_match=True,
                           uniform_eigenvalue=float(np.ones(n + 1) @ matrix @ np.ones(n + 1) / (n + 1)),
                           operator_distance_from_continuum=error))
    return dict(exact_simplex_integrals=continuous, finite_bin_projections=finite)


def word_sampler_probability(t, theta, cutoff):
    u = rotation(theta)
    powers = [I2]
    for _ in range(cutoff):
        powers.append(u @ powers[-1])
    total = 0.0
    for n in range(cutoff + 1):
        words = [powers[n - k] @ Z @ powers[k] @ PSI for k in range(n + 1)]
        summed = np.sum(words, axis=0)
        uniform_probability = float(np.vdot(summed, summed).real / (n + 1) ** 2)
        accept = uniform_probability + (1 - uniform_probability) / (n + 2)
        total += math.exp(-1) * poisson.pmf(n, t) * accept
    return float(total)


def insertion_circuit_reference_checks():
    """Check the explicit fixed-n circuit and its bit/reference instrument."""
    records = []
    psi = np.eye(2, dtype=complex) / math.sqrt(2)
    for n, theta in [(1, .2), (3, .37), (7, .7)]:
        u = rotation(theta)
        state = np.repeat((psi / math.sqrt(n + 1))[None, :, :], n + 1, axis=0)
        state[0] = Z @ state[0]
        for step in range(1, n + 1):
            state = np.einsum("ab,kbr->kar", u, state)
            state[step] = Z @ state[step]
        ordered = np.array([np.linalg.matrix_power(u, n - k) @ Z @
                            np.linalg.matrix_power(u, k) @ psi / math.sqrt(n + 1)
                            for k in range(n + 1)])
        circuit_error = float(np.linalg.norm(state - ordered))
        effect = np.array(continuous_pullback_exact(n), dtype=float)
        # The actual effect, integrated from the physical time simplex.
        event_reference = np.einsum("lk,ksr,lsq->rq", effect, ordered, ordered.conj())
        uniform_amplitude = state.sum(axis=0) / math.sqrt(n + 1)
        uniform_reference = np.einsum("sr,sq->rq", uniform_amplitude, uniform_amplitude.conj())
        reference = np.einsum("ksr,ksq->rq", state, state.conj())
        # The operational uniform-position test plus known residual coin.
        sampled_reference = uniform_reference + (reference - uniform_reference) / (n + 2)
        instrument_error = float(np.linalg.norm(event_reference - sampled_reference))
        require(circuit_error < 3e-14, f"Insertion circuit ordering failed for n={n}")
        require(instrument_error < 3e-14, f"Bit/reference instrument mismatch for n={n}")
        require(np.linalg.eigvalsh(sampled_reference).min() >= -2e-14,
                f"Bit-one reference block is not positive for n={n}")
        require(np.linalg.eigvalsh(reference - sampled_reference).min() >= -2e-14,
                f"Bit-zero reference block is not positive for n={n}")
        records.append(dict(main_photons=n, theta=theta, ordered_circuit_error=circuit_error,
                            bit_reference_instrument_error=instrument_error,
                            event_probability=float(np.trace(sampled_reference).real),
                            prematurely_measured_position_probability=2 / (n + 2)))
    return records


def continuous_and_word_checks():
    values = []
    gamma = math.exp(-1) * (1 - 1 / (2 * math.pi) - 1 / (2 * math.pi**2))
    cases = [(0.7, .23), (3., .6)]
    cases += [(t, math.asin(2 * math.pi / t) / 2) for t in [2 * math.pi, 10., 30., 100.]]
    for t, theta in cases:
        z = complex(-2 * t * math.sin(theta)**2, t * math.sin(2 * theta))
        analytic = continuous_probability(t, theta)
        quadrature = math.exp(-1) * 2 * quad(
            lambda s: (1 - s) * math.exp(z.real * s) * math.cos(z.imag * s),
            0, 1, epsabs=2e-13, epsrel=2e-13)[0]
        cutoff = int(poisson.ppf(1 - 1e-13, t))
        word = word_sampler_probability(t, theta, cutoff)
        tail_bound = math.exp(-1) * poisson.sf(cutoff, t)
        require(abs(analytic - quadrature) < 3e-12, f"Continuum formula/quadrature mismatch at t={t}")
        require(abs(analytic - word) <= tail_bound + 3e-12, f"Continuum formula/word sampler mismatch at t={t}")
        values.append(dict(t=t, theta=theta, analytic_probability=analytic,
                           quadrature_probability=quadrature, word_sampler_probability=word,
                           word_count_cutoff=cutoff, omitted_probability_bound=float(tail_bound),
                           word_absolute_error=abs(analytic - word)))

    bounds = []
    for t in [2 * math.pi, 10., 30., 100., 1e3, 1e5, 1e8]:
        theta = math.asin(2 * math.pi / t) / 2
        probability = continuous_probability(t, theta)
        gap = math.exp(-1) - probability
        oracle_distance = 2 * math.sin(theta / 2)
        require(gap >= gamma - 1e-13, f"Universal observer-event gap failed at t={t}")
        require(oracle_distance <= math.pi**2 / (2 * t) + 1e-13,
                f"Controlled-oracle norm upper failed at t={t}")
        bounds.append(dict(t=t, theta=theta, gap=gap, controlled_oracle_norm_distance=oracle_distance,
                           hybrid_query_bound_at_error_point_one=(gap - .2) / oracle_distance))
    return dict(probability_comparisons=values, hard_family=bounds,
                universal_gap=gamma, universal_linear_query_coefficient=(gamma - .2) * 2 / math.pi**2)


def centered_reference_checks():
    rng = np.random.default_rng(20261031)
    rows = []
    for mean, epsilon in [(1., .1), (10., .1), (100., .1), (400., .1)]:
        d = 3
        x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        basis, _ = np.linalg.qr(x)
        phases = rng.uniform(-math.pi, math.pi, d)
        unitary = basis @ np.diag(np.exp(1j * phases)) @ basis.conj().T
        # A maximally entangled input gives the channel's normalized Choi matrix.
        psi = np.eye(d, dtype=complex) / math.sqrt(d)
        # The explicit C8 window reserves half the error for state preparation.
        ell = math.log(8 / epsilon**2)
        deviation = math.sqrt(2 * mean * ell)
        low = max(0, math.floor(mean - deviation))
        high = math.ceil(mean + deviation + 2 * ell)
        counts = np.arange(low, high + 1)
        weights = poisson.pmf(counts, mean)
        mass = float(weights.sum())
        coefficients = np.sqrt(weights / mass)
        original = np.array([c * np.linalg.matrix_power(unitary, int(n)) @ psi
                             for c, n in zip(coefficients, counts)])
        centered = np.array([c * np.linalg.matrix_power(unitary, int(n - low)) @ psi
                             for c, n in zip(coefficients, counts)])
        original_output = partial_system_trace(original)
        centered_output = partial_system_trace(centered)
        error = float(np.linalg.norm(original_output - centered_output))
        tail = float(poisson.cdf(low - 1, mean) + poisson.sf(high, mean))
        require(error < 3e-11, f"Centered reference Choi identity failed for mean={mean}")
        require(tail <= epsilon**2 / 4, f"Poisson concentration window failed for mean={mean}")
        overlap = np.vdot(original, centered)
        retained_system_distance = math.sqrt(max(0, 1 - abs(overlap)**2))
        dephased = np.zeros_like(original_output)
        for k in range(len(counts)):
            block = slice(k * d, (k + 1) * d)
            dephased[block, block] = original_output[block, block]
        coherence = float(np.linalg.norm(original_output - dephased))
        require(coherence > .05, f"Number-coherence negative control is ineffective for mean={mean}")
        if low:
            require(retained_system_distance > .05,
                    f"Retained-system negative control is ineffective for mean={mean}")
        row = dict(mean=mean, epsilon=epsilon, window=[low, high], forward_queries=high - low,
                   tail_probability=tail, half_diamond_upper=math.sqrt(tail),
                   entangled_reference_choi_error=error,
                   field_number_coherence_frobenius_norm=coherence,
                   retaining_system_negative_control_distance=retained_system_distance)

        if mean <= 10:
            maximum = max(high + 8, int(poisson.ppf(1 - 1e-14, mean)))
            all_counts = np.arange(maximum + 1)
            all_weights = poisson.pmf(all_counts, mean)
            all_weights /= all_weights.sum()
            full = np.array([math.sqrt(p) * np.linalg.matrix_power(unitary, int(n)) @ psi
                             for p, n in zip(all_weights, all_counts)])
            embedded = np.zeros_like(full)
            embedded[low:high + 1] = original
            distance = trace_distance(partial_system_trace(full), partial_system_trace(embedded))
            require(distance <= math.sqrt(tail) + 3e-7,
                    f"Finite full-field/reference truncation bound failed for mean={mean}")
            row["finite_full_field_reference_trace_distance"] = distance
        rows.append(row)

    # A common shift must fail without the commuting-powers hypothesis.
    psi = np.eye(2, dtype=complex) / math.sqrt(2)
    choices = [(n, m) for n in range(2, 5) for m in range(3, 6)]
    u1 = rotation(.41)
    for label, u2 in [("commuting", rotation(.73)),
                      ("noncommuting", math.cos(.73) * I2 - 1j * math.sin(.73) * Z)]:
        full = np.array([np.linalg.matrix_power(u2, m) @ np.linalg.matrix_power(u1, n) @ psi / 3
                         for n, m in choices])
        shifted = np.array([np.linalg.matrix_power(u2, m - 3) @ np.linalg.matrix_power(u1, n - 2) @ psi / 3
                            for n, m in choices])
        distance = trace_distance(partial_system_trace(full), partial_system_trace(shifted))
        if label == "commuting":
            require(distance < 2e-13, "Commuting coordinatewise centering failed")
        else:
            require(distance > .1, "Noncommuting-centering negative control is ineffective")
        rows.append(dict(multijump_control=label, field_reference_distance=distance))
    return rows


def phase_contract_check():
    mean, phase = 8., .4
    # Same system unitary channel, different specified phase-resolved output.
    a = rotation(.31)
    b = np.exp(1j * phase) * a
    system_difference = float(np.linalg.norm(np.kron(a, a.conj()) - np.kron(b, b.conj())))
    phase_distance = math.sqrt(-math.expm1(-2 * mean * (1 - math.cos(phase))))
    require(system_difference < 1e-13, "Global rephasing changed the system channel")
    require(phase_distance > .5, "Jump-phase field-output negative control is ineffective")
    return dict(system_channel_difference=system_difference,
                coherent_field_distance_on_a_known_eigenstate=phase_distance,
                interpretation="Jump phases are part of the specified dilation and controlled-oracle interface.")


def main():
    global VALIDATION_COUNT
    VALIDATION_COUNT = 0
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("audit_results.json"))
    args = parser.parse_args()
    result = {
        "status": "passed",
        "seed": 20261031,
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "scope": "Finite normalization, time ordering, coherence, output encoding and error checks; analytical proofs establish general bounds.",
        "collisions": collision_checks(),
        "measurement_pullback": pullback_checks(),
        "insertion_circuit_reference": insertion_circuit_reference_checks(),
        "continuous_and_word_witness": continuous_and_word_checks(),
        "centered_reference": centered_reference_checks(),
        "phase_contract": phase_contract_check(),
    }
    result["checks_performed"] = VALIDATION_COUNT
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "output": str(args.output),
                      "checks_performed": result["checks_performed"],
                      "universal_gap": result["continuous_and_word_witness"]["universal_gap"],
                      "linear_query_coefficient_at_error_point_one": result["continuous_and_word_witness"]["universal_linear_query_coefficient"],
                      "exact_simplex_sectors": len(result["measurement_pullback"]["exact_simplex_integrals"]),
                      "finite_bin_sectors": len(result["measurement_pullback"]["finite_bin_projections"])}, indent=2))


if __name__ == "__main__":
    main()
