# A weak observer with a linear query lower bound

Consider a qubit with zero Hamiltonian and two unitary jumps,

```math
\begin{aligned}
L_1&=U_\theta=e^{-i\theta X},\qquad L_2=t^{-1/2}Z,\\
\rho_0&=|0\rangle\langle0|,\qquad t\geq2\pi.
\end{aligned}
\qquad\text{(O1)}
```

The unknown input is the phase-referenced controlled oracle for $`U_\theta`$. The second jump and its rate $`1/t`$ are known. Both fields start in vacuum. The total observation time is $`t`$, so the mean photon number in the observer field is exactly one for every $`\theta`$. This is a horizon-indexed family of generators. The second rate is not held fixed as $`t`$ increases.

Let $`\rho_\theta^{\mathrm{obs}}(t)`$ be the physical state of the second field after tracing out the qubit and the first field. We use the bounded, photon-number-conserving projector

```math
P_f=|1_f\rangle\langle1_f|,\qquad
f(s)=t^{-1/2}\ \ (0\lt s\lt t).
\qquad\text{(O2)}
```

Here $`|1_f\rangle`$ means exactly one photon in the uniform temporal mode and vacuum in every orthogonal observer mode. The associated event is more restrictive than “one observer photon.”

## Exact probability of the temporal-mode event

Project the observer field onto its one-photon sector. For a fixed main-field photon history, let $`N_s`$ be the number of main jumps before $`s`$, and $`N=N_t`$. If the observer photon is emitted at $`s`$, the system amplitude is

```math
U_\theta^{N-N_s}Z U_\theta^{N_s}|0\rangle.
\qquad\text{(O3)}
```

Tracing out the main field pairs identical main-photon histories on the bra and ket. For $`s\leq u`$, the overlap of the two system amplitudes is

```math
\begin{aligned}
&\langle0|
U_\theta^{-N_u}Z
U_\theta^{N_u-N_s}Z
U_\theta^{N_s}|0\rangle\\
&\hspace{1cm}
=\langle0|U_\theta^{-2(N_u-N_s)}|0\rangle
=\cos\!\left(2\theta(N_u-N_s)\right).
\end{aligned}
\qquad\text{(O4)}
```

This uses $`ZU_\theta Z=U_\theta^\dagger`$. The increment $`N_u-N_s`$ is Poisson with mean $`u-s`$. The two observer jump amplitudes contribute $`1/t`$, while observer no-jump survival on the two branches contributes $`e^{-1}`$. Therefore the exact one-photon kernel is

```math
\langle1_s|\rho_\theta^{\mathrm{obs}}(t)|1_u\rangle
=\frac{e^{-1}}{t}
\mathrm{Re}
\exp\!\left[
|s-u|\left(e^{i2\theta}-1\right)
\right].
\qquad\text{(O5)}
```

Its diagonal integrates to $`e^{-1}`$, as required by the observer's Poisson count of mean one.

Integrating (O5) against the uniform mode gives

```math
\begin{aligned}
p_\theta(t)
&=\mathrm{Tr}\!\left[P_f\rho_\theta^{\mathrm{obs}}(t)\right]\\
&=\frac{2e^{-1}}{t^2}
\mathrm{Re}\int_0^t
(t-v)e^{v(e^{i2\theta}-1)}\,dv\\
&=e^{-1}F(z),\qquad
F(z)=2\mathrm{Re}\frac{e^z-1-z}{z^2},\qquad
z=t(e^{i2\theta}-1),
\end{aligned}
\qquad\text{(O6)}
```

where $`F(0)=1`$ by continuity. In particular, $`p_0(t)=e^{-1}`$.

## A uniform constant gap

Set $`\beta=2\pi`$ and choose

```math
\theta_t=\frac12\arcsin\frac{\beta}{t},\qquad
a=t-\sqrt{t^2-\beta^2}.
\qquad\text{(O7)}
```

Then $`0\leq a\leq\beta`$ and $`z=-a+i\beta`$. Since $`e^{i\beta}=1`$, the probability factor becomes

```math
F(-a+i\beta)
=2\left[
\frac{a}{a^2+\beta^2}
+\frac{(1-e^{-a})(\beta^2-a^2)}
{(a^2+\beta^2)^2}
\right]
\leq\frac1\beta+\frac2{\beta^2}.
\qquad\text{(O8)}
```

The first term is bounded using $`2a\beta\leq a^2+\beta^2`$. The second uses $`0\leq1-e^{-a}\leq1`$ and $`0\leq a\leq\beta`$. It follows that

```math
p_0(t)-p_{\theta_t}(t)
\geq
g:=
e^{-1}\left(1-\frac1{2\pi}-\frac1{2\pi^2}\right)
=0.2906926194\ldots.
\qquad\text{(O9)}
```

