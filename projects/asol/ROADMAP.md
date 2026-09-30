# ASOL — Roadmap

Tied to BOLTE Model: Problem → Idea → Research → Engineering → Prototype → Testing → Improvement → Deployment → Impact. Gated: no build beyond paper prototype until AeroPulse-NG trial report + treasury review.

## Phase 0 — Spec (now)
- [x] SPEC.md single source of truth (from PDF export)
- [x] ARCHITECTURE.md + DATABASE.md + API.md (this set)
- [ ] Armory workflow walkthrough with 1–2 domain advisers `[TBD]`; paper forms mapped to schema

## Phase 1 — Prototype (post-gate)
- Encrypted DB + journal + `verify_chain`; CLI `register/check_out/check_in`
- Simulated barcode/RFID/pulse drivers (sim == live path)
- Dual-custodian + liveness-gate enforcement + failing tests for bypass attempts
- Exit: bench demo (10 items, full shift cycle, signed export verifies), TRL 4

## Phase 2 — Pilot (field)
- Real USB/BT barcode + UHF RFID bring-up; optical pulse sensor integration
- Desk GUI (Tauri/Qt); print log; power-loss recovery test
- Trial at `[TBD armory]`; audit by independent count
- Exit: trial report, TRL 6

## Phase 3 — Harden & scale
- Key backup/rotation procedure, multi-desk merge via signed files, training pack
- Exit: deployable kit + maintainer guide
