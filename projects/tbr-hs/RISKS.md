# TBR-HS — Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| False URGENT trauma score causes panic / wrong triage | M | Critical | Advisory labels only, confidence + trend shown, medic owns decisions, never auto-triage | `[TBD medic]` |
| Through-wall false positive (fan, animal, multipath) | H | High | Persistence + SNR gates, POSSIBLE vs MOTION tiers, clutter-cancel calibration | `[TBD]` |
| IFF spoof / replay marks foe as friend | M | Critical | Epoch nonces, short validity, unknown-by-default; failed verify → unknown wedge | Founders |
| RF overexposure / wearable skin risk in testing | L | Critical | Power limits, duty-cycle caps, safety review + abort criteria before any human contact | Founders |
| Privacy violation (biometric storage/leak) | M | High | Derived metrics only, ≤60 s waveform ring-buffer, encrypted DB, no export without consent | `[TBD]` |
| Scope creep into targeting/fire-control | L | Critical | Sensing + advisory only; no weapon interfaces ever; founders gate | Founders |

Safety rule: phantoms before people; medic present for any human contact; both-founders written approval required for security-institution testing.
