# Data Links

**Document ID:** HFPX-COM-DTL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X data links for Volume 11, Chapter 11.7: link types, performance framework, and selection criteria.

## 2. Scope

Covers digital data-link bearers supporting command, telemetry, pilot data, and mission data transport. Link types, waveforms, spectra, hardware, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.3 ground links, 11.4 telemetry, 11.5 command links, 11.8 redundancy, 11.11 mission data, 11.12 security); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Data link: digital bearer for command/telemetry/data transport (types TBD).
- Selection criteria: criteria for choosing among data-link types (TBD).
- Performance framework: structure for data-link performance budgets (values TBD).

## 5. System Context

Data links provide bearers for command uplink, telemetry downlink, pilot data, and mission-data traffic between vehicle and ground elements. They sit within the 11.1 partition and serve consumers in 11.4, 11.5, and 11.11 (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CDL-001|Data-link types, including roles and applicability, shall be defined (types TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CDL-002|The data-link performance framework, including availability, throughput, and timing budget structure, shall be defined (values TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CDL-003|Selection criteria for choosing among data-link types per mission phase and traffic class shall be defined (criteria TBD).|REQ-HFPX-MIS-004|Inspection|
|REQ-HFPX-CDL-004|Data-link security and spectrum/regulatory hooks to 11.12/Vol 17 and Vol 25 shall be defined (mechanisms and licensing path TBD).|REQ-HFPX-STK-007|Inspection|

## 7. Architecture

Candidate data-link types (TBD) are mapped to traffic classes (command, telemetry, pilot data, mission data — mapping TBD). Selection logic chooses bearers per phase and link state (logic TBD). Security hooks per 11.12/Vol 17 and spectrum hooks per Vol 25 apply (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Waveforms, modems, antennas, networks, and protocols are TBD.

## 9. Interfaces

Air and ground data-link interfaces, including antennas, terminals, and network handoffs, are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Data links support all flight modes and ground operations, with selection/handover across bearers and degraded-link behaviour per 11.9. Procedures are TBD.

## 11. Safety

Loss or mis-selection of data links carrying safety-relevant traffic is hazardous. Mitigation is via defined link types (CDL-001), performance framework (CDL-002), selection criteria (CDL-003), and security/spectrum hooks (CDL-004), plus redundancy (11.8) and loss management (11.9). No performance claim is made at this revision.

## 12. Performance

Availability, throughput, and timing budgets for data links are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later bearer and end-to-end data-link testing (detail TBD, Vol 19/33).

## 14. Risks

- Bearer trade incomplete; mitigation: Vol 11 trade, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.
- Security overhead vs link behaviour; mitigation: Vol 17 hooks sized by analysis, TBD.

## 15. Open Issues

Link types TBD; performance values TBD; selection criteria TBD; security mechanisms TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.3/11.4/11.5/11.11 traffic needs, 11.8 redundancy, 11.9 loss management, 11.12 security, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: data-link trade/design, ICDs, V&V cases. RTM: REQ-HFPX-CDL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.7) |
