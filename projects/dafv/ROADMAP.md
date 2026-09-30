# DAFV — Roadmap

Tied to BOLTE Model. Gated: no hardware probing beyond lab fixtures until AeroPulse-NG trial report + treasury review.

## Phase 0 — Spec (now)
- [x] SPEC.md + ARCHITECTURE.md + DATABASE.md + API.md
- [ ] Trust model review with founders (root custody, rotation, revocation) `[TBD]`

## Phase 1 — Lab prototype (post-gate)
- File-import path: hash → manifest issue → verify → report (no bus yet)
- Golden fixtures: valid / expired / forged / bit-flipped images
- Exit: `verify` PASS/FAIL/INCONCLUSIVE correct on fixtures, TRL 4

## Phase 2 — Bus + tags
- JTAG/UART/USB acquisition on sacrificial boards; RFID provision/read round-trip
- Depot-style receiving-dock dry run in lab
- Exit: end-to-end audit on real reads, TRL 5–6

## Phase 3 — Depot pilot
- Trial at `[TBD depot]`; operator training; signed-report acceptance flow
- Exit: pilot report + hardening list
