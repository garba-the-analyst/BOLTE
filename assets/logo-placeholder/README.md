# Logo Assets — Drop Files Here

Approved BOLTE logo set (received 2026-09-06). Save source files in this folder with these exact names:

| File | Use |
|---|---|
| `bolte-lockup-dark.png` | Full wordmark (white) on dark navy — hero, deck titles, site header on dark |
| `bolte-lockup-light.png` | Full wordmark (navy) on white/transparent — documents, light backgrounds |
| `bolte-lockup-watermark-dark.png` | Large faded lockup on dark (presentation backgrounds) |
| `bolte-mark-dark.png` | Bolt-in-hex mark (white) on dark — favicon base, avatars, small sizes |
| `bolte-mark-light.png` | Bolt-in-hex mark (navy) on white — favicon base, print |
| `bolte-mark-split.png` | Dual mark (navy on white / white on navy) — brand sheet only |

Accepted: PNG with transparency (min 2000px wide for lockups, 1024px for marks) + SVG masters if available (`bolte-*.svg` same basenames).

After dropping files, run `./build-scripts/make-pdfs.sh` (docs) and rebuild the deck — the website and deck reference these paths with text-wordmark fallback if a file is missing.
