# Inflatable Protection System

**Document ID:** HFPX-SAFE-IPS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define inflatable-protection-system requirements (Vol 13.13): inflation functions and coverage, trigger criteria, inadvertent-deployment protection, and storage/inspection/maintenance hooks.
This document owns requirements, architecture, interfaces, and test methodology only.

## 2. Scope

Covers inflation-function definition and coverage (both TBD), trigger criteria (thresholds TBD), inadvertent-deployment safeguards (methods TBD), and storage/inspection/maintenance hooks (Vol 27).
Hover/low-altitude is the limiting case for deployment-timing claims (quantification TBD).
Out of scope: inflatable detailed design/materials, gas-generation implementation, suit/airframe integration design (Vol 12/03), and test execution (Vol 23).

## 3. Applicable Documents

- SYS-003 (system basis — stub, values TBD); REC tier hooks as applicable (values TBD)
- Vol 12/03 integration context (mating and volume definitions TBD); Vol 27 sustainment context (maintenance framework TBD)
- HFPX-SAFE-CAS-001 Safety Case; Vol 13.2–13.7 hazard hooks (deployment hazards, values TBD)
- HFPX-VV-PLN-001 V&V Plan; HFPX-PGM-SEM-001 SEMP (gating)

## 4. Definitions & Acronyms

- Inflatable protection system: gas-deployed attenuation/barrier function; inflation medium and mechanism TBD, unselected.
- Coverage: body/airframe regions shielded when inflated; zones TBD.
- Trigger criteria: conditions for inflation command; thresholds, latencies, and sensing TBD.
- Inadvertent-deployment protection: interlocks/safeguards against uncommanded inflation; methods TBD.
- Storage/inspection/maintenance hooks: shelf-life, packing, inspection-interval, and servicing needs feeding Vol 27; values TBD.

## 5. System Context

Inflatable protection is a deployable attenuation branch: trigger → inflate → interpose protection → sustain through impact (each effectiveness TBD).
It constrains integration and sustainment volumes without designing hardware; allocation flows via SAD and Vol 27.
Recovery effectiveness is unproven (ISS-008); inflatable protection claims no injury-reduction outcome in this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-IPS-001 | The system shall provide inflation functions with coverage TBD, with medium, geometry, and mechanism unselected in this revision. | SYS-003 | Inspection |
| REQ-HFPX-IPS-002 | The system shall define trigger criteria for inflation, with all thresholds, latencies, and sensing TBD. | SYS-003 | Analysis |
| REQ-HFPX-IPS-003 | The system shall provide inadvertent-deployment protection, with interlocks, safeguards, and verification methods TBD. | SYS-003 | Analysis |
| REQ-HFPX-IPS-004 | The system shall define storage, inspection, and maintenance hooks for inflatables, with intervals, methods, and criteria TBD (Vol 27). | SYS-003 | Inspection |

## 7. Architecture

Inflatable architecture (details TBD, mechanism unselected): trigger/decision function TBD, inflation chain TBD, restraint/venting TBD, safing path TBD.
Segregation TBD: separation of trigger/inflation path from primary systems where credited for safety (SAD to allocate).
Sustainment hooks TBD: packed state, shelf-life management, and field-inspection access feed Vol 27 definitions.

## 8. Detailed Design

Inflation functions are stubs in this revision (coverage TBD, pressures/volumes TBD, no timelines baselined).
Methodology only: coverage demand → trigger criterion → inflation performance TBD → inadvertent-deployment safeguard → sustainment demand; completeness criteria TBD.
No medium, material, geometry, or gas-generation decisions are made in this revision.

## 9. Interfaces

- IPS ↔ Trigger/sensing: inflation-command inputs and signal integrity TBD.
- IPS ↔ Airframe/suit (Vol 03/12): mounting, volume allocation, and load paths TBD.
- IPS ↔ Recovery/impact volumes (Vol 13.11/13.12): sequencing and residual-impact assumptions TBD, no credit claimed.
- IPS ↔ Sustainment (Vol 27): storage, inspection, and maintenance data and access needs TBD.
- IPS ↔ Procedures/alerts (Vol 13.8, Vol 10): deployment annunciation and crew/operator actions TBD.

## 10. Operational Concept

