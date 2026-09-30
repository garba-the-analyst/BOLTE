# Pilot Controls

**Document ID:** HFPX-HUM-CTL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define pilot-controls requirements for HFP-X (Chapter 12.6). This Tranche 6 draft establishes control-inventory, feel, inadvertent-operation, and flight-control interface placeholders; all values are TBD.

## 2. Scope

Covers pilot control inventory, control feel provisions, inadvertent-operation protection, and the flight-control system interface. Excludes ergonomics envelopes (12.5), pilot-interface labelling (12.13), and FCS detailed design, which is Vol 07 scope including Chapter 07.3.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — training/evaluation inputs to follow)
- Vol 07 FCS including Chapter 07.3 (TBD), HFPX-HUM-ARC-001 (Chapter 12.1)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UCT: pilot-controls requirement tier; IDs `REQ-HFPX-UCT-NNN`; verification TBD.
- FCS: Flight Control System.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Pilot controls refine system-level workload and interface needs into testable placeholders:

```text
STK-002 + HUM tier → UCT-001..004 → control / FCS detail (Vol 07.3) → V&V cases
```

No control layout, feel, or protection value is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-UCT-001 | The system shall provide a defined pilot-control inventory covering defined functions and phases (control inventory TBD). | STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD) | Inspection |
| REQ-HFPX-UCT-002 | Pilot controls shall provide defined feel provisions supporting intended operation (feel provisions TBD). | STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD) | Inspection |
| REQ-HFPX-UCT-003 | The system shall protect against inadvertent operation of pilot controls under defined conditions (protection provisions TBD). | STK-002, REQ-HFPX-HUM-001, HSA tier (ID TBD) | Demonstration |
| REQ-HFPX-UCT-004 | Pilot controls shall interface to the flight control system at defined provisions (FCS interface TBD; Vol 07.3 detail to follow). | STK-002, REQ-HFPX-HUM-002, HSA tier (ID TBD) | Test |

All inventories, provisions, and interfaces are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UCT-001/002/003 → pilot controls and protection provisions; UCT-004 → FCS interface (Vol 07.3). V&V framework hooks to Vol 30. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Control types, layouts, guarding, and FCS interface detail are TBD in follow-on revisions.

## 9. Interfaces

Control interfaces (inceptors, guards, linkages, FCS signals) are TBD in Vol 02 ICDs, Vol 07.3, and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Control requirements apply across preparation, flight, emergency, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Control failures, inadvertent operation, and FCS-interface faults feed Vol 13 safety analyses (to follow). No UCT requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UCT requirement quantifies performance. All control-related measures are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, task scenarios, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 07/12/30 inputs. No controls credit is claimed at this revision.

## 14. Risks

- Control inventory undefined → late functional gaps; mitigation: early UCT-001 placeholder plus review gates.
- Inadvertent-operation protection undefined → safety-driven redesign; mitigation: UCT-003 placeholder plus Vol 13 coordination.

## 15. Open Issues

TBD: control inventory, feel provisions, inadvertent-operation protection, and FCS interface definition pending Vol 07.3, HSA-tier, and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 07.3 FCS work, Chapter 12.1 architecture, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-001, REQ-HFPX-HUM-002), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: control specs, Vol 07.3 interface specs, V&V cases, RTM rows. RTM seed for UCT-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or interface changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.6) |
