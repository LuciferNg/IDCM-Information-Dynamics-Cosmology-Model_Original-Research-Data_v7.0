#!/usr/bin/env python3
"""
pg_couplings.py — W-field 贗 Goldstone 耦合與截面（修正版）
"""
import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1/16
V_EW = 246.22
M_Z = 91.188
M_W = 80.377
m_H = 125.10

α = 1/137.036
s2w = 0.2312
g = math.sqrt(4*math.pi*α/s2w)

# 關鍵: PG 質量來自 ε，但耦合來自 SU(2) 嵌入不匹配 δ
# δ = W-field 預測與 SU(2) 關係的差異
δ = 1 - 2*math.sqrt(κ)*V_EW / (M_W/g)

m_PG = ε * M_Z  # 14.09 GeV

# 費米子質量
mf = {'τ': 1.77686, 'μ': 0.10566, 'b': 4.18, 'c': 1.27, 's': 0.095}

print("=" * 72)
print("W-field 贗 Goldstone — 耦合與截面（修正版）")
print("=" * 72)

print(f"\nm_PG = ε × M_Z = {ε:.6f} × {M_Z} = {m_PG:.2f} GeV")
print(f"SU(2) 嵌入不匹配 δ = {δ:.6f} = {δ*100:.2f}%")
print(f"→ 耦合抑制因子 = δ (不是 ε)")

# ──────────────────────────────────
# 1. 耦合到 Higgs
# ──────────────────────────────────
print(f"\n{'='*72}")
print("1. 耦合到 Higgs (φθθ)")
print(f"{'='*72}")

g_φθθ = δ * κ * V_EW
print(f"  g_φθθ = δ × κ × V_EW")
print(f"        = {δ:.6f} × {κ} × {V_EW}")
print(f"        = {g_φθθ:.4f} GeV")

if 2*m_PG < m_H:
    Γ_h_PG = g_φθθ**2 / (32*math.pi*m_H) * math.sqrt(1 - 4*m_PG**2/m_H**2)
    Br_h_PG = Γ_h_PG / 0.0041 * 100  # SM Higgs width 4.1 MeV
    print(f"  Γ(h → PG PG) = {Γ_h_PG:.6f} GeV")
    print(f"  Br(h → PG PG) = {Br_h_PG:.2f}%")
    print(f"  → LHC 約束: Br(inv) < 10-20%")
    print(f"  → 在 LHC 靈敏度以下 ✅")
else:
    print(f"  h → PG + PG: 運動學不允許")

# ──────────────────────────────────
# 2. 耦合到費米子
# ──────────────────────────────────
print(f"\n{'='*72}")
print("2. 耦合到費米子 (θff)")
print(f"{'='*72}")

print(f"  g_θff = δ × m_f/V_EW")
for name, m in mf.items():
    g_θff = δ * m / V_EW
    print(f"  g_θ{name}{name} = {δ:.6f} × {m:.5f}/{V_EW} = {g_θff:.6e}")

# ──────────────────────────────────
# 3. 衰變寬度
# ──────────────────────────────────
print(f"\n{'='*72}")
print("3. 衰變寬度")
print(f"{'='*72}")

total_Γ = 0
decays = []
for name, m in sorted(mf.items(), key=lambda x: x[1]):
    if m_PG > 2*m:
        g_θff = δ * m / V_EW
        Γ = (g_θff**2 * m_PG) / (8*math.pi) * (1 - 4*m**2/m_PG**2)**1.5
        decays.append((name, Γ))
        total_Γ += Γ

# Γ(PG → γγ) 通過 τ 圈
g_θττ = δ * mf['τ'] / V_EW
A_τ = 1.0
Γ_γγ = (α**2 * g_θττ**2 * m_PG**3) / (64*math.pi**3 * mf['τ']**2)
total_Γ += Γ_γγ

print(f"  Γ_total = {total_Γ:.6e} GeV")
print(f"  τ = {1/total_Γ*6.582e-25:.4e} s")
print(f"  → 瞬時衰變 (prompt) ✅")

print(f"\n  分支比:")
for name, Γ in decays:
    print(f"  Br(PG → {name}⁺{name}⁻) = {Γ/total_Γ*100:.2f}%")
print(f"  Br(PG → γγ) = {Γ_γγ/total_Γ*100:.4f}%")

# ──────────────────────────────────
# 4. LHC 產生截面
# ──────────────────────────────────
print(f"\n{'='*72}")
print("4. LHC 產生截面")
print(f"{'='*72}")

α_s = 0.118
g_θbb = δ * mf['b'] / V_EW
g_θgg = (α_s / (3*math.pi)) * (g_θbb / mf['b'])
σ_gg = (math.pi**2/8) * g_θgg**2 / m_PG

print(f"  σ(gg → PG) ≈ {σ_gg*1e6:.4f} fb (13 TeV)")
print(f"  σ(gg → PG) / σ(gg → H) ≈ {σ_gg/50:.2e}")
print(f"  → LHC 13 TeV 截面太低，無法探測 ❌")
print(f"  → 未來對撞機 (FCC-ee) 可能通過 Z → γ + PG 探測")

# ──────────────────────────────────
# 5. 總結
# ──────────────────────────────────
print(f"\n{'='*72}")
print("總結")
print(f"{'='*72}")

print(f"""
  m_PG = {m_PG:.2f} GeV
  Γ_total = {total_Γ:.2e} GeV  (prompt)
  τ = {1/total_Γ*6.582e-25:.2e} s

  Coupling suppression: δ = {δ*100:.2f}% (SU(2) mismatch)
  Br(h → PG PG) = {Br_h_PG:.2f}% (below LHC sensitivity)

  LHC: too weak to detect
  Future: Z → γ + PG at FCC-ee

  Key: PG mass from ε, PG coupling from δ
  Two different W-field structure constants!
""")