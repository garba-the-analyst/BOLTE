# Flight Computer

**Document ID:** HFPX-AVN-FLC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X flight computer (Chapter 08.2): deterministic execution, input/output capacity, growth/spare policy, development-assurance scaffolding, and verification thread. No parts, topologies, or values selected.

## 2. Scope

Covers flight-computer execution principles, I/O capacity definition, growth/spare capacity policy, assurance scaffolding structured according to recognised concepts, and verification approach. Excludes hardware selection, scheduling design, bus selection, and quantitative budgets (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-SYS-ARC-001 SAD (AVN, HWA, SWA, DAT views)
- HFPX-AVN-ARC-001 Avionics Architecture (Chapter 08.1)
- Vol 08 Chapters 08.4–08.6 (hardware, real-time, bus context)

## 4. Definitions & Acronyms

- Flight computer: primary computing path for flight functions.
- Deterministic execution: repeatable execution behaviour under defined conditions.
- WCET: worst-case execution time concept (value TBD).
- SIL/HIL: software/hardware-in-the-loop verification concepts.
- Assurance scaffolding: document and process structure organised according to recognised concepts.

## 5. System Context

The flight computer hosts flight functions and exchanges data with sensors, actuators, the safety computer, and ground interfaces. Timing, capacity, and environmental details are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VFC-001 | The flight computer shall provide deterministic execution of allocated functions (execution bounds including WCET TBD). | REQ-HFPX-SYS-003; SAD SWA view | Analysis |
| REQ-HFPX-VFC-002 | The flight computer shall define input/output capacity for allocated interfaces (capacity details TBD). | REQ-HFPX-SYS-002; SAD HWA view | Inspection |
|REQ-HFPX-VFC-003|The flight computer shall define a growth and spare-capacity policy (margins TBD).|REQ-HFPX-SYS-002; SAD AVN view|Inspection|
|REQ-HFPX-VFC-004|The flight computer development artefacts shall be structured according to DO-178C and DO-254 concepts (details TBD).|REQ-HFPX-SYS-005; SAD SWA view|Inspection|
| REQ-HFPX-VFC-005 | The flight computer shall be verified through a defined thread including SIL, HIL, and test (cases and coverage TBD). | REQ-HFPX-SYS-005; SAD AVN view | Test |

## 7. Architecture

Flight-computer concept (details TBD): execution environment, I/O groupings, and assurance artefact structure. Determinism is stated as a principle with bounds TBD. I/O and growth provisions are defined as policies without values. No devices, topologies, or schedules selected.

## 8. Detailed Design

Not applicable at this revision. Hardware design, software design, and interface wiring are deferred to Vol 08 detail and ICDs. No parts selected.

## 9. Interfaces

Flight-computer interfaces: sensor/actuator data exchanges, safety-computer coordination, data-bus attachments, power feeds, and test interfaces. Definitions are TBD in ICDs.

## 10. Operational Concept

Flight computer supports flight modes plus built-in test, degraded, and maintenance states. Deterministic behaviour is required across supported modes with details TBD.

## 11. Safety

Determinism, capacity policy, and structured assurance artefacts support parent safety intent. Fault annunciation feeds safety analyses. No safety values stated.

## 12. Performance

Execution bounds, I/O capacity, and growth margins are TBD. No values stated.

## 13. Verification & Validation

Verified by analysis (determinism argument), inspection (I/O and policy definitions), and review (assurance structure). Validated later by SIL, HIL, and test with cases and coverage TBD.

## 14. Risks

- Execution non-determinism discovered late; mitigation: early determinism analysis thread.
- I/O growth exceeding provision; mitigation: spare-capacity policy with review gate.

## 15. Open Issues

Execution bounds, I/O details, growth margins, assurance details, and verification cases are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS, SAD AVN/HWA/SWA/DAT views, Chapter 08.1 architecture, and Vol 08 hardware/real-time/bus chapters.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; SAD AVN/HWA/SWA/DAT views. Children: Vol 08 detail and verification artefacts. RTM: REQ-HFPX-VFC-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.2.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.2) |
