# K-Chain 配對對稱性與 Defocus s — 費米子質量階層的幾何起源

## 從 Temperley-Lieb 代數到 CY₃ 投影的結構推導

### L. Ng

---

## Abstract

The CY₃ projection model expresses fermion mass ratios as $m_X = V_{EW} \cdot F_n / CY_3^s$, where $F_n$ is a Fibonacci number and $s$ is the defocus parameter. The values of $s$ — 1 for second-generation particles and 2,3 for first-generation particles — have been empirically observed but not structurally derived. We demonstrate that the defocus parameter $s$ is determined entirely by the pairing symmetry of the K-chain Laplacian eigenmodes, governed by three nested mathematical structures:

1. **Temperley-Lieb algebra** $TL_N(q)$ with $q = e^{i\pi/44}$ — the K-chain Laplacian eigenvalues $\gamma_n = 4\sin^2(\pi n/88)$ are the spectrum of the $TL_{44}(q)$ transfer matrix at a root of unity, where Fibonacci and Lucas numbers appear naturally.

2. **$\mathbb{Z}_2$ grading** — the Binet formula $L_n = \varphi^n + (-\varphi)^{-n}$ forces even-indexed Lucas numbers $\{L_0, L_2, L_4\} = \{2, 3, 7\}$ to be parity-even (bosonic, symmetric) and odd-indexed Lucas numbers $\{L_1, L_3\} = \{1, 4\}$ to be parity-odd (fermionic, antisymmetric). The even-indexed Lucas numbers are forbidden by a $\mathbb{Z}_2$ selection rule, leaving the available K-chain mode indices $\{1, 4, 5, 6, 8, 9\}$.

3. **Coxeter $A_{87}$ outer automorphism** — the Dirac pairing $n \leftrightarrow 44-n$ with $\gamma_n + \gamma_{44-n} = 4$ corresponds to the Dynkin diagram outer automorphism of $A_{87}$, representing chiral symmetry.

The partition $\{1, 4, 6\} \to s=1$ and $\{5, 8, 9\} \to s=2,3$ is determined by the tree depth $k_X$: deeper tree depth (larger $k_X = 33\beta, 26\beta, 19\beta$) yields larger gap $\Delta n = 8, 4, 1 = 2^{k_X/L_5}$, and larger gap requires larger $s$. The lepton sector exhibits a forced reversal ($6\to5$ instead of $6\to7$) because $7 = L_4$ is forbidden by the $\mathbb{Z}_2$ selection rule, demonstrating that the reversal is structurally necessary, not arbitrary.

The sector sums $1+9=10$, $4+8=12$, $6+5=11$ are centered on $L_5 = 11$, establishing the lepton sector as the symmetry origin of the mass hierarchy.

---

## 1. 引言

### 1.1 問題

CY₃ 投影模型將費米子質量比表述為：

$$m_X = V_{EW} \cdot \frac{F_n}{CY_3^s} \cdot \varphi^B \cdot (1 + \varepsilon^3 \cdot c_X)$$

其中 $F_n$ 是 Fibonacci 數，$CY_3 = 134$ 是 Calabi-Yau 三折叠的總 Hodge 數，$s$ 是 defocus 參數。經驗觀察顯示：

| Generation | s | 粒子 | Fibonacci index n | F_n |
|:----------:|:-:|:----|:-----------------:|:---:|
| 2nd (s=1) | 1 | c, s, μ | 1, 4, 6 | 1, 3, 8 |
| 1st (s=2) | 2 | d, e | 8, 5 | 21, 5 |
| 1st (s=3) | 3 | u | 9 | 34 |

但 $s$ 的數值為何如此分配，至今未有結構推導。

### 1.2 方法

我們從 K-chain 的圖 Laplacian 特徵值出發：

$$\gamma_n = 4\sin^2\left(\frac{\pi n}{2N_d}\right), \quad N_d = 44$$

