# Adaptive Impact Protection

**Document ID:** HFPX-SAFE-AIP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define adaptive impact-protection requirements (Vol 13.12): impact-attenuation functions, deployment/activation criteria, suit/airframe interface needs, and analysis-plus-component-test verification methodology.
This document owns requirements, architecture, interfaces, and test methodology only.

## 2. Scope

Covers attenuation-function definition (zones TBD), activation criteria (thresholds TBD), suit/airframe interface hooks (Vol 12), and verification by analysis plus component test (methods TBD).
Hover/low-altitude is the limiting case for impact-energy claims (quantification TBD).
Out of scope: suit detailed design (Vol 12), airframe detailed design (Vol 03), recovery hardware (Vol 13.11), and test execution (Vol 23).

## 3. Applicable Documents

- SYS-003 (system basis — stub, values TBD); REC tier hooks as applicable (values TBD)
- Vol 12 suit/airframe interface context (mating definitions TBD)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13.2–13.7 hazard hooks (impact cases, values TBD)
- HFPX-VV-PLN-001 V&V Plan; HFPX-PGM-SEM-001 SEMP (gating)

## 4. Definitions & Acronyms

- Adaptive impact protection: attenuation function that changes state to reduce impact loading; adaptivity mechanism TBD.
- Attenuation zone: body/airframe region to which protection applies; zones TBD.
- Deployment/activation criteria: conditions for protection to arm, deploy, or stiffen/soften; thresholds, latencies, and sensing TBD.
- Suit/airframe interface: mechanical/functional coupling between worn protection and vehicle structure; loads and protocols TBD (Vol 12).
- Component test: subassembly-level impact/actuation testing supporting verification; methods and pass criteria TBD.

## 5. System Context

Adaptive impact protection is the impact-attenuation branch downstream of recovery: it assumes a residual impact vector TBD and bounds transmitted loading to TBD levels (both uncredited here).
It constrains suit and airframe mating without designing either; allocation flows via SAD.
Recovery effectiveness is unproven (ISS-008); impact protection claims no injury-reduction outcome in this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-AIP-001 | The system shall provide impact-attenuation functions, with zones and adaptivity TBD. | SYS-003 | Analysis |
| REQ-HFPX-AIP-002 | The system shall define deployment/activation criteria for impact protection, with all thresholds, latencies, and sensing TBD. | SYS-003 | Analysis |
| REQ-HFPX-AIP-003 | The system shall define the suit/airframe interface for impact protection, with loads, couplings, and protocols TBD (Vol 12). | SYS-003 | Inspection |
| REQ-HFPX-AIP-004 | Impact protection shall be verified by analysis plus component test, with methods and pass criteria TBD. | SYS-003 | Test |

## 7. Architecture

Protection architecture (details TBD): sensing/activation path TBD, attenuation elements TBD, zone allocation TBD, annunciation TBD.
Adaptivity TBD: what adapts (stiffness, geometry, damping, or TBD), on what input, with what authority and failure behaviour TBD.
Segregation TBD: separation of activation path from primary systems where credited for safety (SAD to allocate).

## 8. Detailed Design

Attenuation functions are stubs in this revision (zones TBD, mechanisms unselected, no loads or strokes baselined).
Methodology only: impact case → attenuation demand → activation criterion → interface load → analysis/component-test evidence; completeness criteria TBD.
No material, geometry, sizing, or actuation decisions are made in this revision.

## 9. Interfaces

- AIP ↔ Suit (Vol 12): worn-element mating, loads, and donning/doffing hooks TBD.
- AIP ↔ Airframe (Vol 03/12): mounted-element fixings, load paths, and volume allocation TBD.
- AIP ↔ Trigger/sensing: activation inputs and signal integrity TBD.
- AIP ↔ Recovery (Vol 13.11): residual-impact assumptions feeding attenuation demand; values TBD, no credit claimed.
- AIP ↔ Procedures/alerts (Vol 13.8, Vol 10): activation annunciation and crew/operator actions TBD.

