# HFP-X Airframe-Concept Trade Study

**Document ID:** HFPX-STR-TRD-001  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only) — Tranche 7 draft, not baselined  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

## 1. Purpose

Define and record the airframe-concept trade study for HFP-X: trade criteria, candidate concepts, qualitative assessment with ordinal judgement scoring, data needs, conditional recommendation, and deferral of selection. This revision establishes trade structure and traceability only; no selection is made and no measured values are stated.

## 2. Scope

Covers the airframe-concept trade governed by ISS-004. Applies to five candidate concepts: conventional wing; lifting body; blended lifting body; deployable wing; hybrid architecture. Applies to prone distributed-propulsion VTOL and transition. Excludes concept selection, sizing, geometry, loads definition (Chapter 03.13), strength and testing (Chapters 03.14–03.20), and propulsion, control-law, and human-systems design owned by other volumes. Selection is explicitly out of scope at this revision; the decision is deferred per Section 6.

## 3. Applicable Documents

- HFPX-STR-ARC-001 Airframe Architecture (parent structural decomposition and ISS-004 input capture)
- HFPX-SYS-ARC-001 SAD, physical view (SYS tier parent, via HFPX-STR-ARC-001)
- HFPX-SYS-REQ-001 SyRS (SYS tier parent requirements, via SAD)
- ISS-004 airframe-concept trade (governing open issue; no selection recorded)
- ISS-006 control-authority allocation (linked criterion; TBD)
- Volume 06 Chapters 06.11 (6-DOF methodology, TBD), 06.19 (CFD methodology, TBD), 06.20 (wind-tunnel methodology, TBD), 19.3 (6-DOF verification methodology cross-reference, TBD)
- Gravity Industries — jet suit with distributed micro-turbines, arm-vectoring, and minimal lifting surfaces; company information (retrieval 2026-09-29) — precedent for thrust-borne hover with body-position control, not a selection
- WIRED (2020) — reporting on Gravity Industries jet suit flight demonstration (retrieval 2026-09-29) — precedent context for thrust-borne hover, not a selection
- Interface register (TBD)

## 4. Definitions & Acronyms

- STR: structures domain, Volume 03
- TRD: trade study document type
- CONCEPT: status label meaning pre-decision concept description; no selection or sizing implied
- TBD: to be determined; TBC: to be confirmed
- ISS-004: open issue governing airframe-concept trade; stays OPEN at this revision
- ISS-006: open issue governing control-authority allocation (linked to control-authority contribution criterion)
- Ordinal 1–5: judgement-based rank ordering only (5 = most favourable judgement, 1 = least favourable judgement); not a measurement, not a computed score, not a weighting outcome
- Hover download penalty: adverse download on airframe surfaces from distributed-propulsion slipstream in hover
- Transition behaviour: handling and configuration continuity between hover, transition, and cruise
- Lift-sharing: distribution of weight support between powered lift and aerodynamic lift
- DDR: design decision review (future, gated on screening evidence; TBD)
- CFD: computational fluid dynamics (methodology per 06.19, TBD)
- 6-DOF: six-degree-of-freedom flight-dynamics modelling (methodology per 06.11 / 19.3, TBD)

## 5. System Context

The airframe concept determines how lifting surfaces, pilot volume, and propulsion mounts are arranged for a prone distributed-propulsion VTOL that must hover, transition, and cruise. The trade sits between the airframe architecture (HFPX-STR-ARC-001) and future loads, strength, dynamics, and test evidence (Chapters 03.13–03.20; Volume 06). Context inputs: SYS-tier requirements via the SAD physical view; ISS-004 as the governing trade issue; ISS-006 as the control-authority allocation link; Volume 06 analysis and test methodology (TBD). No evidence base exists at this revision; assessment is qualitative and judgement-based.

