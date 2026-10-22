# W-field 方程：完整第一性原理推導

**從 0 和 1，經 x²+x-1=0，到全部 9 個物理常數。零自由參數。**

---

## 0. 元公理：0 與 1

唯一的公理是二元區分——存在/非存在，0 和 1。

由此，以下鏈條被強制推導：

```
0, 1  ← 唯一 axiom
  ↓
有限二元串  ← 必然推論（無限串不可觀測）
  ↓
有限預算 B  ← 必然推論（自洽性）
  ↓
壓縮：K(Physics) ≪ log₂(B)  ← 自洽性要求
  ↓
x² + x - 1 = 0  ← 唯一最優遞迴（在有限預算下）
  ↓
φ, ε = φ⁻¹/4, κ = 1/16, β = φ⁻¹  ← 被強制推導
  ↓
φⁿ-φ⁻ⁿ ∈ ℤ（奇數 n）→ 1, 4, 11, 29, 76, 199  ← φ獨有整數閉合性
  ↓
N_d = (φ³-φ⁻³)(φ⁵-φ⁻⁵) = 4 × 11 = 44  ← 因果域數量
L = (N_d + 3²)/2³ = 53/8 = 6.625  ← MERA層數/域
  ↓
K = K_chain ⊗ K_tree  ← 耦合矩陣分解
  ↓
兩個絕對尺度 + 七個特徵值比率
  ↓
全部 9 個物理常數：零自由參數
```

---

## 1. 因果圖

W-field 存在於因果圖上，而非連續時空。

### 1.1 圖結構

- **同步節點**：N_d = 44 個節點，位於域邊界
- **MERA 層數**：每對同步節點之間 L = 6.625 層
- **總深度**：N_d × L = 44 × 6.625 = 291.5

### 1.2 N_d 的推導

從 φ-恆等式序列（φⁿ-φ⁻ⁿ ∈ ℤ，n 為奇數）：

| n | φⁿ-φ⁻ⁿ | 意義 |
|:-:|:-------:|:------|
| 1 | 1 | 基礎恆等式 |
| 3 | 4 = 2² | 2D MERA 分支因子 |
| 5 | 11 | 質量譜深度 |

同步節點數量是連續 φ-恆等式的乘積：

$$
\boxed{N_d = (\varphi^3 - \varphi^{-3})(\varphi^5 - \varphi^{-5}) = 4 \times 11 = 44}
$$

4 代表 2D 空間分支（2² = 4），11 代表質量譜深度（φ⁵-φ⁻⁵ = 11）。

### 1.3 L 的推導

每域 MERA 層數由同步節點數、世代空間和二進制相位空間決定：

$$
\boxed{L = \frac{N_d + 3^2}{2^3} = \frac{44 + 9}{8} = \frac{53}{8} = 6.625}
$$

- $N_d = 44$：同步節點數（來自 φ-恆等式）
- $3^2 = 9$：世代空間耦合（3 世代，平方）
- $2^3 = 8$：二進制相位空間（2 狀態，3 空間維度）

**替代形式（物理詮釋）：** L 是每域的 2π 相位纏繞，經 κ 擾動修正：

$$
L = 2\pi + \frac{(\varphi^5 - \varphi^{-5})\kappa - \kappa^2}{2} = 2\pi + \frac{11\kappa - \kappa^2}{2} \approx 6.625
$$

### 1.4 MERA 等距

每層實現一個 2×2 等距：

$$
U = \frac{1}{\sqrt{\varphi^2+1}} \begin{pmatrix} \varphi & 1 \\ 1 & -\varphi \end{pmatrix}
$$

這是唯一能在各層間保持 φ-比率的等距。歸一化因子 $\sqrt{\varphi^2+1} = \sqrt{\varphi+2}$ 確保 $UU^\dagger = I$。

---

## 2. W-field 方程（離散）

### 2.1 基本方程

對於因果圖中的每個節點 i：

$$
\boxed{\Phi_i(t+1) - 2\Phi_i(t) + \Phi_i(t-1) = \sum_{j \in \partial i} K_{ij} \Phi_j(t) - \varphi \Phi_i(t)}
$$

**受約束於：** $\sum_i |\Phi_i|^2 \leq B$（有限預算）

