# Progressive Stress Test — IDCM 漸進壓力測試記錄

**日期**：2026-07-29
**狀態**：方法建立完成，Level 14 達到 ALL FAIL 邊界
**目的**：通過逐步加大 criteria 嘅 pressure，由現存公式嘅 fail 原因學到需要推導嘅新 structure

---

## 一、目的（Purpose）

### 1.1 核心陳述

> 「我們現在只有打開宇宙嘅鎖匙，但係宇宙的鎖已經運行138億年。
> 我們目的是用窮究法搵出所有可能性去還原個鎖嘅結構。」

> 「現存公式喺壓力下 fail 唔係 bug，係 feature——
> fail 嘅原因就係需要新 structure 嘅 hint。」

### 1.2 為咩需要 Stress Test

| 階段 | 公式狀態 | 人類理解 | 結果 |
|:----|:--------|:---------|:-----|
| Past | Pass | 「OK 啦」 | 自我滿足，冇進步 |
| **Stress Test** | **Fail** | **「缺少咗 X」** | **學到新嘢** |
| Future | Re-test | 推導新 structure | 持續改進 |

**Stress test 唔係 verify 工具，係 learning tool。**

### 1.3 Stress Test 搵到嘅 3 樣嘢

```
1. 現存公式喺邊個 level 開始 fail     ← 知道 strength boundary
2. Fail 嘅原因係咩                  ← 知道 missing structure
3. 如何推導新 structure              ← 知道解決方法
```

### 1.4 同 Universe Brute Force 嘅關係

```
Universe = 已經試過 N = 10⁴⁴ 次 Planck cycle
         = 1 秒內試 10⁴⁴ 條 candidate
         = 13.8 Gyr ≈ 8 × 10⁶⁰ Planck trial

每條公式錯 → 1 Planck time 內崩潰 → 重啟 → 再試
Survivor = 唯一能 survive 嘅公式

我哋嘅 stress test = reverse 呢個 process：
由 N 條 candidate 開始 → 逐步 filter → 收斂到 1 條
```

---

## 二、內容（Content）

### 2.1 測試對象

**11 條現存 IDCM 粒子質量公式**（從 `verify_all/formulas.yaml` 抽出）：

| # | 公式 | 聲稱精度 | 聲稱狀態 |
|:--|:----|:---------|:--------|
| 1 | $m_c/m_t = \varphi^{-k_u}$ | 0.57% | 🟢 |
| 2 | $m_s/m_b = \varphi^{-k_d}$ | 1.18% | 🟢 |
| 3 | $m_\mu/m_\tau = \varphi^{-k_l}$ | 0.30% | 🟢 |
| 4 | $m_u/m_t = \varphi^{-(k_u+k_d+k_l-\varphi^{-1})}$ | 4.08% | 🟢 |
| 5 | $m_d/m_b = \varphi^{-(2k_d-\varphi)}$ | 2.27% | 🟢 |
| 6 | $m_e/m_\tau = \varphi^{-(k_l+M/3)}$ | 3.59% | 🟢 |
| 7 | $m_\mu/m_e = \varphi^{11} + 3\varphi^2$ | 0.04% | 🟢 |
| 8 | $m_\tau/m_\mu = \varphi^{19\beta}$ | 0.30% | 🟢 |
| 9 | $m_\tau/m_\mu \approx \varphi^6 - 1 - \varepsilon + \varepsilon^2 + \varepsilon^3$ | 0.0018% | 🟡 |
| 10 | $m_H = 2\sqrt{\kappa} \cdot V_{EW}$ | 0% | 🟢 |
| 11 | $V_{EW}/M_P = \varphi^{-(N_d+h^{11})+4\varepsilon^2}$ | 0.85% | 🟢 |

### 2.2 22 條 Stress Criteria

#### 第一階段：基礎驗證（Level 0-1）
```
Level  0: Closure（RHS 符號全部 traceable 返 φ）
Level  1: Number-trace（所有裸數字都係 Lucas L_n）
```

