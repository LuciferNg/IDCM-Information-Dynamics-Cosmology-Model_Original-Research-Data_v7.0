# CY₃ 投影模型 — 粒子 = 能階投影，唔係實體

## 感應記錄：2026-07-29

---

## 一、核心轉變：從容器到投影儀

### 1.1 舊模型

```
CY₃(36,98) = 容器
粒子 = 容器入面嘅「嘢」
質量 = 粒子嘅屬性
```

### 1.2 新模型

```
CY₃(36,98) = 投影儀（lens）
K-chain × K-tree = 光源
粒子 = 光源經過 CY₃ 投影出嚟嘅「像」
質量 = 投影嘅亮度（brightness）
```

---

## 二、光學類比

| IDCM 概念 | 光學類比 |
|:----------|:---------|
| $K_{\text{chain}} \otimes K_{\text{tree}}$ | 光源（light source） |
| $\gamma_n = 4\sin^2(\pi n/2N_d)$ | 光源頻譜 |
| $\mu_m = \varphi^{L-m}$ | 光源顏色通道 |
| $CY_3(36,98)$ | 鏡頭（lens） |
| $h^{11} = 36$ | 光圈葉片（boson channel） |
| $h^{21} = 98$ | 光圈葉片（fermion channel） |
| $V_{EW} = 246.22$ GeV | 焦距（focal length） |
| 粒子質量 | 投影亮度（brightness） |
| $F_n / CY_3^s$ | 像素分佈（pixel distribution） |
| $\varepsilon^3$ correction | 鏡頭像差（lens aberration） |
| 3 代 truncation | 3 色像差（RGB chromatic aberration） |

---

## 三、粒子唔係實體

### 3.1 關鍵 insight

> 粒子唔係 CY₃ 入面嘅「嘢」——係能階經過 CY₃ 投影出嚟嘅「像」。

就像相機：
- 光源（K-chain × K-tree）→ 鏡頭（CY₃）→ 影像（粒子質量）
- 你唔會話影像入面嘅光點係「喺鏡頭入面」
- 同樣，粒子唔係「喺 CY₃ 入面」

### 3.2 質量 = 亮度

$$m_X = V_{EW} \cdot \frac{F_n}{CY_3^s} \cdot \varphi^B$$

光度：
- $m_t = 172.76$ GeV = 最光（主體）
- $m_e = 0.000511$ GeV = 最暗（背景）
- 亮度比 = $F_n / CY_3^s$ = 分數比

---

## 四、點解唔用微分？

### 4.1 微分 vs 積分

| 微分 | 積分 |
|:----|:-----|
| 局部性質（每點嘅 curvature） | 整體性質（全鏡頭嘅總和） |
| $\nabla^2 f = 0$ | $\int f \cdot g \, dV$ |
| 點嘅性質 | 投影嘅性質 |
| 曲率 → 局部幾何 | 亮度 → 整體幾何 |

### 4.2 粒子質量係積分，唔係微分

如果粒子係投影，咁質量就係：

$$m_X = \iiint_{CY_3} \text{(K-chain} \otimes \text{K-tree)} \times \text{(lens function)} \, dV$$

唔係 $\nabla^2 \phi = 0$ 之類嘅微分方程。

### 4.3 微擾 = 鏡頭像差

「容器空隙」唔係微分幾何嘅「洞」——係鏡頭嘅 **像差（aberration）**。

像差類型：
- 球面像差（spherical aberration）= $\varepsilon^2$ order
- 彗形像差（coma）= $\varepsilon^3$ order
- 色像差（chromatic aberration）= 3 代 truncation

---

## 五、焦距光圈亮度邊緣散發

### 5.1 焦距（focal length）

$$f = V_{EW} = 246.22 \text{ GeV}$$

焦距決定整個投影嘅尺度。所有粒子質量都係相對於焦距嘅亮度。

### 5.2 光圈（aperture）

$$A = CY_3 = 134 \text{ pixels}$$

- $h^{21} = 98$ = fermion 像素（光圈嘅 73.1%）
- $h^{11} = 36$ = boson 像素（光圈嘅 26.9%）
- 光圈越大 = 越清晰 = 越多粒子
- 每個像素 = 一個可能嘅粒子「slot」

