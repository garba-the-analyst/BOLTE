# TBR-HS — API / Interface Design

## SensorFrame (single ingest contract)
```c
struct SensorFrame { int64_t t_ms; uint8_t channel; float *samples; size_t n; };
```
BLE/UWB drivers, capture files, and simulator all emit `SensorFrame`s; DSP never branches on source.

## DSP verbs (core library)
| Verb | Inputs | Outputs |
|---|---|---|
| `vitals_update(frames)` | BLE/UWB window | `{hr_bpm, hrv_ms, trauma_score, confidence, quality}` |
| `radar_scan(iq_window)` | mmWave IQ window | `[{arc_deg, range_m, band, snr_db, verdict}]` |
| `iff_verify(token)` | Ed25519 token | `friend(subject_id) \| unknown` |
| `hud_snapshot()` | — | `{vitals_ring[], motion_wedges[], alerts[]}` for 60–180° arc |
| `replay(capture)` | recorded/sim file | deterministic snapshot stream (tests/demos) |

## IFF token (mesh)
```json
{"subject":"…","epoch":0,"nonce":"…","signature":"ed25519:…"}
```
Epoch-rotated, replay-resistant; verification is offline against `subjects.iff_pubkey`.

## HUD contract
Arc 60–180° configurable; wedges show `POSSIBLE` (hollow) vs `MOTION` (solid) + SNR; vitals ring shows `STABLE|WATCH|URGENT` per IFF subject + trend arrow. No auto-triage text — advisory labels only.

## CLI (bench)
` tbr-hs replay --capture … | iff gen|verify | hud --headless ` mirrors GUI pipeline for SSH/bench use.
