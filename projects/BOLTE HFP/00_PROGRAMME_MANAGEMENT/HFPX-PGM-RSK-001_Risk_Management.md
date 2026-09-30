# Risk Management

**Document ID:** HFPX-PGM-RSK-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define risk management for HFP-X: risk process, register discipline, review cadence, escalation and opportunity handling. Owns Chapter 00.12.

## 2. Scope

Covers programme, technical, safety-related, schedule-related and supplier risks, including opportunities. Detailed safety hazard analysis is owned by the safety programme. Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-GOV-001 Project Governance (escalation path)
- HFPX-PGM-REV-001 Design Reviews (risk review at gates)
- Risk register: `00_PROGRAMME_MANAGEMENT/registers/risk_register.csv`

## 4. Definitions & Acronyms

- Risk: uncertain event with cause, effect and handling actions
- Opportunity: uncertain event with potential benefit requiring handling
- Severity / Probability: risk characterisation dimensions (values TBD per risk)
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Risk management operates as a continuing control loop:

```text
IDENTIFY → ANALYSE → MITIGATE → TRACK → REVIEW → ESCALATE
   ↑________________ RISK REGISTER ________________↑
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GRK-001 | The programme shall manage risks through a defined process of identify, analyse, mitigate and track. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GRK-002 | The programme shall maintain a risk register with a defined schema covering identification, cause, effect, severity, probability, mitigation, owner and status. | REQ-HFPX-PGM-002 | Inspection |
| REQ-HFPX-GRK-003 | The programme shall review risks at a defined cadence, with timing and participation recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GRK-004 | The programme shall escalate risks meeting defined conditions along the governance escalation path, with thresholds recorded as TBD at this revision. | REQ-HFPX-PGM-003 | Inspection |
| REQ-HFPX-GRK-005 | The programme shall handle opportunities through identification, assessment and action tracking, with provisions recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |

## 7. Architecture

Risk architecture TBD in detail. Elements: risk register, assessment method, mitigation owners, review forum, escalation linkage. Assessment scales and ownership assignments TBD.

## 8. Detailed Design

Risk process steps, register schema, review cadence, escalation conditions and opportunity provisions TBD, consistent with the register created alongside this document. Severity and probability values per risk are TBD. No assessment thresholds are stated at this revision.

## 9. Interfaces

- To governance (00.2): escalation path for risks
- To reviews (00.14): risk review at gates
- To safety programme: boundary between programme risks and safety hazards
- To change (00.10): risk-driven changes handled by record
- To risk register: living record of risk state

## 10. Operational Concept

Risks and opportunities are raised, assessed, assigned mitigation, tracked to closure or acceptance, reviewed at the defined cadence and escalated when conditions are met. Review scheduling TBD.

## 11. Safety

Programme risk management does not replace independent safety analysis. Safety-impacting risks shall be visible to the safety authority. Coordination provisions TBD.

## 12. Performance

Risk performance indicators TBD. No thresholds are baselined at this revision.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Risks identified but not tracked to mitigation; mitigation TBD
- Risk register diverging from programme reality; mitigation TBD
- Escalation delayed until options narrow; mitigation TBD

## 15. Open Issues

Seed risks RSK-001..RSK-006 are OPEN with severity, probability and owner TBD. See risk register. Further programme risks TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on governance escalation path (00.2), gate review provisions (00.14), safety hazard coordination and issue-register discipline.

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/002/003/004). Children: risk register, risk reviews, mitigation actions (register seeded, remainder TBD). RTM: REQ-HFPX-GRK-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.12) |
