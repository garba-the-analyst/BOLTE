# Built-In Test

**Document ID:** HFPX-AVN-BIT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define avionics built-in test (BIT) requirements, architecture, interfaces and maintenance flow scaffolding (Chapter 08.15). Establishes structure only; BIT scope, coverage, annunciation and maintenance flow are TBD.

## 2. Scope

Covers BIT scope across power-up, continuous and initiated test, BIT coverage policy, BIT-fault annunciation, and BIT-to-maintenance flow. Test thresholds, coverage values, annunciation timing and maintenance procedures are TBD. Excludes detailed test design and maintenance execution (Vol 27). No numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (notably REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-ARC-AVN-001 Avionics Architecture
- VAA tier requirements (TBD)
- Vol 27 — maintenance flow
- Vol 13 — safety analyses (notably SFA/CCA hooks)

## 4. Definitions & Acronyms

- BIT: Built-In Test — avionics self-test capability; scope TBD.
- Power-up BIT: self-test executed at power application; scope TBD.
- Continuous BIT: background monitoring during operation; scope TBD.
- Initiated BIT: operator or maintainer commanded test; scope TBD.
- BIT coverage: extent of faults addressed by BIT; policy TBD.
- BIT-fault annunciation: reporting of BIT-detected faults; provisions TBD.
- TBD: To Be Determined.

## 5. System Context

BIT spans avionics nodes and networks, consuming self-test stimuli and producing BIT-fault annunciations to health monitoring, fault logic and maintenance. BIT outcomes flow to maintenance (Vol 27) and safety hooks (Vol 13). All scope, coverage and timing TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VBT-001 | The BIT scope, including power-up, continuous and initiated test, shall be defined; all scope TBD. | REQ-HFPX-SYS-002, REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-VBT-002 | The BIT coverage policy shall be defined; coverage claims TBD. | REQ-HFPX-SYS-003, CCA hook | Analysis |
| REQ-HFPX-VBT-003 | BIT-fault annunciation, including reporting paths and conditions, shall be defined; provisions TBD. | REQ-HFPX-SYS-003, SFA hook | Analysis + Test |
| REQ-HFPX-VBT-004 | The BIT-to-maintenance flow shall be defined per Vol 27; allocation TBD. | REQ-HFPX-SYS-005, VAA tier | Inspection |

## 7. Architecture

BIT architecture (structure only): BIT STIMULI (power-up, continuous, initiated, TBD) → COVERAGE POLICY (TBD) → BIT-FAULT ANNUNCIATION (TBD) → MAINTENANCE FLOW (Vol 27, TBD), with SFA/CCA hooks (Vol 13, TBD).

## 8. Detailed Design

Not applicable at CONCEPT. Test sequences, thresholds, coverage implementations, annunciation logic and maintenance data formats are TBD and deferred. No design values stated.

## 9. Interfaces

- Within avionics nodes/networks: BIT stimulus and response paths — TBD.
- To health/fault logic (Ch 08.10/08.11): BIT-fault annunciations — TBD.
- To maintenance (Vol 27): BIT results and download provisions — TBD, ICD before CDR.
- To verification thread (VAA tier): BIT verification hooks — TBD.
- To Vol 13: SFA/CCA hooks — TBD.

## 10. Operational Concept

BIT supports ground and flight states as applicable: power-up BIT at application of power, continuous BIT during operation, initiated BIT on command. Behaviour in degraded modes is TBD. No operational BIT values are stated.

## 11. Safety

Undetected faults, nuisance BIT trips or missed annunciation are hazardous: REQ-HFPX-VBT-002 (coverage policy), REQ-HFPX-VBT-003 (defined annunciation) and SFA/CCA hooks mitigate them. No coverage claim is made; all capability TBD and unproven at CONCEPT.

## 12. Performance

BIT coverage, detection latency, false-alarm behaviour and resource budgets are TBD. Budget holder: this document (REQ-HFPX-VBT-001..003) with Vol 27 and Vol 13. No values stated.

## 13. Verification & Validation

Verified by inspection (BIT scope and maintenance flow) and analysis/test (coverage and annunciation) per VAA tier. Cases trace to REQ-HFPX-VBT-001..004; methods and acceptance criteria TBD. No gate skipping.

## 14. Risks

- BIT coverage gaps masking faults; mitigation: coverage policy required by REQ-HFPX-VBT-002 with gated analysis.
- Nuisance BIT annunciation eroding trust; mitigation: defined annunciation provisions per REQ-HFPX-VBT-003.
- BIT results not usable by maintenance; mitigation: defined BIT-to-maintenance flow per REQ-HFPX-VBT-004 aligned to Vol 27.

## 15. Open Issues

BIT scope, coverage policy and claims, annunciation provisions, and BIT-to-maintenance allocation are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS SYS-002/003/005, VAA tier, health monitoring (08.10), fault detection (08.11), Vol 27 maintenance flow, and Vol 13 SFA/CCA hooks.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; VAA tier; SFA/CCA hooks. Children: detailed BIT design, annunciation ICDs, maintenance ICDs, V&V evidence (all TBD). RTM: REQ-HFPX-VBT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.15.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.15) |
