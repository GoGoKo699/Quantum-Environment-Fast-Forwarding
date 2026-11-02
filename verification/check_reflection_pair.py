#!/usr/bin/env python3
"""Finite diagnostics for two-reflection field witnesses; no asymptotic proof."""
import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm
from scipy.stats import poisson

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def ad(u):
    # Column-vectorization: vec(u rho u^dagger)=(conj(u) tensor u) vec(rho).
    return np.kron(u.conj(), u)


def require(condition, message):
    """Keep scientific checks active under Python optimization."""
    if not condition:
        raise ValidationError(message)


class ValidationError(RuntimeError):
    """A required finite scientific comparison failed."""


def run(output_path):
    states = {
        "zero": np.diag([1, 0]).astype(complex),
        "plus": np.ones((2, 2), dtype=complex) / 2,
        "mixed": I / 2,
        "generic": np.array([[0.7, 0.1 + 0.2j], [0.1 - 0.2j, 0.3]]),
    }
    cases = [(0.0, 0.4), (0.2, 0.03), (1.0, 1.0), (3.0, 0.4),
             (12.0, 0.9), (30.0, 1 / np.sqrt(30))]
    rows = []
    max_pgf = max_counts = max_coherent = max_series = 0.0
    for t, theta in cases:
        c, s = np.cos(theta), np.sin(theta)
        rp, rm = c * Z + s * X, c * Z - s * X
        lb, ld = (rp + rm) / 2, (rp - rm) / 2
        transform_error = max(np.linalg.norm(lb - c * Z), np.linalg.norm(ld - s * X))
        reflection_error = max(np.linalg.norm(rp @ rp - I), np.linalg.norm(rm @ rm - I))
        mu = t * s * s
        # Resolve the count master equation into 0,...,nmax photons. Probability
        # in each retained block is exact up to floating-point arithmetic;
        # truncation of higher blocks never feeds back into lower blocks.
        nmax = int(max(8, poisson.ppf(1 - 1e-13, mu)))
        k0, jump = ad(lb) - np.eye(4), ad(ld)
        master = np.kron(np.eye(nmax + 1), k0)
        master += np.kron(np.diag(np.ones(nmax), -1), jump)
        evolved = expm(t * master)
        case = {"t": t, "theta": theta, "dark_mean": float(mu),
                "count_cutoff": nmax, "states": {},
                "transform_error": float(transform_error),
                "reflection_error": float(reflection_error)}
        for name, rho in states.items():
            vec = rho.reshape(-1, order="F")
            start = np.zeros(4 * (nmax + 1), dtype=complex)
            start[:4] = vec
            block_out = (evolved @ start).reshape((nmax + 1, 4))
            probs = np.real(block_out[:, 0] + block_out[:, 3])
            exact = poisson.pmf(np.arange(nmax + 1), mu)
            count_error = float(np.max(np.abs(probs - exact)))
            pgf_errors = []
            for z in [0, 0.25, 0.7, 1, 1.2, np.exp(0.8j)]:
                tilted = ad(lb) + z * ad(ld) - np.eye(4)
                out = expm(t * tilted) @ vec
                pgf_errors.append(abs(out[0] + out[3] - np.exp(mu * (z - 1))))
            pgf_error = float(max(pgf_errors))
            max_pgf, max_counts = max(max_pgf, pgf_error), max(max_counts, count_error)
            case["states"][name] = {"max_pgf_error": pgf_error,
                                     "max_count_probability_error": count_error,
                                     "dark_nonvacuum_probability": float(1 - probs[0])}
        # Independent finite Poisson word-average series for the coherent test.
        # Averaging every N-letter word produces A^N, A=(R_++R_-)/2.
        avg = (rp + rm) / 2
        k = expm(t * (avg - I))
        cutoff = int(max(8, poisson.ppf(1 - 1e-14, t)))
        term = np.exp(-t) * I
        series = term.copy()
        for n in range(1, cutoff + 1):
            term = (t / n) * avg @ term
            series += term
        series_error = float(np.linalg.norm(series - k))
        coherent_p = float(np.vdot(k[:, 0], k[:, 0]).real)
        coherent_exact = float(np.exp(-2 * t * (1 - c)))
        coherent_error = abs(coherent_p - coherent_exact)
        max_series, max_coherent = max(max_series, series_error), max(max_coherent, coherent_error)
        case.update({"coherent_probability": coherent_p,
                     "coherent_formula_error": coherent_error,
                     "poisson_word_average_series_error": series_error,
                     "word_series_cutoff": cutoff})
        rows.append(case)

    # Explicit untouched-reference diagnostic: Bell input, jumps on system only.
    bell = np.array([1, 0, 0, 1], complex) / np.sqrt(2)
    rho_bell = np.outer(bell, bell.conj())
    t, theta = 3.0, 0.4
    lb, ld = np.cos(theta) * np.kron(Z, I), np.sin(theta) * np.kron(X, I)
    ref_error = 0.0
    for z in [0, 0.7, np.exp(0.8j)]:
        tilted = ad(lb) + z * ad(ld) - np.eye(16)
        out = (expm(t * tilted) @ rho_bell.reshape(-1, order="F")).reshape((4, 4), order="F")
        ref_error = max(ref_error, abs(np.trace(out) - np.exp(t * np.sin(theta)**2 * (z - 1))))

    summary = {"max_transform_error": max(row["transform_error"] for row in rows),
               "max_reflection_error": max(row["reflection_error"] for row in rows),
               "max_pgf_error": max_pgf,
               "max_count_probability_error": max_counts,
               "max_coherent_formula_error": max_coherent,
               "max_word_average_series_error": max_series,
               "bell_reference_pgf_error": float(ref_error)}
    require(all(np.isfinite(x) and x < 1e-11 for x in summary.values()),
            "Two-reflection finite diagnostic exceeded the 1e-11 tolerance")
    report = {"purpose": "finite numerical diagnostics, not asymptotic proof",
              "python": platform.python_version(), "numpy": np.__version__,
              "scipy": scipy.__version__, "status": "passed",
              "tolerance": 1e-11,
              "summary": summary, "cases": rows}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": "passed", "summary": summary,
                      "results": str(output_path)}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("reflection_pair_results.json"))
    args = parser.parse_args()
    run(args.output)


if __name__ == "__main__":
    main()
