# Which output carries the computational cost?

The same stochastic dynamics can define different algorithmic tasks. The reduced system retains the mean accumulated rotation, while the single-jump field can lose a common system rotation after that system is discarded. Count fluctuations then control its query cost. A noncommuting observer records where it was inserted among the main jumps, preserving information that a count-window shift cannot remove.

These comparisons use the phase-referenced controlled-unitary oracle and half diamond convention in [model.md](model.md). The specified physical coupling has $`H=0`$. Exact query constructions are in [centered_environment.md](centered_environment.md) and [noncommuting_observer.md](noncommuting_observer.md); [resources.md](resources.md) distinguishes digital and physical output costs.

## Number dephasing removes all single-jump field information

For one unitary jump $`L=\sqrt{\lambda}\,U`$, put $`\mu=\lambda t`$. In the uniform temporal-mode number code, the field/reference blocks are

```math
\left[
(\Gamma_\mu\otimes\mathrm{id}_R)(\rho_{SR})
\right]_{n,m}
=
\sqrt{p_\mu(n)p_\mu(m)}
\mathrm{Tr}_S
\left[
(U^n\otimes I_R)\rho_{SR}(U^{-m}\otimes I_R)
\right].
\tag{P1}
```

Let $`\Delta_{\mathrm{num}}`$ dephase this complete number basis. On its diagonal,

```math
\mathrm{Tr}_S
\left[
(U^n\otimes I_R)\rho_{SR}(U^{-n}\otimes I_R)
\right]
=\rho_R.
\tag{P2}
```

Consequently,

```math
\left[
(\Delta_{\mathrm{num}}\circ\Gamma_\mu)
\otimes\mathrm{id}_R
\right](\rho_{SR})
=
\left(\sum_{n=0}^{\infty}p_\mu(n)|n\rangle\langle n|\right)
\otimes\rho_R.
\tag{P3}
```

The count is Poisson, independent of the input and the unknown unitary, and it is uncorrelated with the original reference marginal. The dephased encoded field can therefore be generated with zero unknown-unitary queries. A finite count cutoff with omitted probability $`\delta`$, with that probability assigned to a fixed fallback count, gives half diamond error at most $`\delta`$.

For commuting jumps, dephasing the complete vector of uniform-mode photon numbers gives the analogous product of independent Poisson distributions tensored with $`\rho_R`$. This is not a statement about dephasing only the total count of several fields.

For general noncommuting jumps, a fixed photon-count sector still contains temporal and word degrees of freedom. Dephasing the total count, or even the count in every bath, need not erase those coherences. The observer witness uses exactly one observer photon and exploits coherence between its possible emission times. A fully time-resolved classical trajectory record is independent of the unitary jumps, but count-sector dephasing is a weaker operation.

## Reduced system output has linear query complexity in the same model

The reduced system channel for the same jump is

```math
\Phi_{U,\mu}(\rho)
=\sum_{n=0}^{\infty}p_\mu(n)\,U^n\rho U^{-n}.
\tag{P4}
```

Take $`U_\theta=e^{-i\theta Z}`$ and input $`|+\rangle`$. The off-diagonal entry is multiplied by

```math
z_\theta
=\exp\!\left[\mu(e^{-2i\theta}-1)\right].
\tag{P5}
```

For $`\mu\geq\pi`$, choose

```math
\theta_\mu=\frac12\arcsin\frac{\pi}{\mu},
\qquad
a=\mu-\sqrt{\mu^2-\pi^2}.
\tag{P6}
```

Then $`0\leq a\leq\pi`$, and $`z_{\theta_\mu}=-e^{-a}`$. The two system outputs for $`U=I`$ and $`U=U_{\theta_\mu}`$ are

```math
\rho_0=\frac12(I+X),\qquad
\rho_1=\frac12(I-e^{-a}X).
\tag{P7}
```

Their trace distance and oracle distance obey

