# Website — Functional Specification (static multi-page, v0.3 redesign)

Status: approved for static build. Stack: vanilla HTML/CSS/JS, no framework, works from `file://` and any static host. Docusaurus migration later reuses this IA + content model.

## 1. Goals
- FR-G1: Public face for BOLTE that states identity, model, products (TRL-honest), roadmap, team (privacy-safe), contact (TBD-safe), legal status.
- FR-G2: Works offline from disk (`file://`), no build step, no external fonts/CDN/JS.
- FR-G3: Content sourced 1:1 from `docs/` + `projects/*/SPEC.md`; no invented people, contacts, or capabilities.

## 2. Information architecture
| Route | File | Source of truth |
|---|---|---|
| `/` Home | `website/index.html` | Video hero (lockup + mission + CTAs + chips) + what-we-do + model/stats band + 6-product tier grid + ethics |
| About | `website/about.html` | `docs/01-canon/01-identity-vision-mission-aim.md` + Goals 1–7 |
| Products | `website/products.html` | `docs/04-products/*.md` + `projects/*/SPEC.md` (user-facing functions only, no RF/solver internals beyond published brief) |
| Roadmap | `website/roadmap.html` | `docs/03-roadmap/roadmap.md` Phase 0–3 |
| Team | `website/team.html` | `docs/05-people/org-structure.md` — founders named, 5 members `[TBD]` until consented |
| Contact | `website/contact.html` | `[TBD domain/email]` + form placeholder (mailto + print, no backend) |
| Legal | `website/legal.html` | `docs/06-legal/` status — templates only, lawyer review required, privacy/terms/imprint |

## 3. Functional requirements
- FR-NAV1: Shared header nav (Home, About, Products, Roadmap, Team, Contact, Legal) with active-page highlight, mobile collapse without JS dependency (details/summary + JS enhancement).
- FR-B rand1: Navy `#0A1428` bg, accent `#2E86DE`, text `#FFF/#B8C2CC`; wordmark `BOLTE` letter-spacing 0.08em; logo `<img src="../assets/logo-placeholder/bolte-lockup-dark.png">` with `onerror` fallback to text wordmark (never broken-image icon).
- FR-CONT1: Every page states pre-CAC status + TRL honesty + `[TBD]` where contact/member/site data missing. No personal data published.
- FR-PROD1: Products page lists all 6 (AeroPulse-NG prototype; ASOL/DAFV/C4ISR-DFE/TBR-HS concept TRL 1–2, spec-only, gated; HFP-X programme concept BL-0.0, separate evidence-gated track). Each card: problem → solution → user → offline property → status → link to `docs/04-products/<x>.md` path text.
- FR-ROAD1: Roadmap page renders Phase 0–3 with exit criteria + gate note (no new build until AeroPulse trial + treasury review).
- FR-TEAM1: Team page names co-founders + mandates only; 5 seats listed as `[TBD — withheld until onboarded]`; link to onboarding forms (Stage 1 info-only, Stage 2 agreements).
- FR-CONT2: Contact page: `[TBD]` domain/email block, inbox-holder note, precautions (no secrets via form), print-friendly.
- FR-LEG1: Legal page: MOU/NDA/IP status (templates, unsigned, lawyer review), CAC path summary, privacy (no analytics, no cookies, forms stay in browser via localStorage), terms (content CC/internal, code per-project licence), imprint (founders + Lagos seat + TBD contact).
- FR-A11Y1: Semantic landmarks, alt text, 44px targets, focus visible, contrast ≥4.5:1 body, keyboard-operable nav.
- FR-SEO1: Unique `<title>` + meta description per page, OG tags with relative image path, sitemap comment in README.

## 4. Non-functional / constraints
- No external requests; total page <150KB excl. logo; print CSS hides nav/CTA.
- Relative links only (`about.html`, not `/about`) so `file://` works.
- Shared assets: `website/assets/css/site.css`, `website/assets/js/site.js` (nav + year + logo fallback). No inline-style drift — all pages link the stylesheet.

## 5. Acceptance checklist
- [ ] All 7 pages open from `file://` with no 404, no broken-image icon, active nav correct.
- [ ] Text matches `docs/` verbatim for identity/vision/mission, goals titles, product stages, roadmap phases.
- [ ] No unpublished names/emails/phones; every unknown renders `[TBD]`.
- [ ] Legal page carries lawyer-review banner.
- [ ] Print preview of each page hides nav/CTA, shows pre-CAC footer.

## 6. Build / run / migrate
- Run: `python3 -m http.server -d website 8080` or open `website/index.html` directly.
- Migrate to Docusaurus later: IA maps to docs sidebar (`docs/` as plugin source); these HTML files become MDX content drafts. Do not delete until migration lands.
