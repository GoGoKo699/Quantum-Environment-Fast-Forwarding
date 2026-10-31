# Quantum Environment Fast Forwarding

**How does the cost of simulating open-system dynamics change when the requested output is the emitted quantum field?** For a specified vacuum dilation with unitary jumps, discarding the system permits a square-root query cost for one jump. A known noncommuting observer with only one emitted photon on average can restore a linear requirement, even when the requested output is a single measurement bit.

The access model supplies phase-referenced controlled unitary oracles, known jump rates, and a known horizon. The Hamiltonian parameter of the dilation is zero. The error is half diamond distance, so the field simulation preserves correlations with any untouched input reference. Digital field encodings and their known-gate costs are stated explicitly.

## Principal results

At a fixed error of $`0.1`$, the worst-case query costs have the following time dependence. The single unknown jump has unit rate, and the first three rows concern the same single-jump dynamics.

| Requested output | Query cost | Reason and scope |
|---|---:|---|
| Classical jump record at a chosen time resolution | $`0`$ | The counting law is Poisson and independent of the unitary. Producing the record still has a classical cost. |
| Complete coherent single-jump field, with the system discarded | $`\Theta(\sqrt t)`$ | A common power can be removed from a concentrated count window; a qubit phase family gives the lower bound. |
| Reduced system | $`\Theta(t)`$ | Established system-simulation scaling; an exact-model comparison is given in the interpretation page. |
| Complete two-field output after adding the known jump $`Z/\sqrt t`$ | $`\Theta(t)`$ | A one-photon observer-mode measurement gives the lower bound; the chronological-word construction gives the upper bound. |
| Only the bit from that observer-mode measurement | $`\Theta(t)`$ | An explicit insertion-position circuit matches the lower bound, without a field decoder. |

### Centering the count

For one jump $`L=\sqrt\lambda U`$, put $`\mu=\lambda t`$. The exact dilation is

```math
V_\mu|\psi\rangle
=\sum_{n=0}^{\infty}\sqrt{e^{-\mu}\mu^n/n!}\,
U^n|\psi\rangle\otimes|n\rangle_f.
```

After restricting the Poisson count to a window $`[a,b]`$, replace $`U^n`$ by $`U^{n-a}`$. The removed common factor acts only on the system that is discarded. This leaves the field-reference state unchanged within the window. An omitted probability $`\delta`$ contributes at most $`\sqrt\delta`$ to half diamond error. For $`0<\epsilon\leq1/2`$, the resulting forward-query bound is

```math
q=O\!\left(
\sqrt{\mu\log(1/\epsilon)}+\log(1/\epsilon)+1
\right).
```

The count amplitudes are computed and compiled from an explicit classical list. There is no QRAM or free state-loading oracle. For pairwise commuting jumps, the same argument applies to independent count registers and gives a sum of concentration-window widths. The fixed-error time exponent is optimal for one jump; no matching precision law or direct-sum optimality in the number of jumps is claimed.

### A mean-one-photon obstruction

Take a qubit initially in $`|0\rangle`$, with

```math
L_1=e^{-i\theta X},\qquad L_2=Z/\sqrt t,\qquad t\geq2\pi.
```

The second field has mean photon number one. Its probability of exactly one photon in the uniform temporal mode, with all orthogonal modes in vacuum, is

```math
p_\theta(t)
=e^{-1}\,2\operatorname{Re}\frac{e^z-1-z}{z^2},
\qquad z=t(e^{2i\theta}-1),
```

with the continuous value $`p_0(t)=e^{-1}`$. Choosing $`\theta=\tfrac12\arcsin(2\pi/t)`$ gives an event-probability gap of at least $`0.2906926194`$ from $`\theta=0`$, while the oracle distance is $`O(1/t)`$. A query hybrid therefore forces $`\Omega(t)`$ calls. The witness is bounded and preserves photon number: it detects temporal coherence within the one-photon sector.

The exact measurement also has a finite circuit. Conditional on $`n`$ main photons and one observer photon, its effect on the observer's insertion position is $`(I+\mathbf J)/(n+2)`$, where $`\mathbf J`$ is the all-ones matrix. Sampling the count and coherently inserting the known $`Z`$ among $`n`$ forward calls yields the matching upper bound for the bit itself.

## Read the science

Start with the [model and output contract](science/model.md), then follow [count centering](science/centered_environment.md) and the [noncommuting observer](science/noncommuting_observer.md). The [resource account](science/resources.md) specifies preparation, storage and encoding costs. The [interpretation](science/interpretation.md) connects the results and the reduced-system benchmark.

| To inspect | Authoritative account |
|---|---|
| Fixed dilation, oracle phases, reference systems and exact word code | [Model](science/model.md) |
| Uniform truncation proof, commuting extension and square-root lower bound | [Centered environment](science/centered_environment.md) |
| One-photon kernel, constant gap, linear lower bound and direct sampler | [Noncommuting observer](science/noncommuting_observer.md) |
| Known gates, classical compilation, storage and SELECT access | [Resources](science/resources.md) |
| Physical meaning, measured records and the system-output comparison | [Interpretation](science/interpretation.md) |
| Inherited ingredients and closest prior results | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Independent finite checks and their limits | [Verification](verification/README.md) |

The square-root scale, phase estimation, and typical-window compression have close precedents. The [comparison](references/RELATED_WORK.md) credits those ingredients and distinguishes them from the specified forward-oracle channel construction and its noncommuting observer boundary.

## Reproduce the checks

Use Python 3.12 and the pinned numerical dependencies:

```bash
python -m pip install -r verification/requirements.txt
python verification/audit_environment.py --output verification/audit_results.json
```

The suite compares full collision states with a separate recurrence, exact simplex integrals with finite-bin projections, the direct measurement circuit with its reference-preserving channel, and the centered field with its uncentered Choi matrix. Negative controls exercise the assumptions that make the proofs work. These finite checks supplement the analytical arguments; they do not prove the asymptotic bounds.

## Scope

The field target is fixed by its microscopic vacuum dilation, including coupling phases. A reduced Lindblad generator alone is insufficient to specify it. The observer's rate is $`1/t`$, so the lower-bound family changes with the requested horizon. The result is an existence boundary for noncommuting jumps, not a classification of every noncommuting model.

The global chronological-word code generally does not factor into separate bath registers. Deleting labels is not a physical bath trace. The one-bit algorithm implements its specific measurement directly. Encoded simulation also does not reduce the energy or elapsed time needed to emit a physical field; physical production and arbitrary decoding have separate costs.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
