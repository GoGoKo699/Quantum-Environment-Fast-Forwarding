# Centering a commuting jump count

We use the phase-referenced forward oracle and half diamond convention in [model.md](model.md). The Hamiltonian is zero. The input system may be entangled with an arbitrary reference, and only the field is returned. The accuracy-dependent upper bounds below are stated for $`0\lt \epsilon\leq1/2`$.

## One unitary jump

Let $`L=\sqrt{\lambda}\,U`$ and $`\mu=\lambda t`$. In the uniform temporal-mode number code, the exact isometry is

```math
\begin{aligned}
V_\mu|\psi\rangle
&=\sum_{n=0}^{\infty}\sqrt{p_\mu(n)}\,
U^n|\psi\rangle\otimes|n\rangle,\\
p_\mu(n)&=e^{-\mu}\frac{\mu^n}{n!}.
\end{aligned}
\qquad\text{(C1)}
```

For any input $`\rho_{SR}`$, the field-reference output has blocks

```math
\begin{aligned}
&\bigl[(\Gamma_\mu\otimes\mathrm{id}_R)(\rho_{SR})\bigr]_{n,m}\\
&\quad=\sqrt{p_\mu(n)p_\mu(m)}\,
\mathrm{Tr}_S
\left[
(U^n\otimes I_R)\rho_{SR}(U^{-m}\otimes I_R)
\right].
\end{aligned}
\qquad\text{(C2)}
```

The occurrence of $`U^{-m}`$ in this formula is a bra-side adjoint, not an inverse-oracle requirement.

### Centering lemma

Choose integers $`0\leq a\leq b`$, let
$`A=\{a,\ldots,b\}`$, and write $`P_A=\sum_{n\in A}p_\mu(n)\gt 0`$.
The normalized truncated isometry is

```math
V_A|\psi\rangle
=\sum_{n=a}^{b}\sqrt{\frac{p_\mu(n)}{P_A}}\,
U^n|\psi\rangle\otimes|n\rangle.
\qquad\text{(C3)}
```

Define

```math
\widehat V_A|\psi\rangle
=\sum_{n=a}^{b}\sqrt{\frac{p_\mu(n)}{P_A}}\,
U^{n-a}|\psi\rangle\otimes|n\rangle.
\qquad\text{(C4)}
```

Then $`V_A=(U^a\otimes I)\widehat V_A`$. For every reference-assisted input,

```math
\begin{aligned}
&\mathrm{Tr}_S
\left[(V_A\otimes I_R)\rho_{SR}(V_A^\dagger\otimes I_R)\right]
\\
&\quad=\mathrm{Tr}_S
\left[(\widehat V_A\otimes I_R)\rho_{SR}
(\widehat V_A^\dagger\otimes I_R)\right].
\end{aligned}
\qquad\text{(C5)}
```

This is invariance of the partial trace under a unitary acting only on the discarded system. It holds for mixed and entangled inputs. Thus the truncated field channel can be implemented with $`b-a`$ forward queries. Prepare the amplitudes in (C4), and, for each $`j=1,\ldots,b-a`$, apply $`U`$ conditioned on $`n\geq a+j`$. The number of active queries on branch $`n`$ is exactly $`n-a`$.

This circuit does not simulate the final system jointly with the field. Its system factor has been changed by the common $`U^{-a}`$, expressed here without ever implementing that inverse.

### Reference-uniform truncation error

For any purified input $`|\psi\rangle_{SR}`$,

```math
\langle\psi|(V_\mu^\dagger V_A\otimes I_R)|\psi\rangle
=\sqrt{P_A}.
\qquad\text{(C6)}
```

The two pure joint outputs therefore have trace distance $`\sqrt{1-P_A}`$. Taking the partial trace over the system cannot increase it. Purifying a mixed input gives the same conclusion, and hence

```math
d_\diamond(\Gamma_\mu,\Gamma_A)\leq \sqrt{1-P_A}.
\qquad\text{(C7)}
```

No input-dependent success probability or postselection is used. The algorithm directly prepares the normalized truncated amplitudes.

### Explicit concentration window

For $`0\lt \epsilon\leq1/2`$ and $`\mu\gt 0`$, set

```math
\begin{aligned}
x&=\log\frac{8}{\epsilon^2},\qquad
d=\sqrt{2\mu x},\\
a&=\max\{0,\lfloor\mu-d\rfloor\},\\
b&=\lceil\mu+d+2x\rceil.
\end{aligned}
\qquad\text{(C8)}
```

If $`N\sim\mathrm{Pois}(\mu)`$, then

```math
\begin{aligned}
\Pr(N\lt a)+\Pr(N\gt b)&\leq 2e^{-x}=\epsilon^2/4,\\
b-a&\leq 2\sqrt{2\mu x}+2x+2.
\end{aligned}
\qquad\text{(C9)}
```

For completeness, the Poisson moment-generating function gives
$`\log\mathbb E e^{s(N-\mu)}=\mu(e^s-1-s)`$.
For $`0\lt s\lt 1`$,
$`e^s-1-s\leq s^2/[2(1-s)]`$, and Chernoff's bound gives
$`\Pr(N-\mu\geq v)\leq\exp[-v^2/(2(\mu+v))]`$.
Taking $`v=d+2x`$ proves the upper-tail claim. For the lower tail,
$`e^{-s}-1+s\leq s^2/2`$ gives
$`\Pr(N-\mu\leq-d)\leq e^{-d^2/(2\mu)}`$ when $`d\leq\mu`$; otherwise the relevant nonnegative-count event is empty.
The integer rounding in (C8) only enlarges the retained interval.