Reference precedent: the Gravity Industries jet suit demonstrates thrust-borne hover using distributed micro-turbines with arm-vectoring and body-position control with minimal lifting surfaces (Gravity Industries; WIRED 2020; retrieval 2026-09-29). It is cited only as evidence that thrust-borne hover with body-position control is an existing precedent class, and as context for why HFP-X lifting-surface concepts must justify their hover-download and transition behaviour relative to a minimal-surface thrust-borne baseline. It is not a candidate, not a baseline, and not a selection.

## 6. Requirements

| ID | Requirement (shall) | Parent | Verification |
| --- | --- | --- | --- |
|REQ-HFPX-TFA-001|The airframe-concept trade criteria shall be defined, with a recorded rationale for why each criterion matters for prone distributed-propulsion VTOL/transition.|SYS tier via SAD physical view; ISS-004|Inspection|
|REQ-HFPX-TFA-002|Each candidate concept shall be assessed qualitatively against each defined criterion, recording strengths and concerns with an ordinal 1–5 judgement rank and a one-line rationale.|SYS tier via SAD physical view; ISS-004|Inspection|
|REQ-HFPX-TFA-003|Each candidate-by-criterion assessment cell shall enumerate the data need (analysis or test) that would confirm or refute the judgement.|SYS tier via SAD physical view; ISS-004|Inspection|
|REQ-HFPX-TFA-004|Any trade recommendation shall be stated as conditional on future screening evidence and shall not constitute selection.|SYS tier via SAD physical view; ISS-004|Inspection|
|REQ-HFPX-TFA-005|The concept-selection decision shall be deferred to a future DDR gated on defined screening evidence; ISS-004 shall remain OPEN at this revision.|SYS tier via SAD physical view; ISS-004|Inspection|
|REQ-HFPX-TFA-006|This trade study shall be updated when screening evidence becomes available, recording evidence references and revised judgements without back-editing prior judgements.|SYS tier via SAD physical view; ISS-004|Inspection|

Scoring note (applies to all of Sections 7–8 and 12): all 1–5 values in this document are ORDINAL judgement ranks only, assigned at CONCEPT stage without analysis or test evidence. They express relative reviewer judgement, not measured performance. Higher means judged more favourable. No masses, areas, coefficients, loads, stresses, or computed scores are stated.

## 7. Architecture

Trade method: define criteria (this section); assess each candidate per criterion qualitatively with ordinal judgement plus data need (Section 8); synthesise findings without selection (Section 12); defer decision to a future evidence-gated DDR (Sections 13 and 15).

Criteria definitions — each defined with why it matters for prone distributed-propulsion VTOL/transition:

1. Hover download penalty — why it matters: distributed-propulsion slipstream impinges on airframe surfaces in hover; download directly opposes thrust-borne lift and degrades hover efficiency and control margin. A concept that minimises obstructed area in the slipstream preserves hover authority.
2. Transition behaviour — why it matters: the vehicle must pass continuously from thrust-borne hover through a mixed-lift regime to wing-borne cruise without discontinuities in lift, trim, or handling that the pilot or control system cannot manage.
3. Cruise lift-sharing efficiency — why it matters: in cruise, aerodynamic surfaces should relieve propulsion of weight support; poor lift-sharing leaves propulsion carrying weight it need not carry, penalising the cruise segment.
4. Structural mass outlook — why it matters: qualitative judgement of whether the concept implies simple, continuous load paths or complex, interrupted, or mechanism-dependent load paths; heavier or more complex structure propagates into every phase. No mass values are stated.
5. Pilot integration (prone loads/restraint) — why it matters: the prone pilot is both payload and control effector; the concept must accommodate restraint loads, body-position control range, visibility, and ingress/egress without compromising structure or handling.
6. Control-authority contribution (ISS-006 link) — why it matters: the airframe either aids or hinders control power from propulsion vectoring, aerodynamic surfaces, and body-position inputs across hover, transition, and cruise; assessment here is an input to ISS-006 allocation, not the allocation itself.
7. Manufacturability/testability — why it matters: a concept that cannot be built or tested at subscale or full scale with available methodology (CFD per 06.19, tunnel per 06.20, 6-DOF per 06.11/19.3) cannot generate the evidence needed for downselect.
8. Growth/adaptability — why it matters: the concept should tolerate future changes in propulsion layout, pilot accommodation, or mission demands without requiring a clean-sheet rearrangement.

