# C4ISR-DFE — API / Interface Design

## Protobuf deltas (UDP mesh)
```proto
message TrackDelta {
  string track_id = 1; double lat = 2; double lon = 3;
  double alt_m = 4; double vx = 5; double vy = 6;
  float confidence = 7; int64 updated_at_ms = 8; uint64 seq = 9;
}
message EventMsg {
  string id = 1; string kind = 2; string track_id = 3;
  string detail_json = 4; int64 created_at_ms = 5; uint64 seq = 6;
}
message SyncEnvelope { uint64 seq = 1; string peer_id = 2; bytes payload = 3; }
```
Compressed (zstd/delta), idempotent, sequence-numbered; receivers ack highest contiguous seq, request gaps.

## Local query API (dashboard / CLI)
| Verb | Inputs | Outputs |
|---|---|---|
| `ingest_report` | sensor_id, lat/lon/alt, accuracy, time | report id (queued for fusion) |
| `get_picture` | bbox, since_ms | FusedPicture{tracks, events} |
| `get_track` | track_id | track + history + events |
| `sync_status` | — | peers, last_seq, backlog |
| `export_picture` | bbox + range | signed snapshot file (offline carry) |
| `replay` | fixture file | deterministic fused output (tests/demos) |

## Ingest adapters
`adsb-adapter` (reuse AeroPulse decode), `uav-adapter` (video coord frames → lat/lon), `rf-adapter` (bearings → triangulated fix + ellipse), `gps-adapter` (troop tracks). All emit `TrackReport`; all ship a `sim` mode through the same path.

## Map contract
MBTiles packs by region (`region.mbtiles` + manifest hash). Renderer never fetches network; missing tiles render as grid + label, never blank-fail.
