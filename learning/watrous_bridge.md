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

Watrous develops the finite-dimensional channel language used by the algorithms. The vacuum-field dynamics, Poisson concentration, query model and observer calculation are supplied in the project's scientific pages, with their own primary references. Their presence in the bridge does not attribute them to the textbook.

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

## Connecting the outcomes and the prior work

At fixed small error, classical counting records for the single-jump model require zero unknown-unitary queries at a chosen digital resolution. The worst-case query cost grows as the square root of the mean count for the coherent field and linearly in that mean for the reduced system. Adding the specified known noncommuting observer gives a one-bit task with worst-case linear query cost in time. The first distinction concerns what information is discarded. The second concerns the temporal coherence retained by a particular measurement.

Ordinary forward phase estimation already explains the fixed-error square-root scale of the single-field complement. Earlier work also provides typical-window centering, Gaussian phase-clock purifications and coherent trajectory preparation. The project's [related-work account](../references/RELATED_WORK.md) attributes those mechanisms. The direct Poisson argument adds its explicit precision dependence and resource account in the stated model, while the observer construction supplies the bounded-output obstruction and matching sampler. The [Gaussian comparison](../science/gaussian_connection.md) exhibits a known output conversion and distinguishes it from an uncharged finite implementation.

These primary research citations support the scientific claims. Watrous remains the sole educational anchor. The [milestone map](milestones.md) joins its foundations to the supplied derivations, ending with the scope of the complete output-dependent comparison. Numerical reproduction in [verification](../verification/README.md) checks finite instances and independent formulations; the analytical pages establish the uniform and asymptotic claims.

[W]: https://cs.uwaterloo.ca/~watrous/TQI/
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
