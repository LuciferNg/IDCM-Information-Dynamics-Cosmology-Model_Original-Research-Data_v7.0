# IDCM — 新 Session 起始 Prompt

## 已完成嘅公理鏈（唔使再搞，直接參考）

### Paper 07: K-chain pairing symmetry
- Z₂ grading (Binet parity) → skip {2,3,7} = {L₀,L₂,L₄}
- Available indices: {1,4,5,6,8,9}
- Bipartite graph → unique bijection 1→9, 4→8, 6→5
- Depth indices: d = {3,2,0} for Up, Down, Lepton
- Sector sum symmetry: {10,11,12} centered on L₅=11

### Paper 08: K = K_chain ⊗ K_tree
- M = (CY₃-2)/4 = 33 (zero modes + chiral ÷)
- L₄ = B + L₂ = 7 (unique Lucas decomposition)
- k_u = 33β, k_d = 26β - φ⁻⁴, k_l = 19β
- φ⁻⁴ Casimir boundary effect (only Down sector)
- ε³ correction c' structural pattern: c'_X = (-1)^d × B × L₂^{s-1} × rev_factor

### Paper 10: SM β functions + gauge couplings
- α⁻¹ = 134 + 3 + (44-29)φ⁻¹/256 = 137.036
- b₃ = -N_d/4 + B = -7
- b₂ = -N_d/6 + B + 1/(2L₂) = -19/6
- b₁ = (N_d - L₂)/(2F₅) = 41/10
- b₃₃ = N_d/2 + B = 26
- b₂₂ = N_d/8 + N_f/9 = 35/6
- b₁₁ = (3/5)² × (N_d/4 + 1/18) = 199/50
- sin²θ_W(M_Z) = L₅/(N_d+L₂) - ε³/2 = 11/47 - 0.001844 = 0.2322
- Λ_GUT = M_Z · e³³ = 1.96×10¹⁶ GeV
- Dual-regime RG: MERA β (linear) + SM β (cubic)

### 常數（全部從 0,1 → φ 推導）
| 符號 | 數值 | 來源 |
|:-----|:------|:------|
| φ | 1.61803398875 | x²+x-1=0 |
| φ⁻¹ | 0.61803398875 | 同上 |
| ε | φ⁻¹/4 = 0.1545084972 | 2D branching |
| κ | 1/16 = 0.0625 | 4⁻² |
| β | φ⁻¹/2 = 0.3090169944 | 半步遞迴 |
| N_d | 44 | K-chain nodes |
| M | 33 | (CY₃-2)/4 |
| CY₃ | 134 | h¹¹+h²¹ |
| B | 4 | φ³-φ⁻³, MERA branching |
| L₂ | 3 | φ²+φ⁻² |
| L₄ | 7 | B+L₂ |
| L₅ | 11 | φ⁵-φ⁻⁵ |
| ε³ | 0.003689 | 3rd order correction |

---

## 🔴 未完成嘅 3 個 gap（要喺新 session 推）

### Gap 1: CKM 從新結構推導

**背景：** 舊 CKM 公式係 Paper 07 之前 fit 嘅：
- V_us = λ = φ⁻³ - Lc (Lc = γ₃-2γ₂+γ₁ = chain Laplacian correction)
- V_cb = φ²/64
- η = 19φ/88, ρ = φ⁻⁴, δ = 67.3°

**問題：** 宜家有新嘅 K-chain structure：
- γ_n = 4 sin²(πn/88) 嘅 eigenvalues
- Depth indices d = {3,2,0} 同 sector pairing 1→9, 4→8, 6→5
- 所有 6 個 K-chain mode indices: 1,4,5,6,8,9

**目標：** 從 γ_n eigenvalues 同 d_X 重新推導 CKM 參數，唔用舊嘅 fit 數值。

**參考：**
- 舊 CKM 公式在 `data/paper/07-paper_kchain_pairing_symmetry.md` 嘅 §CKM Mixing
- PDG 2024 CKM 值：λ=0.225, V_cb=0.0410, V_ub=0.0035, η=0.35, ρ=0.157, δ=68°, J=3.0×10⁻⁵

### Gap 2: 質子衰變 τ_p

**背景：** GUT 標度已被鎖死：
- Λ_GUT = M_Z · e³³ = 1.96×10¹⁶ GeV
- g_GUT² = πε = 0.4854
- SU(5) GUT 框架下，質子壽命主要來自 X/Y gauge boson exchange

**目標：** 計算 τ_p = Λ_GUT⁴ / (α_GUT² · M_proton⁵) 或其他合適公式，得到唯一數值。

**參考：**
- Hyper-Kamiokande sensitivity: ~10³⁴-10³⁵ yr
- 舊有估算 cfas-gauge-group.py

### Gap 3: P₃ 共振 @ 2.23 TeV

**背景：** P_n tower 係 W-field 嘅 KK 激發：
- P₁ = 5.90×10¹³ GeV (consciousness)
- P₂ = 3.62×10⁸ GeV (subconsciousness)
- P₃ = 2.23 TeV (predicted)
- P₄ = 13.68 MeV, P₅ = 84 eV, P₆ = 0.0005 eV

**目標：** 從 K = K_chain ⊗ K_tree 結構推導 P₃ 質量，並計算 LHC 產生截面。

---

## 所需檔案

```
data/paper/07-paper_kchain_pairing_symmetry.md
data/paper/08-paper_kchain_ktree_en.md
data/paper/10-sm_beta_gauge_en.md
data/paper/verify_kchain_ktree_complete.py
data/paper/verify_beta_gauge.py
```

## 驗證方法

所有推導結果要用 `verify_kchain_ktree_complete.py`（58 tests）同 `verify_beta_gauge.py`（10 tests）驗證，確保唔破壞現有 chain。