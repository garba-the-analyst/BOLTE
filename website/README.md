# BOLTE website (v4)

Static HTML, CSS and a small JS file. No framework, no build step, no cookies, no third-party requests.

## Pages
- `index.html`: hero air-picture display, focus areas, AeroPulse-NG summary, commitments
- `technology.html`: AeroPulse-NG overview, standards, programme portfolio, path forward
- `company.html`: vision, mission, principles, leadership, advisory board (seats open)
- `contact.html`: email contact and enquiry types
- `legal.html`: privacy and notices

## Design
- Palette unchanged from v3: navy `#0A1428`, blue `#2E86DE`, steel `#5B6B7F`, pale `#f4f7fa`
- Fonts (self-hosted, SIL OFL): Archivo (headings), IBM Plex Sans (body)
- The hero radar is an inline SVG labelled "Illustrative". Replace it with a real AeroPulse-NG capture when one is cleared for publication.

## Content rules
- Advisers are shown as open seats until each has signed their agreement. Add names only after onboarding.
- Team members other than the founders appear by role only. Add a name or photo only with that person's written consent.
- Nothing from the restricted tier (detection logic, deployment configuration, HFP-X drawings) belongs on this site.
- Keep maturity labels honest: Prototype, Concept, Research concept, Documentation only.

## Run and deploy
- Preview: `python3 -m http.server -d website 8080`
- Deploy: push to `main`. `.github/workflows/pages.yml` runs `build-scripts/package-pages.sh`.