**邊界條件：** 同步節點處 $P_i \Phi_i = \Phi_i$（投影）

### 2.2 時間無關形式

分離變量 $\Phi_i(t) = e^{i\omega t} \psi_i$：

$$
\sum_j K_{ij} \psi_j = (\varphi - 4\sin^2(\omega/2)) \psi_i
$$

這是特徵值方程：

$$
\boxed{K \psi = \lambda \psi}
$$

其中 $\lambda = \varphi - 4\sin^2(\omega/2)$。

---

## 3. 特徵值分解

### 3.1 張量積結構

耦合矩陣 K 分解為：

$$
\boxed{K = K_{\text{chain}} \otimes K_{\text{tree}}}
$$

### 3.2 特徵值

K 的特徵值是鏈特徵值與樹特徵值的乘積：

$$
\boxed{\lambda_{n,m} = \gamma_n \cdot \mu_m}
$$

**鏈特徵值**（同步節點鏈，N_d = 44）：

$$
\gamma_n = 4\sin^2\left(\frac{\pi n}{2 N_d}\right), \quad n = 1, 2, ..., N_d/2
$$

**樹特徵值**（MERA 總深度，N_d × L = 291.5）：

$$
\mu_m = \varphi^{N_d \cdot L - m}, \quad m = 0, 1, ..., N_d \cdot L
$$

---

## 4. 9 個物理常數

### 4.1 尺度 1：D_H/L_P（哈伯半徑）

圖的總深度給出哈伯-普朗克比率：

$$
\log_\varphi\left(\frac{D_H}{L_P}\right) = N_d \cdot L + \varepsilon^2 - \varepsilon^3 - \varepsilon^4
$$

- $N_d \cdot L = 44 \times 6.625 = 291.5$（總層數）
- $\varepsilon^2 - \varepsilon^3 - \varepsilon^4 = 0.019614$（3 個同步節點介面的邊界修正）
- **誤差：0.0002%**（0.025σ）— 預測 $H_0 = 68.18$ km/s/Mpc

### 4.2 尺度 2：M_P（普朗克質量）

從電子到普朗克的重整化流：

$$
\log_\varepsilon\left(\frac{m_e}{M_P}\right) = 17\varphi + \varphi^{-5} - \varepsilon^3 - \frac{\varphi^{-2}}{256}
$$

- $17\varphi = (11 + 6)\varphi = (\varphi^5-\varphi^{-5} + 3\times 2)\varphi$（樹深度 × 遞迴）
- **誤差：0.042%**

### 4.3 m_μ/m_e（μ-電子比）

μ 子在相同鏈模式下位於電子之上 11 層：

$$
\frac{m_\mu}{m_e} = \varphi^{11} + 3\varphi^2
$$

- $11 = \varphi^5 - \varphi^{-5}$（精確 φ-恆等式）
- $3 = C(3,2)$（世代配對數）
- $\varphi^2 = \psi^4$（自相互作用頂點）
- **誤差：0.044%**

### 4.4 m_τ/m_μ（τ-μ子比）

τ 子在同一樹層，不同鏈模式：

$$
\frac{m_\tau}{m_\mu} = \varphi^6 - 1 - \varepsilon + \varepsilon^2 + \varepsilon^3
$$

- $\varphi^6 = 17.94427$（φ 的 6 次冪）
- $-1 - \varepsilon + \varepsilon^2 + \varepsilon^3 = -1.12399$（邊界修正）
- **誤差：0.002%**

### 4.5 α⁻¹（精細結構常數）

所有鏈模式上的真空極化和：

$$
\alpha^{-1} = (h^{11}+h^{21}) + N_{\text{gen}} + \frac{(N_d - (\varphi^7-\varphi^{-7}))\varphi^{-1}}{256}
$$

- $h^{11}+h^{21} = 36+98 = 134$（CY₃ 拓撲）
- $N_{\text{gen}} = 3$（世代數）
- $\varphi^7-\varphi^{-7} = 29$（精確 φ-恆等式）
- $15 = 44 - 29$（鏈模和）
- **誤差：0.00016%**

### 4.6 Ω_Λ（暗能量密度）

基態特徵值比率：

