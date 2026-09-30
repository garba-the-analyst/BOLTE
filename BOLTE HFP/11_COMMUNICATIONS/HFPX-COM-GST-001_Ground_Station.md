# Ground Station

**Document ID:** HFPX-COM-GST-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X ground station for Volume 11, Chapter 11.10: station functions for monitor, command, and telemetry, plus displays and staffing.

## 2. Scope

Covers ground-station functions, operator displays, and staffing concepts supporting all flight modes and ground operations. Equipment selections, display designs, staffing levels, and facility details are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.3 ground links, 11.4 telemetry, 11.5 command links, 11.6 emergency, 11.9 loss management); Vol 13.17 (ground-station authority); Vol 17 (cybersecurity); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Ground station: ground element hosting monitor, command, and telemetry functions (details TBD).
- Monitor: ground observation of vehicle/link state via telemetry (details TBD).
- Staffing: ground-station roles and responsibilities (TBD).

## 5. System Context

The ground station terminates ground links (11.3), hosts telemetry monitoring (11.4) and command origination (11.5), supports emergency communications (11.6) and loss management (11.9), and operates under Vol 13.17 authority (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CGS-001|Ground-station functions for monitor, command, and telemetry handling shall be defined (functions TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CGS-002|Ground-station displays for link state, telemetry, and loss-response status shall be defined (designs TBD).|REQ-HFPX-OPC-003|Demonstration|
|REQ-HFPX-CGS-003|Ground-station staffing, including roles, responsibilities, and authority per Vol 13.17, shall be defined (details TBD).|REQ-HFPX-OPC-003|Inspection|
|REQ-HFPX-CGS-004|Ground-station interfaces to communications links, networks, and recording, including spectrum/regulatory hooks to Vol 25, shall be defined (details TBD).|REQ-HFPX-STK-007|Inspection|

## 7. Architecture

Ground-station segments (RF, network, consoles, recorders — allocation TBD) host monitor/command/telemetry functions. Displays present link state, telemetry, and loss-response status (designs TBD). Staffing roles map to command-authority and emergency concepts (mapping TBD, Vol 13.17).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Station equipment, console designs, networks, and facilities are TBD.

## 9. Interfaces

Interfaces to ground-link terminals, operations networks, recorders, and vehicle command/telemetry paths are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

The ground station supports all flight modes and ground operations, including handover between stations, degraded-link operations per 11.9, and emergency operations per 11.6 under Vol 13.17 authority. Procedures and staffing concepts are TBD.

## 11. Safety

Ground-station failure or operator error affecting command/telemetry is hazardous. Mitigation is via defined functions (CGS-001), displays (CGS-002), staffing/authority (CGS-003), and interfaces (CGS-004), plus redundancy (11.8) and loss management (11.9). No availability or human-factors claim is made at this revision.

## 12. Performance

Display, staffing-response, and station-availability budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review and later ground-station integration and operator-in-the-loop testing (detail TBD, Vol 19/33).

## 14. Risks

- Staffing/authority definition incomplete; mitigation: Vol 13.17 hooks and human-factors input, TBD.
- Facility/site constraints unknown; mitigation: siting trade, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Station functions TBD; display designs TBD; staffing TBD; interfaces TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.3/11.4/11.5/11.6/11.9, Vol 13.17 (authority), Vol 17, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: ground-station design, ICDs, V&V cases. RTM: REQ-HFPX-CGS-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.10) |
