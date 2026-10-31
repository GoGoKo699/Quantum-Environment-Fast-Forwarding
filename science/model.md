# Model: a specified vacuum output field

The input is a finite-dimensional quantum system $`S`$, a horizon $`t\geq 0`$, and unitary jump operators with known rates,

```math
\begin{aligned}
L_j&=\sqrt{\lambda_j}\,U_j,\qquad\lambda_j\geq0,\\
\Lambda&=\sum_{j=1}^{m}\lambda_j,\qquad H=0.
\end{aligned}
\qquad\text{(M1)}
```

The associated system generator is

```math
\mathcal L(\rho)=\sum_{j=1}^{m}\lambda_j
\bigl(U_j\rho U_j^\dagger-\rho\bigr).
\qquad\text{(M2)}
```

Each jump couples to a separate bosonic field initially in vacuum. The coupling phases and the field labels are part of the input model. In the Hudson–Parthasarathy convention with identity scattering, the joint unitary satisfies

```math
d\mathsf U_s=
\left[
\sum_j\left(L_j\,dB_j^\dagger(s)-L_j^\dagger\,dB_j(s)\right)
-\frac12\sum_jL_j^\dagger L_j\,ds
\right]\mathsf U_s.
\qquad\text{(M3)}
```

The vacuum input defines an isometry $`V_t:S\to S\otimes\mathcal F_t`$, where
$`\mathcal F_t=\bigotimes_j\mathcal F(L^2([0,t]))`$. The field-output channel is

```math
\Gamma_t(\rho)=\mathrm{Tr}_S[V_t\rho V_t^\dagger].
\qquad\text{(M4)}
```

