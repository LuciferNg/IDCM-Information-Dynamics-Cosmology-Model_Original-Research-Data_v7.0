#!/usr/bin/env python3
"""
registry.py — IDCM Formula Registry Object Model
================================================
載入 formulas.yaml，建立 typed objects + 依賴圖 (DAG)

Key classes:
  - Formula: 單條公式的完整物件
  - FormulaRegistry: 整個 registry，含依賴圖
  - DependencyGraph: 拓撲排序引擎
"""

import yaml
import math
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional, Literal, Any

# ─── Type aliases ───
DerivationType = Literal["axiom", "input", "structural", "perturbative", "fitting"]
StatusType = Literal["📥", "🟢", "🟡", "🔮", "❌"]


# ═══════════════════════════════════════════════════════════════
# 1. Object Model
# ═══════════════════════════════════════════════════════════════

@dataclass
class ParentStructure:
    """母構體 — 公式從哪個結構湧現"""
    structure: str
    sector: Optional[str]
    mode: Optional[str]
    parameter: Optional[str]
    generation: Optional[int]
    eigenvalue: Optional[str]


@dataclass
class Correction:
    """微擾修正記錄"""
    type: str              # none | RG | boundary | instanton | geometric
    source: Optional[str] = None
    terms: list[str] = field(default_factory=list)
    structural_justification: Optional[str] = None
    note: Optional[str] = None
    expected: Optional[str] = None
    status: Optional[str] = None


@dataclass
class AuditInfo:
    """審計標記 — 自動檢測用 metadata"""
    parameter_count: int = 0
    consecutive_powers: bool = False
    power_ratio_check: Optional[str] = None
    suspicious_patterns: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class Formula:
    """單條公式的完整物件"""
    id: str
    expression: str
    value: float
    unit: str
    error_pct: Optional[float]
    status: StatusType
    parent: Optional[ParentStructure]
    derivation_type: DerivationType
    derivation_path: list[str]
    corrections: list[Correction]
    audit: AuditInfo
    papers: list[str]
    
    def is_structural(self) -> bool:
        """是否為結構推導（非擬合）"""
        return self.derivation_type in ("axiom", "input", "structural")
    
    def is_suspicious(self) -> bool:
        """是否有可疑擬合模式"""
        if self.audit.suspicious_patterns:
            return True
        if self.audit.consecutive_powers:
            return True
        if self.derivation_type == "fitting":
            return True
        return False
    
    def effective_parameter_count(self) -> int:
        """有效自由參數數量（structural = 0, fitting = 參數數）"""
        if self.derivation_type == "structural":
            return 0
        if self.derivation_type == "perturbative":
            return len(self.corrections) if self.corrections else 0
        return self.audit.parameter_count


@dataclass
class DependencyGraph:
    """依賴圖 — 有向無環圖 (DAG)"""
    edges: dict[str, set[str]] = field(default_factory=dict)
    
    def add_dependency(self, formula_id: str, depends_on: str):
        if formula_id not in self.edges:
            self.edges[formula_id] = set()
        self.edges[formula_id].add(depends_on)
    
    def topological_sort(self) -> list[str]:
        """Kahn's algorithm — 拓撲排序"""
        in_degree: dict[str, int] = {}
        for node in self.edges:
            in_degree.setdefault(node, 0)
            for dep in self.edges[node]:
                in_degree.setdefault(dep, 0)
                in_degree[dep] = in_degree.get(dep, 0) + 1
        
        # 修正：in_degree 是依賴數，不是被依賴數
        # 重新計算：每個節點的被依賴數
        dep_count: dict[str, int] = {n: 0 for n in self.edges}
        for node, deps in self.edges.items():
            for dep in deps:
                if dep in dep_count:
                    dep_count[dep] += 1
        
        # 修正：Kahn's algorithm
        # 入度 = 還有多少依賴未滿足
        in_degree = {}
        for node in self.edges:
            in_degree[node] = len(self.edges[node])
        
        # 收集所有節點
        all_nodes = set(self.edges.keys())
        for deps in self.edges.values():
            all_nodes.update(deps)
        
        for node in all_nodes:
            if node not in in_degree:
                in_degree[node] = 0
        
        queue = [n for n in all_nodes if in_degree.get(n, 0) == 0]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            # 找所有依賴此節點的節點
            for n, deps in self.edges.items():
                if node in deps:
                    in_degree[n] -= 1
                    if in_degree[n] == 0:
                        queue.append(n)
        
        # 檢查循環依賴
        if len(result) != len(all_nodes):
            remaining = set(all_nodes) - set(result)
            raise ValueError(f"Circular dependency detected: {remaining}")
        
        return result


