# Incident Reporting

**Document ID:** HFPX-OPS-INR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X incident-reporting framework (Chapter 26.15): reportable-event criteria structure, reporting-timeline structure, investigation-flow structure and records structure. All criteria, timelines, flows and retention are TBD.

## 2. Scope

Covers incident reporting at structure-only level from event identification through reporting, investigation and records retention, including criteria placeholders, timeline hooks, flow hooks and records hooks. Excludes executable flight-operation instructions, event lists, timeline values and form contents — all TBD. No executable flight-operation instructions are given in this document.

## 3. Applicable Documents

- HFPX-SYS-CON-001 CONOPS (off-nominal threads); OPC tier (allocation TBD); OLI tier Vol 26.2 (allocation TBD)
- Vol 13 safety hooks (allocation TBD); Vol 23 test hooks (allocation TBD); Vol 27 and Vol 28 records hooks (allocations TBD)
- HFP prompt operations and MVP progression sections (values TBD)

## 4. Definitions & Acronyms

- Reportable-event criteria: conditions requiring a report (criteria TBD).
- Reporting timeline: timing for initial and follow-up reports (timeline TBD).
- Investigation flow: steps from report to cause and action (flow TBD).
- Records: retained reports and investigation artefacts (retention TBD).

## 5. System Context

Incident reporting links operations, safety, test and quality with the vehicle, ground station, safety path and range. Event detection, authority, investigation ownership and records retention are TBD and owned with OPC, CON, OLI, Vol 13, Vol 23, Vol 27 and Vol 28.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-OIR-001|The operations volume shall define the reportable-event criteria structure (criteria TBD).|OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2, allocation TBD)|Inspection|
|REQ-HFPX-OIR-002|Incident reporting shall define the reporting-timeline structure (timeline TBD).|OPC tier, Vol 13 hook (allocation TBD)|Inspection|
|REQ-HFPX-OIR-003|Incident reporting shall define the investigation-flow structure (flow TBD).|CON tier, Vol 13 and Vol 23 hooks (allocations TBD)|Inspection|
|REQ-HFPX-OIR-004|Incident reporting shall define the records structure for reports and investigations (retention TBD).|OPC tier, Vol 27 and Vol 28 hooks (allocations TBD)|Inspection|

## 7. Architecture

Reporting framework with placeholders for identification, notification, investigation and closure branches (all TBD), linked to CON off-nominal threads and Vol 13, Vol 23, Vol 27 and Vol 28 hooks. Structure only; criteria, timelines and flows are TBD in later Vol 26 detail.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Event lists, timeline values, investigation steps and report forms are TBD. No executable flight-operation instructions are stated; detailed procedures will be owned in later Vol 26 revisions.

## 9. Interfaces

Interfaces to OLI bounds, CONOPS detection and mitigation, safety analysis, test records and Vol 27 and Vol 28 records systems are TBD. Each shall be captured in an ICD before CDR (method TBD).

## 10. Operational Concept

Reportable events from any thread enter notification, investigation and closure within operations, safety and quality coordination (sequence TBD), with handover and escalation represented as structure only. All validation is unmanned first. No executable flight-operation instructions are given.

## 11. Safety

Unreported or uninvestigated events allowing recurrence is hazardous: bounded criteria structure (OIR-001), explicit timeline hooks (OIR-002), investigation hooks (OIR-003) and records hooks (OIR-004) plus the safety path mitigate it. No coverage claim is made; all criteria TBD pending Vol 13 analysis and unmanned experience.

## 12. Performance

Detection coverage, notification latencies, investigation durations and retention completeness budgets are TBD. No time, count or margin values are stated.

## 13. Verification & Validation

Verified by inspection and analysis of criteria structure, timeline hooks, flow hooks and records hooks and validated by unmanned progression records (methods TBD, Vol 23). Investigation effectiveness is covered by Vol 13 and Vol 27 and Vol 28 hooks (methods TBD).

## 14. Risks

- Criteria TBD — reportable events may be missed or over-reported; mitigation: explicit criteria stub with safety hooks, TBD.
- Flow and retention TBD — investigations may stall or records may be incomplete; mitigation: explicit flow and records stubs with Vol 27 and Vol 28 hooks.

## 15. Open Issues

Reportable-event criteria TBD; reporting timeline TBD; investigation flow TBD; records retention and verification methods TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on OPC tier, CON tier (HFPX-SYS-CON-001), OLI tier (Vol 26.2), Vol 13 safety view, Vol 23 test progression and Vol 27 and Vol 28 records and quality flows.

## 18. Traceability

Parents: OPC tier; CON tier (HFPX-SYS-CON-001); OLI tier (Vol 26.2); Vol 13, Vol 23, Vol 27 and Vol 28 hooks (allocations TBD). Children: Vol 26 detailed incident-reporting procedures, V&V cases. RTM: REQ-HFPX-OIR-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 26.15) |
