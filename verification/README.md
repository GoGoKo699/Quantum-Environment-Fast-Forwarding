# Verification and reproduction

The analytical claims are proved in [the scientific account](../science/model.md). This suite checks their normalization, time ordering, channel representation and operational measurement formulas through independently constructed finite objects. It also includes negative controls for assumptions that cannot be removed.

## Run the checks

Use Python 3.12 from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/audit_environment.py --output verification/audit_results.json
```

The [script](audit_environment.py) performs no network access. Its random seed is fixed to `20261031`. The [recorded output](audit_results.json) was generated with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0, as recorded in the JSON. Dependencies are pinned in [requirements.txt](requirements.txt).

Every required comparison uses an explicit check that raises `ValidationError` on failure. The checks remain active with `python -O`. A successful run exits with status zero and writes a result with `status: "passed"` and `checks_performed: 112`. Results are written only after the checks succeed. A failing run exits nonzero and does not replace an existing result file, so use a fresh output path when retaining multiple runs.

Exact rational equalities have no numerical tolerance. Floating-point checks use the explicit tolerances in the script. Library versions are descriptive metadata; runs on different platforms need not agree byte for byte. The pass criterion is the set of mathematical comparisons, not identity with a historical JSON file.

## Independent constructions

| Check | Construction compared | Failure mode addressed |
|---|---|---|
| Finite collision witness | Entire qubit/two-bath amplitudes versus a separate recurrence that traces the main field | Wrong chronological order, normalization or cross-time coherence |
| Continuous limit | Successively finer mutually exclusive collision bins versus the continuous expression | Missing survival factors or an inconsistent simultaneous-event convention |
| Exact measurement pullback | Rational repeated integration of gap polynomials over ordered time simplices | Wrong factorials or observer-position matrix |
| Finite-bin measurement | Main-bin subsets and allowed observer-bin amplitudes enumerated directly | Treating a global word code as a product over physical baths |
| One-bit circuit | Sequential oracle calls with a coherently placed known insertion, tested on a maximally entangled input | Incorrect insertion order or loss of bit/reference correlations |
| Continuous probability | Numerical quadrature and a sum over independently evaluated word-sector circuits | Sign, cancellation or boundary errors in the closed formula |
| Centered output | Reduced field/reference Choi matrices before and after count centering | Checking only a product input or discarding the reference accidentally |
| Negative controls | Retain the system; subtract noncommuting powers; remove coherence; rephase a jump | Applying an identity beyond its actual assumptions |

## The measurement normalization

For $`n`$ main photons and one observer photon, the continuous calculation yields

```math
E_n=\frac{I+\mathbf J}{n+2},
```

where $`\mathbf J`$ is the all-ones matrix of dimension $`n+1`$. The suite independently integrates the gap moments exactly for $`n=0,\ldots,7`$. It also constructs finite-bin field projections directly, obtaining

```math
E_{n,K}
=\frac{(K+1)I+(K-n-1)\mathbf J}{K(n+2)}.
```

The uniform-position eigenvalue is $`1-n/K`$; every orthogonal eigenvalue is $`(1+1/K)/(n+2)`$. The matrices approach $`E_n`$ as the bin count grows. These checks test the physical field projection independently of the compact matrix formula. The complete derivation and the direct sampling circuit are in [the observer account](../science/noncommuting_observer.md).

## Recorded results

The full finite collision states and the independent recurrence agree within $`5.6\times10^{-17}`$ in the tested cases. Eight simplex sectors and seven finite-bin projections agree exactly in rational arithmetic. The word-sector sampler and continuous probability differ by at most $`1.1\times10^{-15}`$ in their checked cases. The largest centered Choi-matrix discrepancy is below $`4\times10^{-14}`$.

The evaluated uniform event-gap bound is $`0.290692619438537`$. At approximation error $`0.1`$ per oracle instance, the corresponding conservative query lower bound is

```math
q\geq0.018378167098273324\,t.
```

This coefficient evaluates an analytical inequality; it is not a fit to numerical data. The actual checked event gaps range from about $`0.3093`$ at $`t=2\pi`$ toward $`e^{-1}`$ at larger horizons.

The negative controls produce substantial discrepancies when a required condition is removed. In two nontrivially centered examples, retaining the system changes the joint state by trace distance about $`0.960`$ and $`0.811`$. Subtracting powers of two noncommuting jumps changes the field/reference output by about $`0.668`$. Rephasing a jump leaves its reduced-system channel unchanged to numerical precision while changing the specified coherent field output by about $`0.847`$ on the checked eigenstate.

## Validation boundary

The finite cases test formulas and their physical representations. The reference-uniform error bounds, arbitrary-input claims, asymptotic query lower bounds and concentration estimates rest on the written proofs. A normalized Choi-matrix comparison is not itself a numerical computation of diamond distance. This suite does not assess external priority, physical field-generation hardware, or the cost of an arbitrary decoder.

The auxiliary computation for the direct one-bit sampler is charged explicitly in [resources.md](../science/resources.md). Its count is sampled classically before the position circuit is compiled. Only the circuit for the sampled count is needed; no library of every possible count-dependent circuit is assumed.