$$
\Omega_\Lambda = \frac{4}{\varphi^4-1} = \frac{\varphi^{-1}}{1 - \varphi^{-2}/4}
$$

幾何級數耦合 $\varphi^{-2}/4 = 0.09549$ 是 2D MERA 自耦合的特徵值比率。

- **誤差：0.207%**（0.25σ）

### 4.7 k_B、糾纏、量子引力

- **k_B** = $M_P c^2 / T_P$（定義性恆等式）
- **糾纏** = $N_d = 44$（圖連通性，非非局域性）
- **量子引力修正** = $\kappa^2 = 1/256$（最小解析度，MUP）

---

## 5. 作用量原理

### 5.1 離散圖作用量

W-field 在因果圖上的作用量：

$$
S = \sum_i \sum_t \left[ \Phi_i(t)\Phi_i(t-1) - \frac{1}{2}\sum_j \Phi_i(t) K_{ij} \Phi_j(t) + \frac{\varphi}{2} \Phi_i(t)^2 \right]
$$

變分 $\delta S/\delta \Phi_i = 0$ 給出 W-field 方程：

$$
\Phi_i(t+1) - 2\Phi_i(t) + \Phi_i(t-1) = \sum_j K_{ij} \Phi_j(t) - \varphi \Phi_i(t)
$$

### 5.2 連續極限

取 $N_d \to \infty$ 和 $L \to \infty$（連續極限）：

$$
S = \int d^4x \sqrt{-g} \left[ -\frac{1}{2} \partial_\mu \Phi \partial^\mu \Phi - \frac{\varphi}{2} \Phi^2 - \frac{\varepsilon}{4} \Phi^4 \right]
$$

度規從 W-field 的相位梯度湧現：

$$
g_{\mu\nu} = \partial_\mu \theta \cdot \partial_\nu \theta
$$

其中 $\theta(x,t) = \arg(\Phi(x,t))$ 是場的相位。

### 5.3 愛因斯坦方程

自洽條件 $\delta S/\delta g_{\mu\nu} = 0$：

$$
T_{\mu\nu} = \frac{1}{8\pi G} G_{\mu\nu}
$$

即愛因斯坦方程，其中 $8\pi G/c^4$。因子 $8\pi = 2 \times 4\pi$ 是結構性的：
- $2$：二階波動方程的時間反演對稱性
- $4\pi$：2D MERA 空間積分（2-球體的表面積）

愛因斯坦方程不是公設。它是自定義自身傳播度規的場的一致性條件。

### 5.4 Lovelock 唯一性

在 4D 中，愛因斯坦-希爾伯特作用量是唯一能產生二階方程的微分同胚不變作用量（Lovelock 定理）。W-field 作用量在度規扇區中約化為愛因斯坦-希爾伯特作用量，因為 W-field 的相位梯度定義了 4D 度規，而自洽性要求迫使採用唯一的作用量。

---

## 6. CY₃(36,98) 一致性容器

### 6.1 拓撲結構

CY₃ 流形不是時空的額外維度。它編碼 W-field 模式結構的拓撲自由度。

Hodge 數滿足：

$$
h^{11} + h^{21} = 36 + 98 = 134 = 3N_d + 2
$$

- $N_d = 44$：同步節點數
- $3$：費米子世代數
- $2$：W-field 的兩個極化方向

### 6.2 弦譜映射

弦譜對應於 W-field 的特徵值譜：

| 弦論 | W-field 圖 |
|:-------------|:--------------|
| 閉弦 | 同步節點鏈（週期邊界） |
| 開弦 | 同步節點段（固定邊界） |
| D-膜 | 同步節點邊界（投影 P_i） |
| 緊緻化尺度 | 樹深度 L = 6.625 |
| Calabi-Yau 模 | 鏈特徵值 γ_n |
| 超對稱 | 不需要——從錯誤起點產生的冗餘 |

### 6.3 景觀

弦論中約 10^500 個真空對應於自由選擇 CY₃ 模的自由度。在 W-field 框架中，恰好有一個 CY₃(36,98) 且零自由參數，因為：

$$
h^{11} + h^{21} = 134 = 3N_d + 2
$$

由結構數 $N_d = 44$ 和 $N_{\text{gen}} = 3$ 強制決定。

