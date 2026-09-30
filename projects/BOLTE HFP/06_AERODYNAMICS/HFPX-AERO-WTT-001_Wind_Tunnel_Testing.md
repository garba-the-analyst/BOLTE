# Wind-Tunnel Testing

**Document ID:** HFPX-AERO-WTT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define wind-tunnel testing methodology for HFP-X (Chapter 06.20): test objectives, scaling and similarity requirements, data-capture requirements, and the tunnel-to-model correlation rule.
This document owns requirements, methodology, interfaces, and verification discipline only; it contains no test execution instructions.

## 2. Scope

Covers wind-tunnel test objectives (TBD), scaling and similarity requirements (TBD), data-capture requirements (TBD), and the rule correlating tunnel data to the aerodynamic model.
Out of scope: CFD execution (Vol 06.19), aerodynamic database values (TBD), and tunnel or flight-test execution (Vol 23 and facility procedures).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (SYS-001/008)
- HFPX-PGM-SEM-001 SEMP; HFPX-VV-PLN-001 V&V Plan
- Sibling hooks: Vol 06.5 Aerodynamic Drag, Vol 06.6 Lift Characteristics, Vol 06.7 Propulsion-Airframe Interaction, Vol 06.11 model chapter as applicable (values TBD)
- Vol 06.19 CFD methodology (correlation partner); Vol 19 analysis support

## 4. Definitions & Acronyms

- Wind-tunnel test objectives: measurement goals bounding a tunnel campaign; objectives TBD.
- Scaling and similarity: requirements preserving flow-physics relevance between tunnel article and flight article; parameters TBD.
- Data capture: measurement set, conditioning, and recording required from tunnel testing; scope TBD.
- Tunnel-to-model correlation: rule mapping tunnel data with uncertainty into the aerodynamic model; rule TBD.

## 5. System Context

Wind-tunnel testing provides the first measured aerodynamic evidence above CFD screening: objectives bound what each campaign must answer, scaling preserves relevance, data capture preserves usability, and correlation governs how tunnel data enters the model.
No tunnel result is baselined in this revision; all objectives, scaling, capture, and correlation content is TBD.
This document constrains testing methodology and correlation discipline without directing facility conduct or test execution.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-AWT-001 | The system shall define wind-tunnel test objectives, with all objectives TBD. | SYS-001/008 | Inspection |
| REQ-HFPX-AWT-002 | The system shall define scaling and similarity requirements for wind-tunnel testing, with all parameters TBD. | SYS-001/008 | Analysis |
| REQ-HFPX-AWT-003 | The system shall define data-capture requirements for wind-tunnel testing, with scope TBD. | SYS-001/008 | Inspection |
| REQ-HFPX-AWT-004 | The system shall define the tunnel-to-model correlation rule, with rule and uncertainties TBD. | SYS-001/008 | Analysis |

## 7. Architecture

Tunnel methodology architecture (details TBD): objectives register TBD, scaling-requirements record TBD, data-capture record TBD, correlation-rule record TBD.
Campaign-to-objective allocation TBD; facility and article selection TBD.
Record linkage TBD between objectives, scaling records, captured data, correlation records, and fed model tables.

## 8. Detailed Design

Objectives definition is a stub in this revision (objectives TBD, priorities TBD, success criteria TBD).
Scaling and similarity definition is a stub (parameters TBD, allowable distortions TBD, corrections TBD).
Data-capture definition is a stub (measurement set TBD, conditioning TBD, recording TBD, quality flags TBD).
Correlation rule is a stub (mapping TBD, uncertainty treatment TBD, labelling TBD).
No tunnel value, correction, or uncertainty is baselined in this revision.

## 9. Interfaces

- WTT ↔ Aerodynamic consumers (Vol 06.5 / 06.6 / 06.7 / 06.11 as applicable): objective flow-down and table feed; scope TBD.
- WTT ↔ CFD (Vol 06.19): pre-test prediction and post-test correlation partnership; allocation TBD.
- WTT ↔ Analysis (Vol 19): scaling assessment and correlation analysis support; methods TBD.
- WTT ↔ Test execution (Vol 23) and facilities: gated handover of objectives, scaling, and capture requirements; conduct excluded here.

## 10. Operational Concept

Tunnel concept (test-methodology only): state objectives (objectives TBD) → state scaling and similarity requirements (parameters TBD) → state data-capture requirements (scope TBD) → correlate to model per rule TBD with uncertainty TBD.
This concept defines methodology and evidence flow only; it contains no facility instructions, run conduct, or test execution instructions (execution owned and gated under Vol 23 and facility control).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, methodology, interfaces, and verification discipline only; it contains no propulsion build, ignition, or operation instructions.
No model table fed by tunnel data shall be used beyond its correlated uncertainty; use beyond uncertainty is prohibited pending further evidence (criteria TBD).
Tunnel-article hazards and facility safety are owned by the facility and Vol 23 (scope TBD).

## 12. Performance

Tunnel-methodology performance measures TBD with no thresholds baselined: objective coverage TBD, scaling compliance TBD, capture completeness TBD, correlation-uncertainty magnitudes TBD.
No numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-AWT-001 verified by Inspection of wind-tunnel test objectives (completeness criteria TBD).
- REQ-HFPX-AWT-002 verified by Analysis of scaling and similarity requirements against flight relevance (parameters and criteria TBD).
- REQ-HFPX-AWT-003 verified by Inspection of data-capture requirements against objectives and correlation needs (criteria TBD).
- REQ-HFPX-AWT-004 verified by Analysis of tunnel-to-model correlation records with uncertainty treatment (rule and criteria TBD).
- Validation is gate review of tunnel-methodology adequacy for its claimed model feeds (scope TBD).

## 14. Risks

- Objectives left TBD, producing unfocused campaigns; mitigation: objectives register gated before campaign commitment (criteria TBD).
- Scaling distortions unaddressed, breaking flight relevance; mitigation: scaling-requirements review with corrections TBD.
- Correlation without uncertainty, overstating model standing; mitigation: mandatory uncertainty labelling per feed (rule TBD).

## 15. Open Issues

Test objectives, priorities, and success criteria TBD. Scaling parameters, allowable distortions, and corrections TBD. Measurement set, conditioning, recording, and quality flags TBD. Correlation rule, uncertainty treatment, and labelling TBD. Facility and article selection TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-001/008, sibling aerodynamic chapters (objective sources and table consumers), Vol 06.19 (CFD correlation partner), Vol 19 (analysis support), SEMP / V&V Plan (gates and discipline), Vol 23 and facilities (test execution).

## 18. Traceability

Parents: SYS-001/008. Children: objectives register, scaling-requirements records, data-capture records, correlation records, and fed-table records (artefact IDs TBD).
RTM: REQ-HFPX-AWT-001..004 → CONCEPT. Each objective traces to at least one scaling record and at least one capture element; each fed table traces to at least one correlation record with uncertainty TBD (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Objectives, scaling, capture, and correlation content is under document control once populated; changes via change records with affected-table impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (wind-tunnel testing; Ch 06.20) |
