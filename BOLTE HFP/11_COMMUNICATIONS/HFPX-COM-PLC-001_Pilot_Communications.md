# Pilot Communications

**Document ID:** HFPX-COM-PLC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X pilot communications for Volume 11, Chapter 11.2: pilot voice and data paths, intelligibility, and priority.

## 2. Scope

Covers onboard pilot voice/data links and their interfaces to vehicle and ground functions. Waveforms, spectra, hardware, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1 architecture, 11.8 redundancy, 11.9 loss management, 11.12 security); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Pilot voice: voice connectivity for pilot operations (details TBD).
- Pilot data: data connectivity for pilot operations (details TBD).
- Intelligibility: ability to understand voice communications (criteria TBD).
- Priority: precedence of pilot communications over other traffic (scheme TBD).

## 5. System Context

Pilot communications connect the pilot to vehicle functions and, via vehicle/ground paths, to ground operations across all flight modes. Interfaces to command, telemetry, and emergency communications are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CPC-001|Pilot voice connectivity, including functions and interfaces, shall be defined (details TBD).|REQ-HFPX-OPC-003|Inspection|
|REQ-HFPX-CPC-002|Pilot data connectivity, including functions and interfaces, shall be defined (details TBD).|REQ-HFPX-OPC-003|Inspection|
|REQ-HFPX-CPC-003|Pilot voice intelligibility criteria shall be defined (criteria TBD).|REQ-HFPX-SYS-005|Demonstration|
|REQ-HFPX-CPC-004|Priority of pilot communications relative to other traffic, including emergency traffic, shall be defined (scheme TBD).|REQ-HFPX-SYS-005|Inspection|

## 7. Architecture

Pilot voice and data paths are allocated within the communications partition (11.1). Priority logic orders pilot traffic relative to command, telemetry, and emergency traffic (scheme TBD). Redundancy and loss behaviour hook to 11.8 and 11.9 (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Audio paths, terminals, waveforms, and protocols are TBD.

## 9. Interfaces

Interfaces to avionics, headsets/panels, vehicle systems, and ground paths are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Pilot communications support all flight modes and ground operations, including degraded-link operations per 11.9. Procedures and phraseology are TBD.

## 11. Safety

Loss or misinterpretation of pilot communications is hazardous. Mitigation is via defined voice/data paths (CPC-001, CPC-002), intelligibility criteria (CPC-003), and priority scheme (CPC-004), plus redundancy (11.8) and loss management (11.9). No performance or safety claim is made at this revision.

## 12. Performance

Voice quality, intelligibility thresholds, availability, and timing budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later test of voice/data paths and priority behaviour (detail TBD, Vol 19/33).

## 14. Risks

- Intelligibility criteria undefined; mitigation: human-factors and test input, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Pilot voice details TBD; pilot data details TBD; intelligibility criteria TBD; priority scheme TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.8 redundancy, 11.9 loss management, 11.12 security, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: pilot comms design, ICDs, V&V cases. RTM: REQ-HFPX-CPC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.2) |
