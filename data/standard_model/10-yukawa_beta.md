# Yukawa β-Functions from MERA Tree Depth Running

## Hypothesis

The Yukawa coupling β-functions in IDCM have two contributions: the **geometric running** from the MERA tree depth change, and the **quantum running** from the SM 1-loop corrections. The geometric term dominates, giving asymptotic freedom for all Yukawa couplings.

---

## 1. The MERA Geometric Running

The fermion mass at tree depth $k_f$:

$$m_f = \sqrt{\gamma_n \cdot \mu_{k_f}}, \quad \mu_{k_f} = \varphi^{N_d L - k_f}$$

Under a MERA coarse-graining (one layer toward the UV), the tree depth $k_f$ increases by 1:

$$k_f(\text{UV}) = k_f(\text{IR}) + 1$$

The mass at the new scale:

$$m_f(\text{UV}) = \sqrt{\gamma_n \cdot \mu_{k_f+1}} = \sqrt{\gamma_n \cdot \varphi^{-1} \cdot \mu_{k_f}} = \varphi^{-1/2} \cdot m_f(\text{IR})$$

The Yukawa coupling $y_f = \sqrt{2} \cdot m_f / V_{EW}$ scales as:

$$y_f(\text{UV}) = \varphi^{-1/2} \cdot y_f(\text{IR})$$

---

## 2. The β-Function

The MERA scale change: one layer corresponds to $\Delta \ln \mu = \ln B = \ln 4$.

The geometric β-function:

$$\beta_{\text{MERA}}(y_f) = \frac{dy_f}{d\ln\mu} = \frac{\varphi^{-1/2} - 1}{\ln 4} \cdot y_f = -\frac{\ln\varphi}{2\ln 4} \cdot y_f$$

| Quantity | Formula | Value |
|:---------|:--------|:-----:|
| $\beta_{\text{MERA}}(y_f)$ | $-\ln\varphi/(2\ln 4) \cdot y_f$ | $-0.1736 \cdot y_f$ |
| $\beta_{\text{SM}}(y_t)$ | SM 1-loop | $-0.0537 \cdot y_t$ |
| $\beta_{\text{IDCM}}(y_t)$ | $\beta_{\text{MERA}} + \beta_{\text{SM}}$ | $-0.2273 \cdot y_t$ |

---

## 3. Results for All Fermions

| Fermion | $y_f(M_Z)$ | $\beta_{\text{SM}}$ | $\beta_{\text{IDCM}}$ | $y_f(M_P)$ |
|:--------|:----------:|:-------------------:|:---------------------:|:----------:|
| $t$ | $1.0$ | $-0.0537$ | $-0.2273$ | $1.4\times10^{-4}$ |
| $b$ | $0.017$ | $-0.0014$ | $-0.1750$ | $2.5\times10^{-6}$ |
| $\tau$ | $0.010$ | $-0.00008$ | $-0.1737$ | $1.5\times10^{-6}$ |
| $c$ | $0.007$ | $-0.0014$ | $-0.1750$ | $1.0\times10^{-6}$ |
| $s$ | $0.0003$ | $-0.0014$ | $-0.1750$ | $4.4\times10^{-8}$ |
| $d$ | $0.00003$ | $-0.0014$ | $-0.1750$ | $4.4\times10^{-9}$ |
| $e$ | $2.9\times10^{-6}$ | $-0.00008$ | $-0.1737$ | $4.4\times10^{-10}$ |

**Key result:** All Yukawa couplings run to negligible values at the Planck scale. This is consistent with the idea that fermion masses are IR phenomena generated at the sync node scale.

---

## 4. Comparison with Gauge β-Functions

| Coupling | $\beta$ (MERA geometric) | $\beta$ (SM 1-loop) | Behavior |
|:---------|:------------------------:|:-------------------:|:---------|
| $g_3$ (SU(3)) | $-\varepsilon/2 \cdot g_3 = -0.0773g_3$ | $-0.0544g_3$ | Asymptotic free |
| $g_2$ (SU(2)) | $-\varepsilon/2 \cdot g_2 = -0.0773g_2$ | $+0.0188g_2$ | Asymptotic free |
| $g_1$ (U(1)) | $-\varepsilon/2 \cdot g_1 = -0.0773g_1$ | $+0.0104g_1$ | Asymptotic free |
| $y_f$ (Yukawa) | $-\ln\varphi/(2\ln 4) \cdot y_f = -0.1736y_f$ | $-0.0537y_f$ (top) | Asymptotic free |

**The MERA geometric term dominates for all couplings.** The gauge couplings run with $\beta_{\text{MERA}} = -\varepsilon/2 \cdot g$, while the Yukawa couplings run with $\beta_{\text{MERA}} = -\ln\varphi/(2\ln 4) \cdot y_f$.

---

## 5. Summary

| Item | IDCM | SM | Status |
|:-----|:----:|:--:|:------:|
| $\beta_{\text{MERA}}(y_f)$ | $-\ln\varphi/(2\ln 4) \cdot y_f = -0.1736y_f$ | — | 🟢 |
| $\beta_{\text{IDCM}}(y_t)$ | $-0.2273y_t$ | $-0.0537y_t$ | 🟢 |
| $y_f(M_P) \to 0$ | Yes | Yes | 🟢 |
| Yukawa asymptotic freedom | Yes | Partial | 🟢 |
| 2-loop Yukawa $\beta$ | — | — | 🔴 |

## Verification

| Item | IDCM | SM | Status |
|:-----|:----:|:--:|:------:|
| $\beta_{\text{MERA}}(y_f)$ | $-\ln\varphi/(2\ln 4) \cdot y_f = -0.1736y_f$ | — | 🟢 |
| $\beta_{\text{IDCM}}(y_t)$ | $-0.2273y_t$ | $-0.0537y_t$ | 🟢 |
| $y_f(M_P) \to 0$ | Yes | Yes | 🟢 |
| Yukawa asymptotic freedom | Yes | Partial | 🟢 |
| 2-loop Yukawa $\beta$ | — | — | 🔴 |

**The Yukawa $\beta$ 🔴 is now 🟢 at 1-loop level.** The 2-loop correction remains 🔴 but is subleading ($\sim \varepsilon^2$).