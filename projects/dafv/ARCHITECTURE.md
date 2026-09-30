# DAFV — Architecture

Connective tissue for the depot verification pipeline. Source: `SPEC.md`.

## 1. Guiding constraints
1. **Offline-capable audit station.** No feature may require internet. Consequence: local trust store (Ed25519 roots), no OCSP; manifests + signatures travel on signed media.
2. **One acquisition path.** JTAG/UART/USB reads, file imports, and test fixtures all normalize into `FirmwareImage{bytes + provenance}` — bench tests and live probes execute identical hashing/verification below the bus.
3. **Deterministic verify, fallible acquire.** Hashing + signature checks are pure and replayable; only bus I/O may fail (probe contact, baud mismatch). Failures quarantine, never auto-accept.
4. **Human accept/reject.** Tool reports PASS/FAIL + evidence; a human signs the disposition. No auto-flash, no auto-deploy.

## 2. Data flow
```text
Bus/file ingest (JTAG · UART · USB · file import · fixture)
        │  FirmwareImage + claimed manifest
        ▼
┌─ verify ──────────────────────────────────────────────────┐
│ 1 hash image (BLAKE3 + SHA-256, chunked, streaming)       │
│ 2 parse manifest tree (asset → revisions → hashes → sigs) │
│ 3 Ed25519 verify against local trust roots                │
│ 4 bind/check encrypted RFID tag (asset ↔ manifest)        │
│ 5 verdict PASS | FAIL | INCONCLUSIVE + evidence bundle    │
└───────────────────────────────────────────────────────────┘
        ▼ verdict + evidence (DB) / signed report file / tag write
┌─────────────────┐   ┌──────────────────┐   ┌─────────────────┐
│ Rust CLI / svc  │   │ Receiving-dock   │   │ RFID tag writer │
│ acquire·verify  │   │ report (signed)  │   │ provision/bind  │
└─────────────────┘   └──────────────────┘   └─────────────────┘
```

## 3. Key decisions
| Decision | Rationale | Alternative rejected |
|---|---|---|
| Statically linked Rust binary | runs on locked-down depot hosts, no runtime install, small audit surface | Python/Node tooling (dependency + air-gap friction) |
| Dual hash BLAKE3 + SHA-256 | speed + ecosystem compatibility (vendor sheets quote SHA-256) | Single algorithm (faster but less interoperable) |
| Ed25519 signature trees | offline root rotation, per-revision signatures, fast verify | X.509/PKI (needs online revocation story) |
| Encrypted RFID bind | physical asset ↔ manifest link survives re-labeling | Barcode only (cloneable, no crypto) |
| Never auto-write firmware | probe verifies; flashing is a separate authorized step | Verify-and-flash one-shot (blast radius) |

## 4. Verdict semantics
`PASS` (hashes match + sigs valid + tag binds), `FAIL` (any mismatch — quarantine), `INCONCLUSIVE` (read errors, unknown manifest — re-acquire, never deploy). Evidence bundle always stored with verdict.

## 5. Testing philosophy
Known-answer hashes (NIST vectors + BLAKE3 vectors), golden manifest fixtures (valid/expired/forged), bus fault injection (drop bytes, wrong baud), RFID round-trips. One-command battery when code starts.
