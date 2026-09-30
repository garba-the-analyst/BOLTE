# Failure Modes and Effects Analysis

**Document ID:** HFPX-SAFE-FME-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X Failure Modes and Effects Analysis (Vol 13.5): item scope, worksheet schema, criticality rule, design-action tracking, and maintenance with design changes.

## 2. Scope

Item scope: propulsion modules, FCS, avionics, power, recovery (item list TBD). Covers failure modes, effects, and causes at item level; system-level propagation via FTA/CCA. Boundary note: analysis structure only — no propulsion build, ignition, or operation instructions; no recovery build or operation instructions.

## 3. Applicable Documents

- HFPX-SAFE-CAS-001 Safety Case (REQ-HFPX-SCA-001/002/006)
- HFPX-SAFE-HAZ-001; HFPX-SAFE-PHA-001; HFPX-SAFE-FHA-001
- Safety tier SAF-001..006; SAD SFA-003; SEMP; V&V Plan

## 4. Definitions & Acronyms

- FMEA: Failure Modes and Effects Analysis — bottom-up item failure analysis.
- Worksheet schema: Item → Failure mode → Hazard → Cause → Effect → Severity(TBD) → Probability(TBD) → Mitigation/TBD design action → Verification(TBD).
- Criticality scale TBD (levels, definitions, and thresholds TBD).

## 5. System Context

FMEA grounds system hazards in item failures: each row ties an item mode to hazard-log effects and drives design actions verified under Vol 24.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FME-001 | The FMEA shall address propulsion modules, FCS, avionics, power, and recovery items with a TBD item list. | REQ-HFPX-SCA-002, SAF-002, SFA-003 | Analysis |
| REQ-HFPX-FME-002 | Each FMEA entry shall record failure mode, effect, and cause per the §8 worksheet schema with the Hazard → Cause → Effect → Severity → Probability → Mitigation → Verification chain. | REQ-HFPX-SCA-001, SAF-006, SFA-003 | Inspection |
| REQ-HFPX-FME-003 | Criticality shall use a TBD scale; no criticality rating shall be asserted until the scale is approved. | REQ-HFPX-SCA-001, SAF-003 | Inspection |
| REQ-HFPX-FME-004 | FMEA-driven design actions shall be tracked to closure with traced verification. | REQ-HFPX-SCA-002, SAF-006 | Analysis |
| REQ-HFPX-FME-005 | The FMEA shall be maintained with design changes; affected rows shall be re-assessed and deltas recorded. | REQ-HFPX-SCA-006, SAF-006, SFA-003 | Inspection |

## 7. Architecture

FMEA organised by item group (propulsion / FCS / avionics / power / recovery); rows owned by domain delegates, reviewed by safety lead.

## 8. Detailed Design

Worksheet columns: Item, Failure mode, Hazard, Cause, Effect, Severity (TBD), Probability (TBD), Criticality (TBD), Mitigation / Design action (TBD), Verification (TBD).

Starter worksheet (effects qualitative, ratings TBD):

| Item / Failure mode | Hazard → Cause → Effect | Severity | Probability / Criticality | Mitigation / Design action | Verification |
| --- | --- | --- | --- | --- | --- |
| Arm-module thrust loss | Hazard: hover thrust asymmetry → Cause (qualitative): module fault or feed fault (detail TBD) → Effect: degraded hover control (quantification TBD) | TBD | TBD / TBD | TBD | TBD |
| Safety-computer channel fault | Hazard: loss of voted control → Cause (qualitative): channel fault or common software fault (detail TBD) → Effect: control degradation or failover (quantification TBD) | TBD | TBD / TBD | TBD | TBD |
| Fuel-feed interruption | Hazard: thrust loss across modules → Cause (qualitative): feed blockage or valve fault (detail TBD) → Effect: multi-module thrust decay (quantification TBD) | TBD | TBD / TBD | TBD | TBD |
| Telemetry-link loss | Hazard: loss of off-board awareness → Cause (qualitative): link or ground fault (detail TBD) → Effect: delayed abort decision (quantification TBD) | TBD | TBD / TBD | TBD | TBD |

## 9. Interfaces

- FMEA ↔ Hazard log: modes extend log rows.
- FMEA ↔ FTA/CCA: modes feed basic events / common-cause candidates.
- FMEA ↔ Design volumes: actions allocated to Vol 03–18.

## 10. Operational Concept

Scope items → analyse modes → rate (TBD scale) → assign actions → track to closure → maintain with changes. Methodology and gating only.

## 11. Safety

No criticality values asserted. Analysis only — no build/ignition/operation instructions.

## 12. Performance

Indicators TBD: item coverage, action closure, re-assessment currency. No thresholds baselined.

## 13. Verification & Validation

Verified by inspection (schema, scale) and analysis (closure tracking). Validation at CDR/FRR gates.

## 14. Risks

- Item-list incompleteness; mitigation: SAD-tied list TBD.
- Unrated criticality drift; mitigation: TBD scale gate.
- Orphan actions; mitigation: closure tracking (REQ-HFPX-FME-004).

## 15. Open Issues

Item list TBD. Criticality scale TBD. Action owners TBD. All ratings/actions TBD.

## 16. Assumptions

- A-FME-01: Item groups listed bound concept FMEA scope; validation: SAD review (TBD).
- A-FME-02: Qualitative effects suffice before CDR; validation: CDR review (TBD).

## 17. Dependencies

Depends on Safety Case, HAZ/PHA/FHA, SAF-001..006, SFA-003, SEMP, Vol 24.

## 18. Traceability

Parents: REQ-HFPX-SCA-001/002/006; SAF-001..006; SFA-003. Children: Vol 13.8–13.18; Vol 24. RTM: REQ-HFPX-FME-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes via change records.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (FMEA structure, starter worksheet) |
