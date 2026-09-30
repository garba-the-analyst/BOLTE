# Fault-Tolerant Control

**Document ID:** HFPX-FCS-FTC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fault-tolerant control (FTC) framework (Chapter 07.18): the fault detection → isolation → reconfiguration chain with the safety computer, the single-module-out controllability objective, the degraded-mode set, handover to emergency stabilisation, and FTC verification ownership.

## 2. Scope

Covers FTC structure, ownership, and methodology for the production-aircraft concept across hover, transition, and cruise. Detection thresholds, isolation logic, reconfiguration laws, degraded-mode definitions, handover criteria, gains, margins, and limits are TBD. FTC ownership and methods only — no numeric values are allocated in this document.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001, SYS-002, SYS-003)
- HFPX-SYS-ARC-001 SAD (ARC-004)
- HFPX-ARC-CTL-001 Control Architecture (CTL-004 — fault-tolerant hooks; CTL-001, CTL-002, CTL-003)
- HFPX-FCS-MIX-001 Propulsion Mixing (Ch 07.15); HFPX-FCS-ALC-001 Thrust Allocation (Ch 07.16); HFPX-FCS-AUT-001 Control Authority (Ch 07.17)
- HFPX-SFA-001 Safety Architecture (SFA-001); HFPX-VVP-001/004 V&V (VVP-001, VVP-004)
- HFP prompt §§11–13 (control view, flight modes)

## 4. Definitions & Acronyms

- FTC: Fault-Tolerant Control — detection, isolation, and reconfiguration preserving controlled flight after faults; all logic TBD.
- Detection → isolation → reconfiguration: chain from fault annunciation to faulty-source identification to control redistribution; thresholds and logic TBD.
- Degraded mode: reduced-capability control regime after reconfiguration; set TBD.
- Emergency stabilisation: independent safety-path function assuming control when FTC cannot preserve margins; handover criteria TBD.
- SIL/HIL: Software/Hardware-in-the-Loop. TBD: To Be Determined.

## 5. System Context

FTC takes health/fault inputs from monitoring and the safety computer, commands reconfiguration through allocation/mixing (exclusions, table switches, law-mode changes), and hands over to emergency stabilisation when authority or integrity cannot be preserved. The safety computer participates in the chain with independent monitoring and handover authority. Single-module-out controllability is an objective, unproven at this level.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FFT-001 | The fault detection → isolation → reconfiguration chain, including the safety-computer role, shall be defined; thresholds, logic, and timing are TBD. | CTL-004, SFA-001 | Analysis + Test |
| REQ-HFPX-FFT-002 | A single-module-out controllability objective shall be defined and assessed; the objective is unproven, criteria and results TBD. | CTL-004, CTL-003, SYS-002 | Analysis + Test |
| REQ-HFPX-FFT-003 | The degraded-mode set (modes, entry/exit conditions, capability claims) shall be defined; all definitions TBD. | CTL-001, CTL-004, SFA-001 | Analysis + Test |
| REQ-HFPX-FFT-004 | Handover from FTC to emergency stabilisation (conditions, authority transfer, timing) shall be defined; criteria TBD. | CTL-004, SFA-001 | Analysis + Test |
| REQ-HFPX-FFT-005 | FTC shall be verified by fault-injection in SIL, HIL, and test; methods, cases, and acceptance criteria TBD per Vol 19 and HFPX-FCS-VER-001. | VVP-001, VVP-004 | Test |

## 7. Architecture

FTC chain owned by FCS/safety jointly (owners TBD): detection block (monitoring inputs TBD), isolation block (source identification TBD), reconfiguration block (allocation/mixing/law commands TBD), degraded-mode supervisor (mode set TBD), and handover block to emergency stabilisation (criteria TBD). The safety computer provides parallel monitoring and independent handover authority. Structure and ownership only — no numeric content.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Detection thresholds, isolation logic, reconfiguration laws, degraded-mode definitions, handover criteria, and timing budgets are TBD (Vol 07, Vol 08/16, Vol 19).

## 9. Interfaces

- From monitoring / safety computer (SFA-001): fault/health inputs — TBD.
- To allocation/mixing (HFPX-FCS-ALC-001, HFPX-FCS-MIX-001): exclusion and redistribution commands — TBD.
- To control laws: law-mode switch commands — TBD.
- To emergency stabilisation (SFA-001): handover signals and authority transfer — TBD, ICD before CDR.
- To verification thread (HFPX-FCS-VER-001, VVP-001/004): fault-injection hooks — TBD.

## 10. Operational Concept

FTC supports all flight modes; hover stresses single-module-out retention, transition stresses reconfiguration during configuration change, cruise stresses degraded-mode endurance. When reconfiguration cannot preserve authority, control hands over to emergency stabilisation per REQ-HFPX-FFT-004. No operational FTC values are stated.

## 11. Safety

Failed or mistriggered FTC (missed detection, wrong isolation, destabilising reconfiguration, failed handover) is hazardous: REQ-HFPX-FFT-001 (defined chain with safety computer), REQ-HFPX-FFT-003 (bounded degraded modes), and REQ-HFPX-FFT-004 (handover backstop) plus the independent safety path (SFA-001) mitigate it. No controllability claim is made; single-module-out capability is an unproven objective (REQ-HFPX-FFT-002) pending Vol 07/13 analysis.

## 12. Performance

Detection latency, isolation accuracy, reconfiguration transients, degraded-mode capability, and compute budgets are TBD. No allocation value is stated. Methods for budgeting are TBD (Vol 07/08).

## 13. Verification & Validation

Per REQ-HFPX-FFT-005 and HFPX-FCS-VER-001: FTC verified by fault-injection across SIL, HIL, and test covering detection, isolation, reconfiguration, degraded modes, and handover. Cases trace to FFT-001..005; acceptance criteria TBD per case. No gate skipping.

## 14. Risks

- Single-module-out controllability unproven; mitigation: objective stated as TBD/unproven, analysis and fault-injection owned by Vol 07/19.
- Nuisance reconfiguration or failed handover; mitigation: defined chain with safety-computer role plus handover backstop, all TBD.
- Degraded-mode proliferation without bounds; mitigation: closed mode set required by REQ-HFPX-FFT-003.

## 15. Open Issues

Detection/isolation/reconfiguration logic TBD; single-module-out assessment TBD; degraded-mode set TBD; handover criteria TBD; FTC owners TBD; fault-injection cases and acceptance criteria TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-004), Control Architecture (CTL-001..004), mixing/allocation/authority (HFPX-FCS-MIX-001, HFPX-FCS-ALC-001, HFPX-FCS-AUT-001), safety view including emergency stabilisation (SFA-001), verification thread (VVP-001/004, HFPX-FCS-VER-001), Vol 19 (SIL/HIL/fault-injection).

## 18. Traceability

Parents: SYS-001, SYS-002, SYS-003; ARC-004; CTL-001, CTL-002, CTL-003, CTL-004; SFA-001; VVP-001, VVP-004. Children: FTC logic, degraded modes, handover ICD, V&V cases (all TBD). RTM: REQ-HFPX-FFT-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.18) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
