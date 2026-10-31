# Thirty milestones for Quantum Environment Fast Forwarding

This map follows the scientific question: how does the requested output change the cost of simulating the same open quantum dynamics? It contains exactly 30 understanding targets, independent of any reader's prior knowledge or progress. The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [source bridge](watrous_bridge.md) translates its notation and identifies the additional field and oracle arguments supplied by this project.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background joins finite quantum registers, channel accuracy and the specified continuous field into one operational contract. The narrative starts with a removable common system rotation, then develops the observer obstruction and ends with the global comparison of outputs. This allocation reflects the project's two interfaces, quantum information and vacuum-field simulation. It does not follow the textbook's chapter count or claim to cover every technical lemma.

Dependencies refer only to earlier milestones. Scientific equation labels identify the authoritative statements; the map explains their roles without replacing their proofs. Watrous section links refer to the author's freely accessible prepublication chapter files, linked from the [official book page][W].

## Background and preliminaries: M01–M12

### M01 · System, field and reference

- **Phase:** Background/preliminaries.
- **Central question:** Which parts of a joint quantum state belong to the task?
- **Understanding target:** Identify the input system, emitted field and untouched reference, and explain which subsystems are retained or discarded.
- **Dependencies and story role:** None. Establish the objects before discussing dynamics or accuracy.
- **Conceptual connection:** Tensor-product structure determines the physical meaning of a partial trace; a register name alone does not specify a physical subsystem.
- **Source pointers:** Watrous [§§2.1.1–2.1.3][W2]; [model, (M1)–(M4)](../science/model.md).

### M02 · Probabilities and coherent amplitudes

