#!/usr/bin/env python3
"""BOLTE website generator (v4.2). Writes the static pages into a website/ folder.
Usage: python3 build-scripts/generate-pages.py website [site_url]
Edit copy and structure here, then regenerate. Styles live in assets/css/site.css."""
import math, sys, pathlib

OUT = pathlib.Path(sys.argv[1])
EMAIL = "bolte.tech0@gmail.com"
import os
# Absolute site URL (used for the social-share image). Override per host:
#   python3 generate-pages.py website https://your-site.netlify.app/
SITE = (sys.argv[2] if len(sys.argv) > 2 and sys.argv[2].strip("/") else "https://garba-the-analyst.github.io/BOLTE/").rstrip("/") + "/"

# ------------------------------------------------------------------ team data
# Members who chose initials-only display (roster Q9) are shown as initials until they re-consent.
TEAM_FOUNDERS = [
    ("Abdullahi Garba", "Co-founder, CEO and CTO", "Leads engineering direction, R&amp;D programmes and product architecture.", "p1-garba.jpg"),
    ("Essien Frances", "Co-founder, COO and Research Lead", "Leads operations, partnerships, compliance and the research programme.", "p2-frances.jpg"),
]
TEAM_CORE = [
    ("David Uzondu", "Lead Engineer", "Hardware, embedded and RF systems, and engineering standards.", "c-david.jpg"),
    ("Abdulazeez Masud", "Assistant to the Lead Engineer", "Hardware, CAD, electronics and systems support.", "d-abdulazeez.jpg"),
    ("Essien Timiobong Dunnhill", "Treasurer and Research Assistant", "Financial records, reporting and research support.", "b1-timi.jpg"),
    ("Yusuf Azeemah Oyiza", "Product Designer and Manager", "Delivery planning, quality assurance and design.", "b2-azeemah.jpg"),
]

def rv(i=0):
    return f'class="rv" style="--i:{i}"'

# ------------------------------------------------------------------ hero system map
def sysmap():
    W, H, cx, cy = 860, 700, 430, 350
    inner = [("Systems engineering", -90), ("Aerospace", -30), ("Cybersecurity", 30),
             ("Robotics and autonomy", 90), ("Computing and AI", 150), ("Telecom and RF", 210)]
    outer = [("Agriculture", -60), ("Healthcare", 0), ("Energy", 60),
             ("Transportation", 120), ("Education tech", 180), ("Financial tech", 240)]
    R, RX, RY = 180, 335, 300
    def cw(t): return round(len(t) * 10.6 + 32)
    s = []
    s.append(f'<svg class="sm-svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="sm-t sm-d" xmlns="http://www.w3.org/2000/svg">')
    s.append('<title id="sm-t">BOLTE capability map</title>')
    s.append('<desc id="sm-d">Defence and security sits at the centre. Around it are six engineering disciplines: systems engineering, aerospace, cybersecurity, robotics and autonomy, computing and AI, and telecommunications and RF. An outer dashed ring shows sectors on the roadmap: agriculture, healthcare, energy, transportation, education technology and financial technology.</desc>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#68b0ff" stroke-opacity=".3"/>')
    s.append(f'<ellipse class="sm-ring" cx="{cx}" cy="{cy}" rx="{RX}" ry="{RY}" fill="none" stroke="#a9bdd8" stroke-opacity=".5" stroke-dasharray="3 7" style="--d:1.5s"/>')
    pos = []
    for i, (t, a) in enumerate(inner):
        r = math.radians(a)
        x, y = cx + R * math.cos(r), cy + R * math.sin(r)
        pos.append((t, x, y, i))
        s.append(f'<line class="sm-spoke" pathLength="1" x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#2E86DE" stroke-width="1.4" style="--d:{.5+.12*i:.2f}s"/>')
    for t, x, y, i in pos:
        s.append(f'<circle class="sm-dot" r="3.2" fill="#9fd0ff"><animateMotion dur="{3.6+.4*(i%3):.1f}s" begin="{3+.5*i:.1f}s" repeatCount="indefinite" path="M{cx} {cy} L{x:.1f} {y:.1f}"/></circle>')
    s.append(f'<g class="sm-core"><circle class="sm-pulse" cx="{cx}" cy="{cy}" r="74" fill="none" stroke="#2E86DE" stroke-width="2"/>'
             f'<circle cx="{cx}" cy="{cy}" r="74" fill="#2E86DE"/>'
             f'<text class="sm-core-t" x="{cx}" y="{cy-4}" text-anchor="middle">Defence</text>'
             f'<text class="sm-core-t" x="{cx}" y="{cy+17}" text-anchor="middle">and security</text></g>')
    for t, x, y, i in pos:
        w = cw(t)
        s.append(f'<g class="sm-node" style="--d:{.8+.12*i:.2f}s"><rect x="{x-w/2:.1f}" y="{y-21:.1f}" width="{w}" height="42" rx="3" fill="#16335a" stroke="#68b0ff" stroke-width="1.6"/>'
                 f'<text class="sm-t" x="{x:.1f}" y="{y+6.5:.1f}" text-anchor="middle">{t}</text></g>')
    for i, (t, a) in enumerate(outer):
        r = math.radians(a)
        x, y = cx + RX * math.cos(r), cy + RY * math.sin(r)
        w = cw(t)
        s.append(f'<g class="sm-node" style="--d:{1.9+.1*i:.2f}s"><rect x="{x-w/2:.1f}" y="{y-21:.1f}" width="{w}" height="42" rx="3" fill="#12233f" stroke="#a9bdd8" stroke-width="1.4" stroke-dasharray="4 4"/>'
                 f'<text class="sm-t2" x="{x:.1f}" y="{y+6.5:.1f}" text-anchor="middle">{t}</text></g>')
    s.append('</svg>')
    return "\n".join(s)

