# Resource accounting and output encodings

The query results concern phase-referenced controlled unitary oracles, zero Hamiltonian, and digital representations of the specified vacuum output field. The error is half diamond distance unless the output is explicitly a classical bit. These conditions are fixed in [model.md](model.md).

## Compiled count-state preparation without QRAM

For the centered single-jump algorithm, let $`W=b-a`$, where $`[a,b]`$ is the retained Poisson window. Prepare

```math
|\chi_A\rangle
=\sum_{k=0}^{W}
\sqrt{\frac{p_\mu(a+k)}{P_A}}\,|k\rangle.
\qquad\text{(R1)}
```

There are $`W+1`$ explicitly known amplitudes. Pad this vector to the next power of two and use a binary tree of conditional rotations, or a uniformly controlled-rotation state-preparation circuit [MVBS05, SBM06]. The number of elementary rotations and CNOT gates is $`O(W+1)`$. This is an explicit circuit compiled from a classical list, not an amplitude-loading oracle.

The list can be computed stably without evaluating $`e^{-\mu}`$ or $`\mu^n/n!`$ separately. Start at the mode $`n_*=\lfloor\mu\rfloor`$, which lies in the retained window, assign relative weight one, and recurse outward:

```math
\frac{w_{n+1}}{w_n}=\frac{\mu}{n+1},
\qquad
\frac{w_{n-1}}{w_n}=\frac{n}{\mu}.
\qquad\text{(R2)}
```

Each outward multiplier is at most one. Normalize by the sum of the computed weights. Finite arithmetic errors therefore do not undergo exponential amplification in this recurrence. To make the input-precision cost explicit, let $`B_\mu`$ be the bit length of the supplied mean and take arithmetic precision $`P=O(B_\mu+\log(\mu+W+2)+\log((W+1)/\eta))`$. The weights and rotation data can be computed with $`O((W+1)\mathrm{poly}(P))`$ classical bit operations and $`O((W+1)P)`$ bits of working storage. These conservative bounds follow by propagating the absolute roundoff error through $`W`$ contractive recurrence steps and allocating an $`\ell_1`$ probability error of order $`\eta^2`$. When the classical input has polylogarithmic description length, this is $`W`$ times polylogarithmic overhead.

The normalization and tree-rotation angles are computed classically. A list of $`O(W)`$ angles, each to $`O(\log(W/\eta))`$ useful output bits plus arithmetic guard bits, is stored explicitly. It can be compiled into a sequence of gates. Choosing the operator-norm synthesis error of each of the $`O(W)`$ rotations to be $`O(\eta/(W+1))`$ keeps the total preparation error $`O(\eta)`$. A fixed inverse-closed universal gate set admits polylogarithmic single-qubit synthesis overhead by the Solovay–Kitaev construction [DN05]. A chosen gate set may allow sharper synthesis bounds; these are not needed here.

To output an absolute photon count, prepare $`k`$, append zero high bits as needed, and add the known integer $`a`$. This avoids preparing an arbitrary vector of length $`b+1`$. Alternatively, the register may remain a shifted count with $`a`$ included as classical metadata in its declared embedding. Both codes are independent of the unknown unitary.

## Centered circuit costs

Use the absolute-count version for a simple upper bound. Put
$`\ell=\lceil\log_2(b+1)\rceil`$, with a one-dimensional register when $`b=0`$. The $`W`$ oracle calls are controlled by comparisons with known thresholds $`a+1,\ldots,a+W`$. A reversible comparator and its uncomputation use $`O(\ell)`$ known gates and $`O(\ell)`$ reusable workspace.

With truncation error and preparation error allocated as in [centered_environment.md](centered_environment.md), the resource bounds are

```math
\begin{aligned}
\text{forward queries}&=W,\\
\text{known gates}&=
O\!\left(
W\,[\,\ell+\mathrm{polylog}(W/\epsilon)\,]
+\mathrm{poly}(\ell)
\right),\\
\text{quantum workspace beyond }S&=O(\ell+\log(W+1)),\\
\text{compiled angle/circuit storage}&=
O\!\left((W+1)\mathrm{polylog}((\mu+W+1)/\epsilon)\right)
\text{ bits}.
\end{aligned}
\qquad\text{(R3)}
```

The cost of implementing the unknown oracle itself is excluded from “known gates” and counted through its $`W`$ uses. The classical description of the compiled circuit is included in the storage accounting; the preceding $`P`$-dependent bound also charges the classical arithmetic workspace. For fixed accuracy and large $`\mu`$, these bounds give $`O(\sqrt{\mu})`$ queries and $`\widetilde O(\sqrt{\mu})`$ other work when the known parameters have polylogarithmic description length. No gate-optimality claim is needed.

