# Reflection primitives and the coherent-field threshold

The number of supplied reflection primitives controls the worst-case query cost of the specified coherent field. This is the field-output counterpart of [Quantum Dephasing Threshold](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold): the word-reduction upper bounds transfer coherently, but the lower bounds require measurements of the retained field.

This page owns the field theorem and its upper-bound/resource account. The [qubit pair witness](reflection_pair.md) and [three-reflection tree witness](reflection_tree.md) give the converse proofs. The sister repository owns the original reduced-system theorem, involution-word geometry and tree parity scaffold; its [source version](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/tree/549582272ce6f5a3274be12de1bc5b2f16ed290e) fixes those inherited ingredients.

## Fixed physical output and oracle contract

For $`k\in\{1,2,3\}`$ supplied Hermitian involutions, fix

```math
\begin{aligned}
R_j&=R_j^\dagger,\qquad R_j^2=I,\\
L_j&=\frac{R_j}{\sqrt{k}},\qquad
H=0,\qquad \lambda_j=\frac1k.
\end{aligned}
\qquad\text{(R1)}
```

The total jump rate is one. Time $`t`$ is physical time multiplied by that total rate. Use separate labelled bosonic fields, vacuum input, identity scattering and the Hudson–Parthasarathy convention in [model.md](model.md). The displayed matrices, including their signs, fix the jump phases; they are not supplied only modulo a global phase.

The target is the entire emitted field, after discarding the final system,

```math
\Gamma_{t,R}(\rho)=\mathrm{Tr}_S[V_{t,R}\rho V_{t,R}^\dagger].
\qquad\text{(R2)}
```