Candidates (from ISS-004; no selection; listed without preference order):

- C1 Conventional wing: distinct fuselage/body volume carrying the prone pilot with discrete attached wing surfaces for cruise lift.
- C2 Lifting body: pilot volume shaped as the primary lifting form; no discrete wing; lift from body shaping across transition and cruise.
- C3 Blended lifting body: pilot volume blended continuously into lifting surfaces; intermediate between discrete wing and pure lifting body.
- C4 Deployable wing: lifting surfaces stowed or retracted in hover and deployed for transition/cruise; mechanism-dependent configuration change.
- C5 Hybrid architecture: combinable features of the above (e.g., body lift plus discrete or deployable surfaces); arrangement TBD.

## 8. Detailed Design

Not applicable at this revision — no geometry, sizing, section properties, or construction detail is stated. This section records the qualitative candidate assessment. Each cell: strengths/concerns, ordinal 1–5 judgement with one-line rationale, and DATA NEED naming the confirming analysis or test.

Conventions: CFD screening per 06.19; wind-tunnel per 06.20; first-order 6-DOF per 06.11/19.3. All ordinals are judgement-based at CONCEPT stage; no evidence exists.

### 8.1 C1 — Conventional wing

| Criterion | Strengths / Concerns | Ordinal (judgement) + Rationale | Data Need |
| --- | --- | --- | --- |
| Hover download penalty | Strength: well-understood layout. Concern: discrete wing sits in distributed-propulsion slipstream in hover, judged worst for obstructed download. | 1 — judged most exposed wing area in hover slipstream | CFD hover-download screening per 06.19; tunnel hover-download per 06.20 |
| Transition behaviour | Strength: conventional aero behaviour best understood. Concern: abrupt shift from thrust-borne to wing-borne lift as wing becomes effective. | 3 — judged predictable but discontinuous across transition | First-order 6-DOF transition sweep per 06.11/19.3; CFD transition matrix per 06.19 |
| Cruise lift-sharing efficiency | Strength: discrete wing purpose-built for cruise lift. | 4 — judged efficient cruise lift-sharing once established | CFD cruise polar screening per 06.19; tunnel cruise polar per 06.20 |
| Structural mass outlook | Strength: simple wing-box and fuselage load paths; simplest to analyse. | 4 — judged simplest load paths of the candidates | Load-path review per 03.13 methodology (TBD); no sizing at this revision |
| Pilot integration | Concern: fuselage optimised around wing carry-through conflicts with prone volume, restraint, and body-position range. | 2 — judged weakest pilot-volume integration alongside download | Human-systems review with Vols 10/12 (TBD); mock-up/restraint assessment (TBD) |
| Control-authority contribution (ISS-006 link) | Strength: conventional surfaces give familiar cruise authority. Concern: contributes little in hover; input to ISS-006, not the allocation. | 3 — judged cruise-strong, hover-neutral | 6-DOF control-power sweep per 06.11/19.3 as input to ISS-006 |
| Manufacturability/testability | Strength: simplest to build and test at subscale; standard tunnel models and CFD cases. | 5 — judged simplest to analyse, build, and test | CFD screening per 06.19; tunnel per 06.20 |
| Growth/adaptability | Strength: wing and body can be resized semi-independently. | 3 — judged moderately adaptable within conventional limits | Configuration sensitivity review (TBD) |

### 8.2 C2 — Lifting body

