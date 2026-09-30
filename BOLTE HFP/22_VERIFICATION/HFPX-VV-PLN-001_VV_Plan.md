# Verification & Validation Plan (V&V Plan)

**Document ID:** HFPX-VV-PLN-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X requirements are verified and validated across all volumes and lifecycle gates. Owns Volume 22 direction and is backbone document 4 of 5.
Establishes verification methods, levels, VCRM discipline, gated test progression, and acceptance principles.
This plan sets methodology and gating only; it contains no propulsion build, ignition, or operation instructions.

## 2. Scope

Covers verification and validation of hardware, software, system integration, and safety for all 34 volumes.
Governs Vol 22.3 VCRM, Vol 22.9–22.12 verification levels, Vol 22.13 acceptance, and allocation of test execution to Vol 23.
Applies from SRR through ORR; detailed test cases and procedures are owned by Vol 22/23 children (IDs TBD).

## 3. Applicable Documents

- HFPX-PGM-SEM-001 SEMP (REQ-HFPX-PGM-010/011/013 — requirements management, verification method, gated reviews)
- HFPX-SYS-REQ-001 SyRS, notably §13 (verification approach stub)
- HFPX-SYS-ARC-001 SAD (stub), HFPX-PGM-CHR-001 Programme Charter
- HFPX-SAFE-CAS-001 Safety Case (companion backbone 5/5), Vol 19 (analysis), Vol 23 (test execution)
- Standards (structured according to): ISO/IEC/IEEE 29148, ISO/IEC/IEEE 15288, SAE ARP4754A, ARP4761/4761A concepts; DO-178C/DO-254/DO-160 concepts — no compliance claimed

## 4. Definitions & Acronyms

- V&V: Verification (was it built right) vs Validation (was the right thing built); VCRM: Verification Cross-Reference Matrix (Vol 22.3)
- Verification methods — Analysis (A): calculation, modelling, simulation review; Inspection (I): visual/document examination; Demonstration (D): witnessed functional observation without quantitative pass/fail instrumentation; Test (T): measured execution against TBD acceptance criteria
- Levels: hardware, software, system, safety (Vol 22.9–22.12); SIL: Software/System Integration Laboratory; HIL: Hardware-in-the-Loop
- Gate skipping: proceeding to a higher test level without closing prior gate exit criteria — prohibited

## 5. System Context

V&V sits as the right-hand side of the programme V-model, traced from stakeholder needs through requirements, architecture, and design:

```text
NEEDS → SyRS → SAD → DESIGN → BUILD → INTEGRATE
                                          ↓
VALIDATE ← ACCEPT ← SYSTEM ← HIL ← SIL ← SIM
   ↑________ VCRM TRACEABILITY (no orphans) ________↑
   ↑________ INDEPENDENT SAFETY VERIFICATION ________↑
```

MVP (Vol 33) follows the same V-model in miniature under separate control; production V&V evidence is not claimed from MVP unless explicitly traced.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-VVP-001 | The programme shall assign every requirement exactly one primary verification method: Analysis, Inspection, Demonstration, or Test. | Inspection |
| REQ-HFPX-VVP-002 | The programme shall maintain a VCRM (Vol 22.3) tracing every requirement to its verification case(s), with no orphaned requirements and no orphaned verification cases. | Analysis |
| REQ-HFPX-VVP-003 | Verification shall be executed at defined hardware, software, system, and safety levels (Vol 22.9–22.12), with level allocation recorded in the VCRM. | Inspection |
| REQ-HFPX-VVP-004 | Test progression shall be gated sim → SIL → HIL → unmanned testing, with no gate skipping; each gate requires entrance criteria, completed evidence, and formal gate decision before progression. | Demonstration |
| REQ-HFPX-VVP-005 | Every verification case shall define acceptance criteria before execution; where criteria are not yet defined they shall be recorded as TBD per case. | Test |
| REQ-HFPX-VVP-006 | Safety verification shall be independent of the design organisation to a degree TBD, with independent review or test of safety requirements and safety-critical verification cases. | Inspection |

## 7. Architecture

V&V organisation (roles TBD): V&V / Test lead, analysis lead (Vol 19), ground-test lead (Vol 23.2), flight-test lead (Vol 23.10–23.11/23.13), independent safety verifier reporting via Safety Review Board.
Level structure: Vol 22.9 hardware (component/subsystem qualification logic, environments TBD), Vol 22.10 software (assurance logic TBD, advisory-AI vs deterministic-control separation), Vol 22.11 system integration (interface and end-to-end threads), Vol 22.12 safety verification (independent path, hazard-closure evidence).
VCRM (Vol 22.3) is the single traceability authority: Requirement → Verification case ID (TBD) → Method (A/I/D/T) → Level → Executing volume → Result/status.

