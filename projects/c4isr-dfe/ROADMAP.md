# C4ISR-DFE — Roadmap

Tied to BOLTE Model. Gated: prototype sync work may start in lab, but field radios only after AeroPulse-NG trial report + treasury review.

## Phase 0 — Spec (now)
- [x] SPEC.md + ARCHITECTURE.md + DATABASE.md + API.md
- [ ] Region pack list for MBTiles pilot area `[TBD]`; fixture scripts defined

## Phase 1 — Lab fusion (post-gate)
- `TrackReport` normalize + associate + coast; R*Tree index; fixture replay == live path
- Single-node dashboard on MBTiles (no mesh yet)
- Exit: multi-sensor script fuses to known picture, TRL 4

## Phase 2 — Mesh
- Protobuf deltas over UDP; loss/dupe/reorder chaos tests; 2-node store-and-forward
- Exit: 2-station bench sync with partition recovery, TRL 5

## Phase 3 — Vehicle/bunker pilot
- Hardened ingest adapters; RF + GPS live; snapshot export carry
- Trial at `[TBD site]`; OPSEC review of what syncs
- Exit: pilot report, TRL 6
