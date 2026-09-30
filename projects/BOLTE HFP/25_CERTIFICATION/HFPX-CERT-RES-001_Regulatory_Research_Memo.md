# Regulatory Research Memo (First Findings)

**Document ID:** HFPX-CERT-RES-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Record first authoritative-source findings on the regulatory basis for HFP-X flight activity in Nigeria, and the gaps that keep ISS-001 OPEN. Findings only — no compliance claim, no authority contact made.

## 2. Scope

NCAA framework (confirmed items only) plus one foreign reference model (labeled non-applicable). Airworthiness-certification specifics, experimental-category provisions, and HFP-X applicability rulings are out of scope (TBD actions).

## 3. Applicable Documents

- HFPX-CERT-RGB-001 (25.2 — these findings feed it; basis still TBD)
- HFPX-CERT-STR-001, HFPX-CERT-FTA-001 (authorisation threads awaiting basis)
- Sources (retrieved 2026-09-29): NCAA official site ncaa.gov.ng (Nig.CARs 2023 parts catalogue; Part 18 April 2023 Amendment 4); eCFR 14 CFR 91.319; FAA Orders 8130.2G/H/J; FAA experimental-exhibition guidance

## 4. Definitions & Acronyms

- Nig.CARs: Nigeria Civil Aviation Regulations (2023 issue current per NCAA site)
- PNCF/PAAS: NCAA Permit for Non-Commercial Flights / Permit for Aerial Aviation Services (Part 18 economic permits — not airworthiness findings)
- Reference model: foreign framework studied for process insight only; confers zero Nigerian applicability

## 5. System Context

Regulatory basis gates flight authorisation, which gates unmanned testing, which gates everything after it (DDR-001 chain). This memo narrows the search; it does not establish the basis.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-RES-001 | Regulatory findings shall cite the authoritative source and retrieval date, distinguishing confirmed text from interpretation. | REQ-HFPX-QRB-001 | Inspection |
| REQ-HFPX-RES-002 | Foreign frameworks shall be labelled reference models with no applicability implied. | REQ-HFPX-QRB-001 | Inspection |
| REQ-HFPX-RES-003 | Unconfirmed provisions (experimental category, permit-to-fly, HFP-X applicability) shall remain TBD with named research actions, never inferred. | REQ-HFPX-QRB-001 | Inspection |
| REQ-HFPX-RES-004 | Authority engagement shall be initiated through a recorded plan before any flight-authorisation claim (plan TBD). | REQ-HFPX-QAE-001 | Inspection |

## 7. Architecture

Two-track record: confirmed NCAA framework items (§8) and open research actions (§8); foreign reference model annexed separately (§8).

## 8. Detailed Design

CONFIRMED (source-quoted, retrieval 2026-09-29):
1. NCAA is Nigeria's aviation regulator (Civil Aviation Act 2006/2022 lineage; autonomous safety oversight; info@ncaa.gov.ng; Abuja). Source: ncaa.gov.ng.
2. Nig.CARs 2023 is the current regulation set, organised in Parts. Confirmed parts: Part 8 Operations (based on ICAO Annex 2 Rules of the Air and Annex 6 Operation of Aircraft; applies to Nigerian-registered aircraft and operations within Nigeria); Part 12 Aerodromes; Part 18 Air Transport Economics (includes PNCF for non-commercial flights and PAAS for aerial-work/flying-school services — economic permits, not HFP-X authorisation); Parts 19/20/21 exist (Consumer Protection, Safety Management, RPAS). Source: ncaa.gov.ng documents catalogue + Part 18 PDF (April 2023 Amdt 4).
3. RPAS has a dedicated part (Part 21) — relevant context for the unmanned demonstrator path, provisions TBD.
NOT CONFIRMED (TBD actions): the Nig.CARs airworthiness-certification part number and contents; any NCAA experimental-category or permit-to-fly provision; HFP-X classification under any part; test-area/range authorisation mechanics; NCAA engagement channel for novel aircraft. Action: obtain the airworthiness part text from authoritative source; submit classification query to NCAA (owner TBD; Vol 25.11 plan TBD).
FOREIGN REFERENCE MODEL (no applicability): US 14 CFR 21.191 experimental purposes + 91.319 operating limitations (purpose-limited ops; Phase I flight-test area; controllable-throughout envelope demonstration; no densely-populated/congested-airway ops without authorisation; day-VFR default; occupants advised of experimental nature) under FAA Order 8130.2 certification procedures. Studied as a process reference for the kind of evidence package (controllability demonstration, test-area discipline, operating limitations) BOLTE should expect to negotiate — NOT as a basis. Sources: eCFR; FAA Orders 8130.2G/H/J.

## 9. Interfaces

- To 25.2 (RGB-001): findings feed basis determination; basis remains TBD
- To 25.6/25.11: authorisation and engagement threads await basis + plan
- To ISS-001: partial progress recorded; issue stays OPEN

## 10. Operational Concept

Research → record with sources → identify gaps → engage authority → determine basis → flow into strategy/authorisation docs. This memo completes the first two steps.

## 11. Safety

No flight-authorisation inference is drawn: nothing here permits any test or flight activity. Unauthorised operation would violate the very framework being researched.

## 12. Performance

Research performance: 3 confirmed items, 5 TBD actions, 0 applicability rulings.

## 13. Verification & Validation

Verified by inspection (sources cited with retrieval dates; confirmed-vs-TBD separation). Validation: Vol 25 owner review + eventual authority confirmation of the TBD items.

## 14. Risks

- Foreign framework mistaken for Nigerian basis; mitigation: RES-002 labelling + this memo's repeated non-applicability statements
- Part 18 economic permits mistaken for flight authorisation; mitigation: explicitly classified above as economic, not airworthiness

## 15. Open Issues

ISS-001 stays OPEN. TBD: airworthiness part text, experimental provisions, HFP-X classification, range authorisation, engagement plan.

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Vol 25 ownership, authority engagement (25.11), and access to current Nig.CARs airworthiness text.

## 18. Traceability

Parents: QRB/QAE tier, ISS-001. Children: basis determination, engagement plan, authorisation artifacts. RTM: REQ-HFPX-RES-001..004 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | First regulatory research memo (Tranche 8; confirmed items + TBD actions) |
