# Changelog

All notable documentation changes tracked here. Format: `YYYY-MM-DD — change`.

## [Unreleased]
- Membership intake 30 Sept–01 Oct 2026: 5 questionnaires processed (P1 Garba, P2 Frances, P3 Timi, P4 Zheemah, P5A Abdulazeez, P5B David). Full PII in gitignored `docs/05-people/private/roster.md` ONLY — nothing personal committed.
- Founders' decisions applied: contact bolte.tech0@gmail.com live on site; effective date 02 Oct 2026; Lagos/₦/Nigerian-English kept; Team Lead Garba; NEW split 70/6+6/4.5×4 (E vacant) in equity model + cap-table + MOU + site. OPEN: P5A/P5B→C/D assignment, 5th-seat math (0 vs 5×3.6), F8 spending/commitment rules (founders split), P3 gaps + 3hrs Treasurer concern.
- Website team page: 2 named members added (consent: full name), B1/B2 as initials, seats table updated.
- Project repos split: all 6 projects moved out of `BOLTE/projects/` into own public repos (`aeropulse-ng` re-attached w/ history + WIP push; new `asol`, `dafv`, `c4isr-dfe`, `tbr-hs`, `bolte-hfp`); BOLTE keeps briefs + `projects/README.md` link index; all doc/website paths rewired to repo URLs; HFP figure vendored into `website/assets/hfp/`.
- Hosted member form: new `forms/all-member-questionnaire.html` (P1–P7 slot picker, Q1–Q24 + founders F1–F12 collapsible section, portrait, age check, autosave, JSON/CSV/print export, JS syntax-checked); linked from website contact page; ships in Pages bundle via existing `forms/**` workflow path + `../forms/` link rewrite.
- HFP-X moved into `projects/` + drawings landed: `BOLTE HFP/` relocated from repo root to `projects/BOLTE HFP/`; new `HFP-X blueprints/` (9 DWG sheets DWG-001–009 + dark/print PDFs); all doc paths updated; brief `hfp-x.md` gains drawings register; website HFP card shows DWG-002 flight-configurations figure (vendored into Pages bundle).
- GitHub: repo initialized at BOLTE root, pushed to private `garba-the-analyst/BOLTE`; Pages deploy via `.github/workflows/pages.yml` + `build-scripts/package-pages.sh` (self-contained `_pages` bundle: website + vendored logos/video + forms, link-rewritten, locally verified 200s). Excluded via `.gitignore`: node_modules, Rust target/, venv, raw RF archives. Nested `aeropulse-ng/.git` history preserved at `/tmp/opencode/aeropulse-ng-git-backup` (move it to safe storage — NOT pushed).
- Website v0.3 redesign (light/dark mix, full reskin + layout): dark video hero (lockup + mission + CTAs + chips, `BOLTE.mp4` w/ poster + reduced-motion), light content sections, dark model/stats band (6/7/7/34), tiered product cards (proto/concept/safety/programme), roadmap timeline, goal grid, founder avatar cards, footer nav + watermark, CSS hamburger nav; all 7 pages + CSS/JS/video/watermark 200-verified, links OK.
- Registered HFP-X programme: `BOLTE HFP/` (Human Flight Platform, Concept BL-0.0, 34 volumes) added to `projects/README.md`, `docs/04-products/overview.md` + new brief `hfp-x.md` + `functional-overview.md` + `pipeline.md` (separate track), website `products.html` + home grid, root `README.md` structure.
- Logos live: promoted 6 files from `assets/logos/` (WhatsApp JPEGs) to canonical `assets/logo-placeholder/bolte-*.png`; wired header logo + mark favicon into all 7 website pages (200s verified); brand guide v0.3 (masters SVG/transparent still pending).
- New `docs/05-people/all-member-questionnaire.md`: single collection pass for all 7 (Part 1 everyone Q1–Q24 + Part 2 founders F1–F12), maps answers to MOU/eligibility/cap-table/website.
- Website v0.2 functional: static 7-page site (home/about/products/roadmap/team/contact/legal) + shared CSS/JS, served 200s locally, link-checked; added `website/FUNCTIONAL-SPEC.md`; added `docs/04-products/functional-overview.md` (5-product user-facing consolidation).
- Legal v0.2 hardening: rewrote MOU/NDA/IP+CoI with definitions, schedules, signature blocks, onboarding linkage; added `00-index.md` register, `signing-checklist.md`, `cac-conversion-note.md`; website `legal.html` summaries + privacy/terms/imprint.
- Planning pack for all 4 concepts: each of `asol/`, `dafv/`, `c4isr-dfe/`, `tbr-hs/` now has ARCHITECTURE.md + DATABASE.md (SQL DDL) + API.md + ROADMAP.md + RISKS.md. Still spec-only, no code; gated behind AeroPulse-NG trial + treasury review (TBR-HS also safety/ethics gate).
- Created `projects/` monorepo: moved `/Projects/aeropulse-ng` → `projects/aeropulse-ng/` (git history + uncommitted work preserved); added spec scaffolds `projects/asol/`, `projects/dafv/`, `projects/c4isr-dfe/`, `projects/tbr-hs/` (README+SPEC each, no code yet, from Specification Overview PDF).
- Added product briefs `docs/04-products/asol.md`, `dafv.md`, `c4isr-dfe.md`, `tbr-hs.md`; updated `overview.md` + `pipeline.md` + `README.md` structure.

## 2026-09-05 — v0.1.0 initial scaffold
- Created repo structure (docs/01–09, website/, assets/).
- Locked profit default: 50% Treasury / 10/10 Founders / 7.5/7.5/5/5/5 Members.
- Locked NDAIE 2026 category: Flight Planning & Air Traffic Management.
- Added competition playbook, canon, people, legal templates, equity, brand, roadmap, products, strategy drafts.
- CAC: not registered — contractual + future-conversion basis.
- Logo/domain/contact: TBD placeholders.
