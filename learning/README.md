# Learning route

The project studies a concrete distinction: an open quantum process can be expensive to simulate when its system is retained, cheaper when only one coherent output field is retained, and cheap again when that field is reduced to a classical counting record. A known noncommuting observer can make even one measurement bit linearly hard in the evolution time. Restricting the jump unitaries to reflections gives another precise boundary: one, two and three supplied reflections have constant, square-root and linear worst-case field-query cost. The [scientific entrypoint](../README.md) states the exact results and assumptions.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018)**. Its [official author page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the accessible prepublication manuscript. The relevant foundations are channels, reductions, measurements and channel distance in Chapters 2 and 3. The [Watrous bridge](watrous_bridge.md) specifies the sections, translates notation and explains the additional steps supplied by this project.

## Reading routes

| Reading purpose | Route |
|---|---|
| Understand the whole scientific story | Follow the [30-milestone map](milestones.md), using the bridge and its canonical source pointers where needed. |
| Understand the main mechanism first | Read the bridge's [two-count example](watrous_bridge.md#a-two-count-example), then the [centering lemma](../science/centered_environment.md#centering-lemma) and [observer measurement](watrous_bridge.md#the-observer-measurement-as-a-finite-effect). |
| Understand the sister-project exchange | Read the bridge's [reflection-field comparison](watrous_bridge.md#reflection-jumps-and-the-sister-project), then the [reflection theorem](../science/reflection_threshold.md), [pair witness](../science/reflection_pair.md) and [modified tree](../science/reflection_tree.md). |
| Inspect the exact task and guarantees | Start with the [model](../science/model.md), then the [centered-field proof](../science/centered_environment.md) and [observer proof](../science/noncommuting_observer.md). |
| Check resource and novelty claims | Read [resources](../science/resources.md), [interpretation](../science/interpretation.md), the [Gaussian comparison](../science/gaussian_connection.md) and [related work](../references/RELATED_WORK.md). |
| Reproduce finite checks | Follow the commands and validation boundaries in [verification](../verification/README.md). |

## The milestone structure

The common map contains **exactly 30 milestones**: M01–M12 cover background and preliminaries, and M13–M30 develop the narrative and innovation. The background moves from individual registers and measurements to the full simulation contract. The narrative joins count centering and its observer boundary to coherent reflection-word reduction, the field-only pair and tree witnesses, and the final output/resource comparison. Each milestone has a central question, an understanding target, dependencies and story role, a conceptual connection, and source pointers.

The allocation reflects the need to connect finite-dimensional quantum information with a specified continuous vacuum field. It is a map of the project's central understanding targets, rather than every technical calculation or every chapter of the anchor. The bridge gives a small worked example and distinguishes the textbook foundation, locally supplied derivations and primary research dependencies.

## Distinctions that organize the route

The input system may be entangled with an untouched reference, so the simulator's accuracy is a channel guarantee. The field is specified by its microscopic coupling, including phases; its reduced Lindblad generator alone is insufficient. A finite digital field encoding requires an explicit embedding and error bound. For noncommuting jumps, the chronological-word code generally does not factor across physical baths, so a physical measurement must be represented correctly within it.

The single-unitary upper bounds count forward controlled calls. The reflection theorem supplies controlled SELECT access at fixed rates. Known gates, classical compilation and storage, and physical field production remain separate costs. The lower bounds use specified discrimination examples. The observer's rate is inversely proportional to the requested horizon; the reflection tree instead has fixed rates and growing dimension. Its parity signal disappears under total-photon-number dephasing, whereas the pair dark-port witness survives that dephasing. These qualifications stay attached to the scientific reading route.

The sister [Quantum Dephasing Threshold](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold) owns the reflection-word geometry and reduced-system theorem. This repository owns the field-only proof and physical measurement constructions. Watrous is their common educational anchor; each project supplies its own bridge and 30-target map. The field witness must be proved separately: hardness of a measured system output does not transfer automatically after that system is discarded.

Return to the [repository overview](../README.md) for the principal results, or begin with the [Watrous bridge](watrous_bridge.md).
