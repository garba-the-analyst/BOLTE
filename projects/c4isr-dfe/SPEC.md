# C4ISR-DFE — Specification (single source of truth)

Source: Specification Overview PDF §3 + AI Agent Prompt Block `SYSTEM_3`.

Use this file for architectural planning, database schema generation, API interface design, and implementation code construction.

## 1. Identity
- **Name:** Tactical C4ISR Data Fusion Engine (C4ISR-DFE)
- **Domain:** Spatial Intelligence & Multi-Sensor Tactical Mapping
- **Type:** Standalone software project (3 of 4 in export)

## 2. Purpose
Spatial intelligence, ADS-B/RF/UAV sensor data fusion, low-bandwidth delta mesh sync, offline vector mapping.

## 3. Operational scope
Real-time operational command dashboard for tactical vehicles and bunkers. Ingests ADS-B flight feeds, UAV video coordinates, RF signal triangulation, and troop GPS tracks over lossy, low-bandwidth links.

## 4. Tech stack
- Rust/Node.js telemetry pipeline
- PostGIS / SQLite R*Tree spatial database
- MBTiles offline vector tile engine (Leaflet/Maplibre)
- Protocol Buffers
- Compressed UDP delta mesh sync

## 5. BOLTE constraints
- Offline-first; lossy-link tolerant; deterministic replay where feasible.
- Lawful users only; human in the loop for operational judgments.
- Defensive/situational-awareness posture.
- TRL honesty: concept stage.

## 6. Downstream agent instruction
`INSTRUCTION_FOR_AGENT: Use this specification as the single source of truth for architectural planning, database schema generation, API interface design, and implementation code construction.`
