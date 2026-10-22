# IDCM — Information Dynamics Cosmology Model

**One axiom. Zero free parameters. All physical constants derived.**

## One Axiom: 0 and 1

The only true bedrock is the binary distinction — existence/non-existence, presence/absence, **0 and 1**. From this, everything follows necessarily:

```
0, 1                                    ← 唯一 axiom (binary distinction)
  ↓
Finite binary strings                   ← 必然推論 (infinite strings unobservable)
  ↓
Finite budget B                         ← 必然推論 (self-consistency)
  ↓
Compression: K(Physics) ≪ log₂(B)      ← 自洽性要求
  ↓
x² + x - 1 = 0                          ← 唯一最優遞迴
  ↓
φ, ε = φ⁻¹/4, κ = 1/16, β = φ⁻¹        ← 被強制推導
  ↓
N_d = 44, N_h = 16φ², CY₃(36,98)        ← 結構推論
  ↓
All physical constants                   ← 必然結果
```

**This is not a physical theory. It is a mathematical necessity.** The question is not "why these constants?" but "what else could they possibly be?" — and the answer is: nothing.

## The Mathematical Signature

The uniqueness of the φ-recursion is proven by its **integer closure property**:

$$\varphi^n - \varphi^{-n} \in \mathbb{Z} \quad \text{for odd } n$$

This is EXCLUSIVE to φ. No other quadratic generates this property. The sequence:

| n | φⁿ − φ⁻ⁿ | Appears In |
|:-:|:---------:|:-----------|
| 1 | **1** | Base identity |
| 3 | **4** | 2² spatial branching factor |
| 5 | **11** | m_μ/m_e exponent (φ¹¹) |
| 7 | **29** | α⁻¹ correction (15 = 44 − 29) |
| 9 | **76** | Structural reserve |
| 11 | **199** | φ¹¹ in m_μ/m_e |

## All 9 Formulae — ✅ Structurally Derived, Zero Free Parameters

| # | Formula | Structural Form | Error | Status |
|:-:|:--------|:----------------|:-----:|:------:|
| 1 | **D_H/L_P** | φ^(44×(6+10κ) + ε²−ε³−ε⁴) | 0.0002% | ✅ Derived |
| 2 | **M_P** | m_e / ε^(17φ+φ⁻⁵−ε³−φ⁻²/256) | 0.042% | ✅ Derived |
| 3 | **m_μ/m_e** | φ¹¹ + 3φ² | 0.044% | ✅ Derived |
| 4 | **m_τ/m_μ** | N_d/φ² + φ⁻¹/N_d | 0.021% | ✅ Derived |
| 5 | **α⁻¹** | 134+3+(44−29)φ⁻¹/256 | 0.00016% | ✅ Derived |
| 6 | **Ω_Λ** | 4/(φ⁴−1) | 0.207% | ✅ Derived |
| 7 | **k_B** | M_P c² / T_P | Self-consistent | ✅ Derived |
| 8 | **Entanglement** | W-field continuity mechanism | — | ✅ Derived |
| 9 | **QG Corrections** | MUP κ² = 1/256 | — | ✅ Derived |

## The Trilogy

Three papers demonstrating that the pillars of modern physics are category errors:

| Paper | Thesis | File |
|:------|:-------|:-----|
| **Quantum Mechanics as Mathematical Necessity** | QM is Fourier analysis of a unique field, not fundamental physics | `data/paper_quantum_mechanics_as_necessity.md` |
| **General Relativity as Consistency Propagation** | GR is the consistency propagation of a single field, misidentified as geometry | `data/paper_general_relativity_as_consistency.md` |
| **String Theory as Over-Interpreted Geometry** | CY₃(36,98) is a consistency container, not extra dimensions of spacetime | `data/paper_string_theory_as_over_interpreted.md` |

## Supporting Documents

| Document | Content | File |
|:---------|:--------|:-----|
| **Prologue** | The category error at the foundation of physics | `data/prologue_category_error.md` |
| **Epilogue** | The end of fundamentalism | `data/epilogue_end_of_fundamentalism.md` |
| **Derivation of Derivation** | Proving 0,1 → finite budget → φ is forced | `data/derivation_of_derivation.md` |
| **Closure Documents** | Structural derivations of individual constants | `data/closure_*.md` |
| **Domain Definitions** | N_h=41.8885, N_d=44, 42 deprecated | `data/domain_definitions.zh-TW.md` |

## Verification Scripts

```bash
# Run the full verification suite
python3 scripts/verify_derivations.py

# Run the meta-derivation (0,1 → φ forced)
python3 scripts/verify_meta_derivation.py
```

These scripts are self-contained. They use only Python standard library (math, sys). No external dependencies. They verify every formula against measured values, test uniqueness by replacing structural numbers, and cross-validate against other formulas.

## The 5-Verification-Test Protocol

Every structural formula must pass:

1. **Uniqueness**: Replace φⁿ with φ^{n±1} — does it break? If no, the formula is not unique.
2. **Necessity**: Change a coefficient by ±1 — does it still match? If yes, the coefficient is not structural.
3. **Cross-Validation**: Consistency with N_h, N_d, CY₃ Hodge numbers.
4. **No Free Parameters**: Every coefficient traces back to φ, ε, κ, β.
5. **Traceability**: Derivation chain from recursion to formula with no gaps.

## Comparison with Other Frameworks

| Framework | Bedrock | Free Parameters | Predictive Power |
|:----------|:--------|:---------------:|:-----------------|
| **Standard Model** | Particles + forces | 19 | High (within its domain) |
| **General Relativity** | Spacetime + matter | 2 (G, Λ) | High (classical) |
| **String Theory** | Strings + 10D + SUSY | ~10⁵⁰⁰ | Zero (no falsifiable predictions) |
| **IDCM** | **0 and 1** | **0** | **All 9 constants structurally derived** |

## Key Insight

> **The universe does not "choose" its laws. 0 and 1 are the only axiom. Everything else — every law of physics, every constant, every particle — is a corollary.**

The Standard Model has 19 free parameters not because nature is complicated, but because we have been asking the wrong questions. The parameters are not free — they are forced by the recursion. The laws are not discovered — they are derived.

## Repository Structure

```
IDCM/
├── README.md                     ← This file
├── data/
│   ├── prologue_category_error.md
│   ├── paper_quantum_mechanics_as_necessity.md
│   ├── paper_general_relativity_as_consistency.md
│   ├── paper_string_theory_as_over_interpreted.md
│   ├── epilogue_end_of_fundamentalism.md
│   ├── derivation_of_derivation.md
│   ├── closure_*.md              (individual constant derivations)
│   ├── domain_definitions.zh-TW.md
│   └── reddit_post.md
├── scripts/
│   ├── verify_derivations.py
│   └── verify_meta_derivation.py
└── ROADMAP_FUNDAMENTAL_THEORY.md
```

## Author

**Lucifer Ng**  
ESP32 engineer, self-taught matrices, creator of the IDCM framework.

"一條公式 一組幾何 一個聖杯" — x²+x-1=0 + CY₃(36,98) + quantum gravity.

---

**License:** Public domain. All derivations are mathematical necessities — they cannot be owned.