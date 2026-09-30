# Fault Tree Analysis

**Document ID:** HFPX-REL-FTA-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X system-level Fault Tree Analysis direction for Volume 24 (Chapter 24.5): how system-level top events, method, data inputs, and hooks to Vol 13.6 will be controlled.
Sets analysis-method and recording rules only; it contains no failure rates, probabilities, or top-event quantifications beyond TBD.

## 2. Scope

Covers system-level FTA for defined top events, with top-event list TBD.
In scope: top-event selection, method rules, data rules, and hooks to Vol 13.6 fault trees. Out of scope: Vol 13.6 tree content, and quantitative basic-event data owned by Vol 24.3.
Feeds allocation assessment and safety-path inputs as applicable.

## 3. Applicable Documents

- Programme Charter STK-001; SyRS SYS-002/003; reliability classification tier TBD; SAF tier (stubs)
- HFPX-REL-ENG-001 Reliability Engineering, HFPX-REL-FRA-001 Failure Rate Analysis, HFPX-REL-FME-001 FMEA, HFPX-SAFE-CAS-001 Safety Case
- Vol 13.6 fault trees, Vol 13 hazard log, HFPX-VV-PLN-001 V&V Plan
- Standards (structured according to): TBD — no compliance claimed in this revision

## 4. Definitions & Acronyms

- FTA: Fault Tree Analysis; deductive analysis from a top event through logic gates to basic events; method TBD
- Top event: undesired system-level event at the tree root; list TBD
- Basic event: terminal input event with data TBD; all quantifications TBD
- Cut set: combination of basic events causing the top event; computation method TBD
- TBD: to be determined; TBC: to be confirmed

## 5. System Context

System-level FTA constrains design by exposing combinations of causes behind top events before quantitative targets can be discussed.
This document governs tree discipline; top-event conclusions require evidenced data and safety-path acceptance before any claim.
Inputs depend on Vol 24.3–24.4 rules (all values TBD) and exchange logic with Vol 13.6 as applicable.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RFT-001 | The programme shall define system-level FTA top events, with selection criteria and list TBD. | TBD reliability classification; HFPX-REL-ENG-001 | Inspection |
| REQ-HFPX-RFT-002 | The programme shall apply a defined FTA method, with conventions, gate rules, and tool qualification TBD. | TBD reliability classification; REQ-HFPX-SCA-002 | Inspection |
| REQ-HFPX-RFT-003 | The programme shall govern FTA data inputs under defined data rules, with all data TBD per Vol 24.3 hierarchy. | TBD reliability classification; Vol 24.3 | Analysis |
| REQ-HFPX-RFT-004 | System-level FTA shall maintain defined hooks to Vol 13.6 fault trees, with interface, traceability, and update rules TBD. | TBD reliability classification; Vol 13.6; REQ-HFPX-SCA-002 | Inspection |

## 7. Architecture

FTA organisation TBD: system-level owner, Vol 13.6 owners, independent reviewer TBD.
Tree architecture TBD: top events, intermediate gates, basic events, with naming and coding rules TBD.
Hook architecture TBD: system trees trace to Vol 13.6 trees and hazard-log entries as applicable.

## 8. Detailed Design

Methodology only, no values:
- Top events: selection criteria TBD; list TBD; scope per event TBD.
- Method: gate conventions TBD; common-cause treatment reference TBD (CCA owned by Vol 13.7 as applicable); cut-set computation TBD; tool rules TBD.
- Data: basic-event data qualification TBD; uncertainty propagation TBD per Vol 24.3; all quantifications TBD.
- Vol 13.6 hooks: model exchange format TBD; consistency checks TBD; change-propagation rule TBD.

## 9. Interfaces

- FTA ↔ FMEA (Vol 24.4 failure-mode logic cross-check as applicable)
- FTA ↔ Failure-rate analysis (Vol 24.3 hierarchy applies; values TBD)
- FTA ↔ Vol 13.6 and hazard log (tree and hazard exchange; hazard authority owned by Vol 13)
- FTA ↔ Allocation (Vol 24.2 intent assessed against tree findings as applicable)
- FTA ↔ V&V (FTA-derived actions enter VCRM; verification returns closure TBD)

## 10. Operational Concept

FTA matures across the lifecycle: top-event definition at SRR/PDR as applicable → trees through CDR → data maturation through test → gate acceptance TBD.
This concept defines analysis-maturation discipline only, not design changes or test conduct.
No top-event quantification or closure is claimed in this revision.

## 11. Safety

No safety claim is made in this revision; FTA outputs may inform Vol 13 analyses but take no safety credit until verified through the safety path.
No top-event probability claim is made here; hazard probabilities owned by Vol 13 with scales TBD.

## 12. Performance

FTA performance indicators TBD (no thresholds baselined): top-event coverage TBD, tree-completeness TBD, data traceability TBD, Vol 13.6 hook coverage TBD.
No failure rates, probabilities, MTBF values, availability figures, or life limits are set in this revision.

## 13. Verification & Validation

This document is verified at SRR/PDR against the SEMP checklist (header, 20 sections, IDs, hook coverage, no-values rule).
Requirement verification follows the V&V Plan: Inspection/Analysis methods; acceptance criteria TBD per case; evidence TBD until closed.
Validation is programme-authority approval at gates; certification validation owned by Vol 25 with no claims here.

## 14. Risks

- Top-event omission leaving system risk unanalysed; mitigation: selection criteria and coverage review TBD
- Unevidenced basic-event data treated as proven; mitigation: Vol 24.3 hierarchy enforcement at gates
- Divergence between system and Vol 13.6 trees; mitigation: hook and consistency-check rules TBD

## 15. Open Issues

Top-event list TBD. Method conventions TBD. All data TBD. Tool qualification TBD. Vol 13.6 hook details TBD. Gate applicability TBD. Common-cause interface TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-001/SYS-002/003 and TBD reliability classification, HFPX-REL-ENG-001, HFPX-REL-FRA-001, HFPX-REL-FME-001, SEMP, V&V Plan, SAF tier and HFPX-SAFE-CAS-001, Vol 13.6/13.7 and hazard log.

## 18. Traceability

Parents: SYS-002/003, TBD reliability classification, SAF tier, REQ-HFPX-SCA-002. Children: system fault trees and Vol 13.6 trees (artefact IDs TBD).
RTM: REQ-HFPX-RFT-001..004 → CONCEPT. Each top event traces to tree → basic events TBD → data sources TBD → VCRM cases (all TBD except direction).

## 19. Configuration

BL-0.0. Tranche 6 draft, CONCEPT, not baselined. Fault trees under reliability configuration control once opened; changes via change records with affected-tree impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (system-level FTA direction; top events and data TBD) |
