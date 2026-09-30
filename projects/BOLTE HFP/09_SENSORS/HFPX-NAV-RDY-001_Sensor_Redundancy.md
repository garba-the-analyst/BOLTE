# 09.15 Sensor Redundancy

**Document ID:** HFPX-NAV-RDY-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the structure and subsystem requirements for sensor redundancy within Volume 09, Chapter 09.15. This revision establishes requirement placeholders only; redundancy approach, independence evidence, verification, and FTA flow are TBD. No redundancy scheme selection or design approval is implied.

## 2. Scope

Covers redundancy approach, independence evidence rules, redundancy verification structure, and flow to fault-tree analysis.

Out of scope: detailed voting or selection design; hardware selection; software implementation. No redundancy scheme is selected and no parts are selected at this revision.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-004 and related functional tier, including FUN-003 where applicable)
- HFPX-NAV-IDX-001 Volume 09 index / README (Chapter 09.15)
- Volume 09 sensor chapters 09.2 through 09.14 (redundancy scope TBD)
- Safety analyses references Vol 13 including SFA/CCA and FTA (hooks TBD)
- HFPX-VV-PLN-001 V&V Plan (not written, verification cases TBD)

## 4. Definitions & Acronyms

_TBD_

- RDY: Sensor Redundancy chapter (09.15)
- NSR: sensor redundancy requirement prefix (REQ-HFPX-NSR)
- TBD: to be determined; TBC: to be confirmed
- SFA: system functional analysis or equivalent safety analysis hook TBD; CCA: common-cause analysis hook TBD; FTA: fault-tree analysis
- Verification methods: Analysis / Inspection / Demonstration / Test (allocation per requirement TBD)

## 5. System Context

Sensor redundancy supports availability and integrity of navigation and related measurements by providing defined behaviour under sensor failures within the scope of SYS-004.

Context TBD. Allocation TBD. Relationship to functional tier FUN-003 TBD. Relationship to fusion (NSF) and algorithms (NNA) tiers TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-NSR-001 | The sensor redundancy function shall implement a redundancy approach TBD, including voting and selection behaviour TBD. | REQ-HFPX-SYS-004, FUN-003 | Analysis + Test (details TBD) |
| REQ-HFPX-NSR-002 | The sensor redundancy function shall comply with independence evidence rules TBD, including CCA hooks TBD. | REQ-HFPX-SYS-004, FUN-003, SFA/CCA hooks TBD | Analysis / Inspection (details TBD) |
| REQ-HFPX-NSR-003 | The sensor redundancy function shall be verified by means TBD. | REQ-HFPX-SYS-004, FUN-003 | Analysis + Test (details TBD) |
| REQ-HFPX-NSR-004 | The sensor redundancy function shall flow to FTA TBD. | REQ-HFPX-SYS-004, FUN-003, SFA/CCA hooks TBD | Analysis (details TBD) |

No quantitative values are stated. All schemes, thresholds, and test conditions are TBD. No redundancy scheme selection is made.

## 7. Architecture

_TBD_

Redundant channel arrangement, placement, and management TBD. Relationship to sensor architecture (09.1) TBD. Structure only at this revision.

## 8. Detailed Design

_TBD_

No detailed design is defined. No voting scheme, selector, technology, or supplier is selected. No parts are selected at this revision.

## 9. Interfaces

_TBD_

Interfaces between redundant channels, fusion, algorithms, and monitoring TBD. ICD details TBD.

## 10. Operational Concept

_TBD_

Redundancy behaviour across flight phases and failure conditions TBD.

## 11. Safety

_TBD_

Safety relevance TBD. Hooks to SFA/CCA and FTA/FMEA TBD. Independence claims TBD. No safety claim is made at this revision.

## 12. Performance

_TBD_

All performance values TBD. No value in this document is approved.

## 13. Verification & Validation

_TBD_

Verification for REQ-HFPX-NSR-001..004 TBD, including redundancy demonstration and analysis TBD. Cases and acceptance criteria TBD in the V&V Plan.

## 14. Risks

- TBD density high: redundancy approach and independence undefined; mitigation: placeholders with SFA/CCA hooks established
- FTA flow undefined; mitigation: trace placeholder TBD

## 15. Open Issues

- Redundancy approach TBD (voting / selection TBD)
- Independence evidence rule TBD (CCA hooks)
- Redundancy verification TBD
- Redundancy-to-FTA flow TBD

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: functional tier FUN-003; sensor definitions (09.2 through 09.14); safety analyses Vol 13 (SFA/CCA/FTA); V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-SYS-004, FUN-003. Hooks: SFA/CCA, FTA. Tier links: NSF/NNA TBD. Children: TBD (design, V&V cases, RTM rows). RTM seed for REQ-HFPX-NSR-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Changes require change control in later revisions.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 09.15) |
