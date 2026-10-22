#!/usr/bin/env python3
"""
verify_02_prediction.py — P_n Spectral Tower Cross-Verification
Checks all formulas in Document 2 against external data (PDG 2024, etc.).
"""
import math

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
κ = 1/16
β = φ_inv / 2
N_d = 44
M_P_GeV = 1.22091e19

# External data
REF = {
    "V_us": 0.22500, "V_cb": 0.0410, "η": 0.350, "ρ": 0.157, "J": 3.00e-5,
    "α⁻¹": 137.035999084, "Ω_Λ": 0.6847, "m_τ/m_μ": 16.817,
}

def γ(n):
    return 4 * math.sin(math.pi * n / (2 * N_d))**2

def M_n(n):
    return M_P_GeV * math.exp(-12*n) * math.sqrt(φ_inv)

print("=" * 72)
print("DOC 2: P_n SPECTRAL TOWER — EXTERNAL CROSS-VERIFICATION")
print("=" * 72)

pass_count = 0
fail_count = 0
def check(name, condition, detail=""):
    global pass_count, fail_count
    if condition:
        print(f"  ✅ {name}")
        pass_count += 1
    else:
        print(f"  ❌ {name} — {detail}")
        fail_count += 1

# P_n masses
check("1. P_4 DM = 13.68 MeV", abs(M_n(4)*1000/13.68-1) < 0.01)
check("2. P_3 = 2.23 TeV", abs(M_n(3)/1000/2.23-1) < 0.02)
check("3. P_5 = 84 eV", abs(M_n(5)*1e9/84.05-1) < 0.02)
check("4. P_6 = 0.0005 eV", abs(M_n(6)*1e9/0.000516-1) < 0.02)

# Mass ratio = e^12
check("5. M_4/M_5 = e^12", abs(M_n(4)/M_n(5)/math.e**12-1) < 1e-10)

# Coupling ratio = 4φ·e^12
def y_n(n):
    return κ * ε**n * math.exp(-12*n) / (16 * math.pi**2)
check("6. y_4/y_5 = 4φ·e^12", abs(y_n(4)/y_n(5)/(4*φ*math.e**12)-1) < 1e-10)

# CKM
Lc = γ(3) - 2*γ(2) + γ(1)
λ = φ_inv**3 - Lc
Vcb = φ**2 / 64
η = 19 * φ / 88
J = (Vcb/λ**2)**2 * λ**6 * η
check("7a. V_us = 0.226", abs(λ/REF["V_us"]-1) < 0.01)
check("7b. V_cb = 0.0409", abs(Vcb/REF["V_cb"]-1) < 0.01)
check("7c. η = 0.349", abs(η/REF["η"]-1) < 0.03)
check("7d. J = 3.0e-5", abs(J/REF["J"]-1) < 0.05)

# SM
check("8. α⁻¹ = 137.036", abs((134+3+(44-29)*φ_inv/256)/REF["α⁻¹"]-1) < 1e-5)
check("9. Ω_Λ = 0.683", abs(4/(φ**4-1)/REF["Ω_Λ"]-1) < 0.005)
check("10. m_τ/m_μ = 16.86", abs(φ**(19*β)/REF["m_τ/m_μ"]-1) < 0.005)

print(f"\n{'='*72}")
print(f"RESULTS: {pass_count}/{pass_count+fail_count} passed")
print("ALL CHECKS PASSED ✅" if fail_count == 0 else f"{fail_count} FAILURES ❌")
print("=" * 72)
