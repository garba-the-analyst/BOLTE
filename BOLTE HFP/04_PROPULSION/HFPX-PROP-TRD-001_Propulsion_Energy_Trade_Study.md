# Propulsion Energy Trade Study

**Document ID:** HFPX-PROP-TRD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 7 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define the HFP-X propulsion energy-source trade (ISS-003 input): trade criteria, candidate set, authoritative data sources, ordinal assessment, conditional recommendation, and update rule. No selection is baselined in this revision; decision is explicitly deferred to a future selection Design Decision Record (DDR) under change control.

## 2. Scope

Covers the energy-source trade for the HFP-X distributed thrust system: jet-fuel turbine, ethanol turbine, hydrogen turbine (liquid hydrogen [LH2] and 700-bar gaseous storage assessed separately), hydrogen-electric fuel cell, and battery-electric. All HFP-X chain details, ratings, masses, thrust levels, endurances, and budgets remain TBD/TBC/reference-class except where explicitly cited as authoritative reference data in §8/§12.

> **Hazardous-subsystem boundary.** This document is analysis only (requirements, trade criteria, published-data comparison, safety considerations, and methodology). It contains NO instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 3. Applicable Documents

Authoritative research pack — all sources cited with retrieval date 2026-09-29. Only the figures quoted in §8/§12 are authoritative; every other numerical value in this document is TBD/TBC/reference-class.

- ASTM D1655 — Standard Specification for Aviation Turbine Fuels (Jet A-1 LHV minimum 42.8 MJ/kg basis). Retrieved 2026-09-29.
- AFQRJOS — Aviation Fuel Quality Requirements for Jointly Operated Systems, Issue 30 (Jet A-1 requirements). Retrieved 2026-09-29.
- Boehm et al., Fuel 311 (2022) — Jet fuel property reference. Retrieved 2026-09-29.
- Leone, Fuel (2026) — Ethanol LHV reference. Retrieved 2026-09-29.
- GREET Model (Argonne National Laboratory) — Ethanol LHV 26.95 MJ/kg reference. Retrieved 2026-09-29.
- NASA TM-20250007133 — Hydrogen storage system performance reference. Retrieved 2026-09-29.
- DOE / Argonne 2024 — Hydrogen storage system assessment. Retrieved 2026-09-29.
- Mazzoni et al., ICAS 2024 — Small-scale LH2 aircraft tank assessment. Retrieved 2026-09-29.
- Viswanathan et al., ACS Energy Letters — Li-ion specific-energy assessment. Retrieved 2026-09-29.
- NASA NTRS — X-57 battery pack data (225 Wh/kg cell → 149 Wh/kg pack reference). Retrieved 2026-09-29.
- AIAA Aerospace America (2025) — NASA battery thresholds (400 Wh/kg general aviation / 750 Wh/kg regional) reference. Retrieved 2026-09-29.
- PBS Aerospace — TJ100 / TJ40 published specifications. Retrieved 2026-09-29.
- Wikipedia — PBS TJ100 specification summary (used only as pointer to PBS published specs). Retrieved 2026-09-29.
- Gravity Industries — Jet suit reference system publications. Retrieved 2026-09-29.
- NATO / Milipol reporting — Gravity-class system reporting. Retrieved 2026-09-29.
- WIRED (2020) — Gravity jet suit reporting. Retrieved 2026-09-29.
- HFPX-PROP-ARC-001 Propulsion Architecture (Chapter 04.2; ISS-003 owner).
- HFPX-PROP-REQ-001 Propulsion System Requirements (Chapter 04.1).
- Vol 05 (fuel), Vol 07 (control/allocation), Vol 08 (monitoring), Vol 13 (safety), Vol 14 (thermal), Vol 19 (verification).

## 4. Definitions & Acronyms

- ISS-003: energy-source trade issue — OPEN until selection DDR (see §15).
- ISS-007: endurance / energy-budget issue — framed by reference-class check in §12; all HFP-X budgets TBD.
- DDR: Design Decision Record — no DDR is recorded by this revision; a DDR follows only upon selection.
- LHV / HHV: lower / higher heating value (chemical specific energy basis as cited).
- LH2: liquid hydrogen.
- T/W: thrust-to-weight ratio (reference-class published values only; HFP-X T/W TBD).
- SFC: specific fuel consumption (reference-class published value only; HFP-X SFC TBD).
- MVP: minimum-viable demonstrator (concept status; scope TBD).
- SRR: System Requirements Review (confirmation gate; date and entry criteria TBD).
- Usable specific energy (SYSTEM level): chemical/electrical energy per unit mass including storage, conditioning, and distribution penalties (values TBD except cited reference data).
- Reference-class: published data from an analogous system used for order-of-magnitude framing only; not an HFP-X selection, requirement, or prediction.
- TBD / TBC: to be determined / to be confirmed.

