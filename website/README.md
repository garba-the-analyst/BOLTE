# Website — Static Multi-Page (v0.3 redesign: light/dark mix)

Stack: vanilla HTML/CSS/JS, no framework, no build. Works from `file://` and any static host. Spec: `FUNCTIONAL-SPEC.md`.

## Pages
- `index.html` — Video hero (lockup + mission + CTAs + chips) + what-we-do + model/stats band + 6-product tier grid + ethics
- `about.html` — Vision/Mission/Aim cards + Goals 1–7 grid + model/values/ethics band (from `01-canon`)
- `products.html` — 6 tiered detail cards with Users/Does/Offline/Limits rows (from `04-products/functional-overview.md`)
- `roadmap.html` — Phase 0–3 vertical timeline + gate (from `03-roadmap`)
- `team.html` — Founder cards with mark avatars + open-seats table, privacy-safe (from `05-people`)
- `contact.html` — `[TBD]` inbox + styled browser-only draft form + onboarding form links
- `legal.html` — pre-CAC status, template summaries, privacy/terms/imprint grid (full texts private in `docs/06-legal/`)

## Assets
- `assets/css/site.css` — v2 system: light sections + dark hero/bands/footer, tier badges, timeline, stats, hamburger nav, print + reduced-motion
- `assets/js/site.js` — active nav, year, logo fallback, reduced-motion video pause
- Hero video: `../assets/animations/BOLTE.mp4` (3.2MB, poster = lockup PNG); watermark: `bolte-lockup-watermark-dark.png` at 7–8% in bands/footer

## Run
`python3 -m http.server -d website 8080` or open `index.html` directly. All links relative.

## Rules
- Content mirrors `docs/` verbatim for identity/goals/stages/phases. No invented people, contacts, capabilities.
- Logo: `../assets/logo-placeholder/bolte-lockup-dark.png` with text fallback. No personal contacts until provided.
- Migrate to Docusaurus later: this IA + copy becomes the MDX source. Do not delete until migration lands.
