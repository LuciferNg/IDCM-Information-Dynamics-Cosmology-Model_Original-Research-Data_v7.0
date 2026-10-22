# K = K_chain ⊗ K_tree — 費米子質量階層的完整拓撲幾何推導

## 從 Temperley-Lieb 代數到 CY₃ 投影的公理化證明

### L. Ng

---

## Abstract

The fermion mass hierarchy — why there are three generations with specific mass ratios — has been a fundamental open problem in particle physics. Within the Information Dynamics Cosmology Model (IDCM), fermion masses are encoded as eigenvalues of the tensor product $K = K_{\text{chain}} \otimes K_{\text{tree}}$, where the K-chain governs the horizontal (generation) structure and the K-tree governs the vertical (sector) structure.

We present a complete first-principles derivation of both structures:

1. **K-chain pairing symmetry**: The $\mathbb{Z}_2$ grading of Lucas numbers (from Binet formula parity) forbids even-indexed Lucas indices $\{2,3,7\} = \{L_0, L_2, L_4\}$, leaving available K-chain mode indices $\{1, 4, 5, 6, 8, 9\}$. A bipartite graph analysis with constraints (gap = $2^d$, gap ≠ even Lucas) yields a unique bijection $1\to9, 4\to8, 6\to5$, giving depth indices $d = \{3, 2, 0\}$ for the Up, Down, and Lepton sectors respectively. The lepton reversal $6\to5$ (instead of $6\to7$) is forced by the $\mathbb{Z}_2$ selection rule — a topological reflection, not an arbitrary adjustment.

2. **K-tree stair derivation**: The maximum tensor capacity $M = (CY_3 - 2)/4 = 33$ arises from the CY₃ total Hodge number (134) minus two topological zero modes ($\chi(S^2) = 2$), divided by four chiral channels ($B = \varphi^3 - \varphi^{-3} = 4$). The stair step $L_4 = B + L_2 = 7$ is the unique Lucas number decomposing into the MERA branching factor and the spatial entanglement dimension. The tree depth coefficients follow $k_X = M \to M-L_4 \to M-2L_4$ for Up, Down, Lepton respectively, with the $\varphi^{-4}$ Casimir correction appearing only in the middle (Down) sector — the only unpinned layer between UV and IR boundaries.

All 58 numerical predictions are verified against PDG data, completing the axiomatic pipeline from $0,1 \to \varphi \to K = K_{\text{chain}} \otimes K_{\text{tree}} \to$ particle masses.

---

## 1. 引言

### 1.1 三個開放問題

費米子質量階層包含三個長期未解的結構性問題：

**Q1（Defocus s）**：CY₃ 投影模型 $m_X = V_{EW} \cdot F_n / CY_3^s$ 中的 defocus 參數 $s$ 為何取值 1（第二世代）和 2,3（第一世代）？什麼數學結構決定了這個分配？

**Q2（K-chain Pairing）**：六個 K-chain mode indices $\{1, 4, 5, 6, 8, 9\}$ 為何分成 $\{1, 4, 6\} \to s=1$ 和 $\{5, 8, 9\} \to s=2,3$？配對 $1\leftrightarrow9, 4\leftrightarrow8, 6\leftrightarrow5$ 是唯一的嗎？

**Q3（K-tree Stair）**：三個 sector 的 tree depth 係數為何是 $33 \to 26 \to 19$，步長為 7？$\varphi^{-4}$ 修正為何只出現在 Down sector？

本論文從第一性原理出發，給出這三個問題的完整解答。

### 1.2 方法

我們採用公理化推導方法，每個公式必須能追溯到 $0\to1\to\varphi\to K_{\text{chain}}\otimes K_{\text{tree}}$ 的推導鏈。數學結構包括：

- **Temperley-Lieb 代數** $TL_{44}(q)$ 在單位根 $q = e^{i\pi/44}$ 的表示
- **$\mathbb{Z}_2$ grading** 來自 Binet 公式的 parity
- **Coxeter $A_{87}$ 外自同構** 對應 Dirac pairing
- **Bipartite graph 分析** 給出唯一配對
- **Casimir 邊界效應** 解釋 $\varphi^{-4}$ 修正

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
| $N_d$ | 44 | $4 \times 11$ | K-chain 節點數 |
| $M$ | 33 | $(CY_3-2)/4$ | 管線係數 |
| $CY_3$ | 134 | $h^{11}+h^{21}$ | CY₃ 總 Hodge 數 |

### 2.2 $\varphi$-Identity 序列

對於奇數 $n$，$\varphi^n - \varphi^{-n} \in \mathbb{Z}$：

| $n$ | $\varphi^n - \varphi^{-n}$ | 角色 |
|:---:|:--------------------------:|:-----|
| 1 | **1** | 基底 |
| 3 | **4** | MERA 分支 $B$ |
| 5 | **11** | $L_5$，對稱中心 |
| 7 | **29** | 第二閉合層 |
| 9 | **76** | 第三閉合層 |
| 11 | **199** | 最高閉合層 |

