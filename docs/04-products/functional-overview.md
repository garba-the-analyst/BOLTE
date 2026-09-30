# Products — Functional Overview (user-facing, website source)

Consolidates `projects/*/SPEC.md` + `ARCHITECTURE.md` + `API.md` (plus `projects/BOLTE HFP/` charter/mission docs) into what each product *does for a user*. No internals beyond published briefs. TRL honesty enforced.

## AeroPulse-NG — Prototype v2.4.0, TRL 4–5 (flagship)
- **Users:** secondary-aerodrome ATC-adjacent operators, tactical air-picture users, trainees.
- **Functions:** ingest 1090 MHz ADS-B/Mode S + 131.55 MHz ACARS → decode → 6-state filter + dead reckoning → STCA conflict alert (Doc 4444 5NM/1000ft advisory) → 3-source weather fusion → defence overlays (7500/7600/7700, dark/silence, geofence, intercept solver) → dual-window display + headless console + DuckDB record + synthetic-feed demo mode.
- **Offline:** air-gapped by contract; sim == live decode path; deterministic replay.
- **Limits (public):** synthesized FFT now, real RTL-SDR I/Q next; single-site now; cooperative targets primarily.

## ASOL — Concept TRL 1–2, spec-only
- **Users:** armory desk (armorer + duty officer + auditor).
- **Functions:** register item → check-out (dual-custodian + fresh liveness) → check-in → shift handover (dual-out + dual-in signatures + count reconcile) → quarantine/dispose → signed audit export → `verify_chain`.
- **Offline:** SQLCipher AES-256 local DB, hash-chained journal, removable-media export only.

## DAFV — Concept TRL 1–2, spec-only
- **Users:** depot receiving-dock auditor/operator.
- **Functions:** acquire image (JTAG/UART/USB/file) → dual-hash (BLAKE3 + SHA-256) → manifest issue → Ed25519 verify → RFID provision/bind → PASS/FAIL/INCONCLUSIVE verdict + evidence → signed report. Never auto-flashes.
- **Offline:** static Rust binary, local trust roots, content-addressed store.

## C4ISR-DFE — Concept TRL 1–2, spec-only
- **Users:** vehicle/bunker command users.
- **Functions:** ingest ADS-B/UAV-coords/RF-bearings/GPS tracks → normalize to TrackReport → associate/track/coast → geofence/proximity/silence/SOS events → offline MBTiles map → compressed protobuf UDP delta mesh sync → export snapshot.
- **Offline:** MBTiles on device, store-and-forward, idempotent sequenced deltas.

## TBR-HS — Concept TRL 1–2, spec-only, safety-gated
- **Users:** squad + medic (advisory only, human decides).
- **Functions:** BLE/UWB ingest → Butterworth + FFT DSP → vitals scores (STABLE/WATCH/URGENT + confidence) + radar motion verdicts (NO_MOTION/POSSIBLE/MOTION + arc/SNR) → Ed25519 IFF friend/unknown → 60–180° HUD + encrypted alert log + bench replay.
- **Safety:** phantoms before people; no human contact until safety/ethics review + both-founders sign-off; advisory labels only, never auto-triage.

## HFP-X — Concept BL-0.0, structure-only, evidence-gated
- **Users:** test pilots (long-term), ground crew, ground station, regulators, test range.
- **Functions:** vertical take-off → controlled hover → transition ↔ horizontal cruise → landing, across 15 mission modes + emergency stabilisation/recovery states; mission telemetry to ground station throughout; independent emergency recovery for defined failures.
- **Programme:** 34-volume doc tree (requirements → architecture → propulsion/avionics/safety → verification → flight test → certification → operations → sustainment) + separate unmanned-first MVP demonstrator (Vol 33); human flight only after unmanned hover/transition/cruise evidence gates.
- **Limits (public):** all performance values TBD; no design selected; propulsion/airframe options are unstarted trade studies; nothing claimed standards-compliant.

Gate for all concepts: no build beyond paper/bench-sim until AeroPulse-NG trial report + treasury review. (HFP-X additionally gated stage-by-stage per REQ-HFPX-PGM-003; no build/ignition/operation outside controlled conditions.)
