# Propulsion Status

**Document ID:** HFPX-HMI-PST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the helmet propulsion-status display requirements for HFP-X (Chapter 10.10): what propulsion parameters are presented to the pilot, how exceedances are highlighted, and what data-source interface feeds the display. No parameter set, threshold, symbology, or timing value is defined in this document.

## 2. Scope

Covers helmet display of propulsion status allocated from SYS-005 and STK-007, including parameter presentation, exceedance highlighting, and the data-source interface to Vol 04.11. Excludes propulsion sensing and instrumentation design (Vol 04), warning prioritisation logic (Chapter 10.11), alert inventory and acknowledgement (Chapter 10.12), and power/environmental implementation (Chapters 10.16/10.17). All parameters, thresholds, latencies, and formats are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-002 controllability, STK-007 status/warning guidance)
- HFPX-ARC-HUM-001 Human-System Architecture (REQ-HFPX-HSA-001 helmet integration, REQ-HFPX-HSA-003 workload principles)
- HFPX-SYS-HUM-001 Human Factors Requirements (REQ-HFPX-HUM-001 workload, REQ-HFPX-HUM-002 legibility)
- Vol 04.11 engine instrumentation / propulsion data source (signals TBD)
- Vol 30 human-factors principles (limits and methods TBD)

## 4. Definitions & Acronyms

- HPS: propulsion-status requirement tier; ID prefix `REQ-HFPX-HPS-NNN`
- Propulsion status: helmet-presented propulsion parameters and exceedance states (parameter set TBD)
- Exceedance highlighting: distinct presentation of out-of-bounds propulsion states (means and criteria TBD)
- Data source: propulsion data provider in Vol 04.11 (signals, rates, and integrity TBD)
- TBD: to be defined. No values stated.

## 5. System Context

The helmet propulsion-status function presents propulsion data sourced from Vol 04.11 to the pilot within the integrated helmet/HUD/audio presentation owned by HSA-001. It consumes propulsion estimates and exceedance flags (all TBD) and renders them per legibility and workload constraints (HUM-001/002, Vol 30). It does not generate propulsion measurements and does not own warning prioritisation (Chapter 10.11).

```text
[Vol 04.11 propulsion data (TBD)] --> [Propulsion-status display function (this doc)] --> [Helmet presentation + exceedance highlighting (TBD)]
   constrained by [HUM-001/002 legibility/workload (TBD, Vol 30)] | coordinated with [10.11 warning logic (TBD)]
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HPS-001 | The helmet shall display defined propulsion parameters to the pilot (parameter set, arrangement, and update behaviour TBD). | STK-007, SYS-005, HUM-002 | Demonstration (TBD) |
| REQ-HFPX-HPS-002 | The helmet shall provide distinct exceedance highlighting for defined propulsion exceedance states (states, means, and criteria TBD). | STK-007, SYS-005, HSA-001 | Demonstration (TBD) |
| REQ-HFPX-HPS-003 | The propulsion-status display shall obtain its data from the defined Vol 04.11 source via a defined interface (signals, rates, integrity, and ICD TBD). | SYS-005, HSA-001 | Inspection (TBD) |
| REQ-HFPX-HPS-004 | Each propulsion-status requirement in this document shall have a defined verification method and pass criteria (methods and criteria TBD). | SYS-005 | Inspection (TBD) |

No parameter, threshold, rate, latency, or symbology value in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: HPS-001 → parameter-presentation function; HPS-002 → exceedance-highlighting function; HPS-003 → Vol 04.11 data-source interface; HPS-004 → V&V thread (Vol 22 pattern). Authoritative allocation lives in Vol 10 integration views; this section states derivation intent only. Display structures, symbology, and interface implementations are TBD.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Symbology, layouts, fonts, colours, highlight mechanisms, data formats, and interface implementations are TBD.

## 9. Interfaces

- Propulsion data-source interface to Vol 04.11: signals, rates, integrity, and ICD TBD.
- Helmet presentation interface (display pipeline, symbology host): TBD.
- Warning-system coordination interface (Chapter 10.11 exceedance flag exchange): TBD.
- Workload/legibility constraint interface (Vol 30, HUM-001/002): TBD.
- Formal ICDs are TBD.

## 10. Operational Concept

Requirements are exercised through nominal propulsion-monitoring threads and off-nominal exceedance threads under controlled conditions. Normal threads present propulsion parameters; exceedance threads present highlighted states and hand over to warning/alert handling per Chapters 10.11/10.12. Scenario details and crew procedures are TBD.

## 11. Safety

Missed, delayed, or misleading propulsion-status presentation is hazardous. Mitigations required (all TBD): defined parameter set (HPS-001), distinct exceedance highlighting (HPS-002), assured data source (HPS-003). No integrity, latency, or legibility claim is made at this revision. Safety-path independence is owned by Chapter 10.11 and Vol 13 analyses (TBD).

## 12. Performance

Intentionally TBD. No parameter count, update rate, latency, legibility distance, luminance, contrast, or accuracy value is stated. Future revisions reference budgets and models, never invented figures.

## 13. Verification & Validation

HPS-004 establishes the thread: each HPS requirement maps to at least one V&V case (method stated in section 6 table). Intended strategy is inspection of interface definitions and demonstration of display behaviour including exceedance highlighting (rigs, scenarios, and pass criteria TBD). No V&V is complete at this revision.

## 14. Risks

- Parameter set and Vol 04.11 source undefined → display requirements unquantifiable; mitigation: explicit TBD with named parents, refined with Vol 04.
- Exceedance criteria undefined without propulsion limits and Vol 13 input; mitigation: highlighting requirement held as TBD placeholder.
- Workload/legibility limits undefined (Vol 30, HUM-001/002); mitigation: constraint interface TBD, evaluation deferred to Chapter 10.14.

## 15. Open Issues

- Propulsion parameter set, arrangement, and update behaviour TBD.
- Exceedance states, highlight means, and criteria TBD.
- Vol 04.11 signals, rates, integrity, and ICD TBD.
- Verification methods, rigs, scenarios, and pass criteria TBD per requirement.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-005 policy stability, STK-002/007 needs, HSA-001 integration view, HUM-001/002 human-factors inputs, Vol 04.11 data-source definition, Vol 30 workload/legibility principles, warning/alert coordination (Chapters 10.11/10.12), and V&V planning.

## 18. Traceability

Parents: STK-002, STK-007, SYS-005, HSA-001, HSA-003, HUM-001, HUM-002; Vol 30 hooks. Children: Vol 10 display design, Vol 04.11 ICD, V&V cases, RTM rows. RTM: REQ-HFPX-HPS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.10, 4 requirements) |
