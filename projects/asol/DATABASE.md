# ASOL — Database Schema (SQLCipher / SQLite)

Encrypted at rest (AES-256). All writes journaled + hash-chained in `audit_log`. Times in INTEGER ms (local clock authoritative — air-gapped).

```sql
PRAGMA journal_mode = WAL;

CREATE TABLE custodians (
  id TEXT PRIMARY KEY,          -- staff service number
  full_name TEXT NOT NULL,
  role TEXT NOT NULL,           -- armorer / duty-officer / auditor
  active INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE items (
  id TEXT PRIMARY KEY,          -- internal UUID
  serial TEXT UNIQUE NOT NULL,
  kind TEXT NOT NULL,           -- weapon / magazine / ammunition-lot / accessory
  barcode TEXT, rfid_epc TEXT,
  status TEXT NOT NULL DEFAULT 'AVAILABLE', -- REGISTERED|AVAILABLE|CHECKED_OUT|OVERDUE|QUARANTINE|DISPOSED
  created_at INTEGER NOT NULL
);

CREATE TABLE transactions (
  id TEXT PRIMARY KEY,
  item_id TEXT NOT NULL REFERENCES items(id),
  type TEXT NOT NULL,           -- CHECK_OUT|CHECK_IN|REGISTER|ADJUST|QUARANTINE|DISPOSE
  custodian_out TEXT NOT NULL REFERENCES custodians(id),
  custodian_witness TEXT NOT NULL REFERENCES custodians(id),
  liveness_id TEXT REFERENCES liveness_checks(id),
  due_at INTEGER, returned_at INTEGER,
  note TEXT, created_at INTEGER NOT NULL,
  CHECK (custodian_out <> custodian_witness)  -- dual-custodian rule in schema
);

CREATE TABLE shifts (
  id TEXT PRIMARY KEY,
  opened_at INTEGER NOT NULL, closed_at INTEGER,
  custodian_a TEXT NOT NULL REFERENCES custodians(id),
  custodian_b TEXT NOT NULL REFERENCES custodians(id)
);

CREATE TABLE handovers (
  id TEXT PRIMARY KEY,
  shift_id TEXT NOT NULL REFERENCES shifts(id),
  outgoing_a TEXT NOT NULL, outgoing_b TEXT NOT NULL,
  incoming_a TEXT NOT NULL, incoming_b TEXT NOT NULL,
  expected_count INTEGER NOT NULL, counted_count INTEGER NOT NULL,
  sig_out TEXT NOT NULL, sig_in TEXT NOT NULL, -- dual signatures
  created_at INTEGER NOT NULL
);

CREATE TABLE liveness_checks (
  id TEXT PRIMARY KEY,
  custodian_id TEXT NOT NULL REFERENCES custodians(id),
  method TEXT NOT NULL,         -- optical-pulse / biometric
  passed INTEGER NOT NULL,
  score REAL, valid_until INTEGER NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE TABLE audit_log (
  seq INTEGER PRIMARY KEY AUTOINCREMENT,
  prev_hash TEXT NOT NULL, entry_hash TEXT NOT NULL,
  actor_a TEXT NOT NULL, actor_b TEXT NOT NULL,
  action TEXT NOT NULL, payload TEXT NOT NULL,
  created_at INTEGER NOT NULL
);
CREATE INDEX idx_tx_item ON transactions(item_id);
CREATE INDEX idx_audit_action ON audit_log(action);
```

Integrity rules: every release `CHECK_OUT` must reference a fresh passed `liveness_checks` row; every `handovers` row requires count match or quarantine flag; `audit_log` verified by `prev_hash` chain + dual signatures.
