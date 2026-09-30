# Safety Architecture

**Document ID:** HFPX-ARC-SAF-001  
**Revision:** B (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 2 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X safety architecture view (Chapter 02.10): the independent safety path, the detection→stabilisation→recovery/mitigation chain, and hooks for safety analyses and AI/human authority rules.

## 2. Scope

Covers safety-path structure, independence principles, and analysis feeds. Applies to the production-aircraft concept. No component selected; detailed design and all values TBD.

## 3. Applicable Documents

- HFPX-SYS-REQ-001 SyRS (REQ-HFPX-SYS-001..008); HFPX-SYS-ARC-001 SAD (REQ-HFPX-ARC-001..005)
- Vol 13 (FHA/FMEA/FTA); Vol 18.10/18.11 (AI constraints, human override); Vol 08.3 (safety computer)
- HFP prompt §§11, 14 (architecture views, safety)

## 4. Definitions & Acronyms

- Primary path: pilot/operator commands → FCS → thrust allocation → propulsion.
- Safety path: independent sensing → safety computer → stabilisation/recovery commanding.
- FHA/FMEA/FTA: hazard, failure-mode, and fault-tree analyses (Vol 13).

## 5. System Context

Safety architecture sits alongside primary flight control and the pilot: it observes the same vehicle state through an independent path and commands stabilisation or recovery when thresholds are crossed. Thresholds, sensors, and commands are TBD.

## 6. Requirements

| ID | Requirement (shall) | Verification |
| --- | --- | --- |
| REQ-HFPX-SFA-001 | The safety architecture shall maintain a safety path independent of the primary flight-control path (sensors → safety computer → stabilisation/recovery). | Analysis + Inspection |
| REQ-HFPX-SFA-002 | The architecture shall implement a detection→stabilisation→recovery/mitigation chain with defined handover criteria (criteria TBD). | Analysis |
| REQ-HFPX-SFA-003 | The safety view shall be fed by FHA/FMEA/FTA (Vol 13); analysis findings shall reshape this view by change record. | Inspection |
| REQ-HFPX-SFA-004 | AI (SYS-21) shall be constrained per Vol 18.10 and shall never silently override pilot or safety authority; human override hooks per Vol 18.11 shall be preserved. | Analysis + Test |

## 7. Architecture

Dual-path structure: (a) primary path — pilot/operator → FCS mixing/thrust allocation → propulsion modules; (b) safety path — independent sensors → safety computer (Vol 08.3) → independent stabilisation laws and recovery triggering. Detection thresholds (Vol 13/16) feed the safety computer; outputs command stabilisation or hand over to the recovery architecture (02.14). Independence criteria (separation, dissimilarity, authority priority — TBD) are enforced by design rule. AI monitoring (SYS-21) feeds advisories only, bounded by Vol 18.10 constraints, with human override per 18.11. FHA/FMEA/FTA outputs allocate new monitors, thresholds, and mitigations into this view.

## 8. Detailed Design

Not applicable at Tranche 2 draft level. Safety computer selection, sensor allocation, thresholds, and stabilisation laws are TBD (Vol 08.3, Vol 13, Vol 16).

## 9. Interfaces

Safety computer interfaces to sensors, FCS, recovery system, and pilot alerting (helmet/HUD/audio) are TBD. Each interface shall be captured in an ICD (02.17) before CDR per ARC-005.

## 10. Operational Concept

Safety path is armed in all flight modes; detection→stabilisation→recovery sequencing applies per CONOPS state machine. Pilot retains override authority except where TBD interlocks (Vol 18.11) apply; all interlocks TBD.

## 11. Safety

Safety is the governing emphasis of this view: independence by construction (SFA-001), bounded AI with no silent override (SFA-004), and analysis-driven evolution (SFA-003). No safety claim is made; effectiveness is unproven pending Vol 13 analyses and Vol 19/33 verification.

## 12. Performance

Detection latency, false-alarm rate, stabilisation authority, and availability budgets are TBD. No allocation value is stated.

## 13. Verification & Validation

Verified by analysis (independence argument, chain completeness) and inspection (FHA/FMEA/FTA feed recorded). Later validated by SIL/HIL fault injection and unmanned flight (Vol 19/33). All methods TBD in detail.

## 14. Risks

- Common-cause failure across primary and safety paths; mitigation: independence criteria TBD, analysis per Vol 13.
- Late hazard discovery reshaping architecture; mitigation: change-record discipline, stub status explicit.

## 15. Open Issues

Safety-computer independence criteria TBD; detection thresholds TBD; stabilisation laws TBD; AI constraint set TBD (Vol 18.10); override interlock list TBD (Vol 18.11).

## 16. Assumptions


_TBD_

All unknowns in this document are recorded as TBD. No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SAD (ARC-001..005), SyRS, Vol 08.3 (safety computer), Vol 13 (safety analyses), Vol 16 (software/compute), Vol 18 (AI/autonomy), recovery architecture (02.14).

## 18. Traceability

Parents: SyRS REQ-HFPX-SYS-001..008; SAD REQ-HFPX-ARC-001..005 (esp. ARC-002, ARC-003); tier inputs FUN/SAF/HUM as allocated. Children: safety analyses (Vol 13), safety-computer design (Vol 08.3), recovery view (02.14). RTM: REQ-HFPX-SFA-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 2 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 2 draft (Chapter 02.10) |
| B | 2026-09-29 | Assumptions removed; all unknowns recorded as TBD (no assumptions raised or relied upon). |
