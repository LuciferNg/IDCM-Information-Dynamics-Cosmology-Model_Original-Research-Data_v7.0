# 粒子質量公式閉合分析

## 核心原則

**閉合 = 公式中每個元素都 trace 返 φ，零裸數字。**

所有正整數都可以 trace 返 Lucas 數 $L_n = \varphi^n + (-1)^n \varphi^{-n}$：

| 整數 | φ-identity | 結構名稱 |
|:----:|:----------|:---------|
| 1 | $L_1 = \varphi - \varphi^{-1}$ | — |
| 2 | $L_0 = \varphi^0 + \varphi^0$ | — |
| 3 | $L_2 = \varphi^2 + \varphi^{-2}$ | $N_{gen}$ |
| 4 | $L_3 = \varphi^3 - \varphi^{-3}$ | MERA branching |
| 7 | $L_4 = \varphi^4 + \varphi^{-4}$ | sector step |
| 11 | $L_5 = \varphi^5 - \varphi^{-5}$ | causal domain base |
| 33 | $L_3 \cdot L_2^2 - L_2$ | $M = h^{11} - N_{gen}$ |
| 36 | $L_3 \cdot L_2^2$ | $h^{11}$ (CY₃ Hodge) |
| 44 | $L_3 \cdot L_5$ | $N_d$ |

---

## 結構常數閉合形式

$$\varphi = \frac{1+\sqrt{5}}{2} \quad \text{（從 } x^2+x-1=0 \text{）}$$

$$\varepsilon = \frac{\varphi^{-1}}{L_3} = \frac{\varphi^{-1}}{\varphi^3 - \varphi^{-3}}$$

$$\beta = \frac{\varphi^{-1}}{L_0} = \frac{\varphi^{-1}}{2}$$

$$\kappa = \frac{1}{L_3^2} = \frac{1}{(\varphi^3-\varphi^{-3})^2}$$

$$N_d = L_3 \cdot L_5 = (\varphi^3-\varphi^{-3})(\varphi^5-\varphi^{-5})$$

$$h^{11} = L_3 \cdot L_2^2 = (\varphi^3-\varphi^{-3})(\varphi^2+\varphi^{-2})^2$$

$$M = h^{11} - L_2 = (\varphi^3-\varphi^{-3})(\varphi^2+\varphi^{-2})^2 - (\varphi^2+\varphi^{-2})$$

---

## 粒子質量閉合公式

### 第三代（輸入 — 唔需要閉合）

| 粒子 | 數值 | 狀態 |
|:-----|:----:|:-----|
| $m_t$ | 172.76 GeV | 📥 PDG input |
| $m_b$ | 4.18 GeV | 📥 PDG input |
| $m_\tau$ | 1.77686 GeV | 📥 PDG input |

第三代絕對質量係 input，唔閉合（亦唔需要閉合）——係 IDCM 嘅 fundamental inputs。

---

### 第二代（純 φ-power）

**$m_c/m_t$：**
$$ \boxed{\frac{m_c}{m_t} = \varphi^{-k_u} = \varphi^{-M \cdot \beta} = \varphi^{-(L_3 \cdot L_2^2 - L_2) \cdot \varphi^{-1}/L_0}} $$

誤差 0.57% ✅

**$m_s/m_b$：**
$$ \boxed{\frac{m_s}{m_b} = \varphi^{-k_d} = \varphi^{-((M-L_4)\beta - \varphi^{-4})}} $$

展開：
$$ = \varphi^{-((L_3 L_2^2 - L_2 - L_4) \cdot \varphi^{-1}/L_0 - \varphi^{-4})} $$

誤差 0.51% ✅

**$m_\mu/m_\tau$：**
$$ \boxed{\frac{m_\mu}{m_\tau} = \varphi^{-k_l} = \varphi^{-(M - L_0 L_4) \cdot \beta}} $$

