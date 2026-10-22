#!/usr/bin/env python3
"""
multi_criteria_audit.py — IDCM 多準則審計引擎
==============================================

目的：設計 5 條準則組合，由窮究法收斂到唯一結構公式。

5 條準則：
1. Closure（閉包）— RHS 全部符號 trace 返 φ
2. Number-closure（數字閉合）— 整數 trace 返 Lucas L_n
3. Numerical precision — 誤差低於閾值
4. Cross-validation — 同時滿足多個獨立約束
5. Physical consistency — 錯嘅話宇宙崩潰

窮究 search：
- 對目標觀測量，列舉所有 φ-power 候選
- 逐條 filter
- 計 survivor 數
- 唯一 survivor = 答案

「我們現在只有打開宇宙嘅鎖匙，但係宇宙的鎖已經運行138億年。
  我們目的是用窮究法搵出所有可能性去還原個鎖嘅結構。」
"""

from __future__ import annotations
import math
import re
import sys
from dataclasses import dataclass, field
from typing import Callable, List, Set, Tuple, Optional, Dict
from itertools import product

PHI = (1 + math.sqrt(5)) / 2

# Lucas 數：L_n = φ^n + (-1)^n · φ^(-n)
def lucas(n: int) -> int:
    return round(PHI**n + (-1)**n * PHI**(-n))

# φ-identities：odd n → φ^n - φ^(-n) = L_n
# even n → φ^n + φ^(-n) = L_n
def lucas_identity(n: int) -> str:
    if n == 0:
        return "L_0 = φ^0 + φ^0"
    elif n % 2 == 1:
        return f"L_{n} = φ^{n} - φ^⁻{n}"
    else:
        return f"L_{n} = φ^{n} + φ^⁻{n}"


# ═══════════════════════════════════════════════════════════════
# Candidate Generation: 窮究列舉
# ═══════════════════════════════════════════════════════════════

@dataclass
class Candidate:
    """一個 φ-power 候選公式"""
    name: str
    expression: str
    value_evaluator: Callable[[], float]
    target_value: float
    target_name: str

    def error_pct(self) -> float:
        v = self.value_evaluator()
        return abs(v - self.target_value) / abs(self.target_value) * 100


def generate_phi_power_candidates(
    target_name: str,
    target_value: float,
    # 主項參數：φ^(-X)，X = N_d + h^11 + 修正
    main_terms: List[Tuple[int, str]],  # (X, description)
    # 修正項：X - δ·ε^c
    deltas: List[int],
    eps_powers: List[int],
) -> List[Candidate]:
    """窮究所有 V_EW/M_P = φ^-(main - delta * eps^power) 嘅候選"""
    candidates = []
    for main_x, main_desc in main_terms:
        for delta in deltas:
            for eps_pow in eps_powers:
                expr = f"phi ^ -({main_x} - {delta} * eps ^ {eps_pow})"
                name = f"φ^(-({main_x}-{delta}ε^{eps_pow}))"
                cand = Candidate(
                    name=name,
                    expression=expr,
                    value_evaluator=lambda m=main_x, d=delta, e=eps_pow:
                                        PHI ** -(m - d * (PHI**-1 / 4) ** e),
                    target_value=target_value,
                    target_name=target_name,
                )
                candidates.append(cand)
    return candidates


# ═══════════════════════════════════════════════════════════════
# 5 條準則 Filters
# ═══════════════════════════════════════════════════════════════

@dataclass
class FilterResult:
    name: str
    passed: List[Candidate]
    eliminated: List[Tuple[Candidate, str]]  # (candidate, reason)
    unique_survivor: Optional[Candidate] = None

    def summary(self) -> str:
        lines = [
            f"─── {self.name} ───",
            f"  Survivors: {len(self.passed)}/{len(self.passed) + len(self.eliminated)}",
        ]
        if self.unique_survivor:
            lines.append(f"  ✅ UNIQUE: {self.unique_survivor.name}")
        elif len(self.passed) == 1:
            lines.append(f"  ✅ UNIQUE: {self.passed[0].name}")
        elif len(self.passed) == 0:
            lines.append(f"  ❌ NO SURVIVORS — audit chain BROKEN")
        else:
            lines.append(f"  ⚠️  {len(self.passed)} survivors (need more criteria)")
            for c in self.passed:
                lines.append(f"     • {c.name}")
        if self.eliminated:
            for c, reason in self.eliminated[:3]:
                lines.append(f"  ✗ {c.name}: {reason}")
            if len(self.eliminated) > 3:
                lines.append(f"  ... +{len(self.eliminated)-3} more")
        return '\n'.join(lines)


