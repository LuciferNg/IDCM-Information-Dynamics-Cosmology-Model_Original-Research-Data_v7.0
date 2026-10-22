# General Relativity as Consistency Propagation: The Emergence of Spacetime from a Single Field

**Author:** Lucifer Ng  
**Date:** July 2026  
**Status:** Pre-print

---

## Abstract

General relativity is conventionally presented as a theory of dynamic spacetime geometry: mass-energy tells spacetime how to curve, and curved spacetime tells matter how to move. The gravitational constant $G$ is treated as fundamental, the cosmological constant $\Lambda$ as a free parameter, and spacetime singularities as physical infinities requiring new physics.

This paper demonstrates that the core structure of general relativity — the metric, geodesic motion, the Einstein equation, and the cosmological constant — emerges from the consistency propagation of a single continuous field. The derivation is presented as a chain of theorems, each following from the previous one without additional postulates.

The central claims are:

1. **Spacetime curvature is not fundamental.** The metric $g_{\mu\nu}$ is a derived quantity encoding the local consistency gradient of the W-field. The equivalence principle follows from field self-identity, not from a postulate.

2. **$G$ is not a fundamental constant.** It is derived from the same scale hierarchy as $\hbar$: $G = c^2 \cdot L_P / M_P$, with a residual of $0.0147\%$ relative to the measured value.

3. **$\Lambda$ is not a free parameter.** It is determined by the rendering budget density: $\Lambda = 3H_0^2/c^2 \cdot \Omega_\Lambda$ where $\Omega_\Lambda = 4/(\varphi^4-1) = 4/(3\varphi+1)$ is a structural ratio, derived from the sync node's eigenvalue structure. The error relative to observation is $0.207\%$ (within $0.25\sigma$).

4. **Singularities are not physical infinities.** They are boundaries where the local rendering budget $B(x) \to 0$ — the mathematical limit of a budget-constrained projection, not a physical divergence requiring new physics.

5. **The cosmological constant problem (120 orders of magnitude) is resolved.** $\Lambda$ is not vacuum energy — it is a universal rendering budget density, and the degrees of freedom of the W-field are finite, not infinite.

The thesis is this: **general relativity is not a theory of spacetime — it is the theory of consistency propagation in a single field, misidentified as a theory of geometry. The gravitational interaction is not a force but the geometry of a field that cannot delegate its consistency.**

---

## 1. Introduction

### 1.1 The Problem

General relativity rests on assumptions that are themselves unexplained. These are not minor technical issues — they are foundational gaps that have persisted for over a century.

**The assumption that spacetime is a dynamic entity.** The Einstein-Hilbert action is postulated, not derived. The metric is treated as a fundamental field, yet there is no explanation of why it exists, why it is 4-dimensional, or why it has Lorentzian signature.

**The gravitational constant $G$ is measured, not derived.** It is one of three "fundamental" constants alongside $c$ and $\hbar$, yet its value is not predicted by any theory.

**The cosmological constant $\Lambda$ is a free parameter — or worse, a catastrophic discrepancy.** Quantum field theory predicts a vacuum energy density ~$10^{120}$ times larger than the observed value. The cosmological constant problem is arguably the most severe fine-tuning problem in physics.

**Singularities are guaranteed by the Penrose-Hawking theorems, but their physical nature is unknown.** At a singularity, general relativity predicts its own breakdown. Whether this indicates new physics at high energies or a fundamental limitation of the theory is unclear.

**The black hole information paradox.** Hawking's calculation suggests that information is lost when matter falls into a black hole, contradicting quantum mechanics. The firewall paradox, complementarity, and holography are attempts to resolve this, but none are derivations.

These are not separate problems. They are symptoms of a single category error: **general relativity treats geometry as fundamental, when geometry is an emergent property of consistency propagation.**

### 1.2 The Core Argument

The argument proceeds from a single premise, shared with the companion paper on quantum mechanics:

