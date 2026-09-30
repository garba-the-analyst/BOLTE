# Pilot Alerts

**Document ID:** HFPX-HMI-ALT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the helmet pilot-alert requirements for HFP-X (Chapter 10.12): alert inventory, multi-modal alerting, and acknowledgement behaviour. No alert list, modality assignment, timing value, or acknowledgement rule is defined in this document.

## 2. Scope

Covers pilot alerts allocated from SYS-005 and STK-007, including inventory definition per FHA, visual/audio multi-modal presentation, and acknowledgement. Excludes warning hierarchy and suppression logic (Chapter 10.11), propulsion parameter presentation (Chapter 10.10), voice-command behaviour (Chapter 10.13), and communications implementation (Chapter 10.15). All inventories, modalities, levels, and timings are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-002 controllability, STK-007 status/warning guidance)
- HFPX-ARC-HUM-001 Human-System Architecture (REQ-HFPX-HSA-001 helmet integration, REQ-HFPX-HSA-003 workload principles)
- HFPX-SYS-HUM-001 Human Factors Requirements (REQ-HFPX-HUM-001 workload, REQ-HFPX-HUM-002 legibility, REQ-HFPX-HUM-004 monitoring annunciation)
- Vol 13 FHA alert-source input (inventory TBD)
- Vol 30 human-factors principles (limits and methods TBD)

## 4. Definitions & Acronyms

- HPA: pilot-alert requirement tier; ID prefix `REQ-HFPX-HPA-NNN`
- Alert inventory: the defined set of pilot alerts and their triggering conditions (set TBD per FHA)
- Multi-modal alerting: presentation across visual and audio paths (modalities and assignments TBD)
- Acknowledgement: pilot action confirming alert receipt and its effect on presentation (means and effects TBD)
- TBD: to be defined. No values stated.

## 5. System Context

The pilot-alert function renders the defined alert inventory through visual and audio helmet paths and manages acknowledgement effects, within workload and legibility constraints (HUM-001/002, Vol 30). It consumes alert triggers from health/fault and monitoring sources (including FHA-derived conditions, TBD) and coordinates with warning-system prioritisation (Chapter 10.11).

```text
[Alert triggers incl. FHA conditions (TBD)] --> [Alert rendering visual/audio (TBD) + acknowledgement handling (TBD)] --> [Pilot]
   constrained by [HUM-001/002 workload/legibility (TBD, Vol 30)] | coordinated with [10.11 prioritisation (TBD)]
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HPA-001 | The helmet shall implement a defined pilot-alert inventory with defined triggering conditions derived per FHA (inventory and conditions TBD). | STK-007, SYS-005, HSA-001 | Inspection + Demonstration (TBD) |
| REQ-HFPX-HPA-002 | Pilot alerts shall be presented multi-modally via defined visual and audio means with defined modality assignments (means and assignments TBD). | STK-007, SYS-005, HUM-002 | Demonstration (TBD) |
| REQ-HFPX-HPA-003 | Defined alerts shall require defined acknowledgement with defined effects on presentation and persistence (alerts, means, and effects TBD). | STK-002, SYS-005, HUM-001 | Demonstration (TBD) |
| REQ-HFPX-HPA-004 | Each pilot-alert requirement in this document shall have a defined verification method and pass criteria (methods and criteria TBD). | SYS-005 | Inspection (TBD) |

No alert, modality, level, timing, or acknowledgement value in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: HPA-001 → inventory/trigger function; HPA-002 → multi-modal rendering function; HPA-003 → acknowledgement-handling function; HPA-004 → V&V thread. Authoritative allocation lives in Vol 10 integration views; this section states derivation intent only. Alert managers, renderers, and input handlers are TBD.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Alert lists, trigger logic, symbology, audio constructs, acknowledgement gestures/inputs, and persistence rules are TBD.

## 9. Interfaces

- Alert-trigger source interface (health/fault/monitoring, FHA-derived): TBD.
- Visual presentation interface (display pipeline): TBD.
- Audio presentation interface (Chapter 10.5 audio system coordination): TBD.
- Acknowledgement input interface (controls/gestures/voice hooks): TBD.
- Formal ICDs are TBD.

## 10. Operational Concept

Requirements are exercised through nominal single-alert threads, multi-alert threads, and acknowledgement threads under controlled conditions. Trigger-to-presentation-to-acknowledgement sequences and crew responses are TBD.

## 11. Safety

Missed, ambiguous, unacknowledged, or nuisance alerts are hazardous. Mitigations required (all TBD): FHA-derived inventory (HPA-001), multi-modal presentation (HPA-002), defined acknowledgement (HPA-003). No alerting-integrity or workload claim is made at this revision.

## 12. Performance

Intentionally TBD. No alert count, latency, persistence, audio level, visual luminance, or acknowledgement timing value is stated. Future revisions reference budgets and models, never invented figures.

## 13. Verification & Validation

HPA-004 establishes the thread: each HPA requirement maps to at least one V&V case (methods stated in section 6 table). Intended strategy is inspection of the inventory definition and demonstration of multi-modal rendering and acknowledgement on representative rigs (scenarios and pass criteria TBD). No V&V is complete at this revision.

## 14. Risks

- FHA undefined → alert inventory ungrounded; mitigation: inventory held as TBD placeholder fed by Vol 13.
- Modality assignments undefined without audio/display allocation; mitigation: multi-modal requirement held as TBD with Vol 10 dependency explicit.
- Acknowledgement effects undefined → persistence/overload behaviour unknown; mitigation: acknowledgement requirement held as TBD with Vol 30 evaluation.

## 15. Open Issues

- Alert inventory and triggering conditions TBD per FHA.
- Visual/audio means and modality assignments TBD.
- Acknowledgement means, applicable alerts, and effects TBD.
- Verification methods, rigs, scenarios, and pass criteria TBD per requirement.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-005 policy stability, STK-002/007 needs, HSA-001 integration view, HUM-001/002/004 human-factors inputs, Vol 13 FHA outputs, Vol 30 workload/legibility principles, coordination with Chapters 10.5/10.11, and V&V planning.

## 18. Traceability

Parents: STK-002, STK-007, SYS-005, HSA-001, HSA-003, HUM-001, HUM-002, HUM-004; Vol 30 hooks. Children: Vol 10 alert design, modality implementations, acknowledgement design, V&V cases, RTM rows. RTM: REQ-HFPX-HPA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.12, 4 requirements) |
