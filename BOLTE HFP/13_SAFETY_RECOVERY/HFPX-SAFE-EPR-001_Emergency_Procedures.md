# Emergency Procedures

**Document ID:** HFPX-SAFE-EPR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X emergency-procedure framework (Vol 13.8): emergency-state definitions, crew/operator actions, procedure-to-alert mapping, and validation approach.
This document owns procedure requirements, allocation, and validation methodology only; it contains no propulsion build, ignition, or flight-operation instructions.

## 2. Scope

Covers emergency-state taxonomy, crew/operator action threads aligned to the CONOPS off-nominal thread, mapping of procedures to Vol 10.11/10.12 alerts, and rehearsal/demo validation methodology.
Hover/low-altitude is treated as the limiting case for procedure timing and effectiveness (quantification TBD).
Out of scope: detailed FCS logic (Vol 06/07), alert implementation (Vol 10), recovery hardware design (Vol 13.11–13.13), and test execution (Vol 23).

## 3. Applicable Documents

- CON-002, CON-004; OPC-004 (CONOPS off-nominal and operator-action basis — stubs, details TBD)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13.2–13.7 hazard analyses (parents for procedure triggers, values TBD)
- Vol 10.11/10.12 alerting and caution/warning definitions (alert sources, thresholds TBD)
- HFPX-PGM-SEM-001 SEMP (gating); HFPX-VV-PLN-001 V&V Plan (verification discipline)

## 4. Definitions & Acronyms

- Emergency state: a declared system/operational condition requiring a prescribed crew/operator response; entry/exit criteria TBD.
- CONOPS off-nominal thread: the CONOPS branch governing off-nominal and emergency conduct; owned by CON-002/CON-004, details TBD.
- Procedure-to-alert mapping: trace from each emergency procedure to the alert(s) that announce its entry condition; alert thresholds and latencies TBD.
- Rehearsal/demo: human-in-the-loop procedure execution in sim or ground demonstration to validate usability; pass criteria TBD.
- Human-procedures gate: no human-flight credit for a procedure until rehearsal/demo closure TBD and authorised at FRR (criteria TBD).

## 5. System Context

Emergency procedures sit between alerting (Vol 10), safety architecture (Vol 13.1–13.7), and operations (CONOPS/Vol 12/Vol 23): alerts announce, procedures direct, safety analyses justify coverage.
Hover/low-altitude bounds procedure design because available decision and execution time is most constrained there (quantification TBD).
Recovery effectiveness is unproven (ISS-008); procedures that terminate in a recovery action claim no effectiveness in this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-EPR-001 | The system shall define emergency states with entry criteria and exit criteria, with all criteria values TBD. | CON-002 | Inspection |
| REQ-HFPX-EPR-002 | The crew/operator shall have a defined action for each emergency state, consistent with the CONOPS off-nominal thread, with sequencing and responsibilities TBD. | CON-004, OPC-004 | Demonstration |
| REQ-HFPX-EPR-003 | Each emergency procedure shall map to the alert(s) that initiate it, traceable to Vol 10.11/10.12 alert definitions, with alert thresholds and latencies TBD. | OPC-004 | Analysis |
| REQ-HFPX-EPR-004 | Each emergency procedure shall be validated by rehearsal and/or demonstration, and no human-flight credit shall be claimed for a human-executed procedure before gated closure, with methods and criteria TBD. | CON-004 | Demonstration |

## 7. Architecture

Procedure architecture (details TBD): emergency-state taxonomy owned here, procedure flows allocated to crew/operator/automation roles TBD, alert linkage owned jointly with Vol 10.
Role allocation TBD: which steps are crew-executed, operator-directed, or automatic, and handover rules TBD.
Independence consideration TBD: whether any procedure relies on the independent safety path versus primary systems.

## 8. Detailed Design

Emergency-state list is a stub in this revision (states TBD, entry/exit criteria TBD, no thresholds baselined).
Procedure format TBD (checklist/flow structure TBD); sequencing, decision branches, and abort/transfer conditions TBD.
Mapping method (methodology only): each REQ-HFPX-EPR-001 state → REQ-HFPX-EPR-002 action thread → REQ-HFPX-EPR-003 alert source(s); completeness is checked by inspection against the hazard list, with coverage criteria TBD.

## 9. Interfaces

