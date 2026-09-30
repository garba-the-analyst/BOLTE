# Thermal Testing

**Document ID:** HFPX-THM-TST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X thermal-testing structure for Chapter 14.14. This Tranche 6 draft establishes test thread, pass/fail criteria structure, model-correlation structure, and V&V hooks with all values TBD; quantified test plans follow in later tranches with the V&V Plan.

## 2. Scope

Covers thermal/environmental test thread, pass/fail structure, model-correlation rules, and hooks to 23.6 and Vol 22/23. Excludes quantified test levels/durations, operating instructions, and qualification credit. All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV-001..005)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- HFPX-THM-ARC-001 through HFPX-THM-WND-001 (Chapters 14.1–14.13, this tranche)
- HFPX-VV-PLN-001 V&V Plan (not written; will own qualification cases); hook to 23.6 (TBD)

## 4. Definitions & Acronyms

- TTS: thermal-testing requirement tier; ID `REQ-HFPX-TTS-NNN`; verification: Test (intended, with Analysis correlation).
- Test thread: ordered set of thermal/environmental tests tracing chapters 14.1–14.13; detail TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Testing tier organises SYS-006 and ENV-001..005 verification into thread, criteria, and correlation:

```text
SYS-006 → ENV-001..005 → Chapters 14.1–14.13 → TTS-001..004 (thread, criteria, correlation) → Qualification (Vol 22/23, hook to 23.6)
```

Test levels and correlation rules require models and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TTS-001 | The programme shall define a thermal test thread of [TBD] tracing Chapters 14.1–14.13 (thread TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001..005 | Test |
| REQ-HFPX-TTS-002 | Each thermal test shall apply defined pass/fail criteria of [TBD] (criteria TBD). | REQ-HFPX-SYS-006 | Test |
| REQ-HFPX-TTS-003 | Thermal tests shall correlate to models of [TBD] with correlation criteria TBD (correlation TBD). | REQ-HFPX-SYS-006 | Analysis + Test |
|REQ-HFPX-TTS-004|Thermal test artefacts shall provide hooks of [TBD] to 23.6 and Vol 22/23 (hooks TBD).|REQ-HFPX-SYS-006|Inspection|

No temperature, heat load, flow rate, level, duration, or pass threshold is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): thread → rig/ground/flight test stages TBD; criteria → per-test pass/fail TBD; correlation → Vol 19.6 model hooks TBD; V&V hooks → Vol 22/23 and 23.6 TBD. All TBC pending V&V Plan.

## 8. Detailed Design

Not applicable — structure level only. Test rigs, instrumentation, and procedures live in Vol 22/23 detail and are TBD.

## 9. Interfaces

Test interfaces (instrumentation, model-data exchange with Vol 19.6, Vol 22/23 qualification interfaces, 23.6 hooks) are TBD in Chapter 01.16 and Vol 02 ICDs. No interface value is approved.

## 10. Operational Concept

Test thread spans CONOPS-representative conditions as applicable; phase coverage matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Test hazards and safety-related thermal findings feed Vol 13 safety analyses (to follow). No test outcome in this revision is a safety claim; safety credit requires qualified results via change record.

## 12. Performance

Test thread does not quantify performance. Thermal-performance interaction measurements are TBD and owned jointly with performance tiers.

## 13. Verification & Validation

Intended methods are Test and Analysis + Test (see table); levels, durations, instrumentation, and pass criteria are TBD in the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Thread undefined → gaps or duplication across 14.1–14.13 verification; mitigation: single TBD-owned thread with CONCEPT status.
- Correlation assumed without criteria; mitigation: change-controlled model-correlation rules only.

## 15. Open Issues

Thread definition, pass/fail criteria, model-correlation rules, and 23.6 / Vol 22/23 hook mapping. RTM seed for TTS-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, Chapters 14.1–14.13, Vol 19.6 models, V&V Plan, and 23.6 target. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001..005 (see table). Children: qualification cases (Vol 22/23, 23.6 hooks), RTM rows. RTM seed for TTS-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.14; all values TBD) |
