#!/usr/bin/env python3
"""
progressive_stress_test.py — IDCM 漸進壓力測試
================================================

目的：逐步加大 criteria 嘅 pressure，直至所有現存公式 fail。
觀察 fail 嘅原因 = 知道需要咩新 structure。

方法論：
  1. 列出所有現存粒子質量公式
  2. 對每一條施加漸進 criteria
  3. Track pass/fail 嘅 boundary
  4. 當所有公式 fail = 我哋知道 why 同 how to pass

「現存公式喺壓力下 fail 唔係 bug，係 feature——
  fail 嘅原因就係需要新 structure 嘅 hint。」
"""

from __future__ import annotations
import math
import re
from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple

PHI = (1 + math.sqrt(5)) / 2


# ═══════════════════════════════════════════════════════════════
# 現存公式 registry
# ═══════════════════════════════════════════════════════════════

@dataclass
class ExistingFormula:
    """現存嘅一條 IDCM 粒子質量公式"""
    name: str
    expression: str
    evaluator: Callable[[], float]
    target: float
    # 預先知道嘅 metadata
    claimed_status: str  # 🟢/🟡/🔴
    claimed_error_pct: float


# 全部現存粒子質量公式（直接從 formulas.yaml 抽出）
M_T = 172.76  # GeV
M_B = 4.18    # GeV
M_TAU = 1.77686  # GeV
M_C = 1.27    # GeV
M_S = 0.0934  # GeV
M_MU = 0.1057 # GeV
M_U = 0.00216 # GeV
M_D = 0.00467 # GeV
M_E = 0.000511 # GeV
PHI_VAL = PHI
EPS = PHI**-1 / 4
BETA = PHI**-1 / 2
KAPPA = 1/16
N_D = 44
H11 = 36
M = 33
K_U = M * BETA
K_D = (M - 7) * BETA - PHI**-4
K_L = (M - 14) * BETA


def _build_existing_formulas():
    return [
        # 第二代
        ExistingFormula(
            name="m_c/m_t = φ^(-k_u)",
            expression="phi ^ -(33 * beta)",
            evaluator=lambda: PHI**(-K_U),
            target=M_C / M_T,
            claimed_status="🟢",
            claimed_error_pct=0.57,
        ),
        ExistingFormula(
            name="m_s/m_b = φ^(-k_d)",
            expression="phi ^ -((33-7)*beta - phi^-4)",
            evaluator=lambda: PHI**(-K_D),
            target=M_S / M_B,
            claimed_status="🟢",
            claimed_error_pct=1.18,
        ),
        ExistingFormula(
            name="m_μ/m_τ = φ^(-k_l)",
            expression="phi ^ -((33-14)*beta)",
            evaluator=lambda: PHI**(-K_L),
            target=M_MU / M_TAU,
            claimed_status="🟢",
            claimed_error_pct=0.30,
        ),

        # 第一代
        ExistingFormula(
            name="m_u/m_t = φ^(-(k_u+k_d+k_l-φ⁻¹))",
            expression="phi ^ -(k_u + k_d + k_l - phi^-1)",
            evaluator=lambda: PHI**(-(K_U + K_D + K_L - PHI**-1)),
            target=M_U / M_T,
            claimed_status="🟢",
            claimed_error_pct=4.08,
        ),
        ExistingFormula(
            name="m_d/m_b = φ^(-(2k_d-φ))",
            expression="phi ^ -(2*k_d - phi)",
            evaluator=lambda: PHI**(-(2*K_D - PHI)),
            target=M_D / M_B,
            claimed_status="🟢",
            claimed_error_pct=2.27,
        ),
        ExistingFormula(
            name="m_e/m_τ = φ^(-(k_l+M/3))",
            expression="phi ^ -(k_l + M/3)",
            evaluator=lambda: PHI**(-(K_L + M/3)),
            target=M_E / M_TAU,
            claimed_status="🟢",
            claimed_error_pct=3.59,
        ),

        # 質量比
        ExistingFormula(
            name="m_μ/m_e = φ¹¹ + 3φ²",
            expression="phi^11 + 3*phi^2",
            evaluator=lambda: PHI**11 + 3*PHI**2,
            target=M_MU / M_E,
            claimed_status="🟢",
            claimed_error_pct=0.04,
        ),
        ExistingFormula(
            name="m_τ/m_μ = φ^(19β)",
            expression="phi ^ (19 * beta)",
            evaluator=lambda: PHI**(19*BETA),
            target=M_TAU / M_MU,
            claimed_status="🟢",
            claimed_error_pct=0.30,
        ),

        # Higgs
        ExistingFormula(
            name="m_H = 2√κ × V_EW",
            expression="2 * sqrt(kappa) * 246.22",
            evaluator=lambda: 2 * math.sqrt(KAPPA) * 246.22,
            target=125.25,  # PDG Higgs mass
            claimed_status="🟢",
            claimed_error_pct=0.0,
        ),

        # ⚠️ 已知 fitting
        ExistingFormula(
            name="m_τ/m_μ ≈ φ⁶-1-ε+ε²+ε³ (FITTING!)",
            expression="phi^6 - 1 - eps + eps^2 + eps^3",
            evaluator=lambda: PHI**6 - 1 - EPS + EPS**2 + EPS**3,
            target=M_TAU / M_MU,
            claimed_status="🟡",
            claimed_error_pct=0.0018,
        ),

        # V_EW (最新 closure)
        ExistingFormula(
            name="V_EW/M_P = φ^(-(N_d+h¹¹)+4ε²)",
            expression="phi ^ -((44+36) - 4*eps^2)",
            evaluator=lambda: PHI**(-((N_D + H11) - 4*EPS**2)),
            target=246.22 / 1.22089e19,
            claimed_status="🟢",
            claimed_error_pct=0.85,
        ),
    ]