並證明 $s$ 由三個嵌套的數學結構決定：
1. Temperley-Lieb 代數 $TL_N(q)$ 在單位根 $q = e^{i\pi/44}$ 的表示
2. $\mathbb{Z}_2$ grading（Binet 公式 parity）
3. Coxeter $A_{87}$ 外自同構（Dirac pairing）

---

## 2. 預備知識

### 2.1 基本常數

| 符號 | 數值 | 來源 | 角色 |
|:----:|:----:|:-----|:-----|
| $\varphi$ | $(1+\sqrt{5})/2 = 1.61803398875$ | $x^2+x-1=0$ | 全局遞迴基底 |
| $\varphi^{-1}$ | $\varphi-1 = 0.61803398875$ | 同上 | 遞迴比 |
| $\varepsilon$ | $\varphi^{-1}/4 = 0.1545084972$ | 2D branching | W-field 注入強度 |
| $\kappa$ | $1/16 = 0.0625$ | $4^{-2}$ | 量子重力量子 |
| $\beta$ | $\varphi^{-1}/2 = 0.3090169944$ | 半步遞迴 | Sync 步長 |
| $N_d$ | 44 | $N_d = 4 \times 11$ | K-chain 節點數 |
| $M$ | 33 | $M = (CY_3 - 2)/4$ | 管線係數 |
| $CY_3$ | 134 | $h^{11}+h^{21} = 36+98$ | CY₃ 總 Hodge 數 |

### 2.2 $\varphi$-Identity 序列

對於奇數 $n$，$\varphi^n - \varphi^{-n} \in \mathbb{Z}$：

| $n$ | 值 | 角色 |
|:---:|:--:|:-----|
| 1 | **1** | 基底 identity |
| 3 | **4** | MERA 分支因子 $B$ |
| 5 | **11** | $L_5$，因果域基底 |
| 7 | **29** | 第二閉合層 |
| 9 | **76** | 第三閉合層 |
| 11 | **199** | 最高閉合層 |

### 2.3 Lucas 數列

Lucas 數由 $L_n = \varphi^n + (-\varphi)^{-n}$ 給出：

| $n$ | $L_n$ | Parity | 角色 |
|:---:|:-----:|:------:|:-----|
| 0 | 2 | even | 基本模式 |
| 1 | **1** | odd | 使用，s=1 |
| 2 | **3** | even | **跳過** |
| 3 | **4** | odd | 使用，s=1 |
| 4 | **7** | even | **跳過** |
| 5 | 11 | odd | 對稱中心 |
| 6 | 18 | even | — |
| 7 | 29 | odd | — |
| 8 | 47 | even | — |
| 9 | 76 | odd | — |
| 10 | 123 | even | — |

### 2.4 Fibonacci 數列

| $n$ | $F_n$ | 使用 | s |
|:---:|:-----:|:----:|:-:|
| 1 | 1 | ✅ | 1 |
| 2 | 1 | ❌ | degenerate |
| 3 | 2 | ❌ | — |
| 4 | 3 | ✅ | 1 |
| 5 | 5 | ✅ | 2 |
| 6 | 8 | ✅ | 1 |
| 7 | 13 | ❌ | — |
| 8 | 21 | ✅ | 2 |
| 9 | 34 | ✅ | 3 |

---

## 3. K-Chain 的 Temperley-Lieb 代數結構

### 3.1 圖 Laplacian 與 TL_N(q) 譜

K-chain 是 $N_d = 44$ 個節點的簡單路徑圖。其 Laplacian 矩陣的特徵值為：

$$\gamma_n = 4\sin^2\left(\frac{\pi n}{2N_d}\right), \quad n = 1, 2, \ldots, N_d$$

這恰好是 Temperley-Lieb 代數 $TL_{44}(q)$ 在單位根 $q = e^{i\pi/44}$ 的轉移矩陣譜。在 Temperley-Lieb 代數中，特徵值對應於量子維度（quantum dimensions）的平方。

### 3.2 Dirac Pairing 與 Coxeter 外自同構

K-chain 滿足互補配對：

