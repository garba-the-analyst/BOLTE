# 6-DOF Verification Cases (First Suite)

**Document ID:** HFPX-SIM-VCS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define and execute the first verification-case suite against the 6-DOF implementation (HFPX-SIM-SIX-002) with proposed tolerances — the first concrete step toward 19.15 registration. Cases verify implementation, not validity.

## 2. Scope

Five cases (VC6-001…005) against code revision of 2026-09-29. Authority-data comparison, tolerance approval, and register entry are out of scope (TBD).

## 3. Applicable Documents

- HFPX-SIM-SIX-002 (implementation under case); HFPX-SIM-VER-001 (register rule; MMV-002/003)
- HFPX-VV-PLN-001 (VVP-005 acceptance criteria before execution — tolerances proposed here, approval TBD)
- Runner: `run_verification_cases()` in `19_SIMULATION/hfpx_sixdof.py`; verdicts: `demo/verification_cases.csv`

## 4. Definitions & Acronyms

- Proposed tolerance (TBC): acceptance threshold used for this run; requires approval before it can gate anything
- Implementation evidence: proof the code does what 06.11 says — not proof the model represents HFP-X

## 5. System Context

```text
CODE REV → CASES (this doc) → VERDICTS (CSV) → TOLERANCE APPROVAL (TBD) → AUTHORITY COMPARISON (TBD) → REGISTER (TBD)
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VSX-001 | Verification cases VC6-001…005 shall be defined with objective, configuration, proposed tolerance and authority (analytic/independent-code for this suite). | REQ-HFPX-MMV-002 | Inspection |
| REQ-HFPX-VSX-002 | Case verdicts shall be recorded per code revision with values and tolerances; reruns required on any code change. | REQ-HFPX-MMV-002 | Demonstration |
| REQ-HFPX-VSX-003 | Proposed tolerances (1e-4 m analytic match; 1e-6 m hover drift; 1e-12 quaternion error; 1e-6 energy drift; 0.5 m cross-check) shall be approved before gating use. | REQ-HFPX-MMV-003 | Inspection |
| REQ-HFPX-VSX-004 | Register entry for the 6-DOF core additionally requires authority-data comparison beyond this suite (criteria TBD). | REQ-HFPX-MMV-004 | Inspection |

## 7. Architecture

Suite: VC6-001 free-fall analytic match; VC6-002 hover-hold drift; VC6-003 quaternion norm; VC6-004 energy drift; VC6-005 independent-Euler cross-check.

## 8. Detailed Design

Run record 2026-09-29 (all PASS, values vs proposed tolerances): VC6-001 8.882e-14 ≤ 1e-4; VC6-002 0.000e+00 ≤ 1e-6; VC6-003 0.000e+00 ≤ 1e-12; VC6-004 1.397e-14 ≤ 1e-6; VC6-005 4.903e-02 ≤ 0.5. Verdicts in `demo/verification_cases.csv`. One defect found and fixed during suite development (VC6-004 normalisation by zero initial energy → energy-scale normalisation), recorded here as process evidence.

## 9. Interfaces

- To 19.15 register: this suite is necessary but not sufficient input
- To code config: rerun mandated on change (HFPX-SIM-SIX-002 §19)

## 10. Operational Concept

Define cases → propose tolerances → execute → record → approve tolerances → compare against authority data → register. This revision completes the first four steps.

## 11. Safety

No safety use: passing implementation cases says nothing about authority, handling, or clearance. 19.15 bars safety reliance until registration.

## 12. Performance

Suite runtime negligible (seconds). Coverage: core integrator + attitude + conservation + independence; input-family verification NOT covered (all TBD).

## 13. Verification & Validation

This document verified by inspection (cases defined, tolerances proposed, verdicts recorded, rerun rule set). Validation: gate approval of tolerances and authority-data plan.

## 14. Risks

- PASS verdicts mistaken for model validity; mitigation: VC6-004 register rule + UNVERIFIED status + file-header warnings
- Tolerance approval rubber-stamped; mitigation: independent review action (owner TBD)

## 15. Open Issues

Tolerance approval TBD. Authority-data comparison TBD. Register mechanism/entry TBD. Input-family cases TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on code revision control, 19.15 methodology, VVP-005, and future authority data (test).

## 18. Traceability

Parents: MMV-002/003/004, VVP-005, MSX-010..014. Children: tolerance approval, authority comparison, register entry. RTM: REQ-HFPX-VSX-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. New code revision re-opens verdicts.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | First 6-DOF verification-case suite (Tranche 8; 5/5 PASS, tolerances TBC) |
