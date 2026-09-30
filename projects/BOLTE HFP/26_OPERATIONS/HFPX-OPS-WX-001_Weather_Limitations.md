# Weather Limitations

**Document ID:** HFPX-OPS-WX-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X weather limitations framework (Chapter 26.11): weather-minima structure, measurement-source structure, go and no-go structure and verification structure. All minima, sources, criteria and methods are TBD.

## 2. Scope

Covers weather limitations at structure-only level, including minima placeholders, source hooks and go and no-go decision hooks. Excludes executable flight-operation instructions, minima values, instrument selections and decision values — all TBD. No executable flight-operation instructions are given in this document.

## 3. Applicable Documents

- HFPX-SYS-CON-001 CONOPS (scenario preconditions); OPC tier (allocation TBD); OLI tier Vol 26.2 (allocation TBD)
- Vol 23 test and range hooks (allocation TBD); Vol 11 telemetry hooks (allocation TBD); Vol 13 safety hooks (allocation TBD)
- HFP prompt operations and MVP progression sections (values TBD)

## 4. Definitions & Acronyms

- Weather minima: bounds on weather parameters permitting operation (minima TBD).
- Measurement sources: instruments and services providing weather data (sources TBD).
- Go and no-go: decision to proceed, hold or abort on weather grounds (criteria TBD).
- OLI: operating limitations tier (Vol 26.2, allocation TBD).

## 5. System Context

Weather limitations bound all flight operations as preconditions owned with OPC, CON and OLI, applied by operator, pilot and ground crew with the vehicle, ground station and range. Envelopes, models and range criteria are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-OWL-001|The operations volume shall define the weather-minima structure (minima TBD).|OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2, allocation TBD)|Inspection|
|REQ-HFPX-OWL-002|Weather limitations shall define the measurement-source structure (sources TBD).|OPC tier, OLI tier (allocation TBD)|Inspection|
|REQ-HFPX-OWL-003|Weather limitations shall define the go and no-go structure with decision hooks (criteria TBD).|CON tier, OLI tier, Vol 23 hook (allocation TBD)|Inspection|
|REQ-HFPX-OWL-004|Weather limitations shall define the verification structure for minima, sources and decisions (methods TBD).|OPC tier, Vol 23 hook (allocation TBD)|Inspection|

## 7. Architecture

Limitation framework with placeholders for parameter bounds, source mapping and go and no-go decision branches (all TBD), linked to OLI bounds and CON preconditions. Structure only; parameters, values and logic are TBD in later Vol 26 detail.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Minima tables, source selections, decision matrices and briefing scripts are TBD. No executable flight-operation instructions are stated; detailed limitations will be owned in later Vol 26 revisions.

## 9. Interfaces

Interfaces to OLI bounds, CONOPS preconditions, weather instruments and services, ground station displays, telemetry and range artefacts are TBD. Each shall be captured in an ICD before CDR (method TBD).

## 10. Operational Concept

Weather is applied as a precondition check within the nominal thread and as a hold or abort trigger within off-nominal handling (thresholds TBD), with go and no-go represented as structure only. All validation is unmanned first. No executable flight-operation instructions are given.

## 11. Safety

Flight outside weather capability is hazardous: bounded minima structure (OWL-001), explicit source mapping (OWL-002) and go and no-go hooks (OWL-003) plus envelope analysis mitigate it. No capability or margin claim is made; all minima TBD pending envelope and safety analysis and unmanned test.

## 12. Performance

Measurement accuracy, update rates, decision latencies and availability budgets are TBD. No parameter, rate or margin values are stated.

## 13. Verification & Validation

Verified by inspection and analysis of minima structure, source mapping and decision hooks and validated by unmanned progression (methods TBD, Vol 23). Source calibration and decision drills are covered by hooks (methods TBD).

## 14. Risks

- Source uncertainty and spatial variability affecting go and no-go quality; mitigation: explicit source and decision stubs, TBD.
- Minima TBD — early bounds may be overly permissive or restrictive; mitigation: minima stub explicit, verification unmanned first.

## 15. Open Issues

Weather minima TBD; measurement sources TBD; go and no-go criteria TBD; verification scope and methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2), envelope models, Vol 11 telemetry, Vol 13 safety view and Vol 23 test and range.

## 18. Traceability

Parents: OPC tier; CON tier (HFPX-SYS-CON-001); OLI tier (Vol 26.2); Vol 11, Vol 13 and Vol 23 hooks (allocations TBD). Children: Vol 26 detailed weather limitations, V&V cases. RTM: REQ-HFPX-OWL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.11) |
