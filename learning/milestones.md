# Thirty milestones for Quantum Environment Fast Forwarding

This map follows the scientific question: how does the requested output change the cost of simulating the same open quantum dynamics? It contains exactly 30 understanding targets, independent of any reader's prior knowledge or progress. The selected educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [source bridge](watrous_bridge.md) translates its notation and identifies the additional field and oracle arguments supplied by this project.

The allocation is **12 background/preliminary milestones and 18 narrative/innovation milestones**. The background joins finite quantum registers, channel accuracy and the specified continuous field into one operational contract. The narrative starts with count centering and its observer obstruction, then follows coherent reflection-word reduction to separate pair and tree field witnesses, ending with the global output and resource comparison. This allocation reflects the project's two interfaces, quantum information and vacuum-field simulation. It does not follow the textbook's chapter count or claim to cover every technical lemma.

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
- **Conceptual connection:** The observer, dark-port and modified-tree results use bounded field effects or observables; their lower bounds do not rely on an unbounded readout.
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
- **Source pointers:** Watrous [§3.3][W3] for channel comparison; the project supplies the oracle conventions in [model, (M5)](../science/model.md#oracle-and-accuracy-conventions), [reflection model](../science/reflection_threshold.md) and [resources, general word code](../science/resources.md#general-exact-word-code).

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
- **Conceptual connection:** Keeping the system, keeping the field and reporting one measured bit can now be compared without silently changing access, the unitary/reflection promise or accuracy.
- **Source pointers:** Watrous [§§2.2 and 3.3][W2W3]; [model](../science/model.md); [resource boundaries](../science/resources.md#resource-boundaries).

## Narrative and innovation: M13–M30

### M13 · Photon counts and a removable system factor

- **Phase:** Narrative/innovation.
- **Central question:** How does the single-jump field encode powers of the unknown unitary?
- **Understanding target:** Read the coherent Poisson isometry, factor a common power from a count window, and explain why discarding the system removes that factor even with a reference.
- **Dependencies and story role:** M02–M04 and M09–M12. Start from the exact field and isolate count centering.
- **Conceptual connection:** Different joint states can have the same retained marginal; count coherence must remain.
- **Source pointers:** Watrous [§§2.1.2–2.2.2][W2W3] for the relevant channel, measurement or distance foundation; [centering, (C1)–(C5)](../science/centered_environment.md); [two-count example](watrous_bridge.md#a-two-count-example).

### M14 · A uniform coherent error budget

- **Phase:** Narrative/innovation.
- **Central question:** Why does a concentrated count window approximate every input?
- **Understanding target:** Relate omitted Poisson mass to the input-independent overlap and its square-root error bound, then connect concentration to time and precision dependence.
- **Dependencies and story role:** M06–M07 and M13. Turn an exact window identity into a channel guarantee.
- **Conceptual connection:** Amplitudes govern coherent tail error; normalized preparation avoids input-dependent postselection.
- **Source pointers:** Watrous [§§3.1–3.3][W2W3] for the relevant channel, measurement or distance foundation; [truncation and concentration, (C6)–(C10)](../science/centered_environment.md#reference-uniform-truncation-error).

### M15 · Preparation and the commuting extension

- **Phase:** Narrative/innovation.
- **Central question:** How are known amplitudes paid for, and when does centering extend to several fields?
- **Understanding target:** Explain the compiled finite-list preparation and threshold controls, then identify why commuting jumps permit independent product-mode count offsets.
- **Dependencies and story role:** M08, M10–M11 and M14. Close the construction and expose its extension's hypothesis.
- **Conceptual connection:** Known amplitude data still requires compilation; commutativity permits removing the product of count offsets.
- **Source pointers:** Watrous [§§2.1–2.2 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [resources, (R1)–(R3)](../science/resources.md#compiled-count-state-preparation-without-qram); [commuting jumps, (C11)–(C13)](../science/centered_environment.md#commuting-unitary-jumps).

### M16 · The single-unitary output comparison

- **Phase:** Narrative/innovation.
- **Central question:** Why can the field cost square-root time while the system costs linear time?
- **Understanding target:** Connect the qubit field gap and query hybrid to the square-root lower bound, then explain the separate same-oracle system witness and accumulated phase.
- **Dependencies and story role:** M05, M08 and M13–M15. Match constructive and converse time exponents.
- **Conceptual connection:** The common power is irrelevant only when the final system is discarded; one input suffices for a lower bound within an all-input task.
- **Source pointers:** Watrous [§§3.1 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [field optimality, (C14)–(C15)](../science/centered_environment.md#constant-error-optimality-for-one-jump); [system comparison, (P4)–(P10)](../science/interpretation.md#reduced-system-output-has-linear-query-complexity-in-the-same-model).

### M17 · A mean-one observer and temporal coherence

- **Phase:** Narrative/innovation.
- **Central question:** How can a weak known observer retain information absent from total count?
- **Understanding target:** Specify the horizon-indexed family, inverse-time observer rate and mean-one activity, and follow the one-photon kernel to the uniform-mode event.
- **Dependencies and story role:** M05, M09–M10 and M16. Introduce a concrete physical obstruction.
- **Conceptual connection:** A concentrated count can coexist with broad coherent insertion positions of a noncommuting jump.
- **Source pointers:** Watrous [§§2.1–2.3][W2W3] for the relevant channel, measurement or distance foundation; [observer model, kernel and gap, (O1)–(O9)](../science/noncommuting_observer.md).

### M18 · A linear bit lower bound and its finite effect

- **Phase:** Narrative/innovation.
- **Central question:** Why is the observer event hard even when only one bit is requested?
- **Understanding target:** Combine inverse-time oracle separation with the event gap, then explain why the exact position-register effect represents a physical measurement.
- **Dependencies and story role:** M07–M08 and M17. Connect the witness to query complexity and encoded readout.
- **Conceptual connection:** The lower bound does not require a large output; pulling back an effect differs from deleting a bath label.
- **Source pointers:** Watrous [§§2.3 and 3.1–3.3][W2W3] for the relevant channel, measurement or distance foundation; [observer lower bound and finite effect, (O10)–(O14)](../science/noncommuting_observer.md#query-lower-bound).

### M19 · The bit sampler and full-field baseline

- **Phase:** Narrative/innovation.
- **Central question:** How do concrete upper bounds match the observer task?
- **Understanding target:** Explain classical count sampling, coherent insertion, the position test and residual coin, then distinguish that sampler from coherent full-word preparation.
- **Dependencies and story role:** M11, M15 and M18. Complete the observer result and retain a general baseline.
- **Conceptual connection:** Classical count sampling is valid for this count-diagonal effect; the full field still requires trajectory coherence.
- **Source pointers:** Watrous [§§2.2–2.3 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [direct sampler, (O15)–(O16)](../science/noncommuting_observer.md#matching-upper-bound-for-the-one-bit-task); [full-word construction, (R4)](../science/resources.md#general-exact-word-code).

### M20 · The reflection promise and one-query endpoint

- **Phase:** Narrative/innovation.
- **Central question:** What changes when every supplied unitary squares to identity?
- **Understanding target:** State the fixed rates, phases, controlled SELECT, half-diamond error and dimension-uniform quantifiers, then explain the coherent parity construction for one reflection.
- **Dependencies and story role:** M08–M12 and M16. Begin the restricted reflection story with its input promise.
- **Conceptual connection:** A reflection is a special unitary; its constant-query parity endpoint does not contradict the generic single-unitary theorem.
- **Source pointers:** Watrous [§§2.2 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [reflection model and theorem](../science/reflection_threshold.md); [bridge comparison](watrous_bridge.md#reflection-jumps-and-the-sister-project).

### M21 · Coherent word reduction for a pair

- **Phase:** Narrative/innovation.
- **Central question:** Why does the sister project's line geometry also give a field upper bound?
- **Understanding target:** Explain reflection cancellation, the signed endpoint and diffusive width, while retaining chronological amplitudes and uncomputing reduction work.
- **Dependencies and story role:** M02, M06 and M20. Transfer a constructive identity with its coherence condition.
- **Conceptual connection:** A per-word identity lifts routinely to the field; a classical endpoint sample would change its coherences.
- **Source pointers:** Watrous [§§2.1–2.2][W2W3] for the relevant channel, measurement or distance foundation; [coherent reflection upper bounds](../science/reflection_threshold.md); [sister geometry](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/549582272ce6f5a3274be12de1bc5b2f16ed290e/science/pair-simulation.md).

### M22 · The qubit dark-port lower bound

- **Phase:** Narrative/innovation.
- **Central question:** What field-only event prevents a better pair exponent?
- **Understanding target:** Transform tilted-reflection couplings by the beamsplitter, interpret the Poisson dark count, and combine its constant gap with inverse-square-root oracle separation.
- **Dependencies and story role:** M05, M08 and M20–M21. Match the pair upper bound without the final system.
- **Conceptual connection:** Bath-label coherence becomes a count difference after a known mixer; this witness does not need cross-number coherence.
- **Source pointers:** Watrous [§§2.3 and 3.1–3.3][W2W3] for the relevant channel, measurement or distance foundation; [pair field proof](../science/reflection_pair.md); [dark-port bridge](watrous_bridge.md#a-dark-port-qubit-example).

### M23 · A system-hard tree with a field-blind input

- **Phase:** Narrative/innovation.
- **Central question:** Why does the original parity witness fail after discarding the system?
- **Understanding target:** Describe the prefix-parity coordinate change, explain why it fixes the root input, and use partial-trace invariance to remove all bit dependence from that field.
- **Dependencies and story role:** M03–M04 and M20–M22. Test the proposed converse transfer.
- **Conceptual connection:** System distinguishability need not survive the required marginal; the exact failed witness identifies a missing operational ingredient.
- **Source pointers:** Watrous [§2.1.3][W2W3] for the relevant channel, measurement or distance foundation; [original-tree field blindness](../science/reflection_tree.md); [sister system converse](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/549582272ce6f5a3274be12de1bc5b2f16ed290e/science/lower-bounds.md).

### M24 · Known leaf couplings make parity visible

- **Phase:** Narrative/innovation.
- **Central question:** How can three fixed-rate reflections put the answer into the field?
- **Understanding target:** Explain the leaf-Z replacement, the coordinate change leaving full parity on leaf emissions, and the orthogonal endpoint decomposition of the field states.
- **Dependencies and story role:** M06 and M23. Construct a field-sensitive family with exactly three involutions.
- **Conceptual connection:** Known endpoint supports make the retained phase distinction measurable through pure-state overlaps.
- **Source pointers:** Watrous [§§2.1.3 and 3.1–3.2][W2W3] for the relevant channel, measurement or distance foundation; [modified tree and field decomposition](../science/reflection_tree.md).

### M25 · Leaf occupation and linear query cost

- **Phase:** Narrative/innovation.
- **Central question:** Why is the modified tree's distinction uniformly large?
- **Understanding target:** Connect leaf hitting, conditional loop counts and occupation time to a constant field-distance gap, then explain the two-bit-query SELECT compiler and parity reduction.
- **Dependencies and story role:** M05–M08 and M24. Complete the converse's physical and oracle steps.
- **Conceptual connection:** Outward motion reaches a parity-bearing boundary; the charged compiler turns a field distinction into the established parity obstruction.
- **Source pointers:** Watrous [§§3.1–3.3][W2W3] for the relevant channel, measurement or distance foundation; [three-reflection proof](../science/reflection_tree.md).

### M26 · Which coherence survives measurement?

- **Phase:** Narrative/innovation.
- **Central question:** Why does number dephasing erase the triple witness but preserve the pair and observer events?
- **Understanding target:** Distinguish total-number phase, bath-label coherence, within-sector temporal coherence and fully counted records, including the exact number-phase relation between the triple parity fields.
- **Dependencies and story role:** M02, M17–M18, M22 and M25. State each witness's physical boundary.
- **Conceptual connection:** Different measurements erase different information; the coherent-field triple result cannot be transferred to a number-superselected target.
- **Source pointers:** Watrous [§§2.2.3 and 2.3][W2W3] for the relevant channel, measurement or distance foundation; [tree number-dephasing limit](../science/reflection_tree.md); [pair count](../science/reflection_pair.md); [observer event](../science/noncommuting_observer.md).

### M27 · Oracle savings and paid output work

- **Phase:** Narrative/innovation.
- **Central question:** What remains to be implemented after an oracle saving?
- **Understanding target:** Compare chronological-word, compressed-endpoint and physical-field representations, charging compilation, output slots, encoding conversion and measurement work separately.
- **Dependencies and story role:** M10–M11, M15, M19 and M21–M26. Complete the common resource account.
- **Conceptual connection:** An oracle-independent embedding is not a free physical implementation; photon count and output writing need not shrink with queries.
- **Source pointers:** Watrous [§§2.1–2.2][W2W3] for the relevant channel, measurement or distance foundation; [resources](../science/resources.md); [reflection resource account](../science/reflection_threshold.md); [tree time-split measurement](../science/reflection_tree.md).

### M28 · Time, dimension and microscopic representation

- **Phase:** Narrative/innovation.
- **Central question:** Which qualifications prevent an unsupported general law?
- **Understanding target:** Separate the horizon-indexed observer from the fixed-rate reflection family; explain growing triple dimension, supplied primitive count, fixed field phases and possible coherent drift in general unitary jumps.
- **Dependencies and story role:** M04, M08, M17, M20 and M25–M27. Interpret the exact physical and asymptotic promises.
- **Conceptual connection:** Zero explicit Hamiltonian does not imply Hermitian jumps; primitive count is not intrinsic Lindblad rank, and growing-dimensional hardness is not a fixed-dimensional theorem.
- **Source pointers:** Watrous [§§2.2.2 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [drift and representation](../science/interpretation.md#zero-explicit-hamiltonian-does-not-remove-coherent-drift); [reflection limits](../science/reflection_threshold.md).

### M29 · Inherited mechanisms and shared-result ownership

- **Phase:** Narrative/innovation.
- **Central question:** Which steps are inherited, and which establish the field boundary?
- **Understanding target:** Credit phase estimation, typical windows, Poisson preparation, word cancellation and parity methods, then identify the pair witness, failed tree transfer and modified field construction.
- **Dependencies and story role:** M13–M28. Integrate attribution before the final synthesis.
- **Conceptual connection:** The sister owns the reduced-system geometry and original theorem; this repository owns the field-only proof. Equal exponents do not make their output witnesses interchangeable.
- **Source pointers:** Watrous [§§2.2 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [related work](../references/RELATED_WORK.md); [Gaussian comparison](../science/gaussian_connection.md); [reflection theorem](../science/reflection_threshold.md).

### M30 · The complete output-dependent boundary

- **Phase:** Narrative/innovation.
- **Central question:** How do the requested output and supplied jump promise determine cost?
- **Understanding target:** Reconstruct the unitary system/field/record comparison, mean-one observer obstruction and one/two/three-reflection field hierarchy, including witnesses, constructions, output charges and limits.
- **Dependencies and story role:** M12 and M13–M29. Synthesize the account into one operational explanation.
- **Conceptual connection:** Discarding the system can remove an accumulated rotation, while retained field coherence can preserve an answer; charged access and retained information determine the conclusion.
- **Source pointers:** Watrous [§§2.2–2.3 and 3.3][W2W3] for the relevant channel, measurement or distance foundation; [principal results](../README.md#principal-results); [reflection theorem](../science/reflection_threshold.md); [interpretation](../science/interpretation.md); [verification boundaries](../verification/README.md).

## Further detail within this route

The [Watrous bridge](watrous_bridge.md) connects these targets to the selected source. The scientific pages retain the full proofs, constants and implementation details. The [verification guide](../verification/README.md) describes finite checks and their relation to the analytical arguments. These references deepen the same 30-milestone map.

[W]: https://cs.uwaterloo.ca/~watrous/TQI/
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W2W3]: https://cs.uwaterloo.ca/~watrous/TQI/
