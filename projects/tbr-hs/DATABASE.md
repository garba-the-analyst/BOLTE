# TBR-HS — Database Schema (SQLite, encrypted at rest)

Local-only. No raw biometrics leave the device. Vitals stored as derived metrics + quality, not waveforms beyond short debug windows. Times INTEGER ms.

```sql
CREATE TABLE subjects (
  id TEXT PRIMARY KEY,          -- squad member id (IFF-bound)
  callsign TEXT UNIQUE NOT NULL,
  iff_pubkey TEXT UNIQUE NOT NULL, -- Ed25519
  active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE vitals_samples (
  id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL REFERENCES subjects(id),
  hr_bpm REAL, hrv_ms REAL,
  trauma_score REAL,            -- 0..1 derived, advisory only
  confidence REAL NOT NULL,
  quality TEXT NOT NULL,        -- GOOD|DEGRADED|BAD
  created_at INTEGER NOT NULL
);
CREATE INDEX idx_vitals_subj ON vitals_samples(subject_id);

CREATE TABLE radar_detections (
  id TEXT PRIMARY KEY,
  arc_deg REAL NOT NULL,        -- bearing center of 60-180 deg HUD
  range_m REAL NOT NULL,
  band TEXT NOT NULL,           -- CARDIAC|RESP|MOTION
  snr_db REAL NOT NULL,
  verdict TEXT NOT NULL,        -- NO_MOTION|POSSIBLE|MOTION
  iff_subject TEXT REFERENCES subjects(id), -- set only on valid token
  created_at INTEGER NOT NULL
);
CREATE INDEX idx_radar_time ON radar_detections(created_at);

CREATE TABLE iff_tokens (
  id TEXT PRIMARY KEY,
  subject_id TEXT NOT NULL REFERENCES subjects(id),
  nonce TEXT NOT NULL UNIQUE,
  signature TEXT NOT NULL,      -- Ed25519 over (subject+nonce+epoch)
  epoch INTEGER NOT NULL,
  verified INTEGER NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE TABLE alerts (
  id TEXT PRIMARY KEY,
  kind TEXT NOT NULL,           -- VITALS_URGENT|MOTION|IFF_FAIL|SENSOR_FAULT
  ref_id TEXT NOT NULL,         -- vitals_samples or radar_detections id
  detail TEXT NOT NULL,
  acked INTEGER NOT NULL DEFAULT 0,
  created_at INTEGER NOT NULL
);
```

Retention: debug waveforms (if any) ring-buffer ≤60 s, never exported; derived metrics retained per mission policy `[TBD]`.