## 5. System Context

This trade supports HFPX-PROP-ARC-001: the energy→thrust chain type is TBD pending ISS-003. It receives hover/transition/cruise demands from Vol 07 allocation, interfaces to Vol 05 fuel/conditioning, Vol 14 thermal, Vol 08 monitoring, and Vol 13 safety. This study provides the criteria, evidence, and conditional assessment; it does not baseline a chain, rating, mass, or budget.

> **Hazardous-subsystem boundary.** Context and interfaces here describe analysis boundaries and safety-analysis inputs only. No build, ignition, fuelled-test, or operational procedures are contained or authorised.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TDE-001|The energy-source trade shall define and apply trade criteria covering usable specific energy at SYSTEM level including storage, power-to-weight, throttleability/transient, personnel/range safety, logistics, maturity/TRL, and certification path.|ISS-003; REQ-HFPX-PAR-002|Inspection|
|REQ-HFPX-TDE-002|The energy-source trade shall assess each candidate — jet-fuel turbine, ethanol turbine, hydrogen turbine (LH2 and 700-bar assessed separately), hydrogen-electric fuel cell, and battery-electric — against each criterion with an ordinal score and one-line rationale.|ISS-003; REQ-HFPX-PAR-002|Inspection|
| REQ-HFPX-TDE-003 | The energy-source trade shall cite authoritative data sources for every cited performance figure and label every other number TBD/TBC/reference-class with no invented values. | ISS-003 | Inspection |
|REQ-HFPX-TDE-004|The energy-source trade recommendation shall be stated as CONDITIONAL only, subject to SRR, safety review, and stated confirmation data needs, with no baselined selection in this revision.|ISS-003|Inspection|
| REQ-HFPX-TDE-005 | The energy-source selection decision shall be deferred to a future selection DDR under change control; no DDR is recorded by this revision. | ISS-003 | Inspection |
|REQ-HFPX-TDE-006|The energy-source trade shall be updated by DDR under change control when confirmation data, requirements, or constraints change prior to selection.|ISS-003|Inspection|

## 7. Architecture

Trade structure (method only; all HFP-X values TBD):

1. **Criteria (C1–C7)** — fixed for this revision per REQ-HFPX-TDE-001:
   - C1 Usable specific energy at SYSTEM level including storage.
   - C2 Power-to-weight (system level including storage/conditioning).
   - C3 Throttleability / transient response for distributed lift control.
   - C4 Personnel / range safety (handling, efflux, exclusion, abort implications).
   - C5 Logistics (fuel/energy supply, storage, turnaround in test range context).
   - C6 Maturity / TRL (published precedent relevant to wearable-scale vertical lift demonstrator).
   - C7 Certification path (manned-rating outlook; MVP demonstrator path vs full certification — both TBD).
2. **Candidates (6 assessment rows):** (a) jet-fuel turbine; (b) ethanol turbine; (c) hydrogen turbine — LH2 storage; (d) hydrogen turbine — 700-bar Type IV storage; (e) hydrogen-electric fuel cell; (f) battery-electric.
3. **Scoring scale:** ordinal 1–5 per criterion (5 = most favourable for MVP demonstrator context; 1 = least favourable). Scores are qualitative ordinals for comparison only, not measured HFP-X performance values. Totals are unweighted ordinal sums for ranking illustration only (TBC).
4. **Evidence rule:** only §8 cited figures are authoritative; all extrapolations to HFP-X are TBD/TBC/reference-class. No selection is baselined.

## 8. Detailed Design

### 8.1 Authoritative candidate data (exactly as cited; no HFP-X inference)

**Jet A-1 (kerosene-type turbine fuel):**

- LHV minimum 42.8 MJ/kg per ASTM D1655 / AFQRJOS Issue 30; analysis value used here 43 MJ/kg (≈11,900 Wh/kg). Sources: ASTM D1655; AFQRJOS Issue 30; Boehm et al., Fuel 311 (2022).
- Density 775–840 kg/m³. Sources: ASTM D1655 / AFQRJOS Issue 30.
- Derivation shown (from cited figures only): 43 MJ/kg ÷ 3.6 MJ/kWh = 11.94 kWh/kg ≈ 11,900 Wh/kg (rounded analysis value as directed).

