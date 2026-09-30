# ASOL — Product Brief (Concept)

Source: `projects/asol/` (`README.md` + `SPEC.md`). Spec only — no code yet.

## Problem
Armory custody runs on paper ledgers: check-in/out is slow to audit, single-custodian handovers create accountability gaps, and unfit personnel can draw equipment unchecked.

## Solution
Air-gapped, local-first armory desk: weapon/ammunition check-in/out with barcode + UHF RFID, enforced dual-custodian shift handovers, and liveness/fitness-for-duty pulse check before release. SQLite + SQLCipher (AES-256), Rust/C++ runtime, Tauri/Qt GUI.

## Status / Evidence
Concept, TRL 1–2. Next: architecture + DB schema + API from `SPEC.md`, then encrypted-DB → ingest → handover → liveness-gate prototype.

## Standards & compliance
Lawful users only, dual-custodian accountability, human in the loop for release. MIT/Apache deps for core.

## Cost & impact
Replaces paper with auditable offline custody; locally maintainable.

## Next 90 days
SPEC expansion only (gated: no build until AeroPulse-NG trial report + treasury review).