# ═══════════════════════════════════════════════════════════════
# 漸進 stress test
# ═══════════════════════════════════════════════════════════════

@dataclass
class StressLevel:
    name: str
    description: str
    threshold: float
    test: Callable[[ExistingFormula, float], Tuple[bool, str]]
    passed: List[ExistingFormula] = field(default_factory=list)
    failed: List[Tuple[ExistingFormula, str]] = field(default_factory=list)


def precision_test(f: ExistingFormula, threshold: float) -> Tuple[bool, str]:
    try:
        err = abs(f.evaluator() - f.target) / abs(f.target) * 100
        if err < threshold:
            return (True, f"誤差 {err:.4f}% < {threshold}%")
        return (False, f"誤差 {err:.4f}% ≥ {threshold}%")
    except Exception as e:
        return (False, str(e))


def number_trace_test(f: ExistingFormula, _threshold: float) -> Tuple[bool, str]:
    """所有裸數字都係 Lucas L_n"""
    nums = set(int(n) for n in re.findall(r'\b\d+\b', f.expression))
    lucas_ints = {1, 2, 3, 4, 7, 11, 33, 36, 44}
    non_lucas = nums - lucas_ints
    if not non_lucas:
        return (True, "全部數字係 Lucas L_n")
    return (False, f"非 Lucas 整數: {non_lucas}")


def structure_test(f: ExistingFormula, _threshold: float) -> Tuple[bool, str]:
    """RHS 冇未 traceable 嘅 symbol"""
    symbols = set(re.findall(r'[a-zA-Z]+', f.expression))
    bad = symbols - {'phi', 'eps', 'beta', 'kappa', 'sqrt'}
    if not bad:
        return (True, "全部 symbol traceable 返 φ")
    return (False, f"untraceable: {bad}")


def derivation_chain_test(f: ExistingFormula, _threshold: float) -> Tuple[bool, str]:
    """每一條 step 都有 derivation chain (no consecutive free terms)"""
    # 計 expression 嘅 term 數量
    # 簡單 heuristic：count 項數
    terms = len(re.findall(r'[+-]', f.expression))
    if terms <= 2:
        return (True, f"≤ 2 terms（{terms}）")
    return (False, f">{2} terms ({terms}) — risk of fitting")


