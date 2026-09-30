# Human-System Integration

**Document ID:** HFPX-HUM-HSI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the human-system integration (HSI) programme requirements for HFP-X (Chapter 12.14). This Tranche 6 draft establishes HSI-programme, analysis, and issue-closure placeholders; all values are TBD.

## 2. Scope

Covers the HSI programme, workload/situation-awareness/error analyses, and HSI issue-closure provisions. Excludes standalone workload limits (01.11), ergonomics detail (12.5), and training curricula, which are Vol 30 scope including Chapters 30.7–30.9.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 including Chapters 30.7–30.9 (TBD — analysis inputs to follow)
- HFPX-HUM-ARC-001 (Chapter 12.1) and Chapters 12.2–12.13 inputs

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UHS: HSI requirement tier; IDs `REQ-HFPX-UHS-NNN`; verification TBD.
- HSI: Human-System Integration; SA: situation awareness.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

HSI integrates human-factors work across Vol 12 into a managed programme:

```text
STK-002 + HUM tier → UHS-001..004 → Vol 30.7–30.9 analyses → issue closure → V&V cases
```

No programme milestone, analysis result, or closure criterion is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-UHS-001|The programme shall define and execute an HSI programme covering defined Vol 12 scope and reviews (HSI programme TBD).|STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UHS-002|The programme shall perform workload, situation-awareness, and error analyses per defined methods (analyses TBD; Vol 30.7–30.9 hooks to follow).|STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD)|Analysis|
|REQ-HFPX-UHS-003|The programme shall manage HSI issues to defined closure provisions, including traceability to analyses (issue-closure rule TBD).|STK-002, REQ-HFPX-HUM-005, HSA tier (ID TBD)|Analysis|
|REQ-HFPX-UHS-004|HSI provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD).|STK-002, REQ-HFPX-HUM-005, HSA tier (ID TBD)|Inspection|

All programme scope, analyses, closure rules, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UHS-001/003 → HSI management and issue-tracking framework; UHS-002 → Vol 30.7–30.9 analysis inputs; UHS-004 → V&V framework. All TBC.

## 8. Detailed Design

Not applicable — programme level only. Plans, analysis models, and tooling are TBD in follow-on revisions.

## 9. Interfaces

HSI interfaces (analysis inputs from Chapters 12.1–12.13, Vol 10/13/22/30 coordination) are TBD in Chapter 12.1 register and programme planning. No interface value or layout is approved.

## 10. Operational Concept

HSI applies across design, preparation, flight, and recovery phases including training coordination; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

HSI findings including workload/SA/error results feed Vol 13 safety analyses (to follow). No UHS requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UHS requirement quantifies performance. All HSI measures are TBD pending Vol 30.7–30.9 studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, analysis protocols, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 12/30 inputs. No HSI credit is claimed at this revision.

## 14. Risks

- HSI programme undefined → fragmented human-factors work; mitigation: early UHS-001 placeholder plus review gates.
- Analyses undefined → late workload/SA/error findings; mitigation: UHS-002 placeholder plus Vol 30.7–30.9 coordination.

## 15. Open Issues

TBD: HSI programme scope, workload/SA/error analysis methods, issue-closure rule, and verification criteria pending HSA-tier and Vol 30.7–30.9 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks including Chapters 30.7–30.9 (TBD), Chapters 12.1–12.13 inputs, Vol 13/22 coordination, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-001, REQ-HFPX-HUM-005), HSA tier (ID TBD), Vol 30 hooks including 30.7–30.9 (TBD) — see table. Children: HSI plan, Vol 30 analyses, issue register, V&V cases, RTM rows. RTM seed for UHS-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or programme changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.14) |
