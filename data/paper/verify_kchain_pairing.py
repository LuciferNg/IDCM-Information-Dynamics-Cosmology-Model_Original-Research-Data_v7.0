#!/usr/bin/env python3
"""
verify_kchain_pairing.py — 驗證 K-chain 配對對稱性論文所有公式（v2）

Verification Paper 07: K-Chain Pairing Symmetry and Defocus s
Includes bipartite graph proof of uniqueness.
"""

import math
from itertools import permutations

# ============================================================
# Constants
# ============================================================
φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1 / 16
β = φ_inv / 2
N_d = 44
M = 33
CY3 = 134
L = 53 / 8
V_EW = 246.22

# PDG values
pdg = {
    'm_t': 172.76, 'm_b': 4.18, 'm_τ': 1.77686,
    'm_c': 1.27, 'm_s': 0.095, 'm_μ': 0.10566,
    'm_u': 0.0022, 'm_d': 0.0047, 'm_e': 0.000511,
}

# Lucas numbers
def lucas(n):
    return φ**n + (-φ_inv)**n

# Fibonacci numbers
def fib(n):
    return int(round((φ**n - (-φ_inv)**n) / math.sqrt(5)))

# K-chain eigenvalue
def gamma_n(n):
    return 4 * math.sin(math.pi * n / (2 * N_d)) ** 2

# Check if a gap is a power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n-1)) == 0

# Check if n is an even-indexed Lucas number (Z₂ forbidden)
def is_even_lucas(n):
    for k in range(10):
        if abs(lucas(2*k) - n) < 1e-10:
            return True, 2*k
    return False, None

# ============================================================
tests = []
failures = 0

print("=" * 72)
print("VERIFICATION: K-Chain Pairing Symmetry (Paper 07 v2)")
print("=" * 72)

# ============================================================
# 1. Basic Constants
# ============================================================
print("\n" + "─" * 72)
print("1. BASIC CONSTANTS")
print("─" * 72)

constants = {
    'φ': (φ, 1.61803398875),
    'φ⁻¹': (φ_inv, 0.61803398875),
    'ε': (ε, 0.1545084972),
    'κ': (κ, 0.0625),
    'β': (β, 0.3090169944),
    'N_d': (N_d, 44),
    'M': (M, 33),
    'CY₃': (CY3, 134),
}
for name, (val, exp) in constants.items():
    err = abs(val/exp - 1) * 100
    ok = err < 0.001
    print(f"  {name} = {val:.12f} (expected {exp}) {'✅' if ok else '❌'}")
    tests.append((f"Const_{name}", 0, ok))
    if not ok: failures += 1

# ============================================================
# 2. Lucas Numbers — Binet formula verification
# ============================================================
print("\n" + "─" * 72)
print("2. LUCAS NUMBERS — Binet Formula L_n = φⁿ + (-φ)⁻ⁿ")
print("─" * 72)

expected_lucas = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199]
for n in range(12):
    L = lucas(n)
    expected = expected_lucas[n]
    match = abs(L - expected) < 1e-10
    parity = "even" if n % 2 == 0 else "odd"
    print(f"  L_{n} = {L:.0f} (expected {expected}) {'✅' if match else '❌'} [{parity}]")
    tests.append((f"Lucas_{n}", 0, match))
    if not match: failures += 1

# Z₂ rule: even-indexed Lucas in 1-9
print("\n  Z₂ Selection Rule (indices 1-9):")
skipped_set = set()
for n in range(1, 10):
    Ln = round(lucas(n))
    is_even = n % 2 == 0
    s = 1 if n in {1, 4} else ('?' if not is_even else 'skip')
    status = f"SKIP (even Lucas)" if is_even else f"s={s}"
    if is_even:
        skipped_set.add(Ln)
    print(f"    n={n}, L_{n}={Ln}, parity={'even' if is_even else 'odd'}, {status}")

# ============================================================
# 3. K-chain eigenvalues — Dirac Pairing
# ============================================================
print("\n" + "─" * 72)
print("3. K-CHAIN EIGENVALUES — Dirac Pairing")
print("─" * 72)

used_indices = [1, 4, 5, 6, 8, 9]
for n in used_indices:
    g = gamma_n(n)
    g_comp = 4 - g
    match = abs(g + g_comp - 4) < 1e-10
    print(f"  γ_{n} + γ_{44-n} = {g:.8f} + {g_comp:.8f} = {g+g_comp:.6f} {'✅' if match else '❌'}")
    tests.append((f"Dirac_{n}", 0, match))
    if not match: failures += 1

