# 03.1 Airframe Architecture

**Document ID:** HFPX-STR-ARC-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the airframe structural architecture for HFP-X: structural decomposition, load-path ownership, and interfaces to dependent volumes. This revision establishes structure and traceability only; no geometry, sizing, or values are stated.

## 2. Scope

Covers Chapter 03.1 Airframe Architecture. Applies to the airframe structural system and its decomposition into primary, secondary, pilot load-bearing, propulsion-mount, lifting-surface, landing, joint, and material elements (Chapters 03.3–03.12). Load definition is owned by Chapter 03.13; strength, fatigue, damage tolerance, dynamics, and testing are owned by Chapters 03.14–03.20.

## 3. Applicable Documents

- HFPX-SYS-ARC-001 SAD, physical view (parent architecture)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent requirements, via SAD)
- Volume 06 aerodynamic loads inputs (TBD)
- Volume 03 Chapters 03.2–03.20 (subordinate structural documents, TBD)
- Interface register (TBD)

## 4. Definitions & Acronyms

- STR: structures domain, Volume 03
- SAD: System Architecture Description (HFPX-SYS-ARC-001)
- Load path: structural route by which applied loads are carried to reaction points
- TBD: to be determined; TBC: to be confirmed
- ISS-004: open issue governing airframe-concept trade

## 5. System Context

Airframe structure carries and reacts loads from lifting surfaces, propulsion mounts, pilot restraint, landing and ground handling, and transmits them through defined load paths. Context inputs: SYS-tier requirements via the SAD physical view; aerodynamic and inertial load inputs from Volume 06 (TBD); propulsion interface demands from Volume 04 (via Chapter 03.6); human-system interfaces from Volumes 10 and 12 (via Chapter 03.5).

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-SAR-001|The airframe structural decomposition shall be defined, identifying primary, secondary, and interface structures with ownership boundaries.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SAR-002|Each structural load path shall have a defined owner and interface points recorded in the interface register.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SAR-003|The airframe concept selection shall use the ISS-004 trade outcome as a recorded input.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SAR-004|All airframe structural interfaces shall be captured in the interface register.|SYS tier via SAD physical view|Inspection|
|REQ-HFPX-SAR-005|Airframe architecture completeness shall be verified by review against SYS-tier parents and subordinate chapter coverage.|SYS tier via SAD physical view|Inspection|

## 7. Architecture

Structural decomposition (TBD): primary structure (Chapter 03.3), secondary structure (Chapter 03.4), pilot load-bearing structure (Chapter 03.5), propulsion mounting structures (Chapter 03.6), wing / lifting-body structure (Chapter 03.7), landing / ground-handling structure (Chapter 03.8), fasteners and joints (Chapter 03.9), materials (Chapter 03.10), with loads, strength, fatigue, damage tolerance, dynamics, and testing addressed in Chapters 03.13–03.20. Load-path ownership boundaries are TBD and will be recorded with interface points. Concept selection follows the ISS-004 trade outcome.

## 8. Detailed Design

Not applicable at this revision. No geometry, member sizing, section properties, or construction detail is stated. Detailed decomposition and drawings are TBD.

## 9. Interfaces

Interfaces are TBD and will be recorded in the interface register. Expected interface groups: aerodynamic loads inputs from Volume 06 (TBD); propulsion interfaces via Chapter 03.6 to Volume 04; pilot/restraint interfaces via Chapter 03.5 to Volumes 10 and 12; landing and ground-handling interfaces via Chapter 03.8; materials and process interfaces via Chapter 03.10 to Volume 20.12. Interface methodology: name each interface, identify owner on each side, and record status in the register.

## 10. Operational Concept

The airframe architecture supports all flight and ground phases defined by the operational concept (TBD). Phase-to-structure mapping methodology: identify which structural elements react loads in each phase and record phase coverage by review. No phase-specific values are stated.

## 11. Safety

Structural safety methodology: allocate structural safety responsibilities to subordinate chapters (philosophy in Chapter 03.2; strength, fatigue, damage tolerance in Chapters 03.14–03.16); require failure-consequence classification of secondary structure (Chapter 03.4); maintain traceability to system safety analyses (Volume 13, TBD). No safety targets or values are stated.

## 12. Performance

Structural performance methodology only: define performance attributes (stiffness, strength, stability, durability behaviours) as TBD characteristics verified by analysis and test methodology in Chapters 03.13–03.20. No performance values are stated.

## 13. Verification & Validation

Verification by review at this revision: check decomposition completeness, load-path ownership recording, ISS-004 input capture, and interface-register coverage against Section 6. Later verification methodology: review of subordinate chapter artefacts, analysis review, inspection, and test witnessing per Chapters 03.13–03.20. No pass/fail values are stated.

## 14. Risks

- Decomposition without concept or load data remains paper architecture; mitigation: CONCEPT status explicit, ISS-004 outcome recorded as input when available
- Unowned load paths or interfaces; mitigation: ownership and register discipline per REQ-HFPX-SAR-002 and REQ-HFPX-SAR-004

## 15. Open Issues

- ISS-004 airframe-concept trade outcome
- Structural decomposition and load-path ownership (TBD)
- Interface register population (TBD)
- Volume 06 loads inputs (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-tier requirements via the SAD physical view, ISS-004 trade outcome, Volume 06 loads inputs (TBD), and subordinate Chapters 03.2–03.20.

## 18. Traceability

Parent: SYS tier via SAD physical view. Children: Chapters 03.2–03.20. RTM: REQ-HFPX-SAR-001..005 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 03.1) |
