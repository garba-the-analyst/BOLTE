# Ground Communications

**Document ID:** HFPX-COM-GDC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X ground communications for Volume 11, Chapter 11.3: ground links, coverage, and handover.

## 2. Scope

Covers vehicle-to-ground-station/operations links for all flight modes and ground operations. Link parameters, spectra, hardware, coverage values, and handover thresholds are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1 architecture, 11.4 telemetry, 11.5 command links, 11.8 redundancy, 11.9 loss management, 11.10 ground station); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Ground link: RF/data connectivity between vehicle and ground elements (details TBD).
- Coverage: geographic/operational extent of ground-link availability (TBD).
- Handover: transfer of ground-link responsibility between stations/sectors (logic TBD).

## 5. System Context

Ground communications connect the vehicle to the ground station and operations network, carrying command uplink and telemetry downlink traffic plus coordination voice/data. Interfaces to 11.4, 11.5, and 11.10 are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CGC-001|Ground links, including functions, roles, and interfaces to the ground station, shall be defined (details TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CGC-002|Ground-link coverage across flight modes and ground operations shall be defined (extent TBD).|REQ-HFPX-MIS-004|Test|
|REQ-HFPX-CGC-003|Handover of ground links between stations/sectors, including logic and responsibilities, shall be defined (logic TBD).|REQ-HFPX-OPC-003|Inspection|
|REQ-HFPX-CGC-004|Spectrum and regulatory constraints applicable to ground links shall be identified as TBD hooks to Vol 25 (licensing path TBD).|REQ-HFPX-STK-007|Inspection|

## 7. Architecture

Ground-link paths are allocated within the communications partition (11.1) and terminate at ground-station elements (11.10). Handover logic coordinates station-to-station transfer (logic TBD). Redundancy and loss behaviour hook to 11.8 and 11.9 (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Antennas, terminals, waveforms, networks, and protocols are TBD.

## 9. Interfaces

RF and network interfaces to ground-station equipment and operations networks are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Ground links support all flight modes and ground operations, including handover between stations/sectors and degraded-link operations per 11.9. Procedures are TBD.

## 11. Safety

Loss or degraded ground communications is hazardous. Mitigation is via defined ground links (CGC-001), coverage (CGC-002), handover logic (CGC-003), plus redundancy (11.8) and loss management (11.9). No coverage or availability claim is made at this revision.

## 12. Performance

Coverage extent, availability, throughput, and handover timing budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later range and handover testing (detail TBD, Vol 19/33).

## 14. Risks

- Coverage gaps unknown; mitigation: analysis and range testing, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Ground-link details TBD; coverage TBD; handover logic TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.4/11.5 links, 11.8 redundancy, 11.9 loss management, 11.10 ground station, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: ground comms design, ICDs, V&V cases. RTM: REQ-HFPX-CGC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.3) |
