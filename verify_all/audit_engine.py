#!/usr/bin/env python3
"""
audit_engine.py — IDCM 審計引擎
=================================
自動檢測：
  - 連續冪次模式（擬合紅旗）
  - 參數計數與自由參數分析
  - 依賴完整性
  - 跨公式共享修正項
  - 輸出審計報告
"""

import math
import re
from collections import defaultdict

from registry import FormulaRegistry, Formula


# ═══════════════════════════════════════════════════════════════
# 1. Pattern Detectors
# ═══════════════════════════════════════════════════════════════

class PatternDetector:
    """檢測公式中的可疑模式"""
    
    # ε 冪次的正則模式
    EPS_POWER_PATTERN = re.compile(r'varepsilon\^\{?(-?\d+)\}?')
    PHI_POWER_PATTERN = re.compile(r'varphi\^\{?(-?\d+)\}?')
    PHI_PYTHON_PATTERN = re.compile(r'phi\*\*\(?(-?\d+\.?\d*)\)?')
    EPS_PYTHON_PATTERN = re.compile(r'eps\*\*\(?(-?\d+\.?\d*)\)?')
    
    @classmethod
    def detect_consecutive_powers(cls, expression: str) -> dict:
        """
        檢測連續冪次模式
        
        Returns:
            {
                'has_consecutive': bool,
                'powers': list[int],
                'base': str,  # 'φ' or 'ε'
                'ratio': float | None,
                'description': str
            }
        """
        result = {
            'has_consecutive': False,
            'powers': [],
            'base': None,
            'ratio': None,
            'description': '',
        }
        
        # 檢測 ε 冪次
        eps_powers = set()
        for m in cls.EPS_POWER_PATTERN.finditer(expression):
            power = int(m.group(1))
            if power > 0:  # 只關注正冪次（修正項）
                eps_powers.add(power)
        
        # 檢測 φ 冪次（LaTeX）
        phi_powers = set()
        for m in cls.PHI_POWER_PATTERN.finditer(expression):
            power = int(m.group(1))
            if power > 0:  # 正冪次
                phi_powers.add(power)
            elif power < 0:  # 負冪次（φ⁻ⁿ）
                phi_powers.add(power)
        
        # 檢測 Python 格式的 φ 冪次
        for m in cls.PHI_PYTHON_PATTERN.finditer(expression):
            power = float(m.group(1))
            if power.is_integer():
                phi_powers.add(int(power))
        
        # 檢測 Python 格式的 ε 冪次
        for m in cls.EPS_PYTHON_PATTERN.finditer(expression):
            power = float(m.group(1))
            if power.is_integer():
                eps_powers.add(int(power))
        
        # 檢查 ε 連續冪次
        eps_sorted = sorted(eps_powers)
        if len(eps_sorted) >= 3:
            # 檢查是否連續
            for i in range(len(eps_sorted) - 2):
                if (eps_sorted[i+1] == eps_sorted[i] + 1 and 
                    eps_sorted[i+2] == eps_sorted[i] + 2):
                    result['has_consecutive'] = True
                    result['powers'] = eps_sorted[i:i+3]
                    result['base'] = 'ε'
                    # 計算比率
                    φ = (1 + math.sqrt(5)) / 2
                    ε = 1/(4*φ)
                    if len(eps_sorted) >= 2:
                        result['ratio'] = 1/ε
                    result['description'] = (
                        f"3 consecutive ε-powers: ε^{eps_sorted[i]}, ε^{eps_sorted[i+1]}, ε^{eps_sorted[i+2]}"
                    )
                    return result
        
        # 檢查 φ 連續冪次
        phi_sorted = sorted(phi_powers)
        # 特別檢查負冪次連續（φ⁻¹, φ⁻², φ⁻³）
        neg_phi = [p for p in phi_sorted if p < 0]
        if len(neg_phi) >= 3:
            for i in range(len(neg_phi) - 2):
                if (neg_phi[i+1] == neg_phi[i] + 1 and 
                    neg_phi[i+2] == neg_phi[i] + 2):
                    result['has_consecutive'] = True
                    result['powers'] = neg_phi[i:i+3]
                    result['base'] = 'φ⁻'
                    result['ratio'] = float(1/φ) if neg_phi[i] < 0 else float(φ)
                    result['description'] = (
                        f"3 consecutive φ-powers: φ^{neg_phi[i]}, φ^{neg_phi[i+1]}, φ^{neg_phi[i+2]}"
                    )
                    return result
        
        # 正 φ 冪次連續
        pos_phi = [p for p in phi_sorted if p > 0]
        if len(pos_phi) >= 3:
            for i in range(len(pos_phi) - 2):
                if (pos_phi[i+1] == pos_phi[i] + 1 and 
                    pos_phi[i+2] == pos_phi[i] + 2):
                    result['has_consecutive'] = True
                    result['powers'] = pos_phi[i:i+3]
                    result['base'] = 'φ'
                    result['ratio'] = float(φ)
                    result['description'] = (
                        f"3 consecutive φ-powers: φ^{pos_phi[i]}, φ^{pos_phi[i+1]}, φ^{pos_phi[i+2]}"
                    )
                    return result
        
        return result
    
    @classmethod
    def count_terms(cls, expression: str) -> int:
        """估算表達式中的項數"""
        # 計算 + 和 - 的數量（粗略估計）
        plus_count = expression.count('+')
        minus_count = expression.count('-')
        # 過濾掉負號在指數中的情況
        # 這是一個粗略估計
        return max(1, plus_count + minus_count)
    
    @classmethod
    def detect_shared_correction(cls, formulas: list[Formula]) -> dict:
        """檢測跨公式共享的修正項"""
        corrections_by_term = defaultdict(list)
        
        for formula in formulas:
            for correction in formula.corrections:
                for term in correction.terms:
                    corrections_by_term[term].append(formula.id)
        
        shared = {}
        for term, ids in corrections_by_term.items():
            if len(ids) >= 2:
                shared[term] = ids
        
        return shared


