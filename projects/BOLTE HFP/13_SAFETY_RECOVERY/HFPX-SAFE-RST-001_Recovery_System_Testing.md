# Recovery System Testing

**Document ID:** HFPX-SAFE-RST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X recovery-system testing direction (Chapter 13.18): the mandatory gated test thread from component through system to unmanned demonstration, envelope-expansion rules, data-capture requirements, and failure-to-deploy investigation rules.
Sets test-methodology requirements, gating rules, and verification direction only; it claims no recovery effectiveness and grants no human-flight credit in this revision.

## 2. Scope

Covers recovery test-thread definition, test-envelope expansion, test data capture, and failure-to-deploy investigation for all recovery functions (Vol 13.11) and their escape handover (Vol 13.14) where applicable.
In scope: test-thread requirements, gating and progression rules, data-capture requirements, investigation rules, and verification hooks.
Out of scope: recovery hardware design (Vol 13.11), flight-test conduct and range operations (Vol 23 owns execution), and any build or operation instructions.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; safety tier SAF-001..006 (all stubs, values TBD)
- HFPX-SAFE-CAS-001 Safety Case; hazard log (`13_SAFETY_RECOVERY/hazard_log.csv`); HFPX-VV-PLN-001 V&V Plan
- Vol 13.11 recovery system; Vol 13.14 escape/separation; Vol 23 test programme (§23.16 hooks); §33.12 data hooks; Vol 22 VCRM
- Standards (structured according to): SAE ARP4754A, ARP4761/4761A concepts — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Test thread: ordered progression component → system → unmanned demonstration, stage definitions TBD
- Unmanned demonstration: recovery demonstration without pilot on board at a fidelity TBD; the only route to recovery credit in early phases
- Test-envelope expansion: controlled growth of demonstrated conditions, step criteria TBD
- Failure to deploy: any demanded recovery function that does not deploy or perform as required, scope TBD
- Data capture: recorded test evidence required to substantiate each progression gate, content TBD (hooks to §33.12/§23.16)

## 5. System Context

Recovery effectiveness is unproven (ISS-008); this document is the gatekeeper that prevents unproven recovery from taking human-flight credit.
Gated progression is mandatory: no stage may be skipped, and no human-flight relevance may be claimed until the full thread to unmanned demonstration is closed with verified evidence.
Test execution is owned by Vol 23; this document owns the thread definition, gate rules, data requirements, and investigation rules that Vol 23 must satisfy.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-RST-001|The programme shall execute a gated recovery test thread from component through system to unmanned demonstration, with no human-flight credit until demonstrated and retired.|REQ-HFPX-MIS-005|Test|
|REQ-HFPX-RST-002|The programme shall apply a defined test-envelope expansion rule, with step criteria, hold criteria, and rollback criteria TBD.|REQ-HFPX-MIS-005|Inspection|
|REQ-HFPX-RST-003|The programme shall capture defined recovery-test data, with content, fidelity, and retention TBD (hooks to §33.12/§23.16).|REQ-HFPX-MIS-005|Inspection|
|REQ-HFPX-RST-004|The programme shall investigate every failure to deploy under a defined investigation rule, with process, close-out criteria, and re-test rules TBD; gated progression is mandatory.|REQ-HFPX-MIS-005|Inspection|

All envelope bounds, step sizes, data rates, and investigation timelines: TBD. No recovery credit is granted in this revision.

## 7. Architecture

Test-thread architecture (stages TBD): component rigs → subsystem integration → system ground demonstration → unmanned flight demonstration, each stage owning entry criteria, success criteria, and evidence artefacts TBD.
Envelope-expansion control is architecturally identified as a gate function owned jointly with Vol 23 and the Safety Review Board (allocation TBD).
Data-capture and investigation workflows are architecturally identified as separate evidence segments feeding the safety case (hooks to §33.12/§23.16, details TBD).
> Hazardous-subsystem boundary: architecture here addresses test methodology, stage allocation, and evidence flow only; it contains no build or operation instructions.

## 8. Detailed Design

No detailed design in this revision — stage criteria, envelope steps, data content, and investigation process TBD.
Design direction (methodology only): per-stage decomposition into entry criteria → execution conditions → success criteria → evidence package, each TBD and entered into the VCRM before stage execution.
Envelope methodology TBD: parameter set, step/hold/rollback logic, and Vol 19 modelling support to be defined before any expansion claim.

## 9. Interfaces