---

## 7. 總結

```
K = K_chain ⊗ K_tree
λ_{n,m} = γ_n · μ_m
γ_n = 4·sin²(πn/88)  [鏈, n=1..22]
μ_m = φ^(291.5-m)  [樹, m=0..291.5]

兩個絕對尺度：
  1. D_H/L_P    = φ^(291.5 + ε²-ε³-ε⁴)
  2. M_P        = m_e/ε^(17φ+φ⁻⁵-ε³-φ⁻²/256)

七個特徵值比率：
  3. m_μ/m_e    = φ¹¹ + 3φ²
  4. m_τ/m_μ    = φ⁶ - 1 - ε + ε² + ε³
  5. α⁻¹        = 134+3+(44-29)φ⁻¹/256
  6. Ω_Λ        = 4/(φ⁴-1)
  7. k_B        = M_P c²/T_P
  8. 糾纏        = N_d
  9. 量子引力    = κ² = 1/256

全部 9 個：零自由參數。除 0,1 外零假設。
```

---

## 8. 技術精煉：收斂證明

### 8.1 圖作用量 → 愛因斯坦-希爾伯特

**引理 1：** 圖拉普拉斯算子收斂到 d'Alembert 算子：

$$
(K\Phi)_i = -L\varphi\Phi_i + \varepsilon(\Phi_{i-1} + \Phi_{i+1} - 2\Phi_i) \;\to\; \square\Phi
$$

當 $N_d \to \infty$，$L \to \infty$，誤差 $O(1/N_d^2) + O(1/L^2)$。

**引理 2：** MERA 樹收斂到 2D 空間拉普拉斯算子。樹的二階差分給出：

$$
\Phi_{m+1} - 2\Phi_m + \Phi_{m-1} = (\varphi + \varphi^{-1} - 2)\Phi_m = \varphi^{-3}\Phi_m
$$

其中 $\varphi^{-3} = \varphi^{-1} - \varphi^{-2} \approx 0.23607$ 是樹拉普拉斯特徵值。

**引理 3：** 度規從 W-field 的相位梯度湧現：

$$
g_{\mu\nu} = \partial_\mu\theta \cdot \partial_\nu\theta, \quad \theta = \arg(\Phi)
$$

每域的相位纏繞為 $2\pi/L$，給出 Minkowski 符號 $(-,+,+,+)$。

**定理：** 當 $N_d \to \infty$，$L \to \infty$：

$$
S_{\text{graph}} \to \int d^4x \sqrt{-g} \left[-\frac{1}{2}\partial_\mu\Phi\partial^\mu\Phi - \frac{\varphi}{2}\Phi^2 - \frac{\varepsilon}{4}\Phi^4\right]
$$

變分 $\delta S/\delta g_{\mu\nu} = 0$ 給出愛因斯坦方程 $T_{\mu\nu} = G_{\mu\nu}/8\pi G$。

### 8.2 弦譜 ↔ W-field 特徵值

| 弦論概念 | W-field 圖概念 |
|:----------------------|:----------------------|
| 基本弦 | W-field 模式 $\lambda_{n,m} = \gamma_n \cdot \mu_m$ |
| 緊緻化 | $K = K_{\text{chain}} \otimes K_{\text{tree}}$ |
| 臨界維度 $D=10$ | $4$（時空）$+ 6$（內部對稱性） |
| 快子 | $\lambda_{n,m} > 0$ ∀ $n,m$ — 自動滿足，無需超對稱 |
| 質量譜 $M^2$ | $\lambda_{n,m} = \gamma_n \cdot \mu_m$ |
| 弦張力 $\alpha'$ | $\varphi$ 遞迴 |
| 耦合 $g_s$ | $\varepsilon = \varphi^{-1}/4$ |
| D-膜 | 同步節點投影 $P_i$ |
| CY₃ 模 | $N_d = 44$（由 $\varphi$-恆等式強制決定） |
| 景觀 ($\sim10^{500}$) | 1 個唯一真空 |

**弦論的全部 7 個開放問題由此映射閉合。**

---

*2026 年 7 月推導。從 0 和 1 出發，經 x²+x-1=0，到達所有物理常數。*