- **Phase:** Background/preliminaries.
- **Central question:** What information is lost when a quantum count register is replaced by a sampled count?
- **Understanding target:** Distinguish diagonal probabilities from off-diagonal coherences and explain why equal photon-count distributions need not imply equal field states.
- **Dependencies and story role:** M01. Introduce the distinction on which the output comparison depends.
- **Conceptual connection:** Density operators describe both mixtures and coherent superpositions; measured trajectories retain less information than a coherent output channel.
- **Source pointers:** Watrous [§2.1.2][W2]; [model, “Counting records”](../science/model.md#counting-records); [interpretation, (P1)–(P3)](../science/interpretation.md).

### M03 · Discarding a subsystem

- **Phase:** Background/preliminaries.
- **Central question:** Why can a unitary on a discarded subsystem leave the requested output unchanged?
- **Understanding target:** Explain partial-trace invariance under a local unitary, including when the retained state contains an untouched reference.
- **Dependencies and story role:** M01–M02. Isolate the elementary operation that later permits count centering.
- **Conceptual connection:** Equality of retained marginals can coexist with different joint states; the output contract decides whether that difference matters.
- **Source pointers:** Watrous [§2.1.3][W2]; [centering lemma, (C3)–(C5)](../science/centered_environment.md#centering-lemma).

### M04 · A channel and its specified dilation

- **Phase:** Background/preliminaries.
- **Central question:** Does a reduced channel uniquely identify the physical field being simulated?
- **Understanding target:** Describe a channel through an isometry and partial trace, while distinguishing that representation from the additional specification of a particular microscopic output field.
- **Dependencies and story role:** M03. Connect the abstract channel language to the physical model.
- **Conceptual connection:** Stinespring representations organize system and environment outputs; field phases and couplings fix which environmental realization is the target here.
- **Source pointers:** Watrous [§§2.2.1–2.2.2][W2]; [model, (M2)–(M4) and oracle conventions](../science/model.md).

### M05 · A measurement event as an effect

- **Phase:** Background/preliminaries.
- **Central question:** How can one bounded measurement event certify that two output states differ?
- **Understanding target:** Interpret an effect between zero and identity, its acceptance probability, and the relation between an event-probability gap and trace distance.
- **Dependencies and story role:** M02–M04. Prepare the operational lower-bound witness.
- **Conceptual connection:** The observer result will concern a specific projector and ultimately a classical output bit, so an unbounded field observable is unnecessary.
- **Source pointers:** Watrous [§2.3.1][W2] and [§3.1.1][W3]; [observer, (O2), (O9)](../science/noncommuting_observer.md).

### M06 · Overlap, trace distance and discarded outputs

- **Phase:** Background/preliminaries.
- **Central question:** How does a small omitted amplitude sector translate into an output error?
- **Understanding target:** Relate pure-state overlap to trace distance and explain why discarding a subsystem cannot increase distinguishability.
- **Dependencies and story role:** M03 and M05. Supply the state-level ingredients for the coherent truncation proof.
- **Conceptual connection:** A coherent tail is controlled through an overlap, whereas a discarded probability in a classical channel mixture admits a different bound.
- **Source pointers:** Watrous [§§3.1.1 and 3.2.1][W3]; [reference-uniform truncation, (C6)–(C7)](../science/centered_environment.md#reference-uniform-truncation-error).

### M07 · Accuracy in the presence of a reference

- **Phase:** Background/preliminaries.
- **Central question:** What makes an approximation valid as a channel rather than only on a chosen input?
- **Understanding target:** Explain the supremum over input/reference states in half diamond distance and keep its factor of one half distinct from the unhalved norm.
- **Dependencies and story role:** M04–M06. Upgrade state comparisons to the project-wide accuracy convention.
- **Conceptual connection:** Uniformity over references lets a field simulator be used without assuming that its supplied input is isolated or known.
- **Source pointers:** Watrous [§§3.3.1–3.3.3][W3]; [model, (M6)](../science/model.md#oracle-and-accuracy-conventions).

### M08 · The oracle as a resource

- **Phase:** Background/preliminaries.
- **Central question:** What exactly counts as access to the unknown jump unitary?
- **Understanding target:** Distinguish controlled forward calls, inverse calls, supplied powers and SELECT access, and explain why the field requires a fixed phase convention.
- **Dependencies and story role:** M04 and M07. Make the input interface precise before counting operations.
- **Conceptual connection:** Channel distinguishability constrains an algorithm only after its allowed queries are specified; an uncontrolled oracle does not automatically supply a controlled one.
- **Source pointers:** Watrous [§3.3][W3] for channel comparison; the project supplies the oracle convention in [model, (M5)](../science/model.md#oracle-and-accuracy-conventions) and [resources, general word code](../science/resources.md#general-exact-word-code).

### M09 · Unitary jumps and Poisson activity

- **Phase:** Background/preliminaries.
- **Central question:** Why are the jump rates independent of the current system state in this model?
- **Understanding target:** Connect unitary jump operators to scalar no-jump survival and Poisson event counts with known mean.
- **Dependencies and story role:** M04 and M08. Introduce the stochastic structure that makes a concentration argument possible.
- **Conceptual connection:** The squared norm of a unitary trajectory does not reveal the unknown unitary, although interference between trajectories can reveal it.
- **Source pointers:** Watrous [§§2.1.2 and 2.2.2][W2] for mixtures and representations; the vacuum-field specialization is supplied in [model, (M1)–(M3), (M7)–(M9)](../science/model.md).

### M10 · Counts, temporal modes and chronological words

- **Phase:** Background/preliminaries.
- **Central question:** Which digital labels represent the continuous field without changing its physical meaning?
- **Understanding target:** Distinguish the single-field number code, commuting product number codes and the general chronological-word code; explain why the last generally does not factor across physical baths.
- **Dependencies and story role:** M01 and M09. Establish the encoding needed to interpret both upper and lower bounds.
- **Conceptual connection:** A known isometric embedding preserves the represented state, but locality of a physical operation depends on how that embedding acts on subsystems.
- **Source pointers:** Watrous [§§2.1.3 and 2.2.2][W2]; [model, (M8)–(M9) and encoding discussion](../science/model.md#which-output-encoding-is-being-simulated).

### M11 · Finite algorithms for an infinite output space

- **Phase:** Background/preliminaries.
- **Central question:** What must be paid for besides unknown-unitary queries?
- **Understanding target:** Separate a finite digital truncation from its infinite-field target and identify state preparation, arithmetic, classical storage, known gates and physical output production as distinct resources.
- **Dependencies and story role:** M07–M10. Complete the resource and approximation framework.
- **Conceptual connection:** A finite register can approximate an infinite-mode state through a declared embedding and a uniform tail estimate; this does not supply a physical optical decoder for free.
- **Source pointers:** Watrous [§2.1][W2] for finite registers; [bridge, finite registers and the field](watrous_bridge.md#finite-registers-and-the-field); [resources, (R1)–(R7)](../science/resources.md).

### M12 · The complete simulation contract

- **Phase:** Background/preliminaries.
- **Central question:** Which assumptions must remain fixed for two simulation costs to be comparable?
- **Understanding target:** State the input system/reference, vacuum coupling, known rates and horizon, controlled oracle, retained output, fixed encoding, error criterion and charged resources as one task.
- **Dependencies and story role:** M01–M11. Synthesize the background from individual objects into the operational problem.
- **Conceptual connection:** Keeping the system, keeping the field and reporting one measured bit can now be compared without silently changing access or accuracy.
- **Source pointers:** Watrous [§§2.2 and 3.3][W2W3]; [model](../science/model.md); [resource boundaries](../science/resources.md#resource-boundaries).

## Narrative and innovation: M13–M30

### M13 · The single-jump field isometry

- **Phase:** Narrative/innovation.
- **Central question:** How does the unknown unitary become correlated with photon number?
- **Understanding target:** Read the coherent Poisson expansion and identify the power applied on each number branch, including its off-diagonal field/reference blocks.
- **Dependencies and story role:** M02, M09–M12. Begin the narrative with the exact object that the algorithm must reproduce.
- **Conceptual connection:** An eigenstate of the unitary emits a coherent mode state, while a general input requires a channel construction that preserves reference correlations.
- **Source pointers:** Watrous [§§2.1.2–2.2.2][W2] for the state/channel language; [centered environment, (C1)–(C2), (C14)](../science/centered_environment.md).

### M14 · Removing a common system rotation

- **Phase:** Narrative/innovation.
- **Central question:** Why does a count window cost its width rather than its largest count?
- **Understanding target:** Factor the same power from all retained branches, use partial-trace invariance, and count the remaining forward calls without implementing an inverse.
- **Dependencies and story role:** M03, M08 and M13. Isolate the constructive mechanism.
- **Conceptual connection:** The freedom to discard the final system converts a large absolute count into a smaller relative-count task.
- **Source pointers:** Watrous [§2.1.3][W2]; [centering lemma, (C3)–(C5)](../science/centered_environment.md#centering-lemma); [two-count example](watrous_bridge.md#a-two-count-example).

### M15 · A tail bound valid for every input

- **Phase:** Narrative/innovation.
- **Central question:** Why does normalization of the retained Poisson window give a uniform channel guarantee?
- **Understanding target:** Explain the input-independent overlap and the square-root omitted-probability bound, including mixed inputs and untouched references.
- **Dependencies and story role:** M06–M07 and M14. Turn an exact identity on a window into an approximation to the full target.
- **Conceptual connection:** Directly preparing normalized amplitudes avoids input-dependent postselection; purification and contractivity transfer the guarantee to the requested output.
- **Source pointers:** Watrous [§§3.1–3.3][W3]; [reference-uniform truncation, (C6)–(C7)](../science/centered_environment.md#reference-uniform-truncation-error).

### M16 · Concentration sets the query width

- **Phase:** Narrative/innovation.
- **Central question:** How do mean count and target error determine the retained interval?
- **Understanding target:** Connect Poisson concentration to the explicit integer window, its square-root mean dependence and its logarithmic precision terms, including the separate preparation-error allowance.
- **Dependencies and story role:** M09 and M15. Derive the algorithm's scaling from the mechanism and its error budget.
- **Conceptual connection:** Fluctuations around the mean determine the number of required powers after the common rotation has been removed.
- **Source pointers:** Watrous [§3.3.2][W3] for composition of channel errors; the concentration argument is supplied in [centered environment, (C8)–(C10)](../science/centered_environment.md#explicit-concentration-window).

### M17 · Compiling the centered algorithm

- **Phase:** Narrative/innovation.
- **Central question:** How are the count amplitudes and query controls implemented without a loading oracle?
- **Understanding target:** Follow the mode-centered probability recurrence, finite-list rotation preparation and reversible threshold controls, and distinguish their gate/storage costs from oracle calls.
- **Dependencies and story role:** M08, M11 and M16. Close the resource account for the upper bound.
- **Conceptual connection:** A query advantage becomes a complete algorithm only after its known input data and preparation procedures have been specified and charged.
- **Source pointers:** Watrous [§2.2][W2] for channel composition; the circuit and arithmetic ingredients are supplied and attributed in [resources, (R1)–(R3)](../science/resources.md#compiled-count-state-preparation-without-qram).

### M18 · The commuting extension

- **Phase:** Narrative/innovation.
- **Central question:** When can one remove a separate count offset for each field?
- **Understanding target:** Use commutativity to obtain the product-mode code and common system factor, combine tail and preparation errors, and interpret the sum of window widths.
- **Dependencies and story role:** M10 and M14–M17. Extend the mechanism while keeping its algebraic requirement visible.
- **Conceptual connection:** Independent Poisson counts and commuting operator products jointly permit local count registers; the upper bound does not establish optimal dependence on the number of fields.
- **Source pointers:** Watrous [§§2.1.1 and 3.3.2][W2W3]; [commuting jumps, (C11)–(C13)](../science/centered_environment.md#commuting-unitary-jumps).

### M19 · Why the square-root exponent is necessary

- **Phase:** Narrative/innovation.
- **Central question:** Can a simulator use substantially fewer calls than the count-window algorithm at fixed error?
- **Understanding target:** Compare two nearby determinant-one qubit oracles, their separated coherent outputs and the query-by-query hybrid bound.
- **Dependencies and story role:** M05, M07–M08 and M16. Match the upper bound's time exponent with an operational lower bound.
- **Conceptual connection:** A constant output distinction produced by oracles separated by inverse square-root mean requires proportionally many queries; the claim concerns fixed error, not optimal precision dependence.
- **Source pointers:** Watrous [§§3.1.1 and 3.3][W3]; [single-jump optimality, (C14)–(C15)](../science/centered_environment.md#constant-error-optimality-for-one-jump).

### M20 · Keeping the system changes the task

- **Phase:** Narrative/innovation.
- **Central question:** Why does the same single-jump dynamics require linear query cost when its system output is retained?
- **Understanding target:** Connect accumulated phase in the reduced-system channel to the exact qubit discrimination pair and its truncated Poisson simulation upper bound.
- **Dependencies and story role:** M12, M14 and M19. Establish the same-oracle baseline for output-dependent complexity.
- **Conceptual connection:** Removing the common system factor was legitimate because that system was discarded; the system-output task retains the phase information that made that factor large.
- **Source pointers:** Watrous [§§3.1.1 and 3.3][W3]; [reduced-system comparison, (P4)–(P10)](../science/interpretation.md#reduced-system-output-has-linear-query-complexity-in-the-same-model).

### M21 · A known observer records insertion position

- **Phase:** Narrative/innovation.
- **Central question:** What extra information can a noncommuting observer place in a weak field?
- **Understanding target:** Describe the qubit jump and known Pauli observer, explain the rate $`1/t`$ and mean-one activity, and identify its coherent positions among the main jumps.
- **Dependencies and story role:** M09–M10, M12 and M18. Introduce the family that tests the limit of count centering.
- **Conceptual connection:** A concentrated total count can coexist with a broad set of noncommuting insertion positions. The family changes with the requested horizon.
- **Source pointers:** Watrous [§§2.1–2.3][W2] for the state and measurement language; [observer, (O1)–(O3)](../science/noncommuting_observer.md).

### M22 · Temporal coherence produces a finite event gap

- **Phase:** Narrative/innovation.
- **Central question:** How can a field with mean count one distinguish two nearby unknown unitaries?
- **Understanding target:** Follow the one-photon kernel to the uniform-mode event and its explicit constant probability gap, while distinguishing that event from total one-photon counting.
- **Dependencies and story role:** M05–M06 and M21. Construct a bounded observable witness rather than relying only on a sensitivity heuristic.
- **Conceptual connection:** Coherence between emission times within one photon-number sector remains accessible even when coherence between different count sectors is removed.
- **Source pointers:** Watrous [§§2.3.1 and 3.1.1][W2W3]; [observer probability and gap, (O4)–(O9)](../science/noncommuting_observer.md#exact-probability-of-the-temporal-mode-event).

### M23 · One bit can require linearly many queries

- **Phase:** Narrative/innovation.
- **Central question:** Why does the observer lower bound survive when the output is only its event bit?
- **Understanding target:** Combine the constant event gap, inverse-time oracle separation and two approximation errors to obtain the linear query requirement at error below half the gap.
- **Dependencies and story role:** M08, M19 and M22. Convert the physical witness into an output-size-independent computational obstruction.
- **Conceptual connection:** The lower bound follows from a binary statistical distinction, so it does not rely on emitting many photons or choosing a costly field decoder.
- **Source pointers:** Watrous [§§3.1.1 and 3.3.2–3.3.3][W3]; [observer query bound, (O10)–(O11)](../science/noncommuting_observer.md#query-lower-bound).

### M24 · Pulling the physical measurement into the word code

- **Phase:** Narrative/innovation.
- **Central question:** How can a physical observer measurement be represented when bath labels are not tensor factors?
- **Understanding target:** Connect integration over the main-photon time gaps to the exact position-register effect, and distinguish a pulled-back measurement from an unjustified bath trace.
- **Dependencies and story role:** M05, M10 and M21–M22. Resolve the interface between the physical witness and a finite algorithm.
- **Conceptual connection:** The effect is the uniform-position projector plus a weighted orthogonal complement; its explicit form permits a known circuit despite the encoding's nonlocality across baths.
- **Source pointers:** Watrous [§2.3.1][W2]; [exact finite-register witness, (O12)–(O14)](../science/noncommuting_observer.md#an-exact-finite-register-implementation-of-the-witness).

### M25 · The matching direct bit sampler

- **Phase:** Narrative/innovation.
- **Central question:** How is the hard bit sampled with a matching linear upper bound?
- **Understanding target:** Explain classical count sampling, coherent insertion of the known Pauli, the uniform-position test and residual coin, and the reference-uniform error from conditioning the Poisson count.
- **Dependencies and story role:** M07, M11, M17 and M24. Complete the observer result with a concrete construction.
- **Conceptual connection:** Count coherence may be discarded because this effect is block diagonal in counts; position coherence must remain. Only the sampled count's loader is compiled.
- **Source pointers:** Watrous [§§2.1.2, 2.3.1 and 3.3][W2W3]; [matching bit upper bound, (O15)–(O16)](../science/noncommuting_observer.md#matching-upper-bound-for-the-one-bit-task); [resource account](../science/resources.md#the-observer-event-is-efficiently-measurable-in-the-word-code).

### M26 · The general full-field baseline

- **Phase:** Narrative/innovation.
- **Central question:** What upper bound remains when count centering is unavailable?
- **Understanding target:** Describe coherent total-count and chronological-label preparation, its Poisson cutoff, and the different query costs of SELECT and individual controlled oracles.
- **Dependencies and story role:** M08–M11 and M23–M25. Place the observer bit inside the complete two-field simulation task.
- **Conceptual connection:** The established coherent trajectory construction yields a linear-query full-field upper bound in the declared global code; it does not automatically give an efficient reduced-bath decoder.
- **Source pointers:** Watrous [§2.2.2][W2] for isometric representations; [general exact word code, (R4)](../science/resources.md#general-exact-word-code); [attribution to Shang–An–Shao](../references/RELATED_WORK.md#lindbladian-simulation-and-phase-estimation).

### M27 · Which measurements erase the oracle information?

- **Phase:** Narrative/innovation.
- **Central question:** Why do classical counting records cost zero queries while the observer bit is hard?
- **Understanding target:** Distinguish complete single-mode number dephasing, multi-bath count-sector dephasing and fully measured time-resolved records, including their effects on reference correlations.
- **Dependencies and story role:** M02, M07, M10 and M22–M26. Connect the quantum and classical output tasks without conflating their measurements.
- **Conceptual connection:** The single-jump number basis is complete for its encoded mode; general number sectors still contain temporal coherence, which the observer projector detects.
- **Source pointers:** Watrous [§§2.2.3 and 2.3][W2]; [number dephasing, (P1)–(P3)](../science/interpretation.md#number-dephasing-removes-all-single-jump-field-information); [counting records](../science/model.md#counting-records).

### M28 · Coherent drift inside a unitary jump

- **Phase:** Narrative/innovation.
- **Central question:** What does zero explicit Hamiltonian mean for the hard family?
- **Understanding target:** Interpret the exact decomposition of a near-identity unitary jump into coherent drift and Pauli dissipation, and explain why changing the jump representation changes the specified output dilation.
- **Dependencies and story role:** M04, M08 and M21–M23. Clarify the physical mechanism behind the inverse-time oracle comparison.
- **Conceptual connection:** A finite accumulated rotation can be transferred to observer temporal coherence even though the given microscopic representation has no separate Hamiltonian term.
- **Source pointers:** Watrous [§2.2.2][W2] for representation language; the generator identities and field qualification are supplied in [interpretation, (P11)–(P12)](../science/interpretation.md#zero-explicit-hamiltonian-does-not-remove-coherent-drift).

### M29 · Prior mechanisms and the surviving contribution

- **Phase:** Narrative/innovation.
- **Central question:** Which parts of the construction follow familiar simulation and estimation ideas, and which distinctions require the project's arguments?
- **Understanding target:** Credit ordinary phase estimation for fixed-error square-root scaling, typical-window centering and coherent trajectory preparation; identify the direct precision bound, specified field conversion and observer boundary separately.
- **Dependencies and story role:** M16–M20 and M23–M28. Integrate the comparison with prior work before assessing the result's scope.
- **Conceptual connection:** Equality of reduced channels does not by itself identify a physical complementary output or pay for its digital implementation. Research citations support attribution without adding another educational anchor.
- **Source pointers:** Watrous [§§2.2.2 and 3.3][W2W3]; [Gaussian and phase-estimation comparison](../science/gaussian_connection.md); [related work](../references/RELATED_WORK.md).

### M30 · The complete output-dependent boundary

- **Phase:** Narrative/innovation.
- **Central question:** What changes when the requested output is a record, a coherent field, the system, or the observer bit?
- **Understanding target:** Reconstruct the zero, square-root and linear worst-case query comparison at fixed small error, identify its matching constructions and witnesses, and retain the digital-record resolution, horizon-indexed observer, oracle, reference and encoding qualifications.
- **Dependencies and story role:** M12 and M13–M29. Synthesize the narrative into one operational explanation.
- **Conceptual connection:** Information discarded by the task can remove a common accumulated rotation; retained temporal coherence can restore linear query cost. Query savings remain distinct from physical emission time, energy and arbitrary decoding cost.
- **Source pointers:** Watrous [§§2.2–2.3 and 3.3][W2W3]; [principal results](../README.md#principal-results), [interpretation](../science/interpretation.md), [resource boundaries](../science/resources.md#resource-boundaries) and [verification limits](../verification/README.md).

## Further detail within this route

The [Watrous bridge](watrous_bridge.md) connects these targets to the selected source. The scientific pages retain the full proofs, constants and implementation details. The [verification guide](../verification/README.md) describes finite checks and their relation to the analytical arguments. These references deepen the same 30-milestone map.

[W]: https://cs.uwaterloo.ca/~watrous/TQI/
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W2W3]: https://cs.uwaterloo.ca/~watrous/TQI/
