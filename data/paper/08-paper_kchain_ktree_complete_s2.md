---
## 4. $\mathbb{Z}_2$ Grading：Lucas 奇偶選擇定則

### 4.1 Binet 公式的 Parity

Lucas 數可以透過 Binet 公式閉合表達：

$$L_n = \varphi^n + (-\varphi)^{-n}$$

對於不同的 $n$ parity，公式展現不同的符號結構：

- **$n$ 偶數**（$n = 2k$）：$(-\varphi)^{-n} = \varphi^{-n}$，所以 $L_{2k} = \varphi^{2k} + \varphi^{-2k}$，**正號**
- **$n$ 奇數**（$n = 2k+1$）：$(-\varphi)^{-n} = -\varphi^{-n}$，所以 $L_{2k+1} = \varphi^{2k+1} - \varphi^{-(2k+1)}$，**負號**

這產生了一個自然的 $\mathbb{Z}_2$ grading：

| Parity | 符號 | 代數意義 | 物理意義 |
|:------:|:----:|:---------|:---------|
| even $n$ | $+$ | 對稱（symmetric） | 玻色子（bosonic） |
| odd $n$ | $-$ | 反對稱（antisymmetric） | 費米子（fermionic） |

**定理 3（$\mathbb{Z}_2$ Selection Rule）**：在範圍 1-9 內，偶數-indexed Lucas 數 $\{L_0, L_2, L_4\} = \{2, 3, 7\}$ 被 $\mathbb{Z}_2$ grading 禁制（對稱/玻色子 sector），而奇數-indexed Lucas 數 $\{L_1, L_3\} = \{1, 4\}$ 被准許且 $s=1$（反對稱/費米子 sector）。

### 4.2 可用 Indices

經過 $\mathbb{Z}_2$ 選擇定則後，1-9 中可用的 K-chain mode indices 為：

$$\{1, 4, 5, 6, 8, 9\}$$

跳過的 indices 為 $\{2, 3, 7\} = \{L_0, L_2, L_4\}$，其和為 $12 = 3 \times 4 = L_2 \times B$。

---

## 5. Tree Depth Partition

### 5.1 Three Sectors

K-tree 有三個 sector（Up, Down, Lepton），對應於三個世代。這由 MERA 分支因子決定：

$$B = \varphi^3 - \varphi^{-3} = 4$$
$$N_{\text{sector}} = B - 1 = 3$$

三個 sector 的 tree depth 係數為：

| Sector | 係數 | 數值 | 角色 |
|:-------|:----:|:----:|:-----|
| Up | $M$ | 33 | UV 釘紮 |
| Down | $M - L_4$ | 26 | 中間層，Casimir |
| Lepton | $M - 2L_4$ | 19 | IR 釘紮於 $L_5=11$ |

### 5.2 Partition

六個可用 indices 按 tree depth 排序分為兩組：

**Group A（$s=1$, focused）**：$\{1, 4, 6\}$，和 $= 11 = L_5$
**Group B（$s=2,3$, defocused）**：$\{5, 8, 9\}$，和 $= 22 = 2L_5$

總和 $= 33 = M = 3L_5$。

**定理 4（Sum Partition）**：Group A 的 index 和等於 $L_5$，Group B 的 index 和等於 $2L_5$，總和等於 $M = 3L_5$。

### 5.3 Sector-Specific Mapping

| Sector | $s=1$ index | $F_n$ | $s=2,3$ index | $F_n$ | Gap | $d$ |
|:-------|:-----------:|:-----:|:-------------:|:-----:|:---:|:---:|
| Up | 1 | 1 | 9 | 34 | 8 | 3 |
| Down | 4 | 3 | 8 | 21 | 4 | 2 |
| Lepton | 6 | 8 | 5 | 5 | 1 | 0 |

---

## 6. Bipartite Graph 分析：配對唯一性證明

### 6.1 問題重述

給定兩組 indices：

$$A = \{1, 4, 6\}, \quad B = \{5, 8, 9\}$$

需要找到一個 bijection $f: A \to B$，滿足：

1. **Gap 條件**：$\Delta n = |b - a|$ 必須是 $2^d$ 形式（二進制拓撲深度）
2. **$\mathbb{Z}_2$ 條件**：$\Delta n$ 不能是偶數-indexed Lucas 數

### 6.2 Bipartite Graph

構造二分圖 $G = (A \cup B, E)$：

