# Communications Security

**Document ID:** HFPX-COM-SEC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X communications security for Volume 11, Chapter 11.12: threat hooks, authentication/authorisation, and key management.

## 2. Scope

Covers security of pilot, ground, telemetry, command, emergency, data-link, and mission-data paths. Threats, mechanisms, key-management implementations, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1–11.11 links and consumers); Vol 17.2 (threats), 17.7/17.8 (authentication/authorisation), 17.11 (data protection); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Authentication: verification of the identity of a communications party (mechanisms TBD, Vol 17.7).
- Authorisation: verification of permission to issue or accept traffic (mechanisms TBD, Vol 17.8).
- Key management: generation, distribution, storage, and revocation of cryptographic keys (TBD).

## 5. System Context

Communications security wraps all Vol 11 links and data flows, applying Vol 17 threat, authentication, authorisation, and key-management provisions to command, telemetry, pilot, ground, emergency, and mission-data traffic (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-CSC-001|Communications threat hooks per Vol 17.2, including applicable threat classes for command and telemetry links, shall be defined (details TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CSC-002|Authentication and authorisation hooks per Vol 17.7/17.8 for command, telemetry, and ground-station paths shall be defined (mechanisms TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CSC-003|Key management for protected communications links shall be defined, including lifecycle and revocation (details TBD).|REQ-HFPX-SYS-005|Inspection|
|REQ-HFPX-CSC-004|Security behaviour under degraded/lost-link conditions per 11.8/11.9 shall be defined (behaviour TBD).|REQ-HFPX-OPC-003|Inspection|

## 7. Architecture

Security overlays the 11.1 partition: authentication/authorisation gates at command/telemetry endpoints (mechanisms TBD, 17.7/17.8), integrity/protection wrappers on links and stored data (mechanisms TBD, 17.11), and key-management services supporting all protected paths (TBD). Threat coverage traces to Vol 17.2 (TBD).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Cryptographic algorithms, protocols, implementations, and key-management designs are TBD.

## 9. Interfaces

Interfaces to Vol 17 security services, link terminals, ground-station systems, and key-management infrastructure are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Security applies across all flight modes and ground operations, including degraded-link and loss-response operations per 11.9 and re-keying/revocation operations. Procedures are TBD.

## 11. Safety

Spoofed, altered, replayed, or unauthorised traffic is hazardous. Mitigation is via threat hooks (CSC-001), authentication/authorisation (CSC-002), key management (CSC-003), and degraded-link security behaviour (CSC-004), coordinated with Vol 17. No security or safety claim is made at this revision.

## 12. Performance

Security overhead and availability impacts are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis and later security and penetration testing of links and key management (detail TBD, Vol 17/19/33).

## 14. Risks

- Threat set incomplete; mitigation: Vol 17.2 hooks, TBD.
- Key-management complexity; mitigation: Vol 17 trade and analysis, TBD.
- Spectrum/regulatory constraints unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Threat hooks TBD; authentication/authorisation mechanisms TBD; key management TBD; degraded-link security behaviour TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1–11.11 links and consumers, Vol 17.2/17.7/17.8/17.11, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: communications-security design, ICDs, V&V cases. RTM: REQ-HFPX-CSC-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.12) |
