# Software Architecture

**Document ID:** HFPX-ARC-SW-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X software architecture (Chapter 02.6): layering, determinism policy, assurance approach and versioning/traceability discipline. No code, languages or tools selected.

## 2. Scope

Covers flight, safety and embedded software layers (TBD), deterministic bounded primary control, assurance structured according to DO-178C concepts, and versioning/traceability per Vol 16. Excludes detailed design, SLOC estimates and tool qualification (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- DO-178C concepts (structured-according-to only, no compliance claimed); Vol 16 (software), Vol 07/08/13

## 4. Definitions & Acronyms

- Deterministic bounded control: primary control executes with predictable behaviour and bounded response (bounds TBD).
- Layers: separation of application, middleware/services, and platform/BSP functions (contents TBD).
- Traceability: linkage from requirements through design, code and verification artefacts.

## 5. System Context

Software architecture implements logical behaviour on the HW-architecture computing paths. It receives command, navigation and health inputs and produces actuator, display and logging outputs across all flight and maintenance states.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-SWA-001 | The software architecture shall define layered flight, safety, and embedded software (contents TBD). | Inspection |
| REQ-HFPX-SWA-002 | Primary flight-control software shall be deterministic and bounded and independently verifiable. | Analysis + Test |
| REQ-HFPX-SWA-003 | Software assurance shall be structured according to DO-178C concepts (no compliance claimed at this stage). | Inspection |
| REQ-HFPX-SWA-004 | The software architecture shall enforce versioning and traceability discipline per Vol 16. | Inspection |

## 7. Architecture

Layered structure (starter; contents, languages and RTOS selections TBD): application layer (control laws, navigation, mode management — laws TBD Vol 07), safety layer (independent monitoring/stabilisation/recovery, thresholds TBD Vol 13), platform layer (drivers, BSP, communications stacks). Primary control is deterministic and bounded by policy with independent verifiability (reviews, analysis, test). AI functions, if present, reside in a segregated advisory partition and never silently override pilot or safety authority (ARC-002). Assurance artefacts follow DO-178C structure without DAL assignment or compliance claim.

## 8. Detailed Design

Not applicable at this level. Software requirements, design descriptions and code are deferred to Vol 16 and subsystem software items. No implementation stated.

## 9. Interfaces

Software interfaces: inter-partition APIs, sensor/actuator service APIs, bus/log service APIs, HMI display APIs. Signatures, timing and protocols TBD; detailed in software ICDs and Vol 16.

## 10. Operational Concept

Software executes across power-up, flight-mode, degraded-mode and maintenance states. Safety partition remains available whenever powered in flight; advisory AI output is display/test-logging only.

## 11. Safety

Determinism/boundedness and partition independence are safety-architecture constraints (ARC-002/003). Software safety inputs and verification independence feed Vol 13/16 plans. No integrity values stated.

## 12. Performance

Timing (WCET, jitter), memory and throughput budgets are TBD. Budget holders: software/compute (Vol 16/08), control (Vol 07). No values stated.

## 13. Verification & Validation

Verified by analysis (determinism argument, layering/partitioning review) and inspection (DO-178C-structured artefact list, versioning discipline). Validated later via SIL/HIL, coverage analysis and flight test (Vol 19).

## 14. Risks

- Non-deterministic behaviour leaking into primary control; mitigation: partitioning policy + independent verification requirement (SWA-002).
- Traceability collapse across layers; mitigation: Vol 16 discipline enforced from Tranche 2.

## 15. Open Issues

Layer contents, partitioning mechanism, determinism bounds, DAL-equivalent targets and toolchains all TBD. Versioning scheme details per Vol 16 TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on HW view separation, LOG flows, control laws (Vol 07), platform selection (Vol 08/16), and safety analyses (Vol 13). Versioning discipline owned by Vol 16.

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-002/003). Children: Vol 03–18 subsystem docs (esp. Vol 16), ICDs, V&V cases. RTM: REQ-HFPX-SWA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.6.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.6) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
