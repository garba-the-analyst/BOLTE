# Safety Case

**Document ID:** HFPX-SAFE-CAS-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X safety argument direction: how claims, arguments, and evidence will show the system is acceptably safe to proceed at each gate. Owns safety-argument direction and is backbone document 5 of 5.
Sets hazard, analysis, independence, and gating rules only; it contains no propulsion build, ignition, or operation instructions.

## 2. Scope

Covers safety argumentation for all flight regimes, with hover/low-altitude explicitly treated as the limiting case (energy, time, and recovery margins TBD).
Governs Vol 13 hazard and analysis programme (Vol 13.3–13.7) and Vol 24 safety verification threads, feeding certification evidence to Vol 25.
Fire, fuel, thermal, structural, and software hazard coverage is in scope; detailed analyses are owned by Vol 13/24 children.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; safety requirements tier SAF-001..006 (all stubs, values TBD)
- HFPX-PGM-SEM-001 SEMP (gated reviews, safety independence), HFPX-VV-PLN-001 V&V Plan (independent safety verification)
- Vol 13 hazard log (`13_SAFETY_RECOVERY/hazard_log.csv`), Vol 13.3–13.7 analyses, Vol 24 assurance, Vol 25 certification basis
- Standards (structured according to): SAE ARP4754A, ARP4761/4761A concepts — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Safety case: claims → arguments → evidence structure; current evidence: TBD/empty (no safety claims proven in this revision)
- PHA: Preliminary Hazard Analysis; FHA: Functional Hazard Assessment; FMEA: Failure Modes and Effects Analysis; FTA: Fault Tree Analysis; CCA: Common Cause Analysis
- Hazard log: controlled record with one row per hazard (schema §8); catastrophic hazard: severity TBD per Vol 13 criteria — any hazard so classified
- Independent safety path: functionally and organisationally separate means to reach a safe state / recovery, details TBD; AI advisory-only: AI may inform but shall not command safety-critical action in early flight

## 5. System Context

Safety argument constrains the whole programme: design claims are only as strong as hazard closure and independent verification behind them.
Hover/low-altitude flight is the limiting case for this argument because abort time, descent energy, and recovery options are most constrained there (quantification TBD).
Recovery effectiveness is unproven (ISS-008); no recovery or safe-state capability is claimed in this revision.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-SCA-001 | The programme shall maintain a mandatory hazard log in which every hazard records Hazard → Cause → Effect → Severity → Probability → Mitigation → Verification. | Inspection |
| REQ-HFPX-SCA-002 | The programme shall perform PHA, FHA, FMEA, FTA, and CCA (Vol 13.3–13.7) before CDR/FRR as applicable, with applicability per analysis TBD. | Analysis |
| REQ-HFPX-SCA-003 | The system shall provide an independent safety path and defined recovery/safe-state behaviour, with independence and effectiveness criteria TBD. | Demonstration |
| REQ-HFPX-SCA-004 | The safety case shall be structured as claims → arguments → evidence, with evidence recorded as TBD/empty until verified closure artefacts exist. | Inspection |
| REQ-HFPX-SCA-005 | No human flight shall proceed with unretired catastrophic hazards; retirement criteria and authorising board TBD (gated by FRR). | Test |
| REQ-HFPX-SCA-006 | Hazard coverage shall include fire, fuel, thermal, structural, and software hazard classes, each traced to safety requirements and verification. | Analysis |

## 7. Architecture

Safety-case architecture (roles TBD): Safety lead, independent safety verifier, design-domain safety delegates, Safety Review Board as retirement authority.
Claims decompose by hazard class (fire/fuel/thermal/structural/software plus TBD classes); each claim is supported by arguments from analyses (§8) and evidenced by VCRM-linked verification cases (Vol 22/24).
Independent safety path is architecturally segregated from primary control to a degree TBD (computer, power, sensing, actuation separation TBD; SAD to allocate).

## 8. Detailed Design

Hazard-log schema reference (`13_SAFETY_RECOVERY/hazard_log.csv` columns): Hazard ID, Hazard, Cause, Effect, Severity, Probability, Mitigation, Verification, Status — one row per hazard, no empty Mitigation or Verification field at retirement.
Analysis-to-requirement flow (methodology only):

