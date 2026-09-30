#!/usr/bin/env python3
"""
HFP-X first-issue mass / thrust / energy budgets (Issue 1).
=============================================================
Document : HFPX-AERO-BDG-001 (budgets computed here, recorded there)
Status   : CONCEPT — reference-class illustration, NOT a design baseline.

METHOD
  Every number below carries a basis tag:
    PUBLISHED  — authoritative source (fuel LHV, manufacturer specs)
    REF-CLASS  — published reference-system value, TBC for HFP-X
    OPERATOR   — operator-defined input (pilot mass), not a design value
    TBD        — no basis; carried as TBD, never filled by guessing
  Hover: T = W. Fuel flow from published reference SFC (TJ100-class,
  0.116 kg/N/h at max thrust — TBC for HFP-X modules). Endurance =
  fuel mass / fuel flow. Cruise: drag TBD -> no endurance result;
  formula and data needs recorded instead.
"""

import csv
from pathlib import Path

G = 9.80665
OUT = Path(__file__).parent / "budgets"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- inputs
P = {
    # published
    "lhv_jet":   (42.8,  "MJ/kg", "PUBLISHED (ASTM D1655 min; AFQRJOS)"),
    "sfc_ref":   (0.116, "kg/N/h", "PUBLISHED (PBS TJ100 max-thrust SFC; REF-CLASS for HFP-X)"),
    "tj40_thrust": (395.0, "N", "PUBLISHED (PBS TJ40)"),
    "tj40_mass": (3.3,   "kg", "PUBLISHED (PBS TJ40)"),
    "gravity_sys": (27.0, "kg", "PUBLISHED (Gravity suit system mass, REF-CLASS)"),
    "gravity_thrust": (144 * G, "N", "PUBLISHED (~144 kgf total, REF-CLASS)"),
    # reference-class / operator (TBC, not design values)
    "pilot_lo": (75.0, "kg", "OPERATOR INPUT (TBC)"),
    "pilot_hi": (95.0, "kg", "OPERATOR INPUT (TBC)"),
    "fuel_lo":  (8.0,  "kg", "REF-CLASS (TBC; Gravity-class fuel load order)"),
    "fuel_hi":  (15.0, "kg", "REF-CLASS (TBC)"),
    "n_modules": (5,   "count", "REF-CLASS layout (TBC; geometry TBD)"),
}

rows_mass = [
    ("Pilot", P["pilot_lo"][0], P["pilot_hi"][0], "kg", P["pilot_lo"][2], "TBC"),
    ("Propulsion modules (5x TJ40-class, dry)", 5 * P["tj40_mass"][0], 5 * P["tj40_mass"][0], "kg", "REF-CLASS (TBC)", "TBC"),
    ("Airframe / lifting structure", None, None, "kg", "No basis (ISS-004 open)", "TBD"),
    ("Avionics / compute / sensors", None, None, "kg", "No basis", "TBD"),
    ("Helmet / HMI / suit", None, None, "kg", "No basis", "TBD"),
    ("Reference-class hardware subtotal (excl. pilot/fuel)", P["gravity_sys"][0], 40.0, "kg", "REF-CLASS (Gravity 27 kg; upper bound TBC)", "TBC"),
    ("Fuel load", P["fuel_lo"][0], P["fuel_hi"][0], "kg", P["fuel_lo"][2], "TBC"),
]
m_lo = P["gravity_sys"][0] + P["pilot_lo"][0] + P["fuel_lo"][0]
m_hi = 40.0 + P["pilot_hi"][0] + P["fuel_hi"][0]
rows_mass.append(("LIFTOFF MASS (reference-class rollup)", round(m_lo, 1), round(m_hi, 1), "kg", "Derived (this script)", "TBC"))

t_lo, t_hi = m_lo * G, m_hi * G
t_avail = P["n_modules"][0] * P["tj40_thrust"][0]
rows_thrust = [
    ("Hover thrust required (= liftoff weight)", round(t_lo, 0), round(t_hi, 0), "N", "Derived: T = W", "TBC"),
    ("Thrust available (5x TJ40-class, REF-CLASS)", t_avail, t_avail, "N", P["tj40_thrust"][2], "TBC"),
    ("Hover T/W (REF-CLASS check)", round(t_avail / t_hi, 2), round(t_avail / t_lo, 2), "-", "Derived", "TBC"),
    ("Per-module mean thrust (hover, even split TBD)", round(t_lo / 5, 0), round(t_hi / 5, 0), "N", "Derived (allocation TBD per 07.16)", "TBC"),
    ("T/W margin policy", None, None, "-", "TBD (07.17 authority budgets)", "TBD"),
    ("Transition thrust requirement", None, None, "N", "TBD (needs 6-DOF corridor, ISS-006)", "TBD"),
]

ff_lo = P["sfc_ref"][0] * t_lo      # kg/h
ff_hi = P["sfc_ref"][0] * t_hi
e_lo = P["fuel_lo"][0] * P["lhv_jet"][0]
e_hi = P["fuel_hi"][0] * P["lhv_jet"][0]
end_lo = P["fuel_lo"][0] / ff_hi * 60   # min (worst combo)
end_hi = P["fuel_hi"][0] / ff_lo * 60   # min (best combo)
rows_energy = [
    ("Fuel energy carried", round(e_lo, 0), round(e_hi, 0), "MJ", "Derived: m_fuel x 42.8", "TBC"),
    ("Hover fuel flow (REF-CLASS SFC)", round(ff_lo, 1), round(ff_hi, 1), "kg/h", "Derived: SFC x T_hover", "TBC"),
    ("Hover endurance (REF-CLASS)", round(end_lo, 1), round(end_hi, 1), "min", "Derived: fuel / flow", "TBC"),
    ("Cruise drag", None, None, "N", "TBD (06.5/06.6)", "TBD"),
    ("Cruise endurance", None, None, "min", "TBD (needs drag + installed SFC)", "TBD"),
    ("Battery-electric 5-min hover pack (sanity)", "~700", "~1000", "kg", "Derived: ~65 kWh @ ~150-200 Wh/kg pack (trade study)", "REF-CLASS"),
]

for name, rows in [("mass_budget.csv", rows_mass), ("thrust_budget.csv", rows_thrust), ("energy_budget.csv", rows_energy)]:
    with (OUT / name).open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["Budget line", "Low", "High", "Unit", "Basis", "Status"])
        w.writerows(rows)

print("FIRST-ISSUE BUDGET SUMMARY (reference-class, TBC — not a baseline)")
print(f"  Liftoff mass : {m_lo:.0f}-{m_hi:.0f} kg")
print(f"  Hover thrust : {t_lo:.0f}-{t_hi:.0f} N  |  available (5xTJ40-class): {t_avail:.0f} N")
print(f"  Hover T/W    : {t_avail/t_hi:.2f}-{t_avail/t_lo:.2f}")
print(f"  Fuel flow    : {ff_lo:.0f}-{ff_hi:.0f} kg/h  |  endurance ({P['fuel_lo'][0]:.0f}-{P['fuel_hi'][0]:.0f} kg fuel): {end_lo:.1f}-{end_hi:.1f} min")
print(f"  Cruise       : TBD (drag TBD)")
print(f"Wrote {OUT}/mass_budget.csv, thrust_budget.csv, energy_budget.csv")
