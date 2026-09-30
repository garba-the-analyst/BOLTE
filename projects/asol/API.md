# ASOL — API / Interface Design

Local-first. No network. GUI calls core via IPC; CLI mirrors every IPC command for headless/audit use.

## IPC / CLI surface (1:1)
| Command | Inputs | Outputs | Gate |
|---|---|---|---|
| `register_item` | serial, kind, barcode?, rfid_epc? | item | dual-custodian |
| `check_out` | item_id, custodian_out, witness, liveness_id, due_at | transaction | dual + fresh liveness |
| `check_in` | transaction_id, condition note | transaction (closed) | dual-custodian |
| `start_shift` | custodian_a, custodian_b | shift | both active |
| `handover_shift` | shift_id, incoming_a, incoming_b, counts | handover | dual-out + dual-in signatures |
| `liveness_check` | custodian_id, sensor sample | liveness_checks row | sensor quality threshold |
| `quarantine_item` | item_id, reason | item (QUARANTINE) | dual-custodian |
| `audit_export` | date range | signed file (JSONL + hashes) | auditor role |
| `verify_chain` | — | ok / first-bad-seq | anyone |

## Event / snapshot contracts
- `CustodyEvent{Register|CheckOut|CheckIn|Handover|Quarantine|Adjust}` — queued, validated, then committed once.
- `CustodySnapshot{items_by_status · open_transactions · active_shift · alerts(overdue, quarantine, liveness-expired)}` at commit cadence + on demand.

## Driver interface
```rust
trait CustodyDriver {
  fn poll(&mut self) -> Vec<CustodyEvent>; // barcode/RFID/pulse normalized here
  fn health(&self) -> DriverHealth;        // connected | degraded | offline
}
```
Simulated driver feeds scripted `CustodyEvent`s through the same path (sim == live principle).

## Export format
JSONL rows + manifest `{range, row_count, chain_head_hash, sig_a, sig_b}`. Verifiable offline with `verify_chain`.