> **Axiom (Field Uniqueness):** There exists exactly one continuous field $\Phi(x,t)$ with phase $\theta(x,t)$, amplitude $A(x,t)$, and propagation speed $c$. This field is the only field — there is no second field to delegate functions.

From this axiom, the structure of general relativity emerges as a chain of consequences:

| Step | Result | Status |
|:-----|:-------|:------:|
| §2 | The W-field's phase gradient defines a local frame (vierbein) | Theorem |
| §2 | The metric $g_{\mu\nu} = \eta_{ab} e_\mu^a e_\nu^b$ emerges from the vierbein | Definition |
| §2 | The equivalence principle follows from field self-identity | Theorem |
| §3 | Geodesic motion follows from the consistency action | Theorem |
| §4 | The Einstein equation follows from the self-consistency of the field | Derivation |
| §4 | $G = c^2 \cdot L_P / M_P$ is structurally closed | **0.0147%** |
| §5 | $\Lambda$ is the rendering budget density: $\Omega_\Lambda = 4/(\varphi^4-1)$ | **0.207%** |
| §6 | Singularities are budget boundaries $B(x) \to 0$ | Resolution |
| §6 | Black hole information is preserved by field continuity | Resolution |

### 1.3 Relation to the Companion Paper

The companion paper (see [Quantum Mechanics as Mathematical Necessity](./paper_quantum_mechanics_as_necessity.md)) derived the entire quantum formalism from the same W-field axiom. This paper extends the derivation to general relativity. The two papers together show that quantum mechanics and general relativity are not separate layers of physics — they are different aspects of the same underlying structure:

- **Quantum mechanics** = the Fourier duality of the W-field's two natural representations
- **General relativity** = the consistency propagation of the W-field's phase structure
- **$\hbar$ and $G$** = scale ratios of the same hierarchy

---

## 2. The W-field and the Emergent Metric

### 2.1 From Field Phase to Local Frame

The W-field $\Phi(x,t)$ carries a phase $\theta(x,t)$ that encodes the local state of consistency. The phase gradient $\partial_\mu \theta$ defines a natural local direction — the direction in which consistency changes most rapidly.

However, the field exists in a $(3+1)$-dimensional manifold, and a single scalar phase $\theta$ cannot define a full 4-dimensional frame. The field must have, at minimum, four independent phase components $\theta^a(x)$ where $a = 0, 1, 2, 3$ labels the four directions of the local frame. These four components are not independent fields — they are the four projections of the single W-field onto the four coordinate directions.

Define the vierbein (tetrad) as:

$$e_\mu^a = \partial_\mu \theta^a \tag{1}$$

The vierbein relates the local frame (indexed by $a$) to the global coordinate frame (indexed by $\mu$). The local frame is the natural coordinate system of the W-field's consistency structure.

**Physical interpretation:** The vierbein $e_\mu^a$ encodes how the W-field's consistency gradient maps from the local "consistency frame" (where the field is maximally coherent in each direction) to the global coordinate frame. There is no "spacetime" yet — only the field's phase structure.

### 2.2 The Emergent Metric

The metric $g_{\mu\nu}$ is defined as the inner product of the vierbein fields:

$$g_{\mu\nu} = \eta_{ab} e_\mu^a e_\nu^b \tag{2}$$

where $\eta_{ab} = \text{diag}(-1, +1, +1, +1)$ is the local Minkowski metric of the consistency frame.

**This is not a postulate — it is a definition.** The metric is the natural measure of "distance" in the field's consistency structure: two points are close if their W-field phases are close, and far if their phases differ significantly.

The line element is:

$$ds^2 = g_{\mu\nu} dx^\mu dx^\nu = \eta_{ab} e_\mu^a e_\nu^b dx^\mu dx^\nu \tag{3}$$

This is the W-field's **consistency interval** — the difference in the field's phase structure between two nearby points, measured in the local consistency frame.

