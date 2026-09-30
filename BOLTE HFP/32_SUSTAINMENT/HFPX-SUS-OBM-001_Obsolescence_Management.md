# Obsolescence Management

**Document ID:** HFPX-SUS-OBM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X obsolescence management framework for anticipating, mitigating and resolving component and technology obsolescence through life. Owns Chapter 32.9.

## 2. Scope

Covers obsolescence monitoring, mitigation planning, resolution governance and design-interface linkage. Does not set technical values. Monitoring approach is TBD; resolution provisions including lifetime-buy considerations are TBD; redesign triggers are TBD; hooks to Vol 08.4 apply.

## 3. Applicable Documents

- HFPX-SUS-PLC-001 Product Lifecycle
- HFPX-SUS-CBL-001 Configuration Baselines
- Design and component concepts (Vol 08.4 hooks, details TBD)
- Vol 24 safety assurance concepts (details TBD)
- Vol 27 support concepts (details TBD)
- Vol 28 configuration and records concepts (details TBD)

## 4. Definitions & Acronyms

- Obsolescence: loss of availability of a component, material, process or technology needed to sustain the product
- Mitigation: planned action reducing obsolescence impact, including resolution selection
- TBD/TBC: unknown data markers; unknown values are never invented

## 5. System Context

Obsolescence management anticipates supply risk before impact:

```text
SUPPLY BASE → MONITORING (TBD) → RISK ASSESSMENT → MITIGATION → RESOLUTION → BASELINE UPDATE
    ↑________ Vol 08.4 DESIGN HOOKS ________↑
    ↑________ CONFIGURATION CONTROL ________↑
```

Monitoring scope, mitigation options and redesign triggers remain TBD at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UOM-001 | Components and technologies at obsolescence risk shall be monitored under a defined monitoring approach. | Lifecycle phase definition (TBD) | Inspection |
| REQ-HFPX-UOM-002 | Obsolescence mitigations, including lifetime-buy considerations where applicable, shall be planned with recorded rationale. | Vol 27 / Vol 28 hooks (TBD) | Inspection |
| REQ-HFPX-UOM-003 | Obsolescence resolutions requiring redesign shall be governed through defined redesign triggers and change control. | Vol 08.4 hooks (TBD) | Demonstration |
| REQ-HFPX-UOM-004 | Obsolescence resolutions with safety relevance shall retain alignment with safety assurance. | Vol 24 hooks (TBD) | Inspection |

## 7. Architecture

Obsolescence organisation (roles TBD): obsolescence focal, design authority, supply liaison and safety concurrence with monitoring tooling TBD. Alignment with Vol 08.4 design governance TBD.

## 8. Detailed Design

Monitored item scope, risk assessment method, mitigation catalogue and redesign trigger framework to be defined (TBD). Monitoring, lifetime-buy provisions and redesign triggers are TBD and not baselined at this revision.

## 9. Interfaces

- Obsolescence ↔ design (Vol 08.4) for resolution and redesign governance
- Obsolescence ↔ configuration (32.2) and change control (00.10) for embodiment
- Obsolescence ↔ support (Vol 27) for supply and spares linkage
- Obsolescence ↔ safety (Vol 24) for safety-relevant resolution review

## 10. Operational Concept

Obsolescence operates as a watch loop: monitor → assess risk → plan mitigation → resolve → update baseline → record. Review forums and cadence TBD.

## 11. Safety

Obsolescence resolutions affecting safety-related items require safety assessment (mechanisms TBD, Vol 24 hooks). No safety thresholds are set in this document.

## 12. Performance

Obsolescence indicators TBD (monitoring coverage criteria TBD, mitigation planning completeness criteria TBD). No thresholds baselined.

## 13. Verification & Validation

This document is verified by inspection against the document template checklist (header, 20 sections, IDs, traceability). Requirements REQ-HFPX-UOM-001..004 verified per §6. Validation: programme authority approval (TBD).

## 14. Risks

- Unmonitored supply base → surprise unavailability; mitigation: define monitoring (TBD)
- Unplanned resolutions → hasty redesign or stock decisions; mitigation: mitigation planning (TBD)
- Unassessed substitutions → safety or compliance impact; mitigation: Vol 08.4 and Vol 24 linkage (TBD)

## 15. Open Issues

Monitoring scope and method, mitigation catalogue, lifetime-buy provisions, redesign triggers and Vol 08.4 interface details to be defined. All open details recorded as TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 08.4 design concepts, Vol 27 support concepts, configuration baselines (32.2), Vol 24 safety assurance and Vol 28 records.

## 18. Traceability

Parent: lifecycle phase definition, Vol 08.4 / Vol 24 / Vol 27 / Vol 28 hooks. Children: upgrade and improvement embodiments arising from obsolescence (32.6, 32.8). RTM: REQ-HFPX-UOM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Future changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 32.9) |
