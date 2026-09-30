# Data Logging

**Document ID:** HFPX-AVN-DLG-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define avionics data-logging requirements, architecture, interfaces and analysis-flow scaffolding (Chapter 08.17). Establishes structure only; logged-parameter inventory, rate/capacity/retention, crash-survivability hooks and log-to-analysis flow are TBD.

## 2. Scope

Covers logged-parameter inventory, logging rates, capacity and retention, crash-survivability hooks, and log-to-analysis flow. Parameter selections, rates, formats, retention periods and survivability implementations are TBD. Excludes analysis execution (Vol 23.17, 33.16) and detailed recorder design. No numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-ARC-AVN-001 Avionics Architecture
- VAA tier requirements (TBD)
- Vol 23.17, 33.16 — log-to-analysis flow
- Vol 13 — safety analyses (notably SFA/CCA hooks)

## 4. Definitions & Acronyms

- Logged-parameter inventory: set of avionics parameters recorded; inventory TBD.
- Rate/capacity/retention: logging cadence, storage bounds and hold periods; all TBD.
- Crash-survivability hooks: provisions supporting post-event log recovery; implementations TBD.
- Log-to-analysis flow: transfer of logs into analysis threads (Vol 23.17, 33.16); allocation TBD.
- TBD: To Be Determined.

## 5. System Context

Data logging consumes avionics node outputs, timestamped via time sync (Ch 08.16), and produces stored logs for maintenance, verification and safety analysis. Logs flow to analysis threads (Vol 23.17, 33.16) with crash-survivability hooks for post-event recovery. All inventory, rates and mechanisms TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VDL-001 | The logged-parameter inventory shall be defined; all parameters TBD. | REQ-HFPX-SYS-002, REQ-HFPX-SYS-005 | Inspection |
| REQ-HFPX-VDL-002 | Logging rate, capacity and retention provisions shall be defined; all provisions TBD. | REQ-HFPX-SYS-003 | Analysis |
| REQ-HFPX-VDL-003 | Crash-survivability hooks for log recovery shall be defined; implementations TBD. | REQ-HFPX-SYS-003, SFA hook | Analysis |
| REQ-HFPX-VDL-004 | The log-to-analysis flow shall be defined per Vol 23.17 and 33.16; allocation TBD. | REQ-HFPX-SYS-005, VAA tier | Inspection |

## 7. Architecture

Logging architecture (structure only): LOGGED PARAMETERS (inventory TBD, timestamped via Ch 08.16) → RATE/CAPACITY/RETENTION PROVISIONS (TBD) with CRASH-SURVIVABILITY HOOKS (TBD) → LOG-TO-ANALYSIS FLOW (Vol 23.17, 33.16, TBD), with SFA/CCA hooks (Vol 13, TBD).

## 8. Detailed Design

Not applicable at CONCEPT. Parameter lists, sampling provisions, formats, storage implementations and survivability implementations are TBD and deferred. No design values stated.

## 9. Interfaces

- From avionics nodes/networks: logged-parameter sources — TBD.
- From time sync (Ch 08.16): correlated timestamps — TBD.
- To storage/survivability provisions: log preservation paths — TBD.
- To analysis (Vol 23.17, 33.16): log export and transfer provisions — TBD, ICD before CDR.
- To verification thread (VAA tier): logging verification hooks — TBD.
- To Vol 13: SFA/CCA hooks — TBD.

## 10. Operational Concept

Logging supports all avionics operating states including degraded modes and post-event recovery. Logs are preserved per retention provisions and exported for analysis. No operational logging values are stated.

## 11. Safety

Missing, corrupt or unrecoverable logs impair fault analysis and post-event investigation: REQ-HFPX-VDL-001 (defined inventory), REQ-HFPX-VDL-003 (survivability hooks) and SFA hooks mitigate them. No logging completeness or survivability claim is made; all capability TBD and unproven at CONCEPT.

## 12. Performance

Logging rates, capacity, retention and export budgets are TBD. Budget holder: this document (REQ-HFPX-VDL-001..002) with Vol 23.17 and 33.16. No values stated.

## 13. Verification & Validation

Verified by inspection (parameter inventory and analysis flow) and analysis (rate/capacity/retention and survivability hooks) per VAA tier. Cases trace to REQ-HFPX-VDL-001..004; methods and acceptance criteria TBD. No gate skipping.

## 14. Risks

- Logged-parameter set incomplete for analysis; mitigation: closed inventory required by REQ-HFPX-VDL-001 aligned to Vol 23.17/33.16.
- Capacity/retention shortfalls losing data; mitigation: defined provisions per REQ-HFPX-VDL-002 with gated analysis.
- Post-event log loss; mitigation: crash-survivability hooks per REQ-HFPX-VDL-003.

## 15. Open Issues

Logged-parameter inventory, rate/capacity/retention provisions, crash-survivability implementations, and log-to-analysis allocation are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS SYS-002/003/005, VAA tier, time sync (08.16), health/fault inputs (08.10/08.11), Vol 23.17 and 33.16 analysis threads, and Vol 13 SFA/CCA hooks.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; VAA tier; SFA/CCA hooks. Children: detailed logging design, parameter ICDs, survivability evidence, analysis ICDs (all TBD). RTM: REQ-HFPX-VDL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.17.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.17) |
