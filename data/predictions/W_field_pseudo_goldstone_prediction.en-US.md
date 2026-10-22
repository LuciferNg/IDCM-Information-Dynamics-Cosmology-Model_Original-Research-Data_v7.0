# W-field Pseudo-Goldstone Boson

**Prediction:** A new light scalar particle at $14.09$ GeV.

**Status:** Theoretical prediction from W-field framework. Not yet observed.

---

## Derivation

The W-field has a global U(1) symmetry:

$$W \to e^{i\alpha}W$$

The VEV $|W|_0 = \sqrt{\varepsilon/(2\kappa)}$ spontaneously breaks this symmetry, producing a massless Goldstone mode $\theta$ (the phase of $W$).

In the Standard Model, the SU(2) doublet embedding $H = (h^+, W)^T$ would eat this Goldstone via the Higgs mechanism — the $Z$ boson absorbs $\theta$ as its longitudinal component. However, the SU(2) embedding is **not exact**. The 3.6% mismatch between the W-field potential formula and the SU(2) formula (discovered in the Higgs cross-validation) explicitly breaks the U(1) symmetry, giving the Goldstone a small mass.

## Mass

$$m_{\text{PG}} = \varepsilon \times M_Z = \frac{\varphi^{-1}}{4} \times 91.188\ \text{GeV} = 14.09\ \text{GeV}$$

where $\varepsilon = \varphi^{-1}/4$ is the W-field structure constant (the linear coefficient of the W-field potential $V = -\varepsilon|W|^2 + \kappa|W|^4$).

## Couplings

All couplings are suppressed by the SU(2) embedding mismatch:

$$\delta = 1 - \frac{2\sqrt{\kappa} \times V_{EW}}{M_W/g} = 0.0354 = 3.54\%$$

| Coupling | Formula | Value |
|:---------|:--------|:------|
| $g_{\phi\theta\theta}$ (Higgs) | $\delta \times \kappa \times V_{EW}$ | 0.545 GeV |
| $g_{\theta ff}$ (fermions) | $\delta \times m_f / V_{EW}$ | $10^{-5} \sim 10^{-3}$ |
| $g_{\theta Z}$ (Z boson) | $\delta \times g / \cos\theta_W$ | 0.025 |

## Decay

| Channel | Branching Ratio | Notes |
|:--------|:---------------:|:------|
| $b\bar{b}$ | **67.4%** | dominant |
| $\tau^+\tau^-$ | **21.2%** | subdominant |
| $c\bar{c}$ | 11.4% | |
| $\mu^+\mu^-$ | 0.08% | |
| $\gamma\gamma$ | 0.001% | loop-induced |
| $\Gamma_{\text{total}}$ | $1.6 \times 10^{-7}$ GeV | prompt ($\tau \sim 10^{-18}$ s) |

## Higgs Decay

$$h \to \text{PG} + \text{PG}$$

$$\Gamma(h \to \text{PG PG}) = 2.3 \times 10^{-5}\ \text{GeV}$$

$$\text{Br}(h \to \text{PG PG}) = 0.56\%$$

This is below current LHC sensitivity ($\text{Br}_{\text{inv}} < 10\text{--}20\%$).

## Production

### LHC 13 TeV

$$\sigma(gg \to \text{PG}) \sim 10^{-14}\ \text{pb}$$

Too weak to detect. The coupling suppression $\delta^2 \sim 10^{-3}$ and the loop factor make the cross-section negligible.

### Future Colliders

The most promising channel is $Z \to \gamma + \text{PG}$ at FCC-ee. The coupling $g_{\theta Z} = 0.025$ gives a detectable rate at $10^{12}$ $Z$ bosons.

## Experimental Status

No known particle at 14.09 GeV. LEP and LHC searches for light scalars in this mass range are not sensitive to the suppressed couplings of the pseudo-Goldstone.

## Key Insight

Two different W-field structure constants control different physical properties:

- $\varepsilon = \varphi^{-1}/4 = 15.45\%$ → **mass** ($m_{\text{PG}} = \varepsilon \times M_Z$)
- $\delta = 3.54\%$ (SU(2) mismatch) → **couplings** ($g_{\text{PG}} = \delta \times \text{SM coupling}$)

This is the W-field's unique signature: the mass and coupling are determined by different aspects of the same underlying structure.

## Files

- `pg_verify.py` — Mass and decay verification
- `pg_couplings.py` — Full coupling and cross-section derivation
- `W_field_pseudo_goldstone.en-US.md` — Detailed derivation document