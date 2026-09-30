# Systems Engineering Management Plan (SEMP)

**Document ID:** HFPX-PGM-SEM-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 1 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define how HFP-X is engineered: processes, gates, baselines, reviews and control boards that turn mission needs into verified, certifiable hardware and software. Owns Chapter 00.4 and is backbone document 1 of 5.

## 2. Scope

Covers all 34 volumes and SYS-01..SYS-23. Governs requirements management (00.9), configuration/change/interface management (00.7/00.10/00.11), risk (00.12), design reviews (00.14) and decision records (00.16). Does not set technical values.

## 3. Applicable Documents

- HFPX-PGM-CHR-001 Programme Charter
- HFPX-SYS-REQ-001 SyRS (stub), HFPX-SYS-ARC-001 SAD (stub), HFPX-VV-PLN-001 V&V Plan (not written), HFPX-SAFE-CAS-001 Safety Case (not written)
- HFPX-PGM-BSL-001 Master Technical Baseline
- Standards (structured according to): INCOSE Handbook, ISO/IEC/IEEE 15288, ISO/IEC/IEEE 29148, SAE ARP4754A, SAE ARP4761/4761A; software/hardware assurance concepts DO-178C/DO-254, environmental DO-160

## 4. Definitions & Acronyms

- SEMP/SyRS/SAD/V&V: as per charter; RTM: Requirements Traceability Matrix
- Gates: SRR, PDR, CDR, TRR, FCA, PCA, FRR, PRR, ORR (prompt §18)
- BL: configuration baseline; DDR: Design Decision Record; TBD/TBC/A-XXX as per charter

## 5. System Context

SE process sits above all technical volumes:

```text
STAKEHOLDER NEEDS → SYSTEM REQUIREMENTS → ARCHITECTURE → DESIGN → IMPLEMENT → INTEGRATE → VERIFY → VALIDATE → CERTIFY → PRODUCE → OPERATE → SUSTAIN
         ↑_________________________ TRACEABILITY (RTM) _________________________________↑
         ↑_________________________ CONFIGURATION CONTROL ______________________________↑
```

MVP (Vol 33) runs the same V-model in miniature, kept separate from production baselines.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-PGM-010 | The programme shall manage requirements per ISO/IEC/IEEE 29148 concepts: atomic, unambiguous, measurable, testable, uniquely identified (`REQ-HFPX-[DOMAIN]-[NNN]`). | Inspection |
| REQ-HFPX-PGM-011 | Every system requirement shall state its verification method (Analysis, Inspection, Demonstration, Test). | Inspection |
| REQ-HFPX-PGM-012 | The programme shall maintain configuration baselines and never silently change a baselined requirement; each change identifies affected requirements, subsystems, interfaces and evidence. | Demonstration |
| REQ-HFPX-PGM-013 | The programme shall hold gated reviews SRR→ORR, each with entrance criteria, required documents, objectives, decision criteria, actions, exit criteria and baseline. | Inspection |
| REQ-HFPX-PGM-014 | Every significant architectural decision shall be recorded as a DDR and never rewritten; contradictions create a new DDR. | Inspection |
| REQ-HFPX-PGM-015 | Unknown data shall be labelled TBD/TBC/ASSUMPTION A-XXX with a defined validation path; assumptions shall never be presented as facts. | Inspection |

## 7. Architecture

SE organisation (roles TBD): Chief Engineer, Systems Engineering, Safety, V&V/Test, Configuration/Data Management, domain leads per Vol 03–18. Control boards: Configuration Control Board, Safety Review Board, Test/Flight Readiness Boards (membership TBD, Vol 00.3).

## 8. Detailed Design

Lifecycle (prompt §17 gated): Simulation → SIL → HIL → subsystem tests → integrated propulsion → unmanned demonstrator → hover → transition → horizontal flight → integrated mission → tethered human → controlled human flight → envelope expansion. Gate artefacts:

- SRR: mission, CONOPS, stakeholder reqs, SyRS stub, SAD stub, hazard log opened
- PDR/CDR: architectures + interface control docs + safety analyses (FHA/FMEA/FTA)
- TRR/FRR: test plans, readiness evidence, range/regulatory authorisations (all TBD, Vol 00.14 to define criteria)

## 9. Interfaces

- SE ↔ all volume owners via Interface Management (00.11) and ICDs (02.17)
- SE ↔ Safety (Vol 13/24, independent), SE ↔ V&V (Vol 22), SE ↔ Certification (Vol 25)
- Tooling: `hfpx_scaffold.py check` for structure/register validity; source control and release management per Vol 16 (details TBD)

## 10. Operational Concept

SE operates as the programme's control loop: plan (this SEMP) → elicit needs → specify → architect → allocate → design → build → integrate → verify → validate → audit (FCA/PCA) → baseline. Cadence and meeting structure TBD (Vol 00.2/00.5).

## 11. Safety

SE enforces safety independence: hazard log (Vol 13) → PHA/FHA/FMEA/FTA/CCA → safety requirements → safety architecture (independent safety computer) → verification. AI is advisory-only; deterministic bounded control for early flight (prompt §24).

## 12. Performance

SE performance indicators TBD (Vol 00.5): requirements volatility, RTM coverage (target 100% of major requirements traced), DDR closure, gate action burn-down. No thresholds baselined.

## 13. Verification & Validation

This SEMP is verified at SRR against prompt §6/§26 checklist (header, 20 sections, IDs, traceability). SE process itself is audited via FCA/PCA and gate action closure. Validation: programme authority approval.

## 14. Risks

- Process without people: roles unassigned → decisions stall; mitigation: Vol 00.3 staffing (TBD)
- Document sprawl (517 chapters) without RTM discipline → orphaned requirements; mitigation: RTM coverage gate at each review
- Premature human-flight pressure; mitigation: DDR-001 gates are mandatory

## 15. Open Issues

ISS-002 (needs baseline to make SE real), plus TBD staffing, tooling and gate-criteria issues to be raised in Vol 00.2/00.5/00.14.

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on Charter (authority), Vol 00.3 (organisation), Vol 00.14 (gate criteria), Vol 22 (V&V Plan), Vol 13 (safety programme), Vol 25 (regulatory basis, ISS-001).

## 18. Traceability

Parent: HFPX-PGM-CHR-001 (REQ-HFPX-PGM-001/002/004). Children: gate criteria (00.14), requirements plan (00.9), configuration/change plans (00.7/00.10), SyRS, SAD, V&V Plan. RTM: REQ-HFPX-PGM-010..015 → CONCEPT.

## 19. Configuration

BL-0.0. Tranche 1 draft, CONCEPT, not baselined. Future changes via change records (prompt §31).

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 1 draft (Chapter 00.4; backbone 1/5) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
