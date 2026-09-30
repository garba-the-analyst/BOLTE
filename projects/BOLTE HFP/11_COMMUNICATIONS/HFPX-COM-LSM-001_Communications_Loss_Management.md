# Communications Loss Management

**Document ID:** HFPX-COM-LSM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X communications loss management for Volume 11, Chapter 11.9: loss detection, timed-response ladder including abort/landing/recovery, annunciation, and link restoration.

## 2. Scope

Covers loss of command, telemetry, pilot, ground, emergency, and data links across all flight modes and ground operations. Detection thresholds, response timings, manoeuvre definitions, and hardware are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1–11.8 links and redundancy, 11.10 ground station); Vol 13 (safety/authority, including 13.17); Vol 17 (cybersecurity); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Loss detection: determination that a communications link is lost or degraded (criteria TBD).
- Timed-response ladder: escalating responses keyed to loss persistence (steps and thresholds TBD).
- Annunciation: pilot/operator indication of link state and active response (details TBD).
- Link restoration: re-establishment of lost links and resumption of normal operations (logic TBD).

## 5. System Context

Loss management monitors pilot, ground, telemetry, command, emergency, and data links and escalates from link re-establishment attempts through abort, landing, and recovery actions, coordinated with safety-path behaviour, command authority (Vol 13), and ground-station roles (11.10) (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-CCM-001 | Loss and degradation detection for communications links, including criteria and monitored parameters, shall be defined (criteria TBD). | REQ-HFPX-SYS-005 | Fault-injection test |
| REQ-HFPX-CCM-002 | A timed-response ladder for persistent communications loss, including escalation steps and thresholds, shall be defined (steps and thresholds TBD). | REQ-HFPX-SYS-005 | Fault-injection test |
| REQ-HFPX-CCM-003 | Abort, landing, and recovery actions commanded by the loss-response ladder shall be defined (behaviour TBD, authority per Vol 13). | REQ-HFPX-OPC-003 | Fault-injection test |
| REQ-HFPX-CCM-004 | Pilot/operator annunciation of link state and active loss-response actions shall be defined (details TBD). | REQ-HFPX-OPC-003 | Fault-injection test |
| REQ-HFPX-CCM-005 | Link-restoration behaviour, including re-establishment attempts and resumption of normal operations, shall be defined (logic TBD). | REQ-HFPX-SYS-005 | Fault-injection test |

## 7. Architecture

Link monitors feed loss-detection logic (criteria TBD) which drives the timed-response ladder (ladder TBD): re-establishment attempts escalate to abort, landing, and recovery actions under Vol 13 authority (actions TBD). Annunciation paths inform pilot and ground-station operators (paths TBD). Restoration logic re-qualifies links before resuming normal operations (logic TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Monitor implementations, ladder thresholds, manoeuvre definitions, and annunciation implementations are TBD.

## 9. Interfaces

Interfaces to link monitors, vehicle guidance/safety paths, pilot displays, and ground-station consoles are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Loss management applies in all flight modes and ground operations, including handover and degraded-link phases. Crew/operator procedures for ladder escalation, abort/landing/recovery, and restoration are TBD.

## 11. Safety

Undetected or mishandled communications loss is hazardous. Mitigation is via defined detection (CCM-001), timed-response ladder (CCM-002), abort/landing/recovery actions (CCM-003), annunciation (CCM-004), and restoration logic (CCM-005), plus redundancy (11.8) and Vol 13 safety/authority hooks. No detection or timing claim is made at this revision.

## 12. Performance

Detection criteria and response-ladder timing budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by fault-injection test of detection, ladder escalation, abort/landing/recovery actions, annunciation, and restoration, plus analysis of ladder logic. Test scope and pass criteria are TBD (Vol 19/33).

## 14. Risks

- Ladder thresholds unvalidated; mitigation: analysis and fault-injection testing, TBD.
- Authority coordination for abort/landing/recovery incomplete; mitigation: Vol 13 hooks, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Detection criteria TBD; ladder steps and thresholds TBD; abort/landing/recovery behaviour TBD; annunciation TBD; restoration logic TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.2–11.8 links and redundancy, 11.10 ground station, Vol 13 (safety/authority), Vol 17, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: loss-management design, safety cases, ICDs, fault-injection V&V cases. RTM: REQ-HFPX-CCM-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.9) |
