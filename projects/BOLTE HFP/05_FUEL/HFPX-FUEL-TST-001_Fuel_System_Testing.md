# Fuel System Testing (Chapter 05.16)

**Document ID:** HFPX-FUEL-TST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the fuel system testing requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure: rig-to-integrated test thread, pass/fail provision, data-capture provision, and the flight-credit rule; procedures and criteria are TBD.

## 2. Scope

Covers Chapter 05.16 Fuel System Testing: test thread from rig to integrated testing, pass/fail criteria provision, data capture, and flight-credit gating. Test procedures, articles, facilities, criteria, and detailed planning are TBD in Vol 22/33.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, handling, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. All fuel testing occurs only under controlled conditions with approved procedures per Vol 13 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- HFPX-SYS-ARC-001 SAD (test-article allocation, TBD)
- Vol 22 V&V Plan (not written; owns cases); Vol 33 Test (controlled conditions)
- Vol 13 Safety analyses (test safety controls)
- Fuel chapters 05.3–05.15, 05.17 (test subjects, Tranche 4 drafts where applicable)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FTS: fuel test thread; requirement IDs `REQ-HFPX-FTS-001..004`
- Test thread: ordered progression from rig to integrated testing (stages TBD)
- Pass/fail: acceptance criteria for each test (TBD)
- Data capture: recorded evidence from tests (contents TBD)
- Flight credit: use of test evidence toward flight authorisation (gated; criteria TBD)
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Fuel testing threads subjects through progressive integration:

```text
RIG (components/subassemblies, TBD) → INTEGRATED (fuel system / vehicle, TBD) → EVIDENCE → FLIGHT-CREDIT GATE (TBD)
   procedures TBD, controlled conditions         procedures TBD, controlled conditions
```

This chapter states testing requirements; test plans, procedures, and approvals live in Vol 22/33. Allocation of test articles and facilities is TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FTS-001 | The programme shall test the fuel system through a thread from rig to integrated testing under controlled conditions (procedures TBD). | FRQ tier (TBD), REQ-HFPX-SYS-006 | Test |
| REQ-HFPX-FTS-002 | Each fuel system test shall define pass/fail criteria to be determined (TBD). | SCA-006, SAF tier (TBD) | Inspection |
| REQ-HFPX-FTS-003 | Each fuel system test shall capture data to be determined (TBD). | SCA-006, FRQ tier (TBD) | Inspection |
| REQ-HFPX-FTS-004 | Fuel system test evidence shall receive flight credit only through a gated evidence process (gate criteria TBD). | REQ-HFPX-SYS-003, SCA-006 | Analysis |

No procedure, criterion, data item, facility, or gate value in this document is approved; all are TBD.

## 7. Architecture

Logical allocation (starter — SAD / Vol 22 own authoritative allocation): rig stages (TBD) → integration stages (TBD) → evidence repository (TBD) → flight-credit gate (TBD). Test-article fidelity, simulant use, instrumentation, and facility allocation are TBD. No rig, facility, or article is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No test procedure, rig design, instrumentation design, or facility drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs / Vol 22, all TBD): test-article interfaces (fuel, power, data); facility interfaces (range, safety systems, GSE); instrumentation/data interfaces (capture, storage, access); evidence interface to Safety Case and flight-authorisation process; environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Tests are executed as V&V threads; each requirement maps to ≥1 test case (mapping TBD in V&V Plan). This document prescribes no test procedure, handling step, or operating instruction — it requires that procedures exist and be approved. All fuel testing occurs only under controlled conditions with approved procedures, range, and safety controls.

## 11. Safety

Test hazards (including live-fuel hazards) are controlled via Vol 13 analyses and Vol 22/33 safety controls; this chapter generates no standalone safety claim and no authorisation to test. REQ-HFPX-FTS-004 gates flight credit on evidence to protect the SYS-003 safety path. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Test coverage, fidelity, throughput, envelope, and gate thresholds are TBD pending architecture, safety targets, and V&V planning. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: inspection (pass/fail and data-capture provisions, procedure existence) → test (thread execution, controlled conditions) → analysis (flight-credit gate closure). Requirements without a verification method are rejected at SRR.

## 14. Risks

- Procedures and criteria defined late → tests ungated → mitigation: pass/fail and data-capture requirements retained as provisions
- Rig-to-integrated thread incomplete → gaps in evidence → mitigation: explicit thread requirement, V&V coverage gate
- Premature flight credit → mitigation: REQ-HFPX-FTS-004 gated-evidence rule

## 15. Open Issues

- Rig and integration stages, articles, facilities, simulants (all TBD)
- Pass/fail criteria and data-capture contents per test (TBD)
- Flight-credit gate criteria, authority, evidence standard (TBD)

## 16. Assumptions

- A-TBD: A rig-to-integrated fuel test thread with gated flight credit is required regardless of final architecture; validation: SRR review
- No assumption is made about test stages, procedures, criteria, data, or gates in this revision

## 17. Dependencies

Depends on fuel architecture test subjects (05.3–05.15, 05.17), V&V planning (Vol 22), test execution and safety controls (Vol 33, Vol 13), and Safety Case evidence needs (SAF tier, SCA-006). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006 (table above). Children: Vol 22 cases, Vol 33 procedures, evidence records, RTM rows. RTM seed for REQ-HFPX-FTS-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Procedure approval, criterion approval, or gate definition requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.16; HFPX-FUEL-TST-001) |