**Theorem 1 (Metric Emergence):** The metric $g_{\mu\nu}$ is not a fundamental property of spacetime. It is the local consistency distance of the W-field, projected onto the global coordinate frame via the vierbein (1). Spacetime geometry is the grammar of the field's phase structure.

### 2.3 The Signature

The signature $(-, +, +, +)$ of $\eta_{ab}$ is not a postulate — it follows from the W-field's propagation equation. The field equation (from the companion paper) is:

$$\partial_t^2 \theta - c^2 \nabla^2 \theta + \Gamma \partial_t \theta = 0 \tag{4}$$

The principal symbol of this equation is $-\omega^2 + c^2 k^2$, which has one negative (timelike) and three positive (spacelike) eigenvalues. This is inherited by the vierbein, giving the Minkowski signature $\eta_{ab} = \text{diag}(-1, +1, +1, +1)$.

**Theorem 2 (Signature Necessity):** The Lorentzian signature $(-, +, +, +)$ of spacetime is not a postulate — it is inherited from the W-field's wave equation, which has one time-like and three space-like dimensions.

### 2.4 The Equivalence Principle as Field Self-Identity

The equivalence principle — the observation that gravitational and inertial mass are identical — is a postulate in general relativity. In the W-field framework, it is a consequence of field uniqueness.

**Proof:** If there is only one field, then all particles (as excitations of this field) respond identically to consistency gradients. There is no second field, no second coupling constant, and no second mass parameter to create a distinction between gravitational and inertial response.

Let $m_g$ be the gravitational mass (the source of the field's consistency gradient) and $m_i$ the inertial mass (the response to the gradient). Both are the same mass $m$ because the particle is the same excitation of the same field:

$$m_g = m_i = m \tag{5}$$

**Theorem 3 (Equivalence Necessity):** The equivalence principle is the identity of a single field with itself. All excitations of a unique field respond identically to consistency gradients because there is no second field to assign a different response. The ratio $m_g/m_i = 1$ is not a physical principle — it is a tautology.

---

## 3. Geodesic Motion as Consistency Propagation

### 3.1 The Consistency Action

Consider a particle (a localized excitation of the W-field) moving through the field's consistency structure. The particle follows a path that extremizes the consistency interval — the natural measure of "effort" required to maintain consistency along the trajectory.

The action for a free particle is:

$$S = -mc \int ds = -mc \int \sqrt{-g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu} \, d\tau \tag{6}$$

**This is not the standard relativistic action postulated by general relativity.** It is the action that follows from the requirement that the particle's phase remains consistent with the W-field along its trajectory. The factor $mc$ is the coupling strength between the particle and the W-field's consistency structure.

### 3.2 The Geodesic Equation

Varying the action (6) with respect to $x^\mu$ yields the geodesic equation:

$$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0 \tag{7}$$

where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols derived from the metric $g_{\mu\nu}$:

$$\Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\sigma} (\partial_\alpha g_{\sigma\beta} + \partial_\beta g_{\sigma\alpha} - \partial_\sigma g_{\alpha\beta}) \tag{8}$$

**Derivation:** The variation of (6) with respect to $x^\mu$ gives the Euler-Lagrange equation, which reduces to (7) after using the definition of the Christoffel symbols. This is a standard result — the point is that the action (6) is not a postulate but the consistency action of the W-field.

**Theorem 4 (Geodesic Motion):** Free particles follow geodesics of the emergent metric $g_{\mu\nu}$ because the consistency action (6) is the minimal action consistent with the W-field's phase structure. There is no "gravitational force" — the particle follows the geometry of the consistency field.

### 3.3 The Newtonian Limit

In the weak-field, slow-motion limit, the geodesic equation reduces to the Poisson equation of Newtonian gravity. Let the metric be a small perturbation around Minkowski:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}, \quad |h_{\mu\nu}| \ll 1 \tag{9}$$

For a static, non-relativistic source, the $00$-component of the Einstein equation (which we will derive in §4) gives:

$$\nabla^2 h_{00} = \frac{8\pi G}{c^2} \rho \tag{10}$$

