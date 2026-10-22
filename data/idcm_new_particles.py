#!/usr/bin/env python3
"""
IDCM_new_particles.py — 推導新粒子候選者質量
"""
import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1/16
V_EW = 246.22
N_d = 44
L = 53/8   # tree depth
M = 33     # h¹¹ - 3
β = φ_inv / 2

print("=" * 72)
print("IDCM 新粒子候選者 — 推導")
print("=" * 72)

print(f"\n─── 基礎常數 ───")
print(f"φ = {φ:.10f}")
print(f"N_d = {N_d}")
print(f"L = {L}")
print(f"M = {M}")
print(f"V_EW = {V_EW} GeV")

# ─────────────────────────────────────────────
# 1. 鏈激發模 n=1
# ─────────────────────────────────────────────
print(f"\n{'='*72}")
print("1. K_chain 第一激發模 (n=1)")
print(f"{'='*72}")

# K_chain eigenvalues
for n in range(1, 5):
    γ_n = 4 * math.sin(math.pi * n / (2 * N_d))**2
    # 質量 = γ_n × φ^L × V_EW
    m_n = γ_n * φ**L * V_EW
    print(f"  n={n}: γ_n = {γ_n:.8f}, m_n = {m_n:.4f} GeV = {m_n:.2f} GeV")

# 但這可能不是正確公式。γ_n 是 K_chain 特徵值，但物理質量需要乘以對應的耦合。
# 在費米子扇區，質量 = γ_n × μ_m × V_EW，其中 γ_n 來自 K_chain，μ_m 來自 K_tree。
# 但鏈激發是純量，它的質量公式可能不同。

# 另一個思路：鏈激發是 K_chain 圖上的玻色子，質量由 K_chain + K_tree 特徵值決定
# 類似於 K = K_chain ⊗ K_tree 的張量積結構
# 對純量，特徵值 = γ_n × μ_m，其中 μ_m 是 K_tree 的基態

# K_tree 基態特徵值
# 樹的離散拉普拉斯算子特徵值：μ_m = 2 - 2cos(πm/(N_h+1))
N_h = 42
for m in [1, 2]:
    μ_m = 2 - 2*math.cos(math.pi*m/(N_h+1))
    print(f"  K_tree μ_{m} = {μ_m:.8f}")

# 對 n=1, m=1: 張量積特徵值
print(f"\n  K_chain ⊗ K_tree 張量積:")
for n in [1, 2]:
    γ_n = 4 * math.sin(math.pi * n / (2 * N_d))**2
    for m in [1, 2]:
        μ_m = 2 - 2*math.cos(math.pi*m/(N_h+1))
        λ_nm = γ_n * μ_m
        # 物理質量需要用 V_EW 標度，並乘以 φ^L 的樹深度因子
        # 但對於鏈-樹張量積的純量模，公式可能不同於費米子
        m_nm = λ_nm * φ**L * V_EW
        print(f"  n={n}, m={m}: λ = {λ_nm:.8f}, m = {m_nm:.4f} GeV = {m_nm:.2f} GeV")

# ─────────────────────────────────────────────
# 2. 贗 Goldstone 玻色子（類軸子）
# ─────────────────────────────────────────────
print(f"\n{'='*72}")
print("2. 贗 Goldstone 玻色子（類軸子）")
print(f"{'='*72}")

# W-field 有全域 U(1) 對稱性 W → e^{iα}W
# VEV 破缺 → Goldstone 模式
# 在 SU(2) 嵌入中，這個 Goldstone 被 Z 吃掉
# 但如果 SU(2) 嵌入有微小破缺，留下贗 Goldstone