# ═══════════════════════════════════════════════════════════════
# 2. Audit Report
# ═══════════════════════════════════════════════════════════════

class AuditReport:
    """完整審計報告"""
    
    def __init__(self, registry: FormulaRegistry):
        self.registry = registry
        self.detector = PatternDetector()
    
    def generate(self) -> str:
        """生成完整審計報告"""
        lines = []
        lines.append("=" * 70)
        lines.append("  IDCM FORMULA AUDIT REPORT")
        lines.append("=" * 70)
        
        # 1. 摘要
        lines.append(self._summary_section())
        
        # 2. 連續冪次檢測
        lines.append(self._consecutive_powers_section())
        
        # 3. 共享修正項檢測
        lines.append(self._shared_corrections_section())
        
        # 4. 按 sector 審計
        lines.append(self._sector_audit_section())
        
        # 5. 公式詳細審計（僅可疑）
        lines.append(self._suspicious_details_section())
        
        # 6. 建議
        lines.append(self._recommendations_section())
        
        return '\n'.join(lines)
    
    def _summary_section(self) -> str:
        s = self.registry.summary()
        lines = [
            "\n─── 1. SUMMARY ───",
            f"  Total formulas:    {s['total']}",
            f"  🟢 Structural:     {s['structural']}",
            f"  🟡 Fitting:        {s['fitting']}",
            f"  ⚠️  Suspicious:     {s['suspicious']}",
            f"  🟢 Green status:   {s['green']}",
            f"  🟡 Yellow status:  {s['yellow']}",
            f"  🔮 Predictions:    {s['prediction']}",
            f"  Sectors:           {len(s['sectors'])}",
        ]
        for sec, count in sorted(s['sectors'].items()):
            lines.append(f"    {sec}: {count}")
        return '\n'.join(lines)
    
    def _consecutive_powers_section(self) -> str:
        lines = ["\n─── 2. CONSECUTIVE POWER DETECTION (FITTING RED FLAG) ───"]
        
        found = False
        for formula in self.registry.formulas.values():
            result = self.detector.detect_consecutive_powers(formula.expression)
            if result['has_consecutive']:
                found = True
                lines.append(f"\n  🟡 {formula.id}")
                lines.append(f"       Expression: {formula.expression}")
                lines.append(f"       Pattern: {result['description']}")
                lines.append(f"       Ratio: {result['ratio']:.4f}" if result['ratio'] else "")
                lines.append(f"       Derivation: {formula.derivation_type}")
                lines.append(f"       Error: {formula.error_pct}%" if formula.error_pct is not None else "")
        
        if not found:
            lines.append("  ✅ No consecutive power patterns detected")
        
        return '\n'.join(lines)
    
    def _shared_corrections_section(self) -> str:
        lines = ["\n─── 3. SHARED CORRECTION TERMS ───"]
        
        shared = self.detector.detect_shared_correction(
            list(self.registry.formulas.values())
        )
        
        if shared:
            for term, ids in shared.items():
                lines.append(f"\n  ⚠️  Term '{term}' appears in: {', '.join(ids)}")
                lines.append(f"       Same correction in multiple formulas = circular fitting risk")
        else:
            lines.append("  ✅ No shared correction terms detected")
        
        return '\n'.join(lines)
    
    def _sector_audit_section(self) -> str:
        lines = ["\n─── 4. SECTOR AUDIT ───"]
        
        sectors = defaultdict(list)
        for formula in self.registry.formulas.values():
            if formula.parent and formula.parent.sector:
                sectors[formula.parent.sector].append(formula)
        
        for sector, formulas in sorted(sectors.items()):
            green = sum(1 for f in formulas if f.status == '🟢')
            yellow = sum(1 for f in formulas if f.status == '🟡')
            suspicious = sum(1 for f in formulas if f.is_suspicious())
            lines.append(f"\n  {sector}: {len(formulas)} formulas")
            lines.append(f"    🟢 {green}  🟡 {yellow}  ⚠️  {suspicious}")
            for f in formulas:
                if f.is_suspicious():
                    lines.append(f"      🟡 {f.id}: {f.audit.suspicious_patterns[0] if f.audit.suspicious_patterns else 'flagged'}")
        
        return '\n'.join(lines)
    
    def _suspicious_details_section(self) -> str:
        lines = ["\n─── 5. SUSPICIOUS FORMULA DETAILS ───"]
        
        for formula in self.registry.formulas.values():
            if formula.is_suspicious():
                lines.append(f"\n  🟡 {formula.id}")
                lines.append(f"       Type: {formula.derivation_type}")
                lines.append(f"       Expression: {formula.expression}")
                lines.append(f"       Error: {formula.error_pct}%" if formula.error_pct is not None else "       Error: N/A")
                lines.append(f"       Effective params: {formula.effective_parameter_count()}")
                if formula.audit.suspicious_patterns:
                    for p in formula.audit.suspicious_patterns:
                        lines.append(f"       ⚠️  {p}")
                if formula.audit.notes:
                    lines.append(f"       Note: {formula.audit.notes}")
        
        return '\n'.join(lines)
    
    def _recommendations_section(self) -> str:
        lines = ["\n─── 6. RECOMMENDATIONS ───"]
        
        # Check m_τ/m_μ
        if 'm_τ/m_μ_approx' in self.registry.formulas:
            lines.append("\n  🔴 CRITICAL: m_τ/m_μ_approx (φ⁶-1-ε+ε²+ε³)")
            lines.append("       This is a 5-parameter polynomial fit.")
            lines.append("       Replace with structural version:")
            lines.append("       • m_τ/m_μ = φ^(19β) — 1 term, 0.30% error")
            lines.append("       • m_τ/m_μ = N_d/φ² + φ⁻¹/N_d — 2 structural terms, 0.021% error")
            lines.append("       Papers 03, 04, 05 must use structural version as primary.")
        
        # Check D_H/L_P corrections
        if 'D_H/L_P' in self.registry.formulas:
            lines.append("\n  🟡 WARNING: D_H/L_P boundary corrections (ε²-ε³-ε⁴)")
            lines.append("       This is a truncated geometric series with ratio 1/ε.")
            lines.append("       Need structural justification for truncation at ε⁴.")
            lines.append("       Same ε³ term appears in M_P formula — verify independence.")
        
        # Check M_P corrections
        if 'M_P' in self.registry.formulas:
            lines.append("\n  🟡 WARNING: M_P correction terms")
            lines.append("       -ε³ and -φ⁻²/256 need structural justification.")
            lines.append("       ε³ is shared with D_H/L_P — verify it's not circular.")
        
        # Check neutrino
        if 'm_ν1' in self.registry.formulas:
            lines.append("\n  🟡 NOTE: Neutrino masses use consecutive ε-powers (ε¹⁴, ε¹⁵, ε¹⁶)")
            lines.append("       This is structurally justified (generation gap = ε × each step).")
            lines.append("       But verify that the consecutive pattern is derived, not fitted.")
        
        lines.append("\n  ✅ Structural formulas (0 free parameters): 🟢")
        lines.append("  ⚠️  Verify perturbative corrections are independently derived.")
        lines.append("  ❌ Deprecate all fitting-type formulas from papers.")
        
        return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════════
# 3. Main
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    registry = FormulaRegistry()
    report = AuditReport(registry)
    print(report.generate())