# Automatic Stabilisation

**Document ID:** HFPX-SAFE-AST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the independent automatic stabilisation function (Vol 13.10): its separation from primary FCS, engagement/disengagement criteria, stabilisation envelope, and fault-injection verification approach.
This document owns requirements, architecture, interfaces, and test methodology only.

## 2. Scope

Covers stabilisation-function definition, independence from primary FCS, engagement/disengagement logic (criteria TBD), hover-first envelope scoping (bounds TBD), and SIL/HIL/unmanned-test verification methodology.
Hover/low-altitude is the limiting case and the first envelope in scope (quantification TBD).
Out of scope: primary FCS laws (Vol 06/07), airframe/aero implementation (Vol 03), and test execution (Vol 23).

## 3. Applicable Documents

- SYS-003; ARC-003/SFA-001 (architecture/safety-function allocation — stubs, details TBD); FFT-005 (flight-test basis — stub, scope TBD)
- HFPX-SAFE-CAS-001 Safety Case; FHA/FMEA stabilisation hooks (Vol 13.4/13.5, values TBD)
- HFPX-VV-PLN-001 V&V Plan; HFPX-PGM-SEM-001 SEMP (gating)

## 4. Definitions & Acronyms

- Automatic stabilisation function: safety-path function that bounds attitude/rates when primary control is degraded or absent; authority and limits TBD.
- Independent of primary FCS: functionally and to a degree TBD physically separate from primary flight control (compute, sensing, actuation separation TBD).
- Engagement/disengagement criteria: conditions for stabilisation takeover and return of authority; thresholds, latencies, and handover logic TBD.
- Stabilisation envelope: flight conditions within which stabilisation is specified; bounds TBD, hover-first.
- Fault-injection verification: deliberate insertion of FCS/sensor/actuation faults in SIL/HIL/unmanned test to exercise engagement; fault set and pass criteria TBD.

## 5. System Context

Automatic stabilisation is a safety-path function, not a backup primary FCS: it bounds divergence to preserve the possibility of a subsequent safe-state or recovery action.
It constrains FCS/sensing/actuation segregation without implementing flight control; allocation flows via ARC-003/SFA-001.
Recovery effectiveness is unproven (ISS-008); stabilisation claims no recovery outcome in this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-AST-001 | The system shall provide an automatic stabilisation function independent of the primary FCS, with independence criteria TBD. | SYS-003, ARC-003/SFA-001 | Analysis |
| REQ-HFPX-AST-002 | The system shall define engagement and disengagement criteria for automatic stabilisation, with all thresholds, latencies, and handover logic TBD. | SYS-003 | Analysis |
| REQ-HFPX-AST-003 | The system shall define the stabilisation envelope, addressed hover-first, with all bounds TBD. | SYS-003, FFT-005 | Analysis |
| REQ-HFPX-AST-004 | Automatic stabilisation shall be verified by fault-injection SIL/HIL and unmanned test, with fault set, environments, and pass criteria TBD. | SYS-003, FFT-005 | Test |

## 7. Architecture

Stabilisation architecture (details TBD): independent sensing/compute/actuation path TBD, takeover logic TBD, annunciation to crew/operator TBD.
Segregation TBD: separation from primary FCS at sensing, compute, power, and actuation layers (SAD to allocate per ARC-003/SFA-001).
Authority TBD: which axes and effectors stabilisation may command, and saturation/priority rules TBD.

## 8. Detailed Design

Engagement logic is a stub in this revision (criteria TBD, no thresholds baselined).
Methodology only: fault taxonomy → engagement trigger → bounded stabilisation law (gains TBD) → disengagement/handover; stability and robustness methods TBD (Vol 19 support).
No control-law values, gains, or sensor selections are made in this revision.

## 9. Interfaces

- AST ↔ Primary FCS (Vol 06/07): takeover/return signalling and authority arbitration; protocols and latencies TBD.
- AST ↔ Sensing/actuation (Vol 06/03 as applicable): independent or shared paths per segregation TBD; interface integrity TBD.
- AST ↔ Alerts/procedures (Vol 10, Vol 13.8): engagement annunciation and crew/operator visibility TBD.
- AST ↔ EPM/recovery (Vol 13.9/13.11): handover to propulsion-management or recovery threads; sequencing TBD.