$$n \leftrightarrow N_d - n = 44 - n$$

特徵值滿足：

$$\gamma_n + \gamma_{44-n} = 4$$

幾何上，這對應於 Coxeter 群 $A_{87}$（87 個節點的 Dynkin diagram）的**外自同構**（outer automorphism），即 Dynkin diagram 的反射對稱性。物理上，這對應於手徵對稱性（chiral symmetry）或粒子-空穴對稱性（particle-hole symmetry）。

**定理 1（Dirac Pairing）**：K-chain 的互補配對 $n \leftrightarrow 44-n$ 生成 Dirac 2-分量旋量結構 $\Psi_n = (\varphi_n, \varphi_{44-n})^T$，其中 $\gamma_n + \gamma_{44-n} = 4 = B = \varphi^3 - \varphi^{-3}$ 是 MERA 分支因子。

---

## 4. $\mathbb{Z}_2$ Grading：奇偶 Lucas 選擇定則

### 4.1 Binet 公式的 Parity

Binet 公式給出 Lucas 數的閉合形式：

$$L_n = \varphi^n + (-\varphi)^{-n}$$

對於不同的 $n$ parity：

- **$n$ 偶數**（$n = 2k$）：$(-\varphi)^{-n} = \varphi^{-n}$，因此 $L_{2k} = \varphi^{2k} + \varphi^{-2k}$，**正號** → 對稱（玻色子）
- **$n$ 奇數**（$n = 2k+1$）：$(-\varphi)^{-n} = -\varphi^{-n}$，因此 $L_{2k+1} = \varphi^{2k+1} - \varphi^{-(2k+1)}$，**負號** → 反對稱（費米子）

**定理 2（$\mathbb{Z}_2$ Selection Rule）**：在 1-9 的範圍內，偶數-indexed Lucas numbers $\{L_0, L_2, L_4\} = \{2, 3, 7\}$ 被 $\mathbb{Z}_2$ grading 禁制（對稱/玻色子 sector），而奇數-indexed Lucas numbers $\{L_1, L_3\} = \{1, 4\}$ 被准許且 $s=1$（反對稱/費米子 sector）。

### 4.2 可用 Indices

經過 $\mathbb{Z}_2$ 選擇定則後，1-9 中可用的 K-chain mode indices 為：

$$\{1, 4, 5, 6, 8, 9\}$$

跳過的 indices 為 $\{2, 3, 7\} = \{L_0, L_2, L_4\}$，其和為 $12 = 3 \times 4 = L_2 \times B$。

---

## 5. Bipartite Graph Analysis：配對唯一性證明

### 5.1 問題重述

給定兩組 indices：

- **Group A**（s=1, focused）：$\{1, 4, 6\}$，sum $= 11 = L_5$
- **Group B**（s=2,3, defocused）：$\{5, 8, 9\}$，sum $= 22 = 2L_5$

需要找到一個 bijection $f: A \to B$，將每個 $a \in A$ 配對到唯一的 $b \in B$，滿足：

1. **Gap 條件**：$\Delta n = |b - a|$ 必須是 $2^d$ 形式（二進制拓撲深度）
2. **$\mathbb{Z}_2$ 條件**：$\Delta n$ 不能是偶數-indexed Lucas number（即 $\Delta n \notin \{L_0, L_2, L_4, \ldots\} = \{2, 3, 7, 18, \ldots\}$）

### 5.2 Bipartite Graph

構造二分圖 $G = (A \cup B, E)$，其中邊 $(a, b) \in E$ 若且唯若滿足上述兩個條件：

| $A$ \ $B$ | 5 | 8 | 9 |
|:----------:|:-:|:-:|:-:|
| **1** | $\Delta n=4=2^2$ ✅ | $\Delta n=7=L_4$ ❌ | $\Delta n=8=2^3$ ✅ |
| **4** | $\Delta n=1=2^0$ ✅ | $\Delta n=4=2^2$ ✅ | $\Delta n=5$ ❌ |
| **6** | $\Delta n=1=2^0$ ✅ | $\Delta n=2=L_0$ ❌ | $\Delta n=3=L_2$ ❌ |