# ═══════════════════════════════════════════════════════════════
# 2. Formula Registry
# ═══════════════════════════════════════════════════════════════

class FormulaRegistry:
    """整個 registry，載入 YAML + 建立物件模型 + 依賴圖"""
    
    def __init__(self, yaml_path: str = None):
        self.yaml_path = yaml_path or self._default_path()
        self.formulas: dict[str, Formula] = {}
        self.parent_structures: dict = {}
        self.dag = DependencyGraph()
        self._load()
    
    def _default_path(self) -> str:
        """自動查找 formulas.yaml 路徑"""
        candidates = [
            Path(__file__).parent / "formulas.yaml",
            Path.cwd() / "verify_all" / "formulas.yaml",
            Path.cwd() / "formulas.yaml",
        ]
        for p in candidates:
            if p.exists():
                return str(p)
        raise FileNotFoundError("formulas.yaml not found")
    
    def _load(self):
        """載入 YAML 並建立物件"""
        with open(self.yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        
        self.parent_structures = {
            ps['id']: ps for ps in data.get('parent_structures', {}).values()
        }
        
        for entry in data.get('formulas', []):
            formula = self._parse_formula(entry)
            self.formulas[formula.id] = formula
            
            # 建立依賴關係
            for dep in self._dependencies_from_expression(formula.expression):
                self.dag.add_dependency(formula.id, dep)
            # 從 derivation_path 推斷依賴
            for step in formula.derivation_path:
                for dep in self._dependencies_from_expression(step):
                    self.dag.add_dependency(formula.id, dep)
            # 從 parent parameter 推斷依賴
            if formula.parent and formula.parent.parameter:
                for dep in self._dependencies_from_expression(formula.parent.parameter):
                    self.dag.add_dependency(formula.id, dep)
    
    def _parse_formula(self, entry: dict) -> Formula:
        """將 YAML dict 解析為 Formula 物件"""
        parent = None
        if entry.get('parent'):
            p = entry['parent']
            parent = ParentStructure(
                structure=p.get('structure', ''),
                sector=p.get('sector'),
                mode=p.get('mode'),
                parameter=p.get('parameter'),
                generation=p.get('generation'),
                eigenvalue=p.get('eigenvalue'),
            )
        
        corrections = []
        for c in entry.get('corrections', []):
            corrections.append(Correction(
                type=c.get('type', 'none'),
                source=c.get('source'),
                terms=c.get('terms', []),
                structural_justification=c.get('structural_justification'),
                note=c.get('note'),
                expected=c.get('expected'),
                status=c.get('status'),
            ))
        
        audit_data = entry.get('audit', {})
        audit = AuditInfo(
            parameter_count=audit_data.get('parameter_count', 0),
            consecutive_powers=audit_data.get('consecutive_powers', False),
            power_ratio_check=audit_data.get('power_ratio_check'),
            suspicious_patterns=audit_data.get('suspicious_patterns', []),
            notes=audit_data.get('notes', ''),
        )
        
        return Formula(
            id=entry['id'],
            expression=entry['expression'],
            value=float(entry.get('value', 0)),
            unit=entry.get('unit', ''),
            error_pct=entry.get('error_pct'),
            status=entry.get('status', '🟡'),
            parent=parent,
            derivation_type=entry.get('derivation_type', 'unknown'),
            derivation_path=entry.get('derivation_path', []),
            corrections=corrections,
            audit=audit,
            papers=entry.get('papers', []),
        )
    
    def _dependencies_from_expression(self, expr: str) -> list[str]:
        """從表達式推斷依賴的公式 ID"""
        # 已知 IDCM 公式 ID 列表
        known_ids = {
            'φ', 'ε', 'κ', 'β', 'N_d', 'L', 'M',
            'k_u', 'k_d', 'k_l', 'k_H',
            'm_t', 'm_b', 'm_τ', 'm_c', 'm_s', 'm_μ', 'm_u', 'm_d', 'm_e',
            'm_H', 'm_PG',
            'm_μ/m_e', 'm_τ/m_μ',
            'α⁻¹',
            'V_us', 'V_cb', 'V_ub',
            'Ω_Λ', 'Ω_Λ_approx', 'N_h',
            'D_H/L_P', 'M_P', 'G', 'ħ', 'L_P',
            'κ²',
            'm_ν3', 'm_ν2', 'm_ν1',
            'θ₁₂_PMNS', 'θ₁₃_PMNS', 'δ_CP_PMNS',
        }
        found = []
        for fid in known_ids:
            if fid in expr:
                found.append(fid)
        return found
    
    def get(self, formula_id: str) -> Optional[Formula]:
        """按 ID 查找公式"""
        return self.formulas.get(formula_id)
    
    def filter_by(self, **kwargs) -> list[Formula]:
        """按條件過濾公式"""
        results = list(self.formulas.values())
        for key, value in kwargs.items():
            if key == 'derivation_type':
                results = [f for f in results if f.derivation_type == value]
            elif key == 'status':
                results = [f for f in results if f.status == value]
            elif key == 'sector' and value:
                results = [f for f in results if f.parent and f.parent.sector == value]
            elif key == 'suspicious':
                results = [f for f in results if f.is_suspicious()]
        return results
    
    def find_consecutive_powers(self) -> list[Formula]:
        """找出所有連續冪次公式（擬合紅旗）"""
        # 從 audit 標記直接返回
        return [f for f in self.formulas.values() if f.audit.consecutive_powers]
    
    def impact_analysis(self, param_id: str) -> list[Formula]:
        """如果改某個參數，哪些公式會受影響？"""
        affected = []
        for formula in self.formulas.values():
            dependencies = self._dependencies_from_expression(
                formula.expression + ' ' + ' '.join(formula.derivation_path)
            )
            if param_id in dependencies:
                affected.append(formula)
        return affected
    
    def summary(self) -> dict:
        """摘要統計"""
        total = len(self.formulas)
        structural = len([f for f in self.formulas.values() if f.is_structural()])
        fitting = len([f for f in self.formulas.values() if f.derivation_type == 'fitting'])
        suspicious = len([f for f in self.formulas.values() if f.is_suspicious()])
        green = len([f for f in self.formulas.values() if f.status == '🟢'])
        yellow = len([f for f in self.formulas.values() if f.status == '🟡'])
        prediction = len([f for f in self.formulas.values() if f.status == '🔮'])
        
        sectors = {}
        for f in self.formulas.values():
            if f.parent and f.parent.sector:
                sectors[f.parent.sector] = sectors.get(f.parent.sector, 0) + 1
        
        return {
            'total': total,
            'structural': structural,
            'fitting': fitting,
            'suspicious': suspicious,
            'green': green,
            'yellow': yellow,
            'prediction': prediction,
            'sectors': sectors,
        }
    
    def verify_order(self) -> list[str]:
        """返回拓撲排序後的驗證順序"""
        try:
            return self.dag.topological_sort()
        except ValueError as e:
            print(f"⚠️  Dependency error: {e}")
            return list(self.formulas.keys())


# ═══════════════════════════════════════════════════════════════
# 3. Quick Test
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    registry = FormulaRegistry()
    
    print("=" * 60)
    print("IDCM FORMULA REGISTRY — LOADED")
    print("=" * 60)
    
    s = registry.summary()
    print(f"\nTotal formulas: {s['total']}")
    print(f"  🟢 Structural: {s['structural']}")
    print(f"  🟡 Fitting:    {s['fitting']}")
    print(f"  ⚠️  Suspicious: {s['suspicious']}")
    print(f"  🟢 Green:       {s['green']}")
    print(f"  🟡 Yellow:      {s['yellow']}")
    print(f"  🔮 Predictions: {s['prediction']}")
    print(f"\nSectors: {s['sectors']}")
    
    print("\nSuspicious formulas:")
    for f in registry.find_consecutive_powers():
        print(f"  🟡 {f.id}: {f.audit.suspicious_patterns}")
    
    print("\nTopological order (first 10):")
    order = registry.verify_order()
    for fid in order[:10]:
        print(f"  {fid}")
    
    print("\nImpact analysis: if φ changes, these formulas are affected:")
    affected = registry.impact_analysis('φ')
    for f in affected[:5]:
        print(f"  {f.id}")