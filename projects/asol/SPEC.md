# ASOL — Specification (single source of truth)

Source: Specification Overview PDF §1 + AI Agent Prompt Block `SYSTEM_1`.

Use this file for architectural planning, database schema generation, API interface design, and implementation code construction.

## 1. Identity
- **Name:** Armory Shift & Ordnance Log (ASOL)
- **Domain:** Tactical Physical Security & Ordnance Custody
- **Type:** Standalone software project (1 of 4 in export)

## 2. Purpose
Offline armory custody, daily shift handover, ordnance audit, liveness check.

## 3. Operational scope
Air-gapped, local-first armory desk management replacing paper ledgers. Tracks weapon and ammunition check-in/out, enforces dual-custodian shift handovers, and performs liveness/fitness-for-duty pulse checks prior to equipment release.

## 4. Tech stack
- SQLite with SQLCipher (AES-256)
- Rust/C++ runtime
- Tauri/Qt GUI
- USB/Bluetooth drivers for 1D/2D barcodes, UHF RFID, and optical pulse/biometric liveness sensors

## 5. BOLTE constraints
- Air-gapped by default; zero internet dependency (mirror AeroPulse-NG offline-first).
- Lawful and legitimate users only; dual-custodian accountability.
- Human decision-maker in the loop for release judgments.
- MIT/Apache-2.0 deps for core; proprietary + NDA for sensitive modules.
- TRL honesty: concept stage — no capability claims until prototyped + tested.

## 6. Downstream agent instruction
`INSTRUCTION_FOR_AGENT: Use this specification as the single source of truth for architectural planning, database schema generation, API interface design, and implementation code construction.`