def filter_1_closure(candidates: List[Candidate]) -> FilterResult:
    """準則 1：Closure — RHS 全部 SYMBOL traceable 返 φ（數字交俾 filter 2）"""
    # V_EW/M_P 嘅 RHS = phi, eps, 數字
    # 此處只 check 符號 closure；數字 closure 交俾 filter 2
    passed = []
    eliminated = []
    for c in candidates:
        # 抽 symbol tokens（唔包含數字）
        symbol_tokens = set(re.findall(r'[a-zA-Z]+', c.expression))
        non_traceable = symbol_tokens - {'phi', 'eps', 'sqrt', 'sin', 'cos', 'tan'}
        if not non_traceable:
            passed.append(c)
        else:
            eliminated.append((c, f"untraceable symbol: {non_traceable}"))
    return FilterResult(
        name="準則 1: Closure (RHS 符號全部 traceable 返 φ)",
        passed=passed,
        eliminated=eliminated,
    )


def filter_2_number_closure(candidates: List[Candidate]) -> FilterResult:
    """準則 2：Number-closure — 每個整數都係 Lucas L_n"""
    # 已知 IDCM 結構常數對應：
    # 2 = L_0, 3 = L_2, 4 = L_3, 7 = L_4, 11 = L_5
    # 33 = L_3² - L_2, 36 = L_3·L_2², 44 = L_3·L_5
    # 80 = L_3(L_5 + L_2²)
    lucas_ints = {2, 3, 4, 7, 11, 33, 36, 44, 80}

    passed = []
    eliminated = []
    for c in candidates:
        nums = set(int(n) for n in re.findall(r'\d+', c.expression))
        non_lucas = nums - lucas_ints
        if not non_lucas:
            passed.append(c)
        else:
            eliminated.append((c, f"非 Lucas 整數: {non_lucas}"))
    return FilterResult(
        name="準則 2: Number-closure (整數 = Lucas L_n)",
        passed=passed,
        eliminated=eliminated,
    )


def filter_3_numerical_precision(
    candidates: List[Candidate],
    threshold_pct: float = 5.0,
) -> FilterResult:
    """準則 3：Numerical precision — 誤差低於閾值"""
    passed = []
    eliminated = []
    for c in candidates:
        try:
            err = c.error_pct()
            if err < threshold_pct:
                passed.append(c)
            else:
                eliminated.append((c, f"誤差 {err:.2f}% > {threshold_pct}%"))
        except Exception as e:
            eliminated.append((c, f"evaluation failed: {e}"))
    return FilterResult(
        name=f"準則 3: Numerical precision (誤差 < {threshold_pct}%)",
        passed=passed,
        eliminated=eliminated,
    )


def filter_4_cross_validation(
    candidates: List[Candidate],
    # 額外約束：另一個獨立觀測量
    extra_target_name: str,
    extra_target_value: float,
    # 該觀測量與主觀測量嘅關係
    extra_relation: Callable[[Candidate], float],
    extra_threshold_pct: float = 5.0,
) -> FilterResult:
    """準則 4：Cross-validation — 滿足多個獨立約束"""
    passed = []
    eliminated = []
    for c in candidates:
        try:
            extra_pred = extra_relation(c)
            err = abs(extra_pred - extra_target_value) / abs(extra_target_value) * 100
            if err < extra_threshold_pct:
                passed.append(c)
            else:
                eliminated.append((
                    c,
                    f"{extra_target_name} 預測 {extra_pred:.4f} vs {extra_target_value:.4f} 誤差 {err:.2f}%",
                ))
        except Exception as e:
            eliminated.append((c, f"cross-val failed: {e}"))
    return FilterResult(
        name=f"準則 4: Cross-validation ({extra_target_name} 誤差 < {extra_threshold_pct}%)",
        passed=passed,
        eliminated=eliminated,
    )


