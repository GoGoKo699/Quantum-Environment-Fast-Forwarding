# A three-reflection field-only parity lower bound

The [reflection theorem](reflection_threshold.md) needs a separate field-only converse for three primitives. The [sister's original tree construction](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/549582272ce6f5a3274be12de1bc5b2f16ed290e/science/lower-bounds.md#5-three-reflections-a-finite-tree-parity-reduction) supplies its tree, radial drift estimate and two-query controlled-SELECT compiler. Its root-input field is nevertheless exactly independent of the unknown bits. The known leaf action below makes the coherent field retain the full parity without adding a fourth reflection or a variable observer rate.

## Fixed output and oracle model

Use the vacuum Hudson–Parthasarathy dilation with identity scattering, explicit Hamiltonian zero, and three separate labelled fields coupled by

```math
L_j=R_j/\sqrt3,\qquad j=1,2,3.
```

All rates are fixed at 1/3. Each supplied matrix is exactly a Hermitian involution with its stated phase. A phase-referenced controlled SELECT of the three reflections, including its inverse, costs one query. We require simulation of the full field channel after discarding the final system, on arbitrary inputs and references, to half diamond error at most 0.1. No unknown-oracle-dependent output embedding is permitted.

The physical embedding is the exact [chronological-word code](model.md#exact-trajectory-expansion). With $`w=(j_1,\ldots,j_N)`$ and normalized uniform ordered-time state $`|N,w\rangle_F`$,

```math
\begin{aligned}
c_{N,w}&=\sqrt{e^{-t}t^N/(N!3^N)},\\
V_t|\psi\rangle
&=\sum_{N,w}c_{N,w}
 R_{j_N}\cdots R_{j_1}|\psi\rangle\otimes|N,w\rangle_F.
\end{aligned}
```

The code states are orthonormal and their physical-field embedding is independent of the unknown bits below.

## Why the original system witness fails for the field

In the source's original tree construction, all missing boundary edges are identity loops. Starting at root with answer zero, every trajectory ends at a vertex $`v`$ with answer equal to the unknown prefix parity at its depth. Hence two trajectories have nonzero final-system overlap exactly when their known endpoints agree. All unknown answer bits disappear from these overlaps. The complete coherent field is exactly independent of the unknown string for this input. Explicitly, on a tree of radius at least the parity depth, let $`p_x(d)=x_1\oplus\cdots\oplus x_d`$ with $`p_x(0)=0`$, and define $`D_x|v,a\rangle=|v,a\oplus p_x(\min\{|v|,m\})\rangle`$. It fixes the root input, and the original identity-loop reflections satisfy

```math
\begin{aligned}
R_j^{(x)}&=D_xR_j^{(0)}D_x,\\
V_x|\varnothing,0\rangle
&=(D_x\otimes I_F)V_0|\varnothing,0\rangle .
\end{aligned}
```

The system factor disappears under the partial trace. The system parity lower bound therefore cannot simply be reused after discarding the system.

## Repair: known Z loops at the parity boundary

For $`t\geq48`$, set

```math
m=\lfloor t/48\rfloor\ge1.
```

Let the vertex set contain the empty word and all words of length at most $`m`$ on $`\{1,2,3\}`$ with unequal adjacent letters. A colour $`j`$ deletes the last letter if it is $`j`$, appends $`j`$ if this is possible below depth $`m`$, and otherwise is a self-loop at a leaf. Call the resulting known involution $`T_j`$.

Let unknown input bits be $`x_1,\ldots,x_m`$, and let an answer qubit be attached to the vertex register. For a nonloop edge with upper depth $`\ell`$, define

```math
R_j^{(x)}|v,a\rangle=|T_jv,a\mathbin\oplus x_\ell\rangle.
```

On a missing boundary edge, define instead

```math
R_j^{(x)}|v,a\rangle=(-1)^a|v,a\rangle.
```

Thus the boundary loop acts by the known $`Z`$ on the answer, not by the identity. Edge bits are symmetric between endpoints, and each loop acts by an involution, so every $`R_j^{(x)}`$ is exactly Hermitian and unitary. There are still exactly three supplied reflection types and no rate, coupling phase, or Hamiltonian depends on the requested time except through the allowed growing finite target instance.

The system dimension is

```math
d=2(3\cdot2^m-2)=6\cdot2^m-4=\exp(\Theta(t)).
```

This is not a fixed-dimension lower bound.

## Gauge reduction: the field depends only on the full parity

Define $`p_x(d)=x_1\oplus\cdots\oplus x_d`$, $`p_x(0)=0`$, and

```math
G_x|v,a\rangle=|v,a\mathbin\oplus p_x(|v|)\rangle,
\qquad P=p_x(m).
```

Conjugating all reflections by $`G_x`$ removes every nonloop bit flip. On a leaf loop it conjugates $`Z`$ to $`(-1)^P Z`$. The initial state $`|\varnothing,0\rangle`$ is fixed by $`G_x`$. After this conjugation the answer remains zero, the vertex moves by $`T_j`$, and each leaf self-loop contributes the scalar $`(-1)^P`$. The final $`G_x`$ is on the discarded system and has no effect on the field. Consequently all strings of the same parity produce exactly the same field state for this fixed known input.

For a word $`w`$, let $`v(w)`$ be its endpoint under the known vertex walk and $`K(w)`$ its number of leaf self-loop events. The isometry on this input is therefore

```math
V_P|\mathrm{root}\rangle
=\sum_{N,w}c_{N,w}(-1)^{P K(w)}|v(w)\rangle|N,w\rangle_F.
```

## Exact endpoint-fibre trace distance

For each vertex define unnormalized field vectors

```math
|F_v^P\rangle=\sum_{N,w:v(w)=v}c_{N,w}(-1)^{P K(w)}|N,w\rangle_F.
```

Different endpoint fibres are orthogonal field subspaces because they contain disjoint orthonormal word states. Put $`p_v=\|F_v^P\|^2`$, independent of $`P`$, and, for $`p_v\gt0`$, $`f_v^P=F_v^P/\sqrt{p_v}`$. The two field states are direct sums

```math
\rho_P=\bigoplus_v p_v|f_v^P\rangle\langle f_v^P|.
```

Their normalized fibre overlaps are

```math
\alpha_v=\langle f_v^0|f_v^1\rangle
=\mathbb E[(-1)^K\mid V_t=v].
```

Let $`L_t`$ be the total amount of time spent at leaves by the continuous-time vertex process. Each leaf has exactly two loop colours, with total rate $`2/3`$; its nonloop exit rate is $`1/3`$. Conditional on the vertex skeleton (which ignores loops), the loop count is Poisson of mean $`(2/3)L_t`$. This is the standard marked-Poisson/thinning construction, so

```math
\alpha_v=\mathbb E[e^{-(4/3)L_t}\mid V_t=v]\in[0,1].
```

It follows exactly that

```math
\begin{aligned}
D(\rho_0,\rho_1)
&=\tfrac12\|\rho_0-\rho_1\|_1
=\sum_vp_v\sqrt{1-\alpha_v^2}\\
&\ge 1-\mathbb E[e^{-(4/3)L_t}].
\end{aligned}
```

This is a field-only calculation; no final-system measurement or reconstruction is used.

## Uniform constant gap

Let $`\tau_m`$ be the first hitting time of a leaf. Up to that time, the depth walk agrees with the infinite three-coloured tree. Its depth at time $`s`$ stochastically dominates

```math
Y_s=\mathrm{Pois}(2s/3)-\mathrm{Pois}(s/3),
\quad \mathbb E Y_s=s/3,\quad\operatorname{Var}Y_s=s.
```

Taking $`s=t-1`$, using $`m\leq t/48`$, and applying Chebyshev,

```math
\begin{aligned}
\Pr(\tau_m\le t-1)
&\ge1-\frac{t-1}{((t-1)/3-m)^2}\\
&\ge1-\frac{2304(t-1)}{(15t-16)^2}
\ge\frac{1513}{1936}=:h_0.
\end{aligned}
```

The last rational function decreases for $`t\geq48`$ and has value $`423/1936`$ at $`t=48`$.

Following a hit by $`t-1`$, the first leaf dwell $`E`$ is exponential of rate $`1/3`$. At least $`\min(E,1)`$ units of leaf time occur before the horizon. The strong Markov property gives

```math
\mathbb E[e^{-(4/3)\min(E,1)}]
=\tfrac15+\tfrac45e^{-5/3}.
```

Consequently

```math
\boxed{\quad
D(\rho_0,\rho_1)
\ge\frac{1513}{1936}\frac45(1-e^{-5/3})
=0.5071203359\ldots>\frac12.
\quad}
```

The ideal equal-prior Helstrom measurement therefore distinguishes parity with success greater than 0.7535. It is a known field measurement, independent of the unknown bits. The two states are related by the known involution that multiplies word $`w`$ by $`(-1)^{K(w)}`$, so a symmetric Helstrom measurement may be chosen with equal individual success probabilities. Alternatively, uniform-average success alone suffices for the parity polynomial bound. Half diamond simulation error 0.1 reduces each event success probability by at most 0.1, leaving bounded-error parity success greater than 0.6535.

## Oracle reduction and linear lower bound

Exactly as in the source construction, a controlled SELECT call can be implemented with two ordinary bit-oracle calls. Reversibly compute the selected edge depth and an active flag for a controlled nonloop move, using address one on inactive branches. Query the addressed bit into a zero buffer, flip the answer conditional on the active flag and buffer, query again to erase the buffer, apply the known vertex move and the known controlled $`Z`$ on boundary-loop branches, and erase the known address/flag. The edge condition and depth are symmetric at its two endpoints. Unused binary labels are fixed and inactive. This implements the complete controlled SELECT exactly, including arbitrary coherent controls and inverse queries, without assuming a free controlled bit oracle or zero sentinel bit.

A $`q`$-query field simulator thus yields a bounded-error parity algorithm with at most $`2q`$ bit queries. Quantum parity requires at least $`m/2`$ bit queries, so

```math
q\ge m/4\ge t/384\qquad(t\ge48).
```

For $`1\leq t\lt48`$, use the one-reflection comparison from [the theorem](reflection_threshold.md#one-reflection-lower-bound), repeated in all three supplied labels: $`(Z,Z,Z)`$ versus $`(X,X,X)`$. A known passive bath mixing concentrates their coupling in one bright field. The half trace separation is $`\sqrt{1-e^{-4t}}/2\gt0.495`$, so a zero-query simulator cannot approximate both to error 0.1. Thus $`q\geq1\geq t/384`$ on this range as well. Together with the routine coherent trajectory upper bound, this proves the dimension-uniform three-reflection full-field order $`\Theta(t)`$ at fixed error.

The inherited parity bound is the polynomial-method result of [Beals–Buhrman–Cleve–Mosca–de Wolf](https://arxiv.org/abs/quant-ph/9802049). It applies to all coherent, adaptive and randomized algorithms under a branchwise query cap. The source's original tree/drift and oracle compilation are credited rather than claimed anew.

## An independent, simpler physical field measurement

An operational witness avoids an abstract exponentially large Helstrom decoder. Let the last interval have length $`\delta=1/2`$. Count photons in the earlier interval $`[0,t-\delta]`$, retaining the labels in chronological order. The known vertex graph computes its endpoint $`v`$; photon counts themselves are independent of $`x`$. The conditional system is a basis state with answer equal to the prefix parity at its depth. If $`v`$ is not a leaf, return an unbiased bit. If $`v`$ is a leaf, its answer is the full parity $`P`$.

For this leaf, let $`j,k`$ be its two missing colours. In the final interval define the normalized one-photon state

```math
|1_M\rangle=(|1_j\rangle+|1_k\rangle)/\sqrt2,
```

where each photon is in the uniform temporal mode of that interval and all other modes are vacuum. Measure the norm-one observable

```math
X_v=|\mathrm{vac}\rangle\langle1_M|+|1_M\rangle\langle\mathrm{vac}|.
```

Only the zero/one-photon sectors contribute, so its exact conditional expectation is

```math
\langle X_v\rangle_P=(-1)^P 2e^{-\delta}\sqrt{2\delta/3}
=(-1)^P\frac{2e^{-1/2}}{\sqrt3}.
```

The depth chain is reversible with stationary leaf probability

```math
\pi_m=\frac{3\cdot2^{m-1}}{3\cdot2^m-2}>\frac12.
```

By the spectral expansion of a reversible continuous-time chain, its diagonal transition probability $`P_{mm}(u)\geq\pi_m`$ for every $`u\geq0`$. Strong Markov at the first hit therefore implies

```math
\Pr(D_{t-\delta}=m)\ge\pi_m\Pr(\tau_m\le t-\delta)
\ge h_0/2.
```

The adaptive field observable, set to zero on nonleaf outcomes, has expectation $`(-1)^P A`$ with

```math
A\ge h_0 e^{-1/2}/\sqrt3=0.2736\ldots.
```

Its associated binary POVM $`(I+X)/2`$ identifies parity with success at least $`(1+A)/2\gt0.636`$, uniformly for every bit string. A simulator with half diamond error 0.1 still yields success greater than 0.536, enough for the same linear query lower bound.

This measurement uses vacuum/one-photon coherence, so it requires the stipulated phase reference. The exact endpoint-fibre proof also uses physical coherences between total photon-number sectors. A photon-count record alone remains oracle-independent and yields no parity information.

More precisely, a word ending at depth $`d`$ has $`N-K`$ nonloop steps and hence $`N-K\equiv d\pmod2`$. Within each endpoint fibre $`(-1)^K=(-1)^{N-d}`$. Therefore the two field states obey the exact identity

```math
\rho_1=e^{i\pi N_{\mathrm{total}}}\rho_0e^{-i\pi N_{\mathrm{total}}}.
```

They become identical if total photon number is dephased. This construction establishes the threshold for the specified phase-referenced coherent field; it establishes no such lower bound for a photon-number-superselected or phase-insensitive output. The physical phases of the supplied matrices are fixed by their explicit edge-XOR / boundary-Z definitions; the sign distinction is not an unspecified oracle phase or an oracle-dependent encoding.

## Field encoding and output work

The lower bound applies to the stated physical-field channel or to any declared oracle-independent digital encoding compared through an explicit isometric embedding. One cannot merely delete a bath label from the global word register to perform a physical trace.

The late-interval witness has an explicit known time-splitting map in the exact code. With $`s=t-\delta`$,

```math
\begin{aligned}
|N,w\rangle_t\longmapsto
\sum_{r=0}^N&
\sqrt{\binom Nr(s/t)^r(\delta/t)^{N-r}}\\
&{}\times |r,w_{1:r}\rangle_s
\otimes|N-r,w_{r+1:N}\rangle_\delta .
\end{aligned}
```

It follows by factoring the ordered-time simplexes. Thus measuring the early interval and implementing the late field POVM are explicit oracle-free operations; chronological labels and the boundary endpoint can be processed in $`O(N)`$ word operations. Finite truncation and finite precision add ordinary known-gate/compilation work, not unknown-reflection queries. The typical count is $`\Theta(t)`$. Producing, reading, or decoding this explicit trajectory output is therefore not a sublinear total-work claim. A physical field additionally requires its photons, energy, modes and elapsed emission time. None of this is supplied for free by the oracle lower or upper bounds.

## Validation scope

The companion [check_reflection_tree.py](../verification/check_reflection_tree.py) enumerates finite word sectors for small trees, computes full reduced field density matrices for every bit string, checks exact parity-only dependence and endpoint-fibre trace distance, and compares unsigned/signed endpoint weights against a separate radial Feynman–Kac matrix exponential (with an explicit Poisson-tail error). It also checks exact field blindness of the original identity-loop construction. These finite checks exercise the derivation; the asymptotic lower bound rests on the analytic arguments above.
