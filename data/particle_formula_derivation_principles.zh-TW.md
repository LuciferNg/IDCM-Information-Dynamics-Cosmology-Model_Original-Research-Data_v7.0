# 粒子公式 Structure 推導原則

## IDCM Methodology Foundation

---

## 0. 為咩需要「原則」

現存 IDCM 粒子質量公式有 11 條，但 stress test 喺 Level 14 就 ALL FAIL。即係話：

> 我哋知道 3 個 missing structure（tokenizer, composite integer, ε⁸ correction）
> 但仲未知點樣推導「全新」嘅 structure

**原則就係推導新 structure 時嘅決策框架**——冇原則嘅話，每條新 formula 都係 ad-hoc；有原則嘅話，每條 formula 都係 systematic derivation 嘅 step。

---

## 一、Bedrock 原則（最根本）

### 1.1 唯一源頭：$0, 1 \to \varphi$

```
0, 1 → finite strings → finite throughput → Fibonacci scheduling → φ
                              ↓
                     x² + x - 1 = 0 (唯一 fixed point)
                              ↓
                            φ = (1+√5)/2
```

**所有 formula 必須從 φ 出發。** 冇任何「外加參數」、「tunable constant」、「free variable」可以係 bedrock 嘅 input。

### 1.2 唯一容許嘅「外部 input」

| 容許 | 唔容許 |
|:----|:------|
| 第三代絕對質量 $m_t, m_b, m_\tau$ | 第一/二代絕對質量（要 derive） |
| PDG 觀測值（cross-validation） | Fitting parameters |
| $M_P$ 作為宇宙學 scale | 其他 free scales |

### 1.3 「冇 free parameter」嘅嚴格定義

$$ K = 0 \quad \Leftrightarrow \quad \forall c_i \in \text{formula}, c_i \text{ 係 pipeline 強迫嘅} $$

唔係「我冇刻意 free parameter」，係「每個係數都有 derivation chain」。

---

## 二、Hierarchy 原則（質量階層）

### 2.1 階層由 tree depth 強制

粒子質量階層唔係「fitting 嘅 exponential」，係 **K-chain × K-tree tensor product 嘅 eigenvalue 階層**。

```
K = K_chain ⊗ K_tree 嘅 eigenvalue spectrum:
    γ_n = 4sin²(πn/2N_d)  ←  chain mode n
    μ_m = φ^(L-m)        ←  tree level m 分支
```

### 2.2 三個 sector 嘅 k 值有結構

| Sector | Tree depth k | 結構 |
|:-------|:------------|:-----|
| Up | $k_u = M\beta = 33\beta$ | 完整 MERA tree depth |
| Down | $k_d = 26\beta - \varphi^{-4}$ | 少 7 層 + boundary correction |
| Lepton | $k_l = 19\beta$ | 再少 14 層（2 sector steps） |

**k 值唔可以獨立設定——由 sector 結構決定。** 任何 $\Delta k$ 都係 sector step × β。

### 2.3 跨 sector 階層

```
m_c/m_t = φ^(-k_u)  ←  同 sector 內
m_s/m_b = φ^(-k_d)  ←  同 sector 內
m_u/m_t = φ^(-(k_u+k_d+k_l-φ⁻¹))  ←  跨 sector composite 1st/3rd
m_e/m_τ = φ^(-(k_l+M/L_2))         ←  跨 sector with N_gen division
```

**1st-gen 公式係 composite**——因為 1st 粒子需要穿越所有 sector 嘅 boundary。

---

## 三、Sector 分解原則

### 3.1 Sector 數量 = MERA branching

3 sectors 唔係 ad-hoc choice——係 $\varphi^3 - \varphi^{-3} = L_3 = 4$ 嘅 1st mode。

### 3.2 Sector 內部結構