Inflatable sequence (methodology only): stow/inspect per Vol 27 hooks TBD → arm (criteria TBD) → trigger on qualifying condition (criteria TBD) → inflate and sustain through impact (performance TBD) → safing/repack (methods TBD).
This concept defines trigger allocation and sustainment hooks only; it does not direct vehicle handling, deployment execution, or flight conduct (owned and gated under Vol 23/CONOPS).
Hover-first emphasis: hover/low-altitude deployment cases are analysed first (scope TBD).

## 11. Safety

Hazardous-subsystem boundary: this document contains requirements, architecture, interfaces, and test methodology only; it contains no build, ignition, or operation instructions for high-energy or gas-generation subsystems.
Inadvertent-deployment and failed-deployment hazards are in scope as analysis hooks (Vol 13.4/13.5); mitigations per REQ-HFPX-IPS-003 with methods TBD.
Recovery effectiveness is unproven (ISS-008): inflatable protection asserts no injury-reduction or survival outcome until verified through gated analysis and test (criteria TBD).
Hover/low-altitude is the limiting case for deployment-validation claims.

## 12. Performance

Inflatable performance measures TBD with no thresholds baselined: inflation latency TBD, inflated coverage TBD, sustain duration TBD, storage life TBD.
All timings, pressures, volumes, and life values TBD; no numerical performance requirement is set in this revision.

## 13. Verification & Validation

- REQ-HFPX-IPS-001 verified by Inspection of the inflation-function and coverage definition (stub accepted at CONCEPT).
- REQ-HFPX-IPS-002 verified by Analysis of trigger criteria, supported by sim where applicable (coverage TBD).
- REQ-HFPX-IPS-003 verified by Analysis of inadvertent-deployment safeguards, supported by test methodology TBD.
- REQ-HFPX-IPS-004 verified by Inspection of storage/inspection/maintenance hooks against Vol 27 framework (criteria TBD).
- Validation is gate review plus Safety Review Board concurrence (scope TBD); human-flight credit gated on closure (criteria TBD).

## 14. Risks

- Deployment-timing shortfall in the hover/low-altitude limiting case; mitigation: timing analysis with bounds TBD, no credit claimed.
- Inadvertent deployment causing hazard; mitigation: safeguard analysis per REQ-HFPX-IPS-003, methods TBD.
- Degraded readiness from storage/packing life exceedance; mitigation: Vol 27 inspection/maintenance hooks, intervals TBD.
- Unproven effectiveness treated as protection (ISS-008); mitigation: explicit unproven status enforced at every gate.

## 15. Open Issues

Inflation medium, geometry, mechanism, and coverage TBD. Trigger thresholds, latencies, and sensing TBD. Inadvertent-deployment safeguards and verification methods TBD. Storage life, inspection intervals, and maintenance methods/criteria TBD (Vol 27). Human-flight gating criteria TBD. ISS-008 applies to all inflatable-effectiveness claims.

## 16. Assumptions

- A-IPS-001: An inflatable solution is feasible within mass/volume/complexity budgets TBD; validation: SAD allocation review (TBD).
- A-IPS-002: Hover/low-altitude deployment cases bound inflatable design for early flight; validation: Vol 13 analysis and Vol 19 modelling (both TBD).
- A-IPS-003: A Vol 27 sustainment framework will exist to own packed-life and inspection execution; validation: Vol 27 definition maturity (TBD).

## 17. Dependencies

Depends on SYS-003 (requirements basis), Vol 03/12 (integration), Vol 13.11/13.12 (recovery/impact sequencing), Vol 27 (sustainment), Vol 13.1–13.7 (hazard hooks), Vol 19 (modelling), SEMP/V&V Plan (gates/discipline), Vol 23 (test execution).

## 18. Traceability

Parents: SYS-003. Children: inflation functions, trigger criteria, safeguard definitions, and sustainment hooks (artefact IDs TBD).
RTM: REQ-HFPX-IPS-001..004 → CONCEPT. Each coverage claim traces to at least one trigger criterion and at least one verification case; each sustainment hook traces to Vol 27 (all TBD except IDs).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Inflation and trigger definitions are under document control once populated; changes via change records with affected-coverage impact stated.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (inflatable protection system; Ch 13.13) |
