# Human-Machine Interface

**Document ID:** HFPX-HMI-HMI-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the overarching human-machine interface requirements for HFP-X (Chapter 10.14): HMI design principles, workload limits, error tolerance, and evaluation method. No principle instantiation, limit value, tolerance mechanism, or evaluation protocol is defined in this document.

## 2. Scope

Covers HMI-level requirements allocated from SYS-005 and STK-002/007 that govern Chapters 10.1–10.13 and 10.15–10.17, including design principles, workload limits per Vol 30.7, error tolerance per Vol 30.8, and the evaluation method. Excludes chapter-level display, warning, alert, voice, comms, power, and environmental implementations (owned by their chapters). All principles, limits, mechanisms, and protocols are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-002 controllability, STK-007 status/warning guidance)
- HFPX-ARC-HUM-001 Human-System Architecture (REQ-HFPX-HSA-001 helmet integration, REQ-HFPX-HSA-003 workload principles)
- HFPX-SYS-HUM-001 Human Factors Requirements (REQ-HFPX-HUM-001 workload, REQ-HFPX-HUM-002 legibility)
- Vol 30.7 workload limits and Vol 30.8 error-tolerance principles (values and methods TBD)
- Vol 10 chapter designs (Chapters 10.1–10.13, 10.15–10.17, TBD)

## 4. Definitions & Acronyms

- HHM: HMI-level requirement tier; ID prefix `REQ-HFPX-HHM-NNN`
- HMI design principles: governing rules for consistency, legibility, and interaction behaviour (rules TBD)
- Workload limits: bounds on pilot task loading and information density per Vol 30.7 (limits TBD)
- Error tolerance: prevention, detection, and recovery provisions for pilot error per Vol 30.8 (provisions TBD)
- TBD: to be defined. No values stated.

## 5. System Context

This document governs the helmet HMI as a whole: Chapters 10.1–10.13 and 10.15–10.17 derive detailed behaviour from the principles, workload limits, error tolerance, and evaluation method defined here. It refines HSA-001/HSA-003 and HUM-001/002 into HMI-level placeholders evaluated per Vol 30.

```text
[HMI principles + workload limits + error tolerance (this doc, TBD)] --> governs [Vol 10 chapter designs 10.1-10.13, 10.15-10.17 (TBD)]
   refines [HSA-001/003, HUM-001/002 (TBD)] | evaluated per [Vol 30.7/30.8 + evaluation method (TBD)]
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HHM-001 | The helmet HMI shall conform to defined HMI design principles for consistency, legibility, and interaction behaviour (principles TBD). | STK-007, SYS-005, HSA-001 | Inspection + Demonstration (TBD) |
| REQ-HFPX-HHM-002 | The helmet HMI shall keep pilot workload within defined limits across defined tasks per Vol 30.7 (limits and task set TBD). | STK-002, SYS-005, HUM-001 | Analysis + Demonstration (TBD) |
| REQ-HFPX-HHM-003 | The helmet HMI shall provide defined error tolerance by defined prevention, detection, and recovery provisions per Vol 30.8 (provisions TBD). | STK-002, SYS-005, HSA-003 | Analysis + Demonstration (TBD) |
| REQ-HFPX-HHM-004 | Each HMI claim in this document shall be evaluated by a defined evaluation method with defined pass criteria (method and criteria TBD). | SYS-005, HUM-001 | Inspection (TBD) |

No principle, limit, provision, protocol, or criterion in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: HHM-001 → principles governance; HHM-002 → workload-budget function; HHM-003 → error-tolerance function; HHM-004 → evaluation thread. Authoritative allocation lives in Vol 10 integration views and Vol 30 frameworks; this section states derivation intent only. Style guides, budgets, and tolerance mechanisms are TBD.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Principle instantiations, style-guide content, workload budgets, tolerance implementations, and evaluation protocols are TBD.

## 9. Interfaces

- Chapter-design governance interface (Chapters 10.1–10.13, 10.15–10.17 conformance): TBD.
- Workload-limit interface (Vol 30.7 limits and task definitions): TBD.
- Error-tolerance interface (Vol 30.8 provisions and recovery paths): TBD.
- Evaluation interface (subjects, rigs, scenarios, instrumentation): TBD.
- Formal agreements are TBD.

## 10. Operational Concept

Requirements are exercised through nominal task threads (workload assessment) and off-nominal error threads (prevention/detection/recovery) under controlled conditions, using the defined evaluation method. Task sets, error scenarios, and crew procedures are TBD.

## 11. Safety

Overload, inconsistency, illegibility, or unmitigated pilot error is hazardous. Mitigations required (all TBD): governing principles (HHM-001), workload limits (HHM-002), error tolerance (HHM-003), defined evaluation (HHM-004). No workload, legibility, or error-tolerance claim is made at this revision.

## 12. Performance

Intentionally TBD. No workload score, task time, error rate, information-density, or legibility value is stated. Future revisions reference Vol 30 budgets and models, never invented figures.

## 13. Verification & Validation

HHM-004 establishes the thread: each HHM requirement maps to at least one evaluation case (methods stated in section 6 table). Intended strategy is inspection of principle conformance plus analysis and demonstration of workload and error tolerance using the defined evaluation method (protocols, rigs, and pass criteria TBD). No V&V is complete at this revision.

## 14. Risks

- Principles undefined → chapter designs diverge; mitigation: governance requirement held as TBD placeholder.
- Workload limits undefined (Vol 30.7) → overload risk unretired; mitigation: workload requirement held as TBD with Vol 30 dependency explicit.
- Error-tolerance provisions undefined (Vol 30.8) → use-error risk unretired; mitigation: tolerance requirement held as TBD with evaluation thread.

## 15. Open Issues

- HMI design principles TBD.
- Workload limits and task set TBD per Vol 30.7.
- Error-tolerance provisions TBD per Vol 30.8.
- Evaluation method, protocols, rigs, and pass criteria TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-005 policy stability, STK-002/007 needs, HSA-001/003 architecture views, HUM-001/002 human-factors inputs, Vol 30.7/30.8 frameworks, Vol 10 chapter designs, and V&V planning.

## 18. Traceability

Parents: STK-002, STK-007, SYS-005, HSA-001, HSA-003, HUM-001, HUM-002; Vol 30 hooks (Vol 30.7, Vol 30.8). Children: Vol 10 chapter conformance, style-guide content, workload/error-tolerance implementations, evaluation cases, RTM rows. RTM: REQ-HFPX-HHM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.14, 4 requirements) |