```text
HAZARD LOG → PHA/FHA (Vol 13.3–13.4) → SAFETY REQUIREMENTS (SAF tier)
     ↓              ↓
   FMEA/FTA/CCA (Vol 13.5–13.7) → DESIGN CONSTRAINTS → VCRM CASES (Vol 22/24)
     ↓_________________________________________↓
              SAFETY CASE: CLAIM → ARGUMENT → EVIDENCE (TBD/empty)
```

Analysis timing TBD per gate: PHA/FHA before PDR/CDR as applicable; FMEA/FTA/CCA before CDR/FRR as applicable; retirement requires closed analyses plus verified mitigations, never analysis alone.

## 9. Interfaces

- Safety ↔ SE (gate entrance/exit criteria, hazard-log open at SRR, retirement gates per Vol 00.14, criteria TBD)
- Safety ↔ V&V (safety requirements enter VCRM; independent verification evidence returns as safety-case evidence)
- Safety ↔ Design volumes (Vol 03–18 own mitigation implementation; Vol 19 supports FTA/CCA modelling; Vol 23 executes safety verification under gating)
- Safety ↔ Certification (Vol 25 determines which safety artefacts take certification credit; no credit claimed here)

## 10. Operational Concept

Safety operates as a gatekeeper across the lifecycle: open hazard log at SRR → analyses mature through PDR/CDR → mitigations verified through sim/SIL/HIL and unmanned testing → Safety Review Board assesses retirement → FRR authorises next envelope step.
Test methodology and gating only: this concept defines readiness evidence and retirement decisions, not vehicle handling, ignition sequencing, or flight conduct (owned and gated under Vol 23).
AI remains advisory-only; deterministic bounded control provides the verifiable safety function for early flight (allocation TBD).

## 11. Safety

No compliance claimed in this revision against any airworthiness or system-safety standard; standard references are structural only.
Recovery effectiveness is unproven (ISS-008): recovery and safe-state behaviours are required by REQ-HFPX-SCA-003 but no effectiveness is asserted until demonstrated through gated verification (criteria TBD).
Hover/low-altitude is the limiting case: catastrophic-hazard retirement (REQ-HFPX-SCA-005) is assessed against this regime first; envelope expansion beyond it requires separate retirement evidence (scope TBD).

## 12. Performance

Safety performance indicators TBD (no thresholds baselined): hazard-log completeness (objective TBD), analysis closure per gate TBD, catastrophic-hazard retirement backlog TBD, mitigation verification closure TBD.
All severity/probability scales, risk matrices, and targets TBD in Vol 13 children; no numerical safety targets are set in this revision.

## 13. Verification & Validation

This Safety Case is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, hazard-schema rule, analysis coverage, independence and no-human-flight rules).
Safety-requirement verification follows the V&V Plan: Analysis/Test methods with independent verification; acceptance criteria TBD per case; evidence recorded as TBD/empty until closed.
Validation is Safety Review Board plus programme-authority approval at gates; certification validation is owned by Vol 25 with no claims in this revision.

## 14. Risks

- Unproven recovery (ISS-008) treated as capability by downstream volumes; mitigation: explicit unproven status enforced at every gate review
- Analysis debt: PHA/FHA/FMEA/FTA/CCA deferred past CDR/FRR applicability; mitigation: gate applicability matrix with TBD owners and due gates
- Severity/probability subjectivity without calibrated scales; mitigation: Vol 13 scale definitions TBD before any retirement claim

## 15. Open Issues

ISS-008 (recovery effectiveness unproven). ISS-001 (regulatory basis TBD, Vol 25). Retirement criteria and authorising-board composition TBD. Independence and safe-state definitions TBD. All safety evidence TBD/empty. Severity/probability scales TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003/SAF-001..006 tiers (requirements basis), SEMP (gates and independence), V&V Plan (verification discipline), Vol 13.3–13.7 and Vol 24 (analyses and safety verification), Vol 19 (modelling support), Vol 23 (gated test execution), Vol 25 (certification basis, ISS-001).

## 18. Traceability

Parents: STK-001, SYS-002/003, SAF-001..006 tier. Children: Vol 13/24 analyses and Vol 25 certification evidence (artefact IDs TBD).
RTM: REQ-HFPX-SCA-001..006 → CONCEPT. Each hazard row traces to mitigations → safety requirements → VCRM cases → safety-case evidence (all TBD except schema).

## 19. Configuration

BL-0.0. Tranche 2 draft, CONCEPT, not baselined. Hazard log is under safety configuration control once opened; changes via change records with affected-hazard impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (safety argument direction; backbone 5/5) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
