# Functional Architecture

**Document ID:** HFPX-ARC-FUN-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X functional architecture (Chapter 02.2): what the system must do, independent of physical implementation. Provides the function decomposition and function-to-system allocation basis for logical, physical and control views.

## 2. Scope

Covers top-level functions (aviate, navigate, communicate, protect, sustain), mode-dependent behaviour (hover/transition/cruise), and functional interface naming. Excludes component selection, physical layout, and quantitative budgets (covered in PHY/LOG/PRP/PWR views).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- HFPX-SYS-CON-001 CONOPS; HFP prompt §§11–13; future ICDs (02.17)

## 4. Definitions & Acronyms

- Aviate: generate and control lift/thrust and attitude. Navigate: sense, fuse and estimate state/position.
- Communicate: exchange information with pilot, operator and ground. Protect: detect faults and drive mitigation/recovery.
- Sustain: provide and manage energy, thermal and structural support. Allocation: mapping of functions to SYS-01..SYS-23.

## 5. System Context

Functional architecture sits between stakeholder needs (mission, CONOPS) and system decomposition. It receives operational modes and mission phases as context inputs and produces allocated functions consumed by logical, physical, hardware, software and safety architectures.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-FNC-001 | The functional architecture shall decompose top-level system behaviour into aviate, navigate, communicate, protect, and sustain functions with defined sub-functions. | Inspection |
| REQ-HFPX-FNC-002 | The functional architecture shall allocate every function to at least one system in SYS-01..SYS-23 with no unallocated functions. | Inspection |
| REQ-HFPX-FNC-003 | The functional architecture shall define mode-dependent functions for hover, transition, and cruise modes. | Analysis |
| REQ-HFPX-FNC-004 | The functional architecture shall name all functional interfaces between top-level functions. | Inspection |

## 7. Architecture

Function decomposition with allocation (starter; laws and values TBD):

```text
[AVIATE] lift/thrust/control → SYS-02/03/05
   ↕ (attitude/state) [NAVIGATE] sense/fuse/estimate → SYS-07/08/10
   ↕ (commands/status) [COMMUNICATE] helmet/ground links → SYS-11/12/13/18
   ↕ (faults/mitigations) [PROTECT] monitor/safety/recovery → SYS-05/13/16/17/21
   ↕ (energy/thermal) [SUSTAIN] power/fuel/thermal/structure → SYS-01/04/09/17
```

Mode dependence: hover stresses aviate/protect; transition stresses aviate/navigate/protect with distinct switching functions; cruise stresses aviate/navigate/sustain. Switching and abort functions allocated to FCS + safety path (details in LOG view, control laws TBD Vol 07).

## 8. Detailed Design

Not applicable at this level. Sub-function breakdowns and detailed functional flows are deferred to subsystem documents (Vol 03–18). No design values stated.

## 9. Interfaces

Functional interfaces named (physical realisation TBD in ICDs): F-AV-NAV (attitude/state estimates), F-AV-COM (pilot/operator commands), F-AV-PRO (fault flags/mitigation commands), F-AV-SUS (energy/thermal status), F-NAV-COM (navigation display/telemetry). Protocol and timing TBD.

## 10. Operational Concept

Functional chains execute in every flight mode per CONOPS state machine. Hover/transition/cruise select mode-dependent aviate and protect sub-functions; emergencies invoke protect-chain priority over aviate responsiveness. Detail per Vol 10/12 and CONOPS.

## 11. Safety

Protect functions are architecturally separate from aviate/navigate chains and feed the independent safety path (ARC-003). Functional hazards for each top-level function feed FHA (Vol 13). AI monitoring functions are advisory only (ARC-002).

## 12. Performance

Functional performance budgets (response, accuracy, availability) are TBD. Budget holders identified per function; no values allocated in this view.

## 13. Verification & Validation

Verified by inspection: completeness of decomposition (FNC-001), allocation with no orphans (FNC-002), mode coverage (FNC-003), interface naming (FNC-004). Validated later via SIL/HIL and trace to subsystem V&V (Vol 19/33).

## 14. Risks

- Functional overlap or gaps across SYS-01..SYS-23; mitigation: allocation matrix review at SRR/PDR.
- Mode-dependent functions diverging across views; mitigation: single mode definitions owned by CONOPS + LOG view.

## 15. Open Issues

Function-to-system allocation matrix incomplete (TBD). Mode-switching function ownership between FCS and safety computer TBD. Functional interface ID numbering scheme TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS stability, SAD view framework, CONOPS modes, and subsystem functional inputs (Vol 03–18). ICD authorship (02.17) depends on named interfaces herein.

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-001/002/004/005). Children: Vol 03–18 subsystem docs, LOG/PHY views, ICDs. RTM: REQ-HFPX-FNC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.2.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.2) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
