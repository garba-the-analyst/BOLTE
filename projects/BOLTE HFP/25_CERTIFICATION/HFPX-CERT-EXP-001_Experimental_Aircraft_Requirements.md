# Experimental Aircraft Requirements

**Document ID:** HFPX-CERT-EXP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how experimental-category authorisation is pursued and bounded for HFP-X demonstrators. Owns Chapter 25.5.

## 2. Scope

Covers experimental-category rules research, operating limitations, MVP/demonstrator authorisation, and unmanned-first alignment. States no experimental finding, lists no limitations, and claims no compliance with any regulation or standard. All regulatory content TBD pending authoritative-source research under ISS-001.

## 3. Applicable Documents

- HFPX-CERT-STR-001 Certification Strategy, HFPX-CERT-RGB-001 Regulatory Basis (this volume)
- HFPX-CERT-FTA-001 Flight-Test Authorisation (this volume, TBD)
- Vol 33 MVP/demonstrator scope (details TBD), Vol 23 test readiness including FRR (Vol 23.13, details TBD)
- Experimental-category regulations, operating-limitation practice, and authority guidance — to be verified from authoritative sources. This document is structured according to general certification-planning practice; no compliance with any regulation or standard is claimed at this revision.

## 4. Definitions & Acronyms

- Experimental category: an authorisation route for non-certified aircraft activity (rules TBD — to be verified from authoritative sources).
- Operating limitations: conditions and restrictions bounding authorised flight (content TBD).
- MVP/demonstrator: early unmanned vehicle(s) used for learning before any human flight (scope TBD, Vol 33).
- TBD/TBC: unknown-data markers only.

## 5. System Context

Experimental authorisation is the near-term route enabling unmanned learning while long-term certified routes remain options:

```text
STRATEGY (25.1) + BASIS (25.2/25.3) → EXPERIMENTAL REQUIREMENTS (25.5)
  → FLIGHT-TEST AUTHORISATION (25.6) + RANGE + FRR (23.13)
  → MVP/DEMONSTRATOR FLIGHTS (Vol 33) → EVIDENCE (25.12)
```

Unmanned-first sequencing is preserved; no human flight is within experimental scope at this revision beyond what future authorised phases (TBD) may address.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-QEX-001 | The programme shall research and record experimental-category rules solely from authoritative sources, with content to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QEX-002 | The programme shall define how operating limitations are obtained, recorded, and flowed to operations and test, with limitation content TBD pending material to be verified from authoritative sources. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QEX-003 | The programme shall define the MVP/demonstrator authorisation sequence, with artifacts and gates TBD. | STK-003, ISS-001 | Inspection |
| REQ-HFPX-QEX-004 | The programme shall align experimental activity with the unmanned-first sequence, such that no human flight is authorised under this chapter at this revision. | STK-003, ISS-001 | Inspection |

Structured according to general requirements practice; no compliance with any regulation or standard is claimed.

## 7. Architecture

Experimental architecture (structure only): rules research → authorisation request → operating limitations → test/range readiness → authorised demonstrator flights → records and feedback to evidence. Each regulatory element TBD — to be verified from authoritative sources.

## 8. Detailed Design

Detail TBD, including: experimental request contents; limitation categories and flow-down to flight operations and range coordination; MVP configuration control; and interface to FRR entrance criteria (Vol 23.13, TBD). No limitations or request contents are stated at this revision.

## 9. Interfaces

- Certification ↔ authority (TBD — to be verified from authoritative sources) for experimental authorisation.
- Certification ↔ Flight Test (Vol 23), Range (TBD), Operations (Vol 27), Safety (Vol 13/24), MVP team (Vol 33).
- Records interface to Vol 25.12 evidence practice (TBD).

## 10. Operational Concept

Research rules → prepare authorisation artifacts → obtain limitations → satisfy FRR and range gates → fly within limitations → record results → feed evidence buildup. Any flight outside limitations stops under the Vol 25.6 stop-rule linkage.

## 11. Safety

Experimental status does not relax safety governance; Vol 13/24 analyses and FRR remain mandatory. Any safety-related experimental rule or limitation is TBD — to be verified from authoritative sources. Structured according to general safety-governance practice; no compliance claimed.

## 12. Performance

Experimental-readiness measures TBD (thresholds TBD, none baselined).

## 13. Verification & Validation

This document is verified by inspection against the template and review checklist (criteria TBD). Validation is programme-authority approval. Authorisation correctness depends on authoritative sources (to be verified from authoritative sources) and authority action; not claimed here. Structured according to general V&V practice; no compliance claimed.

## 14. Risks

- Experimental rules assumed from memory (rules TBD — to be verified from authoritative sources) → invalid request; mitigation: authoritative-source-only research.
- Limitations mis-flowed to operations → non-compliant flight; mitigation: recorded flow-down rule.
- Pressure to advance to human flight early → safety risk; mitigation: unmanned-first alignment rule.

## 15. Open Issues

ISS-001 (experimental-rule research). TBD: rule set, limitation contents, MVP authorisation sequence, FRR/range interfaces. No paragraph citations from memory.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 / SYS tier (TBD); ISS-001; HFPX-CERT-STR-001/RGB-001/FTA-001; Vol 23 (including 23.13 FRR), Vol 33 (MVP), Vol 13/24 (safety), Vol 25.11/25.12.

## 18. Traceability

Parents: STK-003, SYS tier (certification classification), ISS-001. Children: experimental-rules record, limitation records, MVP authorisation artifacts; downstream flight-test authorisations and evidence. RTM: REQ-HFPX-QEX-001..004 → CONCEPT. Regulatory endpoints TBD pending research to be verified from authoritative sources. Structured according to traceability practice; no compliance claimed.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via programme change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 25.5) |
