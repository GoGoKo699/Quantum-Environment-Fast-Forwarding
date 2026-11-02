# Field-only lower bound for two qubit reflections

The [reflection theorem](reflection_threshold.md) has a matching pair lower bound already on a qubit. A fixed mixing of the two physical bath labels turns their unknown angle into a photon-count signal.

## Fixed physical and oracle contract

Use the identity-scattering Hudson–Parthasarathy vacuum dilation on two
independent bosonic baths over $`[0,t]`$, with $`H=0`$ and phase-fixed jumps

```math
\begin{aligned}
R_\pm(\theta)&=\cos\theta\,Z\pm\sin\theta\,X,\\
L_1&=R_+(\theta)/\sqrt2,\qquad L_2=R_-(\theta)/\sqrt2.
\end{aligned}
```

Both supplied primitives are Hermitian involutions. Their rates are exactly
$`1/2`$, so the total rate is one for every value of the parameter. The simulator
receives the phase-referenced controlled SELECT oracle for this ordered pair;
the comparison permits inverse calls, which coincide with forward calls.
The final system is discarded and the full two-bath field is retained. The
physical-field embedding is the oracle-independent chronological-word
embedding specified in [the model](model.md#exact-trajectory-expansion), not an oracle-dependent output
relabeling. The lower bound needs no special input state and therefore applies
also to the stronger reference-preserving half-diamond task.

## Physical dark-count witness

Apply the fixed, time-local 50:50 beamsplitter between bath labels. Its second
quantization is a photon-number-preserving, oracle-independent field unitary.
Equivalently, change the bath coordinates by the real orthogonal matrix

```math
\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
```

The same HP evolution in these coordinates has bright and dark jumps

```math
L_b=(L_1+L_2)/\sqrt2=\cos\theta\,Z,\qquad
L_d=(L_1-L_2)/\sqrt2=\sin\theta\,X.
```

Consequently $`L_b^\dagger L_b=\cos^2\theta\,I`$ and
$`L_d^\dagger L_d=\sin^2\theta\,I`$. The marked dark count is exactly Poisson with mean
$`t\sin^2\theta`$, independently of the initial system state and of any untouched
reference. One rigorous derivation uses the count generating operator:

```math
\mathcal K_z(\rho)=\cos^2\theta\,Z\rho Z
 +z\sin^2\theta\,X\rho X-\rho.
```

Taking the trace gives

```math
\frac{d}{dt}\mathrm{Tr}e^{t\mathcal K_z}(\rho)
 =\sin^2\theta(z-1)\mathrm{Tr}e^{t\mathcal K_z}(\rho),
\qquad
\mathbb E z^{N_d}=e^{t\sin^2\theta(z-1)}.
```

Thus the field-only event “at least one dark photon” has probability

```math
p_\theta=1-e^{-t\sin^2\theta},\qquad p_0=0.
```

This test includes all temporal modes in the dark bath. It neither uses the
discarded system nor assumes a time-bin approximation. It needs coherence
between the two bath labels, which the physical beamsplitter accesses, but no
coherence measurement between distinct total-photon-number sectors.

## Oracle lower bound

For $`t\geq1`$, choose $`\theta=t^{-1/2}`$. Since $`\sin(x)/x`$ decreases on $`(0,1]`$,

```math
t\sin^2(t^{-1/2})\ge\sin^2 1,\qquad
p_\theta\ge g_d:=1-e^{-\sin^2 1}>0.
```

The operator norm distance of the two SELECT oracles, including an additional
coherent control, is

```math
\delta=\max_\pm\|R_\pm(\theta)-Z\|
=2\sin(\theta/2)\le\theta.
```

A query-by-query hybrid bounds the trace distance of the outputs of any
branchwise $`q`$-query algorithm by $`q\delta`$, including adaptive algorithms.
If it simulates both physical field channels within half-diamond error
$`\epsilon`$, applying the fixed field event and the triangle inequality yields

```math
q\delta\ge g_d-2\epsilon,\qquad
q\ge(g_d-2\epsilon)\sqrt t.
```

For every fixed $`\epsilon\lt g_d/2`$, this proves an $`\Omega(\sqrt t)`$ field-only
lower bound in dimension two. Combined with the separately justified routine
coherent word-reduction upper bound, it establishes the matching two-reflection
fixed-error exponent. The distinct [three-reflection converse](reflection_tree.md) uses a growing tree and photon-number coherence.

## Independent coherent-projector cross-check

For input $`|0\rangle`$, let $`|\alpha_t\rangle`$ be the physical product coherent state having
amplitude $`+1/\sqrt2`$ throughout $`[0,t]`$ in each original bath. The exact
trajectory expansion implies

```math
\langle\alpha_t|V_\theta|0\rangle
=e^{t[(R_++R_-)/2-I]}|0\rangle
=e^{-t(1-\cos\theta)}|0\rangle.
```

Its projector therefore has probability $`\exp[-2t(1-\cos\theta)]`$, equal to
one at $`\theta=0`$. This is a second field-only witness with a constant gap at
$`\theta=t^{-1/2}`$. The dark-count witness above has the cleaner physical
interpretation because its test preserves total photon number.

## Resource boundaries and attribution

The fixed field rotation and dark counting require zero unknown-reflection
queries. This is a query-complexity lower bound, not a gate or emission-time
bound. Applying a physical beamsplitter to a horizon-$`t`$ field, counting photons,
preparing a digital word code, producing an explicit photon list, converting
between encodings and emitting the physical field have separate costs.
The word-code embedding is an exact representation; it does not supply free
physical decoding. In the original chronological-word code the beamsplitter
acts as the known two-letter rotation on every photon label; explicitly
processing a length-$`N`$ word costs $`O(N)`$ such known label gates. Its action
cannot be replaced by deleting one original bath label.

The coherent trajectory expansion, covariance under a fixed bath rotation,
Poisson counting for scalar jump intensities and the query hybrid are standard
ingredients. The new calculation here is their specific field-only witness
for the pair of reflections, which survives tracing out the final system.
It must be credited separately from the inherited routine upper-bound lift.

## Numerical diagnostics

[check_reflection_pair.py](../verification/check_reflection_pair.py) compares the full tilted jump generator against the
Poisson generating function at real and complex test points; resolves photon
probabilities using a block count master equation; tests four qubit inputs and
an input entangled with an untouched reference; and checks the independent
coherent-projector formula against an exponential and a finite Poisson
word-average series. The JSON result records errors and dependency versions.
These finite checks supplement, and do not replace, the analytic proof above.
