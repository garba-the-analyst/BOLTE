# Safety Requirements

**Document ID:** HFPX-SYS-SAF-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define system-level safety requirements for HFP-X (Chapter 01.10). This Tranche 2 draft encodes load-bearing safety policies — primacy, determinism, independence, AI limits, and flight gating — ahead of formal safety analyses, which follow in Vol 13.

## 2. Scope

Covers safety primacy, deterministic primary control, independent safety path, AI-override prohibition, gated human flight, and recovery/safe-state behaviour (thresholds TBD). Excludes reliability quantification (01.12) and detailed hazard analyses, which are Vol 13 scope. No flight approval is implied.

## 3. Applicable Documents

- Stakeholder needs STK-001 (safety primacy) and system policies SYS-002/003; mission constraints MIS-005/006
- HFPX-SYS-REQ-001 SyRS (parent system requirements)
- HFPX-SAFE-CAS-001 Safety Case (not written); Vol 13 analyses FHA/FMEA/FTA (to follow)
- HFP prompt §§14, 34 (hazardous-subsystem boundary, safety policy)

## 4. Definitions & Acronyms

- SAF: safety requirement tier; ID `REQ-HFPX-SAF-NNN`; verification: Analysis / Inspection / Demonstration / Test.
- Deterministic primary control: bounded, independently verifiable control path; AI operates as monitoring/advisory only.
- Independent safety path: detection → stabilisation → recovery/safe-state chain separate from primary control; details TBD.

## 5. System Context

Safety tier constrains all other tiers:

```text
STK-001 + SYS-002/003 + MIS-005/006 → SAF-001..006 → Vol 13 analyses → Safety Case → Flight gating
```

Every system function and performance claim must satisfy these safety requirements; conflicts resolve in favour of safety.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-SAF-001 | Safety shall take primacy over mission, performance, and schedule objectives in all system decisions and operations (primacy rule; no exception without safety approval TBD). | STK-001, MIS-005 | Inspection |
| REQ-HFPX-SAF-002 | The system shall implement deterministic, bounded, independently verifiable primary flight control for all flight phases (bounds and methods TBD). | SYS-002, STK-001 | Analysis + Test |
| REQ-HFPX-SAF-003 | The system shall provide an independent safety path, separate from the primary control path, that detects defined hazardous conditions and commands stabilisation and recovery/safe-state behaviour (conditions TBD). | SYS-003, MIS-006 | Analysis + Test |
| REQ-HFPX-SAF-004 | No AI or advisory function shall override, inhibit, or mask primary control or the independent safety path under any conditions. | SYS-002, STK-001 | Analysis + Test |
| REQ-HFPX-SAF-005 | Human flight shall be gated on defined prior evidence including unmanned demonstration, safety-analysis closure, and explicit flight authorisation (evidence set TBD). | MIS-005, MIS-006, STK-001 | Inspection + Demonstration |
| REQ-HFPX-SAF-006 | The system shall achieve a defined recovery or safe-state behaviour within [TBD] of a triggering condition, preserving occupant and third-party safety so far as practicable (envelope and criteria TBD). | SYS-003, MIS-006 | Analysis + Test |

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): SAF-002 → FCS + embedded computing; SAF-003/006 → safety computer + recovery subsystem; SAF-004 → AI monitoring + FCS arbitration; SAF-001/005 → programme/operations and ground-station authorisation logic. All TBC pending Vol 13.

## 8. Detailed Design

Not applicable — system level only. Safety mechanisms, redundancy, and implementation detail live in Vol 03–18 and are TBD pending analyses.

## 9. Interfaces

Safety interfaces (arming, authorisation, abort/recovery commanding, annunciation) are TBD in Chapter 01.16 and Vol 02 ICDs. No safety-critical interface value or protocol is approved.

## 10. Operational Concept

Safety requirements apply across all CONOPS phases; SAF-005 gates any human flight on prior unmanned evidence and authorisation. Off-nominal threads exercise SAF-003/006; thread mapping is TBD in the V&V Plan.

## 11. Safety

This section is the requirement set itself (§6). Formal FHA, FMEA, and FTA follow in Vol 13 and will generate additional derived safety requirements by change record. Hazardous-subsystem boundary applies; no build/ignition/operation instructions for high-energy propulsion are included in this document.

## 12. Performance

Safety requirements do not quantify performance. Timing, margin, and envelope values (including SAF-006's [TBD]) remain TBD pending analyses, budgets, and models; no figure is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs, cases, and evidence standards are TBD in the V&V Plan (Vol 22) and Safety Case. No safety credit or flight approval is claimed at this revision.

## 14. Risks

- Safety policies stated before FHA/FMEA/FTA exist → derived requirements missing; mitigation: explicit Vol 13 follow-on and CONCEPT status.
- AI-scope creep into control authority; mitigation: SAF-004 prohibition plus arbitration review gate.

## 15. Open Issues

ISS-002 (SyRS completeness), ISS-005/006/008 (safety and feasibility unknowns), plus TBC: gating evidence set for SAF-005 and safe-state criteria for SAF-006 pending Vol 13.

## 16. Assumptions

- A-TBD-04: Six requirements encode sufficient Tranche 2 safety scaffolding; validation: SRR plus Vol 13 review.
- Assumption that independence (SAF-003) is achievable within programme constraints; validation: SAD and Vol 13 analyses.

## 17. Dependencies

Depends on stakeholder safety approval (STK-001), mission constraints (MIS-005/006), SAD allocation, Vol 13 analyses, Safety Case structure, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-001, SYS-002/003, MIS-005/006 (see table). Children: Vol 13 analyses and derived safety requirements, subsystem safety specs (Vol 03–18), Safety Case claims, V&V cases, RTM rows. RTM seed for SAF-001..006 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Additions from Vol 13 analyses require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 01.10) |
