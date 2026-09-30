# Product Pipeline (Post-NDAIE)

Prioritized against Goals 1/5/7 (defense-first, Nigerian-fit, buildable with 7-person team).

| Rank | Concept | Problem | Why BOLTE | Depends on |
|---|---|---|---|---|
| 2 | Secure field comms kit (offline mesh + encryption) | Tactical comms fragility | Reuses AeroPulse offline + systems skill | Phase 1 infra |
| 3 | Low-cost robotics/UGV scout | Logistics/surveillance gaps | EKF + autonomy reuse | Field trial learnings |
| 4 | Micro-weather station network | Harmattan/low-alt data | AWOS sidecar reuse | AeroPulse deployment |
| 5+ | Agriculture / Energy / Health adaptations | Per Goal 5 | Only after core traction | Phase 2+ |

## New concept specs (from Specification Overview PDF — spec-only, no code yet)

| Project | Repo | Domain | Status |
|---|---|---|---|
| ASOL — Armory Shift & Ordnance Log | [asol](https://github.com/garba-the-analyst/asol) | Tactical physical security & ordnance custody | Planning pack complete (`ARCHITECTURE` + `DATABASE` + `API` + `ROADMAP` + `RISKS`) |
| DAFV — Defense Asset & Firmware Verifier | [dafv](https://github.com/garba-the-analyst/dafv) | Supply-chain security & anti-tamper | Planning pack complete |
| C4ISR-DFE — Tactical C4ISR Data Fusion Engine | [c4isr-dfe](https://github.com/garba-the-analyst/c4isr-dfe) | Spatial intel & multi-sensor mapping | Planning pack complete |
| TBR-HS — Tactical Biometric Radar & Health System | [tbr-hs](https://github.com/garba-the-analyst/tbr-hs) | Vitals telemetry & micro-Doppler | Planning pack complete (safety review before human testing) |

Gate: no new build until AeroPulse-NG trial report + treasury review.

## Long-horizon programme (separate track — not ranked above)

| Project | Folder | Domain | Status |
|---|---|---|---|
| HFP-X — Human Flight Platform | [bolte-hfp](https://github.com/garba-the-analyst/bolte-hfp) | Piloted VTOL/transition flight, distributed jet propulsion | Concept BL-0.0; Tranche 1 backbone drafts; unmanned-first MVP; stage gates per REQ-HFPX-PGM-003 |
