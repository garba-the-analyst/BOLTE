# Processing Hardware

**Document ID:** HFPX-AVN-PHW-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X avionics processing hardware classes (Chapter 08.4): processor/device classes, environmental qualification hooks, obsolescence hooks, and verification approach. No parts selected.

## 2. Scope

Covers device-class definitions, qualification hooks structured according to recognised concepts, obsolescence hooks, and verification approach. Excludes part selection, board design, packaging, and quantitative environmental values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-SYS-ARC-001 SAD (AVN, HWA, SWA, DAT views)
- HFPX-AVN-ARC-001 Avionics Architecture (Chapter 08.1)
- Vol 32.9 (obsolescence context)

## 4. Definitions & Acronyms

- Processing hardware: computing devices and supporting circuitry hosting avionics functions.
- Device class: role-based category of processors/devices without part selection.
- Qualification hooks: structural placeholders for future environmental qualification activity.
- Obsolescence hooks: structural placeholders for lifecycle and availability management.

## 5. System Context

Processing hardware hosts flight, safety, and interface functions within avionics enclosures across flight and maintenance environments. Thermal, mechanical, and power details are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VPH-001 | The avionics processing hardware shall define processor and device classes without part selection (classes TBD). | REQ-HFPX-SYS-002; SAD HWA view | Inspection |
|REQ-HFPX-VPH-002|The avionics processing hardware shall define environmental qualification hooks structured according to DO-160 concepts (details TBD).|REQ-HFPX-SYS-003; SAD HWA view|Inspection|
|REQ-HFPX-VPH-003|The avionics processing hardware shall define obsolescence hooks linked to Vol 32.9 (details TBD).|REQ-HFPX-SYS-002; SAD AVN view|Inspection|
|REQ-HFPX-VPH-004|The avionics processing hardware definitions shall be verified (method and evidence TBD).|REQ-HFPX-SYS-005; SAD HWA view|Inspection|

## 7. Architecture

Device classes named by role (details TBD) with qualification and obsolescence hooks as structural placeholders. No devices, boards, topologies, or values selected.

## 8. Detailed Design

Not applicable at this revision. Part selection, schematic/layout design, and packaging are deferred. No parts selected.

## 9. Interfaces

Hardware interfaces: device interconnects, I/O attachments, power feeds, thermal/mechanical boundaries, and test access. Definitions are TBD in ICDs.

## 10. Operational Concept

Processing hardware supports flight modes plus built-in test, degraded, and maintenance states. Environmental behaviour and lifecycle actions are TBD.

## 11. Safety

Hardware-class discipline and qualification/obsolescence hooks support parent safety intent. No safety values stated.

## 12. Performance

Capacity, timing, power, and environmental values are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection of device-class definitions and review of qualification and obsolescence hooks. Test and qualification activity is deferred to later tranches.

## 14. Risks

- Premature part lock-in constraining design; mitigation: class discipline with selection gate.
- Obsolescence pressure on long lifecycle; mitigation: hooks linked to Vol 32.9 process.

## 15. Open Issues

Device classes, qualification details, obsolescence details, and verification evidence are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS, SAD AVN/HWA/SWA/DAT views, Chapter 08.1 architecture, and Vol 32.9 lifecycle process.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; SAD AVN/HWA/SWA/DAT views. Children: Vol 08 hardware detail and qualification artefacts. RTM: REQ-HFPX-VPH-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.4.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.4) |