## 10. Operational Concept

Stabilisation sequence (methodology only): detect qualifying condition (criteria TBD) → engage automatically → bound attitude/rates within envelope TBD → disengage or hand over per logic TBD.
This concept defines engagement allocation and handover only; it does not direct vehicle handling or flight conduct (owned and gated under Vol 23/CONOPS).
Hover-first emphasis: hover/low-altitude engagement is specified and verified before envelope expansion (scope TBD).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, architecture, interfaces, and test methodology only; it contains no propulsion build, ignition, or operation instructions.
Independence (ARC-003/SFA-001) is a safety claim to be verified, not assumed: common-cause potential with primary FCS is analysed under Vol 13.7 (scope TBD).
Recovery effectiveness is unproven (ISS-008): stabilisation asserts no safe-state or recovery outcome until verified per REQ-HFPX-AST-004 (criteria TBD).
Hover/low-altitude is the limiting case for engagement validation.

## 12. Performance

Stabilisation performance measures TBD with no thresholds baselined: engagement latency TBD, attitude/rate bounds TBD, sustain duration TBD, disengagement transients TBD.
All thresholds, timings, and envelope bounds TBD; no numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-AST-001 verified by Analysis of independence against ARC-003/SFA-001 allocation (criteria TBD).
- REQ-HFPX-AST-002 verified by Analysis of engagement/disengagement criteria, supported by sim (coverage TBD).
- REQ-HFPX-AST-003 verified by Analysis of envelope definition against FFT-005 test basis (bounds TBD).
- REQ-HFPX-AST-004 verified by Test: fault-injection SIL/HIL plus unmanned test; fault set, environments, and pass criteria TBD; human-flight credit gated on closure (criteria TBD).
- Validation is gate review plus Safety Review Board concurrence (scope TBD).

## 14. Risks

- Common-cause coupling with primary FCS defeating independence; mitigation: CCA scope TBD plus segregation analysis.
- Engagement-gap: qualifying condition outside the TBD envelope or missed trigger; mitigation: fault-injection coverage analysis, fault set TBD.
- Unproven effectiveness treated as recovery (ISS-008); mitigation: explicit unproven status and gated-test requirement enforced at reviews.

## 15. Open Issues

Independence criteria and segregation TBD. Engagement/disengagement thresholds, latencies, and handover logic TBD. Stabilisation envelope bounds TBD. Fault-injection set, SIL/HIL environments, and pass criteria TBD. Unmanned-test scope TBD. Human-flight gating criteria TBD. ISS-008 applies to all stabilisation effectiveness claims.

## 16. Assumptions

- A-AST-001: A functionally independent stabilisation path is architecturally feasible within mass/power/complexity budgets TBD; validation: SAD allocation (TBD).
- A-AST-002: Hover/low-altitude bounds stabilisation design for early flight; validation: Vol 13 analysis and Vol 19 modelling (both TBD).
- A-AST-003: SIL/HIL plus unmanned test adequately represent engagement conditions for verification purposes; validation: Vol 23 test adequacy review (TBD).

## 17. Dependencies

Depends on SYS-003, ARC-003/SFA-001 (allocation), FFT-005 (test basis), Vol 06/07 (FCS context), Vol 03 (effector context), Vol 10/13.8 (annunciation/procedures), Vol 13.4/13.5/13.7 (hazard/CCA hooks), Vol 19 (modelling), SEMP/V&V Plan (gates/discipline), Vol 23 (test execution).

## 18. Traceability

Parents: SYS-003, ARC-003/SFA-001, FFT-005. Children: engagement criteria, envelope definition, and fault-injection cases (artefact IDs TBD).
RTM: REQ-HFPX-AST-001..004 → CONCEPT. Each engagement criterion traces to at least one fault-injection case; each envelope bound traces to analysis or test evidence TBD (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Engagement criteria and envelope definitions are under document control once populated; changes via change records with affected-condition impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (automatic stabilisation; Ch 13.10) |
