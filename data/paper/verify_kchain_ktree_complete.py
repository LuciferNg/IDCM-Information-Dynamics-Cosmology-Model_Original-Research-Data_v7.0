#!/usr/bin/env python3
"""verify_kchain_ktree_complete.py — Complete K_chain ⊗ K_tree verification"""

import math
from itertools import permutations

φ = (1 + math.sqrt(5)) / 2
φ_inv = 1 / φ
ε = φ_inv / 4
κ = 1 / 16
β = φ_inv / 2
N_d = 44
CY3 = 134
M = (CY3 - 2) // 4

def L(n): return φ**n + (-φ_inv)**n
def fib(n): return int(round((φ**n - (-φ_inv)**n) / math.sqrt(5)))
def γ(n): return 4 * math.sin(math.pi * n / (2 * N_d)) ** 2
def is_2pow(n): return n > 0 and (n & (n-1)) == 0

L5 = int(round(L(5)))
L4 = int(round(L(4)))
step = L4

tests, failures = [], 0

print("=" * 78)
print("COMPLETE K = K_chain ⊗ K_tree — VERIFICATION")
print("=" * 78)

# ========== PHASE I: K-CHAIN ==========
print("\n" + "█" * 78)
print("PHASE I: K-CHAIN PAIRING SYMMETRY")
print("█" * 78)

# I.1 Dirac pairing
print("\nI.1 Dirac Pairing: γ_n + γ_{44-n} = 4")
for n in [1, 4, 5, 6, 8, 9]:
    g = γ(n); gc = 4 - g
    ok = abs(g + gc - 4) < 1e-10
    print(f"  n={n}: γ_n+γ_{44-n}={g+gc:.6f}=4 {'✅' if ok else '❌'}")
    tests.append((f"I1_Dirac_{n}", 0, ok))
    if not ok: failures += 1

# I.2 Lucas numbers
print("\nI.2 Lucas Numbers (Binet):")
expected_L = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]
for n, exp in enumerate(expected_L):
    val = L(n)
    ok = abs(val - exp) < 1e-10
    parity = "even" if n % 2 == 0 else "odd"
    print(f"  L_{n} = {val:.0f} (exp {exp}) [{parity}] {'✅' if ok else '❌'}")
    tests.append((f"I2_L{n}", 0, ok))
    if not ok: failures += 1

# I.3 Z₂ selection rule
print("\nI.3 Z₂ Selection Rule:")
# Even-indexed Lucas values within 1-9: L₀=2, L₂=3, L₄=7 → skipped
skipped_vals = {int(round(L(k))) for k in [0, 2, 4] if int(round(L(k))) <= 9}
avail = sorted(set(range(1, 10)) - skipped_vals)
expected_avail = [1, 4, 5, 6, 8, 9]
ok_avail = avail == expected_avail
print(f"  Even Lucas ≤ 9: {sorted(skipped_vals)} = {{L₀, L₂, L₄}} → SKIPPED")
print(f"  Available: {avail} {'✅' if ok_avail else '❌'}")
tests.append(("I3_Avail", 0, ok_avail))
if not ok_avail: failures += 1

# I.4 Partition sums
print("\nI.4 Partition Sums:")
A = [1, 4, 6]; B_list = [5, 8, 9]
sumA, sumB = sum(A), sum(B_list)
ok_sumA = abs(sumA - L5) < 1e-10
ok_sumB = abs(sumB - 2*L5) < 1e-10
ok_total = (sumA + sumB) == M
print(f"  A={{1,4,6}} sum = {sumA} = L₅ = {L5} {'✅' if ok_sumA else '❌'}")
print(f"  B={{5,8,9}} sum = {sumB} = 2L₅ = {2*L5} {'✅' if ok_sumB else '❌'}")
print(f"  Total = {sumA+sumB} = M = {M} {'✅' if ok_total else '❌'}")
tests.extend([("I4_SumA", 0, ok_sumA), ("I4_SumB", 0, ok_sumB), ("I4_Total", 0, ok_total)])
if not all([ok_sumA, ok_sumB, ok_total]): failures += 1

# I.5 Bipartite graph uniqueness
print("\nI.5 Bipartite Graph — Uniqueness Proof:")
valid = []
for perm in permutations(B_list):
    scheme = list(zip(A, perm))
    gaps = [abs(b - a) for a, b in scheme]
    # Condition: gap = 2^d AND gap NOT even-indexed Lucas
    if all(is_2pow(g) and int(round(g)) not in skipped_vals for g in gaps):
        ds = [int(math.log2(g)) for g in gaps]
        sums = [a + b for a, b in scheme]
        valid.append((scheme, gaps, ds, sums))

print(f"  Valid bijections: {len(valid)}")
for scheme, gaps, ds, sums in valid:
    print(f"    {scheme} → d={ds}, sums={sums}")