Because $`P_f`$ is a projector, (O9) is immediately a trace-distance lower bound for the two observer states. It is also a lower bound for the full two-field outputs, by monotonicity under the physical partial trace.

This witness uses coherence between different emission times within one photon-number sector. It does not require interference between vacuum and one-photon sectors, nor an unbounded field observable. Direct time-resolved photon-counting records remain independent of $`\theta`$.

## Query lower bound

The two controlled oracle inputs obey

```math
\|C(U_{\theta_t})-C(I)\|
=2\sin(\theta_t/2)
\leq\theta_t
\leq\frac{\pi^2}{2t}.
\qquad\text{(O10)}
```

The last inequality follows from $`\arcsin x\leq\pi x/2`$ on $`[0,1]`$.
In a $`q`$-query circuit, replace the oracle calls one at a time. Each replacement changes the final state in trace distance by at most the operator-norm distance in (O10), even with ancillary systems. Contractivity under the known intervening channels and the triangle inequality give a total change at most $`q\pi^2/(2t)`$. This is the usual quantum query hybrid argument [BBBV97]. Measurements and adaptive classical control can be purified, and controlled inverse queries have the same norm difference.

If a simulator has half diamond error at most $`\epsilon\lt g/2`$ for both inputs, its outputs have trace distance at least $`g-2\epsilon`$. Thus

```math
q\geq \frac{2(g-2\epsilon)}{\pi^2}\,t.
\qquad\text{(O11)}
```

The same bound holds for an algorithm whose only required output is a classical bit with acceptance probability within $`\epsilon`$ of $`p_\theta(t)`$. It therefore does not depend on a choice of digital field encoding. It also lower-bounds any full-field or reduced-observer simulator for which the stated measurement is available with no additional unknown-unitary queries.

For example, $`\epsilon=0.1`$ leaves a positive constant in (O11). The input system is one qubit, the observer jump is a known Pauli, and the observer emits one photon on average. The lower bound is a worst-case statement for the family (O1), comparing $`\theta=0`$ with $`\theta=\theta_t`$. It does not assert that every noncommuting family is hard, or that a fixed nonzero observer rate has this long-time behavior.

The obstruction comes from the observer's possible insertion positions. Conditional on $`n`$ main photons and one observer photon, all $`n+1`$ chronological positions occur coherently. In the family (O1), the corresponding system factors are $`U_\theta^{n-2k}Z`$. Factoring out the common $`U_\theta^n`$ leaves residual exponents $`-2k`$ spanning an interval of length $`2n`$. Concentration of the total main count does not concentrate this insertion position. The lower bound makes this failure of count centering operational.

## An exact finite-register implementation of the witness

The count-and-word code in [model.md](model.md) does not factor across the two fields. Nevertheless, $`P_f`$ has a simple exact effect in that code.

Restrict to $`n`$ photons in the main field and exactly one in the observer field. A word is determined by the observer position $`k\in\{0,\ldots,n\}`$, meaning that $`k`$ main photons precede it. Let $`|w_k\rangle_{\mathcal F}`$ be its normalized field state from (M8).

Write the ordered main-photon times as $`0\lt x_1\lt \cdots\lt x_n\lt t`$, set $`x_0=0`$, $`x_{n+1}=t`$, and define the gaps $`g_k=x_{k+1}-x_k`$. Projecting the observer coordinate onto $`f`$ sends $`|w_k\rangle_{\mathcal F}`$ to the main-field amplitude

```math
\sqrt{\frac{(n+1)!}{t^{n+2}}}\,g_k.
\qquad\text{(O12)}
```

Under the uniform measure on the ordered main-time simplex, the normalized gaps are Dirichlet distributed with all parameters equal to one. Their second moment follows by elementary integration:

```math
\mathbb E[g_kg_\ell]
=\frac{t^2(1+\delta_{k\ell})}{(n+1)(n+2)}.
\qquad\text{(O13)}
```

The simplex volume is $`t^n/n!`$. Combining (O12) and (O13), the exact pullback of $`I_{\mathrm{main}}\otimes P_f`$ is the effect

```math
\begin{aligned}
(E_n)_{k\ell}&=\frac{1+\delta_{k\ell}}{n+2},\\
E_n&=\frac{I+\mathbf J}{n+2}
=|u_n\rangle\langle u_n|
+\frac{I-|u_n\rangle\langle u_n|}{n+2},\\
|u_n\rangle&=\frac1{\sqrt{n+1}}\sum_{k=0}^{n}|k\rangle,
\end{aligned}
\qquad\text{(O14)}
```

where $`\mathbf J`$ is the all-ones matrix. The effect vanishes in sectors with any other observer count, and it is block diagonal in the main count $`n`$.

