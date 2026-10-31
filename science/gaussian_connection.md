# Exact relation to a Gaussian phase-clock purification

This connection identifies the complementary output obtained from an earlier Gaussian phase-clock construction. The [direct count-centering algorithm](centered_environment.md) establishes its query bound separately. The Gaussian purification is described by Gao, Ji, and Liu, arXiv:2511.10253v2, Section III, under “CV Quantum Phase Estimation.” The conversion to the specified Hudson–Parthasarathy vacuum output and the two-mode reduction below are derived here. The identities concern the output state; they do not alone supply a finite-gate implementation bound.

## A known change of representation fixes the field convention

Let $`H`$ be Hermitian and $`\tau>0`$. Write

```math
g_\tau(s)=(2\pi\tau)^{-1/4}e^{-s^2/(4\tau)},
\qquad
W_{H,\tau}|\psi\rangle
=\int_{\mathbb R}g_\tau(s)|s\rangle e^{-iHs}|\psi\rangle\,ds.
```

This is the coherent purification of Gaussian twirling with variance $`\tau`$. On an eigenvector of eigenvalue $`h`$, its clock wavefunction is $`f_h(s)=g_\tau(s)e^{-ihs}`$.

Fix the oscillator convention $`[q,p]=i`$, with vacuum momentum wavefunction
$`\langle p|0\rangle=\pi^{-1/4}e^{-p^2/2}`$.
Define a unitary change of representation $`\mathcal T_\tau`$ from the clock space $`L^2(\mathbb R,ds)`$ to the oscillator by

```math
\langle p|\mathcal T_\tau|f\rangle
=(2\tau)^{1/4}f\!\left(\sqrt{2\tau}\,p\right).
```

The Jacobian makes this map unitary. It depends only on $`\tau`$, and

```math
\langle p|\mathcal T_\tau|f_h\rangle
=\pi^{-1/4}e^{-p^2/2}e^{-i\sqrt{2\tau}\,hp}
=\langle p|\sqrt{\tau}\,h\rangle.
```

The last equality follows from
$`|\alpha\rangle=e^{-i\sqrt2\alpha p}|0\rangle`$ for real $`\alpha`$.
Thus the conversion has no unknown-eigenvalue-dependent phase. If the physical clock is initially described in a coordinate representation, the specified map includes a known Fourier change of representation and the displayed rescaling.

For the identity-scattering vacuum dilation with Hermitian jump $`L=H`$, zero explicit Hamiltonian, and duration $`\tau`$, an eigenvector of eigenvalue $`h`$ emits

```math
e^{-\tau h^2/2}
\sum_{n=0}^{\infty}
\frac{(\sqrt{\tau}\,h)^n}{\sqrt{n!}}\,|n\rangle
=|\sqrt{\tau}\,h\rangle
```

in the uniform temporal mode. Consequently, after applying $`\mathcal T_\tau`$ to the clock, $`W_{H,\tau}`$ is precisely this Hermitian-jump isometry in the specified mode convention. This is stronger than observing that both purifications produce the same reduced-system channel: the known field transformation has been exhibited.

## Two commuting Hermitian parts recover the unitary-jump complement

For a unitary $`U`$, put

```math
A=\frac{U+U^\dagger}{2},
\qquad
B=\frac{U-U^\dagger}{2i}.
```

These are commuting Hermitian operators. For a spectral projector $`P_\theta`$ of $`U`$ with eigenvalue $`e^{i\theta}`$, the two time-$`2t`$ Hermitian-jump isometries prepare

```math
P_\theta|\psi\rangle
\otimes|\sqrt{2t}\cos\theta\rangle
\otimes|\sqrt{2t}\sin\theta\rangle.
```

Apply the fixed passive two-mode unitary whose action on coherent amplitudes is

```math
\begin{pmatrix}\alpha_+\\\alpha_-\end{pmatrix}
=\frac1{\sqrt2}
\begin{pmatrix}1&i\\1&-i\end{pmatrix}
\begin{pmatrix}\alpha_A\\\alpha_B\end{pmatrix}.
```

Its matrix is unitary, and the resulting pair is

```math
|\sqrt t\,e^{i\theta}\rangle_+
\otimes|\sqrt t\,e^{-i\theta}\rangle_-.
```

For an arbitrary input $`\rho_{SR}`$, define

```math
\sigma_R^\theta
=\mathrm{Tr}_S
\!\left[(P_\theta\otimes I_R)\rho_{SR}
(P_\theta\otimes I_R)\right].
```

Tracing the final system removes terms with different spectral projectors. Tracing the minus mode then leaves

```math
\sum_\theta
\sigma_R^\theta\otimes
|\sqrt t\,e^{i\theta}\rangle
\langle\sqrt t\,e^{i\theta}|.
```

This is exactly the complementary output, together with the untouched reference, of the original unitary-jump isometry

```math
V_{U,t}|\psi\rangle
=\sum_{n=0}^{\infty}
\sqrt{e^{-t}t^n/n!}\,
U^n|\psi\rangle\otimes|n\rangle.
```

The tracing of the system is essential to this conclusion. The reduction establishes equality of the requested complementary channels on every input and reference.

## Algorithmic scope

The identity explains how the Gaussian phase-clock mechanism reaches this complementary-output task. It assumes coherent access to the required evolutions under $`A`$ and $`B`$, together with the indicated known clock transformations. Constructing these Hermitian parts from an unknown $`U`$ introduces $`U^\dagger`$ in the usual linear-combination description. A quantitative digital implementation additionally needs bounds for clock truncation, discretization, state preparation, and coherent Hamiltonian simulation. Those costs do not follow merely from equality of reduced-system channels.

The direct Poisson argument gives its forward-only oracle bound independently. The comparison therefore credits the existing Gaussian purification mechanism while keeping the specified oracle model and output guarantee explicit.

The spectral-mixture formula also explains the fixed-error square-root scale through ordinary phase estimation. For $`t\geq1`$ and $`0<\epsilon<1/2`$, estimate each eigenphase to circular error at most $`\delta=\epsilon/(4\sqrt t)`$ except with probability at most $`\epsilon/4`$, and prepare the corresponding known coherent state. For phase difference $`\Delta`$, the two coherent states have trace distance at most $`\sqrt t\,|\Delta|`$. The phase-estimation contribution to output error is therefore at most $`\epsilon/2`$, uniformly in the eigenphase and hence also for arbitrary input/reference mixtures. Allocate the remaining $`\epsilon/2`$ to known-state preparation. Standard controlled-unitary phase estimation with confidence amplification uses $`O((\sqrt t/\epsilon)\log(1/\epsilon))`$ forward queries; known preparation resources require separate accounting. This elementary comparison does not attain the logarithmic precision dependence of direct Poisson centering.

## Reference

M. Gao, Z. Ji, and C. Liu, “Lévy–Khintchine Structure Enables Fast-Forwardable Lindbladian Simulation,” *Physical Review Letters* **137**, 160405 (2026), DOI [10.1103/qy4b-gzlq](https://doi.org/10.1103/qy4b-gzlq). Inspected author version: [arXiv:2511.10253v2](https://arxiv.org/html/2511.10253v2), 27 January 2026, Section III, “CV Quantum Phase Estimation.”

For the standard phase-estimation primitive, see Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*](https://www.cs.umd.edu/~amchilds/qa/qa.pdf), revision 17 April 2025, Section 4.3. The conversion from its phase-estimation guarantee to a complementary-output error bound is the argument above.