| Criterion | Strengths / Concerns | Ordinal (judgement) + Rationale | Data Need |
| --- | --- | --- | --- |
| Hover download penalty | Strength: compact form with less extended surface in slipstream than a discrete wing. Concern: broad body still obstructs distributed flow. | 3 — judged less exposed than a wing, more than stowed | CFD hover-download screening per 06.19; tunnel hover-download per 06.20 |
| Transition behaviour | Strength: lift builds progressively with body angle and speed; no deployment event. Concern: body lift onset poorly characterised without data. | 3 — judged continuous in principle, unproven in evidence | First-order 6-DOF transition sweep per 06.11/19.3; CFD transition matrix per 06.19 |
| Cruise lift-sharing efficiency | Strength: whole body contributes lift. Concern: body lift efficiency judged below a purpose-built wing. | 2 — judged cruise lift-sharing weaker than winged concepts | CFD cruise screening per 06.19; tunnel cruise polar per 06.20 |
| Structural mass outlook | Strength: continuous shell load paths possible. Concern: doubly-curved shell and cutouts for pilot/propulsion complicate paths. | 3 — judged continuous but harder to analyse than C1 | Load-path review per 03.13 methodology (TBD) |
| Pilot integration | Strength: pilot volume is the lifting form, aiding restraint-load integration. Concern: shaping driven by aero may fight ergonomics and visibility. | 3 — judged integrated but ergonomically constrained | Human-systems review with Vols 10/12 (TBD); mock-up assessment (TBD) |
| Control-authority contribution (ISS-006 link) | Strength: body moments available across regimes. Concern: surface authority limited without discrete surfaces; input to ISS-006. | 2 — judged modest airframe control contribution | 6-DOF control-power sweep per 06.11/19.3 as input to ISS-006 |
| Manufacturability/testability | Strength: single-form test articles feasible. Concern: body-flow CFD and tunnel behaviour harder to predict than a wing. | 3 — judged testable but less standard than C1 | CFD screening per 06.19; tunnel per 06.20 |
| Growth/adaptability | Concern: propulsion or pilot changes reshape the lifting form itself. | 2 — judged tightly coupled, harder to grow | Configuration sensitivity review (TBD) |

### 8.3 C3 — Blended lifting body

| Criterion | Strengths / Concerns | Ordinal (judgement) + Rationale | Data Need |
| --- | --- | --- | --- |
| Hover download penalty | Strength: smooth planform with less discrete obstruction than C1. Concern: large wetted area still in distributed slipstream. | 3 — judged intermediate hover obstruction | CFD hover-download screening per 06.19; tunnel hover-download per 06.20 |
| Transition behaviour | Strength: judged best hover-to-cruise continuity — body lift hands progressively to blended surfaces with no deployment event. Concern: interference flows unmodelled. | 4 — judged most continuous transition conceptually | First-order 6-DOF transition sweep per 06.11/19.3; CFD transition matrix per 06.19 |
| Cruise lift-sharing efficiency | Strength: body plus blended surfaces share lift across cruise. | 4 — judged strong lift-sharing conceptually | CFD cruise screening per 06.19; tunnel cruise polar per 06.20 |
| Structural mass outlook | Strength: continuous blended load paths possible. Concern: complex curvature, junctions, and cutouts; hardest to model credibly without data. | 2 — judged potentially efficient but highest modelling uncertainty | Load-path review per 03.13 methodology (TBD) |
| Pilot integration | Strength: judged best pilot-volume integration — prone volume blends into lifting form rather than fighting a wing carry-through. Concern: egress and visibility shaping still open. | 4 — judged most accommodating pilot integration conceptually | Human-systems review with Vols 10/12 (TBD); mock-up assessment (TBD) |
| Control-authority contribution (ISS-006 link) | Strength: distributed surfaces plus body moments across regimes. Concern: effectiveness unproven; input to ISS-006. | 4 — judged broadest airframe control contribution conceptually | 6-DOF control-power sweep per 06.11/19.3 as input to ISS-006 |
| Manufacturability/testability | Concern: complex blended geometry is hardest to build precisely and mesh credibly at this stage. | 2 — judged hardest to model and test credibly pre-screening | CFD screening per 06.19; tunnel per 06.20 with geometry-fidelity review |
| Growth/adaptability | Strength: blending offers multiple growth paths (span, body, surfaces). | 4 — judged most adaptable arrangement conceptually | Configuration sensitivity review (TBD) |

