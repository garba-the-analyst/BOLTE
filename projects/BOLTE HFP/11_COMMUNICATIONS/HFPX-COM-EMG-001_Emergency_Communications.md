# Emergency Communications

**Document ID:** HFPX-COM-EMG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X emergency communications for Volume 11, Chapter 11.6: emergency signalling, priority/pre-emption, and ground-station authority hooks.

## 2. Scope

Covers emergency signalling paths for pilot, vehicle, and ground elements across all flight modes and ground operations. Signal sets, waveforms, hardware, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1 architecture, 11.2 pilot comms, 11.8 redundancy, 11.9 loss management); Vol 13.17 (ground-station authority); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Emergency signalling: dedicated signalling for emergency conditions (details TBD).
- Priority/pre-emption: precedence of emergency traffic over all other traffic (scheme TBD).
- Ground-station authority: ground-station command authority in emergencies per Vol 13.17 (TBD).

## 5. System Context

Emergency communications overlay pilot/ground/telemetry/command links, ensuring emergency signals and commands reach pilot, vehicle, and ground-station actors. Authority coordination hooks to Vol 13.17 (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CEM-001|Emergency signalling, including signal set, initiators, and recipients, shall be defined (details TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CEM-002|Priority and pre-emption of emergency communications over all other traffic shall be defined (scheme TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CEM-003|Ground-station authority for emergency communications per Vol 13.17, including roles and handover, shall be defined (details TBD).|REQ-HFPX-OPC-003|Inspection|
|REQ-HFPX-CEM-004|Emergency-communications availability under degraded/lost-link conditions per 11.8/11.9 shall be defined (behaviour TBD).|REQ-HFPX-SYS-005|Inspection|

## 7. Architecture

Emergency signals use prioritised paths over the communications partition (paths TBD), pre-empting routine pilot/ground/telemetry/command traffic (scheme TBD). Authority logic coordinates pilot, vehicle-autonomy, and ground-station roles per Vol 13.17 (TBD). Redundancy and loss hooks go to 11.8/11.9 (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Signalling formats, waveforms, hardware, and protocols are TBD.

## 9. Interfaces

Interfaces to pilot displays/controls, vehicle emergency logic, and ground-station consoles are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Emergency communications support all flight modes and ground operations, including degraded-link operations per 11.9 and authority handover per Vol 13.17. Procedures are TBD.

## 11. Safety

Loss or delay of emergency communications is hazardous. Mitigation is via defined signalling (CEM-001), priority/pre-emption (CEM-002), authority definition (CEM-003), and degraded-link availability (CEM-004), plus redundancy (11.8). No availability or timing claim is made at this revision.

## 12. Performance

Emergency signalling availability and timing budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later priority/pre-emption and end-to-end emergency testing, including fault injection (detail TBD, Vol 19/33).

## 14. Risks

- Pre-emption conflicts with routine traffic undefined; mitigation: priority analysis, TBD.
- Authority handover ambiguity; mitigation: Vol 13.17 hooks, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Emergency signal set TBD; priority/pre-emption scheme TBD; ground-station authority TBD; degraded-link behaviour TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.2 pilot comms, 11.8 redundancy, 11.9 loss management, Vol 13.17 (authority), Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: emergency comms design, ICDs, V&V cases. RTM: REQ-HFPX-CEM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.6) |
