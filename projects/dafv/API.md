# DAFV — API / Interface Design

Single static binary: `dafv`. Every operation offline. Exit codes: 0 PASS, 1 FAIL, 2 INCONCLUSIVE/error.

## CLI surface
| Command | Key flags | Output |
|---|---|---|
| `dafv acquire --bus jtag --out store/` | `--bus jtag|uart|usb|file`, `--input`, `--model` | `firmware_images` row + hashes to stdout |
| `dafv hash --input image.bin` | — | `BLAKE3=… SHA256=… size=…` |
| `dafv manifest issue --model X --rev R --image … --sign-key …` | offline signer | signed manifest JSON |
| `dafv verify --asset SERIAL --image … --manifest …` | `--tag UID?` | verdict + evidence JSON; appends `verifications` row |
| `dafv tag provision --asset SERIAL` | writes encrypted UID | binds `assets.rfid_uid` |
| `dafv tag read` | — | UID + bound asset or UNBOUND |
| `dafv report --asset SERIAL --format pdf|json` | date range | signed report file |
| `dafv roots add|revoke --key …` | trust-store mgmt (dual-operator) | updated `trust_roots` |

## Manifest JSON (signed)
```json
{"asset_model":"…","revision":"…","sha256":"…","blake3":"…",
 "signer_key":"…","issued_at":0,"signature":"ed25519:…"}
```

## Verdict JSON
```json
{"verdict":"PASS|FAIL|INCONCLUSIVE","asset":"…","image_sha256":"…",
 "checks":{"blake3_match":true,"sha256_match":true,"sig_valid":true,"tag_bound":true},
 "evidence_ref":"verifications/<id>"}
```

## Service mode
`dafv serve --socket ./dafv.sock` exposes the same verbs over local IPC for dock-GUI integration; no TCP by default.
