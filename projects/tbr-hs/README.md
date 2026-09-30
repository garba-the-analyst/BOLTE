# Tactical Biometric Radar & Health System (TBR-HS)

> Personnel vitals telemetry + micro-Doppler motion detection — squad health tracking paired with through-wall radar + cryptographic IFF.

- **Status:** Concept, TRL 1–2. Spec only — no code yet.
- **Source:** Specification Overview PDF, System 4/4.
- **BOLTE fit:** Goal 1 (protective tech / situational awareness), Goal 5 (healthcare + defense dual-use), Goal 7 (field-maintainable).

## What it does
Wearable squad health tracking paired with obstacle-penetrating micro-Doppler radar. Calculates trauma/shock scores for friendly forces while detecting through-wall human motion (heartbeat/respiration) and using cryptographic IFF to distinguish friend from foe on a directional HUD.

## Tech stack (from spec)
C++/Rust signal processing pipeline (FFT & Butterworth bandpass filtering), BLE/UWB sensor interface, Ed25519 signed mesh tokens, and real-time radar HUD arc interface (60–180 degree radar HUD).

## Structure
```
tbr-hs/
  README.md         # this file
  SPEC.md           # single source of truth (from PDF export)
  ARCHITECTURE.md   # DSP + IFF + HUD design
  DATABASE.md       # vitals/radar schema
  API.md            # SensorFrame + HUD contracts
  ROADMAP.md        # phased plan (safety-gated)
  RISKS.md          # risk register
  docs/ + src/      # created when code starts
```

## Next steps
1. Define safety/ethics review board + phantom-rig parts `[TBD]`.
2. Bench DSP after gate: sim → FFT/filter → scores → headless HUD (no humans).
3. Controlled pilot only after safety gate + founders sign-off.

See `SPEC.md` for the full exported specification.
