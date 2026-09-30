# Derived Requirements — Chapter 01.17

**Document ID:** HFPX-SYS-DER-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture derived system requirements for HFP-X and enforce the derivation rule. This Tranche 8 draft establishes structure only; all quantitative values are TBD.

## 2. Scope

Covers requirements derived from system-level requirements where design, analysis or trade decisions create new obligations. Every derived requirement names its source requirement(s); orphan derivations are rejected. All values TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (Chapter 01.6, source tier)
- HFPX-SYS-ARC-001 SAD (allocation views, TBD)
- Trade and analysis artefacts (Vol 06/19, TBD)
- HFP prompt §§8–10 (requirements format, classification, traceability)

## 4. Definitions & Acronyms

- Derived requirement ID `REQ-HFPX-DRV-NNN`; verification: Analysis / Inspection / Demonstration / Test
- TBD/TBC: unknown data handling; no invented values
- Derivation rule: each DRV requirement shall cite ≥1 source requirement; verification method follows the derivation source

## 5. System Context

Derived requirements close the loop between analysis decisions and the requirement set:

```text
SOURCE (SYS tier) → DERIVATION (analysis/trade) → DERIVED (this document) → SUBSYSTEM → V&V
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-DRV-001 | The system shall implement deterministic primary flight-control bounding derived from source requirement REQ-HFPX-SYS-002 (bounds and scope TBD). | REQ-HFPX-SYS-002 | Analysis + Test |
| REQ-HFPX-DRV-002 | The system shall implement independent safety-path separation derived from source requirement REQ-HFPX-SYS-003 (separation scope TBD). | REQ-HFPX-SYS-003 | Analysis + Inspection |
| REQ-HFPX-DRV-003 | The system shall implement navigation-sensor redundancy management derived from source requirement REQ-HFPX-SYS-004 (management logic and accuracies TBD). | REQ-HFPX-SYS-004 | Analysis + Test |
| REQ-HFPX-DRV-004 | The system shall implement environmental operating envelopes derived from source requirement REQ-HFPX-SYS-006 (envelope values TBD). | REQ-HFPX-SYS-006 | Analysis + Test |

## 7. Architecture

Allocation (SAD owns authoritative allocation): DRV-001 → FCS views; DRV-002 → safety computer + recovery; DRV-003 → nav/sensors; DRV-004 → thermal/environmental views. Allocation table TBD.

## 8. Detailed Design

Not applicable — requirements tier only. Derivation analyses and trade records live in Vol 06/19 and are TBD.

## 9. Interfaces

Derived interface constraints reference Chapter 01.16; ICD details TBD.

## 10. Operational Concept

Derived requirements are exercised through the same CONOPS threads as their source requirements (mapping table TBD in V&V Plan).

## 11. Safety

Derivations affecting safety feed system safety requirements (01.10) and the Safety Case; analyses TBD.

## 12. Performance

No derived performance value is stated; all such values TBD pending source-tier budgets and models.

## 13. Verification & Validation

Each requirement states its method above, following its derivation source; verification cases and IDs are TBD in the V&V Plan (Vol 22). Requirements without a verification method or without a named source are rejected at SRR.

## 14. Risks

- Untraced derivations becoming orphans → mitigation: derivation rule enforced, RTM coverage gate per review
- Source requirements changing underneath derivations; mitigation: change control propagates to derived set

## 15. Open Issues

- Derivation analyses and trade records TBD
- Additional derivations expected as Vol 03–18 and Vol 13 analyses mature

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-tier stability (REQ-HFPX-SYS-002/003/004/006), trade and analysis artefacts, SAD allocation, V&V Plan cases.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-004, REQ-HFPX-SYS-006 (each DRV cites its source in §6). Children: subsystem requirements (Vol 03–18), V&V cases, RTM rows (01.18). RTM seed for DRV-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 8 draft, not baselined. Changes require change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Chapter 01.17) |
