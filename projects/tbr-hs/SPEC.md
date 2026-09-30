# TBR-HS — Specification (single source of truth)

Source: Specification Overview PDF §4 + AI Agent Prompt Block `SYSTEM_4`.

Use this file for architectural planning, database schema generation, API interface design, and implementation code construction.

## 1. Identity
- **Name:** Tactical Biometric Radar & Health System (TBR-HS)
- **Domain:** Personnel Vitals Telemetry & Micro-Doppler Motion Detection
- **Type:** Standalone software project (4 of 4 in export)

## 2. Purpose
Squad vitals telemetry (HR/HRV/Trauma), mmWave micro-Doppler through-wall cardiac motion detection, cryptographic IFF disambiguation, 60–180 degree radar HUD.

## 3. Operational scope
Wearable squad health tracking paired with obstacle-penetrating micro-Doppler radar. Calculates trauma/shock scores for friendly forces while detecting through-wall human motion (heartbeat/respiration) and using cryptographic IFF to distinguish friend from foe on a directional HUD.

## 4. Tech stack
- C++/Rust signal processing pipeline (FFT & Butterworth bandpass filtering)
- BLE/UWB sensor interface
- Ed25519 signed mesh tokens
- Real-time radar HUD arc interface

## 5. BOLTE constraints
- Safety, testing discipline, and documentation before any deployment or human testing.
- Lawful users only; defensive posture; human decision-maker in the loop.
- Local maintainability; TRL honesty: concept stage.

## 6. Downstream agent instruction
`INSTRUCTION_FOR_AGENT: Use this specification as the single source of truth for architectural planning, database schema generation, API interface design, and implementation code construction.`
