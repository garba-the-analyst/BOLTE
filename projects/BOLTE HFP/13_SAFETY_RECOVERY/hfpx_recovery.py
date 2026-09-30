#!/usr/bin/env python3
"""
HFP-X recovery feasibility parametrics (ISS-008 attack, first analysis).
========================================================================
Document : HFPX-SAFE-FSB-001 (analysis recorded there)
Status   : CONCEPT — parametric exploration, NOT a feasibility claim.

METHOD
  Textbook steady-descent physics with SWEPT inputs; every input is
  TBD, reference-class TBC, or published standard atmosphere:
    Vt = sqrt(2*W / (rho * Cd * A))      steady descent rate
    d_stop = Vt^2 / (2*a)                constant-decel stop distance
    h_min  = h_detect + Vt*(t_decide + t_deploy + t_inflate) + d_stop
  No canopy selected. No timeline allocated. No tolerance asserted.
  Outputs are DATA NEEDS (what must be measured/decided), not answers.
"""

import csv
import math
from pathlib import Path

OUT = Path(__file__).parent / "recovery_parametrics"
OUT.mkdir(exist_ok=True)

G = 9.80665
RHO = 1.225  # kg/m^3, ISA sea level (PUBLISHED standard; site TBD)

# Basis-tagged inputs
W_LO, W_HI = 1079.0, 1471.0   # N, hover weight range (TBC, from first-issue budgets)
CD_LO, CD_HI = 1.3, 1.7       # REF-CLASS TBC (parachute-type decelerators; canopy TBD)
AREAS = [20, 30, 40, 60, 80]  # m^2 swept (PARAMETRIC — no selection)
A_ALLOW = [3 * G, 5 * G, 8 * G]  # m/s^2 swept (PARAMETRIC — tolerance TBD, NOT asserted survivable)
T_FIXED = [0.5, 1.0, 2.0, 4.0]   # s timeline placeholders swept (allocations TBD)

with (OUT / "descent_rate_vs_area.csv").open("w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["Canopy area m2", "Vt_lo (m/s)", "Vt_hi (m/s)", "Cd", "Basis", "Status"])
    for A in AREAS:
        for Cd in (CD_LO, CD_HI):
            vt_lo = math.sqrt(2 * W_LO / (RHO * Cd * A))
            vt_hi = math.sqrt(2 * W_HI / (RHO * Cd * A))
            w.writerow([A, round(vt_lo, 2), round(vt_hi, 2), Cd, "Vt=sqrt(2W/rho Cd A); W TBC; Cd REF-CLASS TBC", "PARAMETRIC"])

with (OUT / "min_altitude_vs_timeline.csv").open("w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["Vt (m/s)", "Fixed timeline (s)", "Decel (m/s2)", "d_stop (m)", "h_min (m)", "Basis", "Status"])
    for Vt in (5.0, 7.5, 10.0, 12.5):      # swept outcomes, not requirements
        for tf in T_FIXED:
            for a in A_ALLOW:
                d = Vt ** 2 / (2 * a)
                h = Vt * tf + d
                w.writerow([Vt, tf, round(a / G, 1 + 0), round(d, 1), round(h, 1),
                            "h=Vt*t+d; d=Vt^2/2a; timeline+decel PARAMETRIC", "PARAMETRIC"])

print("RECOVERY PARAMETRICS (ISS-008 first analysis — data needs, not answers)")
for A in AREAS:
    vt = math.sqrt(2 * ((W_LO + W_HI) / 2) / (RHO * 1.5 * A))
    print(f"  area {A:3d} m2 -> Vt ~ {vt:.1f} m/s (mid-weight, Cd 1.5 REF-CLASS TBC)")
print("Hover (0 m AGL) implication: ANY parachute-type recovery needs deployment "
      "altitude it does not have — recorded as the limiting-case finding (TBD-gated).")
print(f"Wrote {OUT}/descent_rate_vs_area.csv, min_altitude_vs_timeline.csv")
