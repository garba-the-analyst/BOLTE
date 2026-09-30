# Data Buses

**Document ID:** HFPX-AVN-DBS-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 5 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define HFP-X avionics data-bus principles (Chapter 08.6): bus/protocol classes, redundancy principles, bandwidth/latency budgets, and verification approach. No protocols or topologies selected.

## 2. Scope

Covers bus/protocol class definitions, redundancy principles, budget placeholders, and verification approach. Excludes protocol selection, topology design, wiring, and quantitative values (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005)
- HFPX-SYS-ARC-001 SAD (AVN, HWA, SWA, DAT views)
- HFPX-AVN-ARC-001 Avionics Architecture (Chapter 08.1)
- ICDs (bus definitions deferred)

## 4. Definitions & Acronyms

- Data bus: shared communication path between avionics nodes.
- Protocol class: role-based category of communication protocols without selection.
- Redundancy: provision of alternate paths or means to sustain communication.
- Budget: placeholder allocation for bandwidth/latency behaviour without values.

## 5. System Context

Data buses interconnect sensors, computers, interface nodes, and ground/test attachments across flight and maintenance states. Physical media, topologies, and mechanisms are TBD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VDB-001 | The avionics data design shall define bus and protocol classes without selection (classes TBD). | REQ-HFPX-SYS-002; SAD DAT view | Inspection |
| REQ-HFPX-VDB-002 | The avionics data design shall define redundancy for data buses (topology and mechanisms TBD). | REQ-HFPX-SYS-003; SAD AVN view | Analysis |
| REQ-HFPX-VDB-003 | The avionics data design shall define bandwidth and latency budgets for data buses (values TBD). | REQ-HFPX-SYS-002; SAD DAT view | Analysis |
|REQ-HFPX-VDB-004|The avionics data-bus definitions shall be verified (method and evidence TBD).|REQ-HFPX-SYS-005; SAD AVN view|Inspection|

## 7. Architecture

Bus concept (details TBD): role-based classes, redundancy principles, and budget placeholders. No protocols, topologies, media, or values selected.

## 8. Detailed Design

Not applicable at this revision. Protocol selection, topology, wiring, and packaging are deferred to later tranches and ICDs.

## 9. Interfaces

Bus interfaces: physical/logical attachments, node endpoints, gateway exchanges, and test access. Definitions are TBD in ICDs.

## 10. Operational Concept

Buses support flight modes plus built-in test, degraded/redundant, and maintenance states. Behaviour in degraded modes is TBD.

## 11. Safety

Class discipline, redundancy principles, and budget placeholders support parent safety intent. No safety values stated.

## 12. Performance

Bandwidth, latency, and availability details are TBD. No values stated.

## 13. Verification & Validation

Verified by inspection (class definitions), analysis (redundancy and budget arguments), and review of definitions. Integration test is deferred to later tranches.

## 14. Risks

- Protocol proliferation across nodes; mitigation: class discipline with selection gate.
- Budget shortfalls discovered late; mitigation: early budget placeholders with analysis thread.

## 15. Open Issues

Bus classes, redundancy details, budget values, and verification evidence are all TBD.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS, SAD AVN/HWA/SWA/DAT views, Chapter 08.1 architecture, and ICDs.

## 18. Traceability

Parents: REQ-HFPX-SYS-002, REQ-HFPX-SYS-003, REQ-HFPX-SYS-005; SAD AVN/HWA/SWA/DAT views. Children: Vol 08 bus detail and ICDs. RTM: REQ-HFPX-VDB-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 5 draft, not baselined. Chapter 08.6.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 5 draft (Chapter 08.6) |