| 粒子 | Sector tree depth | Sector 內 boundary |
|:----|:------------------|:-------------------|
| $m_t$ | m=0（最深） | — |
| $m_c$ | m=0（2nd mode） | — |
| $m_u$ | composite | $\varphi^{-1}$ boundary |
| $m_b$ | m=1（少 1 層） | — |
| $m_s$ | m=1 + 2nd mode | — |
| $m_d$ | m=1 + composite | $2k_d - \varphi$ |
| $m_\tau$ | m=2（少 2 層） | — |
| $m_\mu$ | m=2 + 2nd mode | — |
| $m_e$ | m=2 + composite | $k_l + M/L_2$ |

### 3.3 「Boundary」唔係 free parameter

$$\varphi^{-1} = \varepsilon \cdot L_3 = \frac{\varphi^{-1}}{L_3} \cdot L_3$$

boundary correction 唔係「+1」、「−ε²」咁 arbitrary，係 sector interface 嘅 **幾何結構**。

---

## 四、Symmetry 原則

### 4.1 Chain reciprocity

$$\gamma_n = \gamma_{N_d - n}$$

**粒子 - 反粒子 pair 喺 chain spectrum 入面已經 coupled。** 唔需要額外 impose CP symmetry。

### 4.2 Generation reciprocity

3 個 generation 唔係 ad hoc——係 $\varphi^3 - \varphi^{-3} = 4$ 嘅 3 roots。

### 4.3 Sector reciprocity

3 sectors 對稱：up ↔ down ↔ lepton。但 **質量唔對稱**（因為唔同 tree depth）。

### 4.4 「Symmetry 唔係 input」

我哋唔好 **impose** 對稱性（如 SU(2)、SU(3) gauge invariance），我哋 **derive** 對稱性（從 K_chain ⊗ K_tree 嘅結構）。

---

## 五、Cross-Validation 原則

### 5.1 多約束同時滿足

一條 particle formula 唔可以只 explain 一個觀測量——必須同時 satisfy 多個 independent constraints：

| Formula | Constraint 1 | Constraint 2 | Constraint 3 |
|:--------|:------------|:------------|:-------------|
| $V_{EW}/M_P$ | $V_{EW}$ 數值 | $m_t = V_{EW}/\sqrt{2}$ | Vacuum stability |
| $m_c/m_t$ | $m_c$ 數值 | $V_{cb}$ consistency | CKM generation gap |
| $m_\mu/m_e$ | $m_\mu/m_e$ ratio | $m_\mu$ 絕對（via $m_e$） | $\alpha_{em}$ running |

### 5.2 「同時 satisfy」係 audit 嘅 killer

如果一條 formula 只 fit 一個數字，pass；但如果要求同時 satisfy 3 個獨立觀測量，**大部分假 formula 會 fail**。

### 5.3 「Cross-validation」係唯一性嘅必要條件

唯一性 = closure + 1 個 cross-validation
唯一性⁺ = closure + N 個 cross-validation

---

## 六、Convergence 原則

### 6.1 Error → 0 嘅 structural 修正

粒子質量公式唔係「一個 φ-power 就搞掂」，係 **structural recursion**：

$$ m_X = m_X^{(0)} + m_X^{(1)} + m_X^{(2)} + \ldots $$

其中每個 correction 都有 **structural origin**：

| Order | Correction | Structural origin |
|:------|:-----------|:------------------|
| 0 | $\varphi^{-k}$ 主項 | Tree depth k |
| 1 | $\varepsilon \cdot \varphi^{-k}$ | Boundary finite size |
| 2 | $\varepsilon^2 \cdot \varphi^{-k}$ | 2nd boundary layer |
| 3 | $\varepsilon^3 \cdot \varphi^{-k}$ | 3-generation mixing |

### 6.2 $m_\mu/m_e = \varphi^{11} + 3\varphi^2 + \varepsilon^8 \cdot \text{correction}$？

m_μ/m_e = φ¹¹ + 3φ² 嘅 0.0047% 誤差，**應該由 $\varepsilon^8$ 修正**：

