# Armory Shift & Ordnance Log (ASOL)

> Tactical physical security & ordnance custody — air-gapped, local-first armory desk management replacing paper ledgers.

- **Status:** Concept, TRL 1–2. Spec only — no code yet.
- **Source:** Specification Overview PDF, System 1/4 (`CONTEXT_TYPE: SOFTWARE_SPECIFICATION_EXPORT, DOMAIN: AEROSPACE_DEFENSE_TACTICAL_SOFTWARE`).
- **BOLTE fit:** Goal 1 (indigenous defense & security tech), Goal 7 (built FOR Nigeria — works offline through outages), Goal 3 (idea → prototype pipeline).

## What it does
Tracks weapon and ammunition check-in/out, enforces dual-custodian shift handovers, and performs liveness / fitness-for-duty pulse checks prior to equipment release.

## Tech stack (from spec)
SQLite with SQLCipher (AES-256), Rust/C++ runtime, Tauri/Qt GUI, USB/Bluetooth drivers for 1D/2D barcodes, UHF RFID, and optical pulse/biometric liveness sensors.

## Structure
```
asol/
  README.md         # this file
  SPEC.md           # single source of truth (from PDF export)
  ARCHITECTURE.md   # custody pipeline design
  DATABASE.md       # SQLCipher schema
  API.md            # IPC/CLI + driver interface
  ROADMAP.md        # phased plan
  RISKS.md          # risk register
  docs/ + src/      # created when code starts
```

## Next steps
1. Domain walkthrough with armory adviser `[TBD]`; validate handover flow.
2. Prototype after gate: encrypted DB → ingest → handover → liveness gate.
3. Field validation plan + trial partner `[TBD]`.

See `SPEC.md` for the full exported specification.
