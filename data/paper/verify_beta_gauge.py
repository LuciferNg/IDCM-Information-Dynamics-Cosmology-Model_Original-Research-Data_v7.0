#!/usr/bin/env python3
"""verify_beta_gauge.py — Verify SM β functions and gauge couplings"""

import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = 1/φ
ε = φ_inv / 4
κ = 1/16
N_d = 44
M = 33
B = 4
L2 = 3
L5 = 11
L7 = 29
F5 = 5
N_f = 3
CY3 = 134
M_Z = 91.188

tests, failures = [], 0

print("=" * 72)
print("SM β FUNCTIONS & GAUGE COUPLINGS — VERIFICATION")
print("=" * 72)

# 1. Fine-structure constant
print("\n" + "─" * 72)
print("1. FINE-STRUCTURE CONSTANT α⁻¹")
print("─" * 72)
alpha_inv = CY3 + L2 + (N_d - L7) * φ_inv / B**4
obs_alpha = 137.035999084
err = abs(alpha_inv/obs_alpha - 1) * 100
ok = err < 0.01
print(f"  α⁻¹ = {alpha_inv:.6f} (obs {obs_alpha:.6f}, err {err:.6f}%) {'✅' if ok else '❌'}")
tests.append(("AlphaInv", 0, ok))
if not ok: failures += 1

# 2. GUT coupling
print("\n" + "─" * 72)
print("2. GUT SCALE COUPLING")
print("─" * 72)
alpha_GUT = ε / 4
alpha_GUT_inv = 4 / ε
print(f"  alpha_GUT = eps/4 = {alpha_GUT:.6f}")
print(f"  alpha_GUT^-1 = 4/eps = {alpha_GUT_inv:.6f} = 16*phi = {16*φ:.6f}")
sin2_GUT = κ / ε
print(f"  sin^2_theta_W(GUT) = kappa/eps = {sin2_GUT:.6f} = phi/4 = {φ/4:.6f}")

# 3. 1-loop b_i
print("\n" + "─" * 72)
print("3. 1-LOOP β COEFFICIENTS")
print("─" * 72)
b3 = -N_d/4 + B
b2 = -N_d/6 + B + 1/(2*L2)
b1 = (N_d - L2) / (2*F5)
for name, val, sm in [("b_3", b3, -7), ("b_2", b2, -19/6), ("b_1", b1, 41/10)]:
    ok = abs(val - sm) < 0.001
    print(f"  {name} = {val:.4f} (SM {sm:.4f}) {'✅' if ok else '❌'}")
    tests.append((name, 0, ok))
    if not ok: failures += 1

# 4. 2-loop b_ij
print("\n" + "─" * 72)
print("4. 2-LOOP β COEFFICIENTS")
print("─" * 72)
b33 = N_d/2 + B
b22 = N_d/8 + N_f/9
b11_raw = N_d/4 + 1/18
b11_sm = 9/25 * b11_raw
for name, val, sm in [("b_33", b33, 26), ("b_22", b22, 35/6), ("b_11", b11_sm, 199/50)]:
    ok = abs(val - sm) < 0.001
    print(f"  {name} = {val:.4f} (SM {sm:.4f}) {'✅' if ok else '❌'}")
    tests.append((name, 0, ok))
    if not ok: failures += 1

# 5. Weinberg angle at M_Z
print("\n" + "─" * 72)
print("5. WEINBERG ANGLE AT M_Z")
print("─" * 72)
L_GUT = M_Z * math.exp(M)
sin2_MZ = L5 / (N_d + L2) - ε**3/2
obs_sin2 = 0.23122
err_sin2 = abs(sin2_MZ/obs_sin2 - 1) * 100
ok_gut = abs(L_GUT/2e16 - 1) < 0.1
ok_sin2 = err_sin2 < 1
print(f"  Λ_GUT = M_Z × e^{M} = {L_GUT:.4e} GeV (expected ~2×10^16) {'✅' if ok_gut else '❌'}")
print(f"  sin²θ_W(M_Z) = {L5}/{N_d+L2} - ε³/2 = {sin2_MZ:.6f} (obs {obs_sin2:.6f}, err {err_sin2:.2f}%) {'✅' if ok_sin2 else '❌'}")
tests.append(("GUTscale", 0, ok_gut))
tests.append(("Sin2Mz", 0, ok_sin2))
if not ok_gut: failures += 1
if not ok_sin2: failures += 1

# 6. MERA β
print("\n" + "─" * 72)
print("6. MERA β FUNCTIONS")
print("─" * 72)
beta_MERA_g = -ε/2
beta_MERA_y = -math.log(φ)/(2*math.log(4))
print(f"  β_MERA(g) = -ε/2 = {beta_MERA_g:.6f}")
print(f"  β_MERA(y_f) = -lnφ/(2ln4) = {beta_MERA_y:.6f}")

# 7. MERA-SM matching
print("\n" + "─" * 72)
print("7. MERA-SM MATCHING AT GUT")
print("─" * 72)
g_sq = math.pi * ε
b_eff = -8 * math.pi
b33_val = N_d/2 + B
match_err = abs(abs(b_eff)/b33_val - 1) * 100
ok_match = match_err < 5
print(f"  g_GUT² = πε = {g_sq:.6f}")
print(f"  b_eff = -8π = {b_eff:.2f}")
print(f"  b_33 = {b33_val:.0f}, |b_eff|/b_33 = {abs(b_eff)/b33_val:.4f}, diff {match_err:.2f}% {'✅' if ok_match else '❌'}")
tests.append(("MERA_SM_match", 0, ok_match))
if not ok_match: failures += 1

# Final
print("\n" + "=" * 72)
print(f"RESULT: {len(tests) - failures}/{len(tests)} PASSED")
print("=" * 72)
if failures == 0:
    print("ALL PASSED ✅ — SM β functions and gauge couplings verified")
else:
    print(f"{failures} FAILURES ❌")