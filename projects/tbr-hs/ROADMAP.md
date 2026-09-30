# TBR-HS — Roadmap

Tied to BOLTE Model. Strict gate: no human contact (wearable or radar) until safety + ethics review + both-founders sign-off. No build beyond sim/bench until AeroPulse-NG trial report + treasury review.

## Phase 0 — Spec (now)
- [x] SPEC.md + ARCHITECTURE.md + DATABASE.md + API.md
- [ ] Safety/ethics review board defined `[TBD]`; phantom-rig parts list `[TBD]`

## Phase 1 — Bench DSP (post-gate)
- Simulator → `SensorFrame` → FFT/Butterworth → scores/verdicts → headless HUD
- Recorded-capture regression; IFF forge/replay attack tests
- Exit: phantom heartbeat/resp detected at bench SNR, TRL 4 (no humans)

## Phase 2 — Sensor bring-up (lab, no humans)
- BLE/UWB ingest live; mmWave IQ on phantoms/obstacles (through-wall analog)
- Encrypted local DB + alert log; arc HUD on device
- Exit: bench detection + vitals-proxy scoring stable, TRL 5

## Phase 3 — Controlled pilot (only after safety gate)
- Approved subjects, medic present, opt-in consent, abort criteria
- Trial protocol `[TBD site/medic]`; independent safety observer
- Exit: pilot report or no-go with reasons