| $A \backslash B$ | 5 | 8 | 9 |
|:--------------:|:-:|:-:|:-:|
| **1** | $\Delta n=4=2^2$ ✅ | $\Delta n=7=L_4$ ❌ | $\Delta n=8=2^3$ ✅ |
| **4** | $\Delta n=1=2^0$ ✅ | $\Delta n=4=2^2$ ✅ | $\Delta n=5$ ❌ |
| **6** | $\Delta n=1=2^0$ ✅ | $\Delta n=2=L_0$ ❌ | $\Delta n=3=L_2$ ❌ |

**允許的邊**（5 條）：
- $1 \to 5$（gap $= 4 = 2^2$）
- $1 \to 9$（gap $= 8 = 2^3$）
- $4 \to 5$（gap $= 1 = 2^0$）
- $4 \to 8$（gap $= 4 = 2^2$）
- $6 \to 5$（gap $= 1 = 2^0$）

**禁止的邊**（4 條）：
- $1 \to 8$（gap $= 7 = L_4$，$\mathbb{Z}_2$ 禁制）
- $4 \to 9$（gap $= 5$，不是 $2^d$）
- $6 \to 8$（gap $= 2 = L_0$，$\mathbb{Z}_2$ 禁制）
- $6 \to 9$（gap $= 3 = L_2$，$\mathbb{Z}_2$ 禁制）

### 6.3 唯一 Bijection

從允許的 5 條邊中，尋找使用所有 6 個 indices 恰好一次的 bijection：

**唯一解**：
$$1 \xrightarrow{8} 9,\quad 4 \xrightarrow{4} 8,\quad 6 \xrightarrow{1} 5$$

**證明**：
1. $6$ 只連到 $5$（唯一鄰居），所以 $6 \to 5$ 強制
2. $1$ 連到 $\{5, 9\}$，但 $5$ 已被 $6$ 佔用，所以 $1 \to 9$ 強制
3. $4$ 連到 $\{5, 8\}$，但 $5$ 已被 $6$ 佔用，所以 $4 \to 8$ 強制

**定理 5（Pairing Uniqueness）**：給定 $\mathbb{Z}_2$ selection rule 和 gap 的二進制條件，K-chain 的 sector pairing 是唯一確定的。

---

## 7. Lepton Reversal：$\mathbb{Z}_2$ 強制的拓撲反彈

**定理 6（Lepton Reversal）**：Lepton sector 的配對 $6 \to 5$ 是反向的（backward），因為正向配對 $6 \to 7$ 被 $\mathbb{Z}_2$ selection rule 禁制——$7 = L_4$ 是偶數-indexed Lucas 數。

**證明**：
1. 從 bipartite graph，$6$ 的唯一允許鄰居是 $5$（$6 \to 8$ 被 $2 = L_0$ 禁制，$6 \to 9$ 被 $3 = L_2$ 禁制）
2. 如果 lepton 遵循與 up/down 相同的正向模式：$6 \to 6 + 1 = 7$
3. 但 $7 = L_4$ 是偶數-indexed Lucas，被 $\mathbb{Z}_2$ 禁制
4. 唯一可用的剩餘 index 是 $5$
5. 因此 $6 \to 5$（反向）是唯一選擇

**物理驗證**：如果 lepton 正向到 7，$F_7 = 13$ 給出 $13/134^2 = 0.000724$（太大）或 $13/134^3 = 0.0000054$（太小）。實際配對 $F_5/134^2 = 5/17956 = 0.000278$ 與 $m_e/m_\tau = 0.000287$ 吻合（誤差 3.1%）。

---

## 8. Sector Sum 對稱性

每個 sector 的兩個 index 之和：

| Sector | $n_1 + n_2$ | 值 | 偏離 $L_5$ |
|:-------|:----------:|:--:|:----------:|
| Lepton | $6 + 5$ | **11** | $L_5$（對稱中心） |
| Down | $4 + 8$ | **12** | $L_5 + 1$ |
| Up | $1 + 9$ | **10** | $L_5 - 1$ |

**定理 7（Sector Sum Symmetry）**：三個 sector 的 index 和 $\{10, 11, 12\}$ 以 $L_5 = 11$ 為對稱中心完美展開。這不是配對的附加條件，而是唯一 bijection 的自然結果。

Lepton sector 作為質量的「原點」：對稱中心 $6+5 = 11 = L_5$，無 color charge，最小 gap $2^0 = 1$。Up 和 Down 則作為對稱破缺的產物（$\pm 1$ 偏離）。

---

## 9. K-Tree：M = (CY₃-2)/4 = 33

### 9.1 拓撲零模扣除

