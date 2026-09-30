# Pilot Escape / Separation

**Document ID:** HFPX-SAFE-ESC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X pilot escape / separation concept direction (Chapter 13.14): what escape/separation functions, envelope, recovery handover, and decision authority must be defined before any escape capability can be claimed.
Establishes requirements, architecture, and verification direction only; it selects no escape concept and claims no escape effectiveness in this revision.

## 2. Scope

Covers pilot escape / separation functions, escape envelope definition, escape-to-recovery handover, and escape decision authority for all flight regimes where escape is applicable (applicability TBD).
In scope: escape functional requirements, architectural allocation direction, interface and handover requirements, and test-methodology direction.
Out of scope: escape hardware design, pyrotechnic/mechanism implementation, recovery hardware design (Vol 13.11), and any construction, ignition, or operation instructions.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; safety tier SAF-001..006 (all stubs, values TBD)
- HFPX-SAFE-CAS-001 Safety Case; HFPX-SAFE-HAZ-001 Hazard Analysis; hazard log (`13_SAFETY_RECOVERY/hazard_log.csv`)
- HFPX-VV-PLN-001 V&V Plan; Vol 11 operations concept; Vol 13.11 recovery system; Vol 23 test programme
- Standards (structured according to): SAE ARP4754A, ARP4761/4761A concepts — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Escape / separation: function by which pilot separates from the vehicle in an emergency, means TBD — concept unselected in this revision
- Escape envelope: flight conditions within which escape is intended to function, bounds TBD
- Escape-to-recovery handover: transfer from separation function to recovery/survival function, interface TBD
- Escape decision authority: person or function authorised to command or initiate escape, allocation TBD
- ISS-008: recovery effectiveness unproven — applies equally to escape-to-recovery outcomes claimed through this document

## 5. System Context

Escape / separation is a contingency function of last resort; it constrains crew-safety claims but does not substitute for hazard retirement, independent safety path, or demonstrated recovery.
The escape concept is open in this revision (concept unselected); no escape architecture, envelope, or effectiveness is baselined.
Escape outcomes depend on successful handover to recovery/survival functions whose effectiveness is unproven (ISS-008 context); no end-to-end crew-survival claim is made here.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-ESC-001|The system shall provide pilot escape/separation functions, with concept, means, and functional allocation TBD (concept unselected).|REQ-HFPX-MIS-005|Analysis|
|REQ-HFPX-ESC-002|The programme shall define the escape envelope within which escape functions are intended to operate, with bounds TBD.|REQ-HFPX-MIS-005|Analysis|
|REQ-HFPX-ESC-003|The system shall define escape-to-recovery handover behaviour, with handover conditions, interfaces, and success criteria TBD.|REQ-HFPX-MIS-005|Demonstration|
|REQ-HFPX-ESC-004|The programme shall define escape decision authority, with commanding authority, initiation conditions, and authorisation logic TBD.|REQ-HFPX-MIS-005|Inspection|

All thresholds, envelopes, timings, and performance values: TBD. No escape effectiveness is asserted until demonstrated through gated verification.

## 7. Architecture

Escape functional allocation TBD across vehicle, escape means (TBD), recovery interfaces, and ground/crew roles (TBD); SAD to allocate once concept is selected.
Escape-to-recovery handover is architecturally identified as a separate interface segment with ownership TBD on each side of the handover.
Decision authority is architecturally segregated from advisory functions to a degree TBD; AI shall not command escape initiation in early flight (allocation TBD).
> Hazardous-subsystem boundary: architecture here addresses functional allocation and interfaces only; it contains no build, ignition, or operation instructions.

## 8. Detailed Design

No detailed design in this revision — concept unselected.
Design direction (methodology only): once a concept is proposed, it shall decompose into separation initiation, separation execution, handover, and post-handover survival segments, each with requirements, interfaces, and verification cases TBD.
Envelope definition methodology TBD: parameters, instrumentation, and analysis means to be defined with Vol 19 modelling support before any envelope claim.

## 9. Interfaces

