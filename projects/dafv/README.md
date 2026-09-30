# Defense Asset & Firmware Verifier (DAFV)

> Hardware supply-chain security & anti-tamper verification — cryptographic audit before deployment or post-MRO.

- **Status:** Concept, TRL 1–2. Spec only — no code yet.
- **Source:** Specification Overview PDF, System 2/4.
- **BOLTE fit:** Goal 1 (defense tech resilience), Goal 2 (technology backbone — trust in hardware), Goal 7 (maintainable locally).

## What it does
Cryptographic audit tool used at military depots and receiving docks to verify hardware provenance and firmware binary integrity before deployment or post-MRO (Maintenance, Repair, and Overhaul).

## Tech stack (from spec)
Statically linked native Rust system binary, JTAG/UART/USB bus interface, BLAKE3 and SHA-256 cryptographic hashing algorithms, Ed25519 signature trees, and encrypted RFID tag reader/writers.

## Structure
```
dafv/
  README.md         # this file
  SPEC.md           # single source of truth (from PDF export)
  ARCHITECTURE.md   # depot verification pipeline
  DATABASE.md       # audit DB schema
  API.md            # CLI + manifest/verdict contracts
  ROADMAP.md        # phased plan
  RISKS.md          # risk register
  docs/ + src/      # created when code starts
```

## Next steps
1. Trust-model review with founders (root custody/rotation) `[TBD]`.
2. Prototype after gate: file-import hash → verify → report, then bus + tags.
3. Depot trial plan `[TBD]`.

See `SPEC.md` for the full exported specification.
