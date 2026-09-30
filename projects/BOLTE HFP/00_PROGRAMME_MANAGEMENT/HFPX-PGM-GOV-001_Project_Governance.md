# Project Governance

**Document ID:** HFPX-PGM-GOV-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define programme-level governance for HFP-X: authority structure, decision rights, board cadence and escalation. Owns Chapter 00.2.

## 2. Scope

Covers governance of all programme volumes and backbone documents. Defines who may decide, how decisions are recorded, and how issues escalate. Does not set technical values. Does not assign named individuals.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-PGM-SEM-001 SEMP
- HFPX-PGM-ORG-001 Organisation and Responsibilities (sibling, owns roles)
- HFPX-PGM-REV-001 Design Reviews (gate decisions)
- HFPX-PGM-EDR-001 Engineering Decision Records (decision recording)

## 4. Definitions & Acronyms

- Governance: authority, accountability and decision-making framework for the programme
- Board: formally convened decision body; membership TBD
- Escalation: movement of a decision or issue to a higher authority
- TBD / TBC: to be determined / to be confirmed

## 5. System Context

Governance sits above all technical activity:

```text
BOLTE PROGRAMME AUTHORITY → HFP-X GOVERNANCE (this document)
    → SEMP PROCESSES → TECHNICAL VOLUMES → GATES → BASELINES
    → ESCALATION PATH (TBD) → DECISION RECORDS
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-GOV-001 | The programme shall define and maintain a programme authority structure, with accountabilities at each level recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GOV-002 | The programme shall define decision rights for baseline approval, gate passage, change approval and safety matters, recorded as TBD at this revision. | REQ-HFPX-PGM-004 | Inspection |
| REQ-HFPX-GOV-003 | The programme shall define a governance board cadence, including convening criteria and quorum rules, recorded as TBD at this revision. | REQ-HFPX-PGM-001 | Inspection |
| REQ-HFPX-GOV-004 | The programme shall define an escalation path from working level to programme authority, including entry conditions and time expectations recorded as TBD at this revision. | REQ-HFPX-PGM-003 | Inspection |

## 7. Architecture

Governance architecture TBD. Anticipated elements: programme authority, control boards, safety authority with independence, gate authorities. Membership, chairing and voting rules TBD. No named appointments are made at this revision.

## 8. Detailed Design

Authority structure, decision-rights matrix, board terms of reference and escalation flowchart TBD. Each governance element shall identify its authority source, scope of decisions, records produced and link to decision records. No thresholds or cadence values are stated at this revision.

## 9. Interfaces

- To organisation (00.3): roles that fill governance seats
- To SEMP (00.4): processes that governance controls
- To reviews (00.14): gate decisions requiring governance authority
- To decision records (00.16): recording of governance decisions
- To safety and certification authorities: independence of safety decisions

## 10. Operational Concept

Governance operates by convening boards against defined entry conditions, recording decisions as decision records, and escalating unresolved matters along the defined path. Meeting cadence and convening triggers TBD.

## 11. Safety

Governance shall preserve safety independence: safety matters escalate through the safety authority independent of schedule or performance pressure. Safety veto arrangements TBD.

## 12. Performance

Governance performance indicators TBD. No thresholds are baselined at this revision. Candidate indicators (decision lead time, escalation backlog, action closure) remain TBD.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, sections, identifiers, traceability) at the applicable gate. Validation is by programme authority approval (approver TBD).

## 14. Risks

- Unassigned authority leading to stalled decisions; mitigation TBD
- Overlapping decision rights causing conflicting direction; mitigation TBD
- Escalation path undefined causing issues to remain at working level; mitigation TBD

## 15. Open Issues

_TBD_

All open issues are recorded in the issue register. No issue is closed by this revision.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Charter (authority source), organisation definition (00.3), gate criteria (00.14) and decision-record process (00.16).

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/003/004). Children: board terms of reference, decision-rights matrix, escalation procedure (all TBD). RTM: REQ-HFPX-GOV-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 00.2) |