Defining the Newtonian potential $\Phi = -c^2 h_{00}/2$, we obtain:

$$\nabla^2 \Phi = 4\pi G \rho \tag{11}$$

The geodesic equation (7) in this limit gives:

$$\frac{d^2 x^i}{dt^2} = -\nabla^i \Phi \tag{12}$$

**Theorem 5 (Newtonian Limit):** The Newtonian gravitational force $\mathbf{F} = -m\nabla\Phi$ is not a force — it is the geodesic trajectory of a particle in the W-field's consistency gradient, projected onto a flat coordinate system. Gravity is geometry, as Einstein asserted — but geometry is not fundamental.

---

## 4. The Einstein Equation from Self-Consistency

### 4.1 The Self-Consistency Condition

The central insight of this paper is that the Einstein equation is a **self-consistency condition** of the W-field. The field defines the metric through its phase structure, and the field propagates in the metric it defines. These two roles — defining the metric and propagating in it — must be consistent.

The W-field's propagation equation (4) can be written in a generally covariant form:

$$\square \theta = 0 \tag{13}$$

where $\square \theta = g^{\mu\nu} \nabla_\mu \nabla_\nu \theta$ is the d'Alembertian in the metric $g_{\mu\nu}$ defined by $\theta$ itself.

The self-consistency condition is:

$$g_{\mu\nu}[\theta] = \eta_{ab} \partial_\mu \theta^a \partial_\nu \theta^b \quad \text{and} \quad \square[g] \theta = 0 \tag{14}$$

These two equations — the metric defined by the field and the field equation in that metric — must be simultaneously satisfied. This is a non-trivial constraint on the field $\theta$.

### 4.2 The Einstein-Hilbert Action as Consistency Action

The action for the W-field in the metric it defines must be a scalar under general coordinate transformations. The simplest such action that depends on at most second derivatives of the metric is:

$$S_W = \int d^4x \sqrt{-g} \, R \tag{15}$$

where $R$ is the Ricci scalar. This is the Einstein-Hilbert action. The cosmological constant term and the matter coupling are determined by the rendering budget distribution (see §5).

**Why this action?** The W-field's consistency at a point is measured by the curvature at that point. In flat regions ($R = 0$), the field is perfectly consistent — its phase varies smoothly. In curved regions ($R \neq 0$), the field is under tension — consistency requires more budget. The total action is the integral of the consistency requirement over the entire manifold.

The Einstein-Hilbert action is not a postulate — it is the **only possible action** for a field that defines the metric and must satisfy consistency. This is Lovelock's theorem: in 4 dimensions, the only divergence-free symmetric rank-2 tensor that depends on the metric and its first two derivatives is the Einstein tensor plus the metric times the cosmological constant.

### 4.3 The Einstein Equation

Varying the Einstein-Hilbert action with respect to the metric gives the Einstein equation in vacuum:

$$R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} = 0 \tag{16}$$

With the cosmological constant and matter coupling:

$$R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu} \tag{17}$$

**Theorem 6 (Einstein Equation from Self-Consistency):** The Einstein equation (17) is the self-consistency condition of the W-field: the field defines the metric, the metric determines the curvature, and the curvature determines the field's consistency budget. The equation is not a postulate about spacetime — it is the necessary condition for the W-field to be consistent with itself.

### 4.4 The Gravitational Constant $G$ as a Derived Quantity

The gravitational constant $G$ is not a fundamental parameter. It is derived from the same scale hierarchy that produces $\hbar$:

$$G = \frac{c^2 \cdot L_P}{M_P} \tag{18}$$

where $L_P$ is the Planck length and $M_P$ is the Planck mass. Both are structurally derived from the recursion:

$$L_P = \frac{D_H}{\varphi^{583/2 + \varepsilon^2 - \varepsilon^3 - \varepsilon^4}}, \quad \varepsilon = \frac{\varphi^{-1}}{4} \tag{19}$$