- Recovery testing ↔ Recovery system (Vol 13.11): test articles, configurations, deployment interfaces, details TBD
- Recovery testing ↔ Escape (Vol 13.14): handover test hooks where applicable, details TBD
- Recovery testing ↔ Test execution (Vol 23, §23.16): range, instrumentation, conduct, and §23.16 data hooks, details TBD
- Recovery testing ↔ Data systems (§33.12): capture, retention, and access hooks, details TBD
- Recovery testing ↔ V&V / Safety (Vol 22/24, Safety Review Board): gate evidence, retirement recommendations, details TBD

## 10. Operational Concept

Test methodology and gating only: this concept defines readiness evidence and progression decisions, not vehicle handling or flight conduct.
Lifecycle direction: define thread and gates → execute component → review gate → execute system → review gate → execute unmanned demonstration → Safety Review Board retirement assessment → envelope-expansion decision per REQ-HFPX-RST-002.
Any failure to deploy halts progression pending investigation close-out per REQ-HFPX-RST-004; skipping stages is prohibited.

## 11. Safety

Recovery effectiveness unproven (ISS-008): no recovery or safe-state capability is claimed, and no human flight shall proceed on recovery credit until the thread is demonstrated and catastrophic hazards retired (criteria and board TBD, gated by FRR).
Test-artefact failures shall enter the hazard log and analyses as applicable; investigation close-out requires verified corrective action, never analysis alone (process TBD).
> Hazardous-subsystem boundary: this section states safety-analysis and gating rules only.

## 12. Performance

Recovery-test performance indicators and thresholds TBD (no values baselined): stage-closure completeness TBD, envelope-step success criteria TBD, data-completeness TBD, investigation close-out timeliness TBD.
No numerical targets are set in this revision; scales and acceptance criteria TBD in later revisions with Vol 13/24 concurrence.

## 13. Verification & Validation

Verification direction: REQ-HFPX-RST-001 by test (stage execution observed through unmanned demonstration at a fidelity TBD); REQ-HFPX-RST-002..004 by inspection (expansion rule, data-capture definition, and investigation rule reviewed against V&V Plan and safety governance).
Acceptance criteria TBD per case; evidence recorded as TBD/empty until closed.
Validation by Safety Review Board plus programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Credit creep: unmanned-demo shortfalls treated as human-flight evidence; mitigation: explicit no-credit-until-demonstrated rule enforced at every gate review
- Envelope rush: expansion steps skipped under schedule pressure; mitigation: mandatory step/hold/rollback criteria with independent gate authority (criteria and authority TBD)
- Data poverty: tests executed without capturable evidence (§33.12/§23.16 hooks missing); mitigation: data-capture definition required before stage entry (owner and gate TBD)

## 15. Open Issues

Stage entry/success criteria undefined. Envelope step/hold/rollback criteria undefined. Data content, fidelity, and retention undefined (§33.12/§23.16 hook details TBD). Investigation process and re-test rules undefined. All recovery-test evidence TBD/empty. ISS-008 open.

## 16. Assumptions

- Component → system → unmanned demonstration is sufficient to bound early recovery risk; validation: Vol 13 analysis and Vol 23 test methodology (both TBD)
- Test-envelope expansion can be controlled by defined step/hold/rollback logic; validation: Vol 19 modelling and Vol 23 execution (both TBD)
- Data hooks to §33.12/§23.16 can be defined to support independent verification; validation: data-system and V&V definitions (both TBD)

## 17. Dependencies

Depends on STK-001/SYS-002/003/SAF tier (requirements basis), Safety Case and hazard analyses (hazard basis), Vol 13.11/13.14 (test articles and handover), SEMP (gates), V&V Plan (verification discipline), Vol 19 (modelling), Vol 22–24 including §23.16 (VCRM and test execution), §33.12 (data), Vol 25 (certification basis).

## 18. Traceability

Parents: TBD (safety and test parents to be allocated once thread stages are defined).
Children: stage test plans, envelope-expansion records, data-capture artefacts, and investigation reports (artefact IDs TBD).
RTM: REQ-HFPX-RST-001..004 → CONCEPT. Each recovery test stage traces to requirements → VCRM cases → gate evidence (all TBD except schema).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Thread, envelope-rule, data-requirement, or investigation-rule change requires a change record with affected-requirement and hazard impact stated. Gated progression is mandatory and not tailorable in this revision.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (recovery-test thread and gating direction; no credit claimed) |
