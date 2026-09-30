# Reliability Requirements — Chapter 01.12

**Document ID:** HFPX-SYS-RLB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture system reliability requirements for HFP-X in one tier. This Tranche 8 draft establishes structure only; all rates, targets and values are TBD.

## 2. Scope

Covers system-level reliability expectations derived from stakeholder safety intent and the independent safety path. Subsystem reliability apportionment lives in Vol 03–18. All quantitative values TBD.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (parent tier)
- HFPX-SYS-REQ-001 SyRS (Chapter 01.6, including REQ-HFPX-SYS-003 independent safety path)
- HFPX-SAFE-CAS-001 Safety Case (not written); V&V Plan (not written)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- Reliability requirement ID `REQ-HFPX-RLB-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- Safety path: independent detection → stabilisation → recovery/safe state per REQ-HFPX-SYS-003

## 5. System Context

Reliability requirements constrain loss-of-function behaviour and feed safety analyses (Vol 13) and maintainability (01.13):

```text
STAKEHOLDER (STK-001) → RELIABILITY (this document) → SAFETY ANALYSES → DESIGN → V&V
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RLB-001 | The system shall meet defined reliability targets for safety-critical functions (targets and scope TBD; no rate is stated at this revision). | REQ-HFPX-STK-001 | Analysis |
| REQ-HFPX-RLB-002 | The system shall tolerate defined single-point failures without loss of the independent safety path (failure set TBD). | REQ-HFPX-SYS-003 | Analysis |
| REQ-HFPX-RLB-003 | The system shall implement fault detection and annunciation for defined critical failures (failure list and timing TBD). | REQ-HFPX-SYS-003 | Analysis + Inspection |
| REQ-HFPX-RLB-004 | The system reliability case shall be documented and traceable to analyses and verification evidence (artefact structure TBD). | REQ-HFPX-STK-001 | Inspection |

## 7. Architecture

Allocation (SAD owns authoritative allocation): RLB-001/RLB-002 → FCS + safety computer + propulsion redundancy views; RLB-003 → avionics/sensors; RLB-004 → SE artefacts. Allocation table TBD.

## 8. Detailed Design

Not applicable — requirements tier only. Redundancy and fault-tolerance design lives in Vol 03–18 and is TBD.

## 9. Interfaces

Reliability-relevant interfaces (power, data, cross-channel) reference Chapter 01.16; ICD details TBD.

## 10. Operational Concept

Reliability requirements are exercised through nominal and off-nominal CONOPS threads (mapping table TBD in V&V Plan).

## 11. Safety

Feeds the Safety Case; FHA/FMEA/FTA (Vol 13) will generate further reliability-derived safety requirements by change record. No safety target is quantified at this revision.

## 12. Performance

No reliability rate, MTBF, availability figure or performance value is stated; all such values TBD pending models and analyses.

## 13. Verification & Validation

Each requirement states its method above; verification cases and IDs are TBD in the V&V Plan (Vol 22). Analysis via reliability models and safety analyses; Inspection via documentation review. Requirements without a verification method are rejected at SRR.

## 14. Risks

- Reliability targets set before architectures and failure data exist → mitigation: explicit TBD status, targets deferred until analyses complete
- Apportionment gaps as Vol 03–18 grow; mitigation: RTM coverage gate per review

## 15. Open Issues

- Reliability targets and apportionment TBD
- Fault lists, detection scope and evidence structure TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001 approval, REQ-HFPX-SYS-003 stability, safety analyses (Vol 13), SAD allocation, models (Vol 06/19), V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-STK-001, REQ-HFPX-SYS-003. Children: subsystem reliability requirements (Vol 03–18), safety analyses, V&V cases, RTM rows (01.18). RTM seed for RLB-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.12) |
