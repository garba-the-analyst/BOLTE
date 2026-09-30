# 6-DOF Implementation Record (Code + Smoke Tests)

**Document ID:** HFPX-SIM-SIX-002  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 7 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Record the first 6-DOF code implementation of the 06.11 equation structure, its smoke-test results, and — explicitly — its unverified status. This document implements structure; it verifies nothing.

## 2. Scope

Covers `19_SIMULATION/hfpx_sixdof.py` (rigid-body core, RK4, plug-in force models, demo harness) and the 2026-09-29 smoke-test run. Excludes aerodynamic/propulsion data (still TBD), verification cases (19.15), and any gate use.

## 3. Applicable Documents

- HFPX-AERO-SIX-001 (06.11 structure implemented here); HFPX-SIM-SIX-001 (19.3 ownership)
- HFPX-SIM-VER-001 (19.15 — register rule applied here: this revision is UNREGISTERED)
- HFPX-VV-PLN-001; code run log §8

## 4. Definitions & Acronyms

- Smoke test: implementation check (code runs, math sane) — explicitly NOT model verification
- UNVERIFIED: absent from the verified-model register; barred from gate decisions per MMV-005

## 5. System Context

```text
06.11 STRUCTURE → THIS CODE (structure only) → 19.15 CASES (TBD) → REGISTER (TBD) → GATE USE (barred until then)
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MSX-010 | The 6-DOF core shall implement flat-Earth rigid-body equations with NED position, body velocity, unit quaternion attitude and body rates, integrated by RK4 with quaternion renormalisation. | REQ-HFPX-ASX-001 | Demonstration |
| REQ-HFPX-MSX-011 | Force/moment sources shall be plug-in callbacks defaulting to zero, with gravity computed from attitude and mass; no aerodynamic or propulsion data shall be embedded. | REQ-HFPX-ASX-002 | Inspection |
| REQ-HFPX-MSX-012 | Demo parameters and trajectories shall be labelled illustrative-only and quarantined from design data paths. | REQ-HFPX-ASX-005 | Inspection |
| REQ-HFPX-MSX-013 | This implementation shall be recorded as UNVERIFIED and barred from gate decisions, authority claims and clearances until 19.15 registration. | REQ-HFPX-ASX-004 | Inspection |
| REQ-HFPX-MSX-014 | Smoke tests shall cover free-fall analytic match, hover hold, finite-run scripted sweep, and Jacobian finiteness; results recorded per run. | REQ-HFPX-MSX-003 | Demonstration |

## 7. Architecture

Single module, no dependencies beyond numpy: `SixDOF` core (derivatives/step/simulate), quaternion/DCM utilities, `DEMO` dict, `_run_checks()` harness, `demo/` output folder.

## 8. Detailed Design

Run record 2026-09-29 (`python3 19_SIMULATION/hfpx_sixdof.py`, all PASS): free-fall 2 s down = 19.613300 m vs analytic 19.613300 m; hover hold 5 s drift 0.00e+00 m, quaternion error 0.00e+00; scripted 60° tilt sweep 10 s finite, trajectory in `demo/tilt_sweep_demo.csv`; Jacobian finite, max|Re(ev)| = 0.000 (bare airframe, no aero/control — expected, not a stability finding). Demo config: mass 130 kg, inertia diag(12, 14, 9) kg·m², dt 0.005 s — ILLUSTRATIVE ONLY.

## 9. Interfaces

- Consumes: 06.11 structure (implemented), input-data families (all TBD → zero plug-ins active in tests except scripted thrust)
- Supplies: nothing to gates (barred); trajectory CSV available for inspection only

## 10. Operational Concept

Implement → smoke-test → record here → submit to 19.15 cases (TBD) → register → only then gate use. This revision completes the first two steps.

## 11. Safety

No safety claim is made or implied: hover-hold arithmetic is not controllability evidence (ISS-006 stands); tilt sweep is scripted kinematics, not a controller. 19.15 bars safety use until registration.

## 12. Performance

Runtime performance TBD (not measured for record). Numerical accuracy: free-fall agreement to 1e-6 m at dt 0.005 s RK4.

## 13. Verification & Validation

Code verified by the recorded smoke-test run (implementation checks). MODEL verification (19.15 cases, authority data, tolerances, register) is entirely TBD — this document is evidence of implementation, not of validity.

## 14. Risks

- Demo outputs mistaken for HFP-X predictions; mitigation: MSX-012 labelling + MSX-013 bar + file-header warning
- Plug-in zeros mistaken for modelled physics; mitigation: MSX-011 default-zero rule stated in code and here

## 15. Open Issues

19.15 cases TBD. Input-data families TBD. Register mechanism TBD. ISS-006/007 model-evidence actions in progress, not closed.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on 06.11 structure, 19.3 ownership, 19.15 methodology, and numpy runtime.

## 18. Traceability

Parents: ASX tier, MSX-001..005, MMV tier. Children: 19.15 verification cases against this revision. RTM: REQ-HFPX-MSX-010..014 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 7 draft, CONCEPT, not baselined. Code revision controlled with this document; any code change re-runs smoke tests and revises §8.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | First 6-DOF implementation record (Tranche 7; code + smoke tests, UNVERIFIED) |
