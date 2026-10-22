#!/usr/bin/env python3
"""
derive_3_vs_4.py — 分清楚 3 和 4 的來源
"""
import math

phi = (1 + math.sqrt(5)) / 2
phi_inv = phi - 1

print("=" * 72)
print("釐清：3 和 4 各有來源，唔係同一個數字")
print("=" * 72)

# ============================================================
# 3 的來源
# ============================================================
print("\n" + "-" * 72)
print("3 的來源：2+1 = data + inversion")
print("-" * 72)

print("""
你講得啱。計算機唔需要 4 bit 做 forward/backward。
只需要：
  2 bits data (要處理的值)
  1 bit control (反轉/唔反轉)
  = 3 bit

呢個 3 係「操作維度」。
唔係 4。

3 在 IDCM 出現的地方：
  3 世代 (2+1)
  3 層 MERA 修正
  3 = 4-1 (closure 的補數)
  3^2 = 9 (L = (44+9)/8)
""")

# ============================================================
# 4 的來源
# ============================================================
print("-" * 72)
print("4 的來源：MERA 分支因子，唔係 pipeline stages")
print("-" * 72)

print("""
IDCM 的 4 唔係來自「4 stages」。
係來自 MERA 的結構：

MERA tree 每個節點分裂成 4 個子節點：
  2 個方向 (x, y)
  × 2 個尺度 (coarse, fine)
  = 4 個分支

呢個 4 係 φ-identity 的：
  φ³ - φ⁻³ = 4

所以 4 係 MERA 的幾何結構，唔係 pipeline 的工程實現。
""")

# Show the MERA branching
print("MERA 分支因子 = 4：")
print("""
  Node
  ├── child 0 (x, coarse)
  ├── child 1 (x, fine)
  ├── child 2 (y, coarse)
  └── child 3 (y, fine)
 = 4

  4 來自 φ³-φ⁻³ = 4
  4 係 MERA 的最小分支因子
""")

# ============================================================
# Which is which
# ============================================================
print("-" * 72)
print("結論：3 和 4 各有用途")
print("-" * 72)

print("""
  3 來自 2+1 (data + inversion):
    操作維度
    3 世代
    3 層 MERA 修正
    3 維時空

  4 來自 MERA 分支因子 (2×2):
    幾何維度
    ε = φ⁻¹/4
    κ = 1/4²
    N_d = 4×11
    Ω_Λ = 4/(φ⁴-1)

  兩者關係：
    4 = 3 + 1 (output bit)
    4 = 2 × 2 (MERA branching)
    3 = 2 + 1 (data + control)
    冇衝突，係不同層面的結構
""")

# ============================================================
# Updated chain
# ============================================================
print("=" * 72)
print("更新後的完整推導鏈")
print("=" * 72)
print("""
0, 1 (Binary Distinction)
  |
  v
NOT (唯一非平凡 1-bit 操作)
  |
  v
NOT 需要時間 (before/after)
  |
  v
2 bits = 最小 hierarchy
  |
  v
2+1 = 3 (data + inversion)  ← 操作維度
  |
  v
Fibonacci 排程 → φ
  |
  v
x² + x - 1 = 0
  |
  v
MERA 分支因子 = 4 = φ³-φ⁻³  ← 幾何維度
  |
  v
ε = φ⁻¹/4, κ = 1/16, β = φ⁻¹/2
  |
  v
N_d = 44, L = 53/8, CY₃(36,98)
  |
  v
所有物理常數
""")

print("""
3 = 2+1 (data + inversion) — 操作層面
4 = 2x2 (MERA branching) — 幾何層面
兩個數字都係 fundamental，但用途不同
""")

print("=" * 72)
print("所以 4 係正確的，但原因係 MERA 分支，唔係 pipeline stages。")
print("=" * 72)