## 8. Detailed Design

Level-to-volume mapping (methodology only): analysis and modelling in Vol 19; ground verification in Vol 23.2; tethered and unmanned flight verification in Vol 23.10–23.11; human flight verification in Vol 23.13 only after prior gates close and FRR authorises (criteria TBD).
Each verification case template (Vol 22 children) shall contain objective, traced parent requirement(s), method, level, environment/configuration, acceptance criteria (TBD per case), and independence claim where applicable.
Regression policy TBD: any baselined-requirement change re-opens affected VCRM rows until re-verified; scope defined per change record.

## 9. Interfaces

- V&V ↔ SE (SEMP gates SRR→ORR; entrance/exit criteria per Vol 00.14, details TBD)
- V&V ↔ Safety (Vol 13/24: hazard-derived safety requirements flow into VCRM; closure evidence flows back)
- V&V ↔ Design volumes (Vol 03–18 provide test articles and design evidence; ICDs per 02.17 define interface verification threads)
- V&V ↔ Certification (Vol 25 defines which verification evidence is certification credit; no credit claimed in this revision)

## 10. Operational Concept

V&V operates gate-to-gate: plan cases early (SRR/PDR) → develop procedures and success criteria (CDR/TRR) → execute sim/SIL/HIL → subsystem and integrated ground verification → unmanned verification → readiness reviews (FRR) → acceptance → audit (FCA/PCA).
No test level is an operation: flight-test execution details, range conduct, and vehicle handling belong to Vol 23 and are gated, not directed, by this plan.
Cadence, test-board membership, and tooling TBD (Vol 22/23 children).

## 11. Safety

Safety requirements derived from the hazard log and safety analyses receive Test or Analysis verification with independent review per REQ-HFPX-VVP-006.
Catastrophic-hazard closure evidence is independently verified before any human-flight gate is considered (criterion TBD, owned by Safety Case).
AI outputs are advisory-only in early flight; any AI-influenced verification thread shall identify the deterministic bounded function actually verified (details TBD).

## 12. Performance

V&V performance indicators TBD (no thresholds baselined): VCRM coverage (target TBD, objective no orphans), verification closure burn-down per gate, first-pass rate TBD, regression re-verification backlog TBD.
Measurement method and reporting cadence TBD in Vol 22 children; all thresholds TBD.

## 13. Verification & Validation

V-model applied to this plan: this document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, A/I/D/T on every requirement, VCRM rule, gated progression, independence rule).
Acceptance-test principles (Vol 22.13): acceptance cases are pre-defined, traced, configuration-controlled, executed on representative articles/configurations (representativeness TBD), with TBD criteria and independent witness where safety-relevant.
Validation of the V&V approach is programme-authority approval at gated reviews; certification validation is owned by Vol 25 (no claims here).

## 14. Risks

- VCRM drift across 517 chapters producing orphaned requirements or un-traced tests; mitigation: VCRM coverage gate at each review (threshold TBD)
- Pressure to skip gates (e.g., to unmanned or human flight without HIL/SIL closure); mitigation: REQ-HFPX-VVP-004 no-skipping rule with formal gate records
- Acceptance criteria left TBD indefinitely, blocking closure; mitigation: per-case TBD tracking with owning volume and due gate (assignments TBD)

## 15. Open Issues

All verification case IDs TBD (Vol 22/23 children not written). Acceptance criteria TBD per case. Independence degree and witness rules TBD. Regression scope rules TBD. Tooling for VCRM maintenance TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SEMP (process and gates), SyRS §13 (verification approach), SAD (allocation to levels), Safety Case and Vol 13 hazard/safety requirements (safety verification workload), Vol 19 (analysis capability), Vol 23 (test execution capability), Vol 25 (certification credit rules, ISS-001).

## 18. Traceability

Parents: SEMP REQ-HFPX-PGM-010/011/013; SyRS §13. Children: Vol 22 test-case volumes and Vol 23 execution volumes (verification IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VVP-001..006 → CONCEPT. No orphaned requirements; no orphaned verification cases per REQ-HFPX-VVP-002.

## 19. Configuration

BL-0.0. Tranche 2 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates the VCRM for affected rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Vol 22 direction; backbone 4/5) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