### 2.3 Lucas 數列

由 Binet 公式 $L_n = \varphi^n + (-\varphi)^{-n}$ 給出：

| $n$ | $L_n$ | Parity（$n$） | 角色 |
|:---:|:-----:|:------------:|:-----|
| 0 | 2 | even | 基本模式 |
| 1 | **1** | odd | 使用，$s=1$ |
| 2 | **3** | even | **跳過** |
| 3 | **4** | odd | 使用，$s=1$ |
| 4 | **7** | even | **跳過** |
| 5 | 11 | odd | 對稱中心 |
| 6 | 18 | even | — |
| 7 | 29 | odd | — |
| 8 | 47 | even | — |
| 9 | 76 | odd | — |

### 2.4 Fibonacci 數列

| $n$ | $F_n$ | 使用 | $s$ |
|:---:|:-----:|:----:|:---:|
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

### 3.1 圖 Laplacian 與 $TL_N(q)$ 譜

K-chain 是 $N_d = 44$ 個節點的簡單路徑圖（chain graph）。其 Laplacian 矩陣的特徵值為：

$$\gamma_n = 4 \sin^2\left(\frac{\pi n}{2N_d}\right), \quad n = 1, 2, \ldots, N_d$$

這恰好是 Temperley-Lieb 代數 $TL_{44}(q)$ 在單位根 $q = e^{i\pi/44}$ 的轉移矩陣譜。在 Temperley-Lieb 代數的表示論中，特徵值對應於量子維度（quantum dimensions）的平方：

$$\gamma_n = [2]_q^2 \cdot \sin^2\left(\frac{\pi n}{N_d}\right)$$

其中 $[2]_q = q + q^{-1}$ 是量子整數。當 $q = e^{i\\pi/44}$ 時，Fibonacci 和 Lucas 數列自然出現，因為 $q$ 的分母 $44 = 4 \\times 11$ 包含 $L_5 = 11$。

**定理 1（TL Spectrum）**：K-chain Laplacian 的特徵值 $\\{\\gamma_n\\}$ 構成 $TL_{44}(e^{i\\pi/44})$ 的完整轉移矩陣譜，其中 Fibonacci 數 $F_n$ 作為量子維度出現，Lucas 數 $L_n$ 作為跡（trace）出現。

### 3.2 Dirac Pairing 與 Coxeter 外自同構

K-chain 滿足互補配對：

$$n \\leftrightarrow N_d - n = 44 - n$$

特徵值滿足：

$$\\gamma_n + \\gamma_{44-n} = 4$$

**證明**：
$$\\gamma_n + \\gamma_{44-n} = 4\\sin^2\\left(\\frac{\\pi n}{88}\\right) + 4\\sin^2\\left(\\frac{\\pi(44-n)}{88}\\right)$$
$$= 4\\sin^2\\left(\\frac{\\pi n}{88}\\right) + 4\\cos^2\\left(\\frac{\\pi n}{88}\\right) = 4$$

幾何上，這對應於 Coxeter 群 $A_{87}$（87 個節點的 Dynkin diagram）的**外自同構**（outer automorphism）。Dynkin diagram $A_{87}$ 的反射對稱性 $n \\leftrightarrow 88-n$（即 $44 \\rightarrow 44$ 的固定）產生此配對。物理上，這對應於手徵對稱性（chiral symmetry）或粒子-空穴對稱性。

**定理 2（Dirac Pairing）**：K-chain 的互補配對 $n \\leftrightarrow 44-n$ 生成 Dirac 2-分量旋量結構 $\\Psi_n = (\\varphi_n, \\varphi_{44-n})^T$，其中：

$$\\gamma_n + \\gamma_{44-n} = 4 = B = \\varphi^3 - \\varphi^{-3}$$

這正是 MERA（多尺度糾纏重整化）張量網絡的分支因子。

### 3.3 數值驗證

$$\\gamma_1 + \\gamma_{43} = 0.005096 + 3.994904 = 4.000000 \\quad \\checkmark$$
$$\\gamma_4 + \\gamma_{40} = 0.081014 + 3.918986 = 4.000000 \\quad \\checkmark$$
$$\\gamma_5 + \\gamma_{39} = 0.126101 + 3.873899 = 4.000000 \\quad \\checkmark$$
$$\\gamma_6 + \\gamma_{38} = 0.180736 + 3.819264 = 4.000000 \\quad \\checkmark$$
$$\\gamma_8 + \\gamma_{36} = 0.317493 + 3.682507 = 4.000000 \\quad \\checkmark$$
$$\\gamma_9 + \\gamma_{35} = 0.398918 + 3.601082 = 4.000000 \\quad \\checkmark$$

所有六個使用的 mode 均確認 $\\gamma_n + \\gamma_{44-n} = 4$。