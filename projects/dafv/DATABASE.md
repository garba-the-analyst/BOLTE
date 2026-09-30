# DAFV — Database Schema (SQLite, offline)

Local audit DB on the station. Firmware bytes stored as files by hash; DB holds metadata + verdicts. Times INTEGER ms.

```sql
CREATE TABLE trust_roots (
  key_id TEXT PRIMARY KEY,      -- Ed25519 key id
  pubkey TEXT NOT NULL,
  owner TEXT NOT NULL,          -- vendor / BOLTE lab / depot
  valid_from INTEGER NOT NULL, valid_until INTEGER,
  revoked INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE assets (
  id TEXT PRIMARY KEY,
  serial TEXT UNIQUE NOT NULL,
  model TEXT NOT NULL,
  rfid_uid TEXT UNIQUE,         -- encrypted tag UID, nullable until bound
  created_at INTEGER NOT NULL
);

CREATE TABLE firmware_images (
  sha256 TEXT PRIMARY KEY,      -- content address
  blake3 TEXT NOT NULL,
  size_bytes INTEGER NOT NULL,
  source TEXT NOT NULL,         -- JTAG|UART|USB|FILE|FIXTURE
  path TEXT NOT NULL,           -- file store path by sha256
  acquired_at INTEGER NOT NULL
);

CREATE TABLE manifests (
  id TEXT PRIMARY KEY,
  asset_model TEXT NOT NULL,
  revision TEXT NOT NULL,
  sha256 TEXT NOT NULL REFERENCES firmware_images(sha256),
  blake3 TEXT NOT NULL,
  signer_key TEXT NOT NULL REFERENCES trust_roots(key_id),
  signature TEXT NOT NULL,
  issued_at INTEGER NOT NULL,
  UNIQUE(asset_model, revision)
);

CREATE TABLE verifications (
  id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES assets(id),
  manifest_id TEXT REFERENCES manifests(id),
  image_sha256 TEXT NOT NULL REFERENCES firmware_images(sha256),
  verdict TEXT NOT NULL,        -- PASS|FAIL|INCONCLUSIVE
  evidence TEXT NOT NULL,       -- JSON: hashes, sig checks, tag bind, read stats
  operator_a TEXT NOT NULL, operator_b TEXT, -- dual where policy requires
  created_at INTEGER NOT NULL
);
CREATE INDEX idx_verdict ON verifications(verdict);
CREATE INDEX idx_asset ON verifications(asset_id);
```

Rules: `firmware_images` immutable by hash; `verifications` append-only; `trust_roots` rotation adds rows, never edits history; tag UID unique per asset.
