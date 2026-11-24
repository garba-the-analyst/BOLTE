# TBR-HS — Product Brief (Designed, beyond concept)

Source: [tbr-hs](https://github.com/garba-the-analyst/tbr-hs) repo (planning pack: `ARCHITECTURE` + `DATABASE` + `API` + `ROADMAP` + `RISKS`). Design complete (architecture, signal chain, data model, interfaces); no code yet.

## What it is
A motion sensor that uses microwave signals, which the human body absorbs, to track the movement of nearby people, including through barriers. Positions appear on a screen like a minimap. Uses: tracking enemy movement at the frontline, and locating people in search-and-rescue missions. Tracking personnel health with wearable vitals is an added feature, not the core.

## Problem
At the frontline a squad cannot see who is moving behind a wall or around a corner, and friend and foe are hard to tell apart. In search and rescue, finding people trapped behind obstacles costs critical time.

## Solution
Micro-Doppler radar signal chain (C++/Rust FFT + Butterworth bandpass) detects movement and presence, plotted on a 60–180° radar HUD arc (the minimap), with Ed25519 signed IFF tokens to separate friendly from unknown. Optional wearable vitals (BLE/UWB) add advisory HR/HRV/trauma-shock scores for friendlies.

## Status / Evidence
Designed, beyond concept: architecture, DSP chain, data model and API are written. Next: bench simulation (no people involved). Safety + ethics review mandatory before any human testing.

## Standards & compliance
Safety/testing discipline before deployment, lawful users only, human decision-maker in the loop.

## Cost & impact
Early trauma flagging + IFF-disambiguated sensing on commodity sensors.

## Next 90 days
Bench simulation of the signal chain through to the minimap display (gated: no build beyond simulation until AeroPulse-NG trial report + treasury review).
