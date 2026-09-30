# Life-Limited Components

**Document ID:** HFPX-REL-LLC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X life-limited components direction for Volume 24 (Chapter 24.10): how life-limit determination, limit records, tracking, and verification will be controlled.
Sets determination and tracking rules only; it contains no life limits, cycles, hours, or usage figures beyond TBD.

## 2. Scope

Covers identification, determination, recording, and tracking of life-limited components across flight and ground elements as applicable, with applicability TBD.
In scope: determination method, limit records, tracking hooks to Vol 27.11, verification approach. Out of scope: quantitative limits, which are TBD, and maintenance execution owned by Vol 27.
Feeds maintainability and safety-critical component controls as applicable.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-SCC-001 Safety-Critical Components direction, HFPX-SAFE-CAS-001 Safety Case
- Vol 27.11 tracking/records, HFPX-VV-PLN-001 V&V Plan, Vol 13 safety hooks as applicable
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Life-limited component: item subject to a mandatory retirement or replacement limit; list and limits TBD
- Life-limit determination: analysis and evidence process establishing a limit; method TBD
- Life unit: cycles, hours, or other usage measure as applicable; units and limits TBD
- Tracking: recording of accumulated life against limits; method and location TBD with Vol 27.11 hooks
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Life-limit control constrains operation and support by ensuring retirement before evidence runs out; without determined limits and tracking, no life claim is valid.
This document governs determination and tracking discipline; no limit is claimed as valid in this revision.
Usage spectra and environment definitions feeding determination are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RLL-001 | The programme shall define a life-limit determination method, with method, inputs, and acceptance rules TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RLL-002 | The programme shall record life limits with defined units and scope, with component list TBD and all limits TBD. | TBD reliability classification; SYS-002/003 | Inspection |
| REQ-HFPX-RLL-003 | Life-limited components shall be tracked against limits under defined tracking rules, with method TBD and hooks to Vol 27.11. | TBD reliability classification; Vol 27.11 | Demonstration |
| REQ-HFPX-RLL-004 | Life-limit determination and tracking shall be verified under a defined verification approach, with method and criteria TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Analysis |

## 7. Architecture

Life-limit organisation TBD: life-limit owner, design-domain delegates, Vol 27.11 tracking owner, independent reviewer TBD.
Record architecture TBD: life-limit table schema TBD (component, limit TBD, unit TBD, basis TBD, status).
Tracking architecture TBD: accumulation records, location TBD, update frequency TBD.

## 8. Detailed Design

Methodology only, no values:
- Determination: input data TBD (test, analysis, field as applicable per Vol 24.3 hierarchy); scatter and uncertainty treatment TBD; approval authority TBD.
- Limits: recording schema TBD; all limit fields TBD; interim-limit rules TBD (no limits baselined).
- Tracking: accumulation method TBD; recording location TBD with Vol 27.11 hooks TBD; exceedance-handling rule TBD (procedure TBD, no execution claimed here).
- Change control: re-determination triggers TBD; propagation to support documentation TBD.

## 9. Interfaces

- Life limits ↔ Reliability programme (HFPX-REL-ENG-001 method and gate rules)
- Life limits ↔ Safety-critical components (Vol 24.13 identification and special-control exchange as applicable)
- Life limits ↔ Tracking/records (Vol 27.11 accumulation and record-keeping; details TBD)
- Life limits ↔ Safety (Vol 13 hazard inputs as applicable; hazard authority owned by safety path)
- Life limits ↔ V&V (determination and tracking cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

Life-limit maturity across the lifecycle: candidate list at SRR/PDR as applicable → determination through test and analysis → tracking defined before operation → gate acceptance TBD.
This concept defines determination and tracking discipline only, not operation, retirement execution, or flight conduct.
No life limit is asserted as valid in this revision.

## 11. Safety

No safety claim is made in this revision; life-limit outputs take no safety credit until verified through the safety path.
No retirement-interval adequacy is claimed here; adequacy requires verified determination plus accepted tracking, both TBD.

## 12. Performance

Life-limit performance indicators TBD (no thresholds baselined): determination coverage TBD, limit traceability TBD, tracking completeness TBD.
No life limits, cycles, hours, usage figures, failure rates, MTBF/MTTR values, or availability figures are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, no-values rule, tracking-hook direction).
Requirement verification follows the V&V Plan: Inspection/Analysis/Demonstration methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Operation against undetermined limits treated as controlled; mitigation: TBD-only limits enforced at gates
- Tracking gaps allowing silent exceedance; mitigation: Vol 27.11 tracking rules and exceedance handling TBD
- Determination inputs unqualified; mitigation: Vol 24.3 hierarchy enforcement before determination

## 15. Open Issues

Component list TBD. Determination method TBD. All limits and units TBD. Tracking method and Vol 27.11 schema TBD. Verification criteria TBD. Usage spectra TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-SCC-001, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 27.11 tracking, Vol 13 safety hooks.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, Vol 27.11. Children: life-limit tables and tracking records (artefact IDs TBD).
RTM: REQ-HFPX-RLL-001..004 → CONCEPT. Each limit traces to determination basis TBD → tracking record → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Life-limit tables under reliability configuration control once opened; changes via change records with affected-component impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (life-limit determination and tracking direction; limits TBD) |
