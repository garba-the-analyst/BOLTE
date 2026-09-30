#!/usr/bin/env python3
"""
HFP-X programme scaffold generator and checker
==============================================

Document ID : HFPX-PGM-TOOL-001  (tool, not a controlled technical document)
Status      : PROPOSED

PURPOSE
    Builds the controlled HFP-X documentation tree (Volumes 00-33) directly
    from the schema file, so the folder/volume/chapter structure is never
    re-typed by hand and cannot drift from the source.

    It also seeds the programme registers required by the master prompt:
        - Requirements Traceability Matrix   (prompt section 10)
        - Master issue register              (prompt section 29)
        - Decision log + DDR records         (prompt section 21)
        - Assumption register                (prompt section 32)
        - Change register                    (prompt section 31)
        - Hazard log                         (prompt section 16)
        - Master Technical Baseline BL-0.0   (prompt section 30)

CONFIGURATION-CONTROL BEHAVIOUR (prompt section 3.4)
    The generator NEVER overwrites an existing file unless --force is given.
    Re-running it is therefore safe: it only creates what is missing.

USAGE
    python3 hfpx_scaffold.py build --schema HFP_Documentation_schema --out HFP-X
    python3 hfpx_scaffold.py check --schema HFP_Documentation_schema --out HFP-X

    Options for `build`:  --date YYYY-MM-DD   (default: today)   --force

WHAT THIS TOOL DOES NOT DO
    It creates NO technical content. Every technical item is created as
    status CONCEPT with "TBD". No numerical values, performance figures or
    compliance claims are generated (prompt sections 19, 25, 32).
"""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# --------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------

# Domain codes for document IDs: HFPX-<DOMAIN>-<TYPE>-<NNN>.
# Examples given in the master prompt (SYS, PROP, FCS, SAFE, TEST) are kept
# as-is; the remaining codes are PROPOSED and recorded in DDR-003.
DOMAIN_CODES: dict[int, str] = {
    0: "PGM", 1: "SYS", 2: "ARC", 3: "STR", 4: "PROP", 5: "FUEL",
    6: "AERO", 7: "FCS", 8: "AVN", 9: "NAV", 10: "HMI", 11: "COM",
    12: "HUM", 13: "SAFE", 14: "THM", 15: "ELE", 16: "SW", 17: "CYB",
    18: "AI", 19: "SIM", 20: "MFG", 21: "INT", 22: "VV", 23: "TEST",
    24: "REL", 25: "CERT", 26: "OPS", 27: "MNT", 28: "QA", 29: "TDATA",
    30: "TRN", 31: "VAR", 32: "SUS", 33: "MVP",
}

# Controlled-identifier patterns (prompt sections 7, 8, 21, 29, 31, 32).
ID_PATTERNS: dict[str, re.Pattern[str]] = {
    "doc": re.compile(r"^HFPX-[A-Z]+-[A-Z]+-\d{3}$"),
    "req": re.compile(r"^REQ-HFPX-[A-Z]+-\d{3}$"),
    "issue": re.compile(r"^ISS-\d{3}$"),
    "decision": re.compile(r"^DDR-\d{3}$"),
    "assumption": re.compile(r"^A-\d{3}$"),
    "change": re.compile(r"^CHG-\d{3}$"),
    "hazard": re.compile(r"^HAZ-\d{3}$"),
}

# Document sections, in the order mandated by prompt section 26.
DOC_SECTIONS = [
    "Purpose", "Scope", "Applicable Documents", "Definitions & Acronyms",
    "System Context", "Requirements", "Architecture", "Detailed Design",
    "Interfaces", "Operational Concept", "Safety", "Performance",
    "Verification & Validation", "Risks", "Open Issues", "Assumptions",
    "Dependencies", "Traceability", "Configuration", "Change History",
]

# The five backbone documents (schema, "The five master documents").
MASTER_DOCS = [
    ("HFPX-PGM-SEM-001", "Systems Engineering Management Plan (SEMP)", "00"),
    ("HFPX-SYS-REQ-001", "System Requirements Specification (SyRS)", "01"),
    ("HFPX-SYS-ARC-001", "System Architecture Description (SAD)", "02"),
    ("HFPX-VV-PLN-001", "Verification & Validation Plan", "22"),
    ("HFPX-SAFE-CAS-001", "Safety & Airworthiness Case", "13"),
]