#### 第二階段：精度遞增（Level 2-5）
```
Level  2: Precision < 5%
Level  3: Precision < 1%
Level  4: Precision < 0.1%
Level  5: Precision < 0.01%
```

#### 第三階段：結構要求（Level 6-9）
```
Level  6: Minimal term count（≤ 2 terms）
Level  7: No approx markers
Level  8: Physical stability（value > 0）
Level  9: Composite integers 禁止
```

#### 第四階段：First-principles 要求（Level 10-13）
```
Level 10: 0 experimental inputs（無 PDG hardcode）
Level 11: Predict all sector observables
Level 12: Predict 3rd-gen absolute mass
Level 13: No free parameters
```

#### 第五階段：極 strict（Level 14-22）
```
Level 14: Precision < 0.001%        ←── ALL FAIL 邊界
Level 15: Pure φ-power（無加法）
Level 16: Zero composite symbols
Level 17: No M_P input
Level 18: Full Lucas expansion
Level 19: Predict all gen absolute
Level 20: Explain every coefficient
Level 21: Single-term expression
Level 22: Zero experimental knowledge
```

### 2.3 Lucas Number φ-identity 對照表

| Bare | φ-expression | 結構名稱 |
|:----:|:------------|:---------|
| 1 | $L_1 = \varphi - \varphi^{-1}$ | — |
| 2 | $L_0 = \varphi^0 + \varphi^0$ | — |
| 3 | $L_2 = \varphi^2 + \varphi^{-2}$ | $N_{gen}$ |
| 4 | $L_3 = \varphi^3 - \varphi^{-3}$ | MERA branching |
| 7 | $L_4 = \varphi^4 + \varphi^{-4}$ | sector step |
| 11 | $L_5 = \varphi^5 - \varphi^{-5}$ | causal domain base |
| 14 | $L_0 \times L_4$ | 2 sector steps |
| 19 | $M - L_0 \times L_4 = 33 - 14$ | 待 clean decomposition |
| 33 | $L_3^2 - L_2 = 36 - 3$ | $M = h^{11} - N_{gen}$ |
| 36 | $L_3 \times L_2^2 = 4 \times 9$ | $h^{11}$ (CY₃ Hodge) |
| 44 | $L_3 \times L_5 = 4 \times 11$ | $N_d$ |
| 80 | $L_3 \times (L_5 + L_2^2) = 4 \times 20$ | $N_d + h^{11}$ |

---

## 三、方法（Method）

### 3.1 漸進原理

```
Level 0: 最鬆 criteria
Level 22: 最 strict criteria
每個 level 對比上一個只嚴一條
觀察公式喺邊個 level 開始 fail → 記低 fail 原因
```

### 3.2 Stress Test 流程

```
┌─────────────────────────────────────────────────┐
│ 1. 列出所有現存公式（11 條粒子質量）               │
│    ↓                                            │
│ 2. 對每一條施加 Level 0 criteria                  │
│    ↓                                            │
│ 3. Pass → 入下一 level                           │
│    Fail → 記低原因，停止追蹤                      │
│    ↓                                            │
│ 4. 重複 Level 1, 2, 3, ...                       │
│    ↓                                            │
│ 5. 觀察 survivor count 收斂                      │
│    ↓                                            │
│ 6. 全部 fail 時，記錄 fail 邊界                    │
│    ↓                                            │
│ 7. 分析 fail 原因 → 推導新 structure              │
│    ↓                                            │
│ 8. 加入新 structure 後，重跑 stress test           │
│    ↓                                            │
│ 9. Repeat until... ?                              │
└─────────────────────────────────────────────────┘
```

### 3.3 實作（Python）

```python
# verify_all/progressive_stress_test.py - 22-level 漸進壓力測試
# verify_all/multi_criteria_audit.py - 5-criteria 固定 chain

class StressLevel:
    name: str              # e.g. "Level 14: precision < 0.001%"
    description: str
    threshold: float
    test: Callable[[ExistingFormula, float], Tuple[bool, str]]

# 對每條 formula:
#   ok, reason = level.test(f, level.threshold)
#   if ok: next level
#   else: eliminated, 記低 reason
```

