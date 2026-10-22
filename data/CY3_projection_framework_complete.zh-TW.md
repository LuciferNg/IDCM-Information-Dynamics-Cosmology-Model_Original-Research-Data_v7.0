# CY₃ 投影模型 — 完整框架

## 2026-07-29

---

## 一、框架結構

### 1.1 三層結構

```
Layer 1: 光源 — K-chain × K-tree
  γ_n = 4sin²(πn/2N_d),  μ_m = φ^(L-m)
  → 產生 44 個頻率模式

Layer 2: 鏡頭 — CY₃(36,98)
  h¹¹ = 36 = L₂² × L₃（boson 光圈）
  h²¹ = 98 = 2 × L₄²（fermion 光圈）
  CY₃ = 134 = L₂² × L₃ + 2 × L₄²
  → 將頻譜投影到 4D 粒子質量

Layer 3: 像差 — ε³ correction
  ε³ = (φ⁻¹/4)³ = 3 色像差
  → 校正投影誤差到 < 0.001%
```

### 1.2 成像公式

$$m_X = V_{EW} \cdot \frac{F_n}{CY_3^s} \cdot \varphi^B \cdot (1 + \varepsilon^3 \cdot c)$$

| 參數 | 意義 | 數值 |
|:----|:-----|:-----|
| $V_{EW}$ | 焦距 | 246.22 GeV |
| $F_n$ | 像素佔用 | Fibonacci 數 1, 3, 8 |
| $CY_3$ | 光圈總像素 | 134 |
| $s$ | sector 數量 | 1, 2, 3 |
| $\varphi^B$ | boundary correction | $\varphi^{\varphi^{-1}}, \varphi^{\varphi}, \varphi^{-11}$ |
| $\varepsilon^3$ | 3 色像差 | 0.003689 |
| $c$ | 像差係數 | $\varepsilon^3$ 級別 |

---

## 二、所有公式

### 2.1 Perfect Lens（理想投影）

$$m_X / m_{3rd} = \frac{F_n}{CY_3^s} \cdot \varphi^B$$

| 粒子 | Formula | Error |
|:----|:--------|:------|
| $m_c/m_t$ | $1/134$ | 0.94% |
| $m_s/m_b$ | $3/134$ | 0.32% |
| $m_\mu/m_\tau$ | $8/134$ | 0.70% |
| $m_u/m_t$ | $24/134^3 \cdot \varphi^{\varphi^{-1}}$ | 1.32% |
| $m_d/m_b$ | $9/134^2 \cdot \varphi^{\varphi}$ | 0.63% |
| $m_e/m_\tau$ | $8/134 \cdot \varphi^{-11}$ | 0.70% |

### 2.2 Real Lens（含像差）

$$m_X / m_{3rd} = \varphi^{-k_X}$$

| 粒子 | Formula | Error |
|:----|:--------|:------|
| $m_c/m_t$ | $\varphi^{-33\beta}$ | 0.007% |
| $m_s/m_b$ | $\varphi^{-(26\beta-\varphi^{-4})}$ | 0.007% |
| $m_\mu/m_\tau$ | $\varphi^{-19\beta}$ | 0.007% |
| 其他 | 對應 $\varphi^{-k}$ 形式 | < 0.01% |

### 2.3 理想 vs 真實嘅關係

$$\varphi^{-k_X} = \frac{F_n}{CY_3^s} \cdot \varphi^B \cdot (1 + \varepsilon^3 \cdot c_X)$$

---

## 三、k-values 同 CY₃ 嘅關係

### 3.1 M = (CY₃ - 2)/4

$$M = \frac{CY_3 - 2}{4} = \frac{134-2}{4} = 33$$

### 3.2 k-values 用 CY₃ 表達

| k | CY₃ 形式 | Pipeline 形式 | 數值 |
|:-:|:---------|:-------------|:-----|
| $k_u$ | $(CY_3-2)\beta/4$ | $M\beta$ | 10.198 |
| $k_d$ | $(CY_3-2-4L_4)\beta/4 - \varphi^{-4}$ | $(M-L_4)\beta - \varphi^{-4}$ | 7.888 |
| $k_l$ | $(CY_3-2-8L_4)\beta/4$ | $(M-2L_4)\beta$ | 5.871 |

### 3.3 CY₃ × φ^(-k) = Fibonacci

$$CY_3 \times \varphi^{-k_u} = 0.991 \approx 1 = F_1$$
$$CY_3 \times \varphi^{-k_d} = 3.010 \approx 3 = F_4$$
$$CY_3 \times \varphi^{-k_l} = 7.945 \approx 8 = F_6$$

**Fibonacci 數係 OUTPUT，唔係 INPUT。** 佢哋係 CY₃ 除以 φ^k 嘅結果，gap 係 ε³ 級別。

---

## 四、ε³ 像差嘅結構

### 4.1 每個 sector 嘅像差

| Sector | CY₃ × φ^(-k) | F_n | Gap | c = gap/ε³ |
|:-------|:------------|:---|:---|:----------|
| Up | 0.9907 | 1 | -0.0093 | -2.52 |
| Down | 3.0095 | 3 | +0.0095 | +2.58 |
| Lepton | 7.9446 | 8 | -0.0554 | -15.03 |

### 4.2 像差嘅 Lucas 分解

$$c_u \approx -\frac{F_5}{2} = -2.5$$
$$c_d \approx +\frac{F_5}{2} = +2.5$$
$$c_l \approx -(L_4 + L_3 + L_2 + L_1) = -15$$

### 4.3 像差嘅物理意義

3 色像差 = 3 個 sector 嘅焦距微小差異：
- Up sector: 焦距 slightly longer → 投影略暗
- Down sector: 焦距 slightly shorter → 投影略亮
- Lepton sector: 焦距最大偏差 → 投影最暗

---

## 五、概念驗證總結

### 5.1 正確嘅概念

| 概念 | 狀態 |
|:----|:-----|
| CY₃ = 投影儀，唔係容器 | ✅ |
| 粒子 = 能階投影 | ✅ |
| 質量 = 投影亮度 = V_EW × F_n/CY₃^s | ✅ |
| ε³ = 3 色像差 | ✅ |
| 3 代 = 3 色 truncation | ✅ |
| 1st gen = 離焦 2-3 pixels | ✅ |
| 微分唔適用（投影係積分） | ✅ |

### 5.2 未解決嘅問題

| 問題 | Status |
|:----|:-------|
| 點解 Fibonacci 係 1, 3, 8？ | 🟡 係 output，但 indices 1,4,6 嘅幾何意義未明 |
| exact ε³ 像差公式？ | 🟡 c_u, c_d, c_l 有 Lucas 分解但未 exact |
| V_EW 點從 CY₃ 幾何 derive？ | ❌ 未推導 |
| 焦距同光圈嘅 exact 關係？ | ❌ 未推導 |