HAZARD_NOTE = (
    "> **Hazardous-subsystem boundary (prompt sections 14 and 34).** Content "
    "in this volume is limited to requirements, architecture, modelling, "
    "simulation, interfaces, test methodology and safety analysis. It shall "
    "not contain instructions for constructing, igniting, or operating "
    "human-carrying high-energy propulsion outside appropriate engineering, "
    "test, safety and regulatory controls.\n"
)

VOLUME_NOTES: dict[int, str] = {
    4: HAZARD_NOTE,
    5: HAZARD_NOTE,
    13: HAZARD_NOTE,
    23: HAZARD_NOTE
    + "\n> Test progression is gated: simulation -> SIL -> HIL -> subsystem "
    "-> integrated propulsion -> unmanned -> tethered human -> controlled "
    "human flight -> envelope expansion. Gates shall not be skipped "
    "(prompt section 17).\n",
    18: "> AI operates as a monitoring/advisory layer only. Primary flight "
    "control remains deterministic, bounded and independently verifiable. "
    "AI shall never silently override pilot or safety-system authority "
    "(prompt section 24).\n",
    31: "> HFP-X Defence variant (31.3): legal, export-control and regulatory "
    "implications are TBC (see ISS-005).\n",
    33: "> This volume is SEPARATE from the production-aircraft documentation "
    "(schema note). Production-design transition is governed by 33.20.\n",
}

# Seed issues. Only issues that follow directly from the two source files.
SEED_ISSUES = [
    ("ISS-001", "Regulatory basis for a human-carrying experimental jet "
     "VTOL aircraft (NCAA and other authorities) is undetermined; current "
     "requirements must be verified from authoritative sources",
     "Programme", "Critical", "TBD",
     "Research NCAA/ICAO requirements; record in Vol 25", "TBD", "OPEN"),
    ("ISS-002", "No stakeholder needs or mission definition baselined; "
     "SyRS cannot be written until Vol 01.1-01.4 exist",
     "Programme", "Critical", "TBD",
     "Draft mission definition and CONOPS", "TBD", "OPEN"),
    ("ISS-003", "Propulsion energy-source trade study (jet fuel turbine, "
     "ethanol turbine, hydrogen turbine, hydrogen-electric, battery-electric) "
     "not started", "SYS-03", "High", "TBD",
     "Define criteria and run trade study", "TBD", "OPEN"),
    ("ISS-004", "Airframe trade study (conventional wing, lifting body, "
     "blended lifting body, deployable wing, hybrid) not started",
     "SYS-01/SYS-02", "High", "TBD",
     "Define criteria and run trade study", "TBD", "OPEN"),
    ("ISS-005", "Defence variant (Vol 31.3): legal and export-control "
     "implications not assessed", "Programme", "High", "TBD",
     "Obtain legal/regulatory advice before variant work", "TBD", "OPEN"),
    ("ISS-006", "Feasibility of hover/transition control authority for a "
     "prone or semi-prone pilot with distributed arm, rear and ankle "
     "propulsion is unanalysed", "SYS-05", "Critical", "TBD",
     "Build first-order 6-DOF model (Vol 06, Vol 19)", "TBD", "OPEN"),
    ("ISS-007", "Thrust-to-weight and energy/endurance feasibility not "
     "analysed; no mass or thrust budget exists", "SYS-03/SYS-04",
     "Critical", "TBD", "Create mass and thrust budgets (values TBD)",
     "TBD", "OPEN"),
    ("ISS-008", "Recovery-system effectiveness at low altitude and in hover "
     "is unanalysed", "SYS-16", "Critical", "TBD",
     "Recovery-system feasibility study (Vol 13.11)", "TBD", "OPEN"),
]

