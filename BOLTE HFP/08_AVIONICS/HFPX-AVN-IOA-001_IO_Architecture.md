# I/O Architecture

**Document ID:** HFPX-AVN-IOA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X avionics I/O architecture (Chapter 08.8): I/O channel inventory, sampling/refresh principles, and I/O-fault handling. No channel counts, rates, or parts selected.

## 2. Scope

Covers discrete, analogue, and bus I/O channel classes, sampling/refresh principles, and I/O-fault handling hooks. Excludes sensor/actuator selection, bus protocol selection, wiring design, and quantitative timing values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002/003)
- HFPX-ARC-AVN-001 Avionics Architecture
- Vol 08 data-bus and controller docs (Ch 08.6/08.9)
- Vol 13 (safety analyses: FHA/FMEA hooks)

## 4. Definitions & Acronyms

- I/O: input/output channels linking avionics compute to sensors, actuators, and buses.
- Discrete: binary-state channel class (details TBD).
- Analogue: continuous-signal channel class (details TBD).
- Bus I/O: bus-mediated channel class (details TBD).
- Sampling/refresh: acquisition and update timing principles (values TBD).

## 5. System Context

I/O architecture interconnects compute nodes with sensing, actuation, HMI, and bus nodes across all flight and maintenance states. It bounds channel classes and fault handling; device internals are owned by source subsystems (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-VIO-001|The avionics I/O architecture shall define the I/O channel inventory by class including discrete, analogue, and bus channels (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|
|REQ-HFPX-VIO-002|The avionics I/O architecture shall define sampling and refresh principles for I/O channels (values TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|
|REQ-HFPX-VIO-003|The avionics I/O architecture shall define I/O-fault handling feeding fault logic (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; FHA/FMEA hooks; SFA tier|Inspection|
|REQ-HFPX-VIO-004|The verification approach for avionics I/O architecture shall be defined (TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; SFA tier|Inspection|

## 7. Architecture

I/O classes named by role (discrete/analogue/bus) with channel ownership, direction, and fault-handling hooks. Sampling/refresh principles ensure correlated acquisition across nodes (mechanisms and values TBD). No channel counts or rates stated.

## 8. Detailed Design

Not applicable at this revision. Channel lists, signal conditioning, connector pin-outs, and component selections are TBD in Vol 08 and ICDs. No parts selected.

## 9. Interfaces

I/O interfaces: sensor/actuator channels, bus attachments (Ch 08.6), controller attachments (Ch 08.9), and fault-logic outputs (Ch 08.11). Definitions TBD in ICDs.

## 10. Operational Concept

I/O supports all flight modes plus BIT, degraded/redundant, and maintenance states. Faulted channels are flagged to fault logic while healthy channels remain available (details TBD).

## 11. Safety

I/O faults feed Vol 13 FHA/FMEA. Fail-safe handling of faulted inputs/outputs is TBD. No safety values stated.

## 12. Performance

Channel counts, sampling rates, latency, and availability budgets are TBD. Budget holders: avionics/I/O (Vol 08), safety (Vol 13). No values stated.

## 13. Verification & Validation

Verification approach TBD. Expected later by inspection (channel inventory), analysis (sampling/refresh principles), and integration test (Vol 19). Validation deferred.

## 14. Risks

- Channel-inventory gaps driving ICD rework; mitigation: inventory freeze gate at PDR.
- I/O-fault coverage gaps masking faults; mitigation: coverage analysis tied to Vol 13 FMEA.

## 15. Open Issues

I/O channel inventory, sampling/refresh principles, I/O-fault handling, and verification approach all TBD. Source-subsystem inputs incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on avionics architecture (HFPX-ARC-AVN-001), data-bus design (Ch 08.6), controller allocation (Ch 08.9), fault logic (Ch 08.11), and safety analyses (Vol 13).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks; SFA tier. Children: Vol 08 detail docs, ICDs. RTM: REQ-HFPX-VIO-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.8.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.8) |
