# DAFV — Specification (single source of truth)

Source: Specification Overview PDF §2 + AI Agent Prompt Block `SYSTEM_2`.

Use this file for architectural planning, database schema generation, API interface design, and implementation code construction.

## 1. Identity
- **Name:** Defense Asset & Firmware Verifier (DAFV)
- **Domain:** Hardware Supply Chain Security & Anti-Tamper Verification
- **Type:** Standalone software project (2 of 4 in export)

## 2. Purpose
Hardware supply chain validation, firmware binary SHA-256/BLAKE3 cryptographic hashing, Ed25519 manifest verification.

## 3. Operational scope
Cryptographic audit tool used at military depots and receiving docks to verify hardware provenance and firmware binary integrity before deployment or post-MRO (Maintenance, Repair, and Overhaul).

## 4. Tech stack
- Statically linked native Rust system binary / CLI / system service
- JTAG/UART/USB bus interface
- BLAKE3 and SHA-256 cryptographic hashing algorithms
- Ed25519 signature trees
- Encrypted RFID tag reader/writers

## 5. BOLTE constraints
- Offline-capable audit station; deterministic, replayable verification.
- Lawful users only; chain-of-custody logging.
- Human in the loop for accept/reject decisions.
- TRL honesty: concept stage.

## 6. Downstream agent instruction
`INSTRUCTION_FOR_AGENT: Use this specification as the single source of truth for architectural planning, database schema generation, API interface design, and implementation code construction.`
