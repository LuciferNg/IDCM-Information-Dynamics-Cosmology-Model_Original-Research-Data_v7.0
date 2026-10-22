#!/usr/bin/env python3
"""
derive_2_plus_1.py — 推導 2+1 bit 結構，重新理解 4 的來源
"""
import math

phi = (1 + math.sqrt(5)) / 2
phi_inv = phi - 1

print("=" * 72)
print("推導：2+1 bit — 重新理解 4 的來源")
print("=" * 72)

# ============================================================
# The minimal operation
# ============================================================
print("\n" + "-" * 72)
print("Step 1: 最小操作需要幾多 bit？")
print("-" * 72)

print("""
NOT 係唯一非平凡 1-bit 操作：
  NOT(0)=1, NOT(1)=0

要實現 NOT，需要：
  1 bit data (要 flip 嘅值)
  + 1 bit control (要唔要 flip)
  = 2 bit

但 2 bit 只做到 1-bit 操作，做唔到 hierarchy。
要建立 hierarchy（區分不同尺度），最少需要 2 data bits。
""")

print("""
2 data bits 的最小操作：
  2 bits data (值 a, 值 b)
  + 1 bit control (要唔要 NOT)
  = 3 bit

但 control bit 本身都係 bit——control bit 都可以被 NOT。
所以要完整描述一個操作，需要：
  2 data bits (輸入)
  + 1 control bit (操作選擇)
  + 1 output bit (結果儲存)
  = 4 bit

所以 4 係「最小 closure」：
  2 data + 1 control + 1 output = 4
  input -> process -> output -> store
  = 3 個階段 + 1 個儲存 = 4
""")

# ============================================================
# 3 嘅角色
# ============================================================
print("-" * 72)
print("Step 2: 3 係實際操作，4 係 closure")
print("-" * 72)

print("""
2 data + 1 control = 3 (操作所需)
2 data + 1 control + 1 output = 4 (閉合所需)

3 係「操作維度」：
  2 data bits = 2 維空間
  1 control bit = 1 維時間
  2 + 1 = 3 維時空

4 係「閉合維度」：
  2 data + 1 control + 1 output
  2 + 1 + 1 = 4

所以：
  ε = φ⁻¹/4 係 closure 嘅空隙率
  但 3 世代嘅截斷係嚟自 2+1 嘅操作維度
""")

# Check: 3 in IDCM
print("3 在 IDCM 中的角色：")
items_3 = [
    ("3 generations", "fermion families"),
    ("3 = 2+1", "data + control"),
    ("3 = 4-1", "4 complement"),
    ("3^2 = 9", "L = 53/8 = (44+9)/8"),
    ("3 x 44 = 132", "close to 134 = h^11+h^21"),
]
for item, desc in items_3:
    print(f"  {item:20s}  {desc}")

print()

# ============================================================
# 4 的重新推導
# ============================================================
print("-" * 72)
print("Step 3: 4 的重新推導 — 2+1+1")
print("-" * 72)

print("""
唔係 fetch/decode/execute/writeback。
係：

  2 data bits (輸入)
  + 1 control bit (操作)
  + 1 output bit (結果)
  = 4

每個 bit 都係一個 pipeline stage：
  Stage 0: data bit 0 (輸入)
  Stage 1: data bit 1 (輸入)
  Stage 2: control bit (NOT 或唔 NOT)
  Stage 3: output bit (結果)

但 control bit 同 output bit 都係 bit——佢哋都可以被操作。
呢個就係 closure：
  任何操作都產生新 bit
  新 bit 可以再被操作
  所以系統必須閉合：input → process → output → store → input again
  呢個 cycle 就係 4
""")

# ============================================================
# 4 vs 3
# ============================================================
print("-" * 72)
print("Step 4: 4 vs 3 — 兩個 fundamental 數字")
print("-" * 72)

print("""
IDCM 有兩個 fundamental 數字：
  3 = 操作維度 (2 data + 1 control)
  4 = 閉合維度 (2 data + 1 control + 1 output)

3 出現的地方：
  三代費米子
  3 層 MERA 修正
  L = (44+9)/8, 9 = 3²
  h¹¹+h²¹ = 134, 134 = 3×44+2

4 出現的地方：
  ε = φ⁻¹/4
  κ = 1/4²
  N_d = 4×11
  Ω_Λ = 4/(φ⁴-1)
  4 stages

3 同 4 嘅關係：
  4 = 3 + 1 (output)
  4 = 2 + 2 (two pairs)
  4 = 2² (square of 2)
  但最根本：4 = 2+1+1 (data + control + output)
""")

# Show the 3 vs 4 structure
print("3 vs 4 結構：")
print()
print("  3 = 2 + 1")
print("      data + control")
print("      維度 + 時間")
print("      操作所需")
print()
print("  4 = 2 + 1 + 1")
print("      data + control + output")
print("      維度 + 時間 + 儲存")
print("      閉合所需")
print()

# ============================================================
# Verification
# ============================================================
print("-" * 72)
print("Step 5: 驗證")
print("-" * 72)

print(f"""
  3 的驗證：
    3 generations = 2+1
    3 MERA layers = 2 data + 1 control
    3 = 4-1 (closure minus one)

  4 的驗證：
    ε = φ⁻¹/4 = {phi_inv/4:.10f}
    κ = 1/16 = {1/16} = 1/(4²)
    N_d = 4×11 = {4*11}
    Ω_Λ = 4/(φ⁴-1) = {4/(phi**4-1):.10f}

  4 = 2+1+1:
    2 = data bits (輸入)
    1 = control bit (操作)
    1 = output bit (結果)
    = 4

  8 = 4×2:
    4 = fundamental closure
    2 = forward/backward time direction
    = 8 stages (implementation, not fundamental)
""")

print("=" * 72)
print("結論：4 係 fundamental 因為 2+1+1")
print("3 = 2+1 係操作維度")
print("4 = 2+1+1 係閉合維度")
print("=" * 72)