- Escape ↔ Recovery (Vol 13.11): handover conditions, timing, and state transfer, details TBD
- Escape ↔ Safety programme (Vol 13.2–13.7): escape-related hazards, causes, and mitigations enter the hazard log and analyses, IDs TBD
- Escape ↔ Operations (Vol 11): decision authority, crew procedures, and ground roles, details TBD
- Escape ↔ V&V / Test (Vol 22–24): escape verification cases and test-methodology hooks, IDs TBD

## 10. Operational Concept

Test methodology and gating only: this concept defines readiness evidence and decision logic structure, not vehicle handling or flight conduct.
Lifecycle direction: concept selection → envelope definition → analysis → ground/component demonstration → unmanned demonstration as applicable (scope TBD) → Safety Review Board assessment before any human-flight relevance is claimed.
No operational escape procedure is authorised in this revision; procedures, training, and authority delegation are TBD and gated by FRR.

## 11. Safety

No escape effectiveness claimed in this revision; the concept is open and recovery effectiveness is unproven (ISS-008 context).
Escape functions, if later selected, shall enter hazard analyses (PHA/FHA/FMEA/FTA/CCA as applicable, timing TBD) and shall not take credit for retiring catastrophic hazards until mitigations are verified and retired by the Safety Review Board (criteria TBD).
> Hazardous-subsystem boundary: this section states safety-analysis and gating rules only.

## 12. Performance

Escape performance indicators and thresholds TBD (no values baselined): separation reliability TBD, envelope coverage TBD, handover success criteria TBD, decision latency TBD.
No numerical targets are set in this revision; scales and acceptance criteria TBD in later revisions with Vol 13/24 concurrence.

## 13. Verification & Validation

Verification direction: REQ-HFPX-ESC-001..002 by analysis (concept and envelope definitions reviewed against hazard coverage); REQ-HFPX-ESC-003 by demonstration (handover logic and interfaces demonstrated at a fidelity TBD); REQ-HFPX-ESC-004 by inspection (authority definition reviewed against operations and safety governance).
Acceptance criteria TBD per case; evidence recorded as TBD/empty until closed.
Validation by Safety Review Board plus programme-authority approval at gates; no human-flight credit until demonstrated and retired (criteria TBD).

## 14. Risks

- Concept vacuum: downstream volumes assume an escape capability that is unselected; mitigation: explicit open-concept status enforced at every gate review
- Handover gap: separation succeeds but recovery handover fails (ISS-008); mitigation: handover treated as a separate verification thread with no end-to-end claim until demonstrated
- Authority ambiguity: unclear who commands escape under time pressure; mitigation: decision-authority definition required before PDR as applicable (owner and gate TBD)

## 15. Open Issues

Concept unselected (means, allocation, and feasibility TBD). Escape envelope undefined. Handover conditions and success criteria undefined. Decision authority undefined. All escape evidence TBD/empty. ISS-008 applies to any survival outcome via escape-to-recovery.

## 16. Assumptions

- Escape / separation feasibility within mass, volume, and safety budgets is unproven; validation: SAD allocation and Vol 13 analysis (both TBD)
- An escape envelope can be defined and verified without human-flight trials; validation: Vol 19 modelling and Vol 23 test methodology (both TBD)
- Decision authority can be defined deterministically for early flight; validation: Vol 11 operations concept and safety governance (both TBD)

## 17. Dependencies

Depends on STK-001/SYS-002/003/SAF tier (requirements basis), Safety Case and hazard analyses (hazard coverage), Vol 11 (operations and authority), Vol 13.11 (recovery handover), Vol 19 (modelling), Vol 22–24 (VCRM and verification), Vol 25 (certification basis, ISS-001).

## 18. Traceability

Parents: TBD (safety and operational parents to be allocated at concept selection).
Children: escape verification cases and handover interface requirements (artefact IDs TBD).
RTM: REQ-HFPX-ESC-001..004 → CONCEPT. No baselined trace beyond this document in this revision.

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Concept selection, envelope definition, or authority change requires a change record with affected-requirement and hazard impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (escape/separation direction; concept open) |
