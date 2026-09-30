# Tactical C4ISR Data Fusion Engine (C4ISR-DFE)

> Spatial intelligence & multi-sensor tactical mapping — real-time command dashboard for vehicles and bunkers over lossy links.

- **Status:** Concept, TRL 1–2. Spec only — no code yet.
- **Source:** Specification Overview PDF, System 3/4.
- **BOLTE fit:** Goal 1 (situational awareness), Goal 5 (computing & AI / communications), reuses AeroPulse-NG fusion + offline-first lessons.

## What it does
Real-time operational command dashboard for tactical vehicles and bunkers. Ingests ADS-B flight feeds, UAV video coordinates, RF signal triangulation, and troop GPS tracks over lossy, low-bandwidth links.

## Tech stack (from spec)
Rust/Node.js telemetry pipeline, PostGIS / SQLite R*Tree spatial database, MBTiles offline vector tile engine (Leaflet/Maplibre), Protocol Buffers, and compressed UDP delta mesh sync.

## Structure
```
c4isr-dfe/
  README.md         # this file
  SPEC.md           # single source of truth (from PDF export)
  ARCHITECTURE.md   # fusion + mesh design
  DATABASE.md       # spatial schema (R*Tree → PostGIS)
  API.md            # protobuf deltas + query API
  ROADMAP.md        # phased plan
  RISKS.md          # risk register
  docs/ + src/      # created when code starts
```

## Next steps
1. Define pilot MBTiles region + fixture scripts `[TBD]`.
2. Prototype after gate: normalize → fuse → tile render, then UDP mesh.
3. Coordinate with AeroPulse-NG ADS-B feed for reuse.

See `SPEC.md` for the full exported specification.
