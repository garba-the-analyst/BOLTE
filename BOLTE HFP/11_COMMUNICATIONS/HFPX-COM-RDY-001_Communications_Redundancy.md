# Communications Redundancy

**Document ID:** HFPX-COM-RDY-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X communications redundancy for Volume 11, Chapter 11.8: redundancy approach, independence, and analysis hooks.

## 2. Scope

Covers redundancy for safety-critical pilot, ground, telemetry, command, emergency, and data links. Redundancy schemes, independence claims, hardware, and performance values are TBD. Spectrum and regulatory items are TBD (Vol 25 hooks).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-005); mission requirements (REQ-HFPX-MIS-004); operations concept (REQ-HFPX-OPC-003); stakeholder requirements (REQ-HFPX-STK-007)
- HFPX-ARC-COM-001 SAD communications view; HFPX-COM-ARC-001 (11.1)
- Vol 11 (11.1–11.7 links, 11.9 loss management); Vol 13 (safety); Vol 17 (cybersecurity); Vol 25 (spectrum/regulatory)

## 4. Definitions & Acronyms

- Redundancy: provision of alternate communications paths for safety-critical traffic (approach TBD).
- Independence: freedom from common-cause failure between redundant paths (claims TBD).
- FTA: fault-tree analysis supporting redundancy claims (hooks TBD).

## 5. System Context

Redundancy overlays the 11.1 architecture and protects safety-critical traffic across pilot, ground, telemetry, command, emergency, and data links. It coordinates with loss management (11.9) and safety analysis (Vol 13) (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-CRD-001 | The redundancy approach for safety-critical communications links, including protected traffic classes, shall be defined (approach TBD). | REQ-HFPX-SYS-005 | Inspection |
| REQ-HFPX-CRD-002 | Independence between redundant communications paths, including common-cause considerations, shall be defined (claims TBD). | REQ-HFPX-SYS-005 | Inspection |
| REQ-HFPX-CRD-003 | Redundancy switchover and reversion behaviour, coordinated with 11.9 loss management, shall be defined (behaviour TBD). | REQ-HFPX-OPC-003 | Test |
| REQ-HFPX-CRD-004 | FTA hooks supporting communications redundancy claims per Vol 13 shall be defined (scope TBD). | REQ-HFPX-SYS-005 | Inspection |

## 7. Architecture

Redundant paths (number and diversity TBD) protect safety-critical traffic within the 11.1 partition. Switchover/reversion logic coordinates with 11.9 loss detection and response (logic TBD). Independence provisions address antennas, terminals, spectra, power, and routing (provisions TBD, spectrum hooks to Vol 25).

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Redundant hardware, spectra, and switchover implementations are TBD.

## 9. Interfaces

Interfaces between primary and alternate paths, monitors, and voters/selectors are TBD. Each shall be captured in an ICD before CDR (detail TBD).

## 10. Operational Concept

Redundant links support all flight modes and ground operations; crews/operators are annunciated on switchover per 11.9 concepts (details TBD). Procedures are TBD.

## 11. Safety

Common-cause loss of redundant links is hazardous. Mitigation is via defined redundancy approach (CRD-001), independence (CRD-002), switchover behaviour (CRD-003), and FTA hooks (CRD-004), plus loss management (11.9). No redundancy or availability claim is made at this revision.

## 12. Performance

Redundancy availability and switchover-timing budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verification methods are TBD. Expected methods include review/analysis (including FTA per Vol 13) and later redundancy and switchover testing, including fault injection (detail TBD, Vol 19/33).

## 14. Risks

- Independence unproven; mitigation: FTA and common-cause analysis, TBD.
- Spectrum/regulatory constraints on alternate paths unknown; mitigation: Vol 25 trade and TBD licensing path.

## 15. Open Issues

Redundancy approach TBD; independence claims TBD; switchover behaviour TBD; FTA scope TBD; spectrum/licensing TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, REQ-HFPX-STK-007, SAD communications view (HFPX-ARC-COM-001), 11.1 architecture, 11.2–11.7 links, 11.9 loss management, Vol 13 (safety/FTA), Vol 17, Vol 25 (spectrum/regulatory).

## 18. Traceability

Parents: REQ-HFPX-SYS-005, REQ-HFPX-MIS-004, REQ-HFPX-OPC-003, SAD communications view (HFPX-ARC-COM-001), REQ-HFPX-STK-007. Children: redundancy design, FTA cases, ICDs, V&V cases. RTM: REQ-HFPX-CRD-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 11.8) |
