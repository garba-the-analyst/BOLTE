# Refuelling / Defuelling (Chapter 05.17)

**Document ID:** HFPX-FUEL-RFL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Hold the refuelling/defuelling requirements for HFP-X in one chapter. This Tranche 4 draft establishes the requirement set structure: servicing interfaces, grounding/bonding hooks, spill/containment principles, and demonstration-based servicing verification; all quantitative values and procedures are TBD.

## 2. Scope

Covers Chapter 05.17 Refuelling / Defuelling: servicing interfaces, grounding/bonding hooks (with Vol 21.11), spill/containment principles, and verification approach. Servicing equipment, procedures, quantities, and detailed design are TBD.

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for refuelling, defuelling, handling, or operating fuel or propulsion outside appropriate engineering, test, safety and regulatory controls. Any servicing activity occurs only under controlled conditions with approved procedures per Vol 13 / Vol 21 / Vol 22 / Vol 33.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (parents REQ-HFPX-SYS-003, REQ-HFPX-SYS-006)
- FRQ tier (functional requirements, TBD — parent tier)
- SAF tier (safety requirements, TBD) and SCA-006
- Vol 21.11 Grounding/bonding provisions (hooks, TBD)
- HFPX-SYS-ARC-001 SAD (allocation to fuel subsystem and GSE, TBD)
- Vol 02 ICDs (servicing interfaces, TBD)
- Vol 13 Safety analyses; Vol 21 Maintenance; Vol 22 V&V Plan (not written); Vol 33 Test (controlled conditions)
- HFP prompt §§8–10, 14, 19, 32, 34

## 4. Definitions & Acronyms

- FRF: refuelling/defuelling thread; requirement IDs `REQ-HFPX-FRF-001..004`
- Servicing interfaces: boundaries to refuelling/defuelling equipment and vehicle (TBD)
- Grounding/bonding hooks: provision interfacing to Vol 21.11 (details TBD)
- Spill/containment principles: requirements-level principles for spill avoidance and containment (criteria TBD)
- TBD/TBC/A-XXX: unknown data handling; no invented values
- Verification: Analysis / Inspection / Demonstration / Test

## 5. System Context

Servicing connects the vehicle to ground equipment under controlled conditions:

```text
GSE / SERVICING EQUIPMENT (TBD) → SERVICING INTERFACES (this chapter) → FUEL STORAGE (05.4)
        grounding/bonding hooks → Vol 21.11 (TBD)
        spill/containment principles → GSE + procedures (TBD, controlled conditions)
```

This chapter states interface and principle requirements; equipment, procedures, and approvals live in Vol 21/22/33. Allocation to ports, couplings, and GSE is TBD in the SAD.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FRF-001 | The fuel system shall provide servicing interfaces for refuelling and defuelling (locations and types TBD). | FRQ tier (TBD), REQ-HFPX-SYS-006 | Inspection |
| REQ-HFPX-FRF-002 | The fuel system shall provide grounding/bonding hooks interfacing to Vol 21.11 provisions (details TBD). | SAF tier (TBD), REQ-HFPX-SYS-003 | Inspection |
| REQ-HFPX-FRF-003 | The fuel system shall implement spill/containment principles for servicing (criteria TBD). | REQ-HFPX-SYS-003, SAF tier (TBD) | Analysis |
| REQ-HFPX-FRF-004 | Servicing interfaces and principles shall be verified by demonstration under controlled conditions (procedures TBD). | SCA-006, REQ-HFPX-SYS-006 | Demonstration |

No interface type, location, quantity, criterion, or procedure in this document is approved; all are TBD. This table states verification obligations only; it is not a servicing procedure.

## 7. Architecture

Logical allocation (starter — SAD owns authoritative allocation): vehicle servicing ports/couplings (TBD) → interface boundary → GSE/equipment side (TBD); grounding/bonding path provision (TBD, to Vol 21.11); containment provision (TBD). Access, labelling, interlocks, and filtration at the interface are TBD. No port, coupling, or equipment selection is baselined.

## 8. Detailed Design

Not applicable — requirements/architecture level only. No detailed design, part selection, GSE design, procedure, schematic, or installation drawing is contained or approved in this revision.

## 9. Interfaces

Interface placeholders (controlled via SAD §9 / Vol 02 ICDs, all TBD): fluid/mechanical servicing interfaces (couplings, ports, pressures/flows TBD); grounding/bonding interface to Vol 21.11; spill/containment interface to GSE and facilities; data interface where applicable (quantity/verification feedback); environmental interfaces per SYS-006. Details are TBD.

## 10. Operational Concept

Servicing is exercised through ground-operations threads; each requirement maps to ≥1 nominal/off-nominal scenario (mapping TBD in V&V Plan). This document prescribes no servicing procedure, sequence, handling step, or operating instruction. Any refuelling/defuelling activity occurs only under controlled conditions with approved procedures, trained personnel, equipment, range/facility, and safety controls.

## 11. Safety

Servicing hazards (spill, ignition source, incorrect servicing, uncontrolled release) are controlled via Vol 13 analyses and Vol 21/22/33 procedures and controls; this chapter generates no standalone safety claim and no authorisation to service. Grounding/bonding hooks and spill/containment principles support the SYS-003 safety path at requirements level. Hazardous-subsystem boundary applies (see §2).

## 12. Performance

Intentionally TBD. Servicing rates, quantities, times, envelope, and containment capacity are TBD pending architecture, GSE trades, and safety analysis. No performance value in this document is approved.

## 13. Verification & Validation

Each requirement states its method above; verification IDs and cases are TBD in the V&V Plan (Vol 22). Strategy: inspection (interface and hook provision) → analysis (spill/containment principles) → demonstration (servicing interfaces and principles, controlled conditions, simulants/fluids per approved procedure TBD). Requirements without a verification method are rejected at SRR.

## 14. Risks

- Servicing interfaces defined late → GSE mismatch → mitigation: interface requirements retained as placeholders, ICD gate per review
- Grounding/bonding detail owned elsewhere (Vol 21.11) drifts → mitigation: explicit hook requirement, cross-volume trace
- Spill/containment criteria undefined → mitigation: principle requirement retained, analysis-gated

## 15. Open Issues

- Servicing interface types, locations, pressures/flows (all TBD)
- Grounding/bonding details with Vol 21.11 (TBD)
- Spill/containment criteria and allocation; demonstration procedures and pass/fail (TBD)

## 16. Assumptions

- A-TBD: Dedicated refuelling/defuelling interfaces with grounding/bonding hooks and spill/containment principles are required regardless of final fuel selection; validation: SRR review
- No assumption is made about interface type, equipment, quantities, criteria, or procedures in this revision

## 17. Dependencies

Depends on storage architecture (05.4), Vol 21.11 grounding/bonding, GSE definition (TBD), safety analyses (Vol 13, SAF tier, SCA-006), maintenance inputs (Vol 21), and V&V/test planning (Vol 22/33). FRQ-tier approval gates requirement stability.

## 18. Traceability

Parents: FRQ tier (TBD), REQ-HFPX-SYS-003, REQ-HFPX-SYS-006, SAF tier (TBD), SCA-006, Vol 21.11 (table above). Children: SAD views, servicing-interface specifications (TBD), ICD rows, V&V cases, RTM rows. RTM seed for REQ-HFPX-FRF-001..004 is added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0. Tranche 4 draft, CONCEPT, not baselined. Interface definition, criterion approval, or procedure approval requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.17; HFPX-FUEL-RFL-001) |
