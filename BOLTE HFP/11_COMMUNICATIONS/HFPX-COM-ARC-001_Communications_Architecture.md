# Communications Architecture

**Document ID:** HFPX-COM-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X communications architecture for Volume 11, Chapter 11.1: link inventory, architecture partition, redundancy concept, and security hooks.

## 2. Scope

Covers pilot, ground, telemetry, and command links at architecture level. All link parameters, spectra, hardware selections, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view (02.13)
- Vol 11 Chapters 11.2–11.12; Vol 17 (cybersecurity); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Pilot link: pilot voice/data connectivity (details TBD).
- Ground link: vehicle-to-ground-station connectivity (details TBD).
- Telemetry link: vehicle-to-ground status/health data (details TBD).
- Command link: ground/pilot commands to vehicle (details TBD).
- Architecture partition: allocation of communications functions to segments (TBD).

## 5. System Context

Communications architecture connects pilot, vehicle, and ground station/operations across all flight modes. It partitions pilot/ground/telemetry/command functions and references redundancy (11.8), loss management (11.9), and security (11.12). All parameters TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CAR-001|The communications link inventory, including pilot, ground, telemetry, and command links with roles and criticality, shall be defined (inventory TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CAR-002|The communications architecture partition across vehicle, pilot, and ground segments shall be defined (partition TBD).|HFPX-ARC-COM-001|Inspection|
|REQ-HFPX-CAR-003|The communications redundancy concept for safety-critical links shall be defined (concept TBD, detail in 11.8).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CAR-004|Communications security hooks per Vol 17, including authentication, integrity, and key management, shall be applied to command and telemetry links (mechanisms TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CAR-005|Spectrum and regulatory constraints applicable to communications links shall be identified as TBD hooks to Vol 25 (licensing path TBD).|REQ-HFPX-STK-007|Inspection|

## 7. Architecture

Link classes (pilot, ground, telemetry, command — inventories TBD) are partitioned across vehicle, pilot, and ground segments (partition TBD). Redundant paths protect safety-critical traffic (scheme TBD, see 11.8). Security hooks per Vol 17 wrap command and telemetry links (mechanisms TBD). Spectrum/regulatory interfaces hook to Vol 25 (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Link budgets, spectra, waveforms, hardware, and protocols are TBD (Vol 11 detail chapters).

## 9. Interfaces

RF interfaces (antennas, terminals, ground station) and data handoffs to avionics and logging are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Links support all flight modes and ground operations; degraded and lost-link behaviour follows 11.9. Coverage, handover, and beyond-line-of-sight rules are TBD.

## 11. Safety

Lost, spoofed, or corrupted links are hazardous. Mitigation is via defined link inventory (CAR-001), redundancy concept (CAR-003), loss management (11.9), and Vol 17 security hooks (CAR-004). No availability or security claim is made at this revision.

## 12. Performance

Link performance values, including availability, throughput, and timing budgets, are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by review of architecture definition, partition, redundancy concept, and security and Vol 25 hooks. Later phases add analysis and test (methods TBD, detail in 11.8/11.9/11.12).

## 14. Risks

- Link inventory or partition incomplete; mitigation: Vol 11 detail chapters, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.
- Security-link complexity; mitigation: Vol 17 hooks sized by analysis, TBD.

## 15. Open Issues

Link inventory TBD; architecture partition TBD; redundancy concept TBD; security mechanisms TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), Vol 11 detail chapters (11.2–11.12), Vol 17 (cybersecurity), Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: Vol 11 detail designs, ICDs, V&V cases. RTM: REQ-HFPX-CAR-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.1) |
