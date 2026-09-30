# Communications Architecture

**Document ID:** HFPX-ARC-COM-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X communications architecture view (Chapter 02.13): pilot/ground/telemetry/command links, loss-of-link behaviour, redundancy, and security hooks.

## 2. Scope

Covers air-ground and onboard RF links for the production-aircraft concept. Frequencies, waveforms, ranges, and capacities are TBD. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001..008); HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-001..005)
- Vol 11 (communications; loss-of-link 11.9); Vol 17 (cybersecurity); Vol 21 (ground station)
- HFP prompt §11 (comms view)

## 4. Definitions & Acronyms

- Command link: ground/pilot commands to vehicle (details TBD).
- Telemetry link: vehicle-to-ground status/health data (details TBD).
- Loss-of-link: loss of command/telemetry connectivity (behaviour TBD, Vol 11.9).

## 5. System Context

Comms architecture links pilot, vehicle, and ground station/operations: command uplink, telemetry downlink, and pilot voice/data paths. All link parameters and coverage TBD.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-COM-001 | Pilot, ground, telemetry, and command links shall be defined with roles and criticality (parameters TBD). | Inspection |
| REQ-HFPX-COM-002 | Loss-of-link behaviour shall be defined per Vol 11.9 (behaviour TBD, including autonomous/safety handover). | Analysis + Test |
| REQ-HFPX-COM-003 | Redundancy for safety-critical links shall be defined (scheme TBD). | Analysis |
| REQ-HFPX-COM-004 | Security hooks per Vol 17 (authentication, integrity, key management — TBD) shall be applied to command and telemetry links. | Analysis |

## 7. Architecture

Link classes: pilot link (voice/data, TBD), command uplink (vehicle control, TBD), telemetry downlink (health/status, TBD), ground-network extension (TBD). Loss-of-link logic (Vol 11.9, behaviour TBD) escalates from link re-establishment to safety-path stabilisation and recovery handover. Redundant paths (dual links, fallback channels — TBD) protect safety-critical traffic. Security (Vol 17) wraps command/telemetry with authentication and integrity (mechanisms TBD); AI has no command-link authority per ARC-002.

## 8. Detailed Design

Not applicable at Tranche 2 draft level. Link budgets, spectra, hardware, and protocols are TBD (Vol 11).

## 9. Interfaces

RF interfaces (antennas, terminals, ground station) and data handoffs to avionics/logging are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Links support all flight modes and ground operations; degraded/lost-link procedures follow CONOPS and Vol 11.9. Beyond-line-of-sight and range rules TBD.

## 11. Safety

Lost, spoofed, or corrupted command link is hazardous: defined loss-of-link behaviour (COM-002), redundancy (COM-003), and Vol 17 security (COM-004) plus safety-path independence (ARC-003) mitigate it. No link-availability or security claim is made; all behaviours TBD pending Vol 11/13/17 analysis.

## 12. Performance

Range, availability, latency, throughput, and handover-time budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by analysis (link budgets, loss-of-link logic) and inspection (security hooks). Later validated by range/HIL and flight comms testing (Vol 19/33). Methods TBD in detail.

## 14. Risks

- Spectrum/regulatory constraints unknown; mitigation: Vol 11 trade, TBD licensing path.
- Security-link complexity vs latency; mitigation: Vol 17 hooks sized by analysis, TBD.

## 15. Open Issues

Link parameters TBD; loss-of-link behaviour TBD; redundancy scheme TBD; security mechanisms TBD; spectrum/licensing TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-001..005), Vol 11 (comms), Vol 17 (cybersecurity), Vol 21 (ground station), safety view (02.10), data view (02.11).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (esp. ARC-002, ARC-003, ARC-005); tier inputs FUN/SAF as allocated. Children: Vol 11 designs, ICDs, V&V cases. RTM: REQ-HFPX-COM-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.13) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