The input may be entangled with an untouched reference. Accuracy means [half diamond distance](model.md#oracle-and-accuracy-conventions).

The oracle is the phase-referenced coherent selection

```math
S_R=\sum_{j=1}^k|j\rangle\langle j|\otimes R_j.
\qquad\text{(R3)}
```

One call to SELECT, its inverse, or an externally controlled version costs one query. Unused binary labels act as identity. Since the supplied matrices are reflections, inverse SELECT equals SELECT. Algorithms may use arbitrary known operations, ancillas, randomness, measurements and adaptive control; the number of serial calls is bounded on every branch. No matrix description, power oracle or oracle-dependent encoding is supplied.

Fix the exact chronological-word physical embedding from (M8) of [the model](model.md#exact-trajectory-expansion):

```math
\begin{aligned}
J_t|N,w\rangle
&=\sqrt{\frac{N!}{t^N}}
 \int_{0\lt s_1\lt\cdots\lt s_N\lt t}
 |\mathbf s,w\rangle\,d^N\mathbf s,\\
V_{t,R}|\psi\rangle
&=\sum_{N=0}^{\infty}\sum_{w\in[k]^N}
 \sqrt{\frac{e^{-t}t^N}{N!k^N}}\,
 R_{w_N}\cdots R_{w_1}|\psi\rangle\otimes J_t|N,w\rangle .
\end{aligned}
\qquad\text{(R4)}
```

This embedding is independent of the unknown reflections. It includes every ordered emission time without a time grid and generally does not factor across baths. Deleting labels is not a physical bath trace.

## The field theorem

Let $`Q_k^F(t,\epsilon)`$ be the supremum, over finite target dimensions, of the least worst-case query cap for a simulator of (R2), uniformly over all legal tuples of that dimension. Tuples may include repeated reflections and identity. At $`\epsilon=0.1`$ and every real $`t\geq1`$,

```math
\boxed{
Q_1^F(t,0.1)=1,\qquad
Q_2^F(t,0.1)=\Theta(\sqrt t),\qquad
Q_3^F(t,0.1)=\Theta(t).
}
\qquad\text{(R5)}
```

The same time exponents hold for every smaller fixed positive error, with constants allowed to depend on it.

| Primitives | Coherent upper mechanism | Field-only converse |
|---|---|---|
| One | Count parity; at most one controlled reflection | Qubit even/odd coherence |
| Two | Coherently cancel words to a line endpoint | Qubit dark-port photon count |
| Three | Coherent Poisson trajectory preparation | Modified leaf-phase tree, dimension exponential in time |

This counts supplied oracle primitives, not an invariant Lindblad rank. The three-reflection converse uses dimension $`\exp(\Theta(t))`$ and gives no fixed-dimension long-time linear lower bound. No optimal joint time-and-precision law is claimed. The sister's reduced-system theorem uses unhalved diamond error $`0.01`$; (R5) uses the convention of this repository explicitly.

## Routine coherent word reduction

The cancellation $`R_jR_j=I`$ does not alter any field register. Let $`g=\mathrm{red}(w)`$ be the abstract reduced word and $`W_g`$ its represented operator. Grouping the orthonormal word states in (R4) gives

```math
\begin{aligned}
p_g(t)&=\sum_{\substack{N,w:\\\mathrm{red}(w)=g}}
       \frac{e^{-t}t^N}{N!k^N},\\
|\chi_g(t)\rangle
&=\frac1{\sqrt{p_g(t)}}
 \sum_{\substack{N,w:\\\mathrm{red}(w)=g}}
 \sqrt{\frac{e^{-t}t^N}{N!k^N}}\,J_t|N,w\rangle,\\
V_{t,R}
&=\sum_g\sqrt{p_g(t)}\,W_g\otimes|\chi_g(t)\rangle .
\end{aligned}
\qquad\text{(R6)}
```

Terms with zero weight are omitted. The $`\chi_g`$ are orthonormal and independent of the unknown matrices. The abstract grouping remains valid even when the actual tuple has additional relations.

Equation (R6) is a direct coherent version of the sister's [word cancellation identity](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/549582272ce6f5a3274be12de1bc5b2f16ed290e/science/pair-simulation.md), combined with known coherent Poisson preparation [SAS26, Appendix B.1, Eqs. (51)–(53)]. It is a routine upper-bound lift. Measuring or sampling $`g`$, or discarding reduction garbage, would generally remove coherences required by the field target.

For one reflection, $`g`$ is just even or odd parity. Its weights are

```math
p_{\rm e}=\frac{1+e^{-2t}}2,\qquad
p_{\rm o}=\frac{1-e^{-2t}}2.
\qquad\text{(R7)}
```

Prepare their known amplitudes and apply $`R`$ on the odd branch. This uses one controlled query, even for the joint isometry in the two-fibre encoding.

For two reflections $`A,B`$, the abstract Cayley graph is a line. Give its endpoint a signed integer coordinate $`s`$, with known maps

```math
T_A(s)=s+(-1)^s,\qquad
T_B(s)=s-(-1)^s.
\qquad\text{(R8)}
```

Uniform independent labels induce a symmetric continuous-time random walk on this line. Its law is $`p_s(t)=e^{-t}I_{|s|}(t)`$, and the reduced alternating word has length $`|s|`$. The inherited Bernstein tail estimate is

```math
\Pr\{|S_t|\geq\sqrt{2tu}+u\}\leq2e^{-u}.
\qquad\text{(R9)}
```

For a coherent restriction to $`|s|\lt M`$ with omitted probability $`\delta`$, normalizing the retained amplitudes gives an isometry whose overlap with the exact isometry is $`\sqrt{1-\delta}`$, uniformly on every reference-assisted input. The resulting half diamond error is at most $`\sqrt\delta`$. Taking $`u=\log(C/\epsilon^2)`$ for a sufficiently large absolute constant $`C`$ yields

```math
q=O\!\left(\sqrt{t\log(1/\epsilon)}+\log(1/\epsilon)\right).
\qquad\text{(R10)}
```

For three reflections, the general [coherent word construction](resources.md#general-exact-word-code) with a Poisson count cutoff gives $`O(t+\log(1/\epsilon))`$ queries.

## An explicit output implementation and its separate costs

The compressed fibre code in (R6) is legitimate because its embedding is known and oracle independent. That statement does not supply a cheap physical implementation of $`|g\rangle\mapsto|\chi_g(t)\rangle`$. A concrete simulator can instead retain the original count-and-word code throughout:

1. Prepare the normalized coherent Poisson count up to $`N_{\max}=O(t+\log(1/\epsilon))`$, with coherent labels in padded slots.
2. For a pair, reversibly compute $`s`$ from the word. Apply $`W_s`$ when $`|s|\lt M`$, and identity otherwise.
3. Uncompute $`s`$ from the retained word. Discard only the final system and clean auxiliary registers.

Every output word and its coherence are retained. Replacing words on a tail of probability $`\delta_s`$ by identity changes the joint output vector by at most $`2\sqrt{\delta_s}`$. Count truncation contributes at most $`\sqrt{\delta_N}`$ in half diamond distance. Choosing both probabilities of order $`\epsilon^2`$ and reserving a synthesis allowance proves (R10) in the original embedding.

At fixed $`k`$, conservative costs are:

| Resource | Explicit count-and-word implementation |
|---|---|
| Unknown serial queries | One for one reflection; (R10) for a pair; $`O(N_{\max})`$ for three |
| Output registers | $`O(N_{\max}\log(k+1)+\log(N_{\max}+1))`$ qubits |
| Pair endpoint arithmetic | $`O(N_{\max}\log(N_{\max}+1))`$ known reversible gates, including uncomputation |
| Preparation, synthesis and compilation | $`O(N_{\max}\mathrm{poly}(B,\log((N_{\max}+2)/\epsilon)))`$ known work, conservatively |

Here $`B`$ is the bit length of the known classical parameters. The preparation uses explicitly compiled Poisson lists and finite rotations, with the arithmetic and synthesis conventions of [resources.md](resources.md); no QRAM or free amplitude loader is assumed. Coherent occupancy and label controls are charged. These bounds are sufficient and are not claimed gate optimal.

Thus the square-root oracle bound coexists with roughly linear explicit output work at fixed error. The actual field has mean photon number $`t`$. Physical photon generation, emission time, energy and arbitrary decoding are separate resources.

## One-reflection lower bound

Use input $`|0\rangle`$ and compare the legal qubit reflections $`R=Z`$ and $`R=X`$. In the orthonormal even/odd fibre basis, the first output is pure with off-diagonal entry $`\sqrt{p_{\rm e}p_{\rm o}}`$. For $`R=X`$, even and odd trajectories end in orthogonal system states, so the field has the same diagonal entries and zero off-diagonal entry. Their half trace distance is

```math
D(\rho_F^Z,\rho_F^X)
=\sqrt{p_{\rm e}p_{\rm o}}
=\frac{\sqrt{1-e^{-4t}}}{2}
\geq\frac{\sqrt{1-e^{-4}}}{2}\gt0.495.
\qquad\text{(R11)}
```

A zero-query procedure gives the same output for both unknown oracles. It cannot approximate both within half diamond error $`0.1`$. Together with the one-query construction, this proves the first part of (R5).

## Proof route and boundaries

The [pair proof](reflection_pair.md) gives a constant physical counting gap for nearby qubit reflection oracles. The [tree proof](reflection_tree.md) first shows that the original reduced-system parity witness is exactly field blind, then modifies only the leaf action to make the coherent field retain parity.

The pair counting witness survives complete dephasing between different total photon numbers. The triple witness does not: its parity states become identical under that dephasing. The specified coherent field, including its phase reference, is therefore a load-bearing part of the triple converse.

The [related-work comparison](../references/RELATED_WORK.md#reflection-primitives-and-the-sister-system-task) credits the inherited ingredients and distinguishes the new field witnesses from the reduced-system result. [Finite diagnostics](../verification/README.md#reflection-field-checks) check conventions and negative controls; the all-input and asymptotic claims rest on these proofs.

## References

- **[SAS26]** Z.-X. Shang, D. An, and C. Shao, “Exponential Lindbladian fast forwarding and exponential amplification of certain Gibbs state properties,” author version [arXiv:2509.09517v2](https://arxiv.org/html/2509.09517v2), Appendix B.1, Eqs. (51)–(53).
- **[QDT26]** R. Lin, *Quantum Dephasing Threshold*, [source commit 5495822](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/tree/549582272ce6f5a3274be12de1bc5b2f16ed290e), especially the pair simulation and lower-bound pages.

