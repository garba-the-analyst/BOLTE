# Telemetry

**Document ID:** HFPX-COM-TLM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X telemetry for Volume 11, Chapter 11.4: telemetered-parameter inventory, downlink behaviour, and recording hooks.

## 2. Scope

Covers vehicle-to-ground telemetry for health, status, and mission data transport. Parameter lists, sampling/transport cadences, formats, and recording implementations are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1 architecture, 11.3 ground links, 11.7 data links, 11.10 ground station, 11.11 mission data); Vol 17 (cybersecurity); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Telemetry: vehicle-to-ground transport of status/health data (details TBD).
- Telemetered-parameter inventory: list of parameters carried on telemetry links (TBD).
- Recording: onboard and/or ground capture of telemetry for later use (hooks TBD).

## 5. System Context

Telemetry flows from vehicle sources over ground links (11.3) and data links (11.7) to ground-station displays and recording (11.10), and supports mission-data needs (11.11). Security hooks per 11.12/Vol 17 apply (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CTM-001|The telemetered-parameter inventory, including health, status, and safety-relevant parameters, shall be defined (inventory TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CTM-002|Telemetry transport behaviour, including cadences and prioritisation, shall be defined (values TBD).|REQ-HFPX-MIS-004|Inspection|
|REQ-HFPX-CTM-003|Recording hooks for telemetry, onboard and on the ground, shall be defined (implementation TBD).|REQ-HFPX-OPC-003|Inspection|
|REQ-HFPX-CTM-004|Telemetry integrity and security hooks per 11.12/Vol 17 shall be defined (mechanisms TBD).|REQ-HFPX-SYS-005|Inspection|

## 7. Architecture

Telemetry sources feed framed downlink paths over ground/data links (paths TBD) to ground-station consumers and recorders (consumers TBD). Prioritisation orders safety-relevant parameters ahead of routine traffic (scheme TBD). Integrity/security hooks wrap telemetry (mechanisms TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Frame formats, protocols, sampling schemes, and recorder implementations are TBD.

## 9. Interfaces

Interfaces to avionics sources, link terminals, ground-station displays, and recorders are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Telemetry supports all flight modes and ground operations, including degraded-link prioritisation per 11.9. Display and recording use concepts hook to 11.10 (TBD).

## 11. Safety

Loss or corruption of safety-relevant telemetry is hazardous. Mitigation is via defined parameter inventory (CTM-001), prioritised transport (CTM-002), recording hooks (CTM-003), and integrity/security hooks (CTM-004), plus redundancy (11.8). No availability or integrity claim is made at this revision.

## 12. Performance

Transport cadences, throughput, availability, and recording-capacity budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later link and end-to-end telemetry testing (detail TBD, Vol 19/33).

## 14. Risks

- Parameter inventory incomplete; mitigation: source-system trades, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.
- Security overhead vs transport behaviour; mitigation: Vol 17 hooks sized by analysis, TBD.

## 15. Open Issues

Telemetered-parameter inventory TBD; transport cadences TBD; recording implementation TBD; integrity/security mechanisms TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.3/11.7 links, 11.8 redundancy, 11.10/11.11 consumers, 11.12 security, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: telemetry design, ICDs, V&V cases. RTM: REQ-HFPX-CTM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.4) |
