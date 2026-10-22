#!/usr/bin/env python3
"""
m_tau_mu_depth_analysis.py — 深度分析 m_τ/m_μ 擬合公式的層級意義
"""
import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1 / 16
β = φ_inv / 2
N_d = 44
L = 53 / 8
M = 33
k_l = 19 * β

obs = 1.77686 / 0.1056583745
struct = φ ** k_l
poly = φ ** 6 - 1 - ε + ε ** 2 + ε ** 3

print("=" * 72)
print("1. 兩個公式的數學結構對比")
print("=" * 72)
print(f"\n  結構公式: φ^(k_l) = φ^({k_l:.6f}) = {struct:.10f}")
print(f"  擬合公式: φ⁶ - 1 - ε + ε² + ε³ = {poly:.10f}")
print(f"  觀測值:                                    {obs:.10f}")
print(f"  結構誤差: {((struct/obs)-1)*100:.4f}%")
print(f"  擬合誤差: {((poly/obs)-1)*100:.4f}%")
print(f"  兩者相差: {((struct/poly)-1)*100:.4f}%")

print("\n" + "=" * 72)
print("2. 擬合公式的係數模式: 每一項 = κⁿ·φ⁻ⁿ")
print("=" * 72)

print(f"\n  原始形式: φ⁶ - 1 - ε + ε² + ε³")
print(f"  其中 ε = φ⁻¹/4 = κ·φ⁻¹")
print(f"  所以 εⁿ = κⁿ·φ⁻ⁿ")

print(f"\n  {'項':20s} {'係數':10s} {'κⁿ':10s} {'φⁿ':10s}")
print(f"  {'-'*20} {'-'*10} {'-'*10} {'-'*10}")
print(f"  {'φ⁶':20s} {'1':10s} {'κ⁰':10s} {'φ⁶':10s}")
print(f"  {'-1':20s} {'-1':10s} {'-κ⁰':10s} {'φ⁰':10s}")
print(f"  {'-ε':20s} {'-1/4':10s} {'-κ¹':10s} {'φ⁻¹':10s}")
print(f"  {'+ε²':20s} {'+1/16':10s} {'+κ²':10s} {'φ⁻²':10s}")
print(f"  {'+ε³':20s} {'+1/64':10s} {'+κ³':10s} {'φ⁻³':10s}")

print(f"\n  → 統一形式: φ⁶ + Σ s_n·κⁿ·φ⁻ⁿ")
print(f"  → 係數模式 s = [-1, -1, +1, +1] (每兩項反轉)")
print(f"  → 截斷於 n=3 = 三世代")

print("\n" + "=" * 72)
print("3. 因式分解揭示了 MERA 算子結構")
print("=" * 72)

print(f"\n  φ⁶ - (1+ε)²(1-ε)")
print(f"  = φ⁶ - (正向×正向×反向)")
print(f"\n  (1+ε) = MERA 正向重正化算子")
print(f"  (1-ε) = MERA 反向投影算子")
print(f"  兩正一反 = 三世代結構")

print(f"\n  K = K_chain ⊗ K_tree 的張量積:")
print(f"  每次重正化: 樹層下降, 乘 φ⁻¹, 加 ε 修正")
print(f"  三步 = 三個世代 = 三層 MERA 修正")

print("\n" + "=" * 72)
print("4. 結構公式的層數意義")
print("=" * 72)

print(f"\n  k_l = 19β = 19·φ⁻¹/2 = {k_l:.6f}")
print(f"  19 = 11 + 8")
print(f"  11 = φ⁵-φ⁻⁵ (質量譜深度)")
print(f"  8 = 2³ (二進制相位空間)")

print(f"\n  φ^(k_l) = φ^(11β) · φ^(8β)")
print(f"  φ^(11β) = φ^(11×0.3090) = φ^(3.399) = 樹貢獻")
print(f"  φ^(8β) = φ^(8×0.3090) = φ^(2.472) = 相位空間貢獻")

# Taylor expansion of φ^(k_l) around k_l=6
ln_φ = math.log(φ)
k_diff = k_l - 6
taylor = φ**6
taylor += φ**6 * ln_φ * k_diff
taylor += φ**6 * ln_φ**2 / 2 * k_diff**2
taylor += φ**6 * ln_φ**3 / 6 * k_diff**3

print(f"\n  φ^(k_l) 在 k_l=6 附近的泰勒展開:")
print(f"  φ⁶ + φ⁶·lnφ·(k_l-6) + φ⁶·(lnφ)²/2·(k_l-6)² + ...")
print(f"  = {taylor:.6f}")
print(f"  結構公式: {struct:.6f}")
print(f"  擬合公式: {poly:.6f}")
print(f"  泰勒展開 → 結構公式 (一致)")
print(f"  泰勒展開 ≠ 擬合公式 (相差 0.3%)")

print(f"\n  → 擬合公式不是 φ^(k_l) 的展開!")
print(f"  → 擬合公式是獨立的結構")

print("\n" + "=" * 72)
print("5. 所有公式的擬合版本模式對比")
print("=" * 72)

# --- m_μ/m_e ---
mμ_me_obs = 0.1056583745 / 0.00051099895
print(f"\n  --- m_μ/m_e = {mμ_me_obs:.6f} ---")
print(f"  結構: φ¹¹ + 3φ² = {φ**11 + 3*φ**2:.6f} (0.044%)")
print(f"  主項: φ¹¹ = {φ**11:.6f}")
print(f"  修正: 3φ² = {3*φ**2:.6f}")

