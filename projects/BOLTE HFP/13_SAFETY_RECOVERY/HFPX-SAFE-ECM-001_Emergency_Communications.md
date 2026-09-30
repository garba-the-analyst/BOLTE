# Emergency Communications

**Document ID:** HFPX-SAFE-ECM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X emergency-communications direction (Chapter 13.17): which emergency/priority links, Mayday-type signalling, and ground-station emergency authority must be defined, and how they are verified by demonstration and test.
Sets requirements, architecture, and verification direction only; it specifies no frequencies, protocols, or hardware selections.

## 2. Scope

Covers emergency/priority links, Mayday-type signalling, and ground-station emergency authority across applicable flight and contingency regimes (regimes TBD, with Vol 11.6 inputs).
In scope: emergency-communications functional requirements, architectural allocation direction, interface requirements, and demo/test-methodology direction.
Out of scope: primary communications detailed design (Vol 11/15 as applicable), protocol implementation, spectrum/licensing matters, and any build or operation instructions.

## 3. Applicable Documents

- Programme Charter STK-001; operations tier OPC-003; communications tier COM-001..004 (all stubs, values TBD)
- HFPX-SAFE-CAS-001 Safety Case; hazard log (`13_SAFETY_RECOVERY/hazard_log.csv`); HFPX-VV-PLN-001 V&V Plan
- Vol 11 operations concept, §11.6 contingency communications; Vol 13.16 emergency power (powering companion); Vol 23 test programme
- Standards (structured according to): SAE ARP4754A, ARP4761/4761A concepts — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Emergency / priority link: communications path reserved or prioritised for contingency traffic, bearers and priority scheme TBD
- Mayday-type signalling: standardised distress/priority signalling indicating emergency state and assistance required, format and triggers TBD (Vol 11.6)
- Ground-station emergency authority: powers and responsibilities of the ground station during an emergency, scope TBD
- Demo / test: verification by observed functional exercise (demo) and by measured functional exercise (test), scope TBD per case

## 5. System Context

Emergency communications carry safety-path annunciation, distress signalling, and ground-authority directives; without them, contingency coordination between vehicle, crew, and ground cannot be assured.
Link definitions, signalling formats, and authority scope depend on Vol 11.6 and COM-tier inputs, all TBD; no link or protocol is baselined in this revision.
Emergency comms depend on emergency power (Vol 13.16) and on defined operational authority; both companion inputs are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ECM-001 | The system shall provide emergency/priority links for contingency traffic, with bearers, coverage, and priority scheme TBD. | OPC-003, COM-001..004 | Demonstration |
| REQ-HFPX-ECM-002 | The system shall provide Mayday-type signalling, with format, triggers, and annunciation TBD (Vol 11.6). | OPC-003, COM-001..004 | Demonstration |
| REQ-HFPX-ECM-003 | The programme shall define ground-station emergency authority, with powers, responsibilities, and handover conditions TBD. | OPC-003, COM-001..004 | Inspection |
| REQ-HFPX-ECM-004 | Emergency-communications functions shall be verified by demonstration and test, with scope, conditions, and acceptance criteria TBD. | OPC-003, COM-001..004 | Test |

All link parameters, signal formats, ranges, latencies, and authority thresholds: TBD. No emergency-communications capability is asserted until demonstrated and tested.

## 7. Architecture

Emergency-communications allocation TBD across vehicle transceivers/antennas (TBD), priority handling, signalling generation, ground stations, and operations roles; SAD to allocate with Vol 11.
Priority traffic is architecturally identified as a protected class segregated from routine traffic to a degree TBD.
Ground-station authority is architecturally identified as a control segment with defined handover to/from crew/automation (logic TBD); AI advisory-only constraint applies (allocation TBD).
> Hazardous-subsystem boundary: architecture here addresses functional allocation and interfaces only; it contains no build or operation instructions.

## 8. Detailed Design

No detailed design in this revision — links, signalling, and authority TBD.
Design direction (methodology only): per-function decomposition into generation → prioritisation → transmission → reception → acknowledgement, each with requirements, interfaces, and verification cases TBD.
Signalling-format methodology TBD: Vol 11.6 operational inputs, hazard allocation, and human-factors review criteria to be defined before any format claim.

## 9. Interfaces

