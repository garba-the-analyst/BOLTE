# Computational Fluid Dynamics

**Document ID:** HFPX-AERO-CFD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define computational fluid dynamics methodology for HFP-X (Chapter 06.19): CFD scope, mesh and solution verification practice, CFD-to-model feed rules, and CFD limits.
This document owns requirements, methodology, interfaces, and verification discipline only; it contains no test execution instructions.

## 2. Scope

Covers CFD scope for concept screening and interaction flows per Vol 06.7 (cases TBD), mesh and solution verification practice with Vol 19.15 hooks (practice TBD), rules for which aerodynamic tables CFD may populate with uncertainties TBD, and the limits statement for CFD use.
Out of scope: aerodynamic database values (TBD), wind-tunnel execution (Vol 06.20), and flight-test execution (Vol 23).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001/008)
- HFPX-PGM-SEM-001 SEMP; HFPX-VV-PLN-001 V&V Plan
- Sibling hooks: Vol 06.7 Propulsion-Airframe Interaction; Vol 19.15 analysis verification hooks (details TBD)
- Vol 06.20 wind-tunnel methodology (correlation partner; execution excluded here)

## 4. Definitions & Acronyms

- CFD: computational fluid dynamics analysis of aerodynamic flows and interaction effects; tools and versions TBD.
- Concept screening: comparative CFD use to rank concepts without claiming database accuracy; coverage TBD.
- Interaction flows: propulsion-airframe coupled flows per Vol 06.7; cases TBD.
- Mesh and solution verification: demonstration that discretisation and convergence support the claimed use; practice and criteria TBD.
- CFD-to-model feed: rule governing which aerodynamic tables CFD may populate and with what uncertainty; rule TBD.
- CFD limits: bounds on what CFD shall not claim, including non-substitution for test; statement TBD.

## 5. System Context

CFD supports early aerodynamic understanding and interaction-flow assessment before measured data exists: it screens concepts and informs models within stated uncertainty, but never substitutes for test evidence.
No database value derived from CFD is baselined in this revision; all tables, uncertainties, and limits are TBD.
This document constrains CFD methodology and feed discipline without directing analysis execution or test conduct.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-ACD-001 | The system shall define the CFD scope covering concept screening and interaction flows per Vol 06.7, with cases TBD. | SYS-001/008 | Inspection |
| REQ-HFPX-ACD-002 | CFD mesh and solution verification practice shall be defined with Vol 19.15 hooks, with practice and criteria TBD. | SYS-001/008 | Analysis |
| REQ-HFPX-ACD-003 | The system shall define the CFD-to-model feed rule stating which tables CFD may populate and with what uncertainty, with rule and uncertainties TBD. | SYS-001/008 | Inspection |
| REQ-HFPX-ACD-004 | The system shall state CFD limits, including that CFD is not a substitute for test, with limit statement TBD. | SYS-001/008 | Inspection |

## 7. Architecture

CFD methodology architecture (details TBD): scope register TBD, verification-practice record TBD, feed-rule record TBD, limits statement TBD.
Toolchain identification TBD (tools, versions, custodianship TBD).
Record linkage TBD between CFD cases, verification records, fed tables, and uncertainties.

## 8. Detailed Design

Scope definition is a stub in this revision (screening cases TBD, interaction-flow cases TBD per Vol 06.7).
Mesh and solution verification practice is a stub (refinement practice TBD, convergence practice TBD, acceptance TBD; Vol 19.15 hooks TBD).
Feed rule is a stub (permitted tables TBD, uncertainty treatment TBD, labelling TBD).
Limits statement is a stub (scope TBD, non-substitution clause TBD).
No mesh metric, convergence value, table value, or uncertainty is baselined in this revision.

## 9. Interfaces

- CFD ↔ Interaction flows (Vol 06.7): case definitions and flow conditions; scope TBD.
- CFD ↔ Analysis verification (Vol 19.15): mesh and solution verification practice hooks; methods TBD.
- CFD ↔ Aerodynamic model and database (Vol 06.11 and siblings as applicable): fed tables and uncertainty labels; rule TBD.
- CFD ↔ Wind tunnel (Vol 06.20): correlation partnership and evidence hierarchy; allocation TBD.

## 10. Operational Concept

CFD concept (test-methodology only): register in-scope cases (cases TBD) → apply mesh and solution verification practice (practice TBD) → feed permitted tables with stated uncertainty (rule TBD) → observe limits including non-substitution for test.
This concept defines methodology and evidence flow only; it contains no analysis execution instructions and no test execution instructions (execution owned under Vol 19 and Vol 23 respectively, gated per SEMP).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, methodology, interfaces, and verification discipline only; it contains no propulsion build, ignition, or operation instructions.
No design decision shall rely on CFD beyond its stated uncertainty and limits; reliance beyond limits is prohibited pending test evidence (criteria TBD).
CFD-derived inputs to safety threads are labelled with uncertainty TBD and independently reviewed (scope TBD).

## 12. Performance

CFD performance measures TBD with no thresholds baselined: case coverage TBD, verification-practice compliance TBD, feed-rule compliance TBD, uncertainty magnitudes TBD.
No numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-ACD-001 verified by Inspection of the CFD scope definition against Vol 06.7 interaction-flow needs (completeness criteria TBD).
- REQ-HFPX-ACD-002 verified by Analysis of mesh and solution verification records against Vol 19.15 practice (criteria TBD).
- REQ-HFPX-ACD-003 verified by Inspection of fed tables against the feed rule and uncertainty labelling (criteria TBD).
- REQ-HFPX-ACD-004 verified by Inspection of the limits statement including the non-substitution clause (criteria TBD).
- Validation is gate review of CFD methodology adequacy for its claimed uses (scope TBD).

## 14. Risks

- CFD scope creep into database claims without verification; mitigation: feed rule enforced at reviews (criteria TBD).
- Mesh and solution verification left TBD, leaving CFD evidence without standing; mitigation: Vol 19.15 hook coverage review (scope TBD).
- CFD treated as test substitute; mitigation: explicit limits statement with non-substitution clause enforced at gates.

## 15. Open Issues

CFD cases for screening and interaction flows TBD. Mesh and solution verification practice and criteria TBD. Permitted tables, uncertainty treatment, and labelling TBD. Limits statement TBD. Toolchain, versions, and custodianship TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001/008, Vol 06.7 (interaction-flow scope), Vol 19.15 (analysis verification practice), sibling aerodynamic chapters (table consumers), SEMP / V&V Plan (gates and discipline), Vol 06.20 (correlation partner), Vol 23 (test evidence hierarchy).

## 18. Traceability

Parents: SYS-001/008. Children: CFD scope register, verification-practice records, fed-table records with uncertainties, and limits statement (artefact IDs TBD).
RTM: REQ-HFPX-ACD-001..004 → CONCEPT. Each in-scope case traces to at least one verification record; each fed table traces to at least one verification record with uncertainty TBD (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. CFD scope, verification-practice, feed-rule, and limits content is under document control once populated; changes via change records with affected-table impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (computational fluid dynamics; Ch 06.19) |