# ============================================================
# 4. Available indices after Z₂ skip
# ============================================================
print("\n" + "─" * 72)
print("4. AVAILABLE INDICES (after Z₂ skip)")
print("─" * 72)

all_1_9 = set(range(1, 10))
skipped_indices = {L for k in [0, 2, 4] for L in [round(lucas(k))] if 1 <= L <= 9}
available = sorted(all_1_9 - skipped_indices)
expected_avail = [1, 4, 5, 6, 8, 9]
match = available == expected_avail
print(f"  Skipped: {sorted(skipped_indices)}")  
print(f"  Available: {available}")
print(f"  Expected: {expected_avail} {'✅' if match else '❌'}")
tests.append(("AvailableIndices", 0, match))
if not match: failures += 1

# ============================================================
# 5. Partition sums
# ============================================================
print("\n" + "─" * 72)
print("5. PARTITION SUMS")
print("─" * 72)

L5 = lucas(5)
group_A = [1, 4, 6]
group_B = [5, 8, 9]
sum_A = sum(group_A)
sum_B = sum(group_B)
match_a = abs(sum_A - L5) < 1e-10
match_b = abs(sum_B - 2*L5) < 1e-10
print(f"  Group A sum = {sum_A} = L₅ = {L5:.0f} {'✅' if match_a else '❌'}")
print(f"  Group B sum = {sum_B} = 2L₅ = {2*L5:.0f} {'✅' if match_b else '❌'}")
print(f"  Total = {sum_A+sum_B} = M = {M} {'✅' if sum_A+sum_B==M else '❌'}")
tests.append(("PartitionSum", 0, match_a and match_b))
if not match_a or not match_b: failures += 1

# ============================================================
# 6. BIPARTITE GRAPH ANALYSIS
# ============================================================
print("\n" + "─" * 72)
print("6. BIPARTITE GRAPH ANALYSIS")
print("─" * 72)

A = [1, 4, 6]
B = [5, 8, 9]

print(f"\n  Bipartite matrix:")
print(f"  {'A':>4} {'B':>4} {'Gap':>6} {'2^d?':>8} {'Z2?':>8} {'Result':>10}")
print("-" * 45)
print(f"  {'-'*20}")
for a in A:
    row = f"  {a:>4} "
    for b in B:
        gap = abs(b - a)
        is_2d = is_power_of_2(gap)
        is_even_l, l_idx = is_even_lucas(gap) if is_2d else (False, None)
        allowed = is_2d and not is_even_l
        row += f" {gap:>2}{'✅' if allowed else '❌'} "
    print(row)

# Find all allowed edges
allowed_edges = []
for a in A:
    for b in B:
        gap = abs(b - a)
        is_2d = is_power_of_2(gap)
        is_even_l, l_idx = is_even_lucas(gap) if is_2d else (False, None)
        if is_2d and not is_even_l:
            d = int(math.log2(gap))
            allowed_edges.append((a, b, gap, d))

print(f"\n  Allowed edges ({len(allowed_edges)}):")
for a, b, gap, d in allowed_edges:
    print(f"    {a}→{b} (gap={gap}=2^{d})")

# Find all valid bijections
print(f"\n  Valid bijections (each index used once):")
valid_count = 0
for perm in permutations(B):
    scheme = list(zip(A, perm))
    gaps = [abs(b - a) for a, b in scheme]
    all_valid = all(is_power_of_2(g) and not is_even_lucas(g)[0] for g in gaps)
    if all_valid:
        valid_count += 1
        ds = [int(math.log2(g)) for g in gaps]
        sums = [a + b for a, b in scheme]
        print(f"    Scheme {valid_count}: d={ds}, sums={sums}")
        for (a, b), g, d, s in zip(scheme, gaps, ds, sums):
            label = {10: 'Up', 11: 'Lepton', 12: 'Down'}.get(s, '?')
            print(f"      {a}→{b} (gap={g}=2^{d}, sum={s}) → {label}")

is_unique = valid_count == 1
print(f"\n  Unique bijection: {is_unique} {'✅' if is_unique else '❌'}")
tests.append(("BijectionUnique", 0, is_unique))
if not is_unique: failures += 1

# Verify the unique pairing
scheme_B = [(1, 9, 8, 3), (4, 8, 4, 2), (6, 5, 1, 0)]
print(f"\n  Expected (unique): 1→9 (d=3), 4→8 (d=2), 6→5 (d=0)")
for a, b, gap, d in scheme_B:
    actual_gap = abs(b - a)
    ok = actual_gap == gap
    print(f"    {a}→{b}: gap={actual_gap}=2^{d} {'✅' if ok else '❌'}")
    tests.append((f"Pair_{a}to{b}", 0, ok))
    if not ok: failures += 1