- Procedures ↔ CONOPS (CON-002/004, OPC-004): off-nominal threads supply action intent; this document returns procedure definitions for CONOPS validation (details TBD).
- Procedures ↔ Vol 10.11/10.12: alert definitions supply initiation cues; mapping table owned here, alert implementation owned by Vol 10 (thresholds/latencies TBD).
- Procedures ↔ Recovery volumes (Vol 13.9–13.13): procedures may invoke EPM/AST/PRS/AIP/IPS behaviours without prescribing their implementation (envelopes TBD).
- Procedures ↔ Vol 23: rehearsal/demo needs feed test planning; execution and range conduct owned by Vol 23 (methods TBD).

## 10. Operational Concept

Emergency operations follow: detect (alert per Vol 10) → declare (enter emergency state per REQ-HFPX-EPR-001) → act (procedure per REQ-HFPX-EPR-002) → exit or transfer (exit criteria TBD).
This concept defines declaration and action allocation only; it does not direct vehicle handling, ignition sequencing, or flight conduct (owned and gated under Vol 23/CONOPS).
Hover-first emphasis: procedures applicable in hover/low-altitude are defined and validated first; envelope expansion procedures require separate closure (scope TBD).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, architecture, interfaces, and test methodology only; it contains no instructions for constructing, igniting, or operating high-energy propulsion.
Recovery effectiveness is unproven (ISS-008): procedures ending in stabilisation, propulsion-management, or recovery actions assert no successful outcome until demonstrated through gated verification (criteria TBD).
Hover/low-altitude is the limiting case for procedure validation; timing and workload claims are TBD and uncredited in this revision.

## 12. Performance

Procedure performance measures TBD with no thresholds baselined: declaration latency TBD, action-completion time TBD, rehearsal error rate TBD, mapping completeness TBD.
All timings, workloads, and usability targets TBD; no numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-EPR-001 verified by Inspection of the emergency-state register (criteria TBD).
- REQ-HFPX-EPR-002 verified by Demonstration of crew/operator threads in sim or ground rig (scenarios TBD).
- REQ-HFPX-EPR-003 verified by Analysis of the procedure-to-alert trace against Vol 10.11/10.12 (completeness criteria TBD).
- REQ-HFPX-EPR-004 verified by Demonstration (rehearsal/demo records); human procedures are gated — FRR authorisation required before human-flight credit (criteria TBD).
- Validation is operational-acceptance review plus Safety Review Board concurrence at gates (scope TBD).

## 14. Risks

- Alert-procedure mismatch: procedure assumes an alert that Vol 10 does not provide as specified; mitigation: joint mapping review with Vol 10, criteria TBD.
- Workload exceedance in hover/low-altitude limiting case; mitigation: hover-first rehearsal emphasis, workload criteria TBD.
- Unproven recovery assumed effective by procedure users (ISS-008); mitigation: explicit unproven status in every recovery-terminating procedure.

## 15. Open Issues

Emergency-state list TBD. Entry/exit criteria TBD. Crew/operator role allocation TBD. Vol 10.11/10.12 alert sources and thresholds TBD. Rehearsal/demo methods and pass criteria TBD. Human-flight gating criteria TBD. ISS-008 applies to all recovery-terminating procedures.

## 16. Assumptions

- A-EPR-001: CONOPS off-nominal thread (CON-002/004, OPC-004) will supply action intent sufficient to derive procedures; validation: CONOPS maturity review (TBD).
- A-EPR-002: Vol 10.11/10.12 will supply timely, unambiguous alerts for each emergency state; validation: Vol 10 verification (TBD).
- A-EPR-003: Rehearsal/demo environments adequately represent operational workload for validation purposes; validation: Vol 23 test adequacy review (TBD).

## 17. Dependencies

Depends on CON-002/004 and OPC-004 (action basis), Vol 10.11/10.12 (alerts), Vol 13.1–13.7 (hazard/analysis triggers), SEMP (gates), V&V Plan (verification discipline), Vol 23 (rehearsal/demo execution).

## 18. Traceability

Parents: CON-002, CON-004, OPC-004. Children: procedure flows, mapping table, and rehearsal/demo cases (artefact IDs TBD).
RTM: REQ-HFPX-EPR-001..004 → CONCEPT. Each procedure traces to at least one emergency state and at least one alert; each human procedure traces to at least one rehearsal/demo case (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Procedure and mapping tables are under document control once populated; changes via change records with affected-state impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (emergency-procedure framework; Ch 13.8) |
