# Thrust Allocation

**Document ID:** HFPX-FCS-ALC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X thrust-allocation function (Chapter 07.16): distribution of generalised control demands across arm, rear, and ankle propulsion-module groups, including failed-module reallocation, optimisation-criteria ownership, the allocation-to-mixing interface, and verification ownership.

## 2. Scope

Covers allocation structure, ownership, and methodology for the production-aircraft concept across hover, transition, and cruise. Module geometry, effectiveness data, allocation matrices, optimisation weights, gains, margins, and limits are TBD. Allocation ownership and methods only — no numeric values are allocated in this document.

**Hazardous-subsystem boundary note:** This document covers control design, analysis, and test methodology only. It contains no propulsion build, integration, maintenance, or operation instructions. Propulsion implementation is owned elsewhere (Vol 05 / PRP-002). This document shall not be used as a build or operating instruction for any propulsion subsystem.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001, SYS-002, SYS-003)
- HFPX-SYS-ARC-001 SAD (ARC-004 — determinism/modularity allocation)
- HFPX-ARC-CTL-001 Control Architecture (CTL-002, CTL-004)
- HFPX-FCS-MIX-001 Propulsion Mixing (companion, Ch 07.15); HFPX-FCS-AUT-001 Control Authority (Ch 07.17); HFPX-FCS-FTC-001 Fault-Tolerant Control (Ch 07.18)
- HFPX-PRP-xxx Propulsion (PRP-002 interface); HFPX-SFA-001 Safety Architecture (SFA-001); HFPX-VVP-001/004 V&V (VVP-001, VVP-004)
- HFP prompt §§11–13 (control view, flight modes)

## 4. Definitions & Acronyms

- Allocation: distribution of generalised forces/moments across module groups (arm/rear/ankle); geometry and effectiveness TBD.
- Reallocation: redistribution of demands after module failure/exclusion; logic TBD.
- Optimisation criteria: objectives trading efficiency against control authority (unweighted at this level; weights TBD).
- FCS: Flight Control System. ICD: Interface Control Document. TBD: To Be Determined.

## 5. System Context

Allocation sits between control laws and mixing: laws produce generalised demands → allocation assigns group-level demands using effectiveness data (TBD) and health status → mixing converts to per-module commands. Allocation receives health/fault inputs (via monitoring/FTC) and authority-budget constraints (via HFPX-FCS-AUT-001), and feeds the safety computer for monitoring. Efficiency-vs-authority trade is noted but unweighted at this level.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FAC-001 | Thrust allocation across arm, rear, and ankle module groups shall be defined; module geometry and effectiveness data are TBD. | CTL-002, PRP-002, ARC-004 | Analysis |
| REQ-HFPX-FAC-002 | Failed-module reallocation logic (exclusion and redistribution) shall be defined; logic and triggers are TBD. | CTL-004, SFA-001 | Analysis + Test |
| REQ-HFPX-FAC-003 | Allocation-optimisation criteria trading efficiency against control authority shall be defined; criteria are noted but unweighted, weights TBD. | SYS-003, ARC-004 | Analysis |
| REQ-HFPX-FAC-004 | The allocation-to-mixing interface (signals, scaling, mode dependence) shall be defined in an ICD; contents TBD. | CTL-002, ARC-004 | Inspection |
| REQ-HFPX-FAC-005 | Allocation shall be verified by analysis and test; methods and cases TBD per Vol 19 and HFPX-FCS-VER-001. | VVP-001, VVP-004 | Analysis + Test |

## 7. Architecture

A single allocation function owned by FCS (owner TBD; reallocation only by trade). Inputs: generalised demands, mode ID, module health status, authority-budget constraints. Processing: nominal distribution block, failed-module reallocation block, optimisation-criteria block (efficiency vs authority, unweighted). Outputs: group-level demands to mixing plus status to safety monitoring. Structure only — no numeric content.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Geometry, effectiveness matrices, reallocation logic, optimisation formulation/weights, and signal scaling are TBD (Vol 07, Vol 19).

## 9. Interfaces

- From control laws: generalised demands — TBD.
- From monitoring/FTC (SFA-001, HFPX-FCS-FTC-001): module health/fault status — TBD.
- From authority budgets (HFPX-FCS-AUT-001): per-axis/mode constraints — TBD (methods only).
- To mixing (HFPX-FCS-MIX-001): group demands via ICD — TBD, captured before CDR per ARC-005 pattern.
- To propulsion (PRP-002) via mixing only; no direct allocation-to-effector command path is assumed (TBC).

## 10. Operational Concept

Allocation supports all flight modes; hover stresses multi-module distribution, transition stresses reallocation during configuration change, cruise stresses efficiency-biased distribution. Failed-module cases invoke REQ-HFPX-FAC-002 reallocation or handover to degraded/FTC modes. No operational allocation values are stated.

## 11. Safety

Misallocation (wrong distribution, failure to reallocate, efficiency-biased starvation of authority) is hazardous: REQ-HFPX-FAC-002 (reallocation), REQ-HFPX-FAC-003 (authority-aware criteria), and the safety path (SFA-001) mitigate it. No controllability or safety claim is made; all logic TBD pending Vol 07/13 analysis. This document provides no propulsion build/operation instructions (see boundary note in §2).

## 12. Performance

Distribution accuracy, computation load, execution rate, latency, reallocation transient, and efficiency/authority trade budgets are TBD. No allocation value is stated. Methods for budgeting are TBD (Vol 07/08).

## 13. Verification & Validation

Per REQ-HFPX-FAC-005 and HFPX-FCS-VER-001: allocation verified by analysis (effectiveness, stability under reallocation — data TBD) plus SIL/HIL/test including fault-injection of module-out cases. Cases trace to FAC-001..005; acceptance criteria TBD per case. No gate skipping.

## 14. Risks

- Geometry/effectiveness TBD leaves allocation uncloseable; mitigation: data owners assigned, stub status explicit.
- Efficiency-vs-authority trade resolved against authority; mitigation: REQ-HFPX-FAC-003 keeps authority as explicit criterion, unweighted pending trade.
- Allocation/mixing ownership split causes interface mismatch; mitigation: single ICD (REQ-HFPX-FAC-004).

## 15. Open Issues

Module geometry TBD; effectiveness data TBD; reallocation logic TBD; optimisation criteria/weights TBD; allocation-to-mixing ICD TBD; verification cases and acceptance criteria TBD; allocation owner TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-004), Control Architecture (CTL-002, CTL-004), mixing (HFPX-FCS-MIX-001), authority (HFPX-FCS-AUT-001), FTC (HFPX-FCS-FTC-001), propulsion interface (PRP-002), safety view (SFA-001), verification thread (VVP-001/004, HFPX-FCS-VER-001), Vol 19 (SIL/HIL).

## 18. Traceability

Parents: SYS-001, SYS-002, SYS-003; ARC-004; CTL-002, CTL-004; PRP-002; SFA-001; VVP-001, VVP-004. Children: allocation logic/matrices (TBD), ICD entries, V&V cases. RTM: REQ-HFPX-FAC-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.16) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
