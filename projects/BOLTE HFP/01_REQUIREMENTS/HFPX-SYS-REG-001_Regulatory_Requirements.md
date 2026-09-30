# Regulatory Requirements — Chapter 01.15

**Document ID:** HFPX-SYS-REG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture system regulatory-compliance requirements for HFP-X in one tier. This Tranche 8 draft establishes structure only; all regulatory content is TBD pending authoritative research.

## 2. Scope

Covers the obligation to identify, track and comply with applicable airworthiness, operational and spectrum obligations. No regulation is cited at this revision; all content TBD pending ISS-001.

## 3. Applicable Documents

- HFPX-SYS-STK-001 Stakeholder Requirements (parent tier, including STK-003 compliance intent)
- HFPX-SYS-REQ-001 SyRS (Chapter 01.6)
- ISS-001 authoritative regulatory research (action open, outcome TBD)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- Regulatory requirement ID `REQ-HFPX-RGT-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- ISS-001: open issue owning authoritative regulatory research; no regulation is cited from memory at this revision

## 5. System Context

Regulatory requirements ensure compliance obligations flow from stakeholder intent into design and evidence:

```text
STAKEHOLDER (STK-003) → REGULATORY (this document, via ISS-001 research) → DESIGN → CERTIFICATION EVIDENCE
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RGT-001 | The system shall comply with identified applicable regulatory obligations (obligation set TBD pending ISS-001 authoritative research). | REQ-HFPX-STK-003 | Inspection |
| REQ-HFPX-RGT-002 | The system shall maintain a traceable register of applicable regulations and compliance evidence (register structure TBD pending ISS-001). | REQ-HFPX-STK-003 | Inspection |
| REQ-HFPX-RGT-003 | The system shall meet defined operational and airspace obligations for test and demonstration activities (obligations TBD pending ISS-001). | REQ-HFPX-STK-003 | Inspection |
| REQ-HFPX-RGT-004 | The system shall meet defined spectrum and equipment-approval obligations for radiating and airborne equipment (obligations TBD pending ISS-001). | REQ-HFPX-STK-003 | Inspection |

## 7. Architecture

Allocation TBD pending ISS-001 outcome; SAD owns authoritative allocation once the obligation set is known.

## 8. Detailed Design

Not applicable — requirements tier only. Compliance implementation lives in affected subsystems and is TBD.

## 9. Interfaces

Regulatory interfaces (range, airspace authority, spectrum authority) reference Chapter 01.16; details TBD pending ISS-001.

## 10. Operational Concept

Regulatory constraints apply to all CONOPS threads; thread-specific obligations TBD pending ISS-001.

## 11. Safety

Regulatory safety obligations feed the Safety Case; mapping TBD pending ISS-001 and Vol 13 analyses.

## 12. Performance

No regulatory performance value is stated; all such values TBD pending ISS-001.

## 13. Verification & Validation

Each requirement states its method above; verification cases and IDs are TBD in the V&V Plan (Vol 22). Inspection via compliance register and evidence review. Requirements without a verification method are rejected at SRR.

## 14. Risks

- Citing regulations from memory would create false compliance claims → mitigation: explicit prohibition at this revision; ISS-001 authoritative research required first
- Obligation set unknown → mitigation: structure-only CONCEPT status, compliance register as controlled artefact

## 15. Open Issues

- ISS-001 (authoritative regulatory research) OPEN — all obligation sets, registers and evidence structures TBD pending its outcome
- No regulation is cited at this revision

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-003 approval, ISS-001 authoritative research outcome, SAD allocation, Safety Case scope, V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-STK-003. Children: subsystem compliance requirements, compliance register entries, V&V cases, RTM rows (01.18). RTM seed for RGT-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.15) |