The condition $`H=0`$ fixes this microscopic representation; it does not exclude coherent drift in another representation of the same reduced generator. The [interpretation](interpretation.md#zero-explicit-hamiltonian-does-not-remove-coherent-drift) gives the exact identity for the hard qubit family.

The input state may be entangled with an untouched reference. The target keeps the emitted field and discards the final system. It therefore differs from both the reduced system channel and the joint system-field isometry.

Equations (M3) and (M4) use the vacuum input-output construction of Gough, James, and Nurdin [GJN14, Secs. 2–3, Eqs. (1), (2), and (8)]. The expansions below are its specialization to unitary jumps.

## Oracle and accuracy conventions

An unknown unitary is supplied through its phase-referenced controlled oracle,

```math
C(U)=|0\rangle\langle0|\otimes I+
|1\rangle\langle1|\otimes U.
\qquad\text{(M5)}
```

One use of this oracle counts as one query. Conditions computed from known registers can be attached to its control. The centered algorithm uses forward queries only. The lower bounds remain valid if controlled inverse queries are also available. For several unknown jumps, individual controlled oracles and a coherent SELECT oracle are different access models. Any use of SELECT is stated explicitly.

The phase convention is necessary. Replacing $`U_j`$ by $`e^{i\phi_j}U_j`$ preserves (M2), but applies a photon-number phase rotation to the corresponding output field. A reduced Lindbladian specified only up to this freedom does not determine (M4). An uncontrolled unitary oracle does not, by itself, supply (M5).

For channels with the same output space, the error convention throughout is half diamond distance,

```math
d_\diamond(\Phi,\Psi)
=\frac12\|\Phi-\Psi\|_\diamond
=\frac12\sup_{\rho_{SR}}
\left\|
\bigl[(\Phi-\Psi)\otimes\mathrm{id}_R\bigr](\rho_{SR})
\right\|_1.
\qquad\text{(M6)}
```

The supremum can be taken over a reference of dimension $`\dim S`$. For a digital output with a declared isometric embedding $`J`$ into the physical field, its channel $`\mathcal A`$ is compared with $`\Gamma_t`$ through
$`d_\diamond(\rho\mapsto J\mathcal A(\rho)J^\dagger,\Gamma_t)`$.
Every embedding used below is independent of the unknown unitary oracles.

Known rates and times are classical inputs with a finite description, or are specified to sufficient classical precision. State preparation, arithmetic, and gate synthesis are charged separately from oracle calls. There is no QRAM or unit-cost arbitrary-amplitude-loading assumption.

## Exact trajectory expansion

If $`t=0`$ or $`\Lambda=0`$, the output is vacuum and requires no queries. The trajectory formulas and uniform temporal modes below assume $`t\gt 0`$; the normalized label probabilities additionally assume $`\Lambda\gt 0`$.

Since $`\sum_jL_j^\dagger L_j=\Lambda I`$, the no-jump evolution is the scalar $`e^{-\Lambda s/2}`$. Let
$`\Delta_N(t)=\{0\lt s_1\lt \cdots\lt s_N\lt t\}`$, and let
$`w=(j_1,\ldots,j_N)`$ record the jump labels in chronological order. The vacuum expansion is

```math
\begin{aligned}
V_t|\psi\rangle
&=e^{-\Lambda t/2}
\sum_{N=0}^{\infty}\ \sum_{w\in[m]^N}
\left(\prod_{k=1}^{N}\sqrt{\lambda_{j_k}}\right)\\
&\quad{}\times\int_{\Delta_N(t)}
U_{j_N}\cdots U_{j_1}|\psi\rangle
\otimes|\mathbf s,w\rangle\,d^N\mathbf s .
\end{aligned}
\qquad\text{(M7)}
```

The field kets in this integral are delta normalized in ordered times. Define the normalized field states

```math
|N,w\rangle_{\mathcal F}
=\sqrt{\frac{N!}{t^N}}
\int_{\Delta_N(t)}|\mathbf s,w\rangle\,d^N\mathbf s ,
\qquad\text{(M8)}
```

with the vacuum convention when $`N=0`$. States with different total counts or chronological label words are orthonormal: their time-label configurations have disjoint support, except on sets of measure zero.

For $`\Lambda\gt 0`$, put $`p_j=\lambda_j/\Lambda`$ and $`\mu=\Lambda t`$. Then

```math
\begin{aligned}
V_t|\psi\rangle
&=\sum_{N=0}^{\infty}\sqrt{\mathrm{Pois}_{\mu}(N)}
\sum_{w\in[m]^N}\sqrt{\prod_{k=1}^{N}p_{j_k}}\\
&\quad{}\times
U_{j_N}\cdots U_{j_1}|\psi\rangle
\otimes|N,w\rangle_{\mathcal F}.
\end{aligned}
\qquad\text{(M9)}
```

Equation (M9) defines a fixed isometry $`J_t`$ from a digital count-and-word space into the full field. It involves no time-grid approximation.

## Which output encoding is being simulated?

For a single jump, all ordered trajectories with $`N`$ events apply the same $`U^N`$. Their field state is the $`N`$-photon state of the normalized uniform temporal mode $`f_t(s)=t^{-1/2}`$. Thus a photon-number register is an exact encoding of the field. For commuting jumps, the corresponding code is the tensor product of one uniform-mode number register per field.

For noncommuting jumps, the exact code (M8) retains the chronological label word. Its embedding into the physical field generally does not factor across baths. Deleting one label register, or deleting occurrences of a bath label, does not implement a physical partial trace over that bath. Even a word with one photon in each of two fields has an ordering step function in its two time coordinates.

The full-field query upper bound uses (M9) in this exact global code. The observer lower bound uses a physical field measurement, whose exact finite-register implementation is derived separately. A reduced observer state requires either an explicit channel implementing the physical partial trace in the chosen code, or a product code across baths. No such channel is obtained merely by renaming or deleting word registers.

An encoding is a representation of a state, not a proposal to emit its photons. The number-register algorithm may represent a field with mean photon number of order $`t`$ using logarithmically many qubits. No statement here reduces the optical energy, physical emission time, or cost of an arbitrary field decoder. The gate bound for the centered algorithm refers to the count code. Converting that output to a word list can require a number of output registers proportional to the mean photon count, even though the conversion uses no unknown-unitary queries.

## Counting records

For unitary jumps, the norm of every conditional system trajectory is independent of its label word and times. Consequently, direct time-resolved photon counting gives independent Poisson point processes of rates $`\lambda_j`$, regardless of the $`U_j`$ and the input state. Coherent field output retains off-diagonal matrix elements between trajectories. These are the information used by the results below.

## References

- **[GJN14]** J. E. Gough, M. R. James, and H. I. Nurdin, “Quantum Trajectories for a Class of Continuous Matrix Product Input States,” *New Journal of Physics* **16**, 075008 (2014). [DOI](https://doi.org/10.1088/1367-2630/16/7/075008), [arXiv:1404.5699v1](https://arxiv.org/abs/1404.5699v1).