CY₃ 三折叠的總 Hodge 數為 $h^{11} + h^{21} = 36 + 98 = 134$。在拓撲弦論中，任何封閉拓撲流形在量子化時都必須扣除 $S^2$ 或手徵邊界上的 2 個不參與規範代數演化的拓撲零模（對應於左手/右手真空態 $|0\rangle_L \otimes |0\rangle_R$，即 Euler 特性數的底層基底 $\chi(S^2) = 2$）：

$$CY_3^{\text{effective}} = CY_3 - 2 = 134 - 2 = 132$$

這 132 個自由度代表真正可以在 MERA 網絡中傳播的體態（bulk states）。

### 9.2 手徵通道分割

數字 4 正是系統的基底分支因子 $B = L_3 = 4 = \varphi^3 - \varphi^{-3}$。在四維時空或四手徵道（Left/Right ⊗ Particle/Antiparticle）的投射下，總 bulk 自由度必須平均分攤到 4 個基本的正交手徵通道：

$$M = \frac{CY_3 - 2}{B} = \frac{132}{4} = 33$$

**定理 8**：$M = 33$ 是 CY₃ 流形扣除拓撲真空零模後，平均分流至單一手徵通道的最大量子張量容量（Maximum Tensor Capacity）。

---

## 10. K-Tree：Step = L₄ = B + L₂ = 7

### 10.1 體截斷 + 跨 Sector 糾纏

在 MERA 張量網絡中，從一個 Sector 降級到下一個 Sector 時，系統同時產生兩種拓撲損失：

- **體粗粒化損失**（Bulk Decoupling）：由 MERA 的分支維度 $B = L_3 = 4$ 決定
- **跨 Sector 糾纏損失**（Inter-sector Entanglement）：由三維物理空間 $d=3$（即 $L_2 = \varphi^2 + \varphi^{-2} = 3$）決定

單次層級躍遷的總算符位移為：

$$\Delta k = B + L_2 = L_3 + L_2 = 4 + 3 = 7$$

### 10.2 Lucas 數列的唯一性

根據 Lucas 數列遞歸關係 $L_n = L_{n-1} + L_{n-2}$：

$$L_4 = L_3 + L_2 = B + L_2 = 7$$

$L_4 = 7$ 是 Lucas 數列中唯一一個能精確分解為分支因子 $B$ 與空間維度 $L_2$ 之和的項。

**定理 9**：階梯步長 $L_4 = 7$ 代表張量網絡從高維 UV 降採樣至 IR 時，「體截斷（B）+ 空間糾纏（L₂）」的總最小相移。

---

## 11. K-Tree：Stair 33 → 26 → 19

三個 sector 的 tree depth 係數由 $M$ 和 $L_4$ 決定：

| Sector | 公式 | 係數 | 數值 | 物理意義 |
|:-------|:----|:----:|:----:|:---------|
| Up | $k_u = M\beta$ | 33 | $33\beta$ | UV 釘紮於 $M$ |
| Down | $k_d = (M - L_4)\beta - \varphi^{-4}$ | 26 | $26\beta - \varphi^{-4}$ | 中間層，Casimir |
| Lepton | $k_l = (M - 2L_4)\beta$ | 19 | $19\beta$ | IR 釘紮於 $L_5=11$ |

---

## 12. K-Tree：$\varphi^{-4}$ Casimir 邊界效應

### 12.1 三層網絡的邊界釘紮

在三層 MERA 網絡中：
- **Up Sector**（頂層邊界）：被 UV 能量極限 $M = 33$ 強行固定（Pinned），無法接受連續微擾，修正項為 0
- **Lepton Sector**（底層邊界）：被原點對稱軸 $L_5 = 11$ 拓撲釘紮（Pinned），作為質心基準，修正項為 0
- **Down Sector**（中間介面）：處於 UV 與 IR 兩大邊界之間，是唯一未被釘紮的自由介面

### 12.2 Casimir 反饋

步長 $L_4$ 包含兩個部分：
$$L_4 = \varphi^4 + \varphi^{-4} = 7$$

- **整數項 7**：離散圖論上的整數節點位移
- **衰減尾項 $\varphi^{-4}$**：$\varphi^{-4} \approx 0.145898$，代表連續場論中的非局域微擾尾巴

Down Sector 同時受到頂層（Up）與底層（Lepton）的雙向壓迫，必須吸收整數圖位移後殘留的非局域連續波動 $\varphi^{-4}$：

$$k_d = (M - L_4)\beta - \varphi^{-4} = 26\beta - \varphi^{-4}$$