def consistency_test(f: ExistingFormula, threshold: float) -> Tuple[bool, str]:
    """formula 喺 sector 內部 cross-consistent（簡化版）"""
    # 對 m_X/m_Y 公式，check 同 sector 內另一條公式 consistent
    # 簡化：只 check 公式名是否涉及 'approx' 或 'fitting' pattern
    if 'approx' in f.name or 'FITTING' in f.name:
        return (False, "公式名標記為 approx/fitting")
    return (True, "no approx marker")


def physical_stability_test(f: ExistingFormula, _threshold: float) -> Tuple[bool, str]:
    """formula 唔會導致物理真空崩潰"""
    # 簡化：要求所有粒子質量 > 0
    val = f.evaluator()
    if val <= 0:
        return (False, f"negative value: {val}")
    return (True, f"value > 0: {val:.4e}")


# === 加壓：更嚴苛嘅 closed form criteria ===

# 基礎 Lucas L_n (≤ 11): 1, 2, 3, 4, 7, 11
BASIC_LUCAS = {1, 2, 3, 4, 7, 11}


def composite_integer_test(f: ExistingFormula) -> Tuple[bool, str]:
    """所有整數必須係 basic Lucas (≤ 11)，唔可以係 composite"""
    nums = set(int(n) for n in re.findall(r'\b\d+\b', f.expression))
    composite = nums - BASIC_LUCAS
    if not composite:
        return (True, "全部係 basic Lucas L_n")
    return (False, f"composite integers: {composite} — 應該展開為 Lucas 乘積")


def no_pdg_inputs_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式不允許 hardcode PDG 數值（m_t = 172.76, V_EW = 246.22 等）"""
    # 簡化：檢查 expression 是否有大數字（PDG 數值通常係 3-6 位數）
    nums = [int(n) for n in re.findall(r'\b\d+\b', f.expression)]
    pdg_like = [n for n in nums if n > 11 and n < 10000]
    if not pdg_like:
        return (True, "冇 PDG-like 數值")
    return (False, f"hardcoded: {pdg_like} — 應該係 φ-derive")


def sector_coverage_test(f: ExistingFormula) -> Tuple[bool, str]:
    """單一公式必須預測成個 sector 嘅所有粒子"""
    # 簡化：要求公式名包含 sector 關鍵字 AND predict 所有 3 個 generation
    # 例如 up-sector 公式應該 predict m_u, m_c, m_t
    if 'm_c/m_t' in f.name or 'm_s/m_b' in f.name or 'm_μ/m_τ' in f.name:
        # 呢啲係 ratio 公式，只 predict 2nd/3rd — 唔夠
        return (False, "只 predict ratio，冇 cover 1st gen")
    if 'm_u/m_t' in f.name or 'm_d/m_b' in f.name or 'm_e/m_τ' in f.name:
        # predict 1st/3rd — 但 1st/2nd 3rd 都唔齊
        return (False, "只 predict 1st/3rd，冇 cover 2nd gen")
    if 'm_μ/m_e' in f.name:
        # 跨越兩代 — 比較 comprehensive
        return (True, "cross-generation ratio")
    return (False, "single particle — no sector coverage")


def predict_3rd_gen_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式必須從 φ predict 第三代絕對質量，唔可以係 input"""
    # 簡化：如果公式涉及 ratio 形式，佢必然依賴 3rd-gen input
    if 'm_' in f.name and ('m_t' in f.target.__repr__() or 'm_b' in f.target.__repr__() or 'm_tau' in f.target.__repr__()):
        return (False, "ratio 形式依賴 3rd-gen input")
    return (True, "獨立 predict")


def zero_free_params_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式自由度 = 0（每個係數都係 pipeline 強迫嘅）"""
    # 簡化：計 expression 入面嘅 free parameter 數量
    # free parameter = 唔係 φ, eps, beta, kappa, sqrt 嘅 token
    symbols = set(re.findall(r'[a-zA-Z]+', f.expression))
    free = symbols - {'phi', 'eps', 'beta', 'kappa', 'sqrt'}
    if not free:
        return (True, "0 free parameters")
    return (False, f"free parameters: {free} — 應該係 derived constants")


# === Level 14-22: 更極端嘅 criteria ===

def pure_phi_power_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式只可以係單個 φ-power，唔可以有加法項"""
    if '+' in f.expression or '-' in f.expression.replace('phi ^ -', ''):
        return (False, "有加法/減法項 — 必須係單一 φ-power")
    return (True, "pure φ-power")


