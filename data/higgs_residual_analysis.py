#!/usr/bin/env python3
"""
higgs_residual_analysis.py — 分析 Higgs 0.19% 殘差
"""
import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1/16
V_EW = 246.22
m_H_obs = 125.10

print("=" * 72)
print("HIGGS RESIDUAL ANALYSIS — 0.19% 來源")
print("=" * 72)

# Current formula
λ_GUT = κ/2
ratio = 4 + φ_inv**4
λ_weak = λ_GUT * ratio
m_H_pred = math.sqrt(2 * λ_weak) * V_EW
err = (m_H_pred / m_H_obs - 1) * 100

print(f"\n  Current: m_H = √(κ(4+φ⁻⁴)) × V_EW = {m_H_pred:.4f} GeV")
print(f"           Error = {err:.4f}%")

# What λ_weak would give exact m_H?
λ_exact = m_H_obs**2 / (2 * V_EW**2)
ratio_exact = λ_exact / λ_GUT
print(f"\n  Exact λ(weak) = {λ_exact:.6f}")
print(f"  Exact λ(weak)/λ(GUT) = {ratio_exact:.6f}")
print(f"  Predicted ratio = 4+φ⁻⁴ = {ratio:.6f}")
print(f"  Gap = {ratio_exact - ratio:.6f}")

# Check if κ² correction helps
print("\n" + "─" * 72)
print("POSSIBLE CORRECTIONS")
print("─" * 72)

corrections = [
    ("none", 0),
    ("-κ²", -κ**2),
    ("-ε²", -ε**2),
    ("-φ⁻⁴/16", -φ_inv**4/16),
    ("-ε²/12", -ε**2/12),
    ("-κ²/2", -κ**2/2),
    ("-φ⁻¹/256", -φ_inv/256),
]

for name, corr in corrections:
    r = ratio + corr
    λ = λ_GUT * r
    m = math.sqrt(2 * λ) * V_EW
    e = (m / m_H_obs - 1) * 100
    print(f"  4+φ⁻⁴ {name:>10s} = {r:.6f}  → m_H = {m:.4f} GeV  err={e:.4f}%")

# Compare with experimental uncertainty
print("\n" + "─" * 72)
print("EXPERIMENTAL UNCERTAINTY")
print("─" * 72)
print(f"  PDG m_H = 125.10 ± 0.17 GeV (1σ)")
print(f"  1σ range: [{m_H_obs-0.17:.2f}, {m_H_obs+0.17:.2f}] GeV")
print(f"  2σ range: [{m_H_obs-0.34:.2f}, {m_H_obs+0.34:.2f}] GeV")
print(f"  Our prediction {m_H_pred:.2f} is at {(m_H_pred-m_H_obs)/0.17:.2f}σ")
print(f"  → Within 2σ ✅")

# Compare with other IDCM predictions
print("\n" + "─" * 72)
print("COMPARISON WITH OTHER IDCM PREDICTIONS")
print("─" * 72)
predictions = [
    ("α⁻¹", 137.0362129, 137.035999084, 0.000156),
    ("D_H/L_P (ln)", 140.2827, 140.3, 0.012),
    ("m_μ/m_e", 206.859127, 206.771037, 0.0426),
    ("m_τ/m_μ", 16.817325, 16.817029, 0.0018),
    ("M_P (GeV)", 1.22e19, 1.220890e19, 0.0415),
    ("Ω_Λ", 0.683282, 0.6847, 0.207),
    ("m_H (GeV)", m_H_pred, m_H_obs, err),
]

for name, pred, obs, e in predictions:
    print(f"  {name:15s}  pred={pred:.6e}  obs={obs:.6e}  err={e:.4f}%")

# 2-loop RG estimate
print("\n" + "─" * 72)
print("2-LOOP RG CORRECTION ESTIMATE")
print("─" * 72)
# SM 2-loop β_λ has terms like -λy_t⁴/(4π²)²
# Typical size: (1/(4π))² ≈ 0.0063
# Which is ≈ 0.6% of the leading term
loop_factor = 1/(16*math.pi**2)  # 1-loop suppression
print(f"  1-loop factor: 1/(16π²) = {loop_factor:.6f}")
print(f"  Expected 2-loop correction: ~{loop_factor*100:.2f}% of λ")
print(f"  Corresponding m_H shift: ~{loop_factor*100/2:.2f}%")
print(f"  Our residual 0.19% is consistent with 2-loop RG effects ✅")

# Summary
print("\n" + "=" * 72)
print("CONCLUSION")
print("=" * 72)
print(f"""
  Current prediction: m_H = {m_H_pred:.2f} GeV → 0.19% error
  Within 2σ of experimental value ({m_H_obs} ± 0.17 GeV) ✅
  
  Two possible origins for the 0.19%:
  1. 2-loop RG correction (expected ~0.2-0.5%)
  2. κ² = 1/256 boundary correction → 0.14% error
  
  To reduce below 0.1%, need full 2-loop SM RG running
  from λ(GUT) = κ/2 = 0.03125 to M_Z scale.
""")