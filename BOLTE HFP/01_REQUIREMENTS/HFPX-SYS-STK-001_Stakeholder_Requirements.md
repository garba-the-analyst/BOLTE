# Stakeholder Requirements

**Document ID:** HFPX-SYS-STK-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Capture what stakeholders need from HFP-X in stakeholder language before system requirements are derived. Owns Chapter 01.4; closure of ISS-002 depends on SRR approval of this set with Mission + CONOPS.

## 2. Scope

Stakeholders: pilot/operator, BOLTE programme, regulators (NCAA/ICAO + others TBD), ground/test crew, maintainers, development team. Needs cover safety, controllability, operability, maintainability, regulatory acceptability and programme viability. Excludes derived system requirements (01.17) and design choices.

## 3. Applicable Documents

- HFPX-SYS-MIS-001 Mission Definition; HFPX-SYS-OPC-001 Operational Concept; HFPX-SYS-CON-001 CONOPS
- HFPX-SYS-REQ-001 SyRS (stub, derives from this document)
- HFP prompt §§1–2 (objectives), §9 (classification); schema Vol 01, Vol 25, Vol 30

## 4. Definitions & Acronyms

- Stakeholder need (SH): problem-language need; System requirement (SYS): solution-language requirement derived from SH
- NCAA/ICAO: Nigerian Civil Aviation Authority / International Civil Aviation Organization (regulatory basis TBD, ISS-001)

## 5. System Context

Stakeholder map: pilot needs survivability + workload limits; programme needs gated evidence + certifiable path; regulators need compliance evidence + safe test conduct; crew/maintainers need safe handling + inspectability; developers need verifiable requirements + stable interfaces.

## 6. Requirements

| ID | Stakeholder need (shall) | Source stakeholder | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-STK-001 | Pilot safety and survivability shall take priority over mission performance in every design trade. | Pilot / Safety | Inspection |
| REQ-HFPX-STK-002 | The pilot/operator shall be able to control and stabilise the aircraft across the defined envelope, including transition, without exceptional skill (criteria TBD). | Pilot | Analysis + Test |
| REQ-HFPX-STK-003 | The programme shall be able to demonstrate compliance to the applicable airworthiness basis once determined (basis TBD). | Regulator | Inspection |
| REQ-HFPX-STK-004 | Ground/test crew shall be able to prepare, handle, fuel/power and recover the vehicle without undue hazard (procedures TBD). | Ground crew | Demonstration |
| REQ-HFPX-STK-005 | Maintainers shall be able to inspect, service and replace life-limited components with defined intervals (intervals TBD). | Maintainer | Inspection |
| REQ-HFPX-STK-006 | The development team shall receive atomic, testable, traced system requirements with defined verification methods. | Development | Inspection |
| REQ-HFPX-STK-007 | The pilot/operator shall receive timely status, warning and emergency guidance via the helmet/HMI and ground station. | Pilot / Operator | Demonstration |
| REQ-HFPX-STK-008 | Unmanned validation shall precede human flight for every new flight regime (DDR-001). | Programme / Safety | Inspection |

## 7. Architecture

Needs allocation (starter): STK-001/002 → FCS + safety/recovery (Vol 07/13); STK-003 → certification (Vol 25); STK-004/005 → operations/maintenance (Vol 26/27); STK-006 → SE process (Vol 00); STK-007 → HMI/comms (Vol 10/11); STK-008 → MVP/test (Vol 33/23). Full allocation in SAD.

## 8. Detailed Design

Not applicable — no design implied. Trade studies that will shape satisfaction of these needs (ISS-003 propulsion energy, ISS-004 airframe) are not started.

## 9. Interfaces

Stakeholder interfaces: regulatory engagement (Vol 25.11), training/competency (Vol 30), communications procedures (Vol 26.13), maintenance records (Vol 27.14). Each interface owner TBD.

## 10. Operational Concept

Needs are validated against CONOPS scenarios: every need must be exercisable in ≥1 nominal or off-nominal thread, otherwise the need or the scenario is incomplete.

## 11. Safety

STK-001 is the programme's top need and constrains all others. No need is interpreted as permission to bypass gated testing or to operate high-energy propulsion outside controlled conditions (prompt §34).

## 12. Performance

Stakeholder acceptance thresholds (workload limits, availability, turnaround, envelope minima) are TBD and will be quantified in SyRS 01.8–01.13 once budgets/models exist.

## 13. Verification & Validation

Needs verified by SRR inspection (each need traced to ≥1 system requirement in SyRS; each requirement traced back to a need). Validated by stakeholder acceptance (signatures TBD).

## 14. Risks

- Conflicting needs (performance vs safety vs schedule) unresolved; mitigation: safety primacy (STK-001) + DDR records for each trade
- Regulatory needs unknowable until ISS-001 research completes; mitigation: Vol 25 early engagement, keep needs revisable under change control

## 15. Open Issues

ISS-001 (regulatory needs TBD), ISS-002 (this set unapproved — remains OPEN until SRR).

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on regulatory research (Vol 25), human-factors input (Vol 30), CONOPS completeness, BOLTE authority assignment.

## 18. Traceability

Parent: Mission (REQ-HFPX-MIS-*). Children: SyRS system requirements (REQ-HFPX-SYS-*), SAD views, V&V cases. RTM: REQ-HFPX-STK-001..008 → CONCEPT; parents MIS-001..006.

## 19. Configuration

BL-0.0. Tranche 1 draft, CONCEPT, not baselined. Needs changes after SRR require change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 01.4) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
