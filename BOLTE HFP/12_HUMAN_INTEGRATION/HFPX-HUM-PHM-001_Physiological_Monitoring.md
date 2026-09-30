# Physiological Monitoring

**Document ID:** HFPX-HUM-PHM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define physiological-monitoring requirements for HFP-X pilot integration (Chapter 12.12). This Tranche 6 draft establishes monitored-parameter, alert-threshold, and data-handling placeholders; all values are TBD.

## 2. Scope

Covers monitored physiological parameters, alert thresholds and annunciation, and data-privacy/handling provisions. Excludes fatigue-monitoring detail (12.11), HMI annunciation design (Vol 10), and medical interpretation, which is TBD.

## 3. Applicable Documents

- HFPX-SYS-HUM-001 Human Factors Requirements (parent HUM tier)
- Stakeholder need STK-002 (human involvement)
- HSA tier (ID TBD — allocation to follow)
- Vol 30 hooks (TBD — training/monitoring inputs to follow)
- Vol 10 HMI (TBD annunciation detail), HFPX-HUM-FTG-001 (Chapter 12.11)

## 4. Definitions & Acronyms

- HUM: human-factors requirement tier; IDs `REQ-HFPX-HUM-NNN`.
- UPM: physiological-monitoring requirement tier; IDs `REQ-HFPX-UPM-NNN`; verification TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Physiological monitoring refines system-level monitoring needs into testable placeholders:

```text
STK-002 + HUM tier → UPM-001..004 → sensors / avionics / ground-station detail → V&V cases
```

No parameter, threshold, or handling rule is approved at this revision.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-UPM-001|The system shall monitor defined physiological parameters across defined phases (monitored parameters TBD).|STK-002, REQ-HFPX-HUM-004, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UPM-002|The system shall annunciate defined alert conditions to defined recipients per defined thresholds (alert thresholds TBD).|STK-002, REQ-HFPX-HUM-004, HSA tier (ID TBD)|Demonstration|
|REQ-HFPX-UPM-003|The system shall handle physiological data per defined privacy and handling provisions (data-privacy/handling TBD).|STK-002, REQ-HFPX-HUM-004, HSA tier (ID TBD)|Inspection|
|REQ-HFPX-UPM-004|Monitoring provisions shall be verified against defined criteria (criteria TBD; Vol 30 hook TBD).|STK-002, REQ-HFPX-HUM-004, HSA tier (ID TBD)|Inspection|

All parameters, thresholds, handling provisions, and criteria are TBD. No value is approved.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): UPM-001/002 → sensors, avionics, and ground-station annunciation with Vol 10 hooks; UPM-003 → data-management provisions; UPM-004 → V&V framework with Vol 30 hooks. All TBC.

## 8. Detailed Design

Not applicable — requirements level only. Sensor types, placements, algorithms, and data architectures are TBD in follow-on revisions.

## 9. Interfaces

Monitoring interfaces (sensor/suit couplings, avionics signals, ground-station presentation) are TBD in Vol 02 ICDs, Vol 10, and Chapter 12.1 register. No interface value or layout is approved.

## 10. Operational Concept

Monitoring requirements apply across preparation, flight, and recovery phases; phase-specific applicability is TBD. Unmanned demonstration precedes any crewed evaluation per safety gating.

## 11. Safety

Monitoring failures and missed alerts feed Vol 13 safety analyses (to follow). Monitoring is not a sole safety control unless established in Vol 13. No UPM requirement confers flight approval; human flight remains gated by tier 01.10 and the Safety Case.

## 12. Performance

No UPM requirement quantifies performance. All monitoring measures are TBD pending follow-on studies.

## 13. Verification & Validation

Each requirement states its method above as TBD; verification IDs, test conditions, participant criteria, and pass thresholds are TBD in the V&V Plan (Vol 22) with Vol 10/12/30 inputs. No monitoring credit is claimed at this revision.

## 14. Risks

- Parameter set undefined → mis-scoped sensing; mitigation: early UPM-001 placeholder plus review gates.
- Data-handling undefined → privacy/compliance findings; mitigation: UPM-003 placeholder plus review gates.

## 15. Open Issues

TBD: monitored parameters, alert thresholds and recipients, data-privacy/handling provisions, and verification criteria pending Vol 10, HSA-tier, and Vol 30 inputs.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on STK-002 stability, HUM-tier stability (HFPX-SYS-HUM-001), HSA-tier allocation (TBD), Vol 30 hooks (TBD), Vol 10 annunciation work, Chapter 12.11 fatigue inputs, and V&V Plan cases. Changes propagate by change record.

## 18. Traceability

Parents: STK-002, HUM tier (REQ-HFPX-HUM-004), HSA tier (ID TBD), Vol 30 hooks (TBD) — see table. Children: sensor specs, annunciation specs, data-handling specs, V&V cases, RTM rows. RTM seed for UPM-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Additions or parameter changes require new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 12.12) |
