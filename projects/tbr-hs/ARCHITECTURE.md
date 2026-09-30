# TBR-HS — Architecture

Connective tissue for the vitals + micro-Doppler pipeline. Source: `SPEC.md`. Safety-critical: no human testing until ethics + safety review passes.

## 1. Guiding constraints
1. **Bench-first, humans last.** No wearable/radar contact with people until bench phantoms + safety review + founders sign-off. Consequence: simulator generates vitals + radar returns through the same pipeline from day one.
2. **One signal path.** BLE/UWB packets, recorded captures, and simulator frames all normalize into `SensorFrame{time, channel, samples}` — sim and live execute identical DSP below the antenna/sensor.
3. **Separate vitals from detection.** Trauma/shock scoring (friendlies, IFF-signed) and through-wall motion detection (unknowns) are independent chains that meet only at the HUD. A detection is never auto-labeled friendly without a valid IFF token.
4. **Advisory only.** Scores and arcs inform a human; system never triages, never targets.

## 2. Data flow
```text
Wearables (BLE/UWB HR/HRV) · mmWave micro-Doppler IQ · IFF mesh tokens · simulator
        │  SensorFrame stream (queued, time-ordered)
        ▼
┌─ dsp(tick) ─────────────────────────────────────────────────┐
│ A. Vitals chain: Butterworth bandpass → HR/HRV → shock/     │
│    trauma score + confidence (IFF-signed subjects only)     │
│ B. Radar chain: FFT → clutter cancel → heartbeat/resp bands │
│    → motion verdict (range arc, SNR, persistence)           │
│ C. IFF check: Ed25519 token verify → friend/unknown tag     │
└─────────────────────────────────────────────────────────────┘
        ▼ VitalsSnapshot + RadarArcs → directional HUD (60–180°)
┌──────────────────┐      ┌──────────────────┐
│ Squad HUD arc    │      │ Alert log (local │
│ vitals ring +    │      │ encrypted DB)    │
│ motion wedges    │      │                  │
└──────────────────┘      └──────────────────┘
```

## 3. Key decisions
| Decision | Rationale | Alternative rejected |
|---|---|---|
| C++/Rust DSP core | FFT/filter perf + safety; Rust boundary for mesh/DB | Python DSP in loop (jitter, GIL) |
| Butterworth bandpass + FFT | proven cardiac/resp separation (0.1–2 Hz motion, ~1–2 Hz cardiac harmonics); inspectable | Black-box ML scorer first (unverifiable at TRL 1–2) |
| BLE/UWB both | BLE for vitals ubiquity, UWB for ranging/time-sync | Single radio (loses redundancy) |
| Ed25519 IFF mesh tokens | offline friend/unknown disambiguation, replay-resistant | Plain IDs (spoofable) |
| 60–180° arc HUD (not 360°) | directional antenna reality; honest FOV prevents false confidence | Full-circle display (implies coverage we lack) |

## 4. Score / verdict semantics
Vitals: `STABLE | WATCH | URGENT` + confidence + trend (never a diagnosis). Radar: `NO_MOTION | POSSIBLE (low SNR/transient) | MOTION (persistent, in-band)` + range arc + SNR. HUD shows both; unknown motion never labeled friendly.

## 5. Testing philosophy
Phantom rigs (mechanical heartbeat/resp simulators), recorded-capture regression, IFF forge/replay attacks, RF-interference soaks. Human testing only after safety review. One-command battery when code starts.