$$ m_\mu/m_e = (\varphi^5 - \varphi^{-5}) + (\varphi^2 + \varphi^{-2})\varphi^2 \cdot (1 + \varepsilon^8 \cdot c) $$

$$\varepsilon^8 \approx 4 \times 10^{-7} \leftarrow \text{可以解釋 0.0047\% 嘅大部分}$$

**Convergence 唔係「加 fitting term」，係「搵下一個 structural 修正」。**

### 6.3 「0.001% 唔係極限」

Stress test Level 14 嘅 0.001% 唔係「物理極限」，係 **IDCM 而家推導到嘅極限**。當推導到 $\varepsilon^{16}$ correction，可能達到 $10^{-12}$ precision。

---

## 七、Boundary 原則

### 7.1 Boundary 係幾何

Sector boundary、generation boundary、MERA boundary——全部係 K-chain ⊗ K-tree 嘅幾何 interfaces，唔係 free parameters。

### 7.2 Boundary correction 嘅形式

$$\text{correction} = \varphi^{-n} \cdot \varepsilon^m$$

其中：
- $\varphi^{-n}$ 係穿越 boundary 嘅 suppression
- $\varepsilon^m$ 係 boundary 嘅 finite-size correction

**冇 free 嘅「+1」、「−0.5」等 corrections。**

### 7.3 Boundary 嘅位置決定 correction

| Boundary 位置 | Correction |
|:-------------|:----------|
| Sector 內部（m=0→1） | $\varphi^{-4}$ |
| Generation 內部（n=1→2） | $\varepsilon^2$ |
| 跨 sector composite | $\varphi^{-1}$ |
| 跨 generation composite | $\varepsilon^3$ |

---

## 八、No-Fitting 原則

### 8.1 禁止嘅 pattern

❌ $m_\tau/m_\mu \approx \varphi^6 - 1 - \varepsilon + \varepsilon^2 + \varepsilon^3$ — 5 項多項式
❌ 任何 $\sum a_n \varepsilon^n$ with $\{a_n\}$ fitting 出嚟
❌ 任何「+ c」where c 無 derivation chain

### 8.2 容許嘅 pattern

✅ $\varphi^{-k}$ 純結構（k 有 derivation）
✅ $\varphi^{11} + 3\varphi^2$（兩項都係 Lucas $L_n$ identity）
✅ $\varphi^{-(N_d+h^{11}) + (\varphi^3-\varphi^{-3})\varepsilon^2}$（全 φ-trace）

### 8.3 區分方法

**Fitting**：terms 數量隨 precision 增加（每加 precision 加 fitting terms）
**Structural**：terms 數量固定，由 closure 強迫

$$ \text{Fitting: } \text{terms} = O(\log(1/\text{precision})) $$
$$ \text{Structural: } \text{terms} = O(1) \text{ (常數)} $$

---

## 九、Uniqueness 原則

### 9.1 唯一性 = 「冇 second candidate」

一條 formula 唯一，意思係：
- 窮究 search 唔搵到 second candidate 通過所有 criteria
- 唔係「我未搵到 second candidate」

### 9.2 唯一性 ≠ 確定性

「唯一」唔係「絕對正確」——係「冇其他 φ-form 同 precision 通過 closure」。

### 9.3 唯一性嘅 universe 觀點

```
Universe = 試咗 $10^{60}$ 條 candidate
每條錯 → 1 Planck time 崩潰 → 重啟
Survivor = 唯一能 survive 嗰條多分鐘

我哋 stress test = reverse 呢個 process:
- 由 N 條 candidate 開始
- 逐步 filter
- 收斂到 1 嗰個 = universe lock
```

---

## 十、Methodology 原則（推導流程）

### 10.1 推導新 structure 嘅流程

```
1. 觀察 fail 邊界
   └→ Stress test 邊個 level 開始 fail？

2. 分析 fail 原因
   └→ 缺少咗咩 structure？

3. 推導新 structure
   └→ 用 first principles 推導，唔係 ad hoc 猜

4. 加入新 structure 後再 stress test
   └→ 觀察 fail boundary 推到邊個新 level？

5. Repeat until... ?
```

