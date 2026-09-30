# Fuel Selection

**Document ID:** HFPX-FUEL-SEL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 4 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the fuel-selection framework for HFP-X (Chapter 05.2): selection criteria, candidate compatibility assessment structure, safety/regulatory constraints, and the decision rule. No fuel is chosen in this document. All fuel property values are TBD. The selection decision is deferred to the ISS-003 energy trade study plus a formal Design Decision Record (DDR).

## 2. Scope

Covers selection criteria (compatibility, safety, energy, operability), the candidate compatibility matrix structure (populated TBD), safety/regulatory constraint identification, and the trade-study-plus-DDR decision rule. Explicitly excludes: selection of any fuel type, any fuel property value, procurement, handling procedures, and detailed design of storage/distribution/consumption hardware (Chapters 05.3–05.9).

> **Hazardous-subsystem boundary.** Content in this document is limited to requirements, architecture, interfaces, test methodology and safety analysis. It shall not contain instructions for constructing, igniting, or operating human-carrying high-energy propulsion outside appropriate engineering, test, safety and regulatory controls. No fuel-handling or operation instructions are provided herein.

## 3. Applicable Documents

- HFPX-FUEL-REQ-001 Fuel Requirements (Chapter 05.1, parent)
- HFPX-SYS-REQ-001 SyRS (SYS-001/003)
- ISS-003 energy trade (authorising trade for the deferred decision)
- Vol 04 propulsion demands (TBD); Vol 13 safety analyses (TBD); Vol 22 V&V Plan (TBD)

## 4. Definitions & Acronyms

- FSL: fuel-selection ID prefix `REQ-HFPX-FSL-NNN`
- DDR: Design Decision Record formally recording the future fuel choice
- Compatibility: suitability of a candidate fuel with materials, components, engines, environment, and servicing concept (values TBD)
- Operability: ability to store, distribute, meter, and inject the fuel across the envelope under controlled conditions (limits TBD)
- No-selection rule: no statement in this volume shall be read as choosing a fuel type

## 5. System Context

Selection constrains all downstream fuel chapters without pre-empting them:

```text
CRITERIA (this doc) → CANDIDATE MATRIX (TBD) → TRADE STUDY (ISS-003) → DDR (decision)
  → requirements update (05.1) → tank/storage/distribution/pumps/filter/metering/injection sizing (05.3–05.9)
```

Until the DDR, every downstream document remains fuel-agnostic and TBD-quantified.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FSL-001 | The project shall define fuel-selection criteria covering at minimum compatibility, safety, energy, and operability, with evaluation metrics and weights TBD. | REQ-HFPX-FRQ-002 | Inspection |
| REQ-HFPX-FSL-002 | The project shall maintain a candidate-fuel compatibility matrix mapping each candidate against materials, components, engines, environment, and servicing constraints, with entries TBD and no candidate selected. | REQ-HFPX-FRQ-002 | Inspection |
| REQ-HFPX-FSL-003 | The project shall identify safety and regulatory constraints applicable to candidate fuels (handling class, storage class, transport, test-range, certification implications — details TBD) before any selection decision. | REQ-HFPX-FRQ-004 | Analysis + Inspection |
| REQ-HFPX-FSL-004 | The project shall make the fuel-type decision only through the ISS-003 trade study recorded in a DDR, with re-verification of affected fuel requirements upon approval. | REQ-HFPX-FRQ-005 | Inspection |

No fuel is chosen by this document; any reading that a fuel has been selected is non-compliant with FSL-004.

## 7. Architecture

Criteria architecture (FSL-001): four pillars — compatibility (materials/components/engine/environment/servicing), safety (hazard class, isolation/leak implications, range safety), energy (energy content and mission-endurance linkage — values TBD), operability (storage stability, conditioning needs, metering/injection suitability — details TBD). Weighting and scoring method TBD in the trade-study plan. Matrix (FSL-002) is rows = candidates (TBD, unnamed here), columns = criteria; all cells TBD.

## 8. Detailed Design

Not applicable — no fuel chosen, no property values, no hardware design. Candidate identities, datasheets, and test data are TBD inputs to the trade study, not conclusions of this document.

## 9. Interfaces

Interface placeholders: selection-to-propulsion demand interface (Vol 04 — engine fuel suitability inputs TBD); selection-to-safety/regulatory interface (Vol 13 + range/certification authorities — constraints TBD); selection-to-logistics interface (storage/servicing concept inputs TBD). No procurement or supply-chain commitments are made herein.

## 10. Operational Concept

Trade-study analysis only, under controlled engineering conditions. No fuel handling, transport, storage operations, refuelling, or engine-operation procedures are defined in this document. Any future handling/operation is restricted to appropriate engineering, test, safety, and regulatory controls.

## 11. Safety

FSL-003 requires safety/regulatory constraints to be identified before selection. Hazardous-subsystem boundary applies: safety analysis and test methodology only; no fuel-handling or operation instructions outside controlled conditions. Vol 13 analyses inform the constraint set; no safety case claim is made for any candidate fuel herein.

## 12. Performance

Intentionally TBD. No energy content, specific energy, density, endurance, range, or consumption figure is stated for any candidate. Performance comparison method (metrics, models — TBD) belongs to the ISS-003 trade-study plan, not to this criteria document.

## 13. Verification & Validation

Verification is by inspection of criteria/matrix/constraint artefacts (FSL-001..003) and of the trade-study-plus-DDR record (FSL-004). Test of candidate fuels, if required, is defined in Fuel System Testing (05.16) and the V&V Plan (Vol 22) under controlled conditions; no test execution is authorised by this document.

## 14. Risks

- Implicit fuel assumption leaking into downstream sizing before the DDR; mitigation: explicit no-selection rule + DDR gate
- Criteria weighting disputes delaying ISS-003; mitigation: weighting agreed at SRR, recorded before scoring
- Regulatory constraint discovered after provisional preference; mitigation: FSL-003 constraint survey precedes scoring

## 15. Open Issues

- ISS-003 (energy trade — owns the deferred decision; stays OPEN)
- Criteria metrics/weights (TBD, trade-study plan)
- Candidate list and matrix entries (TBD, unnamed in this revision)
- Safety/regulatory constraint survey (TBD, Vol 13 + authorities)

## 16. Assumptions

- A-FSL-001: Compatibility, safety, energy, operability are sufficient criteria pillars pending trade-study-plan review; validation: SRR review
- A-FSL-002: Downstream chapters can proceed fuel-agnostically to CONCEPT maturity without candidate data; validation: DDR impact review

## 17. Dependencies

Depends on FRQ-002 (quality/conditioning parents), ISS-003 trade authorisation and plan, propulsion fuel-suitability inputs (Vol 04), safety/regulatory inputs (Vol 13, authorities), V&V test-methodology inputs (Vol 22, 05.16).

## 18. Traceability

Parents: REQ-HFPX-FRQ-002, REQ-HFPX-FRQ-004, REQ-HFPX-FRQ-005 (table above); SYS-001/003 via 05.1. Children: ISS-003 trade study, DDR (future), compatibility matrix artefact, constraint survey, downstream quantification updates (05.1, 05.3–05.9). RTM seed for FSL-001..004 added with this tranche (Status CONCEPT).

## 19. Configuration

BL-0.0 (structure only) — Tranche 4 draft, not baselined. Recording any fuel choice in this document without a DDR is a non-compliant change; the decision requires a new revision via change control.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 4 draft (Chapter 05.2, 4 requirements, no fuel chosen) |
