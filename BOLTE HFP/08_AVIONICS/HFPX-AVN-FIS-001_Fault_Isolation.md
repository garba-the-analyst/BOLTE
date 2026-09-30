# Fault Isolation

**Document ID:** HFPX-AVN-FIS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X avionics fault isolation (Chapter 08.12): isolation-action inventory, isolation authority, inadvertent-isolation protection, and isolation-to-recovery handover. No actions, authorities, or logic selected.

## 2. Scope

Covers isolation actions, authority allocation including safety-computer override hooks, inadvertent-isolation protection, and handover to recovery (Ch 08.13). Excludes detection logic, recovery actions, redundancy design, and quantitative values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002/003)
- HFPX-ARC-AVN-001 Avionics Architecture
- Fault detection (Ch 08.11) and fault recovery (Ch 08.13)
- Vol 13 (safety analyses: FHA/FMEA hooks)

## 4. Definitions & Acronyms

- Fault isolation: action confining a detected fault to prevent propagation (details TBD).
- Isolation authority: entity empowered to command isolation (details TBD).
- Safety-computer override: independent safety-path isolation command with behaviour TBD.
- Inadvertent isolation: unintended isolation of a healthy function.
- Handover: transfer of an isolated fault to recovery logic.

## 5. System Context

Fault isolation consumes detection handovers across all flight and maintenance states and hands isolated faults to recovery. It bounds isolation actions and authority; detection and recovery are owned in Ch 08.11 and Ch 08.13 respectively (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VFI-001 | The avionics fault isolation shall define the isolation-action inventory (details TBD). | HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks | Inspection |
| REQ-HFPX-VFI-002 | The avionics fault isolation shall have defined isolation authority including safety-computer override hooks with behaviour TBD (details TBD). | HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; FHA/FMEA hooks; SFA tier | Analysis |
| REQ-HFPX-VFI-003 | The avionics fault isolation shall provide inadvertent-isolation protection (details TBD). | HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; FHA/FMEA hooks; SFA tier | Test |
| REQ-HFPX-VFI-004 | The avionics fault isolation shall define the isolation-to-recovery handover to Ch 08.13 (details TBD). | HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier | Inspection |

## 7. Architecture

Isolation concept with action inventory, authority allocation (including safety-computer override hooks), interlocks against inadvertent isolation, and handover interface to recovery. No isolation logic or values stated.

## 8. Detailed Design

Not applicable at this revision. Isolation sequences, interlock logic, and implementations are TBD. No logic selected.

## 9. Interfaces

Fault-isolation interfaces: detection handover inputs (Ch 08.11), isolation command outputs to affected functions, safety-computer override path, annunciation/recording hooks, and recovery handover outputs (Ch 08.13). Definitions TBD in ICDs.

## 10. Operational Concept

Fault isolation operates in all flight modes plus BIT, degraded/redundant, and maintenance states. Override and interlock functions remain available in degraded modes (details TBD).

## 11. Safety

Isolation authority, override behaviour, and inadvertent-isolation hazards feed Vol 13 FHA/FMEA. Fail-safe behaviour on isolation failure is TBD. No safety values stated.

## 12. Performance

Isolation latency, coverage, and availability budgets are TBD. Budget holders: avionics (Vol 08), safety (Vol 13). No values stated.

## 13. Verification & Validation

Verification approach TBD. Expected later by analysis (authority/interlock argument) and integration/SIL/HIL test (Vol 19). Validation deferred.

## 14. Risks

- Over-isolation removing healthy capability; mitigation: interlock analysis tied to Vol 13 FMEA.
- Under-isolation allowing fault propagation; mitigation: coverage analysis with review gate.

## 15. Open Issues

Isolation-action inventory, isolation authority (including safety-computer override TBD), inadvertent-isolation protection, and isolation-to-recovery handover all TBD. FHA/FMEA inputs incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on fault detection (Ch 08.11), recovery logic (Ch 08.13), safety-computer design (Ch 08.3), avionics architecture (HFPX-ARC-AVN-001), and safety analyses (Vol 13).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks; SFA tier. Children: Vol 08/13 detail docs, ICDs. RTM: REQ-HFPX-VFI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.12.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.12) |
