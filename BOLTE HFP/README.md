# BOLTE HFP-X - Programme Documentation Tree

**Document ID:** HFPX-PGM-IDX-000  
**Revision:** A (draft)  
**Status:** CONCEPT  
**Configuration:** BL-0.0 (structure only)  
**Owner:** TBD  
**Approver:** TBD  
**Date:** 2026-09-29

---

Human Flight Platform - production engineering documentation suite. Chain: MISSION -> REQUIREMENTS -> ARCHITECTURE -> DESIGN -> IMPLEMENTATION -> INTEGRATION -> VERIFICATION -> VALIDATION -> CERTIFICATION -> PRODUCTION -> OPERATIONS -> SUSTAINMENT.

Nothing in this tree is claimed compliant with any standard. Documents are *structured according to* frameworks until *verified compliant* evidence exists.

## Five backbone documents

| Document ID | Title | Volume | Status |
| --- | --- | --- | --- |
| HFPX-PGM-SEM-001 | Systems Engineering Management Plan (SEMP) | 00 | CONCEPT (not written) |
| HFPX-SYS-REQ-001 | System Requirements Specification (SyRS) | 01 | CONCEPT (not written) |
| HFPX-SYS-ARC-001 | System Architecture Description (SAD) | 02 | CONCEPT (not written) |
| HFPX-VV-PLN-001 | Verification & Validation Plan | 22 | CONCEPT (Tranche 2 draft) |
| HFPX-SAFE-CAS-001 | Safety & Airworthiness Case | 13 | CONCEPT (Tranche 2 draft) |

## Volumes

| Vol | Domain | Folder | Chapters |
| --- | --- | --- | --- |
| 00 | PGM | `00_PROGRAMME_MANAGEMENT/` | 16 |
| 01 | SYS | `01_REQUIREMENTS/` | 18 |
| 02 | ARC | `02_ARCHITECTURE/` | 17 |
| 03 | STR | `03_AIRFRAME/` | 20 |
| 04 | PROP | `04_PROPULSION/` | 17 |
| 05 | FUEL | `05_FUEL/` | 17 |
| 06 | AERO | `06_AERODYNAMICS/` | 20 |
| 07 | FCS | `07_FLIGHT_CONTROL/` | 19 |
| 08 | AVN | `08_AVIONICS/` | 17 |
| 09 | NAV | `09_SENSORS/` | 17 |
| 10 | HMI | `10_HELMET_HMI/` | 17 |
| 11 | COM | `11_COMMUNICATIONS/` | 12 |
| 12 | HUM | `12_HUMAN_INTEGRATION/` | 14 |
| 13 | SAFE | `13_SAFETY_RECOVERY/` | 18 |
| 14 | THM | `14_THERMAL/` | 14 |
| 15 | ELE | `15_ELECTRICAL/` | 14 |
| 16 | SW | `16_SOFTWARE/` | 18 |
| 17 | CYB | `17_CYBERSECURITY/` | 14 |
| 18 | AI | `18_AI/` | 12 |
| 19 | SIM | `19_SIMULATION/` | 15 |
| 20 | MFG | `20_MANUFACTURING/` | 14 |
| 21 | INT | `21_INTEGRATION/` | 13 |
| 22 | VV | `22_VERIFICATION/` | 13 |
| 23 | TEST | `23_FLIGHT_TEST/` | 18 |
| 24 | REL | `24_RELIABILITY/` | 13 |
| 25 | CERT | `25_CERTIFICATION/` | 13 |
| 26 | OPS | `26_OPERATIONS/` | 15 |
| 27 | MNT | `27_MAINTENANCE/` | 14 |
| 28 | QA | `28_QUALITY/` | 12 |
| 29 | TDATA | `29_TECHNICAL_DATA/` | 14 |
| 30 | TRN | `30_TRAINING/` | 11 |
| 31 | VAR | `31_VARIANTS/` | 10 |
| 32 | SUS | `32_SUSTAINMENT/` | 11 |
| 33 | MVP | `33_MVP/` | 20 |

## Controlled registers

Located in `00_PROGRAMME_MANAGEMENT/registers/` (hazard log in `13_SAFETY_RECOVERY/`; risk register likewise in `00_PROGRAMME_MANAGEMENT/registers/`). CSV, UTF-8. Validate with `hfpx_scaffold.py check`.

## Tranche 7 additions (beyond one-doc-per-chapter; indexes unchanged by design)

| Document ID | Title | Folder | Status |
| --- | --- | --- | --- |
| HFPX-PGM-SRR-001 | SRR Readiness Assessment (pre-SRR; recommends DO NOT CONVENE) | `00_PROGRAMME_MANAGEMENT/` | CONCEPT |
| HFPX-PROP-TRD-001 | Propulsion Energy Trade Study (conditional: jet-fuel turbine for MVP; decision deferred) | `04_PROPULSION/` | CONCEPT |
| HFPX-STR-TRD-001 | Airframe Concept Trade Study (no selection; screening required) | `03_AIRFRAME/` | CONCEPT |
| HFPX-AERO-BDG-001 | First-Issue Mass/Thrust/Energy Budgets (computed by `hfpx_budgets.py`; TBC) | `06_AERODYNAMICS/` | CONCEPT |
| HFPX-SIM-SIX-002 | 6-DOF Implementation Record (code + smoke tests; UNVERIFIED) | `19_SIMULATION/` | CONCEPT |

Code: `06_AERODYNAMICS/hfpx_budgets.py` + `budgets/*.csv`; `19_SIMULATION/hfpx_sixdof.py` + `demo/` (smoke tests pass; model UNVERIFIED per 19.15, barred from gates).

## Tranche 8 additions (SRR close-out + first evidence)

| Document ID | Title | Folder | Status |
| --- | --- | --- | --- |
| HFPX-PGM-SCO-001 | SRR Close-Out Record (methods/parents/chapters rulebook) | `00_PROGRAMME_MANAGEMENT/` | CONCEPT |
| HFPX-SYS-USR/RLB/MNT/SEC/REG/IFR/DER/RTM-001 (8 docs) | Missing Vol 01 tiers 01.5, 01.12–01.18 | `01_REQUIREMENTS/` | CONCEPT |
| HFPX-VV-VAL/VCR/RQV/ANL/INS/DEM/TST/HWV/SWV/SYV/SFV/ACC-001 (12 docs) | Missing Vol 22 chapters 22.2–22.13 | `22_VERIFICATION/` | CONCEPT |
| HFPX-SAFE-FSB-001 | Recovery Feasibility Study (parametrics; ISS-008 data needs) | `13_SAFETY_RECOVERY/` | CONCEPT |
| HFPX-SIM-VCS-001 | 6-DOF Verification Cases (5/5 PASS, tolerances TBC) | `19_SIMULATION/` | CONCEPT |
| HFPX-CERT-RES-001 | Regulatory Research Memo (Nig.CARs findings + TBD actions) | `25_CERTIFICATION/` | CONCEPT |

Code: `13_SAFETY_RECOVERY/hfpx_recovery.py` + `recovery_parametrics/*.csv`. SRR re-measurement: 517/517 chapters, 100% methods, 100% parents, 9 OPEN / 2 CLOSED issues; HOLD maintained on ownership/authority (HFPX-PGM-SRR-001 Rev B).