For commuting fields, prepare the count registers independently, allocate their preparation errors to sum to at most $`\epsilon/2`$, and add the corresponding bounds. The query count is $`\sum_j W_j`$, the count storage is $`\sum_j O(\log(b_j+1))`$ qubits, and the compiled classical lists have total length $`\sum_j(W_j+1)`$. Rates equal to zero contribute only vacuum.

## General exact word code

For arbitrary unitary jumps, use the exact global count-and-word encoding from (M8)–(M9). Let $`\mu=\Lambda t`$, and choose $`N_{\max}`$ so that
$`\delta=\Pr(\mathrm{Pois}(\mu)\gt N_{\max})\leq\epsilon^2/4`$.
Prepare the normalized truncated coherent count and, conditioned on it, $`N`$ independent coherent labels with amplitudes $`\sqrt{\lambda_j/\Lambda}`$. Padded slots are put in a distinct inactive symbol. Then apply the corresponding chronological jump product and discard the system.

The ideal truncated isometry has overlap $`\sqrt{1-\delta}`$ with the exact isometry for every reference-assisted input. It therefore has half diamond error at most $`\sqrt{\delta}`$. Preparation and synthesis can use the remaining error budget. A choice

```math
N_{\max}
=\left\lceil
\mu+\sqrt{2\mu\log(4/\epsilon^2)}
+2\log(4/\epsilon^2)
\right\rceil
=O(\mu+\log(1/\epsilon)+1)
\qquad\text{(R4)}
```

suffices.

If a phase-referenced coherent SELECT oracle over the $`m`$ jumps is supplied, this uses $`N_{\max}`$ controlled SELECT calls. If only individual controlled $`U_j`$ oracles are supplied, a direct implementation uses at most $`mN_{\max}`$ individual calls. It is not legitimate to count SELECT as one call without declaring it. For the observer construction there is only one unknown unitary and a known Pauli $`Z`$, so each occupied slot uses at most one unknown-unitary query. Its full encoded field therefore has an $`O(t+\log(1/\epsilon)+1)`$ query upper bound.

A straightforward padded word register uses
$`O(N_{\max}\log(m+1)+\log(N_{\max}+1))`$ qubits.
With a compiled $`m`$-amplitude label state, one may charge $`O(m)`$ rotations per occupied-or-inactive slot. Count preparation, label preparation, occupancy control, and gate synthesis then have cost
$`O(N_{\max}\mathrm{poly}(m,\log(N_{\max}/\epsilon)))`$ known gates and comparable explicit classical compilation cost. This loose bound is sufficient for fixed $`m`$; it does not claim an optimal dependence on $`m`$.

No ordered-time discretization is hidden in this construction. The full field is represented through the fixed exact isometry $`J_t`$. Performing $`J_t`$ on a physical optical device is a separate task with separate resources.

The coherent truncated Poisson count and chronological word preparation are already explicit in [SAS26, Appendix B.1, Eqs. (51)–(53)], where the auxiliary registers are discarded to obtain the reduced dynamics. Here the retained word register is identified with the specified vacuum field through (M8). The linear construction here serves as a baseline with a declared coherent field encoding; retaining its word register does not introduce a new reduced-dynamics simulation primitive.

## The observer event is efficiently measurable in the word code

The nonfactorization of $`J_t`$ prevents a bath partial trace from being implemented by deleting word symbols. It does not prevent every local field observable from having an efficient representation.

For the uniform one-observer-photon event, the exact effect in the sector with $`n`$ main photons is

```math
E_n=|u_n\rangle\langle u_n|
+\frac{I-|u_n\rangle\langle u_n|}{n+2}.
\qquad\text{(R5)}
```

Its derivation and circuit are in [noncommuting_observer.md](noncommuting_observer.md). A count of observer labels, an encoding of the unique observer's position, a uniform-position projection, and a known coin implement it with polynomially many known gates in the word length and its bit precision. No physical bath decoder is invoked.

The dedicated one-bit algorithm avoids the full word register altogether. It samples the main count from $`\mathrm{Pois}(t)`$ conditioned on $`n\leq n_{\max}`$ and uses a coherent position register of dimension $`n+1`$. The normalized count weights are generated by the mode-based recurrence (R2), rounded to a finite dyadic law, and sampled classically. With $`b=O(\log((n_{\max}+1)/\eta))`$ fractional bits plus input and arithmetic guard bits, the conservative accumulated weight error $`O((n_{\max}+1)^2 2^{-b})`$ can be made smaller than any specified sampling allowance $`\eta`$. The table has $`O(n_{\max}b)`$ classical storage, with guard-bit costs charged as above.

After sampling $`n`$, compile only its $`O(n+1)`$-rotation uniform-position loader and inverse. The algorithm needs exactly $`n`$ unknown-unitary queries, $`O((n+1)\mathrm{polylog}((n+2)/\epsilon))`$ known gates, and $`O(\log(n+2))`$ ancillary qubits. It does not compile or coherently access a bank of loaders for every possible $`n`$. A Poisson cutoff gives a worst-case query bound $`O(t+\log(1/\epsilon)+1)`$. The retained-count and omitted-count channels form a convex mixture, so conditioning changes the full bit/reference channel by at most $`e^{-1}\Pr(\mathrm{Pois}(t)\gt n_{\max})`$ in half diamond distance.