**Ethanol:**

- LHV ≈26.9 MJ/kg. Sources: Leone, Fuel (2026); GREET 26.95 MJ/kg.
- Energy penalty vs Jet A-1 (shown): (43 − 26.9) ÷ 43 = 16.1 ÷ 43 ≈ 0.374 → ≈37% lower chemical specific energy than Jet A-1 on LHV basis. All turbine-on-ethanol system implications (derate, materials, SFC shift) TBC/reference-class.

**Hydrogen (chemical basis + storage-system penalties):**

- LHV 120 MJ/kg; HHV 142 MJ/kg (chemical basis, excluding storage). Conversion shown: 120 MJ/kg ÷ 3.6 ≈ 33,333 Wh/kg chemical.
- 700-bar Type IV system ≈5–6 wt% system (≈2 kWh/kg-system). Check shown: 5% × 33,333 ≈ 1,667 Wh/kg; 6% × 33,333 ≈ 2,000 Wh/kg → ≈2 kWh/kg-system as cited. Sources: NASA TM-20250007133; DOE/Argonne 2024; Mazzoni, ICAS 2024.
- Small-scale LH2 aircraft tanks ≈20–30% gravimetric efficiency (≈7–10 kWh/kg-system). Check shown: 20% × 33,333 ≈ 6,667 Wh/kg; 30% × 33,333 ≈ 10,000 Wh/kg → ≈7–10 kWh/kg-system as cited. Sources: same as above.
- Best large LH2 65–70% gravimetric efficiency — NOT applicable at HFP-X scale (stated explicitly; no HFP-X LH2 tank mass, boil-off, or insulation value is stated — all TBD).

**Batteries (Li-ion):**

- Current cells 250–300 Wh/kg (0.9–1.1 MJ/kg; check: 250 × 3,600 = 0.90 MJ/kg; 300 × 3,600 = 1.08 MJ/kg). Pack ≈60–70% of cell. Reference point: NASA X-57 — 225 Wh/kg cell → 149 Wh/kg pack (149 ÷ 225 ≈ 66%, consistent with 60–70% range). Sources: ACS Energy Letters (Viswanathan); NASA NTRS.
- Projected maximum 400–500 Wh/kg cell (reference-class projection, not HFP-X assumption). NASA thresholds: 400 Wh/kg general aviation / 750 Wh/kg regional (reference thresholds, not HFP-X requirements). Source: AIAA Aerospace America (2025).
- Jet-fuel-to-battery ratio — SHOWN (from cited figures): 11,900 Wh/kg ÷ 300 Wh/kg ≈ 39.7 (≈40×); 11,900 ÷ 250 ≈ 47.6 (≈48×) at cell level → Jet A-1 ≈40–48× current cells on chemical-vs-electrical stored-energy basis. Pack-level gap is larger (reference-class illustration): pack range from cited factors 250×0.60 = 150 Wh/kg to 300×0.70 = 210 Wh/kg → 11,900 ÷ 210 ≈ 57× to 11,900 ÷ 150 ≈ 79×; X-57 point 11,900 ÷ 149 ≈ 80×. Round-trip efficiency, discharge-rate, and usable-depth effects TBD.

**Reference turbine class (REFERENCE-CLASS — not HFP-X selection):**

- PBS TJ100 published specs: 1100–1250 N thrust, 17.6–19.7 kg dry mass, T/W ≈6.4–7.2, SFC 0.116 kg/N/h on Jet A / A-1. Sources: PBS Aerospace; Wikipedia PBS TJ100 (pointer only).
- PBS TJ40 published specs: 395 N thrust, 3.3 kg mass (T/W ≈12 as published). Source: PBS Aerospace.
- All HFP-X engine counts, ratings, installation masses, inlet/exhaust losses, and throttle maps TBD/TBC.

**Reference system class (REFERENCE-CLASS — not HFP-X selection):**

- Gravity Industries jet suit: 5 turbines, ≈1400–1700 N total thrust, ≈27 kg system mass, Jet A / diesel fuel, flight typically 1–4 min (claims to ~8–10 min). Sources: Gravity Industries; NATO/Milipol reporting; WIRED 2020.
- No HFP-X mass, thrust, or endurance is inferred; HFP-X hover thrust, gross mass, reserves, and endurance all TBD.

### 8.2 Ordinal assessment (1–5 per criterion with one-line rationale each)