# Design Decision Records (prompt section 21). No numerical evidence is
# claimed: these are programme-policy and structure decisions.
SEED_DDRS = [
    {
        "id": "DDR-001",
        "title": "Unmanned-first development progression",
        "context": "HFP-X is a human-carrying, jet-powered aircraft concept "
        "with no verified performance data. Pilot risk must not precede "
        "evidence.",
        "options": "A. Gated unmanned-first progression (prompt section 17). "
        "B. Early tethered human testing. C. Direct human flight.",
        "criteria": "Pilot risk; quality of evidence before exposure; "
        "schedule; cost.",
        "evidence": "None quantitative. Programme safety policy set by BOLTE "
        "(prompt sections 17 and 34). No trade study performed.",
        "trade": "Not performed. TBD if the decision is ever reopened.",
        "selected": "A. Simulation -> SIL -> HIL -> subsystem tests -> "
        "integrated propulsion -> unmanned demonstrator -> hover -> "
        "transition -> horizontal flight -> integrated mission -> tethered "
        "human -> controlled human flight -> envelope expansion.",
        "rationale": "Highest-consequence hazards are exposed to no human "
        "until earlier gates supply evidence.",
        "consequences": "Longer schedule; requires an unmanned "
        "demonstrator airframe and ground station.",
        "risks": "Unmanned demonstrator may not represent human-carrying "
        "dynamics (pilot mass, inertia, CG). Mitigation: representative mass "
        "properties (method TBC).",
        "revisit": "After transition is demonstrated and at Flight "
        "Readiness Review.",
    },
    {
        "id": "DDR-002",
        "title": "34-volume documentation structure (Vol 00-33)",
        "context": "The programme needs one continuous engineering chain "
        "rather than disconnected essays (prompt section 36).",
        "options": "A. 34 volumes per schema, one folder each. B. Fewer, "
        "larger volumes. C. Per-discipline wikis.",
        "criteria": "Separation of requirements, design, safety, "
        "verification, certification, production and operations; ability to "
        "trace across them.",
        "evidence": "Schema file HFP_Documentation_schema.",
        "trade": "Not performed; structure adopted as supplied.",
        "selected": "A, with Volume 33 (MVP) kept separate from production "
        "documentation.",
        "rationale": "Matches the supplied schema and the prompt's "
        "documentation hierarchy exactly.",
        "consequences": "Many small documents; cross-volume traceability "
        "must be maintained via the RTM.",
        "risks": "Orphaned requirements if the RTM is not maintained.",
        "revisit": "If a volume proves too small or too large to manage.",
    },
    {
        "id": "DDR-003",
        "title": "Controlled identifier scheme and domain codes",
        "context": "Prompt section 7 requires a controlled identifier "
        "scheme; only SYS, PROP, FCS, SAFE and TEST are given as examples.",
        "options": "A. HFPX-<DOMAIN>-<TYPE>-<NNN> with one domain code per "
        "volume. B. Sequential numbers only.",
        "criteria": "Consistency with prompt examples; readability; "
        "uniqueness.",
        "evidence": "Prompt section 7 examples.",
        "trade": "Not performed.",
        "selected": "A. Domain codes for volumes not named in the prompt are "
        "PROPOSED (see DOMAIN_CODES in the generator).",
        "rationale": "Extends the prompt's own examples without changing "
        "them.",
        "consequences": "Domain codes become a controlled list; changes go "
        "through change control (prompt section 31).",
        "risks": "Type codes (SEM, CAS, IDX...) are proposed and not yet "
        "exhaustive.",
        "revisit": "When the first non-backbone documents are authored.",
    },
]

REGISTERS: dict[str, tuple[list[str], str]] = {
    # filename -> (header, ID pattern key)
    "requirements_traceability_matrix.csv": (
        ["Requirement ID", "Requirement", "Source", "Parent", "Subsystem",
         "Design Element", "Verification Method", "Verification ID",
         "Status"], "req"),
    "issue_register.csv": (
        ["ID", "Issue", "System", "Severity", "Owner", "Action",
         "Due Date", "Status"], "issue"),
    "decision_log.csv": (
        ["Decision ID", "Title", "Status", "Date", "Record"], "decision"),
    "assumption_register.csv": (
        ["ID", "Assumption", "Owner", "Validation Method", "Status",
         "Date Raised"], "assumption"),
    "change_register.csv": (
        ["Change ID", "Date", "Description", "Affected Requirements",
         "Affected Subsystems", "Affected Interfaces",
         "Affected Verification Evidence", "New Baseline"], "change"),
}
HAZARD_LOG = (
    "hazard_log.csv",
    ["Hazard ID", "Hazard", "Cause", "Effect", "Severity", "Probability",
     "Mitigation", "Verification", "Status"], "hazard")


# --------------------------------------------------------------------------
# Schema parsing
# --------------------------------------------------------------------------

