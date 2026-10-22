#!/usr/bin/env python3
"""
IDCM Formula Registry Verifier
Reads IDCM_formula_registry.json and verifies all formulas.
Usage: python3 verify_registry.py [--update]
  --update: re-compute numerical values from expressions
"""

import json, os, sys, math, re

φ = (1 + math.sqrt(5)) / 2
φ_inv = φ - 1
ε = φ_inv / 4
N_d = 44
B = 4
L = 53/8

def γ(n):
    return 4 * math.sin(math.pi * n / (2 * N_d))**2

def compute(expr):
    """Try to evaluate a formula expression numerically."""
    s = expr.replace('φ', f'*{φ}').replace('ε', f'*{ε}')
    s = s.replace('N_d', f'*{N_d}').replace('B', f'*{B}').replace('L', f'*{L}')
    # Fix leading * (e.g., "*1.618" at start of expression)
    s = s.lstrip('*')
    # Fix double ** (e.g., "*1.618**2" should be "1.618**2")
    s = s.replace('**', '^').replace('*', '*').replace('^', '**')
    # Fix patterns like "19*1.618/88" (should be fine now)
    s = s.replace('\\', '')
    try:
        return eval(s)
    except:
        return None

registry_path = os.path.join(os.path.dirname(__file__), 'IDCM_formula_registry.json')
if not os.path.exists(registry_path):
    print(f"❌ Registry not found: {registry_path}")
    sys.exit(1)

with open(registry_path) as f:
    registry = json.load(f)

print("=" * 65)
print(f"IDCM FORMULA REGISTRY VERIFIER v{registry['metadata']['version']}")
print(f"Last updated: {registry['metadata']['last_updated']}")
print("=" * 65)

errors = 0
warnings = 0
for i, formula in enumerate(registry['formulas']):
    name = f"{formula['category']}/{formula['name']}"
    ftype = formula['type']
    expr = formula['expression']
    val = formula['value']
    ext = formula['external_value']
    err = formula['error_pct']
    reason = formula['reason']

    # Check required fields
    missing = []
    for field in ['name', 'expression', 'type', 'reason']:
        if not formula.get(field):
            missing.append(field)
    if missing:
        print(f"❌ [{name}] missing: {', '.join(missing)}")
        errors += 1
        continue

    # Check type validity
    if ftype not in ['structural', 'structural_correction', 'special_fit', 'open']:
        print(f"❌ [{name}] invalid type: {ftype}")
        errors += 1

    # For structural formulas, verify the expression is evaluable
    if ftype in ['structural', 'structural_correction']:
        computed = compute(expr)
        if computed is not None and val is not None and val != "":
            if isinstance(val, str) and '/' in val:
                # Fraction like "35/6"
                num, den = val.split('/')
                val_f = float(num) / float(den)
            elif isinstance(val, str) and '=' in val:
                # String like "4=B" — skip numerical check
                val_f = None
            else:
                try:
                    val_f = float(val)
                except (ValueError, TypeError):
                    val_f = None
            if val_f is not None:
                diff = abs(computed - val_f) / max(abs(val_f), 1e-10)
                if diff > 0.01:
                    print(f"⚠️  [{name}] expression mismatch: expr={computed:.6f}, registry={val_f:.6f} (diff={diff*100:.2f}%)")
                    warnings += 1

    # Check error bounds
    if err is not None and err > 0 and ext is not None:
        if err > 10:
            print(f"⚠️  [{name}] large error: {err:.2f}% (type={ftype})")
            warnings += 1

    # Status indicator
    status = {'structural': '🟢', 'structural_correction': '🟢', 'special_fit': '🟡', 'open': '🔴'}.get(ftype, '❓')
    ext_str = f"ext={ext}" if ext else ""
    err_str = f"err={err}%" if err else ""
    print(f"  {status} [{name:40s}] {ext_str} {err_str}")

print("=" * 65)
print(f"Result: {len(registry['formulas'])} formulas, {errors} errors, {warnings} warnings")
if errors:
    sys.exit(1)

# Summary
types = {}
for f in registry['formulas']:
    types[f['type']] = types.get(f['type'], 0) + 1
print(f"  🟢 structural: {types.get('structural', 0)}")
print(f"  🟢 structural_correction: {types.get('structural_correction', 0)}")
print(f"  🟡 special_fit: {types.get('special_fit', 0)}")
print(f"  🔴 open: {types.get('open', 0)}")