```math
D(\rho_0,\rho_1)=\frac{1+e^{-a}}2\geq\frac12,
\qquad
\|C(U_{\theta_\mu})-C(I)\|
\leq\theta_\mu\leq\frac{\pi^2}{4\mu}.
\tag{P8}
```

The query hybrid argument therefore gives

```math
q\geq
\frac{4(1/2-2\epsilon)}{\pi^2}\,\mu
\tag{P9}
```

for a simulator with half diamond error at most $`\epsilon<1/4`$ on both inputs. This lower bound uses the same controlled-$`U`$ access as the centered field algorithm.

For the upper bound, sample $`N\sim\mathrm{Pois}(\mu)`$, apply $`U^N`$, and keep the system. The exact algorithm has expected query count $`\mu`$. To obtain a worst-case bound, choose $`N_{\max}`$ with Poisson tail probability $`\delta`$, and use the identity channel on the omitted tail. The resulting channel is

```math
\widetilde\Phi
=\sum_{n=0}^{N_{\max}}p_\mu(n)\mathrm{Ad}_{U^n}
+\delta\,\mathrm{id}.
\tag{P10}
```

It has half diamond error at most $`\delta`$, because the tail is a mixture of channels with total weight $`\delta`$. A Poisson cutoff of size $`O(\mu+\log(1/\epsilon)+1)`$ suffices, with an error allocation for finite-precision classical sampling. At fixed error, the worst-case query complexity is therefore $`\Theta(\mu)`$.

This reduced-system scaling is established in the Hamiltonian-twirling and compound-Poisson simulation literature [GJL26]. The short argument above fixes the comparison in the controlled-unitary model used here. It is a baseline, not a new reduced-dynamics result.

## Zero explicit Hamiltonian does not remove coherent drift

The condition $`H=0`$ specifies one microscopic representation. It does not mean that the generator has no coherent first-order drift. With
$`\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\}`$, direct expansion gives

```math
\mathcal D[U]
=
\mathcal D[U-I]
-i\left[
\frac{i}{2}(U-U^\dagger),\,\cdot
\right].
\tag{P11}
```

For $`U_\theta=e^{-i\theta X}`$, separating its identity and Pauli parts yields the more specific exact identity

```math
\mathrm{Ad}_{U_\theta}-\mathrm{id}
=
-i\left[
\frac{\sin(2\theta)}2X,\,\cdot
\right]
+\sin^2\theta\,
\left(\mathrm{Ad}_X-\mathrm{id}\right).
\tag{P12}
```

Thus the leading drift is generated by $`\theta X+O(\theta^3)`$, while the dissipative rate in this representation is $`O(\theta^2)`$.

At the hard observer value
$`\theta_t=\tfrac12\arcsin(2\pi/t)`$, the Hamiltonian in (P12) is exactly $`(\pi/t)X`$. The Pauli-dissipation rate is
$`(1-\sqrt{1-4\pi^2/t^2})/2=O(t^{-2})`$.
Over time $`t`$, the main jumps can therefore produce a finite coherent rotation while their fluctuation contribution in this representation vanishes with $`t`$. The known observer has rate $`1/t`$, so its integrated observation strength remains finite. This explains why the hard family can expose a coherent drift through a weak output field.

Equations (P11) and (P12) are identities of the reduced generator. Shifting a jump by an identity changes the specified field dilation. In particular, a displacement depending on the unknown $`\theta`$ is not a free oracle-independent encoding change. The simulation task and its access model remain those of the original coupling $`L=U_\theta`$, with the known observer $`t^{-1/2}Z`$.

## Reference

- **[GJL26]** M. Gao, Z. Ji, and C. Liu, “Lévy–Khintchine Structure Enables Fast-Forwardable Lindbladian Simulation,” *Physical Review Letters* **137**, 160405 (2026). [DOI](https://doi.org/10.1103/qy4b-gzlq), [arXiv:2511.10253v2](https://arxiv.org/abs/2511.10253v2), Secs. III–IV and Appendices C.3 and D.2.
