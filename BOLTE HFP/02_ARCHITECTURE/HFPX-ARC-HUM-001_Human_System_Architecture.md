# Human–System Architecture

**Document ID:** HFPX-ARC-HUM-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X human–system architecture view (Chapter 02.15): helmet/HUD/audio/alert integration, pilot-controls/restraint/ergonomics hooks, workload/situational-awareness principles, and physiological-monitoring hooks.

## 2. Scope

Covers pilot-vehicle integration for the production-aircraft concept. Display symbology, control layouts, restraint design, and workload limits TBD (Vol 10/12/30). No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001..008); HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-001..005)
- Vol 10 (helmet/displays/alerts); Vol 12 (pilot controls/restraint/ergonomics); Vol 30 (workload/SA); physiological monitoring (Vol TBD)
- HFP prompt §11 (human-system/operational views)

## 4. Definitions & Acronyms

- HUD: head-up display element of helmet system (design TBD).
- SA: situational awareness (metrics TBD, Vol 30).
- Physiological monitoring: pilot-state sensing hooks (scope TBD).

## 5. System Context

Pilot interacts via helmet (HUD/audio/alerts), manual controls, restraint/suit, and ground-crew interfaces; avionics and safety computer feed displays and alerts; physiological monitoring (if adopted) feeds caution logic. All details TBD.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-HSA-001 | Helmet/HUD/audio/alert integration shall be defined per Vol 10 (symbology, priority, inhibits — TBD). | Analysis + Test |
| REQ-HFPX-HSA-002 | Pilot-controls, restraint, and ergonomics hooks shall be defined per Vol 12 (layouts, forces, envelopes — TBD). | Analysis + Test |
| REQ-HFPX-HSA-003 | Workload and situational-awareness principles shall follow Vol 30 (limits and methods TBD). | Analysis |
| REQ-HFPX-HSA-004 | Physiological-monitoring hooks (parameters, use, privacy/safety policy — TBD) shall be defined. | Inspection |

## 7. Architecture

Pilot-vehicle loop: controls → FCS/safety computer → vehicle response → sensors/fusion → helmet/HUD/audio alerts → pilot. Alert hierarchy (priority, suppression, inhibits — TBD) is owned by Vol 10 logic. Controls/restraint/ergonomics structure (Vol 12) constrains reach, force, and posture envelopes (TBD). Workload/SA principles (Vol 30) bound task loading and information density (limits TBD). Physiological hooks (TBD parameters) feed caution/advisory paths only, never autonomous control per ARC-002; human override authority per Vol 18.11 is preserved.

## 8. Detailed Design

Not applicable at Tranche 2 draft level. Helmet, control, restraint, and monitoring designs are TBD (Vol 10/12/30).

## 9. Interfaces

Human-system interfaces (helmet, controls, suit/restraint, audio/alerts, monitoring sensors) are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Human-system view supports all flight modes and ground handling; normal/abnormal alerting and handover procedures follow CONOPS and Vol 10/12/30. Training implications per SYS-23 TBD.

## 11. Safety

Pilot overload, missed alerts, or inadvertent inputs are hazardous: prioritised alerting (HSA-001), ergonomic control/restraint design (HSA-002), workload/SA limits (HSA-003), and preserved override (Vol 18.11) mitigate them. No human-performance claim is made; all limits TBD pending Vol 10/12/13/30 analysis and test.

## 12. Performance

Display latency, alert timing, control forces, workload scores, and monitoring accuracy are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by analysis (task/workload analysis) and simulator/human-in-the-loop testing (methods TBD). Later validated in flight test (Vol 19/33). All methods TBD in detail.

## 14. Risks

- Alert saturation or mode confusion; mitigation: hierarchy/inhibit discipline per Vol 10, simulator trials TBD.
- Ergonomic mismatch discovered late; mitigation: early mock-up/HITL evaluation, TBD.

## 15. Open Issues

Symbology/alert logic TBD; control/restraint layouts TBD; workload/SA limits TBD; physiological-monitoring scope and policy TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-001..005), Vol 10 (helmet), Vol 12 (pilot systems), Vol 30 (human factors), safety view (02.10), comms view (02.13).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (esp. ARC-002); tier inputs HUM/FUN/SAF as allocated. Children: Vol 10/12/30 designs, ICDs, V&V cases. RTM: REQ-HFPX-HSA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.15) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