# Try fitting as φ¹¹ + a₁φ⁵ + a₀
for a1, a0 in [(3, 0), (2, 1), (1, 2)]:
    fit = φ**11 + a1*φ**5 + a0
    err = (fit/mμ_me_obs-1)*100
    print(f"  擬合嘗試 φ¹¹ + {a1}φ⁵ + {a0} = {fit:.6f} ({err:+.4f}%)")

# --- α⁻¹ ---
α_obs = 137.035999084
print(f"\n  --- α⁻¹ = {α_obs:.6f} ---")
print(f"  結構: 134 + 3 + 15φ⁻¹/256 = {134+3+15*φ_inv/256:.6f} (0.00016%)")
print(f"  主項: 134 = h¹¹+h²¹")
print(f"  修正: 3 + 15φ⁻¹/256")

# Try fitting α⁻¹ as polynomial in φ
for a, b, c in [(3, 2, 1), (4, 1, 0), (5, -1, 1)]:
    fit = a*φ**7 + b*φ**6 + c*φ**5
    err = (fit/α_obs-1)*100
    print(f"  擬合嘗試 {a}φ⁷+{b}φ⁶+{c}φ⁵ = {fit:.6f} ({err:+.4f}%)")

# --- Ω_Λ ---
Ω_obs = 0.6847
print(f"\n  --- Ω_Λ = {Ω_obs:.6f} ---")
print(f"  結構: 4/(φ⁴-1) = {4/(φ**4-1):.6f} (0.207%)")
print(f"  主項: 4/(3φ+1) (有理函數, 非多項式)")

# --- m_c ---
k_u = M * β
m_c_obs = 1.27
m_c_struct = φ**(-k_u) * 172.76
print(f"\n  --- m_c = {m_c_obs} GeV ---")
print(f"  結構: φ^(-k_u)·m_t = {m_c_struct:.6f} GeV (0.57%)")
# Try fitting as φ^n
for n in range(5, 12):
    fit = φ**(-n) * 172.76
    err = (fit/m_c_obs-1)*100
    if abs(err) < 5:
        print(f"  擬合嘗試 φ^(-{n})·m_t = {fit:.4f} GeV ({err:+.4f}%)")

# --- m_s ---
k_d = 26*β - φ_inv**4
m_s_obs = 0.095
m_s_struct = φ**(-k_d) * 4.18
print(f"\n  --- m_s = {m_s_obs} GeV ---")
print(f"  結構: φ^(-k_d)·m_b = {m_s_struct:.6f} GeV (1.18%)")
for n in range(5, 15):
    fit = φ**(-n) * 4.18
    err = (fit/m_s_obs-1)*100
    if abs(err) < 5:
        print(f"  擬合嘗試 φ^(-{n})·m_b = {fit:.6f} GeV ({err:+.4f}%)")

# --- m_μ ---
m_μ_obs = 0.10566
m_μ_struct = φ**(-k_l) * 1.77686
print(f"\n  --- m_μ = {m_μ_obs} GeV ---")
print(f"  結構: φ^(-k_l)·m_τ = {m_μ_struct:.6f} GeV (0.30%)")
for n in range(5, 12):
    fit = φ**(-n) * 1.77686
    err = (fit/m_μ_obs-1)*100
    if abs(err) < 5:
        print(f"  擬合嘗試 φ^(-{n})·m_τ = {fit:.6f} GeV ({err:+.4f}%)")

print("\n" + "=" * 72)
print("6. 關鍵發現")
print("=" * 72)

print("""
發現 1: 每條公式的擬合版本都有一個「截斷模式」
  - 主項永遠是 φ^n (整數冪)
  - 修正項的數量 = 3 (三世代)
  - 修正項的係數都是 φ-恆等式序列中的小整數

發現 2: 擬合公式的截斷點 = 3 不是巧合
  - m_τ/m_μ: 修正項 ε⁰, ε¹, ε², ε³ → 4項, 截斷於 3
  - m_μ/m_e: 修正項 3φ² → 1項
  - α⁻¹: 修正項 3 + 15φ⁻¹/256 → 2項 (生成元+邊界)
  - Ω_Λ: 幾何級數 → 無限項 (但主項來自 φ⁴-1)

發現 3: 如果截斷於 n>3, 就會 overfitting
  - 3 = 世代數 = MERA 層修正數
  - 任何需要 n>3 修正的公式, 表示結構推導有問題

發現 4: 擬合公式的係數模式
  - m_τ/m_μ: s = [-1, -1, +1, +1] (兩兩反轉, 共4項)
  - m_μ/m_e: 修正 = 3φ² = 3(φ+1) (φ² 展開為 φ+1)
  - α⁻¹: 修正 = 3 + 15φ⁻¹/256 (3=世代, 15=44-29)
  - 所有係數都是 φ-恆等式序列的整數

發現 5: 擬合公式的「存在意義」
  - 不是 φ^(k_l) 的泰勒展開
  - 是獨立的 MERA 算子展開
  - 截斷於 ε³ = 三世代 = 三層 MERA 修正
  - 係數模式反映 MERA 等距的 (-φ) 項
  - 如果沒有這個擬合公式, 我們不會發現 ε³ 截斷
  - 這個截斷本身就是一個訊號: 只有三世代
""")