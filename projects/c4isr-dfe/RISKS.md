# C4ISR-DFE — Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Mesh floods lossy link / sync storm | M | High | Delta-only, rate caps, backpressure, snapshot-on-join only | `[TBD]` |
| Clock skew splits tracks (same target, two ids) | M | High | Sequence + time-window association, merge flags visible to operator | `[TBD]` |
| Stale map misleads (old MBTiles) | M | Med | Region manifest hashes + expiry banner; never render unknown as empty | `[TBD]` |
| OPSEC leak via sync (positions broadcast) | M | Critical | Pairing keys, peer allowlist, SOS-only burst mode, radio discipline SOP | Founders |
| GPS spoof / RF false fix poisons fusion | M | High | Confidence weighting, multi-source corroboration, quarantine outliers | `[TBD]` |
| Scope creep into weapons control | L | Critical | Situational-awareness only; no fire-control interfaces; founders gate | Founders |

Posture: defensive/situational-awareness only; human in loop; lawful users; both-founders approval for security partnerships.