### 8.4 C4 — Deployable wing

| Criterion | Strengths / Concerns | Ordinal (judgement) + Rationale | Data Need |
| --- | --- | --- | --- |
| Hover download penalty | Strength: stowed surfaces minimise hover obstruction. | 4 — judged cleanest hover configuration when stowed | CFD stowed-hover screening per 06.19; tunnel stowed-hover per 06.20 |
| Transition behaviour | Concern: deployment event mid-transition introduces configuration, trim, and timing discontinuities. | 2 — judged most discontinuous transition behaviour | First-order 6-DOF with deployment-event modelling per 06.11/19.3; CFD deployed/transit matrix per 06.19 |
| Cruise lift-sharing efficiency | Strength: deployed wing purpose-built for cruise, as in C1. | 4 — judged efficient once deployed and locked | CFD deployed-cruise screening per 06.19; tunnel deployed polar per 06.20 |
| Structural mass outlook | Concern: hinges, actuators, locks, and interrupted load paths add mechanism mass and complexity qualitatively. | 1 — judged heaviest mechanism burden conceptually | Load-path and mechanism review per 03.13/03.9 methodology (TBD) |
| Pilot integration | Strength: stowed hover keeps pilot volume clear. Concern: deployment path, locks, and failure states interact with restraint and egress. | 3 — judged neutral, mechanism-dependent | Human-systems review with Vols 10/12 (TBD); deployment-failure review (TBD) |
| Control-authority contribution (ISS-006 link) | Concern: control configuration changes with deployment state; partial-deployment authority uncertain; input to ISS-006. | 2 — judged state-dependent and uncertain | 6-DOF multi-configuration control sweep per 06.11/19.3 as input to ISS-006 |
| Manufacturability/testability | Concern: mechanism fidelity dominates test-article cost; aero-structural coupling hardest to test. | 2 — judged mechanism risk dominates testability | CFD per 06.19; tunnel per 06.20 including transit configurations; mechanism test per TBD |
| Growth/adaptability | Concern: growth constrained by stow volume and mechanism limits. | 2 — judged constrained by stow and mechanism envelope | Configuration sensitivity review (TBD) |

### 8.5 C5 — Hybrid architecture

| Criterion | Strengths / Concerns | Ordinal (judgement) + Rationale | Data Need |
| --- | --- | --- | --- |
| Hover download penalty | Strength: can combine compact body with minimal fixed surfaces. Concern: combined features risk combined obstruction. | 2 — judged additive obstruction without optimisation | CFD hover-download screening per 06.19; tunnel hover-download per 06.20 |
| Transition behaviour | Strength: multiple lift sources available across regimes. Concern: interactions between body, fixed, and any deployable elements uncharacterised. | 2 — judged flexible but most interference-prone | First-order 6-DOF transition sweep per 06.11/19.3; CFD interaction matrix per 06.19 |
| Cruise lift-sharing efficiency | Strength: body plus surfaces share lift. Concern: compromises likely underperform purpose-built options. | 3 — judged middling lift-sharing without optimisation | CFD cruise screening per 06.19; tunnel cruise polar per 06.20 |
| Structural mass outlook | Concern: mixed construction with multiple junction types; load paths TBD. | 2 — judged complex junctions, undefined paths | Load-path review per 03.13 methodology (TBD) |
| Pilot integration | Strength: arrangement freedom may accommodate pilot needs. Concern: undefined arrangement means undefined integration. | 3 — judged open, neither advantaged nor penalised yet | Human-systems review with Vols 10/12 (TBD) |
| Control-authority contribution (ISS-006 link) | Strength: most effector options available. Concern: allocation most complex; input to ISS-006. | 3 — judged most options, most allocation complexity | 6-DOF control-power sweep per 06.11/19.3 as input to ISS-006 |
| Manufacturability/testability | Concern: hybrid test articles combine the difficulties of their parents. | 2 — judged testable only after parents are screened | CFD screening per 06.19; tunnel per 06.20, sequenced after parent concepts |
| Growth/adaptability | Strength: hybridity is itself a growth path. | 4 — judged adaptable by definition, at complexity cost | Configuration sensitivity review (TBD) |