Scores are qualitative ordinals for MVP-demonstrator comparison; totals are unweighted sums (TBC). Rationales cite only §8.1 data or explicitly qualitative handling/maturity judgement; all HFP-X quantities TBD.

| Candidate | C1 Energy (system) | C2 Power/weight | C3 Throttle/transient | C4 Personnel/range safety | C5 Logistics | C6 Maturity/TRL | C7 Cert path | Ordinal total (TBC) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (a) Jet-fuel turbine | 5 — Highest cited usable density (43 MJ/kg; minimal storage penalty; 775–840 kg/m³). | 5 — Only candidate with published wearable-scale T/W (6.4–7.2; 12 for smaller unit) reference-class. | 5 — Turbine throttle precedent in Gravity-class reference system. | 3 — Hot efflux + fuel-fire hazard, but kerosene handling precedent exists. | 5 — Jet A-1 supply/handling precedent at test ranges. | 5 — Published specs + Gravity-class flight precedent. | 3 — Manned-rating remains hard; MVP demonstrator path least-burdened of chemical options (qualitative). | 31 |
| (b) Ethanol turbine | 4 — Cited 26.9 MJ/kg (≈37% penalty vs Jet A-1); storage penalty small. | 4 — Turbine-class power density; ethanol derate/integration TBC. | 4 — Turbine-like transients expected; ethanol tuning TBC. | 3 — Flammability/handling burden similar order; toxicity/visibility differences TBC. | 4 — Obtainable fuel; airfield handling less standard than Jet A-1 (qualitative). | 3 — Less wearable-scale turbine-on-ethanol flight precedent than Jet A-1. | 3 — Similar manned-rating burden as (a); fuel-approval delta TBC. | 25 |
| (c) H2 turbine, LH2 | 3 — Chemical 120 MJ/kg offset by small-scale LH2 20–30% efficiency (≈7–10 kWh/kg-system); cryo overhead TBD. | 3 — Turbine core compact but LH2 tank + insulation + vent burden at small scale TBD. | 4 — Turbine-like transients expected; LH2 conditioning dynamics TBD. | 2 — Cryogenic + leak/embrittlement + exclusion burden; no MVP handling precedent. | 2 — LH2 supply, liquefaction, boil-off, turnaround burden at test range (qualitative). | 2 — No wearable-scale LH2-turbine flight precedent cited. | 2 — Cryogenic manned-flight certification path longest (qualitative). | 18 |
| (d) H2 turbine, 700-bar | 2 — Cited ≈5–6 wt% system (≈2 kWh/kg-system); worst cited system energy of chemical candidates. | 2 — High-pressure vessel mass dominates at small scale (qualitative; vessel mass TBD). | 4 — Turbine-like transients expected; high-pressure feed dynamics TBD. | 2 — 700-bar stored-energy + leak/dispersion burden; no MVP precedent. | 2 — High-pressure fill/compliance/turnaround burden (qualitative). | 2 — No wearable-scale 700-bar-turbine flight precedent cited. | 2 — Pressure-vessel + manned-flight path burden (qualitative). | 16 |
| (e) H2-electric fuel cell | 2 — Same storage penalties as (c)/(d) plus stack + power-electronics + motor masses TBD. | 2 — Stack + storage + motor system mass unproven at required hover power TBD. | 3 — Electric response good; fuel-cell transient/augmentation architecture TBD. | 2 — Hydrogen hazards as (c)/(d) plus high-voltage DC bus TBD. | 2 — Hydrogen logistics as (c)/(d) plus spares/conditioning TBD. | 2 — No wearable-scale fuel-cell hover precedent cited. | 2 — Combined hydrogen + electric-propulsion manned path (qualitative). | 15 |
| (f) Battery-electric | 1 — Cited cells 0.9–1.1 MJ/kg, packs 60–70% (≈40–48× gap vs Jet A-1 at cell level; ≈57–80× at pack level as shown). | 2 — Motors power-dense but system endurance collapses under storage mass (see §12). | 5 — Electric throttle/transient best in class (qualitative). | 4 — No hot efflux/fuel fire; thermal-runaway/containment still required TBD. | 4 — Charging logistics simple; turnaround energy TBD. | 4 — Multicopter TRL high generally, but no HFP-X-class hover-endurance precedent. | 3 — Electric manned path exists in principle; endurance gap blocks MVP (qualitative). | 23 |

### 8.3 Findings (honest reading of §8.1–§8.2)

