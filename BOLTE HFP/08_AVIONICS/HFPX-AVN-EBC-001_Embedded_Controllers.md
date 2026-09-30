# Embedded Controllers

**Document ID:** HFPX-AVN-EBC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X embedded controllers (Chapter 08.9): controller allocation, firmware ownership, and update/versioning rules. No controllers, processors, or firmware selected.

## 2. Scope

Covers module versus central controller allocation, firmware-ownership hooks to Vol 16.5, and update/versioning rules. Excludes processor selection, board design, software implementation, and quantitative performance values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002/003)
- HFPX-ARC-AVN-001 Avionics Architecture
- Vol 16.5 (firmware/software ownership hooks)
- Vol 13 (safety analyses: FHA/FMEA hooks)

## 4. Definitions & Acronyms

- Embedded controller: avionics compute element hosting firmware/software functions (details TBD).
- Module controller: controller allocated within a subsystem module (details TBD).
- Central controller: shared avionics compute resource (details TBD).
- Firmware ownership: responsibility for firmware lifecycle and configuration (details TBD).

## 5. System Context

Embedded controllers host avionics functions across sensing, compute, HMI, and comms nodes in all flight and maintenance states. They bound allocation and lifecycle rules; implementation is owned with Vol 16.5 (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-VEC-001|The embedded controllers shall have a defined allocation between module and central implementations (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|
|REQ-HFPX-VEC-002|The embedded controllers shall have defined firmware ownership hooks to Vol 16.5 (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|
|REQ-HFPX-VEC-003|The embedded controllers shall follow defined update and versioning rules (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; FHA/FMEA hooks; SFA tier|Inspection|
|REQ-HFPX-VEC-004|The verification approach for embedded controllers shall be defined (TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; SFA tier|Inspection|

## 7. Architecture

Controller allocation named by role (module versus central) with firmware-ownership boundaries to Vol 16.5. Update/versioning rules govern identification, compatibility, and rollback principles (mechanisms TBD). No hardware or firmware selections stated.

## 8. Detailed Design

Not applicable at this revision. Processor selections, board designs, memory maps, and firmware implementations are TBD. No parts selected.

## 9. Interfaces

Controller interfaces: I/O attachments (Ch 08.8), data-bus attachments (Ch 08.6), power feeds (Ch 08.7), and firmware lifecycle interfaces (Vol 16.5). Definitions TBD in ICDs.

## 10. Operational Concept

Controllers support all flight modes plus BIT, degraded/redundant, maintenance, and update states. Version identification remains available in degraded and maintenance states (details TBD).

## 11. Safety

Controller faults feed Vol 13 FHA/FMEA. Safe behaviour on controller fault or failed update is TBD. No safety values stated.

## 12. Performance

Processing, memory, timing, and availability budgets are TBD. Budget holders: avionics/computing (Vol 08/16), safety (Vol 13). No values stated.

## 13. Verification & Validation

Verification approach TBD. Expected later by inspection (allocation and ownership definitions), analysis (update/versioning rules), and integration test (Vol 19). Validation deferred.

## 14. Risks

- Allocation churn driving hardware/software rework; mitigation: allocation freeze gate at PDR.
- Uncontrolled updates breaking compatibility; mitigation: versioning discipline with update gate.

## 15. Open Issues

Controller allocation, firmware ownership, update/versioning rules, and verification approach all TBD. Vol 16.5 hooks incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on avionics architecture (HFPX-ARC-AVN-001), I/O and bus designs (Ch 08.6/08.8), firmware/software lifecycle (Vol 16.5), and safety analyses (Vol 13).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks; SFA tier. Children: Vol 08/16 detail docs, ICDs. RTM: REQ-HFPX-VEC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.9.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.9) |