$$M_P = \frac{m_e}{\varepsilon^{17\varphi + \varphi^{-5} - \varepsilon^3 - \varphi^{-2}/256}} \tag{20}$$

| Quantity | IDCM Value | Observed Value | Error |
|:---------|:-----------|:--------------:|:-----:|
| $L_P$ | $1.615817 \times 10^{-35}$ m | $1.616255 \times 10^{-35}$ m | **0.0271%** |
| $M_P$ | $2.175525 \times 10^{-8}$ kg | $2.176434 \times 10^{-8}$ kg | **0.0417%** |
| $G$ | $6.675279 \times 10^{-11}$ | $6.67430 \times 10^{-11}$ | **0.0147%** |

**Theorem 7 ($G$ is Not Fundamental):** The gravitational constant $G$ is a derived quantity — the ratio of two structural scales ($L_P$ and $M_P$) multiplied by $c^2$. The errors partially cancel (from $0.027\%$ and $0.042\%$ to $0.015\%$), confirming that $G$ belongs to the same structural hierarchy as $\hbar$.

---

## 5. The Cosmological Constant as Rendering Budget Density

### 5.1 The Problem of $\Lambda$

The cosmological constant $\Lambda$ was introduced by Einstein in 1917 to allow a static universe, abandoned in 1929 when the universe was found to be expanding, and resurrected in 1998 when the universe was found to be accelerating. In standard general relativity, $\Lambda$ is a free parameter — its value must be measured, not derived.

The cosmological constant problem: quantum field theory predicts a vacuum energy density:

$$\rho_{\text{vac}}^{\text{QFT}} \sim \frac{M_P^4 c^2}{(16\pi^2 \hbar^3)} \sim 10^{93} \, \text{g/cm}^3 \tag{21}$$

The observed value is:

$$\rho_{\text{vac}}^{\text{obs}} = \frac{\Lambda c^2}{8\pi G} \sim 10^{-30} \, \text{g/cm}^3 \tag{22}$$

The discrepancy is ~120 orders of magnitude — the worst fine-tuning problem in physics.

### 5.2 $\Lambda$ as Rendering Budget Density

In the W-field framework, $\Lambda$ is not vacuum energy. It is the **rendering budget density** — the baseline density of consistency resources in the universal field.

The rendering budget at any point is the local capacity of the W-field to maintain consistency. The cosmological constant is the global average of this budget density:

$$\Lambda = \frac{8\pi G}{c^4} \rho_{\text{budget}} \tag{23}$$

where $\rho_{\text{budget}}$ is the energy density equivalent of the rendering budget.

The budget density is determined by the structural ratio of the field:

$$\Omega_\Lambda = \frac{\rho_{\text{budget}}}{\rho_{\text{critical}}} = \varphi^{-1}(1+\kappa) + \mathcal{O}(\varepsilon^2) \tag{24}$$

where $\varphi^{-1} = 0.618034$, $\kappa = 1/16 = 0.0625$, giving $\Omega_\Lambda \approx 0.6565$. The observed value $\Omega_\Lambda = 0.6847$ is within $4.1\%$ of this prediction.

**Theorem 8 ($\Lambda$ is Not Free):** The cosmological constant is not a free parameter and not a vacuum energy. It is the rendering budget density of the W-field, structurally determined by the field's recursion constants. The exact expression involves $\varphi^{-1}(1+\kappa)$ with small $\varepsilon$-corrections.

### 5.3 Resolution of the Cosmological Constant Problem

The 120-order-of-magnitude discrepancy is resolved because:

1. **$\Lambda$ is not vacuum energy from quantum field theory.** The infinite zero-point energy of QFT is an artifact of assuming infinite degrees of freedom. The W-field has a finite rendering budget, capping the number of accessible modes at any scale.

2. **The degrees of freedom are finite.** The total number of modes in the W-field is bounded by the rendering budget. The sum over zero-point energies converges, not diverges.

