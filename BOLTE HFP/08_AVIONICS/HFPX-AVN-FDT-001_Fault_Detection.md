# Fault Detection

**Document ID:** HFPX-AVN-FDT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X avionics fault detection (Chapter 08.11): detectable-fault inventory, detection-method ownership, false-alarm policy, and detection-to-isolation handover. No thresholds, latencies, or logic selected.

## 2. Scope

Covers detectable faults, detection-method ownership, false-alarm policy, and handover to isolation (Ch 08.12). Excludes isolation actions, recovery actions, redundancy switching, and quantitative threshold/latency values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002/003)
- HFPX-ARC-AVN-001 Avionics Architecture
- Health monitoring (Ch 08.10) and fault isolation (Ch 08.12)
- Vol 13 (safety analyses: FHA/FMEA hooks)

## 4. Definitions & Acronyms

- Fault detection: determination that a fault condition exists (methods TBD).
- Detectable fault: fault in the detection inventory (details TBD).
- False alarm: detection output without a corresponding fault condition.
- Handover: transfer of a detected fault to isolation logic.

## 5. System Context

Fault detection consumes health-monitoring outputs across all flight and maintenance states and hands detected faults to isolation. It bounds what is detectable and how detections are qualified; isolation and recovery are owned in Ch 08.12–08.13 (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-VFD-001|The avionics fault detection shall define the detectable-fault inventory (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks|Inspection|
|REQ-HFPX-VFD-002|The avionics fault detection shall have defined detection-method ownership with thresholds and latency TBD (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; FHA/FMEA hooks; SFA tier|Inspection|
|REQ-HFPX-VFD-003|The avionics fault detection shall follow a defined false-alarm policy (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|
|REQ-HFPX-VFD-004|The avionics fault detection shall define the detection-to-isolation handover to Ch 08.12 (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|

## 7. Architecture

Detection concept with fault inventory, method ownership per fault (thresholds/latency TBD), false-alarm qualification, and handover interface to isolation. No detection logic or values stated.

## 8. Detailed Design

Not applicable at this revision. Detection algorithms, threshold tables, timers, and implementations are TBD. No logic selected.

## 9. Interfaces

Fault-detection interfaces: health-monitoring inputs (Ch 08.10), annunciation/recording hooks, and isolation handover outputs (Ch 08.12). Definitions TBD in ICDs.

## 10. Operational Concept

Fault detection operates in all flight modes plus BIT, degraded/redundant, and maintenance states. Handover to isolation remains available in degraded modes (details TBD).

## 11. Safety

Detection coverage, missed-detection, and false-alarm hazards feed Vol 13 FHA/FMEA. Safety-path interactions are TBD. No safety values stated.

## 12. Performance

Detection latency, coverage, and false-alarm budgets are TBD. Budget holders: avionics (Vol 08), safety (Vol 13). No values stated.

## 13. Verification & Validation

Verification approach TBD. Expected later by analysis (coverage and false-alarm argument) and integration/SIL/HIL test (Vol 19). Validation deferred.

## 14. Risks

- Detection gaps allowing faults to propagate; mitigation: coverage analysis tied to Vol 13 FMEA.
- Excessive false alarms triggering unwarranted isolation; mitigation: false-alarm policy with review gate.

## 15. Open Issues

Detectable-fault inventory, detection-method ownership (thresholds/latency TBD), false-alarm policy, and detection-to-isolation handover all TBD. FHA/FMEA inputs incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on health monitoring (Ch 08.10), isolation logic (Ch 08.12), avionics architecture (HFPX-ARC-AVN-001), and safety analyses (Vol 13).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks; SFA tier. Children: Vol 08/13 detail docs, ICDs. RTM: REQ-HFPX-VFD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.11.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.11) |
