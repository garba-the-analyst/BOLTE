# Data Architecture

**Document ID:** HFPX-ARC-DAT-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X data architecture view (Chapter 02.11): sensor→fusion→control/safety information flows, bus/protocol classes, time-sync and logging principles, and integrity/redundancy approach.

## 2. Scope

Covers onboard and ground-link data flows for the production-aircraft concept. Bus/protocol selection, timing values, and storage capacities are TBD. No component selected.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001..008); HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-001..005)
- Vol 08.6 (buses/protocols), 08.16 (time sync), 08.17 (logging); Vol 16 (computing); Vol 11 (comms)
- HFP prompt §11 (data view)

## 4. Definitions & Acronyms

- Fusion: combining sensor outputs into navigation/health estimates.
- Time sync: common time reference across distributed compute/sensing (mechanism TBD).
- Logging: recording flight/safety data for analysis (scope TBD).

## 5. System Context

Data architecture connects sensors → fusion → FCS/safety computer → actuators, with branches to helmet display, logging, and ground telemetry. All rates, latencies, and capacities TBD.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-DAT-001 | The architecture shall define sensor→fusion→control/safety data flows with producers, consumers, and criticality (details TBD). | Analysis + Inspection |
| REQ-HFPX-DAT-002 | Bus and protocol classes for safety-critical vs non-critical traffic shall be defined per Vol 08.6 (selections TBD). | Inspection |
| REQ-HFPX-DAT-003 | Time-synchronisation and logging principles shall follow Vol 08.16/08.17 (mechanisms and capacities TBD). | Analysis |
| REQ-HFPX-DAT-004 | Data-integrity and redundancy approach (checking, voting, backup paths — TBD) shall be defined for safety-critical flows. | Analysis |

## 7. Architecture

Flow structure: sensors (SYS-08) → fusion/estimation → navigation → FCS (primary) and safety computer (parallel); health monitoring → fault detection → mitigation/alerting; logging tap to onboard recorder; telemetry tap to comms/ground station. Traffic classes (safety-critical deterministic vs best-effort, TBD) map to bus/protocol classes per Vol 08.6 (selections TBD). Time-sync (08.16) provides a common reference (protocol TBD); logging (08.17) captures flight, safety, and maintenance data (scope TBD). Integrity/redundancy (checksums, redundancy, voting — TBD) protects safety-critical flows; AI data use remains advisory-only per ARC-002.

## 8. Detailed Design

Not applicable at Tranche 2 draft level. Bus selections, message sets, timing budgets, and recorder sizing are TBD (Vol 08/16).

## 9. Interfaces

Data interfaces (sensor buses, compute interconnects, telemetry feeds) are TBD. Each shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Data flows support all 15 flight modes; degraded-data behaviour (loss, staleness, corruption — TBD) hands over to safety/recovery views per CONOPS. Detail per Vol 08/11.

## 11. Safety

Corrupted, stale, or lost safety-critical data is hazardous: integrity checks and redundant paths (DAT-004) plus independent safety-path data (SFA-001) mitigate it. No integrity claim is made; all thresholds and mechanisms TBD pending Vol 13/16 analysis.

## 12. Performance

Bandwidth, latency, jitter, sync-accuracy, and logging-capacity budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by analysis (flow completeness, timing feasibility) and inspection (message/ICD coverage). Later validated by SIL/HIL traffic and flight logging (Vol 19/33). All methods TBD in detail.

## 14. Risks

- Bus/protocol selection delay blocking ICDs; mitigation: class-level architecture now, selection by PDR.
- Logging overload or time-skew masking faults; mitigation: principles per 08.16/08.17, budgets TBD.

## 15. Open Issues

Bus/protocol selections TBD; time-sync mechanism TBD; logging scope/capacity TBD; integrity/redundancy scheme TBD; degraded-data behaviour TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-001..005), Vol 08 (avionics/compute), Vol 16 (software), Vol 11 (comms), safety view (02.10), control view (02.12).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (esp. ARC-002, ARC-003, ARC-005); tier inputs FUN/SAF as allocated. Children: Vol 08 designs, ICDs, V&V cases. RTM: REQ-HFPX-DAT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.11) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