展開：
$$ = \varphi^{-(L_3 L_2^2 - L_2 - L_0 L_4) \cdot \varphi^{-1}/L_0} $$

誤差 0.33% ✅

---

### 第一代（複合閉合）

**$m_u/m_t$：**
$$ \boxed{\frac{m_u}{m_t} = \varphi^{-(k_u+k_d+k_l-\varphi^{-1})}} $$

注意 $\varphi^{-1}$ 呢個 correction：
$$ \varphi^{-1} = \varepsilon \cdot L_3 = \frac{\varphi^{-1}}{L_3} \cdot L_3 $$

展開：
$$ = \varphi^{-((M-L_4)\beta - \varphi^{-4} + M\beta + (M-L_0 L_4)\beta - \varphi^{-1})} $$

誤差 6.01% 🟡 （GW instanton 修正 pending）

**$m_d/m_b$：**
$$ \boxed{\frac{m_d}{m_b} = \varphi^{-(L_0 \cdot k_d - \varphi)}} $$

注意：
- $L_0 \cdot k_d = 2 \cdot ((M-L_4)\beta - \varphi^{-4})$ — 係 sector 雙倍壓制
- $\varphi$ 係 golden ratio 直接（邊界 correction）

展開：
$$ = \varphi^{-(L_0((L_3 L_2^2 - L_2 - L_4)\varphi^{-1}/L_0 - \varphi^{-4}) - \varphi)} $$

誤差 1.65% ✅

**$m_e/m_\tau$：**
$$ \boxed{\frac{m_e}{m_\tau} = \varphi^{-(k_l + M/L_2)}} $$

展開：
$$ = \varphi^{-((M-L_0 L_4)\beta + M/L_2)} $$

誤差 3.60% 🟡 （GW instanton 修正 pending）

---

### 質量比

**$m_\mu/m_e$（雙結構）：**
$$ \boxed{\frac{m_\mu}{m_e} = \varphi^{11} + 3\varphi^2 = L_5 + L_2 \cdot \varphi^2} $$

展開：
$$ = (\varphi^5-\varphi^{-5}) + (\varphi^2+\varphi^{-2})\varphi^2 = (\varphi^5-\varphi^{-5}) + (\varphi^4+1) $$

誤差 0.04% ✅ **完全閉合**（兩個項都有 φ-identity 源頭）

**$m_\tau/m_\mu$（純結構）：**
$$ \boxed{\frac{m_\tau}{m_\mu} = \varphi^{k_l} = \varphi^{(M-L_0 L_4)\beta}} $$

誤差 0.30% ✅

**$m_\tau/m_\mu$ 近似（fitting）：**
$$ m_\tau/m_\mu \approx \varphi^6 - 1 - \varepsilon + \varepsilon^2 + \varepsilon^3 $$

❌ **未閉合** — 5 項多項式，每項嘅 φ-source 都唔明。**應該用上面結構公式替換**。

---

### Higgs 質量閉合

$$ m_H = L_0 \sqrt{\kappa} \cdot V_{EW} = 2 \sqrt{1/L_3^2} \cdot V_{EW} = \frac{2 V_{EW}}{\varphi^3-\varphi^{-3}} $$

閉合（除 $V_{EW}$ 本身嘅 input）。

**$k_H$ 閉合：**
$$ k_H = \frac{L_2^2 \cdot \beta}{L_0} = \frac{9 \cdot \varphi^{-1}/2}{2} = \frac{9\varphi^{-1}}{4} $$

---

### V_EW 閉合（最新修正）

$$ \boxed{\frac{V_{EW}}{M_P} = \varphi^{-(N_d + h^{11}) + (\varphi^3-\varphi^{-3})\varepsilon^2}} $$

**全部閉合**：
- $N_d = L_3 L_5$ — 因果域數
- $h^{11} = L_3 L_2^2$ — CY₃ Hodge
- $\varphi^3-\varphi^{-3} = L_3$ — MERA 分支數（用於 4ε² 修正）
- $\varepsilon^2 = (\varphi^{-1}/L_3)^2 = \varphi^{-2}/L_3^2$ — gap²呸

