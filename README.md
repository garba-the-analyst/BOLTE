# BOLTE — Corporate Documentation & Website Monorepo

> BOLTE is a Nigerian research, engineering, and technology company focused primarily on developing indigenous defense and security technologies while building the broader technological capabilities needed to drive Nigeria's — and ultimately Africa's — technological independence.

Co-founders: **Abdullahi Garba & Essien Frances**

## Structure

```
BOLTE/
  README.md                # this file
  CHANGELOG.md             # versioned doc history
  docs/
    01-canon/              # a. Detailed Canon of BOLTE
    02-brand-ip/           # b. Branding / Licensing / Trademark
    03-roadmap/            # c. Roadmap
    04-products/           # d. Product briefs (website source; specs+code live in projects/)
    05-people/             # e. Membership, roles, expectations
    06-legal/              # f. MOU, NDA, IP assignment, CoI
    07-equity/             # g. Shared profit/equity model
    08-focus-ndaie-2026/   # h. Immediate Focus: NDAIE 2026 competition
    09-strategy/           # Business plan + strategic docs
  projects/              # Index of the 6 project repos (code lives on GitHub, not here)
  website/                 # Static multi-page site (7 pages + FUNCTIONAL-SPEC.md) — run via file:// or http.server
  assets/logo-placeholder/ # Brand logo pending — wordmark rules apply
  pdf/                     # Generated PDFs (mirror of docs/ + README + CHANGELOG)
  build-scripts/           # make-pdfs.sh + pdf-style.css (regenerate PDFs)
```

## Status

- CAC: **Not yet registered.** All legal docs are contractual pre-incorporation with future-conversion clauses.
- Team: 2 co-founders + 5 members (names TBD — see `docs/05-people/`).
- Logo: **Still being designed.** Use text wordmark `BOLTE` per `docs/02-brand-ip/brand-guide.md`.
- Domain/email/contact: **TBD.** Placeholders used throughout.
- Competition: **NDAIE 2026 National Innovation Pitch Challenge**, category **Flight Planning & Air Traffic Management**, deadline **26 Sept 2026, 23:59 WAT**. Start at `docs/08-focus-ndaie-2026/competition-playbook.md`.
- Profit model default: **50% Treasury / 10% + 10% Founders / 7.5% + 7.5% + 5% + 5% + 5% Members.** See `docs/07-equity/equity-model.md`.

## Conventions

- All docs are Markdown, docs-as-code, versioned via CHANGELOG.
- Placeholders use `[TBD: ...]` or `[VARIABLE: ...]` — never invent personal data.
- Legal templates are **templates only** under Nigerian law — require lawyer review before signing.
- NASS Rulebook takes precedence over Guidelines where they conflict.

## Quick Links

- Canon: `docs/01-canon/00-index.md`
- Competition playbook: `docs/08-focus-ndaie-2026/competition-playbook.md`
- Equity model: `docs/07-equity/equity-model.md`
- Business plan: `docs/09-strategy/business-plan.md`
- Website plan: `website/README.md`

## PDFs

Every Markdown doc has a styled PDF mirror under `pdf/` (27 files, BOLTE header, A4 print CSS).
Regenerate after any doc edit with:

```bash
./build-scripts/make-pdfs.sh
```