- Jet-fuel turbine leads for MVP on cited energy + published T/W + handling/maturity precedent; no other candidate matches all three simultaneously on cited data.
- Battery-electric is infeasible for hover endurance by the energy gap (math in §12; pack masses become orders of magnitude above reference-class fuel masses for the same stored energy).
- Hydrogen is attractive on chemical gravimetric basis (120 MJ/kg) but small-scale storage penalties (≈2 kWh/kg-system at 700 bar; ≈7–10 kWh/kg-system small LH2) plus cryogenic/pressure handling burden and absence of MVP precedent place it behind jet-fuel for MVP; large-tank 65–70% efficiencies are not applicable at HFP-X scale.
- Ethanol is the viable fallback on cited data with ≈37% LHV penalty vs Jet A-1; turbine integration, derate, and approval deltas TBC.

## 9. Interfaces

Trade inputs: Vol 05 (fuel properties, storage concepts — TBD), Vol 14 (thermal loads — TBD), Vol 07 (thrust/power demand profiles — TBD), Vol 08 (health/monitoring hooks — TBD), Vol 13 (hazard inputs — TBD). Trade outputs: conditional recommendation and confirmation-data needs to SRR and selection DDR; interface signal/pin/flow definitions TBD in ICDs (TBC).

> **Hazardous-subsystem boundary.** Interface discussion is limited to analysis ownership and data needs. No fabrication, plumbing, wiring, fuelling, or test procedures are provided.

## 10. Operational Concept

Trade is evaluated against hover, transition, and cruise phases at concept level. Hover sizes stored-energy and thermal margins; transition stresses throttle/transient; cruise stresses cruise SFC/efficiency. Phase durations, duty cycles, reserves, abort energy, and range rules all TBD/TBC. Operational procedures, checklists, start-up/shutdown sequences, and flight operations are TBD under Ch 04.9 / Vol 07 / Vol 13 and are not contained here.

## 11. Safety

Safety-relevant discriminators (analysis inputs to Vol 13 FHA/FMEA/FTA; no operating instructions):

- Kerosene/ethanol turbines: hot efflux, fuel fire, ingestion, noise; handling precedent exists but personnel-exclusion, abort, and range-safety cases TBD.
- Hydrogen (LH2 / 700-bar / fuel cell): cryogenic burns, embrittlement, leak/dispersion, overpressure, venting, high-voltage (fuel-cell variant); exclusion, detection, and abort cases TBD with larger burden (qualitative assessment in §8.2).
- Battery-electric: thermal runaway, containment, high-voltage; efflux/fire profile differs but endurance gap (§12) dominates MVP feasibility.
- Independent safety-path authority, FHA/FMEA/FTA, and SRR safety review are required prior to any selection DDR (confirmation need).

> **Hazardous-subsystem boundary.** Safety content is limited to trade discriminators and analysis inputs. No instructions for constructing, igniting, testing with fuel, or operating high-energy propulsion outside controlled conditions.

## 12. Performance

All HFP-X performance TBD/TBC except the cited-data checks below (labelled illustrative, reference-class; not HFP-X requirements or predictions).

**SFC-to-endurance check (illustrative, reference-class — frames ISS-007):**

- At cited SFC 0.116 kg/N/h and illustrative hover thrust ≈1300 N (reference-class, Gravity-class order — not an HFP-X requirement): fuel flow = 0.116 × 1300 = 150.8 kg/h ≈ 150 kg/h → 10 kg fuel ÷ 150.8 kg/h × 60 min/h ≈ 3.98 min ≈ 4 min hover (propulsive fuel only; reserves, throttle variation, installation losses, and Accountability factors TBD).
- This reproduces the Gravity-class endurance order of magnitude (cited typically 1–4 min, claims to ~8–10 min) and frames the ISS-007 budget: HFP-X endurance/energy budgets remain TBD and must close the same SFC-vs-stored-energy loop with HFP-X masses and margins.

**Battery hover-energy gap (illustrative, from cited figures):**

- Same illustrative point: 5-min hover at ≈150 kg/h reference-class flow → 150 × 5/60 = 12.5 kg fuel (reference-class illustration only) → chemical energy 12.5 × 43 = 537.5 MJ.
- Battery-pack mass for the same stored energy (before efficiency/discount factors, all TBD): at cited pack illustration 150–210 Wh/kg (0.54–0.756 MJ/kg) → 537.5 ÷ 0.54 ≈ 995 kg to 537.5 ÷ 0.756 ≈ 711 kg; at X-57 point 149 Wh/kg (0.536 MJ/kg) → ≈1,002 kg. Even the 10-kg-fuel (≈430 MJ) equivalence needs ≈569–796 kg pack (430 ÷ 0.756 ≈ 569; 430 ÷ 0.54 ≈ 796). Usable-depth, discharge-rate, reserve, and drivetrain-efficiency effects (TBD) worsen the comparison. HFP-X hover power, mass, and endurance TBD — the gap direction is robust to TBD margins on cited data alone.

