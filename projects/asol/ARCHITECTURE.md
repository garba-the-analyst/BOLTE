# ASOL — Architecture

Connective tissue for the armory custody pipeline. Module detail will live next to code; this doc is the design rationale. Source: `SPEC.md`.

## 1. Guiding constraints
1. **Air-gapped by contract.** No feature may require internet at build or runtime. Consequence: local clocks authoritative, no cloud backup, export via signed files on removable media only.
2. **One ingest path.** Barcodes, RFID reads, and manual entries all normalize into a single `CustodyEvent` stream — bench tests, demo mode, and live sensors execute identical validation below the driver.
3. **Deterministic custody core, async shell.** Custody state machine is a pure function of ordered events: replays are bit-reproducible and auditable without GUI/drivers. Tauri/Qt runtime owns clocks and I/O.
4. **Dual-custodian rule.** No release, handover, or adjustment commits without two distinct authenticated custodians. Liveness/fitness pulse check gates every release.

## 2. Data flow
```text
Drivers (USB/BT barcode 1D/2D · UHF RFID · optical pulse/liveness)
        │  normalized CustodyEvent stream (queued)
        ▼
┌─ tick/commit ─────────────────────────────────────────────┐
│ 1 validate event (schema, duplicate, signature)           │
│ 2 custody transition (AVAILABLE→CHECKED_OUT→RETURNED…)    │
│ 3 policy gates: dual-custodian present? liveness fresh?   │
│ 4 append to SQLCipher journal (AES-256) + audit entry     │
│ 5 publish CustodySnapshot (items · shifts · alerts)       │
└───────────────────────────────────────────────────────────┘
        ▼ snapshot bus (GUI) / signed export file (audit)
┌──────────────────────┐      ┌───────────────────────────┐
│ Desk GUI (Tauri/Qt)  │      │ Audit export + print log  │
│ checkout · handover  │      │ hash-chained, dual-signed │
└──────────────────────┘      └───────────────────────────┘
```

## 3. Key decisions
| Decision | Rationale | Alternative rejected |
|---|---|---|
| SQLite + SQLCipher (AES-256) | single-file encrypted DB, survives power loss, trivial backup to signed media | Postgres/server DB (needs ops, network) |
| Rust core + Tauri/Qt shell | memory safety for custody logic; thin GUI replaceable | Full C++ monolith (larger audit surface) |
| Hash-chained audit journal | tamper-evident paper-ledger replacement; dual signatures per handover | Plain log table (silent edits possible) |
| Driver abstraction trait | barcode/RFID/pulse vendors vary; one `CustodyEvent` path keeps tests == live | Per-device code paths (drift risk) |
| Liveness as release gate, not ID | pulse check proves live fit operator present; identity via custodian login | Biometric ID storage (privacy + legal weight) |

## 4. Custody state machine
`REGISTERED → AVAILABLE ⇄ CHECKED_OUT → (OVERDUE) → RETURNED → AVAILABLE`
`→ QUARANTINE → (DISPOSED | RETURNED)`. Shift: `OPEN → HANDOVER_PENDING → OPEN (new custodians) → CLOSED`. Handover requires outgoing + incoming dual signatures + count reconciliation.

## 5. Testing philosophy
Every custody claim executable: state-machine transitions, dual-sign enforcement, journal hash-chain verify, driver replay fixtures, liveness timeout handling. One-command battery (mirror `aeropulse-ng/scripts/verify.sh`) when code starts.