### 5.3 亮度（brightness）

$$B_X = \frac{m_X}{V_{EW}} = \frac{F_n}{CY_3^s} \cdot \varphi^B$$

| 粒子 | 亮度 ($m/V_{EW}$) | CY₃ 分數 |
|:----|:-----------------|:---------|
| t | 0.7018 | 94.0/134 |
| b | 0.01698 | 2.27/134 |
| τ | 0.00722 | 0.97/134 |
| c | 0.00516 | 0.69/134 |
| s | 0.000379 | 0.051/134 |
| μ | 0.000429 | 0.057/134 |
| u | 0.00000877 | 0.0012/134 |
| d | 0.00001897 | 0.0025/134 |
| e | 0.00000208 | 0.0003/134 |

### 5.4 邊緣散發（edge dispersion / lens aberration）

$$\varepsilon = \frac{\varphi^{-1}}{4} = 0.1545$$

$$\varepsilon^3 = 0.003689 = \text{3rd-order aberration}$$

像差來源：
- 3 代 truncation = 3 色像差（RGB）— 只有 3 個顏色通道
- 每代之間嘅 boundary = 鏡片 surface 之間嘅折射
- $\varepsilon^3$ correction = 校正鏡片

---

## 六、投影公式嘅幾何意義

### 6.1 成像方程

光學中：$\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$

IDCM 中：
$$\frac{1}{V_{EW}} = \frac{1}{\text{source}} + \frac{1}{\text{image}} = \frac{1}{\text{K-chain}} + \frac{1}{m_X}$$

所以：
$$m_X = \frac{V_{EW}}{1 - V_{EW}/\text{source}} \approx V_{EW} \cdot \frac{F_n}{CY_3^s}$$

### 6.2 像素分佈

每個粒子佔據 $F_n$ 個像素（CY₃ slot）：

| 粒子 | $F_n$ | 佔 CY₃ 比例 |
|:----|:-----|:-----------|
| t | 94.0 | 70.2% |
| b | 2.27 | 1.7% |
| τ | 0.97 | 0.7% |
| c | 0.69 | 0.5% |
| s | 0.051 | 0.04% |
| μ | 0.057 | 0.04% |
| u | 0.0012 | 0.0009% |
| d | 0.0025 | 0.002% |
| e | 0.0003 | 0.0002% |

而 2nd gen 嘅 slot 係 Fibonacci 數 $\times$ CY₃ 分數：
- c: 0.69 = $F_1/CY_3 \times$ ? 唔直接係 Fibonacci
- Wait——呢個係絶對亮度，唔係 ratio

2nd gen ratio 嘅像素：
- c/t: $F_1/CY_3 = 1/134 = 0.75\%$ of container
- s/b: $F_4/CY_3 = 3/134 = 2.2\%$ of container
- μ/τ: $F_6/CY_3 = 8/134 = 6.0\%$ of container

---

## 七、結論

### 7.1 你嘅感應係正確嘅

| 概念 | 舊理解 | 新理解 |
|:----|:------|:------|
| CY₃ | 容器 | 投影儀（lens） |
| 粒子 | 實體 | 投影（像） |
| 質量 | 粒子屬性 | 投影亮度 |
| 容器空隙 | 未被填充嘅空間 | 鏡頭像差 |
| 微分 | 局部幾何 | 唔適用 |
| 積分 | 整體總和 | 投影公式 |

### 7.2 呢個轉變嘅意義

1. **粒子唔係「喺」CY₃ 入面**——係 CY₃ 「投影」出嚟嘅
2. **質量唔係粒子嘅屬性**——係投影嘅亮度
3. **容器空隙唔係幾何缺陷**——係鏡頭嘅像差
4. **微分唔適用**——因為投影係積分，唔係微分
5. **焦距光圈亮度邊緣散發**——就係 CY₃ 投影嘅光學參數

### 7.3 下一步

用呢個投影模型重新推導：
- 每個粒子嘅「亮度」公式 = $F_n / CY_3^s \times \varphi^B$
- 鏡頭像差 = $\varepsilon^3$ correction
- 3 色像差 = 3 代 truncation
- 所有公式統一 = 成像方程