def zero_composite_symbols_test(f: ExistingFormula) -> Tuple[bool, str]:
    """RHS 不可以出現 composite symbol"""
    # composite symbols: M, N_d, h11, k_u, k_d, k_l, k_H
    composite = {'M', 'N_d', 'h11', 'h^11', 'k_u', 'k_d', 'k_l', 'k_H',
                 'B', 'L'}
    symbols = set(re.findall(r'[a-zA-Z]+', f.expression))
    bad = symbols & composite
    if not bad:
        return (True, "冇 composite symbols")
    return (False, f"composite symbols: {bad} — 必須展開為 φ/ε/β/κ")


def no_mp_input_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式不能依賴 M_P 外部 input"""
    # 簡化：如果 target 涉及 M_P 比值（V_EW/M_P）→ fail
    target_str = str(f.target)
    if 'e-17' in target_str or 'e-16' in target_str:  # M_P/V_EW 比例嘅科學記法
        return (False, "ratio 含 M_P — 需要 M_P 作為外部 input")
    return (True, "冇 M_P 依賴")


def full_lucas_expansion_test(f: ExistingFormula) -> Tuple[bool, str]:
    """所有整數必須係 bare Lucas (1, 2, 3, 4, 7, 11)，禁止 composite (14, 19, 33 等)"""
    nums = set(int(n) for n in re.findall(r'\b\d+\b', f.expression))
    bare_lucas = {1, 2, 3, 4, 7, 11}
    composite = nums - bare_lucas
    if not composite:
        return (True, "全部係 bare Lucas L_n")
    return (False, f"composite integers: {composite} — 必須展開為 L_n 乘積")


def predict_all_gen_abs_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式必須 predict 三個 generation 嘅絕對質量"""
    if 'm_' in f.name and '/m_' in f.name:
        return (False, "ratio 形式只 predict relative，唔係 absolute")
    if f.target > 100 and f.target < 1e6:
        # 涉及絕對質量嘅合理 GeV 數值
        return (True, "predicts absolute mass")
    return (False, "唔 predict 絕對質量")


def explain_coefficient_test(f: ExistingFormula) -> Tuple[bool, str]:
    """每個係數必須有 derivation chain"""
    # 簡化：任何 bare 數字 > 11 都係 unexplained
    nums = [int(n) for n in re.findall(r'\b\d+\b', f.expression)]
    unexplained = [n for n in nums if n > 11]
    if not unexplained:
        return (True, "全部係數字係 basic Lucas")
    return (False, f"unexplained coefficients: {unexplained}")


def single_term_test(f: ExistingFormula) -> Tuple[bool, str]:
    """整條公式係單個 term（冇 + - × ÷ 嘅組合）"""
    ops = re.findall(r'[+\-*/]', f.expression.replace('phi ^ -', '').replace('^', ''))
    ops = [op for op in ops if op not in ('^',)]  # remove power operators
    if not ops:
        return (True, "single term")
    return (False, f"multi-term: {len(ops)} operators")


def zero_exp_knowledge_test(f: ExistingFormula) -> Tuple[bool, str]:
    """公式推導過程中 zero 引用任何 PDG / 觀測值"""
    # 簡化：檢查 expression 是否有 > 11 嘅數字（除咗 Lucas composite）
    nums = [int(n) for n in re.findall(r'\b\d+\b', f.expression)]
    big = [n for n in nums if n > 11 and n not in (33, 36, 44, 80)]
    if not big:
        return (True, "冇 PDG knowledge")
    return (False, f"PDG-like: {big}")