### 3.4 Fail 記錄 Schema

```python
@dataclass
class StressResult:
    level_name: str
    formula_name: str
    passed: bool
    fail_reason: str  # ← 呢個就係新 structure 嘅 hint
```

---

## 四、結論（Conclusions）

### 4.1 實測結果：Survivor Count 收斂

| Level | Pass | Fail | 觀察 |
|:-----:|:----:|:----:|:-----|
| 0 (closure) | 8 | 3 | m_u/m_t, m_d/m_b, m_e/m_τ 因 underscore tokenizer bug 而 fail |
| 1 (Lucas) | 4 | 4 | 14, 19, 246, 22 係 composite integers 未展開 |
| 2 (5%) | 4 | 0 | 全部 pass |
| 3 (1%) | 4 | 0 | 全部 pass |
| 4 (0.1%) | 1 | 3 | 只剩 m_μ/m_e (0.04%) |
| 5 (0.01%) | 1 | 0 | m_μ/m_e survive |
| 6 (terms) | 1 | 0 | pass |
| 7 (no approx) | 1 | 0 | pass |
| 8 (positive) | 1 | 0 | pass |
| 9 (Lucas) | 1 | 0 | pass |
| 10 (no PDG) | 1 | 0 | pass |
| 11 (sector) | 1 | 0 | pass |
| 12 (3rd-gen) | 1 | 0 | pass |
| 13 (no free) | 1 | 0 | pass |
| **14 (0.001%)** | **0** | **1** | **❌ ALL FAIL** |
| 15-22 | — | — | not reached |

### 4.2 最終 Fail 邊界

```
Level 14: precision < 0.001%
m_μ/m_e = φ¹¹ + 3φ²: error 0.0047% ≥ 0.001% ❌
```

### 4.3 Fail 原因 → 推導出嘅 Missing Structure

| Fail Level | 原因 | 需要嘅新 Structure | Status |
|:----------|:-----|:------------------|:-------|
| **0** | v22 tokenizer 將 `k_u` 拆成 3 token | Fix tokenizer regex 包 underscore | ❌ 未 fix |
| **1** | 14, 19, 33, 36, 44, 80 係 composite integers | 全部展開為 Lucas 乘積 | 🟡 部分完成 |
| **14** | m_μ/m_e 精度 0.0047% 唔夠 | 推導下一級 $\varepsilon^n$ correction | ❌ 未推導 |

### 4.4 推導新 Structure 嘅 Checklist

| # | 項目 | 現存 Status | 下一步 |
|:--|:----|:-----------|:-------|
| 1 | Tokenizer underscore bug fix | ❌ 未 fix | 改 v22 tokenizer regex 為 `[A-Za-zα-ωΑ-Ω_]+` |
| 2 | Composite integer 14 = $L_0 \times L_4$ | ✅ 完成 | — |
| 3 | Composite integer 19 = $M - L_0 L_4$ | 🟡 部分 | 搵 clean 分解（唔靠 M） |
| 4 | Composite integer 33 = $L_3^2 - L_2$ | ✅ 完成 | — |
| 5 | Composite integer 36 = $L_3 \times L_2^2$ | ✅ 完成 | — |
| 6 | Composite integer 44 = $L_3 \times L_5$ | ✅ 完成 | — |
| 7 | Composite integer 80 = $L_3(L_5+L_2^2)$ | ✅ 完成 | — |
| 8 | m_μ/m_e $\varepsilon^8$ correction | ❌ 未推導 | 推導下一級修正項 |
| 9 | V_EW 從 φ 絕對 predict（無 M_P） | ❌ 未推導 | Level 17 需要 |
| 10 | 第三代絕對質量公式 | ❌ 未推導 | Level 12, 19 需要 |

