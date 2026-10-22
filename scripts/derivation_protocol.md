# Structural Equation Derivation Protocol

## Purpose
Ensure that every IDCM equation is derived from first principles (x²+x-1=0 → φ → ε,κ,β → W-field structure), NOT from post-hoc numerical fitting. A formula that merely "looks good" or "matches data" is NOT accepted — it must be **necessary** and **unique**.

## Core Principles

### 1. Uniqueness
The formula must be the **only possible expression** given the structural constraints. If alternative φ-powers would give similar precision, the formula is not unique.

**Test:** Can you replace φ^n with φ^{n±1} and still get a match? If yes, the formula is not unique.

### 2. Necessity
Each term must be **forced by the structure**, not chosen for aesthetic fit. The coefficients must come from the recursion, not from tuning.

**Test:** Can you change a coefficient by ±1 and still match? If yes, the coefficient is not structural.

### 3. Cross-Validation
The formula must be **consistent with other derived formulas**. If one formula uses φ¹¹ and another uses φ⁶, there must be a structural reason connecting them.

**Test:** Does the formula share its power indices with other structural numbers (N_h, N_d, CY₃ Hodge numbers)?

### 4. No Free Parameters
Every coefficient and exponent must be traced back to the recursion constants (φ, ε, κ, β). No tuning of coefficients to match data.

**Test:** Count the number of free parameters. If > 0, it's not derived.

### 5. Traceability
The derivation must be a **chain of steps** from the recursion to the formula, with no gaps.

**Test:** Can you write the derivation as a sequence of "Step A → Step B → Step C → Formula"? If any step is missing, it's not derived.

## Identification Protocol

### Green (✅ DERIVED)
- Follows from the recursion via a traceable chain
- All coefficients are integers or κ, ε, β
- Unique: no alternative φ-powers would work
- Cross-validated with other structural numbers

### Yellow (🟡 CANDIDATE)
- Clean pattern with plausible structural interpretation
- Coefficients are small integers or ±1
- But the derivation chain is incomplete
- Needs further work to become GREEN

### Red (⚠️ FITTED)
- Post-hoc matching of numerical data
- Coefficients tuned to match observation
- Alternative φ-powers would give similar precision
- Not accepted as a structural formula

## Verification Script Template

Every structural formula MUST have a verification script that:

```python
# 1. Derive from recursion only (no observational input)
phi = (1 + sqrt(5)) / 2
eps = 1/(4*phi)
kappa = 1/16

# 2. Compute the formula
prediction = <formula from structural derivation>
observed = <independent measurement>

# 3. Check uniqueness
# Try φ^{n±1} and show they fail
# Try coefficient ±1 and show they fail

# 4. Cross-validate
# Check consistency with N_h, N_d, CY₃ numbers

# 5. Report
error = abs(prediction - observed) / observed * 100
status = "✅ DERIVED" if derivation_chain_complete else "🟡 CANDIDATE"
```

## Current Status Registry

| Formula | Status | Reason |
|:--------|:-------|:-------|
| D_H/L_P | ✅ DERIVED | 44×(6+10κ) + ε²-ε³-ε⁴, traceable chain |
| M_P | ✅ DERIVED | 17φ+φ⁻⁵-ε³-φ⁻²/256, pure φ-exponent |
| m_μ/m_e | 🟡 CANDIDATE | Clean but no derivation for φ¹¹ |
| m_τ/m_μ | ⚠️ FITTED | ε combination is post-hoc |
| α⁻¹ | ⚠️ FITTED | 137 structural, 15/256 tuned |
| Ω_Λ | ⚠️ FITTED | φ⁻²/4 coupling is post-hoc |
| k_B | ✅ DERIVED | Definitional identity |
| Quantum entanglement | ✅ DERIVED | W-field continuity mechanism |
| QG corrections | ✅ DERIVED | MUP κ²=1/256 |

## Rule for Future Work

**BEFORE** writing any new structural equation, ask:

1. "Can I trace this from the recursion?"
2. "Is this the ONLY possible expression?"
3. "Would changing φ^n to φ^{n±1} break it?"
4. "Are all coefficients forced by structure?"
5. "Does it cross-validate with other structural numbers?"

If the answer to ANY of these is "no", the formula is a CANDIDATE at best, not a closure.

## References

- Verification script: `/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/scripts/verify_derivations.py`
- Prologue: `/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/prologue_category_error.md`
- Epilogue: `/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/epilogue_end_of_fundamentalism.md`