@dataclass
class Volume:
    number: int
    title: str = ""
    folder: str = ""
    chapters: list[tuple[str, str]] = field(default_factory=list)

    @property
    def domain(self) -> str:
        return DOMAIN_CODES[self.number]


def parse_schema(text: str) -> dict[int, Volume]:
    """Extract volumes, titles, chapters and folder names from the schema."""
    vol_re = re.compile(r"^# VOLUME (\d{2})\s*$")
    ch_re = re.compile(r"^### (\d{2})\.(\d+) (.+?)\s*$")
    folder_re = re.compile(r"[├└]── (\d{2}_[A-Z0-9_]+)/")

    volumes: dict[int, Volume] = {}
    current: Volume | None = None
    awaiting_title = False

    for line in text.splitlines():
        m = vol_re.match(line)
        if m:
            current = Volume(number=int(m.group(1)))
            volumes[current.number] = current
            awaiting_title = True
            continue
        if awaiting_title and line.startswith("# "):
            current.title = re.sub(
                r"\b(Ai|Mvp)\b", lambda m: m.group(1).upper(),
                line[2:].strip().title())
            awaiting_title = False
            continue
        m = ch_re.match(line)
        if m and current and int(m.group(1)) == current.number:
            current.chapters.append((f"{m.group(1)}.{m.group(2)}", m.group(3)))
            continue
        m = folder_re.search(line)
        if m:
            num = int(m.group(1)[:2])
            if num in volumes:
                volumes[num].folder = m.group(1)

    problems = [v.number for v in volumes.values()
                if not v.folder or not v.title or not v.chapters]
    if problems or sorted(volumes) != list(range(34)):
        sys.exit(f"Schema parse failed; incomplete volumes: {problems}, "
                 f"found {len(volumes)} volumes (expected 34).")
    return volumes


# --------------------------------------------------------------------------
# Content builders
# --------------------------------------------------------------------------

def header(title: str, doc_id: str, today: str, status: str = "CONCEPT",
           config: str = "BL-0.0 (structure only)") -> str:
    """Document header per prompt sections 6 and 26."""
    lines = [
        f"**Document ID:** {doc_id}", "**Revision:** A (draft)",
        f"**Status:** {status}", f"**Configuration:** {config}",
        "**Owner:** TBD", "**Approver:** TBD", f"**Date:** {today}",
    ]
    return f"# {title}\n\n" + "  \n".join(lines) + "\n\n---\n\n"


def csv_text(header_row: list[str], rows: list[tuple] | None = None) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header_row)
    for row in rows or []:
        w.writerow(row)
    return buf.getvalue()


def document_template() -> str:
    body = "".join(
        f"## {i}. {name}\n\n_TBD_\n\n" for i, name in enumerate(DOC_SECTIONS, 1))
    return (
        "<!-- HFP-X controlled document template (prompt section 26). -->\n"
        "<!-- Status labels: CONCEPT, PROPOSED, ASSUMED, UNDER ANALYSIS, "
        "DESIGNED, PROTOTYPE, TESTED, VERIFIED, VALIDATED, CERTIFIED, "
        "RETIRED. -->\n<!-- Unknown data: TBD / TBC / ASSUMPTION A-XXX. "
        "Never invent values. -->\n\n"
        + header("[DOCUMENT TITLE]", "HFPX-[DOMAIN]-[TYPE]-[NNN]", "[YYYY-MM-DD]")
        + body
    )


def volume_readme(v: Volume, today: str) -> str:
    doc_id = f"HFPX-{v.domain}-IDX-001"
    out = header(f"Volume {v.number:02d} - {v.title}", doc_id, today)
    out += (f"**Domain code:** `{v.domain}`  \n"
            f"**Folder:** `{v.folder}/`\n\n")
    out += VOLUME_NOTES.get(v.number, "") + "\n" if v.number in VOLUME_NOTES else ""
    out += "## Chapter index\n\n| Chapter | Title | Document ID | Status |\n"
    out += "| --- | --- | --- | --- |\n"
    for num, title in v.chapters:
        out += f"| {num} | {title} | TBD | CONCEPT |\n"
    out += ("\nDocument IDs are allocated when a chapter document is created "
            "(`HFPX-" + v.domain + "-<TYPE>-<NNN>`).\n")
    return out


