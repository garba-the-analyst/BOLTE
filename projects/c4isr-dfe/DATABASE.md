# C4ISR-DFE — Database Schema (SQLite R*Tree → PostGIS later)

Local-first. HQ may mirror to PostGIS with identical logical schema. Times INTEGER ms. Positions WGS-84 degrees + ENU metres cached.

```sql
CREATE TABLE sensors (
  id TEXT PRIMARY KEY,          -- station/vehicle/uav/gps-unit id
  kind TEXT NOT NULL,           -- ADSB|UAV|RF|GPS|SIM
  last_seen INTEGER, health TEXT NOT NULL DEFAULT 'OK'
);

CREATE TABLE tracks (
  id TEXT PRIMARY KEY,          -- fused track id (stable)
  source_ids TEXT NOT NULL,     -- JSON: contributing report ids
  lat REAL NOT NULL, lon REAL NOT NULL, alt_m REAL,
  vx REAL, vy REAL,              -- m/s ENU estimate
  confidence REAL NOT NULL,
  updated_at INTEGER NOT NULL
);

-- Spatial index (SQLite R*Tree virtual table shadowing tracks)
CREATE VIRTUAL TABLE tracks_rt USING rtree(id, minLat, maxLat, minLon, maxLon);

CREATE TABLE reports (
  id TEXT PRIMARY KEY,
  sensor_id TEXT NOT NULL REFERENCES sensors(id),
  track_hint TEXT,              -- claimed id, nullable (fusion decides)
  lat REAL NOT NULL, lon REAL NOT NULL, alt_m REAL,
  accuracy_m REAL, created_at INTEGER NOT NULL
);
CREATE INDEX idx_reports_time ON reports(created_at);

CREATE TABLE events (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,           -- GEOFENCE|PROXIMITY|SILENCE|SOS|MERGE_FLAG
  track_id TEXT REFERENCES tracks(id),
  detail TEXT NOT NULL,         -- JSON payload
  created_at INTEGER NOT NULL
);
CREATE INDEX idx_events_kind ON events(kind);

CREATE TABLE mesh_peers (
  peer_id TEXT PRIMARY KEY,
  last_seq INTEGER NOT NULL DEFAULT 0,
  last_contact INTEGER
);

CREATE TABLE sync_log (
  seq INTEGER PRIMARY KEY AUTOINCREMENT,
  msg_hash TEXT NOT NULL, kind TEXT NOT NULL,
  created_at INTEGER NOT NULL
);
```

PostGIS migration: `tracks` → `GEOGRAPHY(PointZ)`, `tracks_rt` → GiST index; all else identical. SOS/casualty events append-only, never updated in place.