## 13. Verification & Validation

- Verified by review against REQ-HFPX-TDE-001..006 (criteria applied, candidates scored, sources cited, conditional-only recommendation, deferred decision, update rule).
- SFC/endurance and ratio arithmetic verified by inspection (derivations shown in §8/§12 from cited inputs).
- Validation deferred: SRR review, Vol 13 safety review, and confirmation testing / modelling (Vol 19 methodology TBD) feed the future selection DDR. No fuelled or high-energy operation is authorised by this document.

## 14. Risks

- Selection pressure before confirmation data closes — mitigation: conditional-only recommendation + deferred DDR (REQ-HFPX-TDE-004/005).
- Small-scale hydrogen storage underperformance vs large-tank analogies — mitigation: explicitly rule 65–70% large-tank figures not applicable; require small-scale tank data (TBD) before any hydrogen reconsideration.
- Battery-projection optimism (400–500 Wh/kg cell reference-class) masking MVP gap — mitigation: assess on current cited cells/packs (250–300 Wh/kg; 60–70% pack factor; X-57 point) and treat projections as TBC.
- Reference-class overreach (PBS/Gravity data read as HFP-X guarantees) — mitigation: every HFP-X value TBD; reference figures fenced as REFERENCE-CLASS.

## 15. Open Issues

- ISS-003 stays OPEN until selection DDR — no selection baselined by this revision.
- ISS-007 (endurance/energy budget) OPEN — HFP-X thrust, mass, SFC installed, reserves, and endurance TBD; §12 check is framing only.
- Confirmation data needs (TBD owners/dates): HFP-X demand profile (Vol 07); installed SFC/throttle map (TBD rig methodology, no fuelled procedure here); storage-system masses at HFP-X scale (Vol 05); thermal loads (Vol 14); Vol 13 hazard/safety-path inputs; SRR entry criteria and selection-DDR criteria (TBD).
- Ethanol derate/materials/approval deltas TBC; hydrogen small-scale tank + handling case TBD; battery usable-energy/drivetrain chain TBD.

## 16. Assumptions

TBD — No assumptions are made in this trade study; all undecided values are recorded as TBD, TBC, or reference-class with sources cited where applicable.

## 17. Dependencies

Depends on ISS-003/ISS-007 resolution path, Ch 04.1 requirements, HFPX-PROP-ARC-001 chain structure, Vol 05 fuel/storage inputs, Vol 07 demand profiles, Vol 08 monitoring hooks, Vol 13 safety analyses and safety review, Vol 14 thermal inputs, SRR gate, and Vol 19 verification methodology. Source documents as listed in §3 (retrieval date 2026-09-29 for all published-data sources).

## 18. Traceability

- Parents: ISS-003 (trade), ISS-007 (budget framing); REQ-HFPX-PAR-002 (chain structure pending trade).
- This document: REQ-HFPX-TDE-001..006 → CONCEPT (this revision).
- Children (TBD): selection DDR (follows only upon selection, per §6/§15), SRR inputs, Vol 05/07/08/13/14 subsystem updates, ICDs.
- RTM status: trade complete as analysis; selection NOT baselined; ISS-003 remains OPEN.

## 19. Configuration

BL-0.0 (structure only) — Tranche 7 draft, not baselined. Trade analysis only; registers, READMEs, and baselines untouched by this revision. Changes require change control; selection requires a selection DDR.

**Conditional recommendation (not a decision):** jet-fuel turbine for the MVP demonstrator, subject to SRR and Vol 13 safety review and confirmation of HFP-X demand profile, installed performance, storage/integration masses, thermal loads, and range-safety case (all TBD). Ethanol retained as fallback (≈37% LHV penalty, integration TBC). Hydrogen (either storage) and hydrogen-electric not recommended for MVP on cited small-scale storage + handling/maturity grounds; battery-electric not recommended for MVP hover endurance on cited energy-gap grounds. DECISION EXPLICITLY DEFERRED — no DDR is recorded by this revision; a DDR follows only upon selection.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 7 draft (propulsion energy-source trade study, conditional only, decision deferred) |