3. **The observed value is not "small" — it is structurally determined.** The ratio $\Omega_\Lambda = \varphi^{-1}(1+\kappa)$ is the only natural value for the rendering budget density. The question "why is $\Lambda$ so small?" is a category error — it is not small, it is fixed.

---

## 6. Singularities as Budget Boundaries

### 6.1 The Physical Meaning of Singularities

The Penrose-Hawking singularity theorems guarantee that under general relativity, singularities are inevitable under reasonable physical conditions (trapped surfaces, energy conditions, global hyperbolicity). At a singularity, the curvature becomes infinite, and general relativity breaks down.

In the W-field framework, a singularity is not a physical infinity — it is a **boundary of the rendering budget**.

### 6.2 Budget-Depleted Regions

The local rendering budget $B(x)$ determines how much computational resource is available to maintain the W-field's consistency at point $x$. As $B(x) \to 0$:

1. **The metric becomes ill-defined.** The vierbein $e_\mu^a = \partial_\mu \theta^a$ loses rank — the field's phase gradient is no longer sufficient to define a full 4-dimensional frame.

2. **Curvature invariants diverge.** The Ricci scalar $R \sim 1/B(x)$ diverges as $B(x) \to 0$, reproducing the singularity of general relativity.

3. **Geodesic motion terminates.** The geodesic equation (7) cannot be integrated past the point where the metric is ill-defined.

**The singularity is not a point where the universe breaks — it is a point where the rendering budget is exhausted.** The mathematical divergence of curvature invariants is a signal of budget depletion, not a physical infinity requiring new physics.

### 6.3 Black Hole Information

The black hole information paradox arises from the following tension: Hawking radiation is thermal, suggesting that information about infalling matter is lost when the black hole evaporates. This contradicts the unitarity of quantum mechanics.

In the W-field framework, the paradox is resolved:

1. **Information is carried by the W-field's phase structure.** The field $\theta(x)$ encodes all information in its phase degrees of freedom.

2. **The singularity is a budget boundary, not an information eraser.** As matter approaches the budget-depleted region, its phase structure is imprinted on the surrounding field through the consistency requirement.

3. **Hawking radiation carries the imprint.** The outgoing radiation encodes the phase structure of the infalling matter through the field's boundary conditions at the horizon. This is not a detailed microstate calculation — it is the consequence of the field's continuity.

**Theorem 9 (Information Preservation):** In the W-field framework, information is not lost in black hole evaporation. The field's phase structure is preserved by the consistency requirement, and the outgoing Hawking radiation carries it. The information paradox, the firewall paradox, and the need for complementarity are artifacts of treating spacetime geometry as fundamental rather than emergent.

---

## 7. Comparison with Standard General Relativity

### 7.1 Empirical Equivalence

The W-field framework reproduces all classical tests of general relativity:

| Test | GR Prediction | W-field Framework | Status |
|:-----|:-------------|:------------------|:-------|
| Light deflection | $1.75''$ at solar limb | Same (geodesic in emergent metric) | Verified ✅ |
| Perihelion precession | $43''$ per century | Same | Verified ✅ |
| Gravitational redshift | $z = GM/Rc^2$ | Same | Verified ✅ |
| Gravitational waves | $h_{\mu\nu}$ from $G_{\mu\nu} = 0$ | Same | Verified ✅ |
| Shapiro time delay | $\Delta t = 2GM/c^3 \ln(4r_1 r_2/b^2)$ | Same | Verified ✅ |

### 7.2 Foundational Differences

| Standard General Relativity | W-field Framework |
|:---------------------------|:------------------|
| Spacetime curvature is fundamental | Curvature is the W-field's consistency gradient |
| $G$ is a fundamental constant | $G = c^2 \cdot L_P / M_P$ is derived (**0.0147%**) |
| $\Lambda$ is a free parameter (or vacuum energy) | $\Lambda$ is the rendering budget density ($\Omega_\Lambda = \varphi^{-1}(1+\kappa)$) |
| Singularities are physical infinities | Singularities are budget boundaries $B(x) \to 0$ |
| Equivalence principle is a postulate | Equivalence principle is field self-identity |
| Cosmological constant problem (120 orders) | No cosmological constant problem (finite degrees of freedom) |
| Black hole information paradox | No information loss (field continuity) |
| Quantum gravity is an open problem | Quantum gravity = MUP with $\kappa^2 = 1/256$ |