### 8.6 Ordinal comparison (judgement only, not measured)

| Criterion | C1 Conventional | C2 Lifting body | C3 Blended | C4 Deployable | C5 Hybrid |
| --- | --- | --- | --- | --- | --- |
| Hover download penalty | 1 | 3 | 3 | 4 | 2 |
| Transition behaviour | 3 | 3 | 4 | 2 | 2 |
| Cruise lift-sharing efficiency | 4 | 2 | 4 | 4 | 3 |
| Structural mass outlook | 4 | 3 | 2 | 1 | 2 |
| Pilot integration | 2 | 3 | 4 | 3 | 3 |
| Control-authority contribution | 3 | 2 | 4 | 2 | 3 |
| Manufacturability/testability | 5 | 3 | 2 | 2 | 2 |
| Growth/adaptability | 3 | 2 | 4 | 2 | 4 |

All values are ordinal judgement ranks (5 = most favourable judgement). They are not measurements, not computed totals, and shall not be summed or weighted at this revision. No candidate wins on evidence because no evidence exists.

## 9. Interfaces

Trade inputs and outputs are TBD and will be recorded in the interface register. Expected interface groups: criteria and screening methodology with Volume 06 (CFD per 06.19, tunnel per 06.20, 6-DOF per 06.11/19.3); control-authority inputs to ISS-006; pilot/restraint coordination with Volumes 10 and 12 via Chapter 03.5; propulsion-mount coordination with Volume 04 via Chapter 03.6; selection-decision input to HFPX-STR-ARC-001 and the future DDR. Interface methodology: name each interface, identify owner on each side, and record status in the register.

## 10. Operational Concept

The trade supports all flight and ground phases defined by the operational concept (TBD), with emphasis on hover, transition, and cruise. Phase-to-candidate mapping methodology: record for each candidate which phases it serves thrust-borne, mixed-lift, or wing-borne, and which phase transitions require configuration change (C4 deployment) or regime blending (C2/C3). No phase-specific values are stated.

## 11. Safety

Trade safety methodology: record for each candidate the qualitatively judged failure-consequence drivers (e.g., C4 deployment/lock failure states; C3/C5 complex-structure inspectability; C1/C2 fixed-configuration simplicity) as inputs to system safety analyses (Volume 13, TBD) and to Chapters 03.4 and 03.14–03.16. No safety targets, probabilities, or values are stated. No candidate is excluded on safety grounds at this revision for lack of evidence.

## 12. Performance

Findings, stated honestly on judgement alone (no evidence exists):

- No candidate wins on evidence. None exists at this revision; all ordinals are judgement-based.
- The blended lifting body (C3) is the most BALANCED conceptually — judged strongest on hover-to-cruise continuity, cruise lift-sharing, pilot-volume integration, control-authority contribution, and growth — but carries the highest modelling uncertainty and is judged weakest alongside others on manufacturability/testability and structural-mass confidence.
- The conventional wing (C1) is simplest to analyse, build, and test (ordinal 5 manufacturability/testability) but judged weakest for hover download penalty and weak for pilot integration.
- The deployable wing (C4) offers the judged-cleanest stowed hover but adds mechanism risk: judged lowest on structural-mass outlook and discontinuous on transition behaviour.
- The lifting body (C2) and hybrid (C5) are judged middling across most criteria, with C2 tightly coupled against growth and C5 carrying combination complexity.
- Conditional recommendation only (per REQ-HFPX-TFA-004): subject to screening evidence, retain C1 and C3 through parallel concept screening, with C2 as a fallback reference for body-lift behaviour; sequence C4 mechanism studies and C5 combination studies only after parent-concept screening. This recommendation is conditional and is not a selection.
- Required next step: PARALLEL concept screening — first-order 6-DOF transition and control-power sweeps (per 06.11/19.3) plus CFD screening (per 06.19), followed by tunnel checks (per 06.20) — before any downselect.

