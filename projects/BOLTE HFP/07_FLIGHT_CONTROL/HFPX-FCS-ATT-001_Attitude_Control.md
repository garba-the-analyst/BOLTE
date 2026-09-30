# Attitude Control

**Document ID:** HFPX-FCS-ATT-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the 3-axis attitude control function for HFP-X (Chapter 07.5): stabilisation, command tracking, disturbance rejection, and envelope protection. No control-law values are defined.

## 2. Scope

Covers attitude stabilisation and protection as implemented through the Vol 07 law framework. Gains, bandwidths, errors, disturbance levels, and envelope limits are TBD. Roll/pitch axis details are in ROL/PIT docs.

## 3. Applicable Documents

- HFPX-FCS-REQ-001 (FCR-001..003); HFPX-FCS-LAW-001 (FCL-001..006); HFPX-FCS-ARC-001
- HFPX-ARC-CTL-001 (CTL-001/003); ISS-006 (authority); Vol 19 (SIL/HIL)
- Companions: HFPX-FCS-ROL-001, HFPX-FCS-PIT-001

## 4. Definitions & Acronyms

- Attitude stabilisation: regulation of 3-axis orientation (pitch/roll/yaw, TBD frames).
- Attitude-command tracking: following of commanded attitudes/rates (commands TBD).
- Disturbance rejection: attenuation of gusts/model uncertainty effects (levels TBD).
- Attitude-envelope protection: prevention/limiting beyond defined attitudes (limits TBD).

## 5. System Context

Attitude control is the core inner-loop function fed by shaped commands and fusion attitudes/rates, executing within the selected regime law set and outputting moment demands to allocation. Envelope protection coordinates with the mode supervisor and safety path.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FCT-001 | The FCS shall provide 3-axis attitude stabilisation across hover, transition, and cruise (frames, modes, and criteria TBD). | FCR-001 | Analysis + SIL + HIL (TBD) |
| REQ-HFPX-FCT-002 | The FCS shall track attitude commands within defined criteria (commands, errors, and conditions TBD). | FCR-001 | Analysis + SIL + Test (TBD) |
| REQ-HFPX-FCT-003 | The FCS shall reject disturbances per defined levels (disturbance models and attenuation TBD). | FCR-001 | Analysis + SIL (TBD) |
| REQ-HFPX-FCT-004 | The FCS shall provide attitude-envelope protection with defined limits and responses (limits and responses TBD). | FCR-003 | Analysis + SIL + HIL (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Text block diagram:

```
[Attitude/Rates Estimates] --\
[Attitude Commands] ---------> [Attitude Laws per Regime (LAW framework, TBD)] --> [Moment Demands] --> [Allocation/Mixing (TBD)]
[Disturbances (TBD)] --------/         |
                        [Envelope Protection (FCT-004, TBD)] --> [Limit/Override --> Supervisor / Safety]
```

Structures, estimators, and protection logic are TBD.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Law realisations, parameters, and protection thresholds are TBD.

## 9. Interfaces

- Command input ICD (from INP/supervisor): TBD.
- Estimate input ICD (from fusion): TBD.
- Moment-demand output to allocation ICD: TBD.
- Protection/supervisor/safety ICD: TBD.

## 10. Operational Concept

Attitude control operates in all regimes; hover stresses stabilisation, transition stresses tracking through switching, cruise stresses efficiency/stability; protection engages before envelope exceedance with handover as needed (all TBD).

## 11. Safety

Loss of attitude stabilisation, untracked commands, unrejected disturbances, or missing protection are hazardous. Mitigations required (all TBD): stabilisation (FCT-001), tracking (FCT-002), disturbance rejection (FCT-003), envelope protection plus safety handover (FCT-004). No stability claim is made.

## 12. Performance

Tracking errors, rejection levels, protection margins, and timing are TBD. No performance value is stated.

## 13. Verification & Validation

Verified by analysis, SIL/HIL (Vol 19), and test; disturbance and protection cases by injection/simulation (methods and pass criteria TBD).

## 14. Risks

- Attitude laws and disturbance environment undefined; mitigation: TBD requirements with Vol 19 modelling planned.
- Protection limits unknown; mitigation: explicit TBD, coordinated with ISS-006 and safety view.

## 15. Open Issues

- Frames/modes TBD; tracking criteria TBD; disturbance models/levels TBD; envelope limits/responses TBD.

## 16. Assumptions

- A-FCT-001: 3-axis attitude stabilisation is allocated to FCS inner loop (validation: Vol 07 review, TBD).

## 17. Dependencies

Depends on FCR-001/003, law framework (FCL-001..004), architecture/supervisor, fusion estimates, allocation, ISS-006, Vol 19 rigs.

## 18. Traceability

Parents: FCR-001 (via HFPX-FCS-REQ-001), CTL-001. Children: ROL/PIT axis designs, SIL/HIL cases, V&V cases. RTM: REQ-HFPX-FCT-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.5) |
