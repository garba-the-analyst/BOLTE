# DAFV — Product Brief (Concept)

Source: `projects/dafv/` (`README.md` + `SPEC.md`). Spec only — no code yet.

## Problem
Depots receive hardware/firmware with no local way to prove provenance — tampered or post-MRO-swapped binaries can deploy unchecked.

## Solution
Cryptographic audit station for receiving docks: JTAG/UART/USB readout → BLAKE3 + SHA-256 hashing → Ed25519 signature-tree manifest verify → encrypted RFID tag bind. Statically linked native Rust binary.

## Status / Evidence
Concept, TRL 1–2. Next: manifest format + verification flow + bus-interface design.

## Standards & compliance
Chain-of-custody logging, human accept/reject decision, lawful users only.

## Cost & impact
Catches tamper before deployment using commodity interfaces; locally runnable offline.

## Next 90 days
SPEC expansion only (gated: no build until AeroPulse-NG trial report + treasury review).