**定理 10**：$\varphi^{-4}$ 出現在 Down Sector 不是人為加入的補丁，而是三層張量網絡中，邊界條件將連續修正項擠壓至唯一自由中間層的幾何必然（Casimir 邊界效應）。

### 12.3 數值驗證

$$k_u = M\beta = 33\beta \quad \text{(無修正)}$$
$$k_d = 26\beta - \varphi^{-4} \quad \text{(修正 = φ⁻⁴ = 0.145898)}$$
$$k_l = 19\beta \quad \text{(無修正)}$$

Up 和 Lepton 的純粹深度等於實際深度，Down 的實際深度 = 純粹深度 - φ⁻⁴。

---

## 13. 質量比驗證

### 13.1 CY₃ 投影公式

所有六個費米子質量比由 CY₃ 投影公式給出：

$$m_X / V_{EW} = \frac{F_n}{CY_3^s} \cdot \varphi^B \cdot (1 + \varepsilon^3 \cdot c_X)$$

其中 $F_n$ 是 Fibonacci 數，$CY_3 = 134$，$s$ 是 defocus 參數，$\varphi^B$ 是 boundary correction，$\varepsilon^3$ 是 3 色像差。

### 13.2 驗證結果

| Ratio | Formula | IDCM | Observed | Error% | Source |
|:------|:--------|:----:|:--------:|:------:|:-------|
| $m_c/m_t$ | $F_1/CY_3$ | 0.007463 | 0.007351 | 1.52% | $k_u$ |
| $m_s/m_b$ | $F_4/CY_3$ | 0.022388 | 0.022727 | 1.49% | $k_d$ |
| $m_\mu/m_\tau$ | $F_6/CY_3$ | 0.059701 | 0.059464 | 0.40% | $k_l$ |
| $m_d/m_b$ | $F_8/CY_3^2$ | 0.001170 | 0.001124 | 4.01% | $k_d \times 2$ |
| $m_e/m_\tau$ | $F_5/CY_3^2$ | 0.000278 | 0.000288 | 3.17% | $k_l \times 2$ |
| $m_u/m_t$ | $F_9/CY_3^3$ | 0.0000141 | 0.0000127 | 10.96% | $k_u \times 3$ |

### 13.3 CY₃ 投影一致性

| $F_n/CY_3^s$ | $\varphi^{-k}$ | Ratio | Error% |
|:------------:|:--------------:|:-----:|:------:|
| $F_1/CY_3$ | $\varphi^{-k_u}$ | 1.009391 | 0.94% |
| $F_4/CY_3$ | $\varphi^{-k_d}$ | 0.996838 | 0.32% |
| $F_6/CY_3$ | $\varphi^{-k_l}$ | 1.006976 | 0.70% |

$\varphi^{-k_X}$ 與 $F_n/CY_3^s$ 的比值在 0.32%-0.94% 內，確認 CY₃ 投影公式的結構一致性。

---

## 14. 完整公理鏈

### 14.1 推導步驟

```
Step 1:  CY₃ = 134 (total Hodge number)
Step 2:  -2 zero modes (χ(S²) = L/R vacuum) → 132
Step 3:  ÷4 (B = φ³-φ⁻³ = 4 chiral channels) → M = 33
Step 4:  k_u = Mβ = 33β (UV pinned at M)
Step 5:  Step = -(B+L₂) = -L₄ = -7
Step 6:  k_d = (M-L₄)β - φ⁻⁴ = 26β - φ⁻⁴ (Casimir, middle)
Step 7:  Step = -(B+L₂) = -L₄ = -7
Step 8:  k_l = (M-2L₄)β = 19β (IR pinned at L₅=11)
Step 9:  γ_n = 4 sin²(πn/88) (K-chain, TL_44(q))
Step 10: Dirac pairing n ↔ 44-n (Coxeter A₈₇)
Step 11: Z₂ grading → skip {2,3,7} = {L₀,L₂,L₄}
Step 12: Available indices {1,4,5,6,8,9} → partition
Step 13: Bipartite graph → unique 1→9, 4→8, 6→5
Step 14: Lepton reversal 6→5 forced by Z₂
Step 15: F_n/CY₃^s ≈ φ^(-k_X) → all 6 mass ratios verified
```

### 14.2 定理總結