- Emergency comms ↔ Operations (Vol 11.6): signalling formats, procedures, authority handover, details TBD
- Emergency comms ↔ Primary comms: bearer sharing, pre-emption, fallback, details TBD
- Emergency comms ↔ Emergency power (Vol 13.16): powered-load interface, endurance alignment, details TBD
- Emergency comms ↔ Safety path: distress triggers, annunciation routing, details TBD
- Emergency comms ↔ V&V (Vol 22–24): demo/test cases and hooks, IDs TBD

## 10. Operational Concept

Test methodology and gating only: this concept defines readiness evidence and authority-logic structure, not vehicle handling or flight conduct.
Lifecycle direction: link/priority definition → signalling definition (Vol 11.6) → authority definition → ground demonstration → integrated contingency demo/test at a fidelity TBD → Safety Review Board assessment.
No operational emergency procedure is authorised in this revision; procedures and authority delegation are TBD and gated by FRR.

## 11. Safety

Loss, delay, or misinterpretation of emergency communications is treated as a safety-path hazard input; associated causes, effects, and mitigations enter the hazard log and analyses (IDs TBD).
No compliance claimed in this revision; no link availability or signalling effectiveness is asserted until verified by demo/test.
Emergency communications shall not take credit for retiring catastrophic hazards until mitigations are verified and retired by the Safety Review Board (criteria TBD).
> Hazardous-subsystem boundary: this section states safety-analysis and gating rules only.

## 12. Performance

Emergency-communications performance indicators and thresholds TBD (no values baselined): link availability and coverage TBD, priority latency TBD, signalling integrity TBD, authority-handover timing TBD.
No numerical targets are set in this revision; scales and acceptance criteria TBD in later revisions with Vol 13/24 concurrence.

## 13. Verification & Validation

Verification direction: REQ-HFPX-ECM-001..002 by demonstration (links exercised and Mayday-type signalling observed end-to-end at a fidelity TBD); REQ-HFPX-ECM-003 by inspection (authority definition reviewed against operations and safety governance); REQ-HFPX-ECM-004 by test (measured demo/test with acceptance criteria TBD).
Acceptance criteria TBD per case; evidence recorded as TBD/empty until closed.
Validation by Safety Review Board plus programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Link-assumption drift: contingency operations assume priority connectivity that is undefined; mitigation: explicit undefined-link status enforced at every gate review
- Signalling ambiguity: non-standard or misinterpreted distress signalling across crew/ground roles; mitigation: Vol 11.6 format definition with human-factors review required before any operational claim (criteria TBD)
- Authority conflict: overlapping crew, automation, and ground-station directives in an emergency; mitigation: single authority-definition artefact with handover logic required before PDR as applicable (owner and gate TBD)

## 15. Open Issues

Emergency/priority links undefined (bearers, coverage, priority TBD). Mayday-type signalling format and triggers undefined (Vol 11.6 inputs TBD). Ground-station emergency authority undefined. Demo/test scope and acceptance criteria undefined. COM-001..004 and OPC-003 values TBD. All emergency-comms evidence TBD/empty.

## 16. Assumptions

- Priority handling can be segregated from routine traffic within budgets TBD; validation: SAD allocation with Vol 11 (TBD)
- Mayday-type signalling can be standardised across crew and ground roles once Vol 11.6 is defined; validation: Vol 11 operations concept (TBD)
- Ground demonstration plus integrated contingency demo/test can verify emergency comms without human-flight trials; validation: Vol 23 test methodology (TBD)

## 17. Dependencies

Depends on STK-001/OPC-003/COM-001..004 tiers (requirements basis), Safety Case and hazard analyses (hazard basis), Vol 11.6 (signalling and authority inputs), Vol 13.16 (powering), Vol 19 (modelling as applicable), Vol 22–24 (VCRM and demo/test verification), Vol 25 (certification basis).

## 18. Traceability

Parents: OPC-003, COM-001..004 (values TBD).
Children: link-level, signalling-level, and authority requirements and demo/test cases (artefact IDs TBD).
RTM: REQ-HFPX-ECM-001..004 → CONCEPT. Each emergency function traces to hazards → requirements → VCRM cases → evidence (all TBD except schema).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Link, signalling-format, or authority change requires a change record with affected-requirement and hazard impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (emergency-communications direction; links/signalling/authority TBD) |
