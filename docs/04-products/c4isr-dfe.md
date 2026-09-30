# C4ISR-DFE — Product Brief (Concept)

Source: `projects/c4isr-dfe/` (`README.md` + `SPEC.md`). Spec only — no code yet.

## Problem
Tactical vehicles/bunkers lack a unified offline picture — ADS-B, UAV coords, RF bearings, and troop GPS arrive on separate tools and die on lossy links.

## Solution
Real-time command dashboard: Rust/Node.js telemetry pipeline → PostGIS / SQLite R*Tree spatial DB → MBTiles offline vector tiles (Leaflet/Maplibre) → Protocol Buffers + compressed UDP delta mesh sync.

## Status / Evidence
Concept, TRL 1–2. Next: telemetry schema + spatial schema + sync protocol. Reuse AeroPulse-NG ADS-B feed where possible.

## Standards & compliance
Defensive situational-awareness posture, human in the loop, lawful users only. Offline-first, lossy-link tolerant.

## Cost & impact
One offline map for dispersed units; builds on AeroPulse fusion lessons.

## Next 90 days
SPEC expansion only (gated: no build until AeroPulse-NG trial report + treasury review).
