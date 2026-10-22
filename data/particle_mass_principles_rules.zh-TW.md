# 粒子質量公式 — 目的、原則、規則、定義

## 2026-07-29

---

## 一、目的

**從 0,1 → φ → Lucas → CY₃ 推導所有粒子質量比，零 free parameter。**

- 每條公式必須閉合（traceable 返 φ-identity）
- 每個整數必須分解為 Lucas 數或 Fibonacci 數
- 誤差由 ε³ 像差解釋，唔係 fitting

---

## 二、原則

### 原則 1：Bedrock（基石）
一切從 0,1 開始，經 x² + x - 1 = 0 生成 φ，φ 生成所有 Lucas 數。

### 原則 2：Hierarchy（層次）
- 2nd gen：F_n / CY₃ 形式，唔需要 ε³ correction
- 1st gen：F_n / CY₃^s 形式，需要 ε³ correction
- Correction order：最高 ε³，無 ε⁴ 以上

### 原則 3：Sector（扇區）
- Up sector：k_u = 33β
- Down sector：k_d = 26β - φ⁻⁴
- Lepton sector：k_l = 19β
- 每個 sector 跳轉成本 = 7 = L₄ = JMP

### 原則 4：Symmetry（對稱）
- 2nd gen 整除於 CY₃ = 134
- 1st gen 需 CY₃² 或 CY₃³ 分母
- Mass hierarchy = projection defocus

### 原則 5：Cross-validation（交叉驗證）
- 每條公式必須 matched 到 PDG 粒子數據
- 誤差 < 0.1% 為合格（2nd gen < 1% 可接受）

### 原則 6：Convergence（收斂）
- ε³ correction 必須細（ε³ ≈ 0.0037）
- 無 ε⁴ 或更高階 correction

### 原則 7：Boundary（邊界）
- 無 singularity
- 所有分母非零
- 所有指數有限

### 原則 8：No-fitting（無擬合）
- 每個數字必須 derived，唔係 fitted
- 無裸數字
- 無 random 參數

### 原則 9：Uniqueness（唯一性）
- 每條公式只有一個可能形式
- 如果有 multiple 可能性，用 Lucas 閉合性篩選

### 原則 10：Closure（閉合）
- 每個整數必須 trace 返 φ-identity
- 使用 Lucas 數 L_n = φⁿ + (-1)ⁿφ⁻ⁿ
- 使用 Fibonacci 數 F_n

---

## 三、規則

### 規則 1：零裸數字
每個整數必須分解為 Lucas 數或 Fibonacci 數組合。

**例子：**
- 80 = N_d + h¹¹ = L₅×L₃ + L₂²×L₃ ✅
- 80 ≠ 80（裸數字） ❌

### 規則 2：φ-power 形式
質量比 = φ^(-k)，k 為 Lucas-derived exponent。

### 規則 3：2nd gen = F_n / CY₃
- m_c/m_t = F₁/CY₃ = 1/134
- m_s/m_b = F₄/CY₃ = 3/134
- m_μ/m_τ = F₆/CY₃ = 8/134
- 誤差 < 1%，無 ε³ correction

### 規則 4：1st gen = F_n / CY₃^s × (1 + ε³ × c_n/F_n)
- s = 2 for lepton, down
- s = 3 for up
- c_n = reduced correction value

### 規則 5：c values 必須有 clean Lucas 分解
- c_e' ≈ sum(L₁..L₆) + L₆×ε²
- c_d' ≈ -(2(L₁₀+L₃) + φ⁻¹)
- c_u' ≈ -(3h²¹+L₁₀+L₃) × (φ² - φ⁻³ + ε)

### 規則 6：ε³ 係物理像差，唔係 fitting
- ε³ = 3 色像差（chromatic aberration）
- 3-gen truncation
- 無 ε⁴ 以上

---

## 四、定義

### 基本常數
| 符號 | 值 | 定義 |
|:----|:---|:-----|
| φ | 1.6180339887... | (1+√5)/2，解 x² + x - 1 = 0 |
| φ⁻¹ | 0.6180339887... | 1/φ = (√5-1)/2 |
| ε | 0.1545084971... | φ⁻¹/4，sync amplitude |
| β | 0.3090169943... | φ⁻¹/2，scale exponent |
| κ | 0.0625 | 1/16 = (εφ)²，closure constant |
| ε³ | 0.003689... | (φ⁻¹/4)³，chromatic aberration |

### Lucas 數
| L_n | 值 | φ 形式 |
|:---|:---|:-------|
| L₀ | 2 | φ⁰ + φ⁰ |
| L₁ | 1 | φ¹ - φ⁻¹ |
| L₂ | 3 | φ² + φ⁻² |
| L₃ | 4 | φ³ - φ⁻³ |
| L₄ | 7 | φ⁴ + φ⁻⁴ |
| L₅ | 11 | φ⁵ - φ⁻⁵ |
| L₆ | 18 | φ⁶ + φ⁻⁶ |
| L₇ | 29 | φ⁷ - φ⁻⁷ |
| L₈ | 47 | φ⁸ + φ⁻⁸ |
| L₉ | 76 | φ⁹ - φ⁻⁹ |
| L₁₀ | 123 | φ¹⁰ + φ⁻¹⁰ |

### Fibonacci 數
F₁=1, F₂=1, F₃=2, F₄=3, F₅=5, F₆=8, F₇=13, F₈=21, F₉=34, F₁₀=55

### CY₃ 結構
| 符號 | 值 | Lucas 分解 |
|:----|:---|:-----------|
| h¹¹ | 36 | L₂² × L₃ |
| h²¹ | 98 | 2 × L₄² |
| CY₃ | 134 | L₁₀ + L₅ = h¹¹ + h²¹ |
| N_d | 44 | 2(L₅+L₄+L₃) |
| χ | -124 | -2(L₇+L₆+L₅+L₃) |
| M | 33 | (CY₃ - 2)/L₃ |

### k-values
| k | 值 | Pipeline form |
|:-:|:---|:--------------|
| k_u | 10.197561 | Mβ = 33β |
| k_d | 7.888544 | (M-L₄)β - φ⁻⁴ = 26β - φ⁻⁴ |
| k_l | 5.871323 | (M-2L₄)β = 19β |

### 粒子質量公式
#### 2nd gen（F_n/CY₃ 形式）
| 粒子 | 公式 | Error |
|:----|:-----|:------|
| m_c/m_t | 1/134 ≈ φ^(-33β) | 0.94% |
| m_s/m_b | 3/134 ≈ φ^(-(26β-φ⁻⁴)) | 0.32% |
| m_μ/m_τ | 8/134 ≈ φ^(-19β) | 0.70% |

#### 1st gen（ε³ corrected）
| 粒子 | Base | c' value | Error |
|:----|:----|:---------|:------|
| m_e/m_τ | 5/134² | 44.43005 | 0.0008% |
| m_d/m_b | 21/134² | -254.60 | 0.007% |
| m_u/m_t | 34/134³ | -1061.86 | 0.56% |

### V_EW
V_EW = M_P · φ^(-(80 - 4ε²)) · (1 + (L₅+L₃)/L₃ · φ⁻¹ · ε³) = 246.22 GeV (error 0.0011%)