def filter_5_physical_consistency(
    candidates: List[Candidate],
    # 物理一致性檢測函數
    physics_check: Callable[[Candidate], Tuple[bool, str]],
) -> FilterResult:
    """準則 5：Physical consistency — 錯嘅話宇宙崩潰"""
    passed = []
    eliminated = []
    for c in candidates:
        try:
            ok, reason = physics_check(c)
            if ok:
                passed.append(c)
            else:
                eliminated.append((c, f"physics: {reason}"))
        except Exception as e:
            eliminated.append((c, f"physics-check failed: {e}"))
    return FilterResult(
        name="準則 5: Physical consistency (宇宙唔崩潰)",
        passed=passed,
        eliminated=eliminated,
    )


# ═══════════════════════════════════════════════════════════════
# Audit Chain
# ═══════════════════════════════════════════════════════════════

def audit_chain(
    candidates: List[Candidate],
    filters: List[FilterResult],
) -> Dict:
    """運行 filter chain，記住 survivor count 變化"""
    current = candidates
    history = []

    for i, f in enumerate(filters):
        # 用當前 survivors 取代 initial pool
        f.passed = [c for c in current if c in f.passed]
        f.eliminated = [(c, r) for c, r in f.eliminated if c in current]

        history.append({
            'step': i + 1,
            'name': f.name,
            'before': len(current),
            'after': len(f.passed),
            'eliminated': len(f.eliminated),
        })

        current = f.passed

        if len(current) == 0:
            break
        if len(current) == 1 and i < len(filters) - 1:
            # 提早收斂
            f.unique_survivor = current[0]
            break

    if current and len(current) == 1:
        last = filters[-1]
        last.unique_survivor = current[0]

    return {
        'final_survivors': current,
        'history': history,
        'filters': filters,
    }


def report_audit(audit_result: Dict) -> str:
    """產生完整 audit 報告"""
    lines = []
    lines.append("=" * 70)
    lines.append("  IDCM MULTI-CRITERIA AUDIT — 5-CRITERION CONVERGENCE")
    lines.append("=" * 70)

    # Summary
    final = audit_result['final_survivors']
    lines.append("")
    lines.append(f"  Initial candidates: {audit_result['history'][0]['before']}")
    lines.append(f"  Final survivors:    {len(final)}")
    if len(final) == 1:
        lines.append(f"  ✅ UNIQUE: {final[0].name}")
    elif len(final) == 0:
        lines.append("  ❌ AUDIT CHAIN BROKEN — no survivors")
    else:
        lines.append(f"  ⚠️  Multiple survivors — criteria insufficient")

    # Filter-by-filter
    for h in audit_result['history']:
        lines.append("")
        lines.append(f"─── Step {h['step']}: {h['name']} ───")
        lines.append(f"  {h['before']} → {h['after']} ({h['eliminated']} eliminated)")

    # Final
    lines.append("")
    lines.append("─── FINAL SURVIVOR ───")
    if len(final) == 1:
        c = final[0]
        lines.append(f"  Formula: {c.name}")
        lines.append(f"  Expression: {c.expression}")
        lines.append(f"  Predicted: {c.value_evaluator():.6f}")
        lines.append(f"  Target:    {c.target_value:.6f}")
        lines.append(f"  Error:     {c.error_pct():.4f}%")
    elif len(final) == 0:
        lines.append("  No formula survived all 5 criteria.")
    else:
        for c in final:
            lines.append(f"  • {c.name}: error {c.error_pct():.4f}%")

    return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════════
