# Website — Static Multi-Page (v3 redesign: defence-tech design system)

Stack: vanilla HTML/CSS/JS, no framework, no build. Works from `file://` and any static host. Design inspired by `New UI/index.html` — dark navy hero, light content sections, glass header, defence-tech grid accents, Space Grotesk + DM Sans typography.

## Pages
- `index.html` — Video hero (lockup + mission + CTAs + chips) + capabilities + product grid + engineering model + mission + contact band
- `about.html` — Vision/Mission/Aim cards + Goals 1–7 grid + model/values/ethics (from `01-canon`)
- `products.html` — 6 tiered project cards (AeroPulse-NG prototype + ASOL/DAFV/C4ISR-DFE/TBR-HS concepts + HFP-X programme)
- `roadmap.html` — Phase 0–3 step list + gate (from `03-roadmap`)
- `team.html` — Founder + member photo cards + seats table (from `05-people`)
- `contact.html` — Official inbox + joining links (questionnaire + Stage 1/2 forms)
- `legal.html` — pre-CAC status, template summaries, privacy/terms/imprint (full texts private in `docs/06-legal/`)

## Assets
- `assets/css/site.css` — v3 defence-tech system: navy `#0A1428`, accent `#2E86DE`, steel `#5B6B7F`; grid-pattern dark sections; glass header; hover cards; responsive hamburger nav; print + reduced-motion
- `assets/js/site.js` — active nav, mobile toggle, year, reveal-on-scroll, video pause on reduced motion
- `assets/team/` — member portraits (Garba, Frances, David, Abdulazeez, Timi, Zheemah) @800px
- `assets/hfp/` — HFP-X DWG-002 figure (vendored for Pages)
- Hero video: `../assets/animations/BOLTE.mp4` (3.2MB, poster = lockup PNG); watermark: `bolte-lockup-watermark-dark.png`

## Run
`python3 -m http.server -d website 8080` or open `website/index.html` directly. All links relative.

## Rules
- Content mirrors `docs/` verbatim for identity/goals/stages/phases. No invented people, contacts, capabilities.
- Logo: `../assets/logo-placeholder/bolte-lockup-dark.png` with text fallback. No personal contacts until provided.
- Pages deploy via `.github/workflows/pages.yml` + `build-scripts/package-pages.sh` (self-contained `_pages` bundle).
- Migrate to Docusaurus later: this IA + copy becomes the MDX source. Do not delete until migration lands.