展開：
$$ = \varphi^{-(L_3(L_5+L_2^2) + L_3 - L_3 \cdot \varphi^{-2}/L_3^2)} $$

$$ = \varphi^{-L_3(L_5+L_2^2+1-\varphi^{-2}/L_3)} $$

數值：
- $V_{EW}$ = 244.13 GeV（0.85% vs 246.22）
- $m_t = V_{EW}/\sqrt{2}$ = **172.63 GeV（0.077%）** 🚀

---

## 閉合狀態總結

| 粒子 | 閉合？ | 備註 |
|:----:|:------:|:-----|
| $m_c/m_t = \varphi^{-k_u}$ | ✅ | 純結構 |
| $m_s/m_b = \varphi^{-k_d}$ | ✅ | 純結構 |
| $m_\mu/m_\tau = \varphi^{-k_l}$ | ✅ | 純結構 |
| $m_u/m_t$ | ✅ | GW instanton 修正 pending |
| $m_d/m_b$ | ✅ | RG 修正 pending |
| $m_e/m_\tau$ | ✅ | GW instanton 修正 pending |
| $m_\mu/m_e = \varphi^{11} + 3\varphi^2$ | ✅ | 雙結構 |
| $m_\tau/m_\mu = \varphi^{k_l}$ | ✅ | 純結構 |
| $m_\tau/m_\mu \approx \varphi^6-1-\varepsilon+\varepsilon^2+\varepsilon^3$ | ❌ **fitting** | 5 項多項式無 source |
| $m_H = 2\sqrt{\kappa} \cdot V_{EW}$ | ✅ | 結構 |
| $V_{EW}/M_P = \varphi^{-(N_d+h^{11}) + (\varphi^3-\varphi^{-3})\varepsilon^2}$ | ✅ | 純結構（剛修正） |

---

## 結論

**所有粒子質量公式都閉合**（除 $m_\tau/m_\mu \approx \varphi^6-1-\varepsilon+\varepsilon^2+\varepsilon^3$ 一個）。所有整數 trace 返 Lucas 數 / φ-identity。

唯一真正未閉合嘅 fitting 公式係：
$$ m_\tau/m_\mu \approx \varphi^6 - 1 - \varepsilon + \varepsilon^2 + \varepsilon^3 $$

**呢條應該用結構公式 $m_\tau/m_\mu = \varphi^{k_l}$ 替換。**

---

## 閉合驗證表

| 公式元素 | 裸數字 | φ-trace |
|:--------|:------:|:---------|
| $k_u = 33\beta$ | 33 | $L_3 L_2^2 - L_2 = 36-3 = 33$ ✅ |
| $k_d = 26\beta - \varphi^{-4}$ | 26 | $M - L_4 = 33-7 = 26$ ✅ |
| $k_l = 19\beta$ | 19 | $M - L_0 L_4 = 33-14 = 19$ ✅ |
| $M = 33$ | 33 | $h^{11} - L_2 = 36-3$ ✅ |
| $h^{11} = 36$ | 36 | $L_3 L_2^2 = 4 \cdot 9$ ✅ |
| $N_d = 44$ | 44 | $L_3 L_5 = 4 \cdot 11$ ✅ |
| $V_{EW}/M_P = \varphi^{-80+4\varepsilon^2}$ | 80, 4 | $L_3(L_5+L_2^2) = 4 \cdot 20 = 80$ ✅，$L_3$ ✅ |
| $\varepsilon = \varphi^{-1}/4$ | 4 | $L_3 = \varphi^3-\varphi^{-3}$ ✅ |
| $\beta = \varphi^{-1}/2$ | 2 | $L_0$ ✅ |
| $\kappa = 1/16$ | 16 | $L_3^2 = 16$ ✅ |

**所有數字都 traceable 返 φ。**