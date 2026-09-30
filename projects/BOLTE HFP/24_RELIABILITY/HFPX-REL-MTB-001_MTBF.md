# Mean Time Between Failures

**Document ID:** HFPX-REL-MTB-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Mean Time Between Failures direction for Volume 24 (Chapter 24.8): how MTBF definition, scope, values control, and demonstration method will be governed.
Sets definition and evidence rules only; it contains no MTBF values or failure rates beyond TBD and asserts no claim before evidence.

## 2. Scope

Covers MTBF for defined scopes and operating conditions, with scopes TBD.
In scope: definition and scope rules, value records, demonstration method, no-claim-before-evidence rule. Out of scope: quantitative MTBF claims, which are TBD, and safety-probability claims owned by Vol 13.
Feeds Vol 24.2 allocation assessment and Vol 24.6 availability inputs as applicable.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-FRA-001 Failure Rate Analysis, HFPX-REL-ALC-001 Reliability Allocation
- HFPX-SAFE-CAS-001 Safety Case; HFPX-VV-PLN-001 V&V Plan; Vol 13 analyses as applicable
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- MTBF: Mean Time Between Failures; mean operating time between failures for a defined scope and conditions; definition details and scope TBD
- Demonstration: test or analysis activity intended to evidence an MTBF value; method TBD
- No claim before evidence: rule that no MTBF value is asserted until verified evidence exists; evidence TBD/empty
- Operating conditions: duty, environment, and configuration statements bounding MTBF; statements TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

MTBF assessment depends on controlled scope definitions and qualified data; without both, no comparison to intent is valid.
This document governs definition and evidence discipline; no MTBF outcome is claimed in this revision.
Data qualification follows Vol 24.3 hierarchy (all values TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RMB-001 | The programme shall define MTBF with stated scope and operating conditions, with definition details and scope TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RMB-002 | The programme shall record MTBF values with defined scope, with all values TBD and record schema TBD. | TBD reliability classification; Vol 24.3 | Inspection |
| REQ-HFPX-RMB-003 | The programme shall define an MTBF demonstration method, with method, conditions, and acceptance criteria TBD. | TBD reliability classification; V&V Plan | Test |
| REQ-HFPX-RMB-004 | No MTBF claim shall be asserted before verified evidence exists, with evidence recorded as TBD/empty until closure. | TBD reliability classification; REQ-HFPX-SCA-004 | Inspection |

## 7. Architecture

MTBF organisation TBD: MTBF owner, data owners in Vol 24.3, independent reviewer TBD.
Record architecture TBD: value table schema TBD with all value fields TBD.
Demonstration architecture TBD: test articles, conditions, and recording schema TBD.

## 8. Detailed Design

Methodology only, no values:
- Definition/scope: failure definition TBD; operating-time definition TBD; condition statements TBD; exclusion rules TBD.
- Values: recording schema TBD; all value fields TBD; status values TBD.
- Demonstration: test method TBD; duration and conditions TBD; statistical treatment TBD; acceptance rule TBD (no thresholds baselined).
- No-claim rule: evidence qualification TBD; claim authority TBD; premature-claim prohibition enforced at gates.

## 9. Interfaces

- MTBF ↔ Failure-rate analysis (Vol 24.3 hierarchy applies; values TBD)
- MTBF ↔ Allocation (Vol 24.2 intent assessed against MTBF records as applicable)
- MTBF ↔ Availability (Vol 24.6 model inputs; model TBD)
- MTBF ↔ Safety (no safety credit; safety path owned by HFPX-SAFE-CAS-001)
- MTBF ↔ V&V (demonstration cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

MTBF matures across the lifecycle: definition at SRR/PDR as applicable → placeholders TBD → demonstration through test → gate assessment TBD.
This concept defines definition and evidence discipline only, not test conduct or operations.
No MTBF outcome is asserted in this revision.

## 11. Safety

No safety claim is made in this revision; MTBF outputs take no safety credit until verified through the safety path.
No hazard-probability claim is made here; hazard probabilities owned by Vol 13 with scales TBD.

## 12. Performance

MTBF performance indicators TBD (no thresholds baselined): scope-definition completeness TBD, value traceability TBD, demonstration-closure backlog TBD.
No MTBF values, failure rates, availability figures, MTTR values, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, no-claim rule).
Requirement verification follows the V&V Plan: Inspection/Analysis/Test methods; acceptance criteria TBD per case; evidence TBD/empty until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Undefined scope compared as if comparable; mitigation: scope statements TBD before any assessment
- Unevidenced MTBF treated as commitment; mitigation: no-claim-before-evidence rule enforced at gates
- Demonstration conditions unrepresentative; mitigation: condition-qualification TBD before demonstration

## 15. Open Issues

MTBF definition details TBD. Scope and condition statements TBD. All values TBD. Demonstration method TBD. Evidence TBD/empty. Claim authority TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-FRA-001, HFPX-REL-ALC-001, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 24.6 availability.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, HFPX-REL-ENG-001, SAF tier. Children: MTBF records and demonstration cases (artefact IDs TBD).
RTM: REQ-HFPX-RMB-001..004 → CONCEPT. Each value traces to scope → data source TBD → demonstration → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-MTBF impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (MTBF definition and evidence rules; values TBD, no claim before evidence) |