## 10. Operational Concept

Protection sequence (methodology only): arm (criteria TBD) → activate/deploy on qualifying condition (criteria TBD) → attenuate residual impact (effectiveness TBD) → safing/inspection (methods TBD).
This concept defines activation allocation and verification needs only; it does not direct vehicle handling or flight conduct (owned and gated under Vol 23/CONOPS).
Hover-first emphasis: hover/low-altitude impact cases are analysed first (scope TBD).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, architecture, interfaces, and test methodology only; it contains no build, ignition, or operation instructions for high-energy subsystems.
Inadvertent-activation and failed-activation hazards are in scope as analysis hooks (Vol 13.4/13.5); mitigations and verification TBD.
Recovery effectiveness is unproven (ISS-008): impact protection asserts no injury-reduction or survival outcome until verified per REQ-HFPX-AIP-004 (criteria TBD).
Hover/low-altitude is the limiting case for impact-validation claims.

## 12. Performance

Impact-protection performance measures TBD with no thresholds baselined: transmitted-load reduction TBD, stroke/energy capacity TBD, activation latency TBD, zone coverage TBD.
All loads, energies, timings, and coverage values TBD; no numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-AIP-001 verified by Analysis of attenuation-function coverage against impact cases (criteria TBD).
- REQ-HFPX-AIP-002 verified by Analysis of activation criteria, supported by sim where applicable (coverage TBD).
- REQ-HFPX-AIP-003 verified by Inspection of the suit/airframe interface definition (criteria TBD).
- REQ-HFPX-AIP-004 verified by Test (analysis plus component test; methods, fixtures, and pass criteria TBD); human-flight credit gated on closure (criteria TBD).
- Validation is gate review plus Safety Review Board concurrence (scope TBD).

## 14. Risks

- Attenuation-demand mismatch: residual impact assumed differs from recovery-delivered conditions TBD; mitigation: joint assumption review with Vol 13.11, values TBD.
- Inadvertent or failed activation; mitigation: activation-hazard analysis plus component-test methodology, scope TBD.
- Unproven effectiveness treated as protection (ISS-008); mitigation: explicit unproven status and gated-verification requirement enforced at reviews.

## 15. Open Issues

Attenuation zones and mechanisms TBD. Activation thresholds, latencies, and sensing TBD. Suit/airframe loads, couplings, and protocols TBD (Vol 12). Analysis methods TBD. Component-test methods, fixtures, and pass criteria TBD. Human-flight gating criteria TBD. ISS-008 applies to all impact-effectiveness claims.

## 16. Assumptions

- A-AIP-001: Attenuation functions can be accommodated within suit/airframe mass/volume budgets TBD; validation: Vol 03/12 allocation review (TBD).
- A-AIP-002: Hover/low-altitude impact cases bound attenuation design for early flight; validation: Vol 13 analysis and Vol 19 modelling (both TBD).
- A-AIP-003: Analysis plus component test adequately predict system-level attenuation for verification purposes; validation: Vol 23 test adequacy review (TBD).

## 17. Dependencies

Depends on SYS-003 (requirements basis), Vol 12 (suit interface), Vol 03 (airframe integration), Vol 13.11 (residual-impact assumptions), Vol 13.1–13.7 (hazard hooks), Vol 19 (modelling), SEMP/V&V Plan (gates/discipline), Vol 23 (test execution).

## 18. Traceability

Parents: SYS-003. Children: attenuation functions, activation criteria, interface definitions, and analysis/component-test cases (artefact IDs TBD).
RTM: REQ-HFPX-AIP-001..004 → CONCEPT. Each attenuation zone traces to at least one impact case and at least one verification case (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Attenuation and activation definitions are under document control once populated; changes via change records with affected-zone impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (adaptive impact protection; Ch 13.12) |