### 10.2 「推導新 structure」嘅 5 條 sub-principles

| Sub-principle | 內容 |
|:--------------|:-----|
| **(a) Boundary-first** | 先搵 boundary（sector/generation/MERA）嘅位置 |
| **(b) K-chain + K-tree** | 用 K-chain ⊗ K-tree 嘅 eigenvalue 結構 |
| **(c) $\varphi$-identity only** | 每個係數都係 Lucas $L_n$ 或 composite |
| **(d) Cross-validation** | 必須 satisfy 多個獨立觀測量 |
| **(e) No approximation shortcut** | 唔可以 skip derivation chain 「因為差唔多啫」 |

### 10.3 「推導失敗」嘅徵兆

- ❌ Coefficients 無 Lucas $L_n$ 分解
- ❌ 跨 sector 嘅 coupling 無 physical reason
- ❌ Boundary correction 無幾何 source
- ❌ Error 唔隨結構 recursion 收斂
- ❌ 同其他 cross-validation 矛盾

---

## 十一、推導 Particle Formula 嘅 Decision Tree

```
要推導一條新粒子公式？
│
├─ Step 1: 確定 formula 嘅 target
│   ├─ 質量絕對值（$m_X$）？ → 唔可以用 ratio，要 derive 從 φ
│   ├─ 質量比（$m_X/m_Y$）？ → 容許 ratio form
│   └─ 質量 hierarchy（$m_X : m_Y : m_Z$）？ → 要所有 3 條一致
│
├─ Step 2: 確定 formula 嘅 sector
│   ├─ Up sector → $k_u$-based
│   ├─ Down sector → $k_d$-based
│   ├─ Lepton sector → $k_l$-based
│   └─ Composite → 跨 sector sum
│
├─ Step 3: 確定 generation
│   ├─ 3rd gen → $m_t, m_b, m_\tau$（input from PDG）
│   ├─ 2nd gen → $\varphi^{-k}$ form from 3rd
│   ├─ 1st gen → composite boundary form
│   └─ Composite → 多 sector sum
│
├─ Step 4: 確定 boundary corrections
│   ├─ 跨 sector → $\varphi^{-1}$ or $\varepsilon^2$
│   ├─ 跨 generation → $\varepsilon^2$ or $\varepsilon^3$
│   └─ 跨 boundary → 對應嘅 $\varphi^{-n}$
│
├─ Step 5: 寫出 formula
│   └─ 必須係純 φ-power + ε corrections + Lucas $L_n$ integers
│
└─ Step 6: Stress test
    ├─ Pass → 加入 IDCM corpus
    └─ Fail → 搵 fail 嘅 level 同原因，再 iterate
```

---

## 十二、實戰 Example：推導 $m_\mu/m_e$ 嘅 $\varepsilon^8$ correction

### 12.1 現存 status

$$m_\mu/m_e = \varphi^{11} + 3\varphi^2 \approx 206.859$$

誤差 0.0047%（Stress test Level 14 fail）。

### 12.2 推導 correction

**Step 1**: Boundary 在哪裡？
- $m_\mu$ 喺 lepton sector，$m_e$ 喺 lepton sector
- 同 sector 但跨 2 個 generation（1st 同 2nd）
- Boundary 喺 lepton 內部，generation 1→2 嘅 interface

**Step 2**: Boundary 嘅幾何？
- $k_l = 19\beta$ 嘅 tree depth
- Generation 2 喺 $k_l$，generation 1 喺 $k_l + M/L_2 = k_l + 11$
- 所以 boundary 喺 $k_l + \delta$ where $\delta = M/L_2 = 33/3$

