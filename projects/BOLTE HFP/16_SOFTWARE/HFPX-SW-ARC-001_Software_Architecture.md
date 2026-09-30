# Software Architecture

**Document ID:** HFPX-SW-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Vol 16 software architecture view (Chapter 16.2): layering, flight and safety partitioning, interface ownership, and advisory-only AI segregation. No code, languages, or tools selected.

## 2. Scope

Covers Vol 16 software layering, flight and safety partition scaffolding, interface ownership scaffolding, and verification-by-review scaffolding. Excludes detailed design, partitioning mechanism selection, timing budgets, and tool qualification (all TBD).

## 3. Applicable Documents

- SYS-002 (parent system requirements)
- HFPX-ARC-SW-001 Software Architecture (parent requirements REQ-HFPX-SWA-001..004)
- DO-178C concepts (structured-according-to only, no compliance claimed)
- Vol 16 sibling documents (Chapters 16.1, 16.3..16.9 structure only)
- VVP thread (verification and validation thread, details TBD)

## 4. Definitions & Acronyms

- Layering: separation of application, middleware and services, and platform functions (contents TBD).
- Flight and safety partitions: separation of primary flight functions from independent safety monitoring functions (mechanism TBD).
- Interface ownership: allocation of responsibility for inter-layer and inter-partition interfaces (TBD).
- Advisory-only AI: AI functions, if present, are segregated advisory outputs that never override pilot or safety authority.

## 5. System Context

Vol 16 software architecture refines the SWA tier for implementation. It receives command, navigation, and health inputs and produces actuator, display, and logging outputs, executed under deterministic bounded primary control with independent safety monitoring across all flight and maintenance states.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-WSA-001 | The software architecture shall define layered software structure (contents TBD). | SYS-002; REQ-HFPX-SWA-001; VVP | Inspection |
| REQ-HFPX-WSA-002 | The architecture shall define flight and safety partitions with independence provisions (mechanism TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection |
| REQ-HFPX-WSA-003 | Primary flight-control software shall be deterministic and bounded and independently verifiable (bounds TBD). | SYS-002; REQ-HFPX-SWA-002; VVP | Inspection |
| REQ-HFPX-WSA-004 | AI functions, if present, shall reside in a segregated advisory partition and never override pilot or safety authority. | SYS-002; REQ-HFPX-SWA-002; VVP | Test |
| REQ-HFPX-WSA-005 | Interface ownership for software layers and partitions shall be defined (TBD) and verified by review. | SYS-002; REQ-HFPX-SWA-004; VVP | Inspection |

## 7. Architecture

Layered structure (layers, contents, languages TBD): application layer (control, navigation, mode management), safety layer (independent monitoring and recovery, thresholds TBD), platform layer (drivers, board support, communications stacks). Flight and safety partitions enforce independence (mechanism TBD). Primary control is deterministic, bounded, and verifiable by policy; AI is advisory-only in a segregated partition. Assurance artefacts are structured according to DO-178C concepts with no compliance claim.

## 8. Detailed Design

Not applicable at this level. Software requirements, design descriptions, and code are deferred to Vol 16 subsystem software items. No implementation stated.

## 9. Interfaces

Software interfaces: inter-partition APIs, sensor and actuator service APIs, bus and log service APIs, display APIs. Signatures, timing, and protocols TBD; interface ownership TBD; detailed in software ICDs and Vol 16.

## 10. Operational Concept

Software executes across power-up, flight-mode, degraded-mode, and maintenance states. The safety partition remains available whenever powered in flight; advisory AI output is display and test-logging only.

## 11. Safety

Determinism, boundedness, partition independence, and advisory-only AI are safety-architecture constraints carried from the SWA tier. Software safety inputs and verification independence feed Vol 13 and the VVP thread. No integrity values stated.

## 12. Performance

Timing, memory, and throughput budgets are TBD. Budget holders: software and compute (Vol 16), control and navigation consumers. No timing figures stated.

## 13. Verification & Validation

Verified by review (layering, partitioning, interface ownership, advisory-only segregation, DO-178C-structured artefact scaffolding). Validated later via analysis, SIL and HIL test, and flight test per the VVP thread (details TBD).

## 14. Risks

- Non-deterministic behaviour leaking into primary control; mitigation: partitioning policy plus independent verification requirement (WSA-002..WSA-004).
- Interface ownership gaps across layers and partitions; mitigation: ownership scaffolding verified by review (WSA-005).

## 15. Open Issues

Layer contents, partitioning mechanism, determinism bounds, interface ownership allocation, and assurance targets all TBD. Language, RTOS, and toolchain selections TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-002 system requirements, SWA tier architecture, control laws (Vol 07), platform selection, and safety analyses (Vol 13). Consumed by Vol 16 software items and software ICDs.

## 18. Traceability

Parents: SYS-002; SWA tier (REQ-HFPX-SWA-001..004); VVP thread. Children: Vol 16 software items (Chapters 16.3..16.9), ICDs, V&V cases. RTM: REQ-HFPX-WSA-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Chapter 16.2.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 16.2) |