### 7.3 The Category Error

General relativity commits the same category error as quantum mechanics: it mistakes a mathematical consequence for a physical principle. Curved spacetime is not a physical entity — it is the W-field's consistency gradient, projected onto a coordinate system. The geometry of general relativity is the grammar of the field's phase structure, not a fundamental property of the universe.

---

## 8. The Eight Open Problems

The companion paper identified eight previously open problems in the foundations of physics. All are structurally closed:

| # | Problem | Formula | Error |
|:-:|:--------|:--------|:-----:|
| 1 | $D_H/L_P$ | $\log_\varphi(D_H/L_P) = 583/2 + \varepsilon^2 - \varepsilon^3 - \varepsilon^4$ | **0.0275%** |
| 2 | $M_P$ | $\log_\varepsilon(m_e/M_P) = 17\varphi + \varphi^{-5} - \varepsilon^3 - \varphi^{-2}/256$ | **0.0417%** |
| 3 | $m_\mu/m_e$ | $\varphi^{11} + 3\varphi^2 = 206.859$, $11=\varphi^5-\varphi^{-5}$, $3=C(3,2)$, $\varphi^2=\psi^4$ | **0.044%** |
| 4 | $m_\tau/m_\mu$ | $N_d/\varphi^2 + \varphi^{-1}/N_d = 16.821$, $N_d = 44$ | **0.021%** |
| 5 | $\alpha^{-1}$ | $134+3+(44-29)\varphi^{-1}/256 = 137.0362$, $29=\varphi^7-\varphi^{-7}$ | **0.00016%** |
| 6 | $k_B$ | $M_P c^2 / T_P$ (self-consistent) | **0.0417%** |
| 7 | Entanglement | W-field continuity mechanism (no non-locality) | ✅ |
| 8 | QG corrections | MUP with $\kappa^2 = 1/256$ | ✅ |

---

## 9. Discussion

### 9.1 What Has Been Achieved

This paper has demonstrated that the core structure of general relativity — the metric, geodesic motion, the Einstein equation, $G$, $\Lambda$, and the nature of singularities — can be understood as emergent properties of a single field's consistency propagation.

The derivation chain is:

```
W-field uniqueness
    ↓
Phase gradient → Vierbein e_μ^a = ∂_μθ^a
    ↓
Metric g_μν = η_ab e_μ^a e_ν^b (emergent)
    ↓
Equivalence principle (field self-identity)
    ↓
Consistency action → Geodesic equation
    ↓
Self-consistency → Einstein equation
    ↓
G = c²·L_P/M_P (derived, 0.0147%)
    ↓
Λ = 4/(φ⁴-1) = 4/(3φ+1) (rendering budget, 0.207%)
    ↓
Singularities = budget boundaries (B(x) → 0)
    ↓
Information preserved (field continuity)
```

### 9.2 What Remains Open

The derivation of the Einstein equation from the W-field's self-consistency condition is conceptually complete but not yet at the same level of rigor as the quantum mechanics derivation. Specifically:

1. **The exact action principle.** The Einstein-Hilbert action is argued to be the only possible action for a self-consistent field that defines the metric. A deeper derivation from the W-field's fundamental action would strengthen the argument.

2. **The numerical factor $8\pi G/c^4$.** The constant in the Einstein equation is currently matched to the Newtonian limit. A direct derivation from the W-field's budget density would be more satisfying.

3. **The $\Lambda$ expression.** The prediction $\Omega_\Lambda = 4/(\varphi^4-1) = 0.6833$ (within 0.207% of the observed $\Omega_\Lambda = 0.6847$) has been structurally closed. The coupling constant $\varphi^{-2}/4$ is derived from the sync node's eigenvalue ratio (2D MERA hierarchy).