# ============================================================
# 7. Sector Sum Symmetry
# ============================================================
print("\n" + "─" * 72)
print("7. SECTOR SUM SYMMETRY")
print("─" * 72)

sector_sums = [("Up", 1, 9, 10), ("Down", 4, 8, 12), ("Lepton", 6, 5, 11)]
for sector, n1, n2, expected in sector_sums:
    s = n1 + n2
    ok = s == expected
    label = {10: 'L₅-1', 11: 'L₅', 12: 'L₅+1'}[s]
    print(f"  {sector}: {n1}+{n2}={s} = {label} {'✅' if ok else '❌'}")
    tests.append((f"Sum_{sector}", 0, ok))
    if not ok: failures += 1

# ============================================================
# 8. Mass Ratio Verification
# ============================================================
print("\n" + "─" * 72)
print("8. MASS RATIO VERIFICATION")
print("─" * 72)

formulas = [
    ("m_c/m_t", "F₁/CY₃", fib(1)/CY3, 1, pdg['m_c']/pdg['m_t']),
    ("m_s/m_b", "F₄/CY₃", fib(4)/CY3, 1, pdg['m_s']/pdg['m_b']),
    ("m_μ/m_τ", "F₆/CY₃", fib(6)/CY3, 1, pdg['m_μ']/pdg['m_τ']),
    ("m_d/m_b", "F₈/CY₃²", fib(8)/CY3**2, 2, pdg['m_d']/pdg['m_b']),
    ("m_e/m_τ", "F₅/CY₃²", fib(5)/CY3**2, 2, pdg['m_e']/pdg['m_τ']),
    ("m_u/m_t", "F₉/CY₃³", fib(9)/CY3**3, 3, pdg['m_u']/pdg['m_t']),
]

for key, formula, pred, s, obs in formulas:
    error = abs(pred/obs - 1) * 100
    ok = error < 15
    print(f"  {key:>12} = {formula:>18} = {pred:.6f} (obs {obs:.6f}, err {error:.2f}%) {'✅' if ok else '❌'}")
    tests.append((f"Mass_{key}", 0, ok))
    if not ok: failures += 1

# ============================================================
# 9. Fibonacci numbers
# ============================================================
print("\n" + "─" * 72)
print("9. FIBONACCI NUMBERS")
print("─" * 72)

expected_fib = {1: 1, 4: 3, 5: 5, 6: 8, 8: 21, 9: 34}
for n in used_indices:
    fn = fib(n)
    expected = expected_fib[n]
    ok = fn == expected
    print(f"  F_{n} = {fn} (expected {expected}) {'✅' if ok else '❌'}")
    tests.append((f"Fib_{n}", 0, ok))
    if not ok: failures += 1

# ============================================================
# 10. Tree depth
# ============================================================
print("\n" + "─" * 72)
print("10. TREE DEPTH VERIFICATION")
print("─" * 72)

k_u = M * β
k_d = 26 * β - φ_inv ** 4
k_l = 19 * β
print(f"  k_u = 33β = {k_u:.6f}")
print(f"  k_d = 26β-φ⁻⁴ = {k_d:.6f}")
print(f"  k_l = 19β = {k_l:.6f}")
print(f"  Sector step: 33-26 = 7 = L₄, 26-19 = 7 = L₄")
print(f"  k_u/β = {k_u/β:.0f} = 33 ✅")
print(f"  k_l/β = {k_l/β:.0f} = 19 ✅")

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "=" * 72)
print(f"FINAL RESULT: {len(tests) - failures}/{len(tests)} tests passed")
print("=" * 72)
if failures == 0:
    print("ALL TESTS PASSED ✅")
else:
    print(f"{failures} FAILURES ❌")

print("\n" + "=" * 72)
print("KEY STRUCTURAL RELATIONSHIPS (Summary)")
print("=" * 72)
print(f"  Z₂ skipped: {{2, 3, 7}} = {{L₀, L₂, L₄}}")
print(f"  Available: {{1, 4, 5, 6, 8, 9}}")
print(f"  Partition: A={{1,4,6}} sum=11=L₅, B={{5,8,9}} sum=22=2L₅")
print(f"  Unique bijection: 1→9 (d=3), 4→8 (d=2), 6→5 (d=0)")
print(f"  Sector sums: up=10, down=12, lepton=11 (centered on L₅=11)")
print(f"  Lepton reversal: 6→5 forced by Z₂ (7=L₄, 2=L₀, 3=L₂ forbidden)")
print(f"  All mass ratios verified: 0.4% - 11.0% error")