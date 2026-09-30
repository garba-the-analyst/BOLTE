# Propulsion Mixing

**Document ID:** HFPX-FCS-MIX-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion mixing function (Chapter 07.15): mapping of body-axis flight-control commands to individual propulsion-module thrust-vector commands, including mode dependence, saturation handling, verification ownership, and version control with control laws.

## 2. Scope

Covers mixing structure, ownership, and methodology for the production-aircraft concept across hover, transition, and cruise. All mixing matrices, tables, gains, margins, and limits are TBD. Mixing ownership and methods only — no numeric values are allocated in this document.

**Hazardous-subsystem boundary note:** This document covers control design, analysis, and test methodology only. It contains no propulsion build, integration, maintenance, or operation instructions. Propulsion implementation is owned elsewhere (Vol 05 / PRP-002). This document shall not be used as a build or operating instruction for any propulsion subsystem.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001, SYS-002, SYS-003)
- HFPX-SYS-ARC-001 SAD (ARC-004 — determinism/modularity allocation)
- HFPX-ARC-CTL-001 Control Architecture (CTL-001, CTL-002)
- HFPX-FCS-ALC-001 Thrust Allocation (companion, Ch 07.16); HFPX-FCS-AUT-001 Control Authority (Ch 07.17)
- HFPX-PRP-xxx Propulsion (PRP-002 interface); HFPX-SFA-001 Safety Architecture (SFA-001); HFPX-VVP-001/004 V&V (VVP-001, VVP-004)
- HFP prompt §§11–13 (control view, flight modes)

## 4. Definitions & Acronyms

- Mixing: function mapping generalised body-axis commands (forces/moments) to module-level thrust-vector commands; numeric matrix TBD.
- Mixing table: mode-dependent instance of the mixing mapping (hover/transition/cruise, degraded modes); all tables TBD.
- Saturation/prioritisation: logic for resolving effector demand exceeding available authority; logic TBD.
- FCS: Flight Control System. SIL: Software-in-the-Loop. HIL: Hardware-in-the-Loop.
- TBD / TBC: To Be Determined / Confirmed. No values invented.

## 5. System Context

Mixing sits downstream of control laws and thrust allocation in the FCS chain: laws produce body-axis demands → allocation distributes generalised demands across module groups (arm/rear/ankle, geometry TBD) → mixing converts to per-module thrust-vector commands → propulsion effectors execute. The safety computer monitors mixing outputs in parallel. Mixing behaviour is mode-dependent and version-controlled with the law set it was verified against.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FMX-001 | The FCS mixing function shall map body-axis control commands to individual module thrust-vector commands; the mixing matrix and its dimensioning are TBD. | CTL-002, ARC-004 | Analysis |
| REQ-HFPX-FMX-002 | Mode-dependent mixing tables for hover, transition, cruise, and degraded modes shall be defined; all table contents and switching conditions are TBD. | CTL-001, SYS-002 | Analysis |
| REQ-HFPX-FMX-003 | Saturation and axis-prioritisation logic for over-demanded mixing outputs shall be defined; logic, priorities, and limits are TBD. | CTL-002, SFA-001 | Analysis |
| REQ-HFPX-FMX-004 | Mixing shall be verified by SIL, HIL, and test; methods and cases TBD per Vol 19 and HFPX-FCS-VER-001. | VVP-001, VVP-004 | Analysis + Test |
| REQ-HFPX-FMX-005 | Mixing definitions shall be version-controlled together with the control-law set they were verified against; process TBD. | ARC-004, VVP-004 | Inspection |

## 7. Architecture

A single mixing function owned by FCS (owner TBD; reallocation only by trade with allocation owner). Inputs: body-axis demands from laws/allocation plus active mode identifier. Outputs: per-module thrust-vector commands to propulsion interfaces. Mode-dependent tables select the active mapping; saturation/prioritisation block bounds and orders outputs before release to effectors. The safety computer receives mixing inputs/outputs for independent monitoring. Structure only — no numeric content.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Mixing matrices, mode tables, saturation thresholds, prioritisation order, and interface signal definitions are TBD (Vol 07, Vol 19, ICD 02.17).

## 9. Interfaces

- From control laws / thrust allocation (HFPX-FCS-ALC-001): body-axis demands and mode ID — definition TBD.
- To propulsion modules (PRP-002): per-module thrust-vector commands — signal ICD TBD, captured before CDR.
- To safety computer (SFA-001): mixing inputs/outputs for monitoring — TBD.
- To verification thread (HFPX-FCS-VER-001, VVP-001/004): mixing models for SIL/HIL — TBD.

## 10. Operational Concept

Mixing supports all flight modes; hover exercises full multi-module mixing, transition exercises table switching under supervisor control, cruise exercises reduced-effector mixing. Degraded mixing (failed-module exclusions) is commanded via allocation/FTC inputs. No operational mixing values are stated.

## 11. Safety

Incorrect mixing (wrong mapping, stale table, unbounded saturation) is hazardous: REQ-HFPX-FMX-002 (mode-correct tables), REQ-HFPX-FMX-003 (bounded saturation), and REQ-HFPX-FMX-005 (verified pairing with laws) plus the independent safety path (SFA-001) mitigate it. No controllability or safety claim is made; all logic TBD pending Vol 07/13 analysis. This document provides no propulsion build/operation instructions (see boundary note in §2).

## 12. Performance

Mixing accuracy, computation load, execution rate, latency, and switching-transient budgets are TBD. No allocation value is stated. Methods for budgeting are TBD (Vol 07/08).

## 13. Verification & Validation

Per REQ-HFPX-FMX-004 and HFPX-FCS-VER-001: mixing verified through the sim → SIL → HIL → unmanned-test thread with no gate skipping. Verification cases trace to FMX-001..005; acceptance criteria TBD per case. Fault-injection of stale/wrong-table and saturation cases is planned (methods TBD, Vol 19).

## 14. Risks

- Mixing/allocation ownership split causes interface mismatch; mitigation: single ICD and joint owner TBD, stub status explicit.
- Saturation logic TBD leaves loss-of-control path uncharacterised; mitigation: prioritisation logic owned by Vol 07 trade, safety-path backstop.
- Stale mixing-vs-law pairing; mitigation: REQ-HFPX-FMX-005 version-control rule.

## 15. Open Issues

Mixing matrix TBD; mode tables TBD; saturation/prioritisation logic TBD; mixing owner TBD; verification cases and acceptance criteria TBD; ICD TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-004), Control Architecture (CTL-001, CTL-002), thrust allocation (HFPX-FCS-ALC-001), control authority (HFPX-FCS-AUT-001), propulsion interface (PRP-002), safety view (SFA-001), verification thread (VVP-001/004, HFPX-FCS-VER-001), Vol 19 (SIL/HIL).

## 18. Traceability

Parents: SYS-001, SYS-002, SYS-003; ARC-004; CTL-001, CTL-002; PRP-002; SFA-001; VVP-001, VVP-004. Children: mixing matrices/tables (TBD), ICD entries, V&V cases. RTM: REQ-HFPX-FMX-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.15) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
