# Mean Time To Repair

**Document ID:** HFPX-REL-MTR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Mean Time To Repair direction for Volume 24 (Chapter 24.9): how MTTR definition, values control, demonstration method, and spares/GSE hooks will be governed.
Sets definition and evidence rules only; it contains no MTTR values, task times, or spares figures beyond TBD.

## 2. Scope

Covers MTTR for defined maintenance levels and conditions, with levels and conditions TBD.
In scope: definition rules, value records, demonstration method, spares/GSE hooks. Out of scope: quantitative repair claims, which are TBD, and support-execution owned by Vol 27.
Feeds Vol 24.6 availability inputs and Vol 24.7 maintainability assessment as applicable.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-MNT-001 Maintainability, HFPX-SAFE-CAS-001 Safety Case
- Vol 27 support volumes (spares, GSE, documentation), HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- MTTR: Mean Time To Repair; mean time to restore an item under stated conditions; definition details and scope TBD
- Demonstration: maintenance demo activity intended to evidence an MTTR value; method TBD
- Spares/GSE hooks: interfaces to spares provisioning and ground support equipment concepts; details TBD
- Maintenance conditions: level, tools, spares, personnel, and environment statements; statements TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

MTTR assessment depends on controlled condition statements and Vol 27 support-concept maturity; without both, no comparison to intent is valid.
This document governs definition and evidence discipline; no MTTR outcome is claimed in this revision.
Design-for-maintainability attributes are owned by Vol 24.7 (attributes TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RMR-001 | The programme shall define MTTR with stated maintenance levels and conditions, with definition details TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RMR-002 | The programme shall record MTTR values with defined scope, with all values TBD and record schema TBD. | TBD reliability classification; Vol 24.7 | Inspection |
| REQ-HFPX-RMR-003 | The programme shall define an MTTR demonstration method, with method, conditions, and acceptance criteria TBD. | TBD reliability classification; V&V Plan | Demonstration |
| REQ-HFPX-RMR-004 | MTTR assessment shall maintain defined spares/GSE hooks, with interface, traceability, and update rules TBD. | TBD reliability classification; Vol 27 | Inspection |

## 7. Architecture

MTTR organisation TBD: MTTR owner, Vol 24.7 maintainability owner, Vol 27 support owners, independent reviewer TBD.
Record architecture TBD: value table schema TBD with all value fields TBD.
Demonstration architecture TBD: demo articles, conditions, spares/GSE states TBD.

## 8. Detailed Design

Methodology only, no values:
- Definition: repair-time boundaries TBD (diagnosis, access, replacement, verification inclusions TBD); level definitions TBD; condition statements TBD.
- Values: recording schema TBD; all value fields TBD; status values TBD.
- Demonstration: demo method TBD; task selection TBD; conditions TBD; acceptance rule TBD (no times baselined).
- Spares/GSE hooks: provisioning-concept exchange TBD; GSE-availability treatment TBD; documentation hooks TBD.

## 9. Interfaces

- MTTR ↔ Maintainability (Vol 24.7 attribute alignment; attributes TBD)
- MTTR ↔ Support (Vol 27 spares/GSE/documentation inputs; details TBD)
- MTTR ↔ Availability (Vol 24.6 model inputs; model TBD)
- MTTR ↔ Design volumes (Vol 03–18 own repair-enabling design; details TBD)
- MTTR ↔ V&V (demo cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

MTTR matures across the lifecycle: definition at SRR/PDR as applicable → placeholders TBD → demonstration through integration and test → gate assessment TBD.
This concept defines definition and evidence discipline only, not maintenance execution or operations.
No MTTR outcome is asserted in this revision.

## 11. Safety

No safety claim is made in this revision; MTTR outputs take no safety credit until verified through the safety path.
Maintenance-error controls remain owned by Vol 13 with criteria TBD; no control is claimed here.

## 12. Performance

MTTR performance indicators TBD (no thresholds baselined): scope-definition completeness TBD, value traceability TBD, demo-closure backlog TBD, spares/GSE hook coverage TBD.
No MTTR values, task times, availability figures, failure rates, MTBF values, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, hook direction).
Requirement verification follows the V&V Plan: Inspection/Demonstration methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Undefined repair boundaries compared as if comparable; mitigation: boundary definitions TBD before any assessment
- Unevidenced MTTR treated as commitment; mitigation: TBD-only values enforced at gates
- Spares/GSE immaturity hidden in demo conditions; mitigation: hook qualification TBD before demonstration

## 15. Open Issues

MTTR definition details TBD. Maintenance levels and conditions TBD. All values TBD. Demonstration method TBD. Spares/GSE hook details TBD. Acceptance criteria TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-MNT-001 (Vol 24.7), SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 27 spares/GSE volumes, Vol 24.6 availability.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, Vol 27. Children: MTTR records and demo cases (artefact IDs TBD).
RTM: REQ-HFPX-RMR-001..004 → CONCEPT. Each value traces to conditions → demo → spares/GSE inputs TBD → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-MTTR impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (MTTR definition and demo rules; values TBD) |
