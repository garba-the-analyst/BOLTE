# System Architecture Description (SAD) — Stub

**Document ID:** HFPX-SYS-ARC-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 stub, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the system architecture of HFP-X in one description across all required views. This Tranche 1 version is a **stub**: it fixes the view framework, the SYS-01..SYS-23 breakdown and starter allocations; detailed architectures (02.2–02.17, Vol 03–18) follow. Backbone document 3 of 5.

## 2. Scope

Covers functional, logical, physical, operational, safety, data, electrical, propulsion and control views (prompt §11) plus human-system architecture. Applies to the production-aircraft concept; MVP architecture is separate (Vol 33.3). No component selected; no value baselined.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (stub, allocated here); HFPX-SYS-MIS-001/OPC-001/CON-001/STK-001 (sources)
- HFPX-PGM-SEM-001 SEMP; future ICDs (02.17), subsystem architectures (Vol 03–18)
- HFP prompt §§11–13 (architecture views, breakdown, flight modes)

## 4. Definitions & Acronyms

- Views: functional (what), logical (interactions), physical (components), operational (human use), safety (detect/control/mitigate), data (information flow), electrical (power flow), propulsion (energy→thrust), control (commands→responses)
- SYS-01..SYS-23: airframe, aero/lifting, propulsion, fuel, FCS, avionics, navigation, sensors, electrical, embedded computing, comms, helmet, pilot interface, suit, impact protection, recovery, thermal, ground station, software, cybersecurity, AI monitoring, maintenance, training

## 5. System Context

HFP-X in its environment (starter):

```text
ENVIRONMENT (air, weather TBD) → AIRFRAME/AERO (SYS-01/02) + PROPULSION/FUEL (SYS-03/04)
       → FCS/AVIONICS/COMPUTE (SYS-05/06/10 + safety computer) → HELMET/PILOT (SYS-12/13/14)
       → COMMS/GROUND STATION (SYS-11/18) → OPERATIONS/MAINTENANCE (SYS-22/23)
```

> **Hazardous-subsystem boundary (prompt §§14, 34).** This volume is limited to requirements, architecture, modelling, simulation, interfaces, test methodology and safety analysis. It contains no instructions for constructing, igniting or operating human-carrying high-energy propulsion outside appropriate controls.

## 6. Requirements

| ID | Architectural requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-ARC-001 | The architecture shall allocate every SyRS system requirement to ≥1 system in SYS-01..SYS-23 with no orphans. | Inspection |
| REQ-HFPX-ARC-002 | Primary flight control shall be deterministic, bounded and independently verifiable; AI (SYS-21) shall be monitoring/advisory only and shall never silently override pilot or safety authority. | Analysis + Test |
| REQ-HFPX-ARC-003 | A safety path independent of the primary control path (sensors → safety computer → stabilisation/recovery) shall be maintained. | Analysis |
| REQ-HFPX-ARC-004 | Hover, transition and cruise shall use distinct control-law sets with defined switching and abort criteria (laws TBD, Vol 07). | Analysis |
| REQ-HFPX-ARC-005 | All intersystem interfaces (power, data, fuel, mechanical, human) shall be captured in ICDs (02.17) before CDR. | Inspection |

## 7. Architecture

Functional view (starter): aviate (lift/thrust/control) → navigate (sense/fuse/estimate) → communicate (helmet/ground) → protect (monitor/safety/recovery) → sustain (power/thermal/fuel). Logical view: pilot/operator commands → FCS mixing/thrust allocation → propulsion modules; sensor fusion → navigation → FCS + safety computer in parallel; health monitoring → fault detection → mitigation. Physical view: distributed modules (arm/rear/ankle, positions TBD) + airframe/lifting body (concept TBD, ISS-004) + avionics/compute boxes (TBD) + helmet/ground station. Operational view: CONOPS state machine (see HFPX-SYS-CON-001 §7). Safety view: dual-path (primary + independent safety), recovery system TBD (ISS-008). Data view: buses/protocols TBD (Vol 08.6), time sync (08.16), logging (08.17). Electrical view: primary/auxiliary/battery/emergency distribution TBD (Vol 15). Propulsion view: energy → thrust chain TBD pending ISS-003 trade. Control view: distinct hover/transition/cruise laws TBD (Vol 07).

## 8. Detailed Design

Not applicable at SAD-stub level. Subsystem architectures (02.2–02.15, Vol 03–18) are TBD placeholders.

## 9. Interfaces

Interface register (starter): PWR (electrical distribution, Vol 15), DATA (buses, Vol 08), FUEL (distribution/metering, Vol 05), MECH (mounts, Vol 03.6), HUMAN (helmet/suit/controls, Vol 10/12), RF (comms/telemetry, Vol 11), GROUND (servicing/test, Vol 21/23). Each ICD gets an ID (`HFPX-ARC-ICD-NNN`, TBD) before CDR (ARC-005).

## 10. Operational Concept

Architecture supports all 15 flight modes; mode-to-view mapping: hover stresses propulsion/control/safety views; transition stresses control/safety/aero views; cruise stresses aero/propulsion/thermal views; emergencies stress safety/recovery/data views. Detail per CONOPS.

## 11. Safety

Safety architecture is independent by construction (ARC-003): separate safety computer (Vol 08.3), separate detection thresholds (Vol 13/16), independent stabilisation and recovery commanding. FHA/FMEA/FTA will reshape this view by change record. AI safety constraints (Vol 18.10) and human override (18.11) are mandatory inputs.

## 12. Performance

Architectural performance budgets (mass, power, data, thermal, control authority) are TBD. No allocation value is stated. Budget holders: mass/thrust (Vol 03–06, ISS-007), power (Vol 15), compute (Vol 08/16), control authority (Vol 07, ISS-006).

## 13. Verification & Validation

SAD verified by SRR inspection (every SYS requirement allocated per ARC-001; every interface named; AI/safety policies present). Later validated by SIL/HIL and unmanned flight showing architecture-as-built matches architecture-as-described (Vol 19/33).

## 14. Risks

- Allocation without component data → paper architecture; mitigation: stub status explicit, subsystem trades (ISS-003/004) feed revisions
- Interface sprawl across 23 systems; mitigation: ICD discipline (ARC-005) enforced at PDR/CDR gates

## 15. Open Issues

ISS-003 (propulsion chain unknown), ISS-004 (airframe concept unknown), ISS-006 (control authority), ISS-008 (recovery). New TBDs: bus/protocol selection, safety-computer independence criteria, ICD numbering.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SyRS stability, trade studies (ISS-003/004), control-law breakdown (Vol 07), safety analyses (Vol 13), modelling (Vol 19), ICD authorship (02.17).

## 18. Traceability

Parent: SyRS (REQ-HFPX-SYS-001..008 → allocated per §7). Children: subsystem architectures (Vol 03–18), ICDs, V&V cases. RTM: REQ-HFPX-ARC-001..005 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 1 stub, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 stub (Chapter 02.1; backbone 3/5) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