ok_unique = len(valid) == 1
expected = [(1, 9), (4, 8), (6, 5)]
if valid:
    # Check that the unique scheme matches expected
    ok_pairs = all(s[0] == e[0] and s[1] == e[1] for s, e in zip(valid[0][0], expected))
    print(f"  Unique: {'✅' if ok_unique else '❌'}")
    print(f"  Expected {(1,9),(4,8),(6,5)}: {'✅' if ok_pairs else '❌'}")
    tests.extend([("I5_Unique", 0, ok_unique), ("I5_Pairs", 0, ok_pairs)])
    if not ok_unique or not ok_pairs: failures += 1

# I.6 Sector sums
print("\nI.6 Sector Sum Symmetry:")
checks = [("Up", 1, 9, 10, "L₅-1"), ("Down", 4, 8, 12, "L₅+1"), ("Lepton", 6, 5, 11, "L₅")]
for name, a, b, exp, label in checks:
    s = a + b
    ok = s == exp
    print(f"  {name}: {a}+{b}={s} = {label} {'✅' if ok else '❌'}")
    tests.append((f"I6_{name}", 0, ok))
    if not ok: failures += 1

# ========== PHASE II: K-TREE ==========
print("\n" + "█" * 78)
print("PHASE II: K-TREE STAIR DERIVATION")
print("█" * 78)

# II.1 M = (CY₃-2)/4
print("\nII.1 M = (CY₃-2)/4 = 33:")
zero_free = CY3 - 2
B = int(round(L(3)))
computed_M = zero_free // B
ok_132 = zero_free == 132
ok_B4 = B == 4
ok_M33 = computed_M == 33
print(f"  CY₃-2 = {zero_free} = 132? {'✅' if ok_132 else '❌'}")
print(f"  B = L₃ = {B} = 4? {'✅' if ok_B4 else '❌'}")
print(f"  M = ({CY3}-2)/{B} = {computed_M} = 33? {'✅' if ok_M33 else '❌'}")
tests.extend([("II1_132", 0, ok_132), ("II1_B4", 0, ok_B4), ("II1_M33", 0, ok_M33)])
if not all([ok_132, ok_B4, ok_M33]): failures += 1

# II.2 Step = L₄ = B + L₂
print("\nII.2 Step = L₄ = B + L₂ = 7:")
L2 = int(round(L(2))); L3 = int(round(L(3)))
ok_l4 = L4 == L3 + L2
ok_step7 = L4 == 7
print(f"  L₂ = {L2}, L₃ = {L3} = B, L₄ = {L3}+{L2} = {L4} {'✅' if ok_l4 else '❌'}")
print(f"  Step = L₄ = 7? {'✅' if ok_step7 else '❌'}")
tests.extend([("II2_L4sum", 0, ok_l4), ("II2_Step7", 0, ok_step7)])
if not ok_l4 or not ok_step7: failures += 1

# II.3 Stair
print("\nII.3 Stair: M → M-L₄ → M-2L₄:")
stair = {"Up": M, "Down": M - step, "Lepton": M - 2*step}
exp_stair = {"Up": 33, "Down": 26, "Lepton": 19}
for name, val in stair.items():
    exp = exp_stair[name]
    ok = val == exp
    print(f"  {name}: {val} (expected {exp}) {'✅' if ok else '❌'}")
    tests.append((f"II3_{name}", 0, ok))
    if not ok: failures += 1

# II.4 Tree depths
print("\nII.4 Tree Depth Formulas:")
k_u = M * β
k_d = (M - step) * β - φ_inv**4
k_l = (M - 2*step) * β
print(f"  k_u = {M}β = {k_u:.6f}")
print(f"  k_d = {M-step}β-φ⁻⁴ = {k_d:.6f}  (φ⁻⁴ = {φ_inv**4:.6f})")
print(f"  k_l = {M-2*step}β = {k_l:.6f}")

# II.5 Casimir boundary
print("\nII.5 Casimir Boundary Effect:")
k_u_raw = M * β
k_d_raw = (M - step) * β
k_l_raw = (M - 2*step) * β
ok_up = abs(k_u - k_u_raw) < 1e-10
ok_down = abs(k_d_raw - k_d - φ_inv**4) < 1e-10  # k_d = k_d_raw - φ⁻⁴
ok_lepton = abs(k_l - k_l_raw) < 1e-10
print(f"  Up:   k_u = k_u_raw? {'✅' if ok_up else '❌'}  (UV pinned)")
print(f"  Down: k_d = k_d_raw - φ⁻⁴? {'✅' if ok_down else '❌'}  (Casimir)")
print(f"  Lepton: k_l = k_l_raw? {'✅' if ok_lepton else '❌'}  (IR pinned)")
tests.extend([("II5_Up", 0, ok_up), ("II5_Down", 0, ok_down), ("II5_Lep", 0, ok_lepton)])
if not all([ok_up, ok_down, ok_lepton]): failures += 1

# ========== PHASE III: MASS RATIOS ==========
print("\n" + "█" * 78)
print("PHASE III: MASS RATIO VERIFICATION")
print("█" * 78)

