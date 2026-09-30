# Analysis

**Document ID:** HFPX-VV-ANL-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 8 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define verification by Analysis for Volume 22.5, covering calculation, modelling, and simulation review practice, tool and model control, analyst independence, and records.
Methodology only; detailed analyses remain with Vol 19 and owning design volumes.

## 2. Scope

Covers analysis verification threads across hardware, software, system, and safety where Analysis is the primary method.
Tool qualification, model validation detail, and execution procedures TBD; test and demonstration detail remains with Vol 22.7, Vol 22.8, and Vol 23.

## 3. Applicable Documents

- HFPX-VV-PLN-001 VV Plan (REQ-HFPX-VVP-001..006 — method assignment, acceptance, independence)
- HFPX-PGM-SEM-001 SEMP (gated reviews)
- HFPX-SYS-REQ-001 SyRS §13, HFPX-SYS-ARC-001 SAD (stub)
- Vol 19 (analysis capability, Vol 19.15 registers), Vol 22.3 (VCRM), Vol 23 (test execution)

## 4. Definitions & Acronyms

- Analysis: verification by calculation, modelling, or simulation review without physical measurement of the article
- Model: mathematical or simulation representation used as verification evidence; fidelity TBD per thread
- Tool: software or calculation aid supporting analysis; control status TBD
- Independence: separation between analyst and designer; degree TBD

## 5. System Context

Analysis provides early verification evidence ahead of physical test progression:

```text
REQUIREMENTS → MODELS → ANALYSIS → EVIDENCE → GATE
     ↑________ VCRM TRACE (method: Analysis) ________↑
     ↑________ TOOL AND MODEL CONTROL (Vol 19.15) ___↑
```

Analysis outputs feed sim, SIL, and HIL gating where applicable, with applicability TBD per thread.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-VAN-001 | The programme shall perform verification by Analysis to documented analysis practice, with scope, technique, and acceptance basis recorded as TBD per analysis thread. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-VAN-002 | Analysis tools and models used as verification evidence shall be controlled to documented provisions, with control detail and Vol 19.15 register hooks defined as TBD. | REQ-HFPX-VVP-001 | Analysis |
| REQ-HFPX-VAN-003 | Analysis of safety requirements and safety critical verification threads shall satisfy analyst independence provisions, with independence degree defined as TBD. | REQ-HFPX-VVP-006 | Analysis |
| REQ-HFPX-VAN-004 | Each analysis thread shall define acceptance criteria before credit, with criteria recorded as TBD per thread and records provisions defined as TBD. | REQ-HFPX-VVP-005 | Analysis |

## 7. Architecture

Analysis organisation and analyst roles TBD under VV and analysis lead governance.
Thread structure: parent requirement → model and tool chain → inputs and configuration → results → acceptance finding → VCRM entry.
Vol 19.15 registers provide tool and model control hooks; linkage detail TBD.

## 8. Detailed Design

Analysis plans are drafted early (SRR and PDR) and matured through CDR; model fidelity claims and input pedigrees TBD per thread.
Each analysis case template shall contain objective, traced parents, method, inputs and configuration, tool and model identifiers with versions TBD, acceptance criteria (TBD per case), and independence claim where applicable.
Re-analysis on design or input change follows change control with scope TBD.

## 9. Interfaces

- Analysis ↔ Vol 19 (analysis capability, models, registers)
- Analysis ↔ VCRM (Vol 22.3 traceability and status)
- Analysis ↔ Test and Demonstration (complementary evidence; allocation TBD)
- Analysis ↔ Safety (Vol 13 and Safety Case: safety analysis inputs and closure evidence)

## 10. Operational Concept

Analysis operates model-to-finding: plan threads early → control tools and models → execute calculations and reviews → record findings → claim credit at gates.
Cadence, peer provisions, and tooling TBD.

## 11. Safety

Safety analyses receive independent analysis or independent review per VV Plan independence rules TBD.
AI outputs used in analysis threads are advisory only in early phases; the deterministic bounded function actually verified is identified with details TBD.

## 12. Performance

Analysis indicators TBD, with all thresholds TBD: thread coverage, model control completeness, criteria definition backlog, finding closure burn-down.
Measurement method and reporting cadence TBD.

## 13. Verification & Validation

This document is verified by Inspection against the VV Plan and SEMP checklist (header, 20 sections, IDs, parents, allowed methods only).
Validation of the analysis approach is programme authority approval at gated reviews; certification validation owned by Vol 25.

## 14. Risks

- Uncontrolled tools or models weakening analysis credit; mitigation: control provisions with Vol 19.15 hooks (detail TBD)
- Analyst dependence on design organisation for safety threads; mitigation: independence provisions per REQ-HFPX-VAN-003 (degree TBD)
- Acceptance basis left TBD blocking credit; mitigation: per-thread TBD tracking (assignments TBD)

## 15. Open Issues

Analysis practice detail TBD. Tool and model control provisions TBD. Independence degree TBD. Acceptance criteria TBD per thread. Register linkage TBD.

## 16. Assumptions

_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on VV Plan methodology, SEMP gates, SyRS §13, SAD allocation, Vol 19 capability and registers, Vol 22.3 VCRM, Vol 25 credit rules, Safety Case inputs.

## 18. Traceability

Parents: REQ-HFPX-VVP-001, REQ-HFPX-VVP-005, REQ-HFPX-VVP-006. Children: analysis cases in Vol 19 and owning volumes (case IDs TBD; VCRM rows TBD).
RTM: REQ-HFPX-VAN-001..004 → CONCEPT. Coverage tracked in Vol 22.3 VCRM.

## 19. Configuration

BL-0.0. Tranche 8 draft, CONCEPT, not baselined. Future changes via change records; affected VCRM rows re-validated before gate claims.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 8 draft (Vol 22.5 direction; structure only) |
