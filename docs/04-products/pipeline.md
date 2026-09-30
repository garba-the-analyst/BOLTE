# Product Pipeline (Post-NDAIE)

Prioritized against Goals 1/5/7 (defense-first, Nigerian-fit, buildable with 7-person team).

| Rank | Concept | Problem | Why BOLTE | Depends on |
|---|---|---|---|---|
| 2 | Secure field comms kit (offline mesh + encryption) | Tactical comms fragility | Reuses AeroPulse offline + systems skill | Phase 1 infra |
| 3 | Low-cost robotics/UGV scout | Logistics/surveillance gaps | EKF + autonomy reuse | Field trial learnings |
| 4 | Micro-weather station network | Harmattan/low-alt data | AWOS sidecar reuse | AeroPulse deployment |
| 5+ | Agriculture / Energy / Health adaptations | Per Goal 5 | Only after core traction | Phase 2+ |

## New concept specs (from Specification Overview PDF — spec-only, no code yet)

| Project | Folder | Domain | Next design step |
|---|---|---|---|
| ASOL — Armory Shift & Ordnance Log | `projects/asol/` | Tactical physical security & ordnance custody | Architecture + DB schema + API from `SPEC.md` |
| DAFV — Defense Asset & Firmware Verifier | `projects/dafv/` | Supply-chain security & anti-tamper | Manifest format + verification flow |
| C4ISR-DFE — Tactical C4ISR Data Fusion Engine | `projects/c4isr-dfe/` | Spatial intel & multi-sensor mapping | Telemetry + spatial schema + sync protocol |
| TBR-HS — Tactical Biometric Radar & Health System | `projects/tbr-hs/` | Vitals telemetry & micro-Doppler | Signal chain + vitals schema + IFF tokens (safety review before human testing) |

Gate: no new build until AeroPulse-NG trial report + treasury review.

## Long-horizon programme (separate track — not ranked above)

| Project | Folder | Domain | Status |
|---|---|---|---|
| HFP-X — Human Flight Platform | `BOLTE HFP/` | Piloted VTOL/transition flight, distributed jet propulsion | Concept BL-0.0; Tranche 1 backbone drafts; unmanned-first MVP; stage gates per REQ-HFPX-PGM-003 |
