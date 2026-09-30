# Fuel Management

**Document ID:** HFPX-OPS-FUM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X fuel management framework (Chapter 26.12): fuel-planning structure, reserve-policy structure, in-flight monitoring structure and verification structure. All methods, policies and designs are TBD.

## 2. Scope

Covers fuel management at structure-only level from planning through in-flight monitoring to shutdown, including planning placeholders, reserve hooks and monitoring hooks to Vol 05.10. Excludes executable flight-operation instructions, quantity values, reserve values and monitoring thresholds — all TBD. No executable flight-operation instructions are given in this document.

## 3. Applicable Documents

- HFPX-SYS-CON-001 CONOPS (scenario threads); OPC tier (allocation TBD); OLI tier Vol 26.2 (allocation TBD)
- Vol 05 fuel hooks including Vol 05.10 monitoring (allocation TBD); Vol 13 safety hooks (allocation TBD); Vol 23 test hooks (allocation TBD)
- HFP prompt operations and MVP progression sections (values TBD)

## 4. Definitions & Acronyms

- Fuel planning: estimation of required fuel for the planned thread (method TBD).
- Reserve policy: additional fuel held for off-nominal needs (policy TBD).
- In-flight monitoring: tracking of fuel state during flight (design TBD, Vol 05.10 hook).
- OLI: operating limitations tier (Vol 26.2, allocation TBD).

## 5. System Context

Fuel management links mission planning, the fuel system and the crew and operator with the vehicle, ground station and range. Fuel quantities, burn models, measurement designs and abort rules are TBD and owned with OPC, CON, OLI, Vol 05 and Vol 13.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-OFM-001|The operations volume shall define the fuel-planning structure (method TBD).|OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2, allocation TBD)|Inspection|
|REQ-HFPX-OFM-002|Fuel management shall define the reserve-policy structure (policy TBD).|OPC tier, OLI tier, Vol 13 hook (allocation TBD)|Inspection|
|REQ-HFPX-OFM-003|Fuel management shall define the in-flight monitoring structure consistent with the Vol 05.10 hook (design TBD).|CON tier, Vol 05 hook including Vol 05.10 (allocation TBD)|Test|
|REQ-HFPX-OFM-004|Fuel management shall define the verification structure for planning, reserves and monitoring (methods TBD).|OPC tier, Vol 23 hook (allocation TBD)|Inspection|

## 7. Architecture

Management framework with placeholders for planning inputs, reserve branches and monitoring and alerting branches (all TBD), linked to OLI bounds, CON threads and Vol 05.10 monitoring hooks. Structure only; calculations, policies and thresholds are TBD in later Vol 26 detail.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Planning worksheets, reserve tables, monitoring displays, alert thresholds and checklists are TBD. No executable flight-operation instructions are stated; detailed procedures will be owned in later Vol 26 revisions.

## 9. Interfaces

Interfaces to OLI bounds, mission planning artefacts, Vol 05 fuel quantity and monitoring, ground station displays, telemetry and range artefacts are TBD. Each shall be captured in an ICD before CDR (method TBD).

## 10. Operational Concept

Fuel is planned before flight, checked at pre-flight and start, monitored during hover, transition and cruise and reconciled after landing within the CONOPS thread (quantities TBD), with low-fuel handling as structure only handing to abort or safety paths (thresholds TBD). All validation is unmanned first. No executable flight-operation instructions are given.

## 11. Safety

Fuel exhaustion, starvation or mismanaged reserves is hazardous: bounded planning structure (OFM-001), explicit reserve policy hooks (OFM-002) and monitoring hooks (OFM-003) plus the independent safety path mitigate it. No endurance or margin claim is made; all quantities TBD pending Vol 05 and safety analysis and unmanned test.

## 12. Performance

Burn estimates, measurement accuracy, alert latencies and planning margins are TBD. No quantity, rate or margin values are stated.

## 13. Verification & Validation

Verified by inspection and analysis of planning structure, reserve hooks and monitoring hooks and validated by unmanned progression (methods TBD, Vol 23). Monitoring accuracy is covered by Vol 05 hooks (methods TBD).

## 14. Risks

- Burn-model uncertainty affecting planning and reserve adequacy; mitigation: explicit planning and reserve stubs with Vol 05 hooks, TBD.
- Monitoring design TBD — in-flight state may be incompletely observed; mitigation: Vol 05.10 hook explicit, verification unmanned first.

## 15. Open Issues

Fuel-planning method TBD; reserve policy TBD; in-flight monitoring design TBD with Vol 05.10 hook; verification scope and methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2), Vol 05 fuel system including Vol 05.10, Vol 13 safety view and Vol 23 test progression.

## 18. Traceability

Parents: OPC tier; CON tier (HFPX-SYS-CON-001); OLI tier (Vol 26.2); Vol 05 including Vol 05.10, Vol 13 and Vol 23 hooks (allocations TBD). Children: Vol 26 detailed fuel procedures, V&V cases. RTM: REQ-HFPX-OFM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.12) |
