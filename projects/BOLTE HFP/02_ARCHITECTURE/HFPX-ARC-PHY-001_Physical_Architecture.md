# Physical Architecture

**Document ID:** HFPX-ARC-PHY-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X physical architecture (Chapter 02.3): the modular physical decomposition and the principles governing physical integration. Establishes the structure into which functions are allocated without fixing geometry or values.

## 2. Scope

Covers physical modules (propulsion clusters, airframe/lifting body, avionics/compute, HMI, ground), mounting and load-path principles, and the physical interface register. Excludes positions, masses, dimensions and material selections (all TBD).

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parent requirements REQ-HFPX-SYS-001..008)
- HFPX-SYS-ARC-001 SAD (parent requirements REQ-HFPX-ARC-001..005)
- HFP prompt §§11–13; Vol 03 (airframe), Vol 08 (avionics), Vol 10/12 (HMI)

## 4. Definitions & Acronyms

- Module: a physically separable assembly with defined mechanical/electrical/data interfaces.
- Load path: structural route carrying propulsion/aero/landing loads into the airframe.
- Representativeness: MVP physical properties bounded relative to production concept (method TBC).

## 5. System Context

Physical architecture realises allocated functions in hardware and structure. It bounds the production-aircraft concept geometry and the MVP test article, interfacing with aerodynamic, structural, thermal and ground-support environments (all TBD).

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-PHY-001 | The physical architecture shall decompose the system into propulsion modules, airframe, avionics/compute, HMI, and ground-segment modules with positions TBD. | Inspection |
| REQ-HFPX-PHY-002 | The physical architecture shall define the mass/inertia representativeness principle for the MVP relative to the production concept (method TBC). | Analysis |
| REQ-HFPX-PHY-003 | The physical architecture shall define mounting and structural load paths for all modules (details TBD). | Analysis |
| REQ-HFPX-PHY-004 | The physical architecture shall maintain a physical interface register covering mechanical, electrical, fluid, and human interfaces. | Inspection |

## 7. Architecture

Modular decomposition (starter; positions, masses, dimensions TBD):

- Propulsion modules: arm, rear, ankle clusters (counts and positions TBD).
- Airframe/lifting body: central structure + lifting surfaces (concept TBD, ISS-004).
- Avionics/compute: flight computer + independent safety computer enclosures (locations TBD).
- HMI: helmet, pilot interface, suit attachments (TBD Vol 10/12).
- Ground segment: servicing, test and handling equipment (TBD Vol 21/23).

Representativeness principle: MVP mass/inertia properties shall be bounded and traceable to the production concept by a defined method (TBC); no masses or inertias are stated here. Load paths run from each propulsion mount into primary structure; sizing and materials TBD.

## 8. Detailed Design

Not applicable at this level. Mount details, fasteners, enclosures and layouts are deferred to Vol 03–18. No geometry or material stated.

## 9. Interfaces

Physical interface register (IDs TBD, detailed in ICDs 02.17): MECH (mounts, load interfaces), ELEC (connectors, grounding), FLUID (fuel/coolant couplings), HUMAN (suit/helmet attachment). Mating definitions and tolerances TBD.

## 10. Operational Concept

Physical configuration supports all CONOPS modes and ground handling states. Module access for inspection, servicing and replacement is a physical-architecture driver; maintenance concept details per Vol 21/23.

## 11. Safety

Physical separation and mounting independence support the dual-path safety architecture (ARC-003). Structural failure modes and crashworthiness feed Vol 13 analyses. No safety values stated.

## 12. Performance

Mass, inertia, stiffness and volume budgets are TBD. Budget holders: airframe/propulsion (Vol 03–06), avionics (Vol 08), HMI (Vol 10/12). No allocation values stated.

## 13. Verification & Validation

Verified by inspection (module decomposition, interface register) and analysis (representativeness method, load-path definition). Validated later by structural test and MVP correlation (Vol 19/33).

## 14. Risks

- Premature geometry assumptions before ISS-003/004 trades; mitigation: positions/masses explicitly TBD, method-only principle.
- Interface proliferation across modules; mitigation: register + ICD discipline (ARC-005).

## 15. Open Issues

Module positions, mass/inertia method (TBC), load-path details, and physical ICD numbering all TBD. ISS-003/004 trades not started.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS/SAD stability, propulsion trade (ISS-003), airframe concept (ISS-004), mass-property modelling (Vol 19), and subsystem physical inputs (Vol 03–18).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (notably ARC-001/005). Children: Vol 03–18 subsystem docs, ICDs, V&V cases. RTM: REQ-HFPX-PHY-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Chapter 02.3.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.3) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
