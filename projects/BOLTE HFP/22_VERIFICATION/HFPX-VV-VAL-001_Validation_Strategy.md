# Validation Strategy

**Document ID:** HFPX-VV-VAL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X validation approach for Volume 22.2, distinguishing validation (right thing built) from verification (built right) and setting stakeholder acceptance and records discipline.
This document sets strategy only; it contains no build, ignition, or operation instructions.

## 2. Scope

Covers validation planning for stakeholder needs, operational concepts, and acceptance threads across all volumes.
Governs validation tailoring, stakeholder acceptance, environments, and records; verification execution detail remains with Vol 22.3–22.13 and Vol 23.
Applies from SRR through acceptance; detailed validation cases and procedures are TBD in child documents.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — method assignment, VCRM, levels, gating, acceptance, independence)
- HFPX-PGM-SEM-001 SEMP (gated reviews, requirements management)
- HFPX-SYS-REQ-001 SyRS, HFPX-SYS-ARC-001 SAD (stub), HFPX-PGM-CHR-001 Programme Charter
- HFPX-SAFE-CAS-001 Safety Case, Vol 13 (hazards), Vol 19 (analysis), Vol 23 (test execution), Vol 25 (certification)

## 4. Definitions & Acronyms

- Validation: confirmation that stakeholder needs and intended use are met in a representative environment
- Verification: confirmation that requirements are met by the built article
- Tailoring: documented scoping of validation depth per thread; criteria TBD
- Stakeholder: authority or user role accepting validation outcomes; roles TBD

## 5. System Context

Validation closes the left-hand side of the V-model (needs and concepts) against the right-hand side (acceptance and system evidence):

```text
STAKEHOLDER NEEDS → CONCEPTS → REQUIREMENTS → DESIGN → BUILD
     ↑                                                       ↓
     └────────────── VALIDATE (representative use) ← ACCEPT ┘
```

Validation threads are traced in the VCRM alongside verification threads; validation records are retained per programme records rules TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VVL-001 | The programme shall distinguish validation from verification by a documented tailoring rule, with validation scope and tailoring per thread recorded as TBD. | REQ-HFPX-VVP-001 | Inspection |
| REQ-HFPX-VVL-002 | The programme shall obtain stakeholder acceptance of validation outcomes against acceptance criteria recorded as TBD per validation thread. | REQ-HFPX-VVP-005 | Inspection |
| REQ-HFPX-VVL-003 | The programme shall retain validation records for each validation thread, with record content and retention defined as TBD. | REQ-HFPX-VVP-005 | Inspection |
| REQ-HFPX-VVL-004 | The programme shall perform validation in representative environments and configurations, with representativeness criteria recorded as TBD per thread. | REQ-HFPX-VVP-003 | Inspection |

## 7. Architecture

Validation organisation and roles TBD, operating under the VV Plan governance and SEMP gates.
Validation threads map to stakeholder needs, operational concepts, and acceptance threads; allocation to levels and environments TBD.
VCRM records validation threads distinctly from verification threads; schema owned by Vol 22.3.

## 8. Detailed Design

Validation planning occurs early (needs and concept reviews) with validation cases defined before acceptance; case IDs and procedures TBD.
Each validation case template shall contain objective, traced parent need or requirement, environment and configuration, acceptance criteria (TBD per case), and stakeholder witness provisions TBD.
Regression policy for validation after requirements change is TBD per change record.

## 9. Interfaces

- Validation ↔ Verification (Vol 22.3–22.13): shared VCRM traceability, distinct thread types
- Validation ↔ SE (SEMP gates; entrance and exit criteria TBD)
- Validation ↔ Safety (Vol 13 and Safety Case: safety-relevant validation threads and closure evidence)
- Validation ↔ Certification (Vol 25 defines certification credit; no credit claimed in this revision)

## 10. Operational Concept

Validation operates needs-to-acceptance: define validation threads early → develop criteria and environments → execute on representative articles → obtain stakeholder acceptance → archive records.
Cadence, board membership, and tooling TBD in Vol 22 and Vol 23 children.

## 11. Safety

Safety-relevant validation threads are identified in the VCRM and witnessed per independence rules TBD.
No validation thread authorises human flight; flight gating is owned by the VV Plan, Safety Case, and FRR with criteria TBD.

## 12. Performance

Validation performance indicators TBD, with all thresholds TBD: validation coverage, acceptance closure burn-down, criteria definition backlog.
Measurement method and reporting cadence TBD in Vol 22 children.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the validation strategy is programme authority approval at gated reviews; certification validation is owned by Vol 25 with no claims here.

## 14. Risks

- Validation conflated with verification, leaving stakeholder needs unconfirmed; mitigation: tailoring rule per REQ-HFPX-VVL-001 with VCRM thread typing
- Stakeholder acceptance criteria left TBD indefinitely; mitigation: per-thread TBD tracking with owning volume and due gate (assignments TBD)
- Unrepresentative validation environments weakening acceptance claims; mitigation: representativeness criteria per REQ-HFPX-VVL-004 (criteria TBD)

## 15. Open Issues

Validation case IDs TBD. Acceptance criteria TBD per thread. Stakeholder roles and witness rules TBD. Environment representativeness criteria TBD. Records tooling TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology and gating, SEMP process and gates, SyRS needs and requirements, SAD allocation, Safety Case and Vol 13 safety inputs, Vol 19 analysis capability, Vol 23 execution capability, Vol 25 certification rules.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-003, REQ-HFPX-VVP-005. Children: validation case documents and procedures (IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VVL-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.2 direction; structure only) |
