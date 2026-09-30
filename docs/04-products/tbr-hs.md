# TBR-HS — Product Brief (Concept)

Source: [tbr-hs](https://github.com/garba-the-analyst/tbr-hs) repo (planning pack: `ARCHITECTURE` + `DATABASE` + `API` + `ROADMAP` + `RISKS`). Spec only — no code yet.

## Problem
Squad health degrades silently in the field, and through-wall human presence is invisible without a way to separate friend from foe.

## Solution
Wearable vitals (BLE/UWB) + micro-Doppler radar: C++/Rust FFT + Butterworth bandpass chain → HR/HRV/trauma-shock scores for friendlies + heartbeat/respiration through-wall detection → Ed25519 signed IFF tokens on a 60–180° radar HUD arc.

## Status / Evidence
Concept, TRL 1–2. Next: signal chain + vitals schema + IFF token design. Safety + ethics review mandatory before any human testing.

## Standards & compliance
Safety/testing discipline before deployment, lawful users only, human decision-maker in the loop.

## Cost & impact
Early trauma flagging + IFF-disambiguated sensing on commodity sensors.

## Next 90 days
SPEC expansion only (gated: no build until AeroPulse-NG trial report + treasury review).