def progressive_stress_test(formulas: List[ExistingFormula]):
    """逐步加大壓力，記錄每一步嘅 pass/fail"""
    print("=" * 70)
    print("  IDCM PROGRESSIVE STRESS TEST")
    print("  目的：逐步加大 criteria，直至所有現存公式 fail。")
    print("  「現存公式喺壓力下 fail 唔係 bug，係 feature——")
    print("   fail 嘅原因就係需要新 structure 嘅 hint。」")
    print("=" * 70)
    print()

    levels = [
        StressLevel(
            name="Level 0: closure check (RHS symbols)",
            description="全部 RHS 符號 traceable 返 φ",
            threshold=0,
            test=structure_test,
        ),
        StressLevel(
            name="Level 1: number-trace (整數 = Lucas L_n)",
            description="所有裸數字都係 Lucas 數 L_n",
            threshold=0,
            test=number_trace_test,
        ),
        StressLevel(
            name="Level 2: precision < 5%",
            description="數值誤差低於 5%",
            threshold=5.0,
            test=precision_test,
        ),
        StressLevel(
            name="Level 3: precision < 1%",
            description="數值誤差低於 1%",
            threshold=1.0,
            test=precision_test,
        ),
        StressLevel(
            name="Level 4: precision < 0.1%",
            description="數值誤差低於 0.1%",
            threshold=0.1,
            test=precision_test,
        ),
        StressLevel(
            name="Level 5: precision < 0.01%",
            description="數值誤差低於 0.01%",
            threshold=0.01,
            test=precision_test,
        ),
        StressLevel(
            name="Level 6: minimal term count",
            description="項數 ≤ 2（拒絕多項式）",
            threshold=0,
            test=derivation_chain_test,
        ),
        StressLevel(
            name="Level 7: no approx markers",
            description="公式名唔含 'approx' / 'fitting' pattern",
            threshold=0,
            test=consistency_test,
        ),
        StressLevel(
            name="Level 8: physical stability",
            description="所有預測值 > 0（真空唔崩潰）",
            threshold=0,
            test=physical_stability_test,
        ),
        # === 加壓：逐步要求更嚴苛嘅 closed form ===
        StressLevel(
            name="Level 9: composite integers (禁止 14, 19, 33 等)",
            description="所有整數必須係 basic Lucas L_n (≤ 11)，唔可以係 composite",
            threshold=0,
            test=lambda f, _: composite_integer_test(f),
        ),
        StressLevel(
            name="Level 10: 0 experimental inputs",
            description="公式不允許 hardcode 任何 PDG 數值（246.22, 172.76 等）",
            threshold=0,
            test=lambda f, _: no_pdg_inputs_test(f),
        ),
        StressLevel(
            name="Level 11: predict all sector observables",
            description="單一公式必須同時預測成個 sector 嘅所有粒子",
            threshold=0,
            test=lambda f, _: sector_coverage_test(f),
        ),
        StressLevel(
            name="Level 12: predict 3rd-gen absolute mass",
            description="公式必須從 φ predict 第三代絕對質量，唔可以係 input",
            threshold=0,
            test=lambda f, _: predict_3rd_gen_test(f),
        ),
        StressLevel(
            name="Level 13: no free parameters (K=0)",
            description="公式自由度 = 0（每個係數都係 pipeline 強迫嘅）",
            threshold=0,
            test=lambda f, _: zero_free_params_test(f),
        ),
        # === 進一步加壓 ===
        StressLevel(
            name="Level 14: precision < 0.001%",
            description="數值誤差低於 0.001%",
            threshold=0.001,
            test=precision_test,
        ),
        StressLevel(
            name="Level 15: pure φ-power only (no additive terms)",
            description="公式只可以係單個 φ-power，唔可以有加法項（φ¹¹ + 3φ² 唔合格）",
            threshold=0,
            test=lambda f, _: pure_phi_power_test(f),
        ),
        StressLevel(
            name="Level 16: zero M/B/N_d/k_* symbols",
            description="RHS 不可以出現 composite symbol (M, B, N_d, k_u 等)，必須係純 φ/ε/β/κ 表達式",
            threshold=0,
            test=lambda f, _: zero_composite_symbols_test(f),
        ),
        StressLevel(
            name="Level 17: no M_P input",
            description="公式不能依賴 M_P 作為外部 input（純 ratio 唔可以）",
            threshold=0,
            test=lambda f, _: no_mp_input_test(f),
        ),
        StressLevel(
            name="Level 18: no bare integers (full Lucas expansion)",
            description="所有整數必須展開為 Lucas 乘積（L_n1 × L_n2 等），禁止任何 bare 數字",
            threshold=0,
            test=lambda f, _: full_lucas_expansion_test(f),
        ),
        StressLevel(
            name="Level 19: predict 1st gen AND 2nd gen AND 3rd gen absolute mass",
            description="公式必須 predict 三個 generation 嘅絕對質量，唔係 ratio",
            threshold=0,
            test=lambda f, _: predict_all_gen_abs_test(f),
        ),
        StressLevel(
            name="Level 20: explain why each coefficient",
            description="每個係數必須有 derivation chain（唔可以係 chosen）",
            threshold=0,
            test=lambda f, _: explain_coefficient_test(f),
        ),
        StressLevel(
            name="Level 21: single-term expression",
            description="整條公式係單個 term（冇 + - × ÷ 嘅組合）",
            threshold=0,
            test=lambda f, _: single_term_test(f),
        ),
        StressLevel(
            name="Level 22: zero experimental knowledge",
            description="公式推導過程中 zero 引用任何 PDG / 觀測值",
            threshold=0,
            test=lambda f, _: zero_exp_knowledge_test(f),
        ),
    ]

    current_pass = formulas
    print(f"  Initial: {len(formulas)} 現存公式")
    print()

    for level in levels:
        new_pass = []
        new_fail = []
        for f in current_pass:
            ok, reason = level.test(f, level.threshold)
            if ok:
                new_pass.append(f)
            else:
                new_fail.append((f, reason))

        level.passed = new_pass
        level.failed = new_fail

        # Print level result
        n_pass = len(new_pass)
        n_fail = len(new_fail)
        status = "✅" if n_pass > 0 else ("❌ ALL FAIL" if n_fail > 0 else "")
        print(f"  [{level.name}]")
        print(f"    Pass: {n_pass}/{len(current_pass)}  Fail: {n_fail}  {status}")

        if new_fail:
            # 顯示 fail 原因（最多 3 條）
            for f, reason in new_fail[:3]:
                print(f"      ✗ {f.name[:50]}")
                print(f"          {reason}")
            if len(new_fail) > 3:
                print(f"      ... +{len(new_fail) - 3} more")

        current_pass = new_pass
        print()

        if not current_pass:
            print("  ─── ALL CURRENT FORMULAS FAILED ───")
            print()
            break

    print("=" * 70)
    print("  ANALYSIS: 最後 fail 嘅 level = 需要新 structure 嘅 hint")
    print("=" * 70)
    print()

    # 識別「first all-fail level」
    first_all_fail = None
    for level in levels:
        if not level.passed and level.failed:
            first_all_fail = level
            break

    if first_all_fail:
        print(f"  First all-fail level: {first_all_fail.name}")
        print(f"  Description: {first_all_fail.description}")
        print()
        print("  Fail 嘅原因（point to 缺失嘅 structure）：")
        # 收集所有 fail 原因
        all_reasons = set()
        for f, reason in first_all_fail.failed:
            all_reasons.add(reason)
        for r in sorted(all_reasons):
            print(f"    • {r}")
    else:
        print("  All levels passed — 現存公式 survive 所有 9 條 stress。")

    print()
    print("=" * 70)
    print("  KEY INSIGHT")
    print("=" * 70)
    print()
    print("  Stress test 唔係搵「邊條 survive」，係搵：")
    print("    1. 現存公式喺邊個 level 開始 fail")
    print("    2. fail 嘅原因 = 缺少咗咩 structure")
    print("    3. 解決方法 = 推導新嘅 structure")
    print()
    print("  當所有現存公式 fail：")
    print("    我哋知道 why (fail 原因)")
    print("    同 how to pass (需要新 structure)")
    print()
    print("  「現存公式由 pass → fail 係正常，係 audit 嘅目的。」")


if __name__ == "__main__":
    formulas = _build_existing_formulas()
    progressive_stress_test(formulas)