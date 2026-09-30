# Helmet Power

**Document ID:** HFPX-HMI-PWR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the helmet power requirements for HFP-X (Chapter 10.16): power feeds, endurance, and loss-of-power behaviour. No feed definition, endurance value, load value, or behaviour timing is defined in this document.

## 2. Scope

Covers helmet power provision allocated from SYS-005 and STK-007, including feeds per Vol 15.10, endurance, and loss-of-power behaviour. Excludes vehicle power-system design (Vol 15 ownership), helmet communications implementation (Chapter 10.15), and environmental protection (Chapter 10.17). All feeds, capacities, loads, and behaviours are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-007 status/warning guidance, STK-002 controllability)
- HFPX-ARC-HUM-001 Human-System Architecture (REQ-HFPX-HSA-001 helmet integration)
- HFPX-SYS-HUM-001 Human Factors Requirements (REQ-HFPX-HUM-001 workload, REQ-HFPX-HUM-002 legibility)
- Vol 15.10 power feeds and interfaces (definitions TBD)
- Vol 30 human-factors principles (limits and methods TBD)

## 4. Definitions & Acronyms

- HPO: helmet-power requirement tier; ID prefix `REQ-HFPX-HPO-NNN`
- Power feeds: electrical supplies to helmet functions with defined sources and characteristics (feeds TBD per Vol 15.10)
- Endurance: duration for which helmet functions remain available under defined conditions (value TBD)
- Loss-of-power behaviour: defined helmet and HMI state upon degradation or loss of supply (behaviour TBD)
- TBD: to be defined. No values stated.

## 5. System Context

The helmet power function distributes Vol 15.10 feeds to helmet consumers (display, audio, tracking, comms, and processing clients, all TBD), sustains them for the defined endurance, and enforces defined loss-of-power behaviour preserving warning-relevant presentation so far as practicable (provisions TBD).

```text
[Vol 15.10 feeds (TBD)] --> [Helmet power distribution + endurance provision (TBD)] --> [Helmet consumers display/audio/comms (TBD)]
   with [loss-of-power behaviour (TBD)] | constrained by [HUM-001/002 (TBD, Vol 30)]
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HPO-001 | The helmet shall accept defined power feeds with defined characteristics per Vol 15.10 (feeds and characteristics TBD). | SYS-005, HSA-001 | Inspection + Demonstration (TBD) |
| REQ-HFPX-HPO-002 | The helmet power function shall sustain defined helmet functions for a defined endurance under defined conditions (functions, endurance, and conditions TBD). | STK-007, SYS-005 | Demonstration + Test (TBD) |
| REQ-HFPX-HPO-003 | The helmet shall implement defined loss-of-power behaviour including defined annunciation and degraded states (behaviour and states TBD). | STK-002, SYS-005, HUM-002 | Demonstration (TBD) |
| REQ-HFPX-HPO-004 | Each helmet-power requirement in this document shall have a defined verification method and pass criteria (methods and criteria TBD). | SYS-005 | Inspection (TBD) |

No voltage, current, capacity, load, endurance, or timing value in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: HPO-001 → feed-acceptance function; HPO-002 → endurance-provision function; HPO-003 → loss-of-power handling function; HPO-004 → V&V thread. Authoritative allocation lives in Vol 10/15 integration views; this section states derivation intent only. Converters, storage, switching, and load-shedding implementations are TBD.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Feed circuitry, storage selection, distribution topology, shedding logic, and annunciation implementations are TBD.

## 9. Interfaces

- Vol 15.10 feed interface (sources, connectors, characteristics): TBD.
- Helmet-consumer distribution interface (loads and priorities): TBD.
- Loss-of-power annunciation interface (HMI warning/alert clients): TBD.
- Environmental hosting interface (Chapter 10.17 thermal/sealing constraints): TBD.
- Formal ICDs are TBD.

## 10. Operational Concept

Requirements are exercised through nominal powered-operation threads, endurance threads, and loss-of-power threads (degradation, shedding, annunciation, recovery) under controlled conditions. Load profiles, durations, and crew procedures are TBD.

## 11. Safety

Unannunciated loss of helmet functions, in particular warning presentation, is hazardous. Mitigations required (all TBD): defined feeds (HPO-001), defined endurance (HPO-002), defined loss-of-power behaviour with annunciation (HPO-003). No endurance, availability, or integrity claim is made at this revision.

## 12. Performance

Intentionally TBD. No endurance duration, load, capacity, efficiency, or switchover-time value is stated. Future revisions reference budgets and models, never invented figures.

## 13. Verification & Validation

HPO-004 establishes the thread: each HPO requirement maps to at least one V&V case (methods stated in section 6 table). Intended strategy is inspection of feed definitions plus demonstration and test of endurance and loss-of-power behaviour on representative rigs (profiles, conditions, and pass criteria TBD). No V&V is complete at this revision.

## 14. Risks

- Vol 15.10 feed definitions unavailable → helmet power requirements unquantifiable; mitigation: feed requirement held as TBD placeholder.
- Load set and mission-duration context undefined → endurance unprovable; mitigation: endurance held as TBD with Vol 15/30 dependency explicit.
- Loss-of-power behaviour undefined without shedding-priority and alert-coordination input; mitigation: behaviour held as TBD provision.

## 15. Open Issues

- Power feeds and characteristics TBD per Vol 15.10.
- Sustained functions, endurance, and conditions TBD.
- Loss-of-power behaviour, degraded states, and annunciation TBD.
- Verification methods, rigs, profiles, and pass criteria TBD per requirement.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-005 policy stability, STK-002/007 needs, HSA-001 integration view, HUM-001/002 human-factors inputs, Vol 15.10 feed definitions, Vol 30 principles, coordination with Chapters 10.11/10.12/10.17, and V&V planning.

## 18. Traceability

Parents: STK-002, STK-007, SYS-005, HSA-001, HUM-001, HUM-002; Vol 15.10 and Vol 30 hooks. Children: Vol 10/15 power implementations, shedding/annunciation designs, V&V cases, RTM rows. RTM: REQ-HFPX-HPO-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.16, 4 requirements) |
