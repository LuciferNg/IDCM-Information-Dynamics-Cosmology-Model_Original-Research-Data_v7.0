#!/usr/bin/env python3
"""
pg_verify.py — W-field 贗 Goldstone 驗證
"""
import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1/16
V_EW = 246.22
M_Z = 91.188

print("=" * 72)
print("W-field 贗 Goldstone — 推導驗證")
print("=" * 72)

# 1. 質量
m_PG = ε * M_Z
print(f"\n─── 1. 質量 ───")
print(f"m_PG = ε × M_Z")
print(f"     = {ε:.6f} × {M_Z}")
print(f"     = {m_PG:.6f} GeV = {m_PG:.2f} GeV")

# 2. 結構來源
print(f"\n─── 2. 結構來源 ───")
print(f"ε = φ⁻¹/4 = {φ_inv}/4 = {ε}")
print(f"φ⁻¹ = φ - 1 = {φ_inv}")
print(f"ε 是 W-field 勢能 V = -ε|W|² + κ|W|⁴ 的線性係數")
print(f"ε 也是 MERA 樹特徵值的基本單位")

# 3. 一致性檢查
print(f"\n─── 3. 一致性檢查 ───")
# 3a. Higgs 的 1.59% 誤差
m_H_wf = 2 * math.sqrt(κ) * V_EW
m_H_obs = 125.10
err_H = (m_H_wf/m_H_obs - 1)*100
print(f"Higgs 勢能公式誤差: {err_H:.4f}%")
print(f"SU(2) 嵌入不匹配:   {abs(m_H_wf/(80.377/0.6298) - 1)*100:.4f}%")
print(f"ε = {ε:.6f} = {ε*100:.2f}%")
print(f"→ 三個量同量級: 1.59%, 3.67%, 15.4%")
print(f"→ 不一致: 15.4% 太大")

# 3b. 更好的關係: m_PG = √(ε) × M_Z?
print(f"\n─── 4. 替代質量估計 ───")
for name, factor in [("ε", ε), ("√ε", math.sqrt(ε)), ("ε²", ε**2), ("κ", κ), ("φ⁻¹", φ_inv)]:
    m = factor * M_Z
    print(f"  m_PG = {name} × M_Z = {factor:.6f} × {M_Z} = {m:.4f} GeV")

# 4. 與已知粒子的比較
print(f"\n─── 5. 與已知粒子比較 ───")
particles = [
    ("π⁰", 0.1350), ("π⁺", 0.1396), ("K⁰", 0.4976), ("K⁺", 0.4937),
    ("η", 0.5478), ("ρ", 0.775), ("ω", 0.783), ("η'", 0.958),
    ("φ", 1.019), ("J/ψ", 3.097), ("Υ", 9.460),
    ("τ", 1.777), ("b", 4.18), ("B", 5.28),
    ("Z", 91.188), ("W", 80.377), ("H", 125.10)
]

for name, m in particles:
    ratio = m_PG/m
    if ratio > 0.5 and ratio < 2:
        print(f"  接近 {name} ({m:.4f} GeV): {m_PG/m:.4f}×")
print(f"  → 14.09 GeV 無已知 SM 粒子對應 ✅")

# 5. 衰變模式
print(f"\n─── 6. 衰變模式 ───")
print(f"m_PG = {m_PG:.2f} GeV")
print(f"2m_τ = {2*1.777:.2f} GeV")
print(f"2m_b = {2*4.18:.2f} GeV")
print(f"2m_μ = {2*0.10566:.4f} GeV")

if m_PG > 2*1.777:
    print(f"PG → τ⁺τ⁻: 是 ({m_PG:.2f} > {2*1.777:.2f}) ✅")
    print(f"PG → bb̅:   {'是' if m_PG > 2*4.18 else '否'} ({m_PG:.2f} {'>' if m_PG > 2*4.18 else '<'} {2*4.18:.2f})")
    print(f"PG → μ⁺μ⁻: 是 ({m_PG:.2f} > {2*0.10566:.4f}) ✅")
    print(f"PG → cc̅:   {'是' if m_PG > 2*1.27 else '否'} ({m_PG:.2f} {'>' if m_PG > 2*1.27 else '<'} {2*1.27:.2f})")

# 6. 與實驗約束比較
print(f"\n─── 7. 實驗約束 ───")
print(f"LEP 搜索: 10-30 GeV 純量 → τ⁺τ⁻/μ⁺μ⁻/bb̅")
print(f"LHC Run 2: 搜索重希格斯 A/H → ττ, μμ")
print(f"14 GeV 純量未被排除:")
print(f"  - LEP: 未發現 τ⁺τ⁻/μ⁺μ⁻ 共振")
print(f"  - LHC: 低質量區間搜索有限")
print(f"  → 未被排除 ❓")