def baseline_doc(today: str) -> str:
    out = header("HFP-X Master Technical Baseline", "HFPX-PGM-BSL-001", today)
    out += (
        "## Baseline BL-0.0 - structure only\n\n"
        "This baseline records the documentation structure and programme "
        "policies only. **No technical requirement, architecture, "
        "allocation or performance value is approved.**\n\n"
        "| Element | Current state | Status |\n| --- | --- | --- |\n"
        "| Requirements | None baselined (see ISS-002) | CONCEPT |\n"
        "| Architecture | None baselined | CONCEPT |\n"
        "| Component allocation | None | CONCEPT |\n"
        "| Interfaces | None | CONCEPT |\n"
        "| Assumptions | Register empty | CONCEPT |\n"
        "| Risks | Risk register not yet created (Vol 00.12) | CONCEPT |\n"
        "| Test status | No tests performed | CONCEPT |\n"
        "| Configuration | BL-0.0 | CONCEPT |\n"
        "| Open issues | ISS-001 to ISS-008 | OPEN |\n\n"
        "## Adopted decisions\n\n"
        "- DDR-001: Unmanned-first development progression\n"
        "- DDR-002: 34-volume documentation structure\n"
        "- DDR-003: Controlled identifier scheme\n\n"
        "## Review gates\n\n"
        "| Gate | Status |\n| --- | --- |\n"
        + "".join(f"| {g} | NOT STARTED |\n" for g in
                  ["SRR", "PDR", "CDR", "TRR", "FCA", "PCA", "FRR", "PRR",
                   "ORR"])
        + "\nEntrance/exit criteria for each gate are to be defined in "
        "Volume 00.14 (TBD).\n\n"
        "## Change history\n\n| Rev | Date | Change |\n| --- | --- | --- |\n"
        f"| A | {today} | Initial structure baseline BL-0.0 |\n"
    )
    return out


def ddr_doc(d: dict, today: str) -> str:
    out = header(f"Design Decision Record - {d['title']}",
                 f"HFPX-PGM-DDR-{d['id'][-3:]}", today, status="PROPOSED")
    fields = [("Decision ID", d["id"]), ("Decision", d["title"]),
              ("Context", d["context"]), ("Options Considered", d["options"]),
              ("Evaluation Criteria", d["criteria"]), ("Evidence", d["evidence"]),
              ("Trade Study", d["trade"]), ("Selected Architecture", d["selected"]),
              ("Rationale", d["rationale"]), ("Consequences", d["consequences"]),
              ("Risks", d["risks"]), ("Revisit Conditions", d["revisit"])]
    for name, value in fields:
        out += f"## {name}\n\n{value}\n\n"
    out += ("_Records are never rewritten. A later contradicting decision "
            "creates a new DDR (prompt section 21)._\n")
    return out


def top_readme(volumes: dict[int, Volume], today: str) -> str:
    out = header("BOLTE HFP-X - Programme Documentation Tree",
                 "HFPX-PGM-IDX-000", today)
    out += ("Human Flight Platform - production engineering documentation "
            "suite. Chain: MISSION -> REQUIREMENTS -> ARCHITECTURE -> DESIGN "
            "-> IMPLEMENTATION -> INTEGRATION -> VERIFICATION -> VALIDATION "
            "-> CERTIFICATION -> PRODUCTION -> OPERATIONS -> SUSTAINMENT.\n\n"
            "Nothing in this tree is claimed compliant with any standard. "
            "Documents are *structured according to* frameworks until "
            "*verified compliant* evidence exists.\n\n"
            "## Five backbone documents\n\n"
            "| Document ID | Title | Volume | Status |\n| --- | --- | --- | --- |\n")
    for doc_id, title, vol in MASTER_DOCS:
        out += f"| {doc_id} | {title} | {vol} | CONCEPT (not written) |\n"
    out += "\n## Volumes\n\n| Vol | Domain | Folder | Chapters |\n| --- | --- | --- | --- |\n"
    for n in sorted(volumes):
        v = volumes[n]
        out += f"| {n:02d} | {v.domain} | `{v.folder}/` | {len(v.chapters)} |\n"
    out += ("\n## Controlled registers\n\nLocated in "
            f"`{volumes[0].folder}/registers/` (hazard log in "
            f"`{volumes[13].folder}/`). CSV, UTF-8. Validate with "
            "`hfpx_scaffold.py check`.\n")
    return out


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------

