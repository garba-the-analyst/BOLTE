# Helmet Communications

**Document ID:** HFPX-HMI-COM-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the helmet communications requirements for HFP-X (Chapter 10.15): voice/data links, emergency priority, and redundancy. No link definition, priority rule, redundancy scheme, or performance value is defined in this document.

## 2. Scope

Covers helmet voice/data communications allocated from SYS-005 and STK-007, including link provision per Vol 11, emergency priority per Vol 13.17, and redundancy. Excludes ground-station design (Vol 11 ownership), warning/alert content (Chapters 10.11/10.12), voice-command recognition (Chapter 10.13), and helmet power implementation (Chapter 10.16). All links, rules, schemes, and thresholds are TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent REQ-HFPX-SYS-005 operator-interface policy)
- HFPX-SYS-STK-001 Stakeholder Requirements (STK-007 status/warning guidance, STK-002 controllability)
- HFPX-ARC-HUM-001 Human-System Architecture (REQ-HFPX-HSA-001 helmet integration)
- HFPX-SYS-HUM-001 Human Factors Requirements (REQ-HFPX-HUM-001 workload, REQ-HFPX-HUM-002 legibility)
- Vol 11 communications links (voice/data definitions TBD)
- Vol 13.17 emergency-priority provisions (rules TBD)
- Vol 30 human-factors principles (limits and methods TBD)

## 4. Definitions & Acronyms

- HCO: helmet-communications requirement tier; ID prefix `REQ-HFPX-HCO-NNN`
- Voice/data links: helmet bearers for voice and data exchange with defined endpoints (links TBD per Vol 11)
- Emergency priority: pre-emption/ordering favouring emergency traffic per Vol 13.17 (rules TBD)
- Redundancy: alternate paths or means sustaining defined communications under defined faults (scheme TBD)
- TBD: to be defined. No values stated.

## 5. System Context

The helmet communications function connects helmet audio/data endpoints to vehicle and ground-station counterparts via Vol 11 links, applies emergency priority per Vol 13.17, and sustains defined exchanges via redundancy provisions. It carries warning/alert voice and data content owned by Chapters 10.11/10.12 without defining that content.

```text
[Helmet audio/data endpoints (TBD)] <--Vol 11 links (TBD)--> [Vehicle / ground station (TBD)] with [emergency priority Vol 13.17 (TBD)] + [redundancy (TBD)]
   carries [10.11/10.12 warning/alert content (TBD)] | constrained by [HUM-001/002 (TBD, Vol 30)]
```

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-HCO-001 | The helmet shall provide defined voice and data links with defined endpoints per Vol 11 (links and endpoints TBD). | STK-007, SYS-005, HSA-001 | Demonstration (TBD) |
| REQ-HFPX-HCO-002 | Emergency communications shall take defined priority by defined means per Vol 13.17 (traffic classes, rules, and means TBD). | STK-007, SYS-005 | Demonstration (TBD) |
| REQ-HFPX-HCO-003 | The helmet communications function shall provide defined redundancy sustaining defined exchanges under defined faults (scheme, exchanges, and faults TBD). | SYS-005, HSA-001 | Analysis + Demonstration (TBD) |
| REQ-HFPX-HCO-004 | Each helmet-communications requirement in this document shall have a defined verification method and pass criteria (methods and criteria TBD). | SYS-005 | Inspection (TBD) |

No link, frequency, rate, range, priority rule, or redundancy value in this document is approved; all are TBD.

## 7. Architecture

Parent allocation: HCO-001 → link-provision function; HCO-002 → priority function; HCO-003 → redundancy function; HCO-004 → V&V thread. Authoritative allocation lives in Vol 10/11 integration views; this section states derivation intent only. Bearers, routers, switches, and terminals are TBD.

## 8. Detailed Design

Not applicable at Tranche 6 draft level. Link selections, protocols, priority implementations, redundancy topologies, and terminal designs are TBD.

## 9. Interfaces

- Vol 11 link interface (bearers, protocols, endpoints): TBD.
- Emergency-priority interface (Vol 13.17 rules and signalling): TBD.
- Audio/data endpoint interface (helmet audio system, display/data clients): TBD.
- Power/environmental hosting interface (Chapters 10.16/10.17 constraints): TBD.
- Formal ICDs are TBD.

## 10. Operational Concept

Requirements are exercised through nominal voice/data exchange threads, emergency-priority threads, and loss-of-path threads (redundancy takeover) under controlled conditions. Exchange sequences, priority assertions, and failover procedures are TBD.

## 11. Safety

Loss, blocking, or delay of emergency communications is hazardous. Mitigations required (all TBD): defined links (HCO-001), emergency priority (HCO-002), redundancy (HCO-003). No availability, integrity, or latency claim is made at this revision. Priority rules await Vol 13.17 output by change record.

## 12. Performance

Intentionally TBD. No data rate, range, latency, availability, or audio-quality value is stated. Future revisions reference budgets and models, never invented figures.

## 13. Verification & Validation

HCO-004 establishes the thread: each HCO requirement maps to at least one V&V case (methods stated in section 6 table). Intended strategy is demonstration of nominal exchanges, priority assertion, and redundancy takeover on representative rigs (scenarios, faults injected, and pass criteria TBD). No V&V is complete at this revision.

## 14. Risks

- Vol 11 link definitions unavailable → helmet endpoints unquantifiable; mitigation: link requirement held as TBD placeholder.
- Emergency-priority rules undefined (Vol 13.17) → pre-emption behaviour unknown; mitigation: priority requirement held as TBD with Vol 13 dependency explicit.
- Redundancy scheme undefined without fault-set and Vol 11 topology; mitigation: redundancy held as TBD provision with analysis thread.

## 15. Open Issues

- Voice/data links and endpoints TBD per Vol 11.
- Emergency-priority classes, rules, and means TBD per Vol 13.17.
- Redundancy scheme, sustained exchanges, and fault set TBD.
- Verification methods, rigs, scenarios, and pass criteria TBD per requirement.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-005 policy stability, STK-002/007 needs, HSA-001 integration view, HUM-001/002 human-factors inputs, Vol 11 link definitions, Vol 13.17 priority provisions, Vol 30 principles, and V&V planning.

## 18. Traceability

Parents: STK-002, STK-007, SYS-005, HSA-001, HUM-001, HUM-002; Vol 11, Vol 13.17, and Vol 30 hooks. Children: Vol 10/11 link implementations, priority/redundancy designs, V&V cases, RTM rows. RTM: REQ-HFPX-HCO-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 10.15, 4 requirements) |
