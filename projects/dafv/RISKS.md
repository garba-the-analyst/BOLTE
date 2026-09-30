# DAFV — Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Probe damages target board (voltage, sequence) | M | High | Current-limited adapters, sacrificial-board practice, per-model probe profiles, never probe live ordnance controllers | `[TBD]` |
| Trust-root key compromise | L | Critical | Offline roots, split custody, revocation list, short-lived revision sigs | Founders |
| Evil-maid / swapped image between acquire and verify | M | High | Hash at acquisition, content-addressed store, re-hash at verify | `[TBD]` |
| False PASS from truncated read (short image matches prefix) | M | Critical | Size check + full-stream hash + manifest size binding; INCONCLUSIVE on short reads | `[TBD]` |
| RFID clone / tag swap | M | Med | Encrypted UID + asset bind + verify-time tag check; tamper-evident tags | `[TBD]` |
| Operator auto-deploys on PASS without procedure | M | Med | Tool never flashes; report requires human sign-off; SOP training | `[TBD]` |

Safety: bench power discipline, ESD, no probing of energized/pyrotechnic systems. Lawful users only.