def maplist():
    return '''<div class="sm-list">
<p class="sm-core-l">Defence and security</p>
<p class="sm-l-h">Engineering disciplines</p>
<ul><li style="--i:0">Systems engineering</li><li style="--i:1">Aerospace</li><li style="--i:2">Cybersecurity</li><li style="--i:3">Robotics and autonomy</li><li style="--i:4">Computing and AI</li><li style="--i:5">Telecom and RF</li></ul>
<p class="sm-l-h">Sectors on the roadmap</p>
<ul class="dashed"><li style="--i:6">Agriculture</li><li style="--i:7">Healthcare</li><li style="--i:8">Energy</li><li style="--i:9">Transportation</li><li style="--i:10">Education tech</li><li style="--i:11">Financial tech</li></ul>
</div>'''

# ------------------------------------------------------------------ shared chrome
NAV = [("technology.html", "Technology"), ("company.html", "Company"), ("team.html", "Team"), ("contact.html", "Contact")]

def head(title, desc, page):
    cur = ' aria-current="page"'
    links = "\n".join(f'<a href="{h}"{cur if h == page else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0A1428">
<meta property="og:type" content="website">
<meta property="og:site_name" content="BOLTE">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<script>document.documentElement.className+=' js';</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap nav">
<a class="nav-logo" href="index.html" aria-label="BOLTE home"><img src="assets/img/bolte-lockup.png" alt="BOLTE" width="105" height="30"></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
<nav class="nav-links" id="nav-links" aria-label="Main">
{links}
<a class="btn btn-primary btn-nav" href="mailto:{EMAIL}?subject=Partnership%20enquiry">Partner with us</a>
</nav>
</div>
</header>
<main id="main">
'''

FOOT = f'''</main>
<footer class="site-footer">
<div class="wrap">
<div class="foot">
<div>
<img src="assets/img/bolte-lockup.png" alt="BOLTE" width="98" height="28">
<p>Nigerian research and engineering company building indigenous defence and security technology.</p>
<p>BOLTE is being incorporated in Nigeria.</p>
</div>
<div>
<h4>Explore</h4>
<ul>
<li><a href="technology.html">Technology</a></li>
<li><a href="company.html">Company</a></li>
<li><a href="team.html">Team</a></li>
<li><a href="contact.html">Contact</a></li>
</ul>
</div>
<div>
<h4>Get in touch</h4>
<ul>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><a href="legal.html">Privacy and notices</a></li>
</ul>
</div>
</div>
<div class="foot-base"><span>&copy; <span data-year>2026</span> BOLTE. All rights reserved.</span><span>Nigeria</span></div>
</div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>
'''

def cta(h, p, label, subject):
    return f'''<section class="cta">
<div class="wrap cta-inner">
<div><h2>{h}</h2><p>{p}</p></div>
<a class="btn btn-light" href="mailto:{EMAIL}?subject={subject}">{label}</a>
</div>
</section>
'''

def page_head(h1, lede):
    return f'''<section class="band-navy grid-bg page-head">
<div class="wrap">
<h1>{h1}</h1>
<p class="lede">{lede}</p>
</div>
</section>
'''

def area(title, tag, blurb, items, primary=False, i=0):
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'''<div {rv(i)}>
<div class="area{" primary" if primary else ""}">
<div><h3>{title}</h3><p class="tag">{tag}</p><p class="small">{blurb}</p></div>
<ul class="items">{lis}</ul>
</div>
</div>
'''

def model():
    steps = [("Problem", "Start with a Nigerian need"), ("Idea", "Frame a solution"), ("Research", "Study what is known"),
             ("Engineering", "Design it properly"), ("Prototype", "Build a working version"), ("Testing", "Break it on purpose"),
             ("Improvement", "Fix it, then retest"), ("Deployment", "Put it in real hands"), ("Impact", "Measure what changed")]
    li = "".join(f'<li style="--i:{i}"><b>{a}</b><span>{b}</span></li>' for i, (a, b) in enumerate(steps))
    return f'<ol class="model rv">{li}</ol>'

STEPS = ["Problem", "Idea", "Research", "Engineering", "Prototype", "Testing", "Improvement", "Deployment", "Impact"]

def tracker(done):
    out = []
    for i, n in enumerate(STEPS):
        c = "done" if i < done else ("cur" if i == done else "")
        out.append(f'<li class="{c}"><i></i>{n}</li>')
    return '<ol class="trk" aria-label="Progress through the BOLTE model">' + "".join(out) + '</ol>'

PROGS = [
 dict(id="aeropulse-ng", name="AeroPulse-NG", full="Tactical Radar and Airspace Surveillance Engine", flagship=True,
  dom="Aerospace, defence, computing", mat="Software prototype built", done=5,
  one="Offline airspace surveillance on low-cost radio hardware.",
  body=[("The need", "Secondary aerodromes and tactical sites often lack affordable low-altitude surveillance. Imported systems are costly, depend on connectivity and power, and are hard to maintain locally."),
        ("The approach", "An offline surveillance workstation that runs on low-cost software-defined radio and a standard PC. It receives aircraft transponder and ACARS messages, tracks aircraft, and raises conflict, emergency and geofence alerts. It is advisory: an operator decides."),
        ("Current status", "The software prototype is built and runs on simulated radio signals. We are waiting on the hardware components for real-time testing with live signals.")],
  rm=[("Now", "Obtain the radio hardware for real-time testing with live signals."),
      ("Next", "Live-signal testing, then a field trial at a secondary aerodrome or tactical site."),
      ("Then", "Publish the trial report and prove a second use case."),
      ("Later", "First pilot and deployment to secondary aerodromes and tactical users.")],
  img=("aeropulse-scope.jpg", "Tactical picture screen from the AeroPulse-NG software prototype: a radar display with aircraft tracks, alerts and a live source panel.", "The AeroPulse-NG tactical picture, from the software prototype running on simulated signals.", 1200, 771)),
 dict(id="asol", name="ASOL", full="Armory Shift and Ordnance Log",
  dom="Defence logistics", mat="Designed on paper", done=4,
  one="Armoury custody and ordnance logging without paper ledgers.",
  body=[("The need", "Armoury custody still runs on paper ledgers. Check-in and check-out are slow to audit, single-custodian handovers leave accountability gaps, and unfit personnel can draw equipment unchecked."),
        ("The approach", "An offline armoury desk with barcode and RFID check-in and out, enforced dual-custodian shift handovers, a fitness-for-duty check before release, and an encrypted local database."),
        ("Current status", "The system is designed and planned on paper: architecture, data model and interfaces are written. The working prototype is the next step.")],
  rm=[("Now", "Walk through the real armoury workflow with domain advisers and map today's paper forms to the design."),
      ("Next", "Build a working prototype with simulated scanners, after the first prototype's trial report and a resource review."),
      ("Then", "Field pilot with real barcode and RFID hardware at an armoury, audited by an independent count."),
      ("Later", "Harden, add multi-desk support, and ship a deployable kit with training material.")]),
 dict(id="dafv", name="DAFV", full="Defense Asset and Firmware Verifier",
  dom="Cybersecurity, industrial", mat="Designed on paper", done=4,
  one="Proof that hardware and firmware are what they claim to be.",
  body=[("The need", "Depots receive hardware and firmware with no local way to prove where it came from. Tampered or swapped binaries can be deployed without anyone noticing."),
        ("The approach", "An offline audit station at the receiving dock. It reads a device image, checks it against a signed manifest, and binds the result to the asset. A person accepts or rejects it; it never flashes anything automatically."),
        ("Current status", "Designed on paper: architecture, data model and interfaces are written. The lab prototype is the next step.")],
  rm=[("Now", "Review the design with domain advisers and line up parts for a lab setup."),
      ("Next", "Lab prototype that checks device images against signed manifests, after the first prototype's trial report and a resource review."),
      ("Then", "Connect to real device interfaces and asset tags."),
      ("Later", "Pilot at a depot receiving dock.")]),
 dict(id="c4isr-dfe", name="C4ISR-DFE", full="Tactical C4ISR Data Fusion Engine",
  dom="Communications, computing and AI", mat="Designed on paper", done=4,
  one="One offline picture for dispersed units on weak links.",
  body=[("The need", "Vehicles and bunkers lack a single offline picture. Aircraft, drone, radio-bearing and GPS tracks arrive in separate tools and are lost when links degrade."),
        ("The approach", "A command dashboard that merges those tracks onto an offline map and shares compact updates between units over lossy links, with store-and-forward so nothing is dropped."),
        ("Current status", "Designed on paper: architecture, data model and interfaces are written, reusing lessons from the AeroPulse-NG prototype. The lab prototype is the next step.")],
  rm=[("Now", "Review the design with domain advisers and prepare simulated sensor feeds."),
      ("Next", "Lab fusion of several sensor feeds into one known picture, after the first prototype's trial report and a resource review."),
      ("Then", "Two-station mesh that stays in sync through link loss."),
      ("Later", "Pilot in a vehicle or bunker.")]),
 dict(id="tbr-hs", name="TBR-HS", full="Tactical Biometric Radar and Health System",
  dom="Defence, search and rescue, sensing", mat="Designed, beyond concept", done=4,
  one="A microwave motion sensor that tracks people on a minimap, for frontline and search-and-rescue use.",
  body=[("The need", "At the frontline, a squad cannot see who is moving behind a wall or around a corner. In search and rescue, finding people trapped behind obstacles costs critical time."),
        ("The approach", "A motion sensor that uses microwave signals, which the human body absorbs, to detect movement of nearby people, including through barriers. It plots them on a screen like a minimap in a video game, with signed identity tokens to tell friendly from unknown. Tracking personnel health with wearable vitals is an added feature."),
        ("Current status", "Designed, beyond concept: the architecture, signal-processing chain, data model and interfaces are written. Bench simulation is the next step.")],
  rm=[("Now", "Define the safety and ethics review, and list the parts for a test rig using physical phantoms."),
      ("Next", "Bench simulation of the signal chain through to the minimap display, with no people involved."),
      ("Then", "Lab sensor bring-up on phantoms and obstacles."),
      ("Later", "Controlled pilot, only after safety and ethics review and both founders' sign-off.")]),
 dict(id="hfp-x", name="HFP-X", full="Human Flight Platform",
  dom="Aerospace, transportation", mat="Designed, beyond documentation", done=4,
  one="A body-worn, jet-powered vertical-lift flight platform for a pilot.",
  body=[("The aim", "A Nigerian-engineered platform that takes off vertically, hovers, transitions to forward flight, cruises and lands, with independent recovery for defined failures."),
        ("The approach", "Distributed jet modules, fly-by-wire control, a smart helmet display and emergency recovery, developed through a 34-volume documentation set and a drawing set. An unmanned demonstrator comes first. Human flight comes only after unmanned hover, transition and cruise pass evidence gates."),
        ("Current status", "The schematics and architecture are designed. Performance values are still to be confirmed, and no hardware is built or flown.")],
  rm=[("Now", "Close out the requirements and architecture review, and confirm the design values."),
      ("Next", "Simulation and ground rigs for the subsystems, then the unmanned demonstrator."),
      ("Then", "Unmanned hover, transition and cruise, passing each evidence gate in turn."),
      ("Later", "Controlled human flight, only after every gate is passed.")],
  img=("hfpx-flight-configurations.jpg", "HFP-X drawing showing the platform in hover, transition and horizontal flight, with thrust, weight and lift vectors.", "HFP-X flight configurations: hover, transition and horizontal flight. A design drawing; dimensions are still to be confirmed.", 1500, 938)),
]
FULL = {p["id"]: p["full"] for p in PROGS}

def figure(p):
    if "img" not in p: return ""
    f, alt, cap, w, h = p["img"]
    return f'<figure class="pfig"><img src="assets/img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"><figcaption>{cap}</figcaption></figure>'

def roadmap(p):
    li = "".join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in p["rm"])
    return f'<ol class="rmap">{li}</ol>'

pages = {}

# ------------------------------------------------------------------ index
def card(i, p):
    fl = p.get("flagship")
    badge = '<span class="flag">Flagship</span>' if fl else ""
    pic = ""
    if fl and "img" in p:
        f, alt, cap, w, h = p["img"]
        pic = f'<img class="pg-img" src="assets/img/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy">'
    pct = round(100 * (p["done"] + .5) / 9)
    return f'''<article class="pg rv{" pg-wide" if fl else ""}" style="--i:{i}">
<div class="pg-txt">
<p class="pg-m">{p["mat"]}{badge}</p>
<h3><a href="technology.html#{p["id"]}">{p["name"]}</a></h3>
<p class="pg-f">{p["full"]}</p>
<p class="pg-d">{p["dom"]}</p>
<p>{p["one"]}</p>
<div class="bar" role="img" aria-label="{p["done"]} of 9 BOLTE model steps complete"><i style="width:{pct}%"></i></div>
</div>{pic}
</article>
'''
cards = "".join(card(i, p) for i, p in enumerate(PROGS))

pages["index.html"] = head(
    "BOLTE: Indigenous defence technology, engineered in Nigeria",
    "BOLTE is a Nigerian research and engineering company building defence and security technology, with work across aerospace, communications, cybersecurity and systems engineering.",
    "index.html") + f'''<section class="band-navy grid-bg hero">
<div class="wrap hero-grid">
<div>
<h1>Defence technology, engineered in Nigeria.</h1>
<p class="lede">BOLTE researches, engineers and deploys indigenous technology. We begin with defence and security, and build across aerospace, communications, cybersecurity and systems engineering.</p>
<div class="hero-actions">
<a class="btn btn-primary" href="technology.html">Explore our work</a>
<a class="btn btn-line" href="contact.html">Partner with us</a>
</div>
<p class="hero-status">Pre-seed company, incorporation in progress. Our first software prototype is built and awaiting hardware for live testing.</p>
</div>
<figure class="sysmap">
{sysmap()}
{maplist()}
<figcaption>Solid outlines are the engineering disciplines we build on. Dashed outlines are sectors we will enter as the company grows.</figcaption>
</figure>
</div>
</section>

<section class="band band-pale" id="focus">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Defence first, built on the disciplines it depends on.</h2>
<p class="lede">Our rule is simple. If technology can solve an important problem for Nigeria, BOLTE should be able to explore it. We start where the need is greatest.</p>
</div>
{area("Defence and security", "Primary focus", "Legitimate, lawful and locally maintainable technology for authorised users.",
      ["Surveillance and reconnaissance", "Secure communications", "Robotics and autonomous systems", "Military logistics", "Protective technologies", "Intelligence-support systems", "Cybersecurity and technological resilience", "Aerospace and related technologies"], True, 0)}
{area("Engineering disciplines", "What we build with", "One multidisciplinary team, so a system is designed as a whole.",
      ["Aerospace", "Telecommunications and RF", "Cybersecurity", "Systems engineering", "Robotics and automation", "Computing and AI"], False, 1)}
{area("Sectors on the roadmap", "Beyond defence", "The same engineering applied to other national problems as the company grows.",
      ["Agriculture", "Healthcare", "Education technology", "Financial technology", "Energy", "Transportation", "Environmental technology", "Industrial technology"], False, 2)}
</div>
</section>

<section class="band band-deep" id="mission">
<div class="wrap">
<p class="statement rv">A technologically independent Nigeria and, ultimately, a technologically independent Africa.</p>
<div class="cols2 mm">
<div class="rv" style="--i:1">
<h3>Our mission</h3>
<p class="lede">To research, engineer, develop and deploy indigenous technologies that strengthen Nigeria's technological foundation, with defence and security as our primary focus.</p>
</div>
<div class="rv" style="--i:2">
<h3>Our philosophy</h3>
<p class="lede">All problems are solved when you put things together. Ideas, people, knowledge, resources and technology make progress only when they are combined.</p>
</div>
</div>
</div>
</section>

<section class="band band-white" id="method">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">The BOLTE model: from a Nigerian need to real impact.</h2>
<p class="lede">Every programme follows the same path. We widen the loop over time, from Nigerian solutions to African capability, and on to African technological independence.</p>
</div>
{model()}
</div>
</section>

<section class="band band-pale" id="programmes">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Six programmes across our areas of work.</h2>
<p class="lede">Each one states its real maturity. We build a programme only when the one before it has earned the next step.</p>
</div>
<div class="progs">
{cards}</div>
<p style="margin-top:36px"><a class="link" href="technology.html">See all programmes in detail</a></p>
</div>
</section>

<section class="band band-white" id="principles">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Built to be trusted by the people who deploy it.</h2>
</div>
<div class="cols3">
<div class="rv"><h3>Lawful users only</h3><p>We build for authorised, lawful users and comply with Nigerian law and export controls. Both founders approve every security partnership.</p></div>
<div class="rv" style="--i:1"><h3>People make the decisions</h3><p>Our systems inform operators. A human decision-maker stays in the loop for every operational judgement.</p></div>
<div class="rv" style="--i:2"><h3>Evidence before claims</h3><p>We state each programme's real maturity and test before we deploy. If it has not been proven, we do not say it has.</p></div>
</div>
</div>
</section>
''' + cta("Working on Nigerian defence or security technology?",
          "We are open to pilots, evaluations, research collaboration and institutional partnerships.",
          "Partner with us", "Partnership%20enquiry") + FOOT

# ------------------------------------------------------------------ technology
details = ""
for p in PROGS:
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in p["body"])
    badge = '<span class="flag">Flagship</span>' if p.get("flagship") else ""
    op = " open" if p.get("flagship") else ""
    details += f'''<details class="pd" id="{p["id"]}"{op}>
<summary>
<span class="pn">{p["name"]}{badge}<small>{p["full"]}</small></span>
<span class="ps">{p["one"]}</span>
<span class="pm">{p["mat"]}</span>
<span class="pdm">{p["dom"]}</span>
</summary>
<dl class="pdl">{dl}</dl>
<div class="pst">
<div><h4>Progress through the BOLTE model</h4>{tracker(p["done"])}</div>
{figure(p)}
<div><h4>Roadmap</h4>{roadmap(p)}</div>
</div>
</details>
'''

rules = [("Nigerian fit", "Designed around power, connectivity, climate and the engineers who will maintain it."),
         ("Honest maturity", "Each programme states its technology readiness level. A concept is labelled a concept."),
         ("Standards named, not claimed", "We design against recognised standards and never claim a certification we do not hold."),
         ("Safety before deployment", "Testing and documentation come first. Anything involving people goes through safety and ethics review."),
         ("Cost and maintainability", "Commodity hardware, permissive licences, and software that Nigerian engineers can support."),
         ("Gated growth", "Concepts stay on paper until the first prototype has its trial report and we have reviewed our resources.")]
rules_html = "".join(f'<li class="rv" style="--i:{i%2}"><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(rules))

pages["technology.html"] = head(
    "Technology | BOLTE",
    "BOLTE's six programmes across aerospace, communications, cybersecurity, defence logistics and sensing, each with its real maturity stated.",
    "technology.html") + page_head(
    "Six programmes, one engineering discipline.",
    "From a working software prototype to long-horizon research, each programme states what it addresses, where it stands and where it goes next.") + f'''
<section class="band band-pale">
<div class="wrap">
<div class="pd-head" aria-hidden="true"><span>Programme</span><span>What it does</span><span>Maturity</span><span>Domain</span></div>
<div class="pds">
{details}</div>
<p class="small" style="margin-top:22px">Select a programme to see its progress through the BOLTE model and its roadmap.</p>
</div>
</section>

<section class="band band-white">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Rules every programme follows.</h2>
</div>
<ul class="principles">{rules_html}</ul>
</div>
</section>

<section class="band band-navy grid-bg">
<div class="wrap">
<div class="sec-head"><h2 class="h2 wide">Where we are going.</h2></div>
<div class="path">
<div class="now rv"><h3>Prove</h3><div class="when">Now</div><p>Demonstrate our first software prototype, secure the hardware for live testing, and put governance in place.</p></div>
<div class="rv" style="--i:1"><h3>Validate</h3><div class="when">Next</div><p>Live-signal testing and a field trial, a published trial report and a second use case.</p></div>
<div class="rv" style="--i:2"><h3>Build capability</h3><div class="when">Following</div><p>Prototyping facility, manufacturing partner, incorporation, IP filings and a first pilot.</p></div>
<div class="rv" style="--i:3"><h3>Scale</h3><div class="when">Longer term</div><p>National deployment and partnerships with universities, industry and government.</p></div>
</div>
</div>
</section>
''' + cta("Want to evaluate or support a programme?",
          "We welcome pilot sites, technical reviewers and research partners.",
          "Start a conversation", "Programme%20enquiry") + FOOT

# ------------------------------------------------------------------ company
goals = [("Indigenous defence and security technology", "Build Nigeria's capacity to research, design, develop and sustain it. This is our primary goal."),
         ("Strengthen the technology backbone", "Engineering capability, research infrastructure, prototyping, manufacturing and software, so Nigeria moves from consuming technology to creating it."),
         ("Turn ideas into inventions", "Find important problems, research, prototype, test and improve until there is a viable product or system."),
         ("Develop Nigerian technological talent", "A community of scientists, engineers, programmers, researchers, designers and inventors, with room to learn, build and commercialise."),
         ("Advance technology across strategic sectors", "Defence, agriculture, energy, healthcare, transportation, robotics, communications, computing and AI, aerospace, environmental and industrial technology."),
         ("Build a research and innovation ecosystem", "Connect universities, researchers, engineers, industry, government and investors, so ideas do not die in labs and notebooks."),
         ("Build technologies for Nigeria, not only import them", "Design around Nigerian environment, resources, infrastructure, economics and security, rather than copying foreign systems.")]
goals_html = "".join(f'<li class="rv" style="--i:{i%3}"><span class="gn">{i+1}</span><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(goals))

values = [("Sovereignty by capability", "We build, not only buy. Independence comes from being able to design and sustain what a country depends on."),
          ("Multidisciplinary building", "Aerospace, radio, software and security progress faster when one team builds them as one system."),
          ("Honest engineering", "We admit limits, risks and maturity, and we publish what we can prove."),
          ("Local maintainability", "Everything is designed so that Nigerian engineers can support it, with local parts and local knowledge."),
          ("Talent multiplication", "We train and mentor young engineers and researchers, so every programme grows the people who can build the next one.")]
values_html = "".join(f'<li class="rv" style="--i:{i%2}"><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(values))

ethics = [("Lawful and legitimate users only", "We comply with Nigerian law and export controls."),
          ("A defensive posture", "Defence and situational awareness. No technology that enables indiscriminate harm."),
          ("A human in the loop", "Operational judgements stay with a person. Our alerts are advisory."),
          ("Safety first", "Testing discipline and documentation come before any deployment."),
          ("Two signatures for partnerships", "Any partnership with a security institution needs written approval from both co-founders.")]
ethics_html = "".join(f'<li class="rv" style="--i:{i%2}"><h3>{a}</h3><p>{b}</p></li>' for i, (a, b) in enumerate(ethics))

pages["company.html"] = head(
    "Company | BOLTE",
    "BOLTE's vision, mission, goals, philosophy and ethics.",
    "company.html") + page_head(
    "A Nigerian engineering company with a long view.",
    "BOLTE is a research, engineering and technology company focused on indigenous defence and security technology, and on building the capability that technological independence depends on.") + f'''
<section class="band band-pale">
<div class="wrap">
<div class="cols3 vma">
<div class="rv"><h3>Vision</h3><p class="lede">A technologically independent Nigeria and, ultimately, a technologically independent Africa. A country able to research, develop, manufacture and sustain the technologies essential to its security, prosperity and development.</p></div>
<div class="rv" style="--i:1"><h3>Mission</h3><p class="lede">To research, engineer, develop and deploy indigenous technologies that strengthen Nigeria's technological foundation, with defence and security as our primary focus, and to develop solutions across other strategic sectors.</p></div>
<div class="rv" style="--i:2"><h3>Aim</h3><p class="lede">To strengthen Nigeria's technological self-reliance through indigenous research, engineering, invention and development, creating the foundation for African technological independence.</p></div>
</div>
</div>
</section>

<section class="band band-white">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Seven goals guide everything we build.</h2>
<p class="lede">The goals are durable. Our objectives and roadmap change as we learn.</p>
</div>
<ol class="goals">{goals_html}</ol>
</div>
</section>

<section class="band band-deep">
<div class="wrap">
<p class="statement rv">All problems are solved when you put things together.</p>
<p class="lede rv" style="--i:1;margin-top:28px">Africa's challenges cannot be solved by one discipline, one institution or one person. Progress comes from bringing ideas, people, knowledge, resources and technology together. This is the principle behind how we hire, how we build and who we partner with.</p>
</div>
</section>

<section class="band band-pale">
<div class="wrap">
<div class="sec-head"><h2 class="h2">What we value.</h2></div>
<ul class="principles">{values_html}</ul>
</div>
</section>

<section class="band band-white">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Ethics guardrails for our defence work.</h2>
<p class="lede">These are commitments, and both founders are bound by them.</p>
</div>
<ul class="principles">{ethics_html}</ul>
</div>
</section>
''' + cta("Share our mission? Work with us.",
          "We are looking for engineers, researchers, partners and advisers who want to help build Nigeria's technology base.",
          "Get in touch", "Working%20with%20BOLTE") + FOOT

# ------------------------------------------------------------------ team
def pcard(n, role, line, img, i, big=False):
    alt = f"Portrait of {n}"
    return f'''<figure class="pc rv{" big" if big else ""}" style="--i:{i}">
<div class="ph"><img src="assets/team/{img}" alt="{alt}" width="560" height="700" loading="lazy"></div>
<figcaption><h3>{n}</h3><p class="role">{role}</p><p>{line}</p></figcaption>
</figure>
'''

founders_html = "".join(pcard(*t, i, True) for i, t in enumerate(TEAM_FOUNDERS))
core_html = "".join(pcard(*t, i) for i, t in enumerate(TEAM_CORE))

pages["team.html"] = head(
    "Team | BOLTE",
    "The people building BOLTE: two co-founders and a multidisciplinary engineering team, with an advisory board being appointed.",
    "team.html") + page_head(
    "The people building BOLTE.",
    "A small, multidisciplinary team of engineers, researchers and designers, led by two co-founders.") + f'''
<section class="band band-pale">
<div class="wrap">
<h2 class="h2" style="margin-bottom:44px">Co-founders</h2>
<div class="team-founders">{founders_html}</div>
<h2 class="h2" style="margin:88px 0 44px">Core team</h2>
<div class="team-core">{core_html}</div>
</div>
</section>

<section class="band band-navy grid-bg">
<div class="wrap">
<div class="sec-head">
<h2 class="h2 wide">Advisory board, being appointed.</h2>
<p class="lede">We are bringing in three independent advisers to strengthen how we plan, govern and engage with the defence sector. These seats are not yet filled, and we will name advisers once they have joined.</p>
</div>
<div class="advisers">
<div class="adviser rv"><h3>Business and finance</h3><p>Strategy, financial planning, fundraising and commercial terms.</p><p class="state">Seat open</p></div>
<div class="adviser rv" style="--i:1"><h3>Legal</h3><p>Corporate structure, intellectual property, contracts and regulatory compliance.</p><p class="state">Seat open</p></div>
<div class="adviser rv" style="--i:2"><h3>Defence and security</h3><p>Operational requirements, procurement pathways and responsible engagement with the sector.</p><p class="state">Seat open</p></div>
</div>
</div>
</section>
''' + cta("Interested in joining or advising?",
          "We are looking for engineers, researchers and experienced advisers who share this mission.",
          "Get in touch", "Joining%20BOLTE") + FOOT

# ------------------------------------------------------------------ contact
pages["contact.html"] = head(
    "Contact | BOLTE",
    "Contact BOLTE for partnerships, evaluations, research collaboration and careers.",
    "contact.html") + page_head(
    "Talk to us.",
    "Email is the best way to reach the founders. We read every message and reply to serious enquiries.") + f'''
<section class="band band-pale">
<div class="wrap contact-grid">
<div>
<h2 class="h2">Write to BOLTE.</h2>
<p><a class="mail-big" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="small" style="margin-top:18px">The inbox is monitored by the co-founders.</p>
<div class="notice"><strong>Please do not email</strong> classified or sensitive material, unpublished inventions or personal identity documents. We will arrange a secure channel when it is needed.</div>
</div>
<ul class="enq">
<li><strong>Pilots and evaluations</strong><span>Test our prototype at your site or review it technically.</span></li>
<li><strong>Institutional partnerships</strong><span>Government, security and aviation bodies, and authorised end users.</span></li>
<li><strong>Research collaboration</strong><span>Universities, laboratories and research groups.</span></li>
<li><strong>Investors and advisers</strong><span>Introductions for funding and advisory roles.</span></li>
<li><strong>Joining BOLTE</strong><span>Engineers and researchers in hardware, RF, software and security.</span></li>
</ul>
</div>
</section>
''' + FOOT

# ------------------------------------------------------------------ legal
pages["legal.html"] = head(
    "Privacy and notices | BOLTE",
    "Privacy information and notices for the BOLTE website.",
    "legal.html") + page_head(
    "Privacy and notices.",
    "How this website handles your information, and what it does and does not offer.") + f'''
<section class="band band-white">
<div class="wrap">
<div class="legal">
<h2>Privacy</h2>
<p>This website does not use cookies, analytics or tracking, and it has no forms or user accounts. Fonts are hosted on this site, so no third party sees your visit.</p>
<p>If you email us, we use your message and address only to reply and to follow up on your enquiry. We do not sell or share them. To ask us to delete correspondence, email <a class="link" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Team photographs</h2>
<p>Team portraits and names are published with each person's consent. Anyone can ask us to change how they are shown, or to remove their portrait, by emailing the address above.</p>
<h2>Company status</h2>
<p>BOLTE is being incorporated in Nigeria. Until registration is complete, this website describes the work of its founders and team.</p>
<h2>About our technology</h2>
<p>Descriptions of products reflect their current development stage. Prototypes, concepts and programmes are not commercial offers and carry no warranty. Nothing on this site discloses export-controlled or restricted technical information.</p>
<h2>Copyright and trademarks</h2>
<p>The BOLTE name, logo and site content belong to BOLTE. Please ask before reproducing them.</p>
</div>
</div>
</section>
''' + FOOT

pages["404.html"] = head("Page not found | BOLTE", "This page could not be found.", "") + page_head("Page not found.", "The page you asked for does not exist or has moved.") + f'''<section class="band band-white"><div class="wrap"><p><a class="btn btn-primary" href="index.html">Go to the home page</a></p></div></section>
''' + FOOT

for name, html in pages.items():
    (OUT / name).write_text(html, encoding="utf-8")
    print("wrote", name, len(html))
