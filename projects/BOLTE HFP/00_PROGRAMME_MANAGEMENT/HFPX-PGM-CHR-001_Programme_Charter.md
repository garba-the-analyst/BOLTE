# Programme Charter

**Document ID:** HFPX-PGM-CHR-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Establish the BOLTE HFP-X programme authority, objectives, scope boundaries and success criteria so all Volumes 00–33 work from one controlled baseline. This document owns Chapter 00.1.

## 2. Scope

Applies to the full HFP-X programme: concept → requirements → architecture → prototype → testing → certification → production → operation → sustainment. Covers the 34-volume structure (Vol 00–33) and the five backbone documents. Does not approve any technical value; all performance figures remain TBD.

## 3. Applicable Documents

- HFPX-PGM-SEM-001 SEMP (sibling, owns the process)
- HFPX-SYS-MIS-001 Mission Definition
- HFPX-SYS-ARC-001 System Architecture Description (stub)
- HFPX-PGM-BSL-001 Master Technical Baseline (BL-0.0)
- Schema: HFP Documentation schema; Prompt: HFP prompt (master agent prompt)
- Frameworks (structured according to, not compliant): INCOSE SE, ISO/IEC/IEEE 15288, ISO/IEC/IEEE 29148, SAE ARP4754A, SAE ARP4761/4761A, DO-178C/DO-254/DO-160 concepts

## 4. Definitions & Acronyms

- HFP-X: Human Flight Platform (prone/semi-prone, distributed jet propulsion, VTOL/transition concept)
- BL-0.0: Structure-only baseline; no technical values approved
- SRR/PDR/CDR/TRR/FCA/PCA/FRR/PRR/ORR: formal gates per prompt §18
- TBD/TBC: to be determined / to be confirmed; ASSUMPTION A-XXX: explicitly labelled assumption
- SyRS/SAD/V&V: System Requirements Specification / System Architecture Description / Verification & Validation

## 5. System Context

HFP-X is a human-carrying VTOL/transition aircraft concept (arm + rear/torso + ankle propulsion modules, fly-by-wire, independent safety computer, smart helmet/HUD, ground station). Programme context:

```text
BOLTE PROGRAMME → HFP-X SYSTEM (SYS-01..SYS-23) → MVP DEMONSTRATOR (Vol 33, separate)
       ↑                     ↑                              ↑
  Regulators (NCAA/ICAO)  Safety/Recovery (Vol 13)   Unmanned-first evidence chain
```

Production aircraft documentation and MVP documentation are kept separate per schema (Vol 33 note).

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-PGM-001 | The programme shall maintain the 34-volume documentation structure (Vol 00–33) under configuration control. | Inspection |
| REQ-HFPX-PGM-002 | The programme shall maintain a Requirements Traceability Matrix from Mission → Stakeholder → System → Design → Test → Evidence with no orphaned major requirements. | Inspection |
| REQ-HFPX-PGM-003 | The programme shall gate human flight on prior evidence: simulation → SIL → HIL → subsystem → integrated propulsion → unmanned → tethered human → controlled human flight → envelope expansion; gates shall not be skipped. | Demonstration |
| REQ-HFPX-PGM-004 | The programme shall distinguish "structured according to" a standard from "verified compliant with" it in every document. | Inspection |
| REQ-HFPX-PGM-005 | The programme shall keep Volume 33 (MVP) separate from production-aircraft baselines; production transition is governed by 33.20. | Inspection |

## 7. Architecture

Programme breakdown: Vol 00 (governance), Vol 01 (needs/requirements), Vol 02 (architecture), Vol 03–18 (subsystems), Vol 19 (simulation), Vol 20–21 (build/integrate), Vol 22–23 (verify/test), Vol 24–25 (reliability/certification), Vol 26–32 (operate/sustain), Vol 33 (MVP, separate). Five backbone documents govern: SEMP, SyRS, SAD, V&V Plan, Safety & Airworthiness Case.

## 8. Detailed Design

Not applicable at charter level. Charter decisions implemented via SEMP processes (Vol 00.4–00.16) and adopted DDRs: DDR-001 (unmanned-first), DDR-002 (34-volume structure), DDR-003 (identifier scheme).

## 9. Interfaces

- Upstream: BOLTE programme authority (owner TBD)
- Downstream: all volume owners (TBD), regulators (NCAA/ICAO, see ISS-001)
- Data: registers in `00_PROGRAMME_MANAGEMENT/registers/` + hazard log in `13_SAFETY_RECOVERY/`; change control per prompt §31
- External: suppliers (Vol 00.13), test ranges (Vol 23), certification authorities (Vol 25)

## 10. Operational Concept

Programme operates in gated phases: baseline BL-0.0 (structure) → mission/CONOPS/stakeholder drafts (Tranche 1) → SRR → PDR → CDR → TRR → unmanned test → FRR → controlled flight → PRR/ORR. No human-carrying propulsion operation outside appropriate engineering, test, safety and regulatory controls (prompt §34).

## 11. Safety

Safety-first policy (prompt §3.5): never optimise performance at the expense of controllability, structural integrity, propulsion reliability, pilot survivability, recovery, thermal/fuel/electrical/software integrity or fault tolerance. Safety analyses are independent of performance work (Vol 13, Vol 24).

## 12. Performance

Programme performance metrics are TBD (Vol 00.5/00.6): e.g. gate pass rates, RTM coverage, open-issue burn-down. No aircraft performance value is stated here.

## 13. Verification & Validation

Charter verified by SRR entrance criteria (Vol 00.14, TBD): 34 volumes present, registers valid (`hfpx_scaffold.py check` passes), mission + stakeholder drafts exist, hazard log opened. Validation: BOLTE approval (approver TBD).

## 14. Risks

- Regulatory path for human-carrying experimental jet VTOL undefined (ISS-001) → research NCAA/ICAO before SRR
- Mission/stakeholder vacuum → SyRS unWritable (ISS-002) → closed by Tranche 1 drafts, verified at SRR
- Defence-variant legal exposure (ISS-005) → no Vol 31.3 work before legal advice
- Risk register itself not yet created (Vol 00.12)

## 15. Open Issues

ISS-001 (Critical, regulatory basis), ISS-002 (Critical, mission/stakeholder — partly addressed by Tranche 1, remains OPEN until SRR), ISS-005 (High, defence legal). See `issue_register.csv`.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on: BOLTE authority assignment (owner/approver TBD), Vol 00.14 gate criteria, Vol 25 regulatory research, Vol 01 mission/CONOPS/stakeholder approval before SyRS baseline.

## 18. Traceability

Parent: schema "VOLUME 00" + prompt §3 (philosophy) and §35 (role). Children: HFPX-PGM-SEM-001 (process), HFPX-SYS-MIS-001 (mission), DDR-001/002/003, ISS-001/002/005. RTM entries: REQ-HFPX-PGM-001..005 → Status CONCEPT.

## 19. Configuration

BL-0.0. This document is a Tranche 1 draft, CONCEPT, not baselined. Changes follow prompt §31 (change record with affected requirements/subsystems/interfaces/evidence).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 00.1) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
