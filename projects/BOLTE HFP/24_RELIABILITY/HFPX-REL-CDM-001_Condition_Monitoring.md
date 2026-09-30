# Condition Monitoring

**Document ID:** HFPX-REL-CDM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X condition-monitoring direction for Volume 24 (Chapter 24.11): how monitored indicators, avionics/health hooks, alert rules, and verification will be controlled.
Sets monitoring-definition and alert-governance rules only; it contains no thresholds, indicators beyond TBD, or automated-action authority.

## 2. Scope

Covers condition-monitoring definitions feeding reliability and support decisions, with indicator list TBD.
In scope: indicator definitions, hooks to 08.10/16.11 functions, alert-rule governance, verification approach. Out of scope: implementation of sensing or avionics owned by Vol 08/16, and predictive functions owned by Vol 24.12.
Monitoring informs action; it commands no safety-critical action in this revision.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-PDM-001 Predictive Maintenance direction, HFPX-SAFE-CAS-001 Safety Case
- Vol 08.10 and Vol 16.11 function hooks, Vol 27 support hooks, HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- Condition monitoring: acquisition and assessment of indicators of item or system condition; indicators TBD
- Monitored indicator: parameter or feature assessed for condition insight; list TBD
- Alert rule: governed rule generating an advisory on assessed condition; rules and thresholds TBD
- Advisory-only: monitoring informs human action and commands no safety-critical action in this revision
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

Condition monitoring constrains how health insight is defined and governed before any operational reliance; reliance requires verified indicators plus accepted alert governance.
This document governs definition discipline; no indicator or alert rule is claimed as valid in this revision.
Sensing, processing, and display implementation are owned by Vol 08/16 under TBD hooks.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RCM-001 | The programme shall define monitored indicators with stated scope and conditions, with indicator list TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RCM-002 | Condition monitoring shall maintain defined hooks to 08.10/16.11 functions, with interface, ownership, and update rules TBD. | TBD reliability classification; Vol 08.10/16.11 | Inspection |
| REQ-HFPX-RCM-003 | The programme shall govern alert rules under defined governance, with rules, thresholds, and authority TBD and advisory-only constraint. | TBD reliability classification; SAF tier | Analysis |
| REQ-HFPX-RCM-004 | Condition-monitoring definitions and alert rules shall be verified under a defined verification approach, with method and criteria TBD. | TBD reliability classification; REQ-HFPX-SCA-004 | Test |

## 7. Architecture

Monitoring organisation TBD: condition-monitoring owner, Vol 08/16 function owners, Vol 27 support consumer, independent reviewer TBD.
Definition architecture TBD: indicator table schema TBD (indicator TBD, source TBD, rate TBD, status).
Alert architecture TBD: advisory path only; human action authority TBD; no autonomous safety action.

## 8. Detailed Design

Methodology only, no values:
- Indicators: candidate domains TBD; selection criteria TBD; definition schema TBD; all indicators TBD.
- Hooks: Vol 08.10 interface TBD; Vol 16.11 interface TBD; data-exchange format TBD; update rule TBD.
- Alert rules: rule syntax TBD; threshold governance TBD (no thresholds baselined); false-alert treatment TBD; advisory routing TBD.
- Recording: indicator and alert-rule records TBD; status values TBD; change control TBD.

## 9. Interfaces

- Monitoring ↔ Avionics/health (Vol 08.10/16.11 sensing and processing; implementation TBD)
- Monitoring ↔ Predictive maintenance (Vol 24.12 consumes monitored indicators as applicable; authority human TBD)
- Monitoring ↔ Support (Vol 27 maintenance-decision inputs; details TBD)
- Monitoring ↔ Safety (advisory-only; safety path owned by HFPX-SAFE-CAS-001; no safety credit here)
- Monitoring ↔ V&V (indicator and alert cases enter VCRM; verification returns closure TBD)

## 10. Operational Concept

Monitoring matures across the lifecycle: indicator definitions at SRR/PDR as applicable → hook implementation through CDR → alert governance through test → gate acceptance TBD.
This concept defines definition and governance discipline only, not sensing operation, flight conduct, or maintenance execution.
No monitoring-based action is authorised beyond advisory in this revision.

## 11. Safety

No safety claim is made in this revision; monitoring outputs are advisory-only and take no safety credit until verified through the safety path.
Monitoring shall not command safety-critical action in this revision; action authority is human TBD.

## 12. Performance

Monitoring performance indicators TBD (no thresholds baselined): indicator coverage TBD, hook completeness TBD, alert-governance completeness TBD.
No thresholds, failure rates, MTBF/MTTR values, availability figures, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, hook direction, advisory-only and no-values rules).
Requirement verification follows the V&V Plan: Inspection/Analysis/Test methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Unverified indicators relied upon for decisions; mitigation: TBD-only indicators enforced at gates
- Alert-rule ambiguity causing missed or spurious advisories; mitigation: governance and verification TBD before reliance
- Hook divergence with Vol 08/16 implementation; mitigation: interface and update rules TBD

## 15. Open Issues

Indicator list TBD. Vol 08.10/16.11 hook details TBD. Alert rules and thresholds TBD. Action authority TBD (human TBD). Verification method TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-PDM-001, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 08.10/16.11 functions, Vol 27 support.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, Vol 08.10/16.11. Children: indicator tables, alert-rule records, VCRM cases (artefact IDs TBD).
RTM: REQ-HFPX-RCM-001..004 → CONCEPT. Each indicator traces to source → alert rule TBD → advisory → VCRM closure (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Changes via change records with affected-indicator impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (condition-monitoring direction; indicators and alert rules TBD) |
