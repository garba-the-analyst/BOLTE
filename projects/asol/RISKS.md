# ASOL — Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Liveness sensor spoofed (photo/video, fake pulse) | M | Critical | Quality thresholds + challenge-response + dual-custodian still required; sensor allowlist | `[TBD]` |
| SQLCipher key loss / custodian turnover locks DB | M | Critical | Split-key backup (2-of-3 custodians), sealed rotation procedure, tested restore | `[TBD]` |
| Dual-custodian collusion | L | High | Hash-chained journal + independent auditor export; anomaly flags (off-hours releases) | `[TBD]` |
| Power loss mid-commit corrupts journal | M | Med | WAL + single-commit transactions + startup `verify_chain`; UPS for desk | `[TBD]` |
| RFID misreads / duplicate EPC tags | M | Med | Barcode as fallback key; EPC commissioning check; quarantine on mismatch | `[TBD]` |
| Scope creep into personnel HR/medical records | M | Med | Store pass/fail + expiry only, no raw biometrics; note in privacy review | Founders |

Ethics: lawful users only; release always needs a human decision-maker; both-founders approval for any security-institution partnership.