## 13. Verification & Validation

Verification by review at this revision: check that criteria are defined with VTOL/transition rationale (REQ-HFPX-TFA-001), that each candidate-by-criterion cell records strengths/concerns with an ordinal and one-line rationale (REQ-HFPX-TFA-002), that each cell names its data need (REQ-HFPX-TFA-003), that the recommendation is conditional (REQ-HFPX-TFA-004), that the decision is deferred with ISS-004 OPEN (REQ-HFPX-TFA-005), and that the update rule is recorded (REQ-HFPX-TFA-006). Later verification methodology: review of screening evidence artefacts (6-DOF sweeps, CFD matrices, tunnel results), traceability of revised judgements to evidence references, and DDR gating before selection. No pass/fail values are stated.

## 14. Risks

- Judgement mistaken for evidence; mitigation: ordinal-judgement labelling throughout, no summed scores, no selection at this revision
- Premature downselect on C3 balance before modelling uncertainty is retired; mitigation: parallel screening required before downselect; DDR gate
- Hover-download and transition-interference surprises in blended/hybrid forms; mitigation: CFD screening per 06.19 and tunnel checks per 06.20 sequenced early
- Deployable-mechanism failure states discovered late; mitigation: C4 mechanism studies sequenced after parent screening; safety input to Volume 13
- Control-authority shortfalls misattributed to airframe alone; mitigation: airframe contributions recorded as inputs to ISS-006, not as the allocation

## 15. Open Issues

- ISS-004 airframe-concept trade outcome — stays OPEN; NO SELECTION at this revision; decision deferred to a future DDR gated on parallel screening evidence (6-DOF + CFD per 06.11/19.3/06.19, tunnel per 06.20)
- Screening evidence set definition (6-DOF sweep cases, CFD matrices, tunnel entries; TBD with Volume 06)
- ISS-006 control-authority allocation inputs from this trade (TBD)
- Pilot/restraint integration inputs with Volumes 10 and 12 (TBD)
- Future DDR gating criteria and membership (TBD)

## 16. Assumptions

_TBD_

No assumptions are raised or relied upon at this revision.

## 17. Dependencies

Depends on SYS-tier requirements via the SAD physical view, ISS-004 (governing; OPEN), ISS-006 (control-authority link), Volume 06 screening methodology and capacity (06.11/19.3 6-DOF, 06.19 CFD, 06.20 tunnel), human-systems inputs from Volumes 10 and 12, and propulsion-interface inputs from Volume 04.

Reference-context dependency: Gravity Industries jet-suit precedent (distributed micro-turbines, arm-vectoring, minimal lifting surfaces; Gravity Industries; WIRED 2020; retrieval 2026-09-29) informs the thrust-borne hover context only. HFP-X lifting-surface concepts must still produce their own hover-download, transition, and lift-sharing evidence; the precedent does not substitute for screening and does not favour any candidate.

## 18. Traceability

Parent: SYS tier via SAD physical view (through HFPX-STR-ARC-001); ISS-004 governing issue. Children: future screening evidence artefacts; future DDR selection record; updates to this trade per REQ-HFPX-TFA-006. RTM: REQ-HFPX-TFA-001..006 → CONCEPT. Candidates C1..C5 → no selection. Control-authority rows → input to ISS-006.

## 19. Configuration

BL-0.0 (structure only) — Tranche 7 draft, not baselined.

## 20. Change History

| Rev | Date | Change |
| --- | --- | --- |
| A | 2026-09-29 | Initial Tranche 7 draft (airframe-concept trade; criteria, qualitative assessment with ordinal judgements, data needs, conditional recommendation; no selection; ISS-004 OPEN) |
