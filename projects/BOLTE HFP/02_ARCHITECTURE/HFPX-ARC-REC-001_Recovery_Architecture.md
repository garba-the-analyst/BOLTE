# Recovery Architecture

**Document ID:** HFPX-ARC-REC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X recovery architecture view (Chapter 02.14): recovery functions, deployment envelope, trigger authority, and verification approach. Recovery effectiveness is explicitly unproven.

## 2. Scope

Covers recovery structure and analysis/test methodology for the production-aircraft concept. Mechanism unselected (candidate functions TBD); envelope, authority, and sizing TBD (ISS-008 limiting case). Analysis and requirements only.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001..008); HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-001..005)
- ISS-008 (recovery limiting case); Vol 13 (safety analyses); Vol 19/33 (analysis, test, unmanned demonstrator)
- HFP prompt §§11, 14, 34 (recovery view, hazardous-subsystem boundary)

## 4. Definitions & Acronyms

- Recovery function: last-resort mitigation after loss of controlled flight (mechanism TBD; candidates e.g. parachute / impact protection / escape — all TBD, unselected).
- Deployment envelope: conditions under which recovery can initiate (all TBD, ISS-008).
- Trigger authority: who/what commands deployment (TBD).

## 5. System Context

Recovery sits downstream of the safety path: on detection of unrecoverable flight, the safety computer or pilot commands the recovery function within its deployment envelope. Sizing, placement, and envelope TBD.

> **Hazardous-subsystem boundary (prompt §§14, 34).** This document is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis for the recovery subsystem. It contains no instructions for building, igniting or operating high-energy propulsion, parachute/escape mechanisms, or human-carrying flight outside appropriate controls.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-REC-001 | Recovery functions (parachute / impact-protection / escape — all TBD, mechanism unselected) shall be defined with roles and non-roles. | Inspection |
| REQ-HFPX-REC-002 | The recovery deployment envelope shall be defined (all TBD; ISS-008 is the limiting case). | Analysis |
| REQ-HFPX-REC-003 | Trigger authority (automatic vs pilot-commanded, thresholds, inhibits — all TBD) shall be defined. | Analysis + Test |
| REQ-HFPX-REC-004 | Recovery shall be verified by analysis plus test (methods TBD, Vol 19/33); effectiveness shall be stated as unproven until verified. | Analysis + Test |

## 7. Architecture

Functional chain: fault detection (safety path) → recoverability decision → trigger → deployment → descent/impact mitigation (mechanisms TBD, unselected). Authority logic (automatic thresholds, pilot command, inhibits — TBD) arbitrates triggering; envelope limits (speed, attitude, altitude, all TBD per ISS-008) gate deployment. Interfaces to safety computer, pilot controls, and impact-protection functions (SYS-15/16, TBD) are defined at ICD level. No mechanism is selected and no sizing value is stated.

## 8. Detailed Design

Not applicable at Tranche 2 draft level. Mechanism selection, sizing, placement, and sequencing are TBD pending ISS-008 and Vol 13/19 trades.

## 9. Interfaces

Recovery interfaces (trigger lines, deployment effectors, structural mounts, pilot controls) are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Recovery is a last-resort branch of CONOPS emergency handling; arming, deployment, and post-deployment procedures TBD. Inadvertent-deployment prevention (inhibits, safing — TBD) is mandatory logic.

## 11. Safety

Safety is the governing emphasis: recovery is last-resort mitigation, not a guarantee — effectiveness is explicitly unproven. Hazards include failure to deploy, inadvertent deployment, and deployment outside the envelope; mitigations are envelope definition (REC-002), trigger authority with inhibits (REC-003), and analysis-plus-test verification (REC-004). No survivability claim is made.

## 12. Performance

Deployment time, descent rate, impact attenuation, and envelope limits are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by analysis (envelope, reliability) plus test (deployment/functional testing, methods TBD, Vol 19/33). Unmanned demonstration precedes any human-carriage claim. Effectiveness remains unproven until complete.

## 14. Risks

- ISS-008: envelope may be too narrow to be useful; mitigation: envelope analysis bounds the trade early.
- Inadvertent or failed deployment; mitigation: inhibit/safing logic and test, both TBD.

## 15. Open Issues

ISS-008 (limiting case/envelope); mechanism unselected; trigger authority TBD; envelope values TBD; test methodology TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-001..005), SyRS, safety view (02.10), control view (02.12), Vol 13 (analyses), Vol 19/33 (modelling/test), airframe trade (ISS-004).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (esp. ARC-003); tier inputs SAF/FUN as allocated. Children: recovery trade studies, Vol 13 analyses, V&V cases. RTM: REQ-HFPX-REC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.14) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
