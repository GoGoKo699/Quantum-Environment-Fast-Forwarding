# From Watrous to quantum environment fast forwarding

A simulator of an open quantum process can be asked to return its final system, its emitted field, or a measurement result. These requests preserve different information. This project asks how that choice changes the number of calls to an unknown jump unitary.

The single educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. The [author's book page][W] links the accessible prepublication manuscript and its chapter files. Those files supply the section numbering used here; this repository links to them without redistributing them. The [30-milestone map](milestones.md) organizes this project's story, while the book supplies its quantum-information foundation.

## The relevant parts of the anchor

Use these sections as needed for the indicated project step. Reading the entire book is not a prerequisite for following the scientific account.

| Watrous section | Foundation used here | Project destination |
|---|---|---|
| [§§2.1.1–2.1.3][W2] | Registers, states, reductions and purifications | [System, field and reference](../science/model.md) |
| [§§2.2.1–2.2.2][W2] | Channels and their representations | [Specified dilation, (M3)–(M4)](../science/model.md) |
| [§2.3.1][W2] | Measurement effects and outcome probabilities | [Observer projector and encoded effect](../science/noncommuting_observer.md) |
| [§3.1.1][W3] | Binary state discrimination | [Finite event gap, (O9)](../science/noncommuting_observer.md#a-uniform-constant-gap) |
| [§3.2.1][W3] | Fidelity and pure-state overlap | [Truncation estimate, (C6)–(C7)](../science/centered_environment.md#reference-uniform-truncation-error) |
| [§§3.3.1–3.3.3][W3] | Channel discrimination and completely bounded trace norm | [Reference-uniform accuracy, (M6)](../science/model.md#oracle-and-accuracy-conventions) |
| [§§2.1.3 and 3.1.1][W2W3] | Partial-trace invariance and a measurable output distinction | [Field-blind tree and modified field witness](../science/reflection_tree.md) |
| [§§2.3.1 and 3.3][W2W3] | Pulling known effects back to encoded channels | [Dark-port count and query hybrid](../science/reflection_pair.md) |

Watrous develops the finite-dimensional channel language used by the algorithms. The vacuum-field dynamics, Poisson concentration, query model, reflection-word geometry and field-witness calculations are supplied in the scientific pages, with their own primary references. Their presence in the bridge does not attribute them to the textbook.

## Notation and error conventions

Watrous writes vectors and adjoints without Dirac notation. The project often uses kets and daggers. The following translations keep the mathematical objects unchanged.

| Anchor notation or term | Project notation or use |
|---|---|
| A unit vector $`u`$ and the state $`uu^*`$ | A pure-state ket and its density operator |
| Adjoint $`A^*`$ | Adjoint $`A^\dagger`$ |
| A channel between register spaces | The system channel $`\Phi`$, field channel $`\Gamma`$, or finite algorithm $`\mathcal A`$, with input and output stated explicitly |
| Completely bounded trace norm | Diamond norm; this project uses **one half** of that norm for channel distance |
| An effect in a binary measurement | An operator between zero and identity whose expectation is the acceptance probability |

In Dirac notation, the pure density operator is $`|\psi\rangle\langle\psi|`$. For states and channels, respectively, the project uses

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1,
\qquad
d_\diamond(\Phi,\Psi)=\frac12\|\Phi-\Psi\|_\diamond.
```

The channel distance allows an untouched reference entangled with the input. Thus a statement about one input state does not establish the algorithm's accuracy guarantee. A particular input and measurement can, however, suffice for a lower bound: an algorithm required to work on every input must work on that example too. The exact convention is [model (M6)](../science/model.md#oracle-and-accuracy-conventions).

For pure states, the modulus of the overlap is the unsquared fidelity. Their trace distance is the square root of one minus the squared overlap. This convention explains why a coherent omitted probability $`\delta`$ leads to the bound $`\sqrt\delta`$ in the field algorithm. Keeping the probability, amplitude and squared overlap distinct prevents a factor-of-square-root error.

## The missing step from a channel to a particular output field

An isometry can describe a joint system-environment evolution. Tracing either part gives one of its two marginal channels. In this project the isometry is fixed by vacuum input fields and specified jump couplings. The target retains the field and discards the final system.

The reduced generator alone does not contain all of that specification. Multiplying a jump unitary by a phase leaves its action by conjugation on the system unchanged. It rotates relative photon-number phases in the emitted field. The [model](../science/model.md#oracle-and-accuracy-conventions) therefore supplies a phase-referenced controlled oracle and a fixed coupling convention. The abstract freedom to choose a channel representation does not permit an unknown-parameter-dependent change of the required physical output.

This is the first bridge from the textbook: apply its channel language after specifying which dilation, which marginal and which oracle are part of the task.

## A two-count example

Consider the normalized portion of the single-field isometry supported on photon counts two and three. Let $`c_2,c_3`$ be its known nonnegative amplitudes, with $`c_2^2+c_3^2=1`$. For any pure system input, this portion is

```math
V_A|\psi\rangle
=c_2U^2|\psi\rangle\otimes|2\rangle
+c_3U^3|\psi\rangle\otimes|3\rangle.
```

It factors as

```math
\begin{aligned}
V_A&=(U^2\otimes I)\widehat V_A,\\
\widehat V_A|\psi\rangle
&=c_2|\psi\rangle\otimes|2\rangle
+c_3U|\psi\rangle\otimes|3\rangle.
\end{aligned}
```

Prepare the two count amplitudes, apply one controlled forward call on the count-three branch, and discard the system. The factor $`U^2`$ acts only on that discarded system, so the retained field is exactly the same as for $`V_A`$. The argument also holds with an arbitrary untouched reference. No inverse is implemented.

The field can retain coherence between counts two and three. Sampling one of those counts classically would generally remove that coherence and would be a different channel. Also, this example only concerns a normalized two-count window. Its quality as an approximation to a full Poisson distribution depends on the omitted probability. The full construction chooses a much wider concentration window and proves the error bound in [centered environment (C3)–(C10)](../science/centered_environment.md).

For a general window, the same factorization makes the number of forward calls equal to its width. Poisson concentration places most probability within a width of order square root of the mean at fixed error. The project proves the resulting precision-dependent query bound and compiles the known amplitudes from an explicit classical list. The [resource account](../science/resources.md#compiled-count-state-preparation-without-qram) charges that preparation and storage.

## Finite registers and the field

The physical field is an infinite-dimensional Fock space, while the input system is finite dimensional. The single-jump output occupies one temporal mode, but even that mode has infinitely many photon-number states. Several noncommuting jumps additionally require chronological label information.

The algorithms return finite digital registers. A declared isometric embedding maps those registers into the physical field. It is known from the time, rates and encoding choices and is independent of the unknown unitary. The finite count or word cutoff makes the implemented algorithm a finite-dimensional channel. The approximation is assessed after its output is embedded into the full target space.

The field error is controlled directly: for every purified system/reference input, the exact and normalized truncated isometries have overlap equal to the square root of the retained Poisson mass. The pure-state trace-distance identity and partial-trace contractivity then bound the error against the infinite-field state. The bound is uniform in the input. A reference no larger than the finite input dimension suffices by Schmidt compression of a pure input; convexity handles mixed inputs. This reasoning does not assume that an infinite-dimensional optical state can be prepared by a finite circuit exactly.

The encoding also determines which operations have simple finite circuits. The single-field number code and the commuting product code have a direct mode interpretation. The general chronological-word embedding usually does **not** factor into one register per physical bath. Deleting occurrences of a bath's label is therefore not its physical partial trace. See [model (M8)–(M9) and its encoding discussion](../science/model.md#which-output-encoding-is-being-simulated).

The book provides the finite-register foundation. The declared embedding, reference-uniform tail estimate and explicit treatment of physical measurements supply the bridge to this continuous-output problem. Producing the actual photons, engineering their modes or implementing an arbitrary decoder carries separate physical and computational costs.

## From distinguishability to query lower bounds

Watrous's discrimination framework gives an operational meaning to a trace-distance gap. The query argument adds a resource constraint: a single call to two nearby unitary oracles can change the resulting state only by their operator-norm separation. Replacing the calls one at a time bounds the total distinguishability of a procedure using $`q`$ calls.

The single-field example chooses two qubit oracles separated by the inverse square root of the mean count. Their coherent field outputs remain separated by a constant. The algorithm must make enough calls to create that output distinction, which gives the fixed-error square-root lower bound. The [complete proof](../science/centered_environment.md#constant-error-optimality-for-one-jump) includes the input and the constants.

The observer construction uses a smaller oracle separation, of order inverse time, while retaining a constant measurement gap for horizons $`t\geq2\pi`$. The known observer jump has rate $`1/t`$, so it emits one photon on average over duration $`t`$. The event is exactly one photon in the uniform temporal mode and vacuum in all orthogonal observer modes. This is more selective than simply counting one observer photon. Its probability detects coherence between emission times within that number sector.

At fixed error below half the gap, the constant distinction forces linearly many queries even when only the event bit is requested. The [observer proof, (O1)–(O11)](../science/noncommuting_observer.md), fixes the horizon-indexed family and the constants. This does not classify every noncommuting model. The explicitly specified Hamiltonian is zero in the given representation; the [generator identity](../science/interpretation.md#zero-explicit-hamiltonian-does-not-remove-coherent-drift) explains the coherent drift contained in the near-identity jump.

## The observer measurement as a finite effect

The general word code's failure to factor across baths makes an explicit measurement construction essential. Conditional on $`n`$ main photons and one observer photon, the observer can occupy $`n+1`$ chronological positions. On that position register, the physical uniform-mode event pulls back to

```math
\begin{aligned}
E_n&=\frac{I+\mathbf J}{n+2}\\
&=|u_n\rangle\langle u_n|
+\frac{I-|u_n\rangle\langle u_n|}{n+2},
\end{aligned}
```

where $`\mathbf J`$ is the all-ones matrix and $`|u_n\rangle`$ is the normalized uniform superposition of positions. The project derives this effect from integrals of the time gaps, rather than treating a bath label as a tensor factor. See [observer (O12)–(O14)](../science/noncommuting_observer.md#an-exact-finite-register-implementation-of-the-witness).

For one main photon there are two positions. The effect has eigenvalue one on their symmetric superposition and eigenvalue one third on the orthogonal state. A binary measurement can therefore accept the symmetric outcome with certainty and accept the orthogonal outcome with probability one third. The same rule for general $`n`$ uses the known probability $`1/(n+2)`$.

This yields the matching bit sampler. Sample the main count, prepare a uniform position register, coherently insert the known Pauli among exactly that many forward calls, and perform the effect. Count sampling is legitimate because this particular measurement is block diagonal in counts. The position superposition remains coherent. With a finite conditioned Poisson law, the omitted tail enters as a mixture of channels, giving a bound linear in its probability; it is a different error argument from coherent field truncation. The [direct sampler](../science/noncommuting_observer.md#matching-upper-bound-for-the-one-bit-task) proves the reference-uniform guarantee and its resource bounds.

## Reflection jumps and the sister project

A reflection is a Hermitian unitary: $`R=R^\dagger`$ and $`R^2=I`$. It has only the two possible eigenvalues plus and minus one. A long sequence of identical reflection jumps therefore depends only on whether its count is even or odd. This restriction changes the generic single-unitary field cost from square-root time to one controlled call. The general unitary theorem and the reflection theorem concern different promised inputs.

The sister [Quantum Dephasing Threshold](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold) establishes the constant/square-root/linear threshold when the reduced **system** channel is requested. Its [word reduction](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/549582272ce6f5a3274be12de1bc5b2f16ed290e/science/pair-simulation.md) supplies the geometry used here. This repository owns the [field-only theorem](../science/reflection_threshold.md), including the physical field embedding and the separate field witnesses. The same educational anchor leads to different project-specific routes.

### Which system simplifications preserve the field?

With $`k`$ supplied reflections, fix $`L_j=R_j/\sqrt{k}`$, total rate one, zero explicit Hamiltonian, identity scattering and zero coupling phases. A phase-referenced controlled SELECT is supplied. The target retains every labelled field and discards the system, with arbitrary input references and half diamond error $`0.1`$. The [reflection theorem](../science/reflection_threshold.md) keeps this contract distinct from the single-unitary forward-oracle model.

For one reflection, prepare the known coherent even/odd count amplitudes and apply $`R`$ on the odd branch. For two reflections, cancelling adjacent equal letters reduces each chronological word to an alternating word. The signed reduced endpoint behaves as a diffusive walk on a line, so a typical reduced length is of order $`\sqrt t`$. These operator identities apply separately to every trajectory amplitude. Retaining the original trajectory labels coherently preserves their interference; sampling the reduced endpoint would generally erase it. The lift of the sister's word identity is routine, rather than a new fast-forwarding primitive.

Watrous supplies the distinction between an isometric representation and a classical mixture. The extra algorithmic step here is reversible word processing: compute the endpoint, apply its reduced word, then erase the endpoint work register. Truncating a coherent endpoint tail requires a square-root probability bound, just as in count centering. Known state preparation, output registers and embedding conversion are still charged separately.

### A dark-port qubit example

For two reflections, set

```math
R_\pm=\cos\theta\,Z\pm\sin\theta\,X,
\qquad L_1=R_+/\sqrt2,\quad L_2=R_-/\sqrt2.
```

A known 50:50 mixing of the bath labels changes the couplings to

```math
L_b=\cos\theta\,Z,\qquad L_d=\sin\theta\,X.
```

The dark bath is empty at $`\theta=0`$. Its photon count is Poisson with mean $`t\sin^2\theta`$ for every input; this follows because $`L_d^\dagger L_d=\sin^2\theta I`$. At $`\theta=t^{-1/2}`$, the probability of at least one dark photon remains separated from zero by a constant, whereas the oracle separation is at most $`t^{-1/2}`$. The [pair proof](../science/reflection_pair.md) converts this event gap into the matching square-root query lower bound.

This is a physical field-only measurement. The final system is never read. Mixing bath labels and counting photons preserve total photon number, so the witness survives dephasing between different total-number sectors. In a chronological word encoding, the bath mixer is a known rotation on every photon label; its processing work is proportional to the represented word length. Zero additional unknown queries does not make that processing or the physical optical operation costless.

### Why the original tree argument loses its answer

The sister's original three-reflection construction carries unknown bit parity in a system answer register on a branching tree. From a fixed root input, a change of system coordinates $`G_x`$ removes the unknown edge bits, and it fixes that input. The joint output then differs from the known instance only by $`G_x`$ on the final system. Watrous's partial-trace identity immediately implies that the retained field is exactly unchanged. The system lower bound alone therefore supplies no field lower bound on this input.

The [field proof](../science/reflection_tree.md) replaces the missing leaf transitions by known $`Z`$ actions on the answer qubit. There are still three reflection types with fixed rates $`1/3`$. Removing the edge bits now leaves a sign on leaf-loop emissions determined by the full parity. Within each known endpoint subspace the field is a pure vector. The trace distance of the two full fields is the sum of these subspace weights times their pure-state trace distances. This is a direct use of the textbook's distinguishability and pure-overlap formulas; the tree walk, conditional loop count and local-time estimate are supplied by the project.

The proof gives a field half trace distance at least $`0.5071203359`$. Its oracle reduction uses two bit queries for each controlled SELECT, so the standard parity lower bound yields linear reflection-query cost. The hard dimension grows as $`\exp(\Theta(t))`$. A late-interval measurement of vacuum/one-photon coherence provides an explicit alternative to a general field-state discrimination measurement; its time-splitting map is derived in the same scientific page.

### Which coherence matters?

The three main witnesses retain different coherence:

| Witness | Retained field information | Effect of total-number dephasing |
|---|---|---|
| Mean-one observer | Temporal coherence within its one-photon sector | The lower-bound event survives. |
| Two-reflection dark port | Coherence between bath labels before the fixed mixer | The dark-count lower bound survives. |
| Modified three-reflection tree | Coherence between total photon numbers | The two parity outputs become identical. |

The last statement is exact. For the two parity field states of the tree witness,

```math
\rho_1=e^{i\pi N_{\mathrm{total}}}\rho_0e^{-i\pi N_{\mathrm{total}}}.
```

Complete total-number dephasing removes this distinction. The triple result therefore concerns the specified coherent, phase-referenced field. It does not establish a linear lower bound for number-dephased fields or for fixed system dimension. The phases are fixed physical input data; an unknown-dependent choice of output embedding cannot remove them.

The field threshold and the sister system threshold share a geometry, but their lower-bound outputs have to be checked separately. This is the main conceptual exchange between the two projects. The [30-milestone map](milestones.md) joins it to the original unitary-jump and observer results without counting the routine upper-bound lift as an independent discovery.

## Connecting the outcomes and the prior work

At fixed small error, classical counting records for the single-jump model require zero unknown-unitary queries at a chosen digital resolution. The worst-case query cost grows as the square root of the mean count for the coherent field and linearly in that mean for the reduced system. Adding the specified known noncommuting observer gives a one-bit task with worst-case linear query cost in time. The first distinction concerns what information is discarded. The second concerns the temporal coherence retained by a particular measurement.

Ordinary forward phase estimation already explains the fixed-error square-root scale of the single-field complement. Earlier work also provides typical-window centering, Gaussian phase-clock purifications and coherent trajectory preparation. The project's [related-work account](../references/RELATED_WORK.md) attributes those mechanisms. The direct Poisson argument adds its explicit precision dependence and resource account in the stated model, while the observer construction supplies the bounded-output obstruction and matching sampler. The [Gaussian comparison](../science/gaussian_connection.md) exhibits a known output conversion and distinguishes it from an uncharged finite implementation.

The reflection-field threshold adds a different restriction to this output comparison: the supplied primitives are Hermitian involutions at equal fixed rates. Its upper lift uses inherited word cancellation, while its pair and modified-tree lower witnesses must remain field-visible after the system is discarded. The [reflection theorem](../science/reflection_threshold.md) and the sister's reduced-system theorem state their respective tasks and proof ownership. Their matching exponents do not imply that a system witness automatically transfers to its complementary output.

These primary research citations support the scientific claims. Watrous remains the sole educational anchor. The [milestone map](milestones.md) joins its foundations to the supplied derivations, ending with the scope of the complete output-dependent comparison. Numerical reproduction in [verification](../verification/README.md) checks finite instances and independent formulations; the analytical pages establish the uniform and asymptotic claims.

[W]: https://cs.uwaterloo.ca/~watrous/TQI/
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W2W3]: https://cs.uwaterloo.ca/~watrous/TQI/