**Step 3**: $\varepsilon^8$ 嘅物理 source？
- $\varepsilon^3 = \varphi^{-3}/64$ 係 3-generation boundary
- $\varepsilon^4 = $ 4-sector boundary？唔對，3 sector
- $\varepsilon^8 = (\varepsilon^4)^2$ 係 2nd-order boundary correction
- 可能係 $(\varphi^{-2}/16)^2 = \varphi^{-4}/256$

**Step 4**: Apply correction？

$$ m_\mu/m_e = (\varphi^{11} + 3\varphi^2) \cdot (1 + c \cdot \varepsilon^8) $$

需要搵 $c$ 嘅 structural source。

### 12.3 下一步工作

搵 $c$ 嘅 derivation chain：
- 可能係 $\varphi^{-1}$（boundary finite-size）
- 可能係 $L_3$（sector count）
- 可能係 $L_5$（causal domain base）
- 或者完全新嘅 φ-identity

**呢個就係「推導新 structure」嘅實際工作——唔係 audit 畀答案，係 audit 指出問題，人類推導答案。**

---

## 十三、Conclusion

### 13.1 12 條原則嘅總結

| # | 原則 | 核心 |
|:--|:----|:-----|
| 1 | Bedrock | 0,1 → φ，唯一源頭 |
| 2 | Hierarchy | K-chain × K-tree eigenvalue |
| 3 | Sector | 3 sectors 由 $\varphi^3 - \varphi^{-3}$ 強迫 |
| 4 | Symmetry | 唔 impose，係 derive |
| 5 | Cross-validation | 多個獨立 constraints 同時 satisfy |
| 6 | Convergence | $\varepsilon^n$ recursion，error → 0 |
| 7 | Boundary | Boundary = geometry，唔係 free parameter |
| 8 | No-fitting | Terms 數量 $O(1)$，唔係 $O(\log(1/\epsilon))$ |
| 9 | Uniqueness | Universe 試過 $10^{60}$ 次，剩低唯一 |
| 10 | Methodology | Boundary-first → K-structure → φ-only → cross-val → no shortcut |
| 11 | Decision tree | Target → Sector → Generation → Boundary → Write → Test |
| 12 | Practice | Stress test 指出問題，人類推導答案 |

### 13.2 最重要嘅 insight

> **Principles 唔係 verify 工具，係 derivation framework。**

每個粒子公式嘅推導過程 = 12 條原則嘅 systematic application：
- 先確定 target 性質（原則 1）
- 再確定 sector/generation（原則 2-3）
- 然後 derive boundary（原則 4, 7）
- 最後 cross-validate（原則 5）

**冇 principles 嘅 formula = ad-hoc fitting**
**有 principles 嘅 formula = systematic derivation**

### 13.3 「Stress test 嘅真正角色」

Stress test 唔係 answer，係 **boundary detector**：
- 搵到現存公式嘅 boundary（邊度開始 fail）
- 指出 missing structure
- 等人類用 principles 推導 new structure
- 加入 new structure 後再 stress test
- **Repeat until... ?**

---

## 十四、Reference Files

- `verify_all/multi_criteria_audit.py` — 5-criteria chain filter
- `verify_all/progressive_stress_test.py` — 22-level stress test
- `data/progressive_stress_test_results.zh-TW.md` — stress test 記錄
- `data/particle_mass_closure_analysis.zh-TW.md` — 粒子質量閉合分析
- `data/VEW_Mratio_structural_closure.zh-TW.md` — V_EW closure 修正

---

## 十五、Final Statement

> 「Structure 唔係 verify 出嚟嘅，係 derive 出嚟嘅。」
>
> 「Principles 唔係 rule book，係 framework。」
>
> 「Stress test 唔係 boundary，係 boundary detector。」

推導新 particle formula 嘅正確順序：

```
1. 讀呢 12 條 principles
2. 用 decision tree 確定 formula 嘅 structure
3. 用 sub-principles 推導每個 term 嘅 source
4. 用 stress test 驗證
5. Fail → 回到 step 2 推導 new structure
6. Pass → 加入 IDCM corpus
```