**允許的邊**（共 5 條）：
- $1 \to 5$（gap $= 4 = 2^2$）
- $1 \to 9$（gap $= 8 = 2^3$）
- $4 \to 5$（gap $= 1 = 2^0$）
- $4 \to 8$（gap $= 4 = 2^2$）
- $6 \to 5$（gap $= 1 = 2^0$）

**禁止的邊**（共 4 條）：
- $1 \to 8$（gap $= 7 = L_4$，$\mathbb{Z}_2$ 禁制）
- $4 \to 9$（gap $= 5$，不是 $2^d$）
- $6 \to 8$（gap $= 2 = L_0$，$\mathbb{Z}_2$ 禁制）
- $6 \to 9$（gap $= 3 = L_2$，$\mathbb{Z}_2$ 禁制）

### 5.3 唯一 Bijection

從允許的 5 條邊中，尋找使用所有 6 個 indices 恰好一次的 bijection：

**唯一解**：
$$
1 \xrightarrow{8} 9,\quad 4 \xrightarrow{4} 8,\quad 6 \xrightarrow{1} 5
$$

**證明**：
- $6$ 只連到 $5$（唯一鄰居），所以 $6 \to 5$ 強制
- $1$ 連到 $\{5, 9\}$，但 $5$ 已被 $6$ 佔用，所以 $1 \to 9$ 強制
- $4$ 連到 $\{5, 8\}$，但 $5$ 已被 $6$ 佔用，所以 $4 \to 8$ 強制

**定理 3（配對唯一性）**：給定 $\mathbb{Z}_2$ selection rule 和 gap 的二進制條件，K-chain 的 sector pairing 是唯一確定的，沒有其他可能性。

### 5.4 深度指數

從唯一配對得到每個 sector 的深度指數 $d_X$：

| Sector | 配對 | Gap | $d_X = \log_2(\text{Gap})$ | 物理意義 |
|:-------|:----:|:---:|:--------------------------:|:---------|
| Up | $1 \leftrightarrow 9$ | $8 = 2^3$ | **3** | 最深層，最大質量分裂 |
| Down | $4 \leftrightarrow 8$ | $4 = 2^2$ | **2** | 中層 |
| Lepton | $6 \leftrightarrow 5$ | $1 = 2^0$ | **0** | 對稱中心，點狀粒子 |

**注意**：$6 \to 5$ 是反向配對，因為正向 $6 \to 7$ 被 $\mathbb{Z}_2$ 禁制（$7 = L_4$）。這稱為 **Lepton Reversal**（見第 6 節）。

---

## 6. Sector Pairing 與 Lepton Reversal

### 6.1 Sector Assignment

從唯一 bijection 得到三個 sector 的完整配對：

| Sector | 2nd gen (s=1) | 1st gen | s | Gap | $d_X$ |
|:-------|:------------:|:--------:|:-:|:---:|:-----:|
| **Up** | $n=1$ ($F_1=1$, $m_c/m_t$) | $n=9$ ($F_9=34$, $m_u/m_t$) | 3 | $8 = 2^3$ | 3 |
| **Down** | $n=4$ ($F_4=3$, $m_s/m_b$) | $n=8$ ($F_8=21$, $m_d/m_b$) | 2 | $4 = 2^2$ | 2 |
| **Lepton** | $n=6$ ($F_6=8$, $m_\mu/m_\tau$) | $n=5$ ($F_5=5$, $m_e/m_\tau$) | 2 | $1 = 2^0$ | 0 |

### 6.2 Lepton Reversal（核心發現）

**定理 4（Lepton Reversal）**：Lepton sector 的配對 $6 \to 5$ 是反向的（backward），因為正向配對 $6 \to 7$ 被 $\mathbb{Z}_2$ selection rule 禁制——$7 = L_4$ 是偶數-indexed Lucas number。