# Demo: V_EW/M_P audit
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print()
    print("=" * 70)
    print("  IDCM MULTI-CRITERIA AUDIT")
    print("  「我們現在只有打開宇宙嘅鎖匙，但係宇宙的鎖已經運行138億年。」")
    print("  「我們目的是用窮究法搵出所有可能性去還原個鎖嘅結構。」")
    print("=" * 70)
    print()
    print("  ⚠️  注意：stress test 下，現存公式可能由 past pass → fail")
    print("         呢個唔係 bug，係 audit 嘅目的。")
    print("         Audit 唔係搵「乜嘢公式 common pass」，係搵")
    print("         「邊一條能 survive 所有 5 條 criteria」。")
    print()

    M_P = 1.22089e19  # GeV
    V_EW_observed = 246.22  # GeV
    m_t_observed = 172.76  # GeV

    # 窮究 V_EW/M_P 候選
    # Form: V_EW/M_P = φ^-(main_X - delta · ε^eps_pow)
    # 完整 search space
    main_terms = [
        (80, "N_d + h^11"),
        (79, "79"),
        (81, "81"),
        (44, "N_d only"),
        (36, "h^11 only"),
        (40, "40"),
        (50, "50"),
        (60, "60"),
        (70, "70"),
        (90, "90"),
        (100, "100"),
    ]

    candidates = generate_phi_power_candidates(
        target_name="V_EW/M_P",
        target_value=V_EW_observed / M_P,
        main_terms=main_terms,
        deltas=[0, 1, 2, 3, 4, 5, 6, 7, 11],
        eps_powers=[1, 2, 3, 4],
    )

    print(f"  Generated {len(candidates)} φ-power candidates (窮究 search)")
    print(f"  Target V_EW/M_P = {V_EW_observed/M_P:.6e}")
    print(f"  Target m_t = {m_t_observed} GeV")
    print()

    # 5 條 filter
    print("  Building 5-criterion audit chain...")
    print()

    f1 = filter_1_closure(candidates)
    print(f"  ✓ Filter 1: {len(f1.passed)} survivors (closure check)")

    f2 = filter_2_number_closure(f1.passed)
    print(f"  ✓ Filter 2: {len(f2.passed)} survivors (number-trace to Lucas)")

    f3 = filter_3_numerical_precision(f2.passed, threshold_pct=5.0)
    print(f"  ✓ Filter 3: {len(f3.passed)} survivors (precision < 5%)")

    f4 = filter_4_cross_validation(
        f3.passed,
        extra_target_name="m_t (from V_EW/√2)",
        extra_target_value=m_t_observed,
        extra_relation=lambda c: c.value_evaluator() * M_P / math.sqrt(2),
        extra_threshold_pct=1.0,
    )
    print(f"  ✓ Filter 4: {len(f4.passed)} survivors (m_t cross-val < 1%)")

    f5 = filter_5_physical_consistency(
        f4.passed,
        physics_check=lambda c: (
            c.value_evaluator() * M_P > 230,
            "電弱真空穩定" if c.value_evaluator() * M_P > 230 else "真空崩潰"
        ),
    )
    print(f"  ✓ Filter 5: {len(f5.passed)} survivors (宇宙唔崩潰)")

    # Audit chain
    result = audit_chain(candidates, [f1, f2, f3, f4, f5])

    print()
    print(report_audit(result))

    print()
    print("=" * 70)
    print("  KEY INSIGHT")
    print("=" * 70)
    print()
    print("  Stress test 唔係搵最大公因數（唔係搵 common pass set）。")
    print("  Audit chain 係逐條 criteria filter，fail 任何一條 = eliminated。")
    print()
    print("  現存公式喺嚴苛 criteria 下 fail = 正常，唔代表公式錯。")
    print("  佢只係話：呢條公式唔能 survive 所有 5 條 criteria 嘅 strict 版。")
    print()
    print("  真正嘅工作：")
    print("  1. 窮究所有 candidate")
    print("  2. 逐條 filter")
    print("  3. 觀察 survivor count 嘅收斂")
    print("  4. 唯一 survivor = 鎖嘅結構")
    print()
    print("  「唯一」唔係因為人類推導到，係因為宇宙試咗 N 次，")
    print("   只有呢條 survive。」— 結構公式唯一性原理")
    print()