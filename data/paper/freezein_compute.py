#!/usr/bin/env python3
"""
⚠️ DEPRECATED — Use freezein_warp_corrected.py instead ⚠️

This script uses bare coupling y4 WITHOUT warp factor suppression.
Key difference:
  freezein_compute.py (this file):         y4 = 3.56e-7 (bare)        -> Omega = 136,380  ❌
  freezein_warp_corrected.py (corrected):  y_eff = y4 x e-12 = 2.19e-12 -> Omega = 0.065  ✅

Warp factor e-12 = e^{-A(rc)} from SAME 5D geometry as P3 mass e-36.
P4 wavefunction UV-localized, Higgs zero-mode IR-localized -> overlap suppressed.
"""
import math

# ============================================================
# 1. IDCM Fundamental Constants
# ============================================================