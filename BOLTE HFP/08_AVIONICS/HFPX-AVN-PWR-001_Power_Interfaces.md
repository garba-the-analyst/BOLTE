# Power Interfaces

**Document ID:** HFPX-AVN-PWR-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X avionics power interfaces (Chapter 08.7): avionics power feeds, brownout/switch-over behaviour, and power-monitoring hooks. No voltages, currents, or topologies selected.

## 2. Scope

Covers avionics power-feed definition, brownout/switch-over behaviour, and power-monitoring hooks interfacing to Vol 15 distribution. Excludes power generation, distribution design, wiring sizing, and quantitative electrical values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002/003)
- HFPX-ARC-AVN-001 Avionics Architecture
- Vol 15 (power distribution detail)
- Vol 13 (safety analyses: FHA/FMEA hooks)

## 4. Definitions & Acronyms

- Power feed: electrical supply path from distribution to an avionics load.
- Brownout: undervoltage condition with behaviour TBD.
- Switch-over: transfer between power sources or feeds with behaviour TBD.
- Power monitoring: observation of power-interface state feeding health/fault logic.

## 5. System Context

Avionics power interfaces connect avionics loads to Vol 15 distribution across all flight and maintenance states. They bound feeds, returns, grounding, and monitoring hooks; generation and distribution internals are owned in Vol 15 (details TBD).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-VPI-001|The avionics power interfaces shall define avionics power feeds and returns (details TBD, hooks to Vol 15).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; SFA tier|Inspection|
|REQ-HFPX-VPI-002|The avionics power interfaces shall define brownout and switch-over behaviour (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; FHA/FMEA hooks; SFA tier|Inspection|
|REQ-HFPX-VPI-003|The avionics power interfaces shall define power-monitoring hooks feeding health and fault logic (details TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks|Inspection|
|REQ-HFPX-VPI-004|The verification approach for avionics power interfaces shall be defined (TBD).|HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; SFA tier|Inspection|

## 7. Architecture

Power-interface classes named by load role with feeds, returns, and monitoring hooks identified to Vol 15. Brownout/switch-over behaviour owned at interface level; source selection and redundancy owned in Vol 15. No electrical values or topologies stated.

## 8. Detailed Design

Not applicable at this revision. Feed pin-outs, wiring, protection devices, and component selections are TBD in Vol 15 and ICDs. No parts selected.

## 9. Interfaces

Avionics power interfaces: feeds/returns/grounding (Vol 15), monitoring outputs to health/fault logic (Ch 08.10/08.11), and ground test/servicing hooks. Definitions TBD in ICDs.

## 10. Operational Concept

Power interfaces support all flight modes plus BIT, degraded/redundant, and maintenance states. Monitoring hooks remain available in degraded modes to support fault response (details TBD).

## 11. Safety

Power-interface faults feed Vol 13 FHA/FMEA. Fail-safe behaviour on loss or degradation of feeds is TBD. No safety values stated.

## 12. Performance

Voltage, current, transient, and availability budgets are TBD. Budget holders: power (Vol 15), avionics (Vol 08), safety (Vol 13). No values stated.

## 13. Verification & Validation

Verification approach TBD. Expected later by inspection (feed definitions), analysis (brownout/switch-over behaviour), and integration test (Vol 19). Validation deferred.

## 14. Risks

- Feed-definition gaps driving Vol 15 rework; mitigation: interface freeze gate at PDR.
- Unobserved power anomalies masking faults; mitigation: monitoring-coverage analysis tied to Vol 13 FMEA.

## 15. Open Issues

Avionics power-feed inventory, brownout/switch-over behaviour, monitoring-hook definitions, and verification approach all TBD. Vol 15 hooks incomplete.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on power design (Vol 15), avionics architecture (HFPX-ARC-AVN-001), health/fault logic (Ch 08.10/08.11), and safety analyses (Vol 13).

## 18. Traceability

Parents: HFPX-SYS-REQ-001 REQ-HFPX-SYS-002/003; VAA tier; FHA/FMEA hooks; SFA tier. Children: Vol 15 detail docs, ICDs. RTM: REQ-HFPX-VPI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.7.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.7) |
