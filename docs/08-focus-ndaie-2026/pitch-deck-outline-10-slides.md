# Pitch Deck Outline — Max 10 Slides (PDF)

One idea per slide. Readable text, diagrams/photos/evidence. Prepare for feasibility, safety, cost, limits, impact Q&A.

| Slide | Title | Content + rubric weight |
|---|---|---|
| 1 | Title + team + category | AeroPulse-NG, Flight Planning & ATM, Team Lead + school, BOLTE wordmark, Expo name. (15% presentation) |
| 2 | Problem (specific, real) | Unjustified-radar aerodromes, low-altitude gaps, harmattan/diversion failure, cost of imports. Photo/diagram of gap. (25% clarity) |
| 3 | Why existing approaches fall short | PSR/SSR cost/complexity, ADS-B aggregators need internet, no offline STCA/weather fusion for Nigeria. (25% feasibility) |
| 4 | Solution overview | Air-gapped SDR+PC workstation, dual-window ATC/tactical, offline-first. Architecture block diagram. (25% clarity) |
| 5 | How it works (technical) | 1090/ACARS ingest → DF17/CPR/Gillham decode → 6-state EKF → R*-tree STCA → weather fusion → defence overlays. Single decode path sim==real. (25% feasibility) |
| 6 | Demo / evidence | Synthetic-feed screenshots, 7700 @45s / <1km miss @70s / dropout @112s scenarios, 108 checks green, dual-window UI. Honest TRL 4–5. (15% readiness) |
| 7 | Safety, limits, risks, next steps | Synthesized FFT now → real RTL-SDR I/Q next; AWOS wiring; Comm-B; DB writers; multi-site. Safety + NCAA SI-metric notes. (25% feasibility + 15% readiness) |
| 8 | Impact | >99% capex cut, sovereign maintainability, training, civil + defence dual-use, scalability to secondary aerodromes. (20% impact) |
| 9 | Roadmap + cost | Now→Oct video→semi→finals; field-trial HW; cost table (SDR ~$150 + PC). Realistic milestones. (15% readiness) |
| 10 | Ask + contact | What we need (mentorship, test site, components), Team Lead contact, AI-use disclosure, references. (15% presentation) |

Appendix (not counted — do NOT exceed 10 in submitted PDF; keep as speaker notes): standards map, detailed test log, risk table, bill of materials.

Design: dark background + blue accent per BOLTE brand, min 24pt body, export PDF < [check NASS portal limit].
