# Warning System

**Document ID:** HFPX-HMI-WRN-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the helmet warning-system requirements for HFP-X (Chapter 10.11): warning/caution/advisory hierarchy, prioritisation and suppression behaviour, and independence of the safety path. No priority table, timing value, symbology, or suppression rule is defined in this document.

## 2. Scope

Covers helmet warning presentation allocated from SYS-005 and STK-007, including hierarchy definition, prioritisation/suppression, and safety-path independence. Excludes propulsion parameter presentation (Chapter 10.10), alert inventory and acknowledgement detail (Chapter 10.12), voice-interface behaviour (Chapter 10.13), and communications/power implementation (Chapters 10.15/10.16). All hierarchies, rules, latencies, and integrity provisions are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-002 controllability, STK-007 status/warning guidance)
- HFPX-ARC-HUM-001 Human-System Architecture (REQ-HFPX-HSA-001 alert integration, REQ-HFPX-HSA-003 workload principles)
- HFPX-SYS-HUM-001 Human Factors Requirements (REQ-HFPX-HUM-001 workload, REQ-HFPX-HUM-002 legibility)
- Vol 13 safety analyses (FHA/FMEA/FTA inputs TBD)
- Vol 30 human-factors principles (limits and methods TBD)

## 4. Definitions & Acronyms

- HWS: warning-system requirement tier; ID prefix `REQ-HFPX-HWS-NNN`
- Warning/caution/advisory: hierarchical alert classes (definitions and entry criteria TBD)
- Prioritisation/suppression: ordering and inhibiting of concurrent warnings (rules TBD)
- Safety-path independence: separation of the warning path serving the independent safety path from the primary presentation path (means TBD)
- TBD: to be defined. No values stated.

## 5. System Context

The helmet warning system sits between fault/health sources (including the independent safety path) and the pilot presentation surface. It applies hierarchy, prioritisation, and suppression rules (all TBD) and presents warnings within workload and legibility constraints (HUM-001/002, Vol 30). It coordinates with propulsion-status display (Chapter 10.10) and pilot-alert handling (Chapter 10.12).

```text
[Health/fault sources + safety path (TBD)] --> [Hierarchy + prioritisation/suppression (TBD)] --> [Helmet warning presentation (TBD)]
   constrained by [HUM-001/002 workload/legibility (TBD, Vol 30)] | fed by [10.10 exceedance flags (TBD)] | coordinated with [10.12 alerts (TBD)]
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HWS-001 | The helmet warning system shall implement a defined warning/caution/advisory hierarchy (classes, entry criteria, and presentation distinctions TBD). | STK-007, SYS-005, HSA-001 | Demonstration (fault-injection, TBD) |
| REQ-HFPX-HWS-002 | The helmet warning system shall apply defined prioritisation and suppression rules to concurrent warnings (rules, inhibits, and ordering TBD). | STK-002, SYS-005, HUM-001 | Demonstration (fault-injection, TBD) |
| REQ-HFPX-HWS-003 | Warnings serving the independent safety path shall be independent of the primary presentation path by defined means (means and integrity provisions TBD). | SYS-005, HSA-001 | Analysis + Demonstration (fault-injection, TBD) |
| REQ-HFPX-HWS-004 | Each warning-system requirement in this document shall be verified by defined fault-injection demonstration cases with defined pass criteria (cases and criteria TBD). | SYS-005 | Demonstration (fault-injection, TBD) |

No hierarchy definition, priority rule, suppression rule, latency, or integrity value in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: HWS-001 → hierarchy function; HWS-002 → prioritisation/suppression function; HWS-003 → independence provision; HWS-004 → fault-injection V&V thread. Authoritative allocation lives in Vol 10 integration views; this section states derivation intent only. Logic, state machines, and redundancy implementations are TBD.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Hierarchy tables, rule sets, state transitions, symbology, tones, and independence mechanisms are TBD.

## 9. Interfaces

- Health/fault source interface (including safety-path inputs): signals and integrity TBD.
- Propulsion-status coordination interface (Chapter 10.10): TBD.
- Pilot-alert coordination interface (Chapter 10.12): TBD.
- Presentation interface (visual/audio rendering pipeline): TBD.
- Formal ICDs are TBD.

## 10. Operational Concept

Requirements are exercised through single-warning threads and concurrent-warning threads (prioritisation/suppression), plus safety-path warning threads asserting independence, under controlled conditions. Scenario definitions, injection points, and crew responses are TBD.

## 11. Safety

Missed, masked, delayed, or mis-prioritised warnings are hazardous. Mitigations required (all TBD): defined hierarchy (HWS-001), defined prioritisation/suppression (HWS-002), safety-path independence (HWS-003), fault-injection verification (HWS-004). No safety or integrity claim is made at this revision. FHA-derived constraints feed this document by change record (Vol 13, TBD).

## 12. Performance

Intentionally TBD. No warning count, latency, display persistence, tone level, or suppression timing value is stated. Future revisions reference budgets and models, never invented figures.

## 13. Verification & Validation

HWS-004 establishes the thread: each HWS requirement maps to at least one fault-injection demonstration case (methods, rigs, injection points, and pass criteria TBD). Intended strategy is analysis of hierarchy/suppression logic plus demonstration by fault injection on representative presentation rigs. No V&V is complete at this revision.

## 14. Risks

- Hierarchy and FHA inputs undefined → warning classes ungrounded; mitigation: placeholder requirements with Vol 13 dependency explicit.
- Prioritisation/suppression rules undefined → masking/overload risk unretired; mitigation: fault-injection verification thread held as TBD.
- Independence means undefined without safety-computer allocation; mitigation: independence requirement held as TBD provision.

## 15. Open Issues

- Warning/caution/advisory classes, criteria, and distinctions TBD.
- Prioritisation/suppression rules, inhibits, and ordering TBD.
- Safety-path independence means and integrity provisions TBD.
- Fault-injection cases, rigs, and pass criteria TBD per requirement.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-005 policy stability, STK-002/007 needs, HSA-001 integration view, HUM-001/002 human-factors inputs, Vol 13 FHA/FMEA/FTA outputs, Vol 30 workload/legibility principles, coordination with Chapters 10.10/10.12, and V&V planning.

## 18. Traceability

Parents: STK-002, STK-007, SYS-005, HSA-001, HSA-003, HUM-001, HUM-002; Vol 30 hooks. Children: Vol 10 warning design, suppression logic, independence provisions, V&V fault-injection cases, RTM rows. RTM: REQ-HFPX-HWS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.11, 4 requirements) |
