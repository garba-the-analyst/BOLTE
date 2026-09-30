# Control-System Tests

**Document ID:** HFPX-TEST-CTL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the control-system test methodology (Chapter 23.9): control-law/mixing/allocation verification hooks (FVV thread), fault-injection scope structure, pass/fail discipline, and unmanned-first rule for control changes.
Methodology and gating only; no hazardous test-execution or flight-execution instructions.

## 2. Scope

Covers control-system verification methodology from simulation through HIL and ground integration into gated flight stages, including MVP-thread flight items where traced. Excludes detailed law designs, procedures, threshold values (TBD) and flight conduct (Vol 23.10–23.14, Vol 25-gated).

## 3. Applicable Documents

- HFPX-TEST-STR-001 Test & Evaluation Strategy (gated thread, no-skipping)
- HFPX-VV-PLN-001 V&V Plan (REQ-HFPX-VVP-001..006)
- HFPX-PGM-SEM-001 SEMP (DDR-001 gate discipline)
- HFPX-SYS-REQ-001 SyRS (tier allocation TBD); control-system design volumes + FVV thread (parents, TBD)
- Vol 33 MVP thread (flight items under separate control, TBD); Vol 13 / Vol 24 (hazard-derived obligations, TBD); Vol 25 (authorisation — TBD)

## 4. Definitions & Acronyms

- Control law / mixing / allocation: the deterministic bounded functions distributing commands to effectors (design TBD; verification hooks only).
- FVV: flight-vehicle verification thread hosting control-system claims (details TBD).
- Fault injection: the planned stimulation of failure modes to verify detection, accommodation, and annunciation (scope TBD; methodology only).
- Unmanned-first: the rule that control changes are flight-verified without crew before any crewed consideration (details TBD).

## 5. System Context

Control-system verification ascends sim → SIL → HIL → ground integration, then gated flight, with the FVV thread tracing law/mixing/allocation claims:

```text
SIM → SIL → HIL → INTEGRATED GROUND → [GATE] → UNMANNED → (TETHERED → HUMAN, Vol 25-gated)
  ↑_________ LAW / MIXING / ALLOCATION HOOKS (FVV) __________↑
  ↑_________ FAULT-INJECTION THREAD (scope TBD) _____________↑
```

MVP flight items follow the same gated logic in miniature under separate control; no production credit unless explicitly traced.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TCL-001 | Control laws, mixing, and allocation shall have verification hooks traced to parent FVV-thread requirements, with methods, levels, and criteria recorded as TBD. | VVP-002 | Analysis |
| REQ-HFPX-TCL-002 | Fault-injection verification shall be defined with scope, injected modes, configurations, and environments recorded as TBD, covering methodology and gating only. | VVP-003 | Demonstration |
| REQ-HFPX-TCL-003 | Every control-system test case shall define pass/fail criteria before execution, with all threshold values recorded as TBD in this revision. | VVP-005 | Test |
| REQ-HFPX-TCL-004 | Control-system changes shall be flight-verified unmanned-first, with no crewed flight consideration until unmanned evidence, gate closure, and authorisation are complete and criteria recorded as TBD. | VVP-004, MVP thread | Demonstration |

All pass/fail thresholds: TBD. No quantitative values are baselined in this revision.

## 7. Architecture

Verification levels (details TBD): sim/SIL/HIL configurations (TBD), integrated ground threads (TBD), unmanned flight verification (Vol 23.11, TBD), tethered/human only via closed gates and FRR/Vol 25 (TBD). Ownership and adequacy TBD per HFPX-TEST-GND-001. Data interfaces to Vol 23.16–23.17 (TBD).

## 8. Detailed Design

Hook structure: parent FVV requirement (TBD) → case ID (TBD) → method (A/I/D/T, TBD) → level (TBD) → criteria (TBD).
Fault-injection structure (values TBD): injected-mode list (TBD), configuration, environment, detection/accommodation/annunciation observables (TBD), entrance/exit criteria, evidence set; methodology reference only, no execution instruction.
Unmanned-first structure: change trigger, unmanned evidence package (TBD), gate decision, authorisation hook (Vol 25, TBD), crewed-consideration precondition (TBD).

## 9. Interfaces

- Control tests ↔ FVV thread + design volumes (law/mixing/allocation parents — TBD).
- Control tests ↔ VCRM (case IDs, methods, levels — TBD) and MVP thread (flight items, separately controlled — TBD).
- Control tests ↔ Ground programme (HFPX-TEST-GND-001: rig ownership, credit rule).
- Control tests ↔ Safety/authorisation (Vol 13/24/25: hazard parents, FRR, range-safety — TBD).

## 10. Operational Concept

Define hooks and TBD criteria → verify at lowest adequate level (sim/SIL/HIL/ground) → fault-injection per authorised plan (plan TBD, not in this document) → capture data → gate decision → unmanned flight verification for changes → tethered/human only after closed gates and authorisation.
No case in this document authorises flight execution.

## 11. Safety

Safety-relevant control threads require independent review per VVP-006 (degree TBD). Fault-injection involving hazardous configurations is subject to safety/range controls and authorisation TBD via Vol 25 hooks. This document contains no hazardous test-execution instructions.

## 12. Performance

Indicators TBD (no thresholds baselined): hook-trace completeness (TBD), fault-injection scope-definition completeness (TBD), unmanned-first compliance (TBD), first-pass rate (TBD). Method and cadence TBD.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, shall-statements, A/I/D/T allocation, fault-injection and unmanned-first rules, no-skipping alignment).
Validation is programme-authority approval at gated reviews. Certification validation owned by Vol 25 (no claims here).

## 14. Risks

- Law/mixing/allocation hooks left untraced to FVV parents; mitigation: REQ-HFPX-TCL-001 hook rule with VCRM coverage gate (threshold TBD).
- Fault-injection scope left TBD enabling unverified failure handling; mitigation: per-mode TBD tracking with due gate (assignments TBD).
- Pressure to fly control changes crewed without unmanned evidence; mitigation: REQ-HFPX-TCL-004 unmanned-first rule with DDR-001 / VVP-004 enforcement.

## 15. Open Issues

FVV parents, methods, levels, criteria TBD. Fault-injection modes, configurations, environments TBD. All pass/fail thresholds TBD. Unmanned-first evidence and authorisation details TBD (Vol 25, MVP thread TBD).

## 16. Assumptions

- A-TCL-001: Sim/SIL/HIL environments can be shown representative for control-system claims via arguments TBD per claim; validation: independent review.
- A-TCL-002: Fault-injection methodology can be defined without prescribing hazardous execution in this document; validation: safety review.
- A-TCL-003: MVP-thread unmanned results can inform production threads only through explicitly traced similarity claims (method TBC).

## 17. Dependencies

Depends on HFPX-TEST-STR-001, HFPX-TEST-GND-001, V&V Plan, SEMP gates, SyRS tier allocation, control-system design volumes and FVV thread, MVP thread (Vol 33), Vol 23.10–23.14 flight stages, Vol 23.16–23.17 instrumentation/data, Vol 25 authorisation.

## 18. Traceability

Parents: REQ-HFPX-VVP-001..006; HFPX-SYS-REQ-001 (tier allocation TBD); FVV thread (TBD); MVP thread for flight items (Vol 33, TBD). Children: control-system verification cases and VCRM rows (IDs TBD).
RTM: REQ-HFPX-TCL-001..004 → CONCEPT. No orphaned requirements in this document.

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. CONCEPT. Future changes via change records; changes re-validate affected VCRM rows before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Ch 23.9 Control-System Tests) |