Equations (C7)–(C9) allocate error at most $`\epsilon/2`$ to truncation. Preparing the count-amplitude state to trace distance at most $`\epsilon/2`$ gives total error at most $`\epsilon`$. The query bound is

```math
q=O\!\left(
\sqrt{\mu\log(1/\epsilon)}
+\log(1/\epsilon)+1
\right).
\qquad\text{(C10)}
```

The $`\mu=0`$ output is vacuum and needs no queries. The same is true whenever one deliberately uses the vacuum approximation and its exact error bound is sufficient; (C10) is a general upper bound, not an optimal formula at very small $`\mu`$.

## Commuting unitary jumps

Suppose $`[U_j,U_k]=0`$ for all pairs, and put $`\mu_j=\lambda_jt`$. Let $`f_t`$ be the uniform temporal mode in each bath. Every trajectory with a fixed vector of counts $`\mathbf n=(n_1,\ldots,n_m)`$ applies the same product $`\prod_jU_j^{n_j}`$. Summing its time orders gives the exact product-mode isometry

```math
V_t|\psi\rangle
=\sum_{\mathbf n\in\mathbb N^m}
\left(\prod_j\sqrt{p_{\mu_j}(n_j)}\right)
\left(\prod_jU_j^{n_j}\right)|\psi\rangle
\otimes|\mathbf n\rangle.
\qquad\text{(C11)}
```

Here $`|\mathbf n\rangle`$ denotes $`\bigotimes_j|n_j\rangle_{f_t,j}`$.
The counts are independent Poisson variables. This product code is local across baths.

Choose count windows $`A_j=[a_j,b_j]`$. On their product, commutativity gives

```math
\prod_jU_j^{n_j}
=
\left(\prod_jU_j^{a_j}\right)
\left(\prod_jU_j^{n_j-a_j}\right).
\qquad\text{(C12)}
```

The first factor acts only on the discarded system and cancels as in (C5). Preparing the independent truncated count states and applying the second factor costs
$`\sum_j(b_j-a_j)`$ individual forward controlled-unitary queries.

Omit channels with $`\mu_j=0`$, and let $`m_+`$ be the remaining number. Taking
$`x=\log(8m_+/\epsilon^2)`$ in each window yields a total omitted probability at most $`\epsilon^2/4`$ by the union bound. Therefore

```math
q=
O\!\left(
\sum_{j:\mu_j\gt 0}\sqrt{\mu_j\log(m_+/\epsilon)}
+m_+\log(m_+/\epsilon)+m_+
\right).
\qquad\text{(C13)}
```

Equivalently, the square-root term is at most
$`O(\sqrt{m_+\Lambda t\log(m_+/\epsilon)})`$.
This is an upper bound with explicit dependence on the number of fields. No optimality in $`m_+`$ is claimed.

The amplitudes can be prepared field by field. Allocate total synthesis error $`\epsilon/2`$, for example by giving each field error $`\epsilon/(2m_+)`$. A direct compiled finite-list implementation costs the query-window size times logarithmic factors in the count, number of fields, and precision. The construction and its classical storage cost are specified in [resources.md](resources.md).

## Constant-error optimality for one jump

The time dependence of (C10) is optimal for one unknown jump. Take a qubit,
$`U_\theta=e^{-i\theta Z}`$, and input $`|0\rangle`$. Equation (C1) makes the field a coherent state

```math
|\alpha_\theta\rangle,\qquad
\alpha_\theta=\sqrt{\mu}\,e^{-i\theta}.
\qquad\text{(C14)}
```

For $`\theta=\mu^{-1/2}`$ and $`\mu\geq1`$,

```math
\begin{aligned}
&D\!\left(
|\alpha_0\rangle\langle\alpha_0|,
|\alpha_\theta\rangle\langle\alpha_\theta|
\right)\\
&\quad=
\sqrt{1-\exp[-4\mu\sin^2(\theta/2)]}
\geq
\sqrt{1-e^{-4/\pi^2}}.
\end{aligned}
\qquad\text{(C15)}
```

The inequality uses $`\sin(\theta/2)\geq\theta/\pi`$.
The controlled-oracle distance satisfies
$`\|C(U_\theta)-C(I)\|=2\sin(\theta/2)\leq\theta`$.
A query-by-query hybrid bounds the trace distance between the outputs of any $`q`$-query procedure by $`q\theta`$. If that procedure approximates both field outputs to trace distance $`\epsilon`$, its two outputs must be separated by the right-hand side of (C15) minus $`2\epsilon`$. Thus $`q=\Omega(\sqrt{\mu})`$ for any fixed $`\epsilon`$ below half that constant.

The two unitary oracles have determinant one. This lower bound does not use an unspecified global phase of an otherwise identical unitary. The microscopic coupling phases are nevertheless fixed, as required by the field-output task.

## Relation to Hamiltonian twirling

The Poisson representation of reduced unitary-jump dynamics and purified twirling constructions already appear in the literature. Gao, Ji, and Liu [GJL26] analyze Hamiltonian-twirling simulation, including compound-Poisson system dynamics and lower bounds, and discuss Gaussian phase-estimation constructions. The present algebraic step is the removal of a common system unitary after retaining the complementary output. Its consequence is a forward-query cost controlled by a count window. The noncommuting observer construction shows why this argument does not extend to arbitrary jump families.

## References

- **[GJL26]** M. Gao, Z. Ji, and C. Liu, “Lévy–Khintchine Structure Enables Fast-Forwardable Lindbladian Simulation,” [arXiv:2511.10253v2](https://arxiv.org/abs/2511.10253v2), especially Secs. III–IV and Appendices C.3 and D.2; *Physical Review Letters* **137**, 160405 (2026), [DOI](https://doi.org/10.1103/qy4b-gzlq). The comparison here is to the inspected arXiv version.