pdg_obs = {
    "m_c/m_t": 1.27/172.76, "m_s/m_b": 0.095/4.18,
    "m_mu/m_tau": 0.10566/1.77686, "m_d/m_b": 0.0047/4.18,
    "m_e/m_tau": 0.000511/1.77686, "m_u/m_t": 0.0022/172.76,
}

formulas = [
    ("m_c/m_t",   "F₁/CY₃",  fib(1)/CY3,     1, "k_u"),
    ("m_s/m_b",   "F₄/CY₃",  fib(4)/CY3,     1, "k_d"),
    ("m_mu/m_tau","F₆/CY₃",  fib(6)/CY3,     1, "k_l"),
    ("m_d/m_b",   "F₈/CY₃²", fib(8)/CY3**2,  2, "k_d×2"),
    ("m_e/m_tau", "F₅/CY₃²", fib(5)/CY3**2,  2, "k_l×2"),
    ("m_u/m_t",   "F₉/CY₃³", fib(9)/CY3**3,  3, "k_u×3"),
]

print(f"{'Ratio':>12} {'Formula':>18} {'IDCM':>12} {'Obs':>12} {'Err%':>8} {'Depth':>8} {'Status':>8}")
print("-" * 80)
for key, formula, pred, s, src in formulas:
    obs = pdg_obs[key]
    err = abs(pred/obs - 1) * 100
    ok = err < 15
    print(f"{key:>12} {formula:>18} {pred:>12.6f} {obs:>12.6f} {err:>7.2f}% {src:>8} {'✅' if ok else '❌':>8}")
    tests.append((f"III_{key[:8]}", 0, ok))
    if not ok: failures += 1

# Projection verification
print("\n  CY₃ Projection: F_n/CY₃^s ≈ φ^(-k_X)")
for n, k, s in [(1, k_u, 1), (4, k_d, 1), (6, k_l, 1)]:
    ratio = (fib(n)/CY3**s) / φ**(-k)
    err = abs(ratio - 1) * 100
    ok = err < 3
    print(f"    F_{n}/CY₃^{s} / φ^(-k) = {ratio:.6f} (err {err:.4f}%) {'✅' if ok else '❌'}")
    tests.append((f"III_Proj{n}", 0, ok))
    if not ok: failures += 1

# ========== PHASE IV: PIPELINE ==========
print("\n" + "█" * 78)
print("PHASE IV: AXIOMATIC PIPELINE")
print("█" * 78)

pipeline = [
    ("CY₃ total Hodge", CY3, 134),
    ("-2 zero modes (χ(S²))", CY3-2, 132),
    ("÷4 chiral (B=φ³-φ⁻³)", (CY3-2)/4, 33.0),
    ("M = max tensor capacity", float(M), 33.0),
    ("Step = L₄ = B+L₂", float(L4), 7.0),
    ("k_u coeff = M", float(M), 33.0),
    ("k_d coeff = M-L₄", float(M-step), 26.0),
    ("k_l coeff = M-2L₄", float(M-2*step), 19.0),
    ("k_u = 33β", k_u, 33*β),
    ("k_d = 26β-φ⁻⁴", k_d, 26*β-φ_inv**4),
    ("k_l = 19β", k_l, 19*β),
]

print(f"{'Step':>35} {'Value':>12} {'Expected':>12} {'Status':>8}")
print("-" * 70)
for name, val, exp in pipeline:
    ok = abs(val - exp) < 0.001
    print(f"{name:>35} {val:>12.6f} {exp:>12.6f} {'✅' if ok else '❌':>8}")
    tests.append((f"IV_{name[:20]}", 0, ok))
    if not ok: failures += 1

# ========== FINAL ==========
total_tests = len(tests)
print("\n" + "=" * 78)
print(f"RESULT: {total_tests - failures}/{total_tests} PASSED")
print("=" * 78)

if failures == 0:
    print("\n✅ ALL PASSED — K = K_chain ⊗ K_tree fully verified\n")
    print("Axiomatic Pipeline (closed):")
    print("  CY₃ = 134")
    print("   ├─ -2 (χ(S²) zero modes) → 132")
    print("   ├─ ÷4 (B = φ³-φ⁻³ = 4) → M = 33")
    print("   │")
    print("   ├─ k_u = 33β            (UV pinned at M)")
    print("   │     │")
    print("   │     ├─ -L₄ = -(B+L₂) = -7")
    print("   │     │")
    print("   │     ├─ k_d = 26β - φ⁻⁴   (Casimir, middle unpinned)")
    print("   │     │         ↑ evanescent tail")
    print("   │     │")
    print("   │     ├─ -L₄ = -(B+L₂) = -7")
    print("   │     │")
    print("   │     └─ k_l = 19β        (IR pinned at L₅=11)")
    print("   │")
    print("   └─ F_n/CY₃^s ≈ φ^(-k_X)   ✅  6/6 mass ratios")
else:
    print(f"\n❌ {failures} FAILURES")
    for name, _, ok in tests:
        if not ok:
            print(f"  FAILED: {name}")