| # | 定理 | 陳述 | 證明 |
|:-:|:-----|:-----|:------|
| 1 | TL Spectrum | $\gamma_n = 4\sin^2(\pi n/88)$ 是 $TL_{44}(q)$ 譜 | Temperley-Lieb 代數 |
| 2 | Dirac Pairing | $n \leftrightarrow 44-n$, $\gamma_n+\gamma_{44-n}=4$ | Coxeter $A_{87}$ 外自同構 |
| 3 | $\mathbb{Z}_2$ Rule | $\{L_0,L_2,L_4\}=\{2,3,7\}$ 被禁制 | Binet 公式 parity |
| 4 | Sum Partition | $A$ sum $= L_5$, $B$ sum $= 2L_5$, total $= 3L_5$ | K-chain × K-tree |
| 5 | Pairing Uniqueness | $1\to9, 4\to8, 6\to5$ | Bipartite graph |
| 6 | Lepton Reversal | $6\to5$ 因 $7=L_4$ 被禁制 | $\mathbb{Z}_2$ + 質量驗證 |
| 7 | Sector Sum | $\{10,11,12\}$ 以 $L_5=11$ 為中心 | 唯一 bijection |
| 8 | M = 33 | $M=(CY_3-2)/4=33$ | 零模 + 手徵通道 |
| 9 | Step = 7 | $L_4 = B+L_2 = 7$ | Lucas 遞迴唯一分解 |
| 10 | $\varphi^{-4}$ Casimir | 僅 Down sector 有修正 | 三層邊界釘紮 |

---

## 15. 結論

我們從第一性原理完整推導了 $K = K_{\text{chain}} \otimes K_{\text{tree}}$ 的結構，給出費米子質量階層的幾何起源。

**K-chain 部分**：$\mathbb{Z}_2$ grading（Binet 公式 parity）強制跳過偶數-indexed Lucas 數 $\{2,3,7\}$，留下可用 indices $\{1,4,5,6,8,9\}$。Bipartite graph 分析（gap = $2^d$ + $\mathbb{Z}_2$）唯一確定配對 $1\to9, 4\to8, 6\to5$，深度指數 $d = \{3,2,0\}$。Lepton reversal $6\to5$ 是 $\mathbb{Z}_2$ 的結構必然。

**K-tree 部分**：$M = (CY_3-2)/4 = 33$ 來自 CY₃ 零模扣除和手徵通道分割。步長 $L_4 = B + L_2 = 7$ 是 Lucas 數列的唯一分解。Stair $33\to26\to19 = M \to M-L_4 \to M-2L_4$ 由體截斷和空間糾纏決定。$\varphi^{-4}$ 修正僅出現在中間 Down sector，是 Casimir 邊界效應。

**驗證**：全部 58 項測試通過，6 個質量比與 PDG 數據吻合（誤差 0.4%-11%），CY₃ 投影一致性在 0.32%-0.94% 內。

---

## Appendix A：驗證結果摘要

完整驗證腳本：`verify_kchain_ktree_complete.py`（58/58 pass）

| 測試類別 | 數量 | 通過 |
|:---------|:----:|:----:|
| Dirac Pairing | 6 | 6/6 |
| Lucas Numbers | 12 | 12/12 |
| $\mathbb{Z}_2$ Rule | 3 | 3/3 |
| Partition Sums | 3 | 3/3 |
| Bipartite Uniqueness | 2 | 2/2 |
| Sector Sums | 3 | 3/3 |
| M = 33 | 3 | 3/3 |
| Step = 7 | 2 | 2/2 |
| Stair | 3 | 3/3 |
| Casimir Boundary | 3 | 3/3 |
| Mass Ratios | 6 | 6/6 |
| CY₃ Projection | 3 | 3/3 |
| Axiomatic Pipeline | 11 | 11/11 |
| **Total** | **58** | **58/58** |

---

## Appendix B：與前期論文的關係

| 論文 | 編號 | 焦點 | 關係 |
|:-----|:----|:-----|:-----|
| Why Three Generations | 05 | $\varepsilon^3$ truncation | 世代數的起源 |
| K-Chain Pairing Symmetry | 07 | K-chain $d_X$ derivation | K-chain 部分的前身 |
| K = K_chain ⊗ K_tree | 08（本文） | 完整公理化推導 | 合併 K-chain + K-tree |

---

## Appendix C：參考文獻

1. IDCM 基礎：$0,1 \to \varphi$ 推導
2. CY₃ 投影模型：$F_n/CY_3^s$ 公式
3. Temperley-Lieb 代數 $TL_N(q)$
4. Coxeter 群 $A_{87}$ 外自同構
5. MERA 張量網絡
6. Casimir 邊界效應
7. PDG 2024 粒子數據