To measure (O14), project the position register onto $`|u_n\rangle`$. Accept on that outcome. Otherwise accept with the known probability $`1/(n+2)`$. Both steps have explicit finite-register circuits. No physical bath decoder or deletion of bath-labelled word registers is used.

## Matching upper bound for the one-bit task

Since the effect is block diagonal in both field counts, those counts can be sampled classically. The following uncapped procedure specifies the exact bit channel for an arbitrary input system state. Its finite implementation uses the conditioned count distribution described below.

1. With probability $`1-e^{-1}`$, output zero. This combines all observer counts other than one.
2. Otherwise sample $`n\sim\mathrm{Pois}(t)`$, and prepare the position register in $`|u_n\rangle`$.
3. At each slot $`j=0,\ldots,n`$, apply $`Z`$ to the system conditioned on $`k=j`$. Between adjacent slots apply $`U_\theta`$, for exactly $`n`$ oracle calls in total.
4. Discard the system and measure $`E_n`$ as described above.

The joint state before the last measurement is

```math
\frac1{\sqrt{n+1}}
\sum_{k=0}^{n}|k\rangle\,
U_\theta^{n-k}ZU_\theta^k|\psi\rangle.
\qquad\text{(O15)}
```

This is precisely the conditional system-word state for those field counts. The construction also respects an input reference.

For a worst-case query bound, choose $`n_{\max}`$ and sample the Poisson law conditioned on $`n\leq n_{\max}`$. Its finite list is computed by starting at the Poisson mode, applying the stable outward recurrence, and normalizing the retained weights. This avoids a separate calculation of the exponentially small factor $`e^{-t}`$.

Write $`\delta=\Pr(\mathrm{Pois}(t)\gt n_{\max})`$. The observer-one channel is a convex mixture of its normalized retained-count and omitted-count channels, with weights $`1-\delta`$ and $`\delta`$. Replacing this mixture by its retained-count channel changes half diamond distance by at most $`\delta`$. The observer-one branch has weight $`e^{-1}`$, so the total bit/reference channel error is at most $`e^{-1}\delta`$. This argument is uniform over input references because each normalized count-sector average is a channel.

A concrete error allocation takes $`\delta\leq\epsilon/4`$, bounds the combined error of all classical sampling and known coins by $`\epsilon/4`$, and allocates $`\epsilon/4`$ each to the uniform-position preparation and its final projection circuit. The elementary Poisson bound then gives $`n_{\max}=O(t+\log(1/\epsilon)+1)`$. The circuit errors can be bounded in operator norm uniformly over every sampled $`n\leq n_{\max}`$.

The count table, a uniform-position state, and the known coin require no QRAM. A direct compiled implementation has
$`O(n_{\max}\mathrm{polylog}(n_{\max}/\epsilon))`$ known-gate cost and uses $`O(\log(n_{\max}+1))`$ ancillary qubits beyond the input system. Classical compilation has the same count dependence, with the additional polynomial dependence on the input and arithmetic bit lengths specified in resources.md. Thus the one-bit task has $`\Theta(t)`$ query complexity at constant error, with an explicit efficient measurement in the encoded field model.

The count $`n`$ is sampled classically before the position circuit is compiled. Only the selected $`O(n+1)`$-rotation loader and its inverse are needed. The conditional known-gate bound is $`O((n+1)\mathrm{polylog}((n+2)/\epsilon))`$, which includes $`n=0`$, while the unknown-unitary query count is exactly $`n`$. No coherent or explicitly stored family of loaders for all $`n\leq n_{\max}`$ is assumed, so there is no hidden quadratic compilation table.

For the lower-bound input, a useful independent expression is

```math
\begin{aligned}
h_n(\theta)
&=\frac1{n+2}
\left[
1+\frac1{n+1}
\left|\sum_{k=0}^{n}e^{2ik\theta}\right|^2
\right],\\
p_\theta(t)
&=e^{-1}\sum_{n=0}^{\infty}
\mathrm{Pois}_t(n)\,h_n(\theta).
\end{aligned}
\qquad\text{(O16)}
```

It follows directly from (O14) and the Gram matrix of (O15), and agrees with the continuous-time expression (O6).

## References

- **[BBBV97]** C. H. Bennett, E. Bernstein, G. Brassard, and U. Vazirani, “Strengths and Weaknesses of Quantum Computing,” *SIAM Journal on Computing* **26**, 1510–1523 (1997). [DOI](https://doi.org/10.1137/S0097539796300933), [arXiv:quant-ph/9701001](https://arxiv.org/abs/quant-ph/9701001).
- The vacuum-field convention and trajectory expansion are fixed in [model.md](model.md), following Gough, James, and Nurdin [GJN14]. Equations (O4)–(O16) are explicit derivations in that model.
