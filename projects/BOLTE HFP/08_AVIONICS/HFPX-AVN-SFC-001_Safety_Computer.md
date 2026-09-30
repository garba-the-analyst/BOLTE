# Safety Computer

**Document ID:** HFPX-AVN-SFC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X safety computer (Chapter 08.3): independence from the flight computer, monitoring/stabilisation/recovery-trigger functions, dissimilarity policy, assurance scaffolding, and fault-injection verification. No parts, topologies, or values selected.

## 2. Scope

Covers safety-computer independence principles, monitoring and recovery-trigger functions, dissimilarity policy, assurance scaffolding structured according to recognised concepts, and verification approach. Excludes hardware selection, detailed logic design, and quantitative thresholds (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-SYS-ARC-001 SAD (AVN, HWA, SWA, DAT views)
- HFPX-AVN-ARC-001 Avionics Architecture (Chapter 08.1)
- HFPX-AVN-FLC-001 Flight Computer (Chapter 08.2 context)

## 4. Definitions & Acronyms

- Safety computer: independent computing path for monitoring and recovery-trigger functions.
- Independence: separation across power, sensing, and compute aspects.
- Dissimilarity: policy for difference between flight and safety paths to limit common-cause effects.
- Fault injection: verification by introduction of faults to observe detection and response.

## 5. System Context

The safety computer monitors flight-path behaviour and linked health, and triggers recovery actions through defined interfaces. It operates alongside the flight computer across flight and maintenance states. All allocations and mechanisms are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VSC-001 | The safety computer shall be independent from the flight computer across power, sensing, and compute aspects (details TBD). | REQ-HFPX-SYS-003; SAD AVN view | Analysis |
| REQ-HFPX-VSC-002 | The safety computer shall provide monitoring, stabilisation, and recovery-trigger functions (logic and thresholds TBD). | REQ-HFPX-SYS-003; SAD SWA view | Analysis |
|REQ-HFPX-VSC-003|The safety computer shall be governed by a dissimilarity policy with respect to the flight computer (measures TBD).|REQ-HFPX-SYS-005; SAD HWA view|Inspection|
|REQ-HFPX-VSC-004|The safety computer development artefacts shall be structured according to DO-178C and DO-254 concepts (details TBD).|REQ-HFPX-SYS-005; SAD SWA view|Inspection|
| REQ-HFPX-VSC-005 | The safety computer shall be verified by fault injection covering detection and recovery triggering (cases TBD). | REQ-HFPX-SYS-005; SAD AVN view | Test |

## 7. Architecture

Safety-computer concept (details TBD): independent sensing/compute/power groupings, monitoring functions, and recovery-trigger paths. Dissimilarity is stated as policy without selected measures. No devices, topologies, or logic selected.

## 8. Detailed Design

Not applicable at this revision. Hardware design, monitoring logic, and interface wiring are deferred to Vol 08 detail and ICDs. No parts selected.

## 9. Interfaces

Safety-computer interfaces: independent sensing inputs, flight-computer coordination, recovery-trigger outputs, data exchanges, power feeds, and test interfaces. Definitions are TBD in ICDs.

## 10. Operational Concept

Safety computer monitors across flight modes and triggers recovery through defined paths. Behaviour in degraded and maintenance states is TBD.

## 11. Safety

Independence, dissimilarity, monitoring, and recovery-trigger principles support parent safety intent. Analyses and thresholds are TBD with no values stated.

## 12. Performance

Detection coverage, response behaviour, and capacity details are TBD. No values stated.

## 13. Verification & Validation

Verified by analysis (independence and monitoring arguments), review (dissimilarity policy and assurance structure), and test by fault injection with cases TBD.

## 14. Risks

- Independence claims undermined by shared dependencies; mitigation: dependency analysis with review gate.
- Monitoring gaps or spurious triggers; mitigation: fault-injection campaign tied to safety analyses.

## 15. Open Issues

Independence details, monitoring logic, dissimilarity measures, assurance details, and fault-injection cases are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS, SAD AVN/HWA/SWA/DAT views, Chapters 08.1–08.2, and safety analyses.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; SAD AVN/HWA/SWA/DAT views. Children: Vol 08 detail and verification artefacts. RTM: REQ-HFPX-VSC-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.3.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.3) |
