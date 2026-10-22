# ε-Series Correction Appendix — Parallel to Structural Formulas

## Structural formulas are 🟢; ε-series corrections are shown in parallel, not as replacements

---

## 1. ε-Series Hierarchy

All 22 parameters have residuals following a strict ε-power hierarchy:

| ε-order | Magnitude | Parameters | Meaning |
|:-------:|:---------:|:-----------|:--------|
| ε⁰ | exact | κ, κ², S_inst, ω², v_g, E_cut | Pure structural, no residual |
| ε⁶ | ~10⁻⁵ | δ_e = 63φ⁻⁴/256 | Tree curvature × MERA fully closed |
| ε⁴ | ~10⁻³ | δ_u, V_cb | Chain mode, MERA sector |
| ε³ | ~10⁻³ | λ, η, δ, J | CP sector, complex phase |
| ε² | ~10⁻² | A | Error propagation (derived, not fundamental) |
| ε¹ | ~10⁻¹ | ρ | Complex phase sector NOT included |

---

## 2. ρ — Structural + Correction (Parallel)

### 🟢 Structural

$$\boxed{\rho = \varphi^{-4} = 0.1459}$$

Origin: tree curvature $\varphi^{-4} = \varepsilon \cdot \varphi^{-3}$.

Error from observed $\rho = 0.157$: **7.07%** (largest residual in the framework).

### 🟡 With ε/2 Correction

$$\boxed{\rho = \varphi^{-4} \left(1 + \frac{\varepsilon}{2}\right) = \varphi^{-4} + \frac{\varphi^{-4}\varepsilon}{2} = 0.1572}$$

| Component | Formula | Value |
|:----------|:--------|:-----:|
| Structural | $\varphi^{-4}$ | 0.14590 |
| Correction | $\varphi^{-4} \cdot \varepsilon/2$ | 0.01127 |
| **Total** | $\varphi^{-4} (1 + \varepsilon/2)$ | **0.15717** |
| Observed | — | 0.157 |
| **Error** | | **0.11%** |

**Structural interpretation of $\varepsilon/2$:**
$$\frac{\varepsilon}{2} = \frac{\varphi^{-1}}{8} = \frac{\beta}{4}$$

$\beta = \varphi^{-1}/2$ is the sector step size. $\varepsilon/2 = \beta/4$ is the correction from the W-field complex phase sector — the first-order perturbation of the chain eigenvectors' imaginary parts.

**Representation:** The 7.07% error is the only ε¹-level residual in the entire framework. It confirms that the complex phase sector contributes at O(ε) to ρ, while all other parameters are O(ε²) or smaller.

---

## 3. A — Structural + Correction (Parallel)

### 🟢 Structural

$$\boxed{A = \frac{V_{cb}}{\lambda^2} = \frac{\varphi^2/64}{(\varphi^{-3} - L_c)^2} = 0.801}$$

Origin: ratio of two structural formulas. A is **derived**, not fundamental.

Error from observed $A = 0.826$: **3.02%** (error propagation).

### 🟡 With ε² Correction

$$\boxed{A = \frac{V_{cb}}{\lambda^2} \cdot (1 + \varepsilon^2) = 0.820}$$

| Component | Formula | Value |
|:----------|:--------|:-----:|
| Structural | $V_{cb}/\lambda^2$ | 0.80104 |
| Correction | $\times (1 + \varepsilon^2)$ | 0.82016 |
| Observed | — | 0.826 |
| **Error** | | **0.71%** |

**Structural interpretation of $\varepsilon^2$:** The second-order MERA coupling correction. A is not a fundamental parameter — it's the ratio of V_cb and λ², so its error comes from the propagation of the ε-series truncation of both V_cb and λ.

---

## 4. Complete ε-Series Profile

```text
Parameter    Structural          Corrected        Obs     Struct%   Corr%   Level
───          ──────────          ─────────        ───     ───────   ─────   ─────
δ_u = 2γ₂    4.071%              —                4.08%   0.21%     —       ε⁴
δ_e          63φ⁻⁴/256 = 3.591%  —                3.59%   0.01%     —       ε⁶
V_cb         0.04091             —                0.0410  0.23%     —       ε⁴
λ            0.22598             —                0.225   0.44%     —       ε³
A            0.80104             0.82016          0.826   3.02%     0.71%   ε²
η            0.34935             —                0.345   1.26%     —       ε²
ρ            0.14590             0.15717          0.157   7.07%     0.11%   ε¹
δ            67.3°               —                68°     1.0%      —       ε³
J            2.99×10⁻⁵           —                3.0×10⁻⁵0.5%     —       ε³
```

**Takeaway:** The structural formulas are the correct leading-order expressions. The ε-series corrections encode the next-order perturbations from the W-field's complex phase sector (for ρ) and MERA coupling (for A). Both are presented as parallel refinements, not replacements.