These statements concern sampling one bit with the correct probability. They do not claim to prepare the complete reduced observer field in a logarithmic-size register.

## Precision of a known Poisson mean

The primary input model uses exactly specified finite-description means. If a mean is rounded, its effect can also be bounded directly. Compare $`V_\mu`$ and $`V_\nu`$ in the same declared count code, with the same oracle $`U`$ and the same physical temporal-mode embedding. Then

```math
V_\mu^\dagger V_\nu
=\sum_n\sqrt{p_\mu(n)p_\nu(n)}\,I
=\exp\!\left[-\frac{(\sqrt\mu-\sqrt\nu)^2}{2}\right]I.
\qquad\text{(R6)}
```

The purified-output overlap therefore gives

```math
d_\diamond(\Gamma_\mu,\Gamma_\nu)
\leq\sqrt{1-e^{-(\sqrt\mu-\sqrt\nu)^2}}
\leq|\sqrt\mu-\sqrt\nu|
\leq\sqrt{|\mu-\nu|}.
\qquad\text{(R7)}
```

Absolute mean error at most $`\eta^2`$ consequently suffices for error allowance $`\eta`$. For commuting fields, the squared square-root differences add in the exponent, so total absolute mean error $`\sum_j|\mu_j-\nu_j|\leq\eta^2`$ is sufficient.

For the one-bit sampler, Poisson coupling gives total variation distance at most $`1-e^{-|t-\nu|}\leq|t-\nu|`$ between the exact and rounded main-count laws. This bounds the resulting mixture of count-sector channels by the same amount in half diamond distance, before its observer-one weight is applied. The cutoff error is then charged separately for the rounded distribution. Thus an absolute mean allowance of order $`\eta`$ suffices there. These are bounds on arithmetic mean approximation at a fixed declared output encoding. They do not compare distinct physical temporal-mode functions arising from different time intervals.

## Resource boundaries

The count code, the global word code, and a product code across physical baths are distinct representations. Query complexity is unchanged by a known encoding conversion when its nonquery cost is left unrestricted. Gate counts and output-qubit counts can change substantially. Every stated gate bound is attached to a specified representation.

The centered algorithm uses the freedom to discard the system. It need not preserve the final system state or its correlations with the field. A joint system-field simulation is a different target and does not inherit the centering identity.

The bath state contains coherences that are absent from a classical trajectory sample. Sampling the Poisson count or the jump record alone does not implement the field channel. Conversely, the one-bit sampler can discard count coherence because its particular measurement is block diagonal in those counts; it keeps the position coherence that the measurement tests.

The microscopic coupling has no separately specified nonzero Hamiltonian. Coherent drift can nevertheless be contained in the unitary jump term, as explained in [interpretation.md](interpretation.md). Time-dependent unknown rates, nonunitary jumps, supplied power oracles, and oracle-dependent encodings are not part of these bounds.

## References

- **[MVBS05]** M. Möttönen, J. J. Vartiainen, V. Bergholm, and M. M. Salomaa, “Transformation of quantum states using uniformly controlled rotations,” *Quantum Information and Computation* **5**, 467–473 (2005). [arXiv:quant-ph/0407010](https://arxiv.org/abs/quant-ph/0407010). This supplies explicit finite-vector state-preparation circuits with a number of elementary rotations and CNOT gates linear in the vector dimension.
- **[SBM06]** V. V. Shende, S. S. Bullock, and I. L. Markov, “Synthesis of Quantum Logic Circuits,” *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems* **25**, 1000–1010 (2006). [DOI](https://doi.org/10.1109/TCAD.2005.855930), [arXiv:quant-ph/0406176v5](https://arxiv.org/abs/quant-ph/0406176v5).
- **[DN05]** C. M. Dawson and M. A. Nielsen, “The Solovay–Kitaev algorithm,” [arXiv:quant-ph/0505030v2](https://arxiv.org/abs/quant-ph/0505030v2) (2005). This is used only for explicit polynomial-in-log-precision compilation overhead.
- **[SAS26]** Z.-X. Shang, D. An, and C. Shao, “Exponential Lindbladian fast forwarding and exponential amplification of certain Gibbs state properties,” *Reports on Progress in Physics* (2026). [DOI](https://doi.org/10.1088/1361-6633/ae6df7), [arXiv:2509.09517v2](https://arxiv.org/abs/2509.09517v2), Theorem 1. The relevant comparison is its additive query cost for reduced dynamics with unitary jumps; its structured parallel-depth results concern a different resource.
