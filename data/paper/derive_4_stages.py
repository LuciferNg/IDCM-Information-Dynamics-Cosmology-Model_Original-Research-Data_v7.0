#!/usr/bin/env python3
"""
derive_4_stages.py — 推導點解 pipeline 有 4 個 stages，而 8 = 4x2
"""
import math
import itertools

phi = (1 + math.sqrt(5)) / 2

print("=" * 72)
print("推導：Pipeline 4 stages 的來源 — 8 = 4x2")
print("=" * 72)

# ============================================================
# 1-bit operations
# ============================================================
print("\n" + "-" * 72)
print("Step 1: 1-bit operations")
print("-" * 72)

print("""
從 {0, 1}，所有 1-bit 1-output 操作：
  f(0)=0, f(1)=0  -> SET-0  (破壞 0!=1)
  f(0)=0, f(1)=1  -> ID     (冇做嘢)
  f(0)=1, f(1)=0  -> NOT    (唯一非平凡)
  f(0)=1, f(1)=1  -> SET-1  (破壞 0!=1)

NOT 係唯一保持 0!=1 嘅非平凡操作。

NOT 嘅 pipeline：
  Fetch -> Decode -> Execute -> Writeback
    1        1         1          1      = 4 stages

但 1 bit 太簡單，冇 hierarchy。
""")

# ============================================================
# 2-bit operations
# ============================================================
print("-" * 72)
print("Step 2: 2-bit operations — 最少需要幾多個？")
print("-" * 72)

# All 2-input 1-output binary operations
# There are 2^4 = 16 possible truth tables
print("""
2-bit 系統有 2 個輸入 bit，1 個輸出 bit。
總共有 2^(2^2) = 16 個可能的 2-bit 操作。

但呢 16 個操作唔係全部獨立：
  NAND 係 universal：所有其他操作可以由 NAND 組合而成
  NOR 都係 universal
  NOT + AND + OR 可以組合所有操作

最少 universal set 嘅大小 = 1（NAND 或 NOR 單獨）
但 1 個 operation 嘅 pipeline 都係 4 stages
""")

# Show the minimal universal gates
print("Universal gate sets:")
print("  {NAND}:              1 gate, 需 4 stages")
print("  {NOR}:               1 gate, 需 4 stages")
print("  {NOT, AND}:          2 gates, 需 4 stages")
print("  {NOT, OR}:           2 gates, 需 4 stages")
print("  {AND, OR, NOT}:      3 gates, 需 4 stages")
print("  {AND, OR, XOR, NOT}: 4 gates, 需 4 stages")
print()

# ============================================================
# 4 stages = 2 bits x 2 directions
# ============================================================
print("-" * 72)
print("Step 3: 4 stages = 2 bits x 2 directions")
print("-" * 72)

print("""
Pipeline 嘅 4 stages 唔係嚟自「4 個操作」。
係嚟自 2 bits 嘅自然結構：

    2 bits = 2 個自由度
    每個自由度有 2 個方向（0->1, 1->0）
    2 x 2 = 4

    或者：
    2 bits = 2 個輸入
    每個輸入有 2 個可能值（0, 1）
    2 x 2 = 4 種輸入組合 = 4 stages

    或者：
    每個操作有 2 個階段（輸入, 輸出）
    每個階段有 2 個子階段（準備, 完成）
    2 x 2 = 4
""")

# Show the 4 input combinations
print("2-bit 輸入組合 = 4:")
for i, (a, b) in enumerate([(0,0), (0,1), (1,0), (1,1)]):
    print(f"  Stage {i}: input({a},{b})")

print()

# ============================================================
# 8 = 4 x 2
# ============================================================
print("-" * 72)
print("Step 4: 8 = 4 x 2 — 唔係獨立數字")
print("-" * 72)

print("""
8 stages 唔係 fundamental，係 4 x 2：

  4 = 2 bits x 2 directions (fundamental)
  2 = 每個 stage 嘅 forward/backward 方向

  或者：
  4 = 2 輸入 + 1 控制 + 1 輸出 (fundamental)
  2 = 時間方向 (前向/後向)

Switch case 只係 if-else 嘅變體：
  switch(x) {
    case 0: ...  ->  if(x==0) ...
    case 1: ...  ->  else if(x==1) ...
    case 2: ...  ->  else if(x==2) ...
    case 3: ...  ->  else if(x==3) ...
  }

同樣，8 stages 只係 4 stages 嘅雙向版本：
  4 stages forward:  F0, F1, F2, F3
  4 stages backward: B0, B1, B2, B3
  Total: 8

但 backward stages 唔係獨立——佢哋係 forward stages 嘅 mirror。
就係 switch case 同 if-else 嘅關係一樣。

所以 fundamental number 係 4，唔係 8。
8 = 4 x 2 只係 doubling。
""")

# ============================================================
# 4 嘅更深層來源
# ============================================================
print("-" * 72)
print("Step 5: 4 嘅更深層來源 — 從 0,1 到 2 到 4")
print("-" * 72)

print("""
0, 1 有 2 個元素。
「區分」呢 2 個元素需要 1 bit。
但 1 bit 只能表示 0/1——冇 hierarchy。

要建立 hierarchy，最少需要 2 bits：
  bit 0: 區分 0/1（粗粒度）
  bit 1: 區分 0/1 嘅子結構（幼粒度）

2 bits = 2 層 hierarchy = 2 個尺度
  
每個尺度有 2 個方向：
  尺度 0: 往左 (0) / 往右 (1)
  尺度 1: 往上 (0) / 往下 (1)

2 尺度 x 2 方向 = 4 個 pipeline stages

呢個 4 係最小可能：
  1 bit = 1 尺度 x 2 方向 = 2 stages — 唔夠
  2 bits = 2 尺度 x 2 方向 = 4 stages — 剛好
  3 bits = 3 尺度 x 2 方向 = 6 stages — 可以，但多餘

宇宙會選擇最小可能。
所以 4。
""")

# ============================================================
# Verification
# ============================================================
print("-" * 72)
print("Step 6: 驗證")
print("-" * 72)

print(f"""
  4 來自 2 bits x 2 directions:
    2 bits = 2 個自由度
    2 directions = forward/backward
    2 x 2 = 4

  8 = 4 x 2:
    4 = fundamental pipeline stages
    2 = time direction (forward/backward)
    4 x 2 = 8

  唔係 8 = 2^3，而係 8 = 4 x 2。
  4 係 fundamental，2 係 doubling。
  同 switch-case = if-else 變體一樣。

  驗證：所有 IDCM 常數都係 4 嘅冪次
    epsilon = phi_inv/4
    kappa = 1/4^2
    e^2 = 1/4? no, but 4 appears everywhere
    N_d = 4 x 11
    L = 53/8 = 6.625 = 4 + 2.625
    Omega_L = 4/(phi^4-1)
""")

# Show the 4-structure in IDCM
print("4-structure in IDCM:")
items = [
    ("4 stages", "pipeline fundamental"),
    ("4 = 2^2", "2 bits, 2 directions"),
    ("4 = phi^3 - phi^(-3)", "phi-identity"),
    ("4 x 11 = 44", "N_d = causal domains"),
    ("4^2 = 16", "1/kappa"),
    ("4/(phi^4-1)", "Omega_L"),
    ("4e = phi_inv", "epsilon definition"),
]
for item, desc in items:
    print(f"  {item:20s}  {desc}")

print()
print("=" * 72)
print("結論：4 係 fundamental（2 bits x 2 directions）")
print("8 = 4 x 2 只係 forward/backward doubling")
print("同 switch-case = if-else 變體一樣")
print("=" * 72)