# 破缺參數來自 SU(2) 嵌入的 3.6% 不匹配
δ = 0.0366  # 3.66% 不匹配
# 贗 Goldstone 質量 ≈ √(δ) × m_Z
m_PG = math.sqrt(δ) * 91.188
print(f"  SU(2) 嵌入不匹配: δ = {δ:.4f} ({δ*100:.2f}%)")
print(f"  贗 Goldstone 質量 ≈ √(δ) × M_Z")
print(f"                     = √({δ:.4f}) × 91.188")
print(f"                     = {math.sqrt(δ):.4f} × 91.188")
print(f"                     = {m_PG:.4f} GeV = {m_PG:.2f} GeV")

# 檢查是否接近已知粒子
print(f"\n  質量 {m_PG:.2f} GeV 接近:")
print(f"  - 無已知粒子在此範圍")
print(f"  - 低於 Z 質量 (91 GeV)")
print(f"  - 遠高於輕子質量")

# 另一個破缺尺度：φ⁻¹ × m_Z
print(f"\n  替代估計:")
for name, factor in [("φ⁻¹/2", 0.5*φ_inv), ("φ⁻¹", φ_inv), ("ε", ε), ("κ", κ)]:
    m = factor * 91.188
    print(f"  m = {name} × M_Z = {factor:.6f} × 91.188 = {m:.4f} GeV")

# ─────────────────────────────────────────────
# 3. K_chain 零模殘留
# ─────────────────────────────────────────────
print(f"\n{'='*72}")
print("3. K_chain 零模 (n=0)")
print(f"{'='*72}")

# n=0 是 Goldstone 零模
# 但如果 K_chain 有邊界條件修正，零模有小質量
# 邊界條件修正 ≈ 1/N_d
δ_boundary = 1/N_d
m_zero = δ_boundary * φ**L * V_EW
print(f"  邊界修正: 1/N_d = 1/{N_d} = {δ_boundary:.6f}")
print(f"  零模質量 = (1/N_d) × φ^L × V_EW")
print(f"           = {δ_boundary} × {φ**L:.4f} × {V_EW}")
print(f"           = {m_zero:.4f} GeV = {m_zero:.2f} GeV")

# ─────────────────────────────────────────────
# 4. 總結
# ─────────────────────────────────────────────
print(f"\n{'='*72}")
print("總結：新粒子候選者")
print(f"{'='*72}")

candidates = [
    ("K_chain n=1, m=1", "張量積特徵值", 4*math.sin(math.pi/(2*N_d))**2 * (2-2*math.cos(math.pi/(N_h+1))) * φ**L * V_EW, "暗物質"),
    ("K_chain n=1, m=2", "張量積特徵值", 4*math.sin(math.pi/(2*N_d))**2 * (2-2*math.cos(2*math.pi/(N_h+1))) * φ**L * V_EW, "暗物質"),
    ("贗 Goldstone", "SU(2) 破缺", math.sqrt(0.0366)*91.188, "類軸子/暗物質"),
    ("零模殘留", "邊界條件", (1/N_d)*φ**L*V_EW, "暗物質"),
]

print(f"\n  {'候選者':25s} {'公式':35s} {'質量 (GeV)':15s} {'角色':15s}")
print(f"  {'-'*25} {'-'*35} {'-'*15} {'-'*15}")
for name, source, mass, role in candidates:
    print(f"  {name:25s} {source:35s} {mass:<15.2f} {role:15s}")

# 比較已知粒子
print(f"\n  與已知粒子比較:")
known = [("ν_e", 0), ("e", 0.000511), ("μ", 0.10566), ("τ", 1.77686),
         ("u", 0.0022), ("d", 0.0047), ("s", 0.095), ("c", 1.27),
         ("b", 4.18), ("t", 172.76), ("Higgs", 125.10), ("Z", 91.188),
         ("W", 80.377)]

for name, m in known:
    for cname, _, cmass, role in candidates:
        if abs(cmass/m - 1) < 0.5 or abs(m/cmass - 1) < 0.5:
            print(f"  {cname:25s} {cmass:8.2f} GeV  ~  {name:10s} {m:8.4f} GeV  ({abs(cmass/m-1)*100:.1f}%)")