# Exhaust Heat

**Document ID:** HFPX-THM-EXH-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 6 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X exhaust-heat structure for Chapter 14.3. This Tranche 6 draft establishes plume-impingement inventory, pilot/airframe interfaces, and mitigation-approach structure with all values TBD; quantified design follows in later tranches.

## 2. Scope

Analysis, modelling, and test methodology only. Covers exhaust plume impingement, affected pilot and airframe interfaces, and mitigation approaches. Provides no operating instructions. Excludes engine-bay heat detail (14.2) and qualification detail (14.14, Vol 22/23). All values TBD.

## 3. Applicable Documents

- HFPX-SYS-ENV-001 Environmental Requirements (parent REQ-HFPX-SYS-006, ENV tier)
- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-006 environmental policy)
- Vol 04 propulsion, Vol 06 airframe, Vol 12 pilot interfaces (structure only)
- Vol 19.6 modelling framework (to follow)

## 4. Definitions & Acronyms

- TEX: exhaust-heat requirement tier; ID `REQ-HFPX-TEX-NNN`; verification: TBD (intended Model + Test).
- Plume impingement: exhaust-flow thermal effect on structures or occupants; inventory TBD.
- TBD/TBC: unknown data; no values invented.

## 5. System Context

Exhaust-heat tier refines SYS-006 and ENV-001 into impingement inventory and mitigations:

```text
SYS-006 → ENV-001 → TEX-001..004 (impingement, interfaces, mitigations) → Vol 04/06/12 design → Model correlation + test (14.14, Vol 22/23)
```

Impingement zones and mitigations require plume models and programme decisions before any value is approved.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-TEX-001 | The system shall define an exhaust plume-impingement inventory of [TBD] with affected regions TBD (values TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Model + Test |
| REQ-HFPX-TEX-002 | The system shall identify exhaust-heat pilot and airframe interfaces of [TBD] with Vol 06/12 boundaries TBD (identities TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Model + Test |
| REQ-HFPX-TEX-003 | The system shall apply defined exhaust-heat mitigation approaches of [TBD] (approaches TBD). | REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 | Model + Test |
|REQ-HFPX-TEX-004|Each exhaust-heat requirement shall be verified by method of [TBD] with criteria TBD (verification TBD).|REQ-HFPX-SYS-006|Inspection|

Scope note: analysis, modelling, and test methodology only; no operating instruction is given. No temperature, heat load, flow rate, or limit is stated or implied; all values are TBD.

## 7. Architecture

Starter allocation (SAD owns authoritative mapping): impingement regions → plume model zones TBD; interfaces → Vol 06 airframe / Vol 12 pilot boundaries TBD; mitigations → shielding/routing/procedural-structure provisions TBD (no operating instructions). All TBC pending models.

## 8. Detailed Design

Not applicable — structure level only. Deflectors, shields, and material selections live in Vol 04/06 and are TBD.

## 9. Interfaces

Exhaust interfaces (nozzle, plume boundaries, impinged structure, pilot-station thermal boundaries) are TBD in Chapter 01.16 and Vol 02 ICDs with Vol 04/06/12 counterparts. No interface value is approved.

## 10. Operational Concept

Requirements apply across CONOPS phases as applicable; phase applicability matrix is TBD. No operating instruction is given in this revision.

## 11. Safety

Exhaust-heat hazards (thermal injury, structural degradation) feed Vol 13 safety analyses (to follow). No mitigation in this revision is a safety claim; safety credit requires analysed and tested limits via change record.

## 12. Performance

Exhaust-heat provisions do not quantify performance. Thrust and thermal-performance interactions are TBD and owned jointly with propulsion tiers.

## 13. Verification & Validation

Intended method is Model + Test (see table; REQ-HFPX-TEX-004 TBD); plume model fidelity, impingement test conditions, and pass criteria are TBD in 14.14 and the V&V Plan (Vol 22). No verification credit is claimed at this revision.

## 14. Risks

- Impingement inventory undefined → unprotected structure or occupant exposure; mitigation: single TBD-owned tier with CONCEPT status.
- Mitigations assumed effective without test; mitigation: change-controlled model correlation only.

## 15. Open Issues

Plume-impingement inventory, pilot/airframe interface mapping, mitigation selection, and verification method confirmation. RTM seed for TEX-001..004 added with this tranche (Status CONCEPT).

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-006 stability, ENV tier, Vol 04/06/12 inputs, Vol 19.6 plume models, and 14.14 test thread. Changes propagate by change record.

## 18. Traceability

Parents: REQ-HFPX-SYS-006; REQ-HFPX-ENV-001 (see table). Children: Vol 04/06/12 exhaust provisions, test cases (14.14, Vol 22/23), RTM rows. RTM seed for TEX-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 6 draft, not baselined. Quantification requires new revisions via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 6 draft (Chapter 14.3; all values TBD) |
