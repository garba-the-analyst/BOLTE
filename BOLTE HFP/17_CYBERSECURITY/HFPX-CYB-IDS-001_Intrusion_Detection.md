# 17.12 Intrusion Detection

**Document ID:** HFPX-CYB-IDS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the structure for HFP-X intrusion detection (Chapter 17.12). This Tranche 6 draft defines the requirement set structure and derivation path; all intrusion detection controls, monitored events and quantitative values are TBD and unselected at this revision.

## 2. Scope

Covers intrusion detection requirements for HFP-X, including detection of anomalous or unauthorised activity described as generic threat classes. Excludes selection of specific security mechanisms and excludes exploit or vulnerability specifics beyond generic threat classes. Response actions are covered in HFPX-CYB-INR-001.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent — security classification)
- Vol 08 / Vol 11 / Vol 16 interface requirements (TBD, parents for monitored boundaries)
- HFPX-CYB-ARC-001 Cybersecurity Architecture (allocation parent)
- HFPX-CYB-THR-001 Threat Model; HFPX-CYB-INR-001 Incident Response
- HFPX-CYB-IDX-001 Volume 17 index (README.md, Chapter 17.12)
- V&V Plan (Vol 22, not written)

## 4. Definitions & Acronyms

- IDS: intrusion detection chapter
- Requirement ID `REQ-HFPX-YID-[NNN]`; verification: Analysis / Inspection / Demonstration / Test / Review
- TBD / TBC: unknown data handling; no invented values
- Intrusion detection control: a measure that detects anomalous or unauthorised activity; all controls TBD (mechanisms unselected)

## 5. System Context

Intrusion detection monitors the system and feeds incident response:

```text
SYS TIER (security classification) → CYB ARCHITECTURE → INTRUSION DETECTION (this document) → INCIDENT RESPONSE → VERIFICATION (Vol 22)
```

Monitored events, placement and reporting paths are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-YID-001|The intrusion detection design shall define monitored events indicative of generic threat classes (events TBD).|HFPX-SYS-REQ-001 (security classification)|Inspection|
| REQ-HFPX-YID-002 | The intrusion detection design shall define where detection applies across subsystems and Vol 08 / Vol 11 / Vol 16 boundaries (placement TBD; all mechanisms unselected). | HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD) | Inspection |
| REQ-HFPX-YID-003 | The intrusion detection design shall define the rule for reporting detected events to incident response (reporting rule TBD). | HFPX-SYS-REQ-001 (security classification) | Analysis |
| REQ-HFPX-YID-004 | Intrusion detection controls shall be traceable to the cybersecurity architecture allocation (tracing TBD). | HFPX-SYS-REQ-001 (security classification) | Inspection |

## 7. Architecture

TBD — detection placement, event groupings and allocation views are undefined at this revision. All security controls TBD (mechanisms unselected).

## 8. Detailed Design

Not applicable — requirements level only. No intrusion detection mechanisms are selected, and no parameter values are defined at this revision.

## 9. Interfaces

Monitored boundaries at Vol 08 / Vol 11 / Vol 16 interfaces are TBD. Interface monitoring rules remain TBD until interface requirements exist.

## 10. Operational Concept

Operational handling of intrusion detection (monitoring, alert handling, maintenance interactions) is TBD. No operational procedure is approved at this revision.

## 11. Safety

No safety claim is made in this document. Coordination with the safety process (Vol 13) on detection with safety relevance is TBD.

## 12. Performance

TBD. No quantitative value is defined or approved at this revision.

## 13. Verification & Validation

Each requirement states its method in §6. Verification cases and evidence records are TBD in the V&V Plan (Vol 22). Requirements without a verification method are rejected at review.

## 14. Risks

- Intrusion detection written before events and placement stabilise → high TBD density; mitigation: structure-only status is explicit
- Overlap with communications monitoring and ground station monitoring; mitigation: allocation traceability (REQ-HFPX-YID-004)
- Mechanism selection ahead of requirements stability; mitigation: all mechanisms remain unselected

## 15. Open Issues

- Monitored events, placement and reporting rules undefined (REQ-HFPX-YID-001..003)
- Allocation tracing undefined (REQ-HFPX-YID-004)
- All intrusion detection controls TBD (mechanisms unselected)

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on system-level security classification (SYS tier), cybersecurity architecture (HFPX-CYB-ARC-001), threat model, incident response (HFPX-CYB-INR-001), Vol 08 / Vol 11 / Vol 16 interface requirements, and V&V Plan cases (Vol 22).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 (security classification); Vol 08 / Vol 11 / Vol 16 interfaces (TBD). Children: intrusion detection design, incident response inputs, V&V cases, RTM rows. RTM seed for REQ-HFPX-YID-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Control selection and event definition require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 17.12, structure only) |
