# BOLTE Projects

Code + spec home for every BOLTE product. Each subfolder is a standalone project.

| Folder | Full name | Stage | Source |
|---|---|---|---|
| `aeropulse-ng/` | AeroPulse-NG — Tactical Radar & Airspace Surveillance Engine | Prototype v2.4.0, TRL 4–5 | Moved from `/Projects/aeropulse-ng` (outside dir), now canonical location |
| `asol/` | Armory Shift & Ordnance Log (ASOL) | Concept, TRL 1–2 | Specification Overview PDF (standalone software project 1/4) |
| `dafv/` | Defense Asset & Firmware Verifier (DAFV) | Concept, TRL 1–2 | Specification Overview PDF (standalone software project 2/4) |
| `c4isr-dfe/` | Tactical C4ISR Data Fusion Engine (C4ISR-DFE) | Concept, TRL 1–2 | Specification Overview PDF (standalone software project 3/4) |
| `tbr-hs/` | Tactical Biometric Radar & Health System (TBR-HS) | Concept, TRL 1–2 | Specification Overview PDF (standalone software project 4/4) |
| `BOLTE HFP/` | Human Flight Platform (HFP-X) — piloted VTOL/transition aircraft programme | Concept, BL-0.0 (structure only) | 34-volume doc tree + `HFP-X blueprints/` (9 DWG sheets + dark/print PDFs); active programme docs |

Conventions (mirror `aeropulse-ng/` + BOLTE Canon):
- Each concept project: `README.md` + `SPEC.md` + `ARCHITECTURE.md` + `DATABASE.md` + `API.md` + `ROADMAP.md` + `RISKS.md`. `docs/` + `src/` created when code starts.
- Spec-only for now — no code in `asol/`, `dafv/`, `c4isr-dfe/`, `tbr-hs/` until AeroPulse-NG trial report + treasury review (TBR-HS additionally needs safety/ethics gate).
- Docs briefs stay in `docs/04-products/`; this folder holds specs + future code.
- Placeholders use `[TBD]` — never invent personal data.
- Defense ethics guardrails apply to all: lawful users only, human-in-the-loop, both-founders approval for security partnerships.
