# Pilot Input System

**Document ID:** HFPX-FCS-INP-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 3 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the pilot/operator input system for FCS (Chapter 07.3): command capture, shaping/limiting, inadvertent-input protection, and input-loss behaviour. No devices, values, or limits are selected.

## 2. Scope

Covers pilot/operator command path up to the FCS law interface. Input devices, shaping functions, limits, rates, and loss/freeze logic are TBD (devices TBD, Vol 10/12). Downstream laws are per HFPX-FCS-LAW-001.

## 3. Applicable Documents

- HFPX-FCS-REQ-001 (FCR-001, FCR-005); HMI needs FUN-002, HSA-002
- Vol 10/12 (HMI/operator devices); HFPX-FCS-ARC-001 (architecture); HFPX-ARC-CTL-001
- Vol 19 (SIL/HIL input modelling)

## 4. Definitions & Acronyms

- Command capture: acquisition of pilot/operator intent via input devices (devices TBD).
- Shaping/limiting: conditioning of raw inputs into bounded FCS commands (functions and limits TBD).
- Inadvertent-input protection: rejection/mitigation of unintended commands (mechanism TBD).
- Input-loss/freeze: defined FCS behaviour on loss, stale, or invalid input (behaviour TBD, e.g., hold-last/trim-safe TBD).

## 5. System Context

Pilot/operator inputs feed command shaping then the mode supervisor and law sets. Input health is annunciated to safety/HMI. Input-loss handling coordinates with the safety monitoring path.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
| REQ-HFPX-FCI-001 | The input system shall capture pilot/operator commands and deliver them to the FCS with defined integrity and timing (devices, signals, and budgets TBD, Vol 10/12). | FUN-002 | Analysis + HIL + Test (TBD) |
| REQ-HFPX-FCI-002 | The input system shall shape and limit commands to bounded FCS inputs (shaping functions, limits, and rates TBD). | FUN-002, HSA-002 | Analysis + SIL (TBD) |
| REQ-HFPX-FCI-003 | The input system shall protect against inadvertent inputs (protection means and criteria TBD). | HSA-002 | Analysis + Test (TBD) |
| REQ-HFPX-FCI-004 | The FCS shall execute defined behaviour on input loss, stale, or invalid data, including freeze/handling logic (behaviour, timeouts, and annunciation TBD). | FUN-002, HSA-002 | Analysis + SIL + HIL (TBD) |

No gains, bandwidths, margins, rates, or limits are stated. All quantitative content is TBD.

## 7. Architecture

Text block diagram:

```
[Pilot/Operator Devices (TBD, Vol 10/12)] --> [Capture + Validity Check (FCI-001, TBD)] --> [Shaping/Limiting (FCI-002, TBD)] --> [Inadvertent-Input Protection (FCI-003, TBD)] --> [FCS Laws / Supervisor]
                                                                                                    |
                                                                     [Input-Loss/Freeze Logic (FCI-004, TBD)] --> [Health Annunciation --> Safety / HMI]
```

Devices, signal lists, shaping curves, protection interlocks, and loss timeouts are TBD.

## 8. Detailed Design

Not applicable at Tranche 3 draft level. Device selection, transfer functions, limits, and state logic are TBD.

## 9. Interfaces

- Pilot/operator device ICD (Vol 10/12): TBD.
- Shaped-command output to laws/supervisor ICD: TBD.
- Health/status to safety and HMI ICD: TBD.

## 10. Operational Concept

Supports manned/unmanned command paths (roles TBD); nominal shaping provides bounded commands; inadvertent protection guards handling phases (TBD); loss/freeze preserves safe state pending recovery/handover (TBD).

## 11. Safety

Unbounded/corrupt/inadvertent commands or mishandled input loss are hazardous. Mitigations required (all TBD): integrity-checked capture (FCI-001), shaping/limiting (FCI-002), inadvertent-input protection (FCI-003), defined loss/freeze plus annunciation (FCI-004). No safety claim is made.

## 12. Performance

Capture latency, shaping dynamics, limit values, and loss-detection timing are TBD. No performance value is stated.

## 13. Verification & Validation

Verified by analysis, SIL/HIL with pilot/operator-in-the-loop stubs (TBD), and test including inadvertent-input and loss-injection cases (methods and pass criteria TBD).

## 14. Risks

- Device solution unknown (Vol 10/12); mitigation: device-agnostic TBD interface.
- Shaping/loss behaviour undefined; mitigation: explicit TBD with SIL/HIL validation planned.

## 15. Open Issues

- Devices TBD; shaping/limits TBD; inadvertent-protection means TBD; loss/freeze behaviour and timeouts TBD; verification methods TBD.

## 16. Assumptions

- A-FCI-001: Pilot/operator commands pass through a dedicated shaping/limiting stage before laws (validation: Vol 07/10 review, TBD).

## 17. Dependencies

Depends on FUN-002, HSA-002, FCR-005, Vol 10/12 devices, FCS architecture/laws, safety/HMI annunciation, Vol 19 rigs.

## 18. Traceability

Parents: FUN-002, HSA-002. Children: device selection, shaping design, V&V cases. RTM: REQ-HFPX-FCI-001..004 → CONCEPT.

## 19. Configuration

BL-0.0 (structure only) — Tranche 3 draft, not baselined. Changes by change record only.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 3 draft (Chapter 07.3) |