**證明**：
1. 從 bipartite graph，$6$ 的唯一允許鄰居是 $5$（$6 \to 8$ 被 $2=L_0$ 禁制，$6 \to 9$ 被 $3=L_2$ 禁制）
2. 如果 lepton 遵循與 up/down 相同的正向模式：$6 \to 6 + \text{gap} = 6 + 1 = 7$
3. 但 $7 = L_4$ 是偶數-indexed Lucas，被 $\mathbb{Z}_2$ 禁制
4. 唯一可用的剩餘 index 是 $5$
5. 因此 $6 \to 5$（反向）是唯一選擇

**物理驗證**：如果 lepton 正向到 7：
- $F_7 = 13$，$13/134^2 = 0.000724$（太大，與 $m_e/m_\tau = 0.000287$ 不符）
- $13/134^3 = 0.0000054$（太細）
- 實際 $F_5/134^2 = 5/17956 = 0.000278$（誤差 3.1%，吻合）

**結論**：Lepton reversal 不是任意調整，而是 $\mathbb{Z}_2$ grading 的結構必然。

---

## 7. Sector Sum 對稱性

### 7.1 以 L₅ 為中心的對稱

每個 sector 的兩個 index 之和：

| Sector | n₁ + n₂ | 值 | 偏離 $L_5$ |
|:-------|:-------:|:--:|:----------:|
| Lepton | 6 + 5 | **11** | $L_5$（對稱中心） |
| Down | 4 + 8 | **12** | $L_5 + 1$ |
| Up | 1 + 9 | **10** | $L_5 - 1$ |

**定理 5（Sector Sum Symmetry）**：三個 sector 的 index 和 $\{10, 11, 12\}$ 以 $L_5 = 11$ 為對稱中心完美展開，對應於 $\pm 1$ 的對稱破缺。這不是配對的附加條件，而是唯一 bijection 的**自然結果**。

這解釋了為什麼 lepton 不帶 color charge、不參與強相互作用——它佔據了系統最核心的對稱軸 $L_5 = 11$，而 up 和 down 則是在兩側對稱破缺（$\pm 1$）的產物。

### 7.2 物理意義

Lepton sector 作為質量的「原點」（origin）：
- **對稱中心**：$6+5 = 11 = L_5$
- **無 color charge**：因為處於對稱軸上，不需要 $\pm 1$ 的破缺
- **最小 gap**：$2^0 = 1$，因為處於樹根

Up 和 Down 則作為對稱破缺的產物：
- **Up**：$-1$ 偏離，最深 tree depth（$33\beta$），最大 gap（8），s=3
- **Down**：$+1$ 偏離，中等 tree depth（$26\beta$），中等 gap（4），s=2

---

## 8. 完整推導鏈

### 8.1 推導步驟

```
|Step 1: K-chain Laplacian → γ_n = 4 sin²(πn/88)
        數學結構：Temperley-Lieb TL_44(q), q = e^{iπ/44}

Step 2: Dirac pairing → n ↔ 44-n, γ_n + γ_{44-n} = 4
        數學結構：Coxeter A_87 外自同構

Step 3: Binet formula → L_n = φⁿ + (-φ)⁻ⁿ
        Z₂ grading → even n: 正號(玻色子), odd n: 負號(費米子)

Step 4: Z₂ selection rule → skip {2,3,7} = {L₀, L₂, L₄}
        可用 indices: {1, 4, 5, 6, 8, 9}

Step 5: Tree depth ordering → partition{1, 4, 6} → s=1 (focused), sum = 11 = L₅
        {5, 8, 9} → s=2,3 (defocused), sum = 22 = 2L₅

Step 6: Bipartite graph analysis → ONLY ONE valid bijection
        1→9 (gap=8=2³, d=3) → Up sector
        4→8 (gap=4=2², d=2) → Down sector
        6→5 (gap=1=2⁰, d=0) → Lepton sector (reversal forced by Z₂)

Step 7: Sector sum symmetry → {10, 11, 12} centered on L₅ = 11
```

