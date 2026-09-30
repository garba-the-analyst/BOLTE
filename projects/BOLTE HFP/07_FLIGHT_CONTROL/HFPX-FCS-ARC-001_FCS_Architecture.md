# FCS Architecture

**Document ID:** HFPX-FCS-ARC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the FCS architecture for HFP-X (Chapter 07.2): inner/outer loop partition, mode supervisor with switching/abort, sensor-fusion input interface, safety-computer monitoring path, and software/hardware allocation. No control-law values are defined.

## 2. Scope

Covers FCS structural decomposition and allocation. Law forms, gains, bandwidths, margins, rates, limits, thresholds, and allocation matrices are TBD. No component selected.

## 3. Applicable Documents

- HFPX-FCS-REQ-001 (REQ-HFPX-FCR-001..006); HFPX-ARC-CTL-001 (REQ-HFPX-CTL-001/002)
- HFPX-SYS-ARC-001 SAD (ARC-004); Vol 08/16 (compute); Vol 19 (SIL/HIL)
- Companion Vol 07 docs: INP/LAW/ATT/ROL/PIT; ISS-006 (authority)

## 4. Definitions & Acronyms

- Inner/outer loop: stabilisation (inner) and guidance/command-tracking (outer) partition (allocation TBD).
- Mode supervisor: regime detection, law-set selection, switching, and abort logic (all TBD).
- Sensor-fusion input interface: navigation/estimate inputs to FCS (signals TBD).
- Monitoring path: independent safety-computer observation/intervention path (authority TBD).
- SW/HW allocation: assignment of FCS functions to software and computing hardware (TBD, Vol 08/16).

## 5. System Context

FCS architecture implements FCR-001..005 within the control architecture view (CTL-001/002). It consumes shaped pilot/operator commands and fused estimates, executes the selected law set, allocates to effectors, and exposes health/faults to the safety path.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FCA-001 | The FCS architecture shall partition inner-loop stabilisation and outer-loop command-tracking functions with defined responsibilities and interfaces (partition TBD). | ARC-004, CTL-001 | Analysis + SIL (TBD) |
| REQ-HFPX-FCA-002 | The FCS shall provide a mode supervisor that selects hover/transition/cruise law sets and executes switching and abort logic (detection, hysteresis, thresholds, and abort criteria TBD). | ARC-004, CTL-001 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FCA-003 | The FCS shall provide a defined sensor-fusion input interface for navigation estimates (signals, rates, integrity, and fallback TBD). | ARC-004, CTL-002 | Analysis + SIL (TBD) |
| REQ-HFPX-FCA-004 | The FCS architecture shall provide a safety-computer monitoring path with defined observation and intervention interfaces (authority and latencies TBD). | ARC-004, CTL-002 | Analysis + HIL (TBD) |
| REQ-HFPX-FCA-005 | FCS software and hardware allocation, including redundancy and determinism provisions, shall be defined (allocation TBD, Vol 08/16). | ARC-004 | Analysis (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Text architecture diagram:

```
                    +-----------------------------+
                    |   Sensor Fusion Input I/F   |
                    |        (FCA-003, TBD)       |
                    +-------------+---------------+
                                  v
[Pilot Input (INP)] --> [Outer Loop: command tracking (TBD)] --> [Inner Loop: stabilisation (TBD)] --> [Mode Supervisor: select/switch/abort (TBD)] --> [Allocation/Mixing (TBD)] --> Effectors
                                  ^                                                                          |
                                  |                                                     [Health/Fault] --> | --> Safety Computer Monitoring Path (FCA-004, TBD)
                                  +-- SW/HW Allocation incl. redundancy/determinism (FCA-005, TBD, Vol 08/16) --+
```

Inner/outer responsibilities, supervisor states/transitions, input signal lists, monitoring authority, and SW/HW mapping are TBD. Primary path remains deterministic and bounded per FCR-002 (budgets TBD).

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Loop structures, supervisor state machine, signal definitions, and allocation design are TBD.

## 9. Interfaces

- Inner/outer loop internal interfaces: TBD.
- Sensor-fusion input ICD: TBD.
- Allocation/mixing to propulsion ICD: TBD (owner TBD).
- Safety-computer monitoring ICD: TBD.
- Compute platform (Vol 08/16) interface: TBD.

## 10. Operational Concept

Architecture supports hover/transition/cruise operations; supervisor manages nominal switching and abort-to-safe states (states and criteria TBD). Degraded modes hand over to safety path per CONOPS.

## 11. Safety

Unpartitioned loops, uncommanded switching, corrupt fusion inputs, or ineffective monitoring are hazardous. Mitigations required (all TBD): defined partition (FCA-001), supervised switching/abort (FCA-002), qualified input interface with fallback (FCA-003), independent monitoring path (FCA-004), and deterministic redundant allocation (FCA-005). No safety claim is made.

## 12. Performance

Loop timing, tracking, switching transients, throughput, and latency budgets are TBD. No performance value is stated.

## 13. Verification & Validation

Verified by analysis (partition, supervisor logic) and SIL/HIL (Vol 19); fault-injection for switching/monitoring (methods TBD). Pass criteria TBD per requirement.

## 14. Risks

- Partition/supervisor unstable without law trades; mitigation: hold as TBD structure, refine with Vol 07/19.
- Fusion-interface and monitoring-authority undefined; mitigation: ICD stubs explicit, fallback TBD.
- SW/HW allocation unknown (Vol 08/16); mitigation: allocation TBD, determinism verified later by SIL/HIL.

## 15. Open Issues

- Inner/outer partition TBD; supervisor states/thresholds/abort criteria TBD; fusion signals and fallback TBD; monitoring authority TBD; SW/HW allocation TBD.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on FCR-001..006, CTL-001/002, ARC-004, Vol 08/16 compute, fusion/navigation source, safety architecture, Vol 19 rigs.

## 18. Traceability

Parents: ARC-004, CTL-001, CTL-002. Children: INP/LAW/axis detailed designs; SW/HW allocation in Vol 08/16; V&V cases. RTM: REQ-HFPX-FCA-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.2) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
