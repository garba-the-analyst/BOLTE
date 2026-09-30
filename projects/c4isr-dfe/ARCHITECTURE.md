# C4ISR-DFE — Architecture

Connective tissue for the tactical fusion pipeline. Source: `SPEC.md`. Reuses AeroPulse-NG lessons (offline-first, deterministic replay, R*Tree).

## 1. Guiding constraints
1. **Offline-first, lossy-link tolerant.** No feature may require internet. Consequence: MBTiles on device, store-and-forward sync, operator clock + Lamport/sequence reconciliation.
2. **One normalize path.** ADS-B, UAV coords, RF bearings, and GPS tracks all normalize into `TrackReport{source, id, time, position, confidence}` — sim fixtures and live feeds execute identical fusion below ingest.
3. **Deterministic fusion core, async edge.** Fusion (associate → track → event) is a pure function of ordered reports: replays reproducible. Rust/Node edge owns radios, clocks, UDP.
4. **Delta sync, not full state.** Peers exchange compressed protobuf deltas over UDP; full snapshots only on join. Human stays in loop for operational judgments.

## 2. Data flow
```text
Ingest (ADS-B feed · UAV video coords · RF triangulation · troop GPS · fixture sim)
        │  TrackReport stream (queued, time-ordered)
        ▼
┌─ fuse(tick) ──────────────────────────────────────────────┐
│ 1 associate (nearest + Mahalanobis gate, R*Tree index)    │
│ 2 track update (constant-velocity filter, coast on gaps)  │
│ 3 event scan (geofence, proximity, silence/dark, SOS)     │
│ 4 materialise FusedPicture{tracks · events · areas}       │
└───────────────────────────────────────────────────────────┘
   ▼ local render + ▼ protobuf delta → UDP mesh → peers
┌──────────────────────┐      ┌────────────────────────────────┐
│ Offline map (MBTiles │      │ Compressed UDP delta mesh sync │
│ Leaflet/Maplibre)    │      │ seq + ack + store-and-forward  │
└──────────────────────┘      └────────────────────────────────┘
```

## 3. Key decisions
| Decision | Rationale | Alternative rejected |
|---|---|---|
| SQLite R*Tree now, PostGIS later | single-file deploy for vehicles/bunkers; PostGIS for fixed HQ when infra exists | PostGIS everywhere (ops weight) |
| MBTiles offline vectors | zero-network maps; pre-cut regions on media | Online tiles (fails air-gapped) |
| Protobuf + UDP deltas | tiny payloads on lossy links; schema evolution | JSON over TCP (chatty, fragile) |
| Rust core + Node edge | Rust fusion safety/perf; Node for rapid dashboard iteration | Single-language monolith (slower UI or slower core) |
| Reuse AeroPulse ADS-B path | one decode discipline (sim == live), proven CPR/EKF patterns | Second ADS-B stack (drift risk) |

## 4. Sync semantics
Messages idempotent + sequence-numbered; joins request snapshot then deltas; conflicts last-writer-wins per field with operator-visible merge flags. No silent overwrites of casualty/SOS events — those are append-only.

## 5. Testing philosophy
Fixture replays (multi-sensor scripts with known fuses), partition/chaos tests (drop/duplicate/reorder UDP), tile-offline tests, R*Tree integrity at scale. One-command battery when code starts.
