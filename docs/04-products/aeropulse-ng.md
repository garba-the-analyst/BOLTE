# AeroPulse-NG — Flagship Product Brief

Source: `projects/aeropulse-ng/` codebase (Rust + Tauri host, React 19 + Vite frontend, Python sidecar, DuckDB, SDR ingest).

## Problem
Secondary aerodromes/tactical sites lack affordable low-altitude surveillance; imports cost $M, fail in harmattan/outages, miss non-cooperative targets.

## Solution
Air-gapped offline-first engine: ~$150 SDR + PC → dual-window ATC/tactical workstation. Ingests 1090 MHz ADS-B/Mode S + 131.55 MHz ACARS; DF17/CPR/Gillham decode; 6-state EKF + dead reckoning; R*-tree STCA (Doc 4444 5NM/1000ft); 3-source weather fusion (AWOS > D-ATIS > METAR) + ISA/harmattan fallback; defence overlays (7500/7600/7700, dark-target/silence, geofence, intercept solver). Zero internet required.

## Architecture
- `src-tauri/`: tokio 60 Hz engine, 12 IPC commands, EngineSnapshot, queued ingest.
- Frontend: strict TS + React, Canvas radar (D1: rings/sweep/2525D/FDB/STCA), D2 strip-bay/weather/FFT/threat matrix; SI-metric units; headless ANSI + synthetic-feed dev mode.
- Sidecar: DuckDB recorder + RS-485 AWOS reader, pytest.
- One decode path: sim == live. Deterministic replay. MIT/Apache deps only.

## Status / Evidence
v2.4.0 feature-complete prototype; 108 checks green; demo scenarios (7700 @45s, <1km miss @70s, dropout @112s). Remaining: real I/Q + live FFT, AWOS wiring, DF20/21 Comm-B, alert/weather writers, multi-site/RBAC/offline tiles.

## Standards & compliance
Nig.CARs, ICAO Annex 2/5/10 Vol III, Doc 4444, DO-260B, HF-STD-010A, MIL-STD-2525D, NCAA SI-metric.

## Cost & impact
>$99% capex cut, locally maintainable, training/sovereignty multiplier, civil + defence dual-use.

## Next 90 days
Real I/Q tap → field trial → writers → trial report. Pitch needs no RF hardware (synthetic mode).