def build(schema_path: Path, out: Path, today: str, force: bool) -> None:
    volumes = parse_schema(schema_path.read_text(encoding="utf-8"))
    created: list[Path] = []
    skipped: list[Path] = []

    def write(path: Path, text: str) -> None:
        if path.exists() and not force:
            skipped.append(path)
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        created.append(path)

    write(out / "README.md", top_readme(volumes, today))
    write(out / "_templates" / "DOCUMENT_TEMPLATE.md", document_template())

    for v in volumes.values():
        write(out / v.folder / "README.md", volume_readme(v, today))

    reg_dir = out / volumes[0].folder / "registers"
    decision_rows = [(d["id"], d["title"], "PROPOSED", today,
                      f"decisions/{d['id']}.md") for d in SEED_DDRS]
    seeds = {"issue_register.csv": SEED_ISSUES,
             "decision_log.csv": decision_rows}
    for name, (cols, _key) in REGISTERS.items():
        write(reg_dir / name, csv_text(cols, seeds.get(name)))
    write(reg_dir / "decisions" / "README.md",
          "# Design Decision Records\n\nOne file per decision. Never "
          "rewritten; supersede with a new DDR.\n")
    for d in SEED_DDRS:
        write(reg_dir / "decisions" / f"{d['id']}.md", ddr_doc(d, today))

    name, cols, _key = HAZARD_LOG
    write(out / volumes[13].folder / name, csv_text(cols))
    write(out / volumes[0].folder / "HFPX-PGM-BSL-001_Master_Technical_Baseline.md",
          baseline_doc(today))

    print(f"Created {len(created)} files, skipped {len(skipped)} existing "
          f"(use --force to overwrite).")


# --------------------------------------------------------------------------
# Check
# --------------------------------------------------------------------------

def check(schema_path: Path, out: Path) -> int:
    """Validate the tree against the schema and the ID conventions."""
    errors: list[str] = []
    volumes = parse_schema(schema_path.read_text(encoding="utf-8"))

    if len(set(DOMAIN_CODES.values())) != len(DOMAIN_CODES):
        errors.append("DOMAIN_CODES contains duplicates")

    for v in volumes.values():
        readme = out / v.folder / "README.md"
        if not readme.exists():
            errors.append(f"Missing {readme}")
            continue
        rows = re.findall(r"^\| \d{2}\.\d+ \|", readme.read_text(encoding="utf-8"),
                          re.M)
        if len(rows) != len(v.chapters):
            errors.append(f"{readme}: {len(rows)} chapter rows, schema has "
                          f"{len(v.chapters)}")

    reg_dir = out / volumes[0].folder / "registers"
    all_registers = dict(REGISTERS)
    all_registers[HAZARD_LOG[0]] = (HAZARD_LOG[1], HAZARD_LOG[2])
    for name, (cols, key) in all_registers.items():
        path = (out / volumes[13].folder / name if name == HAZARD_LOG[0]
                else reg_dir / name)
        if not path.exists():
            errors.append(f"Missing register {path}")
            continue
        with path.open(encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh)
            head = next(reader, [])
            if head != cols:
                errors.append(f"{path}: header mismatch")
            seen: set[str] = set()
            for i, row in enumerate(reader, 2):
                if not row:
                    continue
                if not ID_PATTERNS[key].match(row[0]):
                    errors.append(f"{path}:{i}: bad ID '{row[0]}'")
                if row[0] in seen:
                    errors.append(f"{path}:{i}: duplicate ID '{row[0]}'")
                seen.add(row[0])

    for doc_id, _t, _v in MASTER_DOCS:
        if not ID_PATTERNS["doc"].match(doc_id):
            errors.append(f"Backbone doc ID invalid: {doc_id}")

    if errors:
        print("CHECK FAILED:")
        for e in errors:
            print("  -", e)
        return 1
    print(f"CHECK PASSED: {len(volumes)} volumes, "
          f"{sum(len(v.chapters) for v in volumes.values())} chapters, "
          f"{len(all_registers)} registers.")
    return 0


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    p.add_argument("command", choices=["build", "check"])
    p.add_argument("--schema", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    p.add_argument("--date", default=date.today().isoformat())
    p.add_argument("--force", action="store_true")
    a = p.parse_args()
    if a.command == "build":
        build(a.schema, a.out, a.date, a.force)
        return 0
    return check(a.schema, a.out)


if __name__ == "__main__":
    sys.exit(main())