### 8.2 定理總結

| 定理 | 陳述 | 證明 |
|:----|:-----|:-----|
| 1 (Dirac Pairing) | $n \leftrightarrow 44-n$，$\gamma_n + \gamma_{44-n} = 4$ | Coxeter $A_{87}$ 外自同構 |
| 2 ($\mathbb{Z}_2$ Rule) | $\{L_0, L_2, L_4\} = \{2,3,7\}$ 被禁制 | Binet 公式 parity |
| 3 (Pairing Uniqueness) | 唯一 bijection: $1{\to}9, 4{\to}8, 6{\to}5$ | Bipartite graph 分析 |
| 4 (Lepton Reversal) | $6\to5$ 因 $7=L_4$ 被禁制 | $\mathbb{Z}_2$ selection rule + 質量驗證 |
| 5 (Sector Sum) | $\{10, 11, 12\}$ 以 $L_5$ 為中心 | 唯一 bijection 的自然結果 |

---

## 9. 與 Gemini 的對話驗證

本推導經 Google Gemini 2.5 Pro 從數學結構角度驗證，確認：

1. **Temperley-Lieb 代數 $TL_N(q)$** 是核心數學骨架，$q = e^{i\pi/44}$ 是單位根
2. **$\mathbb{Z}_2$ grading** 由 Binet 公式的 parity 決定，even-indexed Lucas 為玻色子（正號），odd-indexed Lucas 為費米子（負號）
3. **Coxeter $A_{87}$ 外自同構** 對應 Dirac pairing 的手徵對稱性
4. **Gap = 2$^k$** 的二進制模式對應 Bratteli Diagram 的樹深度
5. **Lepton reversal** 是拓撲反彈（topological reflection）的結果

---

## 10. 結論

我們從 K-chain 的圖 Laplacian 出發，透過三個嵌套的數學結構——Temperley-Lieb 代數、$\mathbb{Z}_2$ grading、Coxeter 外自同構——完整推導了 CY₃ 投影模型中的 defocus 參數 $s$。

核心發現：
1. **$\mathbb{Z}_2$ selection rule** 跳過 even-indexed Lucas numbers $\{2, 3, 7\}$
2. **Bipartite graph 唯一解** $1{\to}9, 4{\to}8, 6{\to}5$ 由 gap 條件 + $\mathbb{Z}_2$ 強制
3. **Lepton reversal** $6\to5$ 是 $\mathbb{Z}_2$ 的結構必然，不是任意調整
4. **Sector sum 對稱性** $\{10, 11, 12\}$ 以 $L_5 = 11$ 為中心，是唯一 bijection 的自然結果

這將 CY₃ 投影模型從「經驗公式」提升到「公理化推導」，所有參數都可以追溯到 0,1 → $\varphi$ → K-chain → $\mathbb{Z}_2$ 的第一性原理鏈。

---

## Appendix A：數值驗證

所有公式的數值驗證見 `verify_kchain_pairing.py`。

### A.1 基本關係

| 關係 | 公式 | 預期 | 實際 | 狀態 |
|:-----|:-----|:----:|:----:|:----:|
| $\gamma_1 + \gamma_{43}$ | $= 4$ | 4.0 | 4.0 | ✅ |
| $\gamma_4 + \gamma_{40}$ | $= 4$ | 4.0 | 4.0 | ✅ |
| $\gamma_5 + \gamma_{39}$ | $= 4$ | 4.0 | 4.0 | ✅ |
| $\gamma_6 + \gamma_{38}$ | $= 4$ | 4.0 | 4.0 | ✅ |
| $\gamma_8 + \gamma_{36}$ | $= 4$ | 4.0 | 4.0 | ✅ |
| $\gamma_9 + \gamma_{35}$ | $= 4$ | 4.0 | 4.0 | ✅ |

### A.2 Bipartite Graph 驗證

