# Aerodynamic Model

**Document ID:** HFPX-SIM-AER-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the aerodynamic model structure and discipline (Chapter 19.4): table structure, data-source hierarchy, interpolation and extrapolation rules, update-on-evidence rule, and feed to the 6-DOF simulation (19.3). This document defines structures with TBD values; no capability or feasibility claim rests on any unverified model in this revision.

## 2. Scope

Covers lift, drag, and moment table structures versus defined states, the estimate-to-CFD-to-tunnel-to-flight source hierarchy with per-source uncertainty, interpolation/extrapolation discipline, and the evidence-driven update process. Excludes 6-DOF integration (19.3), propulsion and environment contributions (19.5, 19.14), and verification execution (Vol 22/23).

## 3. Applicable Documents

- HFPX-VV-PLN-001 V&V Plan (notably REQ-HFPX-VVP-001, REQ-HFPX-VVP-004)
- HFPX-SYS-REQ-001 SyRS (notably SYS-001, SYS-008)
- HFPX-SIM-STR-001 Digital Engineering Strategy
- HFPX-SIM-SIX-001 6-DOF Simulation (consumer of this model)
- ISS-006 action (evidence-driven modelling; details TBD), ISS-007 action (budget interfaces; details TBD)

## 4. Definitions & Acronyms

- Aerodynamic tables: lift, drag, and moment tabulations versus defined states; states defined TBD, values TBD.
- Data-source hierarchy: ordered sources estimate, CFD, tunnel, flight; uncertainty recorded TBD per source.
- Interpolation/extrapolation rules: permitted treatments between and beyond table entries; rules TBD.
- TBD: to be defined; TBC: to be confirmed.

## 5. System Context

The aerodynamic model supplies lift, drag, and moment data to the 6-DOF simulation (19.3) under the 19.1 hierarchy. Source fidelity ascends from estimate through CFD and tunnel to flight, with uncertainty recorded TBD at each level. Table outputs are consumed only as TBD-valued structures in this revision and gain gate authority solely through verification via 19.15 hooks.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-MAM-001 | The aerodynamic model shall define lift, drag, and moment table structures versus defined states, with states defined TBD and table values recorded as TBD. | SYS-008; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MAM-002 | The programme shall apply an aerodynamic data-source hierarchy of estimate, CFD, tunnel, and flight, with uncertainty recorded as TBD per source. | VVP-001; ISS-006; SYS-001 | Inspection |
| REQ-HFPX-MAM-003 | The programme shall define aerodynamic interpolation and extrapolation rules, with rules recorded as TBD. | VVP-001; ASX tier; ISS-006 | Analysis |
| REQ-HFPX-MAM-004 | The programme shall apply an update-on-evidence rule requiring aerodynamic tables and uncertainties to be revised when higher-fidelity evidence becomes available, with revision records TBD. | VVP-004; ISS-006; SYS-008 | Inspection |
| REQ-HFPX-MAM-005 | The aerodynamic model shall feed the 6-DOF simulation (19.3) as its TBD-valued table consumer, with interface and feed status TBD, such that no capability or feasibility claim rests on unverified aerodynamic data. | SYS-001; VVP-004; ISS-006 | Analysis |

## 7. Architecture

Aerodynamic model architecture (structure only): table layer (REQ-HFPX-MAM-001); source-hierarchy layer (REQ-HFPX-MAM-002) annotating each table entry with source and uncertainty TBD; interpolation/extrapolation layer (REQ-HFPX-MAM-003) governing intermediate and out-of-range queries; update layer (REQ-HFPX-MAM-004) driving revisions; feed layer (REQ-HFPX-MAM-005) exporting to 19.3. Table extents and formats TBD.

## 8. Detailed Design

Table-structure record TBD per coefficient family (lift TBD, drag TBD, moment TBD): state-axis definitions TBD, entry format TBD, values TBD throughout. Source-hierarchy record TBD per entry: source designation TBD (estimate/CFD/tunnel/flight), uncertainty TBD per source, pedigree reference TBD. Interpolation/extrapolation record TBD: permitted methods TBD, boundary handling TBD, prohibited regions TBD. Update record TBD: evidence-acceptance criteria TBD, revision trigger TBD, supersession handling TBD. Feed record TBD: interface format TBD, configuration reference TBD, status TBD.

## 9. Interfaces

- Aerodynamic model ↔ source activities (estimate/CFD/tunnel/flight): evidence ingested per hierarchy (pedigree TBD).
- Aerodynamic model ↔ 19.3 6-DOF: tables supplied as TBD-valued consumer feed (format TBD).
- Aerodynamic model ↔ 19.1 strategy: registration, ownership, and gate authority (assignments TBD).
- Aerodynamic model ↔ 19.15 Model Verification: table, source-hierarchy, and interpolation verification methodology and status.

## 10. Operational Concept

Operates evidence-driven: declare table structures TBD → populate from lowest available source TBD → annotate uncertainty TBD → govern queries by interpolation/extrapolation rules TBD → revise on higher-fidelity evidence TBD → export to 19.3 TBD → submit for verification per 19.15 before any gate use. No table is offered as performance evidence until verified. Cadence TBD.

## 11. Safety

No safety-related claim (including handling, margin, or departure behaviour) is made from aerodynamic tables until verification per 19.15 with independence per VVP-006 (degree TBD). Safety-significant states and uncertainty-treatment for safety analyses are TBD (Vol 13/24 mapping TBD).

## 12. Performance

Aerodynamic model performance indicators TBD (no thresholds baselined): table-definition completeness TBD, source-hierarchy population TBD, interpolation-rule definition status TBD, update-record currency TBD, verification closure TBD. Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against template, header, and requirement discipline. REQ-HFPX-MAM-001..005 are verified by their stated methods applied to the table, hierarchy, interpolation, update, and feed records. Verification methodology for the model is owned by 19.15; execution evidence is owned by Vol 22/23. Validation is programme-authority approval at a gated review (review TBD).

## 14. Risks

- Tables populated with placeholder values later mistaken for data; mitigation: REQ-HFPX-MAM-001 TBD-value rule with source annotation per REQ-HFPX-MAM-002.
- Extrapolation beyond table extents cited as performance; mitigation: REQ-HFPX-MAM-003 explicit rules (rules TBD, default posture TBD).
- Stale low-fidelity tables retained after better evidence arrives (ISS-006 risk); mitigation: REQ-HFPX-MAM-004 update-on-evidence rule with revision records TBD.

## 15. Open Issues

State-axis definitions TBD; table values TBD throughout. Per-source uncertainty TBD. Interpolation and extrapolation rules TBD. Update triggers and revision records TBD. Feed interface and verification status TBD via 19.15.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on state-axis definitions (TBD), source evidence from estimate/CFD/tunnel/flight activities (TBD), 19.3 6-DOF consumer interface (TBD), 19.1 authority rule, 19.15 verification methodology, ISS-006 evidence scope, and Vol 22/23 execution.

## 18. Traceability

Parents: VVP-001, VVP-004; SYS-001, SYS-008; ASX tier (details TBD); ISS-006, ISS-007 actions. Children: table records, source-hierarchy records, interpolation records, update records, verification cases (IDs TBD; rows TBD). RTM: REQ-HFPX-MAM-001..005 → CONCEPT. No capability or feasibility claim in this document rests on an unverified model; authority for any such future claim routes via 19.15.

## 19. Configuration

BL-0.0. Tranche 5 draft, CONCEPT, not baselined. Future changes via change records; any change re-validates affected traceability before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (19.4 aerodynamic structure; requirements REQ-HFPX-MAM-001..005) |