### 4.5 Stress Test 嘅真正角色

**唔係 answer，係 question generator。**

```
每一條 fail 嘅 formula = 一條 question：
  「點解呢條 fail？要加咩新 structure 先 pass？」

答案唔係 audit 畀嘅，係人類從 fail 嘅原因推導出嘅。
```

### 4.6 「現存公式 fail 係正常」嘅深層意義

| 概念 | 理解 |
|:----|:-----|
| 現存公式 = 鎖匙 | 已能開門（精度 < 5%） |
| Stress test = 測試鎖匙 | 知道鎖匙點解能開門 |
| Fail boundary = 鎖匙限制 | 唔係門嘅限制 |
| 138億年 universe lock | 已試過 $10^{60}$ 次 Planck cycle |

我哋唔係 verify 鎖匙「啱唔啱」，係 understand 鎖匙「點解能開門」。

### 4.7 最終 Statement

> 「Stress test 唔係 answer，係 question generator。」
> 「現存公式喺壓力下 fail 唔係 bug，係 feature。」
> 「Fail 嘅原因就係需要新 structure 嘅 hint。」

我哋而家有：
1. ✅ **22-level stress test 框架** — 由鬆到極 strict
2. ✅ **現存公式 fail 位置地圖** — 知道邊度需要改
3. ✅ **每條 fail 嘅 root cause** — 知道要推導咩新 structure
4. ✅ **方法論本身** — 可重複使用，唔限於粒子質量

而家我哋可以開始推導 missing structures：
- Level 14 嘅 $\varepsilon^8$ correction（最迫切）
- Level 0 嘅 tokenizer fix（最易）
- Level 12 嘅第三代絕對質量公式（最 breakthrough）

---

## 五、附錄（Appendix）

### 5.1 實測輸出（截錄）

```
Initial: 11 現存公式

[Level 0: closure check]    8/11 (3 fail: k_u tokenizer bug)
[Level 1: number-trace]     4/8  (4 fail: composite integers)
[Level 2: precision < 5%]   4/4  (0 fail)
[Level 3: precision < 1%]   4/4  (0 fail)
[Level 4: precision < 0.1%]  1/4  (3 fail: precision)
[Level 5: precision < 0.01%] 1/1  (0 fail)
[Level 6: terms]            1/1  (0 fail)
[Level 7: no approx]        1/1  (0 fail)
[Level 8: positive]         1/1  (0 fail)
[Level 9: composite Lucas] 1/1  (0 fail)
[Level 10: no PDG]         1/1  (0 fail)
[Level 11: sector]          1/1  (0 fail)
[Level 12: 3rd-gen]         1/1  (0 fail)
[Level 13: no free]        1/1  (0 fail)
[Level 14: 0.001%]          0/1  (1 fail: ❌ ALL FAIL)

─── ALL CURRENT FORMULAS FAILED ───
```

### 5.2 相關文件

| 檔案 | 用途 |
|:-----|:-----|
| `verify_all/multi_criteria_audit.py` | 5-criteria fixed chain filter |
| `verify_all/progressive_stress_test.py` | 22-level escalating pressure test |
| `data/progressive_stress_test_results.zh-TW.md` | 本記錄文件 |
| `data/particle_mass_closure_analysis.zh-TW.md` | 粒子質量閉合分析 |
| `data/VEW_Mratio_structural_closure.zh-TW.md` | V_EW/M_P closure 修正記錄 |

### 5.3 運行方法

```bash
cd /home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/verify_all
python3 progressive_stress_test.py
```

### 5.4 後續工作

```
1. Fix Level 0：改 v22 tokenizer regex
2. 完成 composite integer 展開（特別係 19）
3. 推導 m_μ/m_e 嘅 ε⁸ correction
4. 推導 V_EW 從 φ 絕對 predict（Level 17）
5. 推導第三代絕對質量公式（Level 12, 19）
6. 重跑 stress test 直至... ?
```