| 邊 | Gap | $2^d$? | $\mathbb{Z}_2$? | 結果 |
|:--|:---:|:------:|:---------------:|:----:|
| $1 \to 5$ | 4 | ✅ $2^2$ | ✅ 通過 | ✅ 允許 |
| $1 \to 8$ | 7 | ❌ | ❌ $L_4$ | ❌ 禁止 |
| $1 \to 9$ | 8 | ✅ $2^3$ | ✅ 通過 | ✅ 允許 |
| $4 \to 5$ | 1 | ✅ $2^0$ | ✅ 通過 | ✅ 允許 |
| $4 \to 8$ | 4 | ✅ $2^2$ | ✅ 通過 | ✅ 允許 |
| $4 \to 9$ | 5 | ❌ | ✅ 通過 | ❌ 禁止 |
| $6 \to 5$ | 1 | ✅ $2^0$ | ✅ 通過 | ✅ 允許 |
| $6 \to 8$ | 2 | ✅ $2^1$ | ❌ $L_0$ | ❌ 禁止 |
| $6 \to 9$ | 3 | ❌ | ❌ $L_2$ | ❌ 禁止 |

**唯一 bijection**：$1 \to 9$, $4 \to 8$, $6 \to 5$（5 條允許邊中唯一使用所有 6 個 indices 的解）

### A.3 Gap 與 $d_X$ 關係

| Sector | 配對 | Gap | $2^{d_X}$ | $d_X$ | 狀態 |
|:-------|:----:|:---:|:---------:|:-----:|:----:|
| Up | $1 \leftrightarrow 9$ | 8 | $2^3$ | 3 | ✅ |
| Down | $4 \leftrightarrow 8$ | 4 | $2^2$ | 2 | ✅ |
| Lepton | $6 \leftrightarrow 5$ | 1 | $2^0$ | 0 | ✅ |

### A.4 Lucas 數 Verification

| $n$ | $L_n$ | $\varphi^n + (-\varphi)^{-n}$ | Parity | 狀態 |
|:---:|:-----:|:-----------------------------:|:------:|:----:|
| 0 | 2 | 2 | even | ✅ |
| 1 | 1 | 1 | odd | ✅ |
| 2 | 3 | 3 | even | ✅ |
| 3 | 4 | 4 | odd | ✅ |
| 4 | 7 | 7 | even | ✅ |

### A.5 Mass Ratio 驗證

| Particle | Formula | IDCM Value | Observed | Error | Status |
|:---------|:--------|:----------:|:--------:|:-----:|:------:|
| $m_c/m_t$ | $F_1/CY_3$ | 0.007463 | 0.00735 | 1.5% | ✅ |
| $m_s/m_b$ | $F_4/CY_3$ | 0.022388 | 0.02273 | 1.3% | ✅ |
| $m_\mu/m_\tau$ | $F_6/CY_3$ | 0.059701 | 0.05946 | 0.3% | ✅ |
| $m_d/m_b$ | $F_8/CY_3^2$ | 0.001170 | 0.001124 | 4.1% | ✅ |
| $m_e/m_\tau$ | $F_5/CY_3^2$ | 0.000278 | 0.000287 | 3.1% | ✅ |
| $m_u/m_t$ | $F_9/CY_3^3$ | 0.0000141 | 0.0000127 | 11.0% | ✅ |

---

## Appendix B：與 Paper 05 的關係

本論文（Paper 07）與 Paper 05（Why Three Generations）的區別：

| 方面 | Paper 05 | Paper 07 |
|:-----|:---------|:---------|
| 焦點 | 為什麼是 3 代 | 為什麼 defocus s 是 1, 2, 3 |
| 方法 | $\varepsilon^3$ truncation | K-chain pairing symmetry |
| 核心結構 | MERA 3-layer projection | $\mathbb{Z}_2$ grading × TL algebra |
| 新發現 | — | Lepton reversal, sector sum symmetry |

兩篇論文互補：Paper 05 解釋了 $\varepsilon^3$ truncation 的世代數，Paper 07 解釋了 $s$ 值的幾何起源。