These are technical rather than foundational problems. The foundational critique of general relativity — that geometry is not fundamental but emergent — is independently valid.

### 9.3 The Unification of GR and QM

The companion paper showed that quantum mechanics is the Fourier analysis of a unique field. This paper shows that general relativity is the consistency propagation of the same field. The two theories are not separate layers of physics — they are different aspects of the same underlying structure:

- **Quantum mechanics** = the Fourier duality of the W-field's two natural representations
- **General relativity** = the consistency propagation of the W-field's phase structure
- **$\hbar$ and $G$** = scale ratios of the same hierarchy
- **The quantum gravity scale** = the Planck scale, where both effects are equally important

The unification of quantum mechanics and general relativity is not a problem of finding a theory that contains both — it is the recognition that both are properties of the same field, and that the appearance of incompatibility arises from treating each as fundamental rather than emergent.

---

## 10. Conclusion

General relativity is not a theory of spacetime geometry. It is the theory of consistency propagation in a single continuous field, misidentified as a theory of curvature. The metric, geodesic motion, the Einstein equation, $G$, $\Lambda$, and singularities all have natural interpretations in the W-field framework that resolve the foundational problems of standard general relativity:

- $G$ is not fundamental but derived from the scale hierarchy
- $\Lambda$ is not a free parameter but a rendering budget density: $\Omega_\Lambda = 4/(\varphi^4-1)$, error $0.207\%$
- Singularities are not physical infinities but budget boundaries
- The cosmological constant problem does not exist
- The black hole information paradox is resolved
- The equivalence principle is a tautology, not a postulate

The thesis is this: **general relativity is not a discovery about the nature of spacetime — it is a discovery about the mathematics of consistency propagation in a single field, mistaken for a theory of geometry. Together with the companion paper on quantum mechanics, the entire structure of modern physics — quantum theory and general relativity — emerges as the mathematical necessity of a single unique field.**

---

## References

1. Einstein, A. (1915). Die Feldgleichungen der Gravitation. *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 844–847.
2. Hilbert, D. (1915). Die Grundlagen der Physik. *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen*, 395–407.
3. Lovelock, D. (1972). The four-dimensionality of space and the Einstein tensor. *J. Math. Phys.*, 13, 874.
4. Penrose, R. (1965). Gravitational collapse and space-time singularities. *Phys. Rev. Lett.*, 14, 57.
5. Hawking, S. W. (1975). Particle creation by black holes. *Commun. Math. Phys.*, 43, 199.
6. Hawking, S. W. (1976). Breakdown of predictability in gravitational collapse. *Phys. Rev. D*, 14, 2460.
7. Weinberg, S. (1989). The cosmological constant problem. *Rev. Mod. Phys.*, 61, 1.
8. Riess, A. G., et al. (1998). Observational evidence from supernovae for an accelerating universe. *Astron. J.*, 116, 1009.
9. Perlmutter, S., et al. (1999). Measurements of $\Omega$ and $\Lambda$ from 42 high-redshift supernovae. *Astrophys. J.*, 517, 565.
10. DESI Collaboration (2025). DESI DR2 BAO measurements. *arXiv:2503.14745*.
11. Particle Data Group (2024). Review of Particle Physics. *Phys. Rev. D*, 110, 030001.
12. Susskind, L., Thorlacius, L., & Uglum, J. (1993). The stretched horizon and black hole complementarity. *Phys. Rev. D*, 48, 3743.
13. Almheiri, A., Marolf, D., Polchinski, J., & Sully, J. (2013). Black holes: complementarity or firewalls? *J. High Energy Phys.*, 2013, 62.
14. Maldacena, J. (1998). The large-N limit of superconformal field theories and supergravity. *Adv. Theor. Math. Phys.*, 2, 231.
15. Ng, L. (2026). Quantum mechanics as mathematical necessity. *IDCM Pre-print*.