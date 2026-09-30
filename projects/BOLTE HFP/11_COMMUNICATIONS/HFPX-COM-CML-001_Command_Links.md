# Command Links

**Document ID:** HFPX-COM-CML-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X command links for Volume 11, Chapter 11.5: command uplink behaviour, integrity/protection, and unauthorised-command protection.

## 2. Scope

Covers ground/pilot-to-vehicle command paths for all flight modes and ground operations. Command sets, formats, protocols, hardware, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1 architecture, 11.3 ground links, 11.7 data links, 11.8 redundancy, 11.9 loss management, 11.12 security); Vol 13 (authority); Vol 17 (cybersecurity); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Command link: ground/pilot-to-vehicle path carrying commands (details TBD).
- Command integrity: assurance that commands arrive unaltered and from an authorised source (mechanisms TBD).
- Unauthorised command: command from an unauthorised source or altered in transit (protection TBD).

## 5. System Context

Command links carry authorised commands from pilot/ground-station sources to vehicle execution, coordinated with command authority (Vol 13) and protected per 11.12/Vol 17. Loss behaviour hooks to 11.9 (TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-CCL-001 | The command uplink, including command set, sources, and execution interfaces, shall be defined (details TBD). | REQ-HFPX-SYS-005 | Inspection |
| REQ-HFPX-CCL-002 | Command-link integrity and protection behaviour shall be defined (mechanisms TBD). | REQ-HFPX-SYS-005 | Test |
| REQ-HFPX-CCL-003 | Protection against unauthorised commands, including authentication and authorisation hooks per 11.12/Vol 17, shall be defined (mechanisms TBD). | REQ-HFPX-SYS-005 | Test |
| REQ-HFPX-CCL-004 | Command-link loss and degraded-link behaviour hooks to 11.9, including rejection/handling of stale or duplicate commands, shall be defined (behaviour TBD). | REQ-HFPX-OPC-003 | Inspection |

## 7. Architecture

Command paths run from authorised pilot/ground sources over ground/data links to vehicle command execution (paths TBD). Integrity checks and authorisation gates sit at transmit and receive ends (mechanisms TBD). Redundant command paths hook to 11.8; loss logic hooks to 11.9 (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Command formats, protocols, cryptographic mechanisms, and hardware are TBD.

## 9. Interfaces

Interfaces to command sources, link terminals, vehicle command execution, and authority logic (Vol 13) are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Command links support all flight modes and ground operations under defined command authority (Vol 13). Degraded/lost-link command handling follows 11.9 (TBD).

## 11. Safety

Lost, corrupted, delayed, duplicated, or unauthorised commands are hazardous. Mitigation is via defined uplink (CCL-001), integrity/protection (CCL-002), unauthorised-command protection (CCL-003), and loss handling (CCL-004), plus redundancy (11.8) and Vol 17 security (11.12). No integrity or availability claim is made at this revision.

## 12. Performance

Command throughput, availability, and timing budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later command-link and protection testing, including fault injection (detail TBD, Vol 19/33).

## 14. Risks

- Command authority coordination incomplete; mitigation: Vol 13 hooks, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.
- Security vs command-path complexity; mitigation: Vol 17 hooks sized by analysis, TBD.

## 15. Open Issues

Command set TBD; integrity mechanisms TBD; unauthorised-command protection TBD; loss handling TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.3/11.7 links, 11.8 redundancy, 11.9 loss management, 11.12 security, Vol 13 (authority), Vol 17, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: command-link design, ICDs, V&V cases. RTM: REQ-HFPX-CCL-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.5) |
