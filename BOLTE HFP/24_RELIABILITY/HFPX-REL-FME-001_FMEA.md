# FMEA

**Document ID:** HFPX-REL-FME-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X system-level Failure Modes and Effects Analysis direction for Volume 24 (Chapter 24.4): how system-level FMEA ownership, worksheet schema, criticality treatment, and hooks to Vol 13.5 item FMEAs will be controlled.
Sets analysis-method and recording rules only; it contains no failure rates or criticality values beyond TBD.

## 2. Scope

Covers system-level FMEA across HFP-X functions and interfaces, with indenture and boundary definitions TBD.
In scope: ownership, worksheet schema, criticality rules, and hooks to Vol 13.5 item FMEAs. Out of scope: item-level FMEA content owned by Vol 13.5, and quantitative failure data owned by Vol 24.3.
Apportionment and verification hooks feed Vol 24.2 and VCRM as applicable.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-FRA-001 Failure Rate Analysis, HFPX-SAFE-CAS-001 Safety Case
- Vol 13.5 item FMEAs, Vol 13 hazard log, HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- FMEA: Failure Modes and Effects Analysis; systematic examination of failure modes, causes, and effects; scope TBD
- Worksheet schema: controlled columns for each FMEA row; schema TBD
- Criticality: ranking or categorisation of severity and related attributes; scales and method TBD
- System-level vs item-level: system FMEA owned here, item FMEAs owned by Vol 13.5; boundary TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

System-level FMEA constrains design by exposing failure-mode effects at interfaces and functions before detailed item analysis completes.
This document governs analysis discipline; effects and criticality conclusions require evidence and safety-path acceptance before any claim.
Inputs depend on Vol 24.3 data rules (all values TBD) and feed Vol 24.5 FTA and Vol 13 analyses as applicable.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RFM-001 | The programme shall own and maintain a system-level FMEA, with ownership, scope, and boundary TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RFM-002 | The programme shall record the system-level FMEA in a defined worksheet schema, with schema and completeness rules TBD. | TBD reliability classification; REQ-HFPX-SCA-001 | Inspection |
| REQ-HFPX-RFM-003 | The programme shall apply a defined criticality treatment to FMEA rows, with method, scales, and ranking rules TBD. | TBD reliability classification; SAF tier | Analysis |
| REQ-HFPX-RFM-004 | The system-level FMEA shall maintain defined hooks to Vol 13.5 item FMEAs, with interface, traceability, and update rules TBD. | TBD reliability classification; Vol 13.5; REQ-HFPX-SCA-002 | Inspection |

## 7. Architecture

FMEA organisation TBD: system-level owner, item-level owners in Vol 13.5, independent reviewer TBD.
Worksheet architecture TBD: one row per failure mode with cause, effect, controls, and verification columns TBD.
Hook architecture TBD: system rows trace to item rows and hazard-log entries as applicable.

## 8. Detailed Design

Methodology only, no values:
- Ownership and scope: functions covered TBD; interfaces covered TBD; ground rules and conventions TBD.
- Worksheet schema: columns TBD; coding rules TBD; completeness criterion TBD (no empty mitigation or verification field at closure — closure criteria TBD).
- Criticality treatment: severity scale TBD; occurrence/detection treatment TBD; ranking thresholds TBD (no thresholds baselined).
- Vol 13.5 hooks: bidirectional trace TBD; change-propagation rule TBD; consistency-check method TBD.

## 9. Interfaces

- FMEA ↔ Failure-rate analysis (Vol 24.3 source hierarchy applies; values TBD)
- FMEA ↔ FTA (Vol 24.5 / Vol 13.6 exchange of causal logic; scope TBD)
- FMEA ↔ Hazard log and Vol 13.5 (hazard causes/effects exchange; hazard authority owned by Vol 13)
- FMEA ↔ Allocation (Vol 24.2 intent assessed against FMEA findings as applicable)
- FMEA ↔ V&V (FMEA-derived actions enter VCRM; verification returns closure TBD)

## 10. Operational Concept

FMEA matures across the lifecycle: ground rules at SRR → system FMEA through PDR/CDR as applicable → item-hook closure before CDR/FRR as applicable → gate acceptance TBD.
This concept defines analysis-maturation discipline only, not design changes or test conduct.
No FMEA closure or criticality outcome is claimed in this revision.

## 11. Safety

No safety claim is made in this revision; FMEA outputs may inform Vol 13 hazard analyses but take no safety credit until verified through the safety path.
Hazard retirement remains owned by Vol 13 and HFPX-SAFE-CAS-001; no retirement is claimed here.

## 12. Performance

FMEA performance indicators TBD (no thresholds baselined): worksheet completeness TBD, criticality-recording completeness TBD, Vol 13.5 hook coverage TBD, action-closure backlog TBD.
No failure rates, MTBF values, availability figures, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, schema rule, hook coverage, no-values rule).
Requirement verification follows the V&V Plan: Inspection/Analysis methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Incomplete system FMEA treated as complete; mitigation: completeness rules and gate applicability TBD
- Criticality subjectivity without calibrated scales; mitigation: scale definitions TBD before any ranking claim
- Divergence between system and Vol 13.5 item FMEAs; mitigation: hook and consistency-check rules TBD

## 15. Open Issues

Ownership TBD. Worksheet schema TBD. Criticality method and scales TBD. System/item boundary TBD. Vol 13.5 hook details TBD. All quantitative inputs TBD. Gate applicability TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-FRA-001, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 13 hazard log and Vol 13.5, Vol 24.5/Vol 13.6 FTA exchange.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, REQ-HFPX-SCA-001/002. Children: system FMEA worksheets and Vol 13.5 item FMEAs (artefact IDs TBD).
RTM: REQ-HFPX-RFM-001..004 → CONCEPT. Each FMEA row traces to cause → effect → criticality TBD → mitigation → VCRM case (all TBD except schema direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. FMEA worksheets under reliability configuration control once opened; changes via change records with affected-row impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (system-level FMEA direction; schema and criticality TBD) |
