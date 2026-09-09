# -*- coding: utf-8 -*-
"""Generates the static portfolio. No dependencies. Run: python3 build.py"""
import os, io, re

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://daejhonneldenton.store"
NAME = "Daejhonnel Denton"
LLC  = "Coronation Market and Software"
TEL  = "8765367328"
TELP = "876 536 7328"
MAIL = "kymanidenton7@gmail.com"
GH   = "https://github.com/7haTSheep"
FX_RATE = 160  # JMD per USD — rounded planning reference, not a live checkout rate.

def head(title, desc, rel="", page=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="{NAME}">
<meta name="theme-color" content="#0A0C0B">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/portrait.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{rel}assets/site.css">
</head>
<body>
{nav(rel, page)}
"""

def nav(rel, page):
    def cls(p): return ' on' if p == page else ''
    return f"""<nav class="nav">
  <div class="wrap">
    <a class="brand" href="{rel}index.html">
      <span class="mark">DD</span>
      <span class="stack"><b>{NAME}</b><span>{LLC}</span></span>
    </a>
    <div class="navlinks">
      <a class="link{cls('work')}" href="{rel}work.html">Work</a>
      <a class="link{cls('about')}" href="{rel}about.html">About</a>
      <a class="link{cls('services')}" href="{rel}services.html">Services</a>
      <a class="link{cls('contact')}" href="{rel}contact.html">Contact</a>
      <a class="cta" href="https://wa.me/{TEL}" target="_blank" rel="noopener">Hire me</a>
    </div>
  </div>
</nav>
"""

WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.48-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.01-1.04 2.47s1.06 2.86 1.21 3.06c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.28.17-1.41-.07-.13-.27-.2-.57-.35zM12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.28-1.38a9.86 9.86 0 0 0 4.76 1.21h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2z"/></svg>')

def foot(rel):
    return f"""
<footer>
  <div class="wrap fgrid">
    <div>
      <div class="small" style="color:var(--paper)">{NAME} &middot; {LLC}</div>
      <div class="small">Kingston, Jamaica &middot; Available worldwide &middot; &copy; <span data-year></span></div>
    </div>
    <div class="flinks">
      <a href="{rel}work.html">Work</a>
      <a href="{rel}about.html">About</a>
      <a href="{rel}services.html">Services</a>
      <a href="{rel}contact.html">Contact</a>
      <a href="{GH}" target="_blank" rel="noopener">GitHub</a>
      <a href="mailto:{MAIL}">Email</a>
    </div>
  </div>
</footer>
<a class="wa" href="https://wa.me/{TEL}" target="_blank" rel="noopener" aria-label="Message me on WhatsApp">{WA_SVG}</a>
<script src="{rel}assets/site.js"></script>
</body>
</html>
"""

def write(path, s):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, 'w', encoding='utf-8').write(s)
    print('wrote', path, len(s))

# ---------------------------------------------------------------- shared bits

TICKER = """<div class="ticker"><div class="row">
<b>React</b><b>TypeScript</b><b>Supabase / Postgres</b><b>Kotlin &amp; Java</b><b>Android</b><b>PHP &amp; MySQL</b><b>.NET</b><b>Angular</b><b>REST APIs</b><b>Row-Level Security</b><b>Double-entry ledgers</b><b>WordPress</b><b>Git</b><b>Agile / JIRA</b>
</div></div>"""

def mock_market():
    return """<div class="mock">
  <div class="bar"><i></i><i></i><i></i><em>coronationmarket.com / orders</em></div>
  <div class="body">
    <div class="sk gold w45"></div>
    <div class="mrow"><div class="mbox"></div><div class="mbox"></div><div class="mbox"></div></div>
    <div class="sk w90"></div><div class="sk w70"></div>
    <div class="sk go w55"></div>
    <div class="mrow"><div class="mbox"></div><div class="mbox"></div></div>
    <div class="sk w70"></div>
  </div>
</div>"""

def mock_haul():
    return """<div class="mock">
  <div class="bar"><i></i><i></i><i></i><em>night_haul.godot &mdash; scene: dock_04</em></div>
  <div class="body">
    <div class="mrow"><div class="mbox" style="height:88px"></div><div class="mbox" style="height:88px"></div></div>
    <div class="sk gold w55"></div>
    <div class="sk w90"></div><div class="sk w45"></div>
    <div class="mrow"><div class="mbox"></div><div class="mbox"></div><div class="mbox"></div></div>
  </div>
</div>"""

def mock_shop():
    return """<div class="mock">
  <div class="bar"><i></i><i></i><i></i><em>freshlinebarbers.com</em></div>
  <div class="body">
    <div class="sk gold w70"></div>
    <div class="sk w90"></div>
    <div class="mrow"><div class="mbox" style="height:60px"></div><div class="mbox" style="height:60px"></div></div>
    <div class="sk go w45"></div>
    <div class="sk w55"></div>
  </div>
</div>"""

def band(title, sub):
    return f"""<section class="sec"><div class="wrap"><div class="band rv">
  <h2>{title}</h2>
  <p class="lead">{sub}</p>
  <div class="herobtns">
    <a class="btn btn-p" href="https://wa.me/{TEL}" target="_blank" rel="noopener">WhatsApp {TELP}</a>
    <a class="btn btn-g" href="mailto:{MAIL}">Email me</a>
  </div>
</div></div></section>"""

def pricing_row(label, jmd, scope, featured=False):
    usd = round(jmd / FX_RATE / 10) * 10
    featured_class = " featured" if featured else ""
    return f"""<article class="price-row{featured_class} rv">
  <div class="price-service"><h3>{label}</h3><p>{scope}</p></div>
  <div class="price-values"><span class="price-jmd">From J${jmd:,.0f}</span><span class="price-usd">~US${usd:,.0f}</span></div>
  <a class="price-ask" href="https://wa.me/{TEL}?text=Hi%20Daejhonnel%20%E2%80%94%20I%27m%20interested%20in%20{label.replace(' ', '%20').replace('&', '%26')}." target="_blank" rel="noopener">Ask about it <span aria-hidden="true">&rarr;</span></a>
</article>"""

# ---------------------------------------------------------------- index

index = head(f"{NAME} — Software engineer, Kingston Jamaica",
             "Software engineer in Kingston, Jamaica. I build marketplaces, mobile apps and business websites that actually ship — React, Supabase, Kotlin, PHP.",
             "", "home")

index += f"""
<section class="hero"><div class="wrap">
  <p class="eyebrow">Kingston, Jamaica &middot; Available now</p>
  <h1>
    <span class="ln"><i>I build software</i></span>
    <span class="ln"><i>that <span class="it">ships</span> &mdash; and</i></span>
    <span class="ln"><i>then gets used.</i></span>
  </h1>
  <p class="lead">I'm {NAME}. I design and build marketplaces, Android apps and business websites end to end &mdash; database, payments, admin, the lot. Five years of production work, one live marketplace with money moving through it, and a habit of finishing.</p>
  <div class="herobtns">
    <a class="btn btn-p" href="work.html">See the work <span aria-hidden="true">&rarr;</span></a>
    <a class="btn btn-g" href="https://wa.me/{TEL}" target="_blank" rel="noopener">Start a project</a>
  </div>
</div></section>

{TICKER}

<section class="sec"><div class="wrap">
  <div class="stats rv">
    <div><b>5+</b><span>Years shipping</span></div>
    <div><b>33</b><span>Tables under RLS</span></div>
    <div><b>2</b><span>Platforms, one codebase</span></div>
    <div><b>72h</b><span>Typical turnaround, small builds</span></div>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv">
    <p class="eyebrow">Selected work</p>
    <h2>Three projects, three different problems.</h2>
    <p class="lead">One is a live marketplace that handles other people's money. One is a game in production. One is what a small Kingston business gets from me in a week.</p>
  </div>

  <div class="cards">
    <a class="card rv" href="work/coronation-market.html">
      <div class="glow"></div>
      <div class="card-in">
        <div>
          <div class="kicker">Marketplace &middot; Web + Android</div>
          <h3>Coronation Market</h3>
          <p>A two-sided marketplace where vendors list, buyers pay, and money sits in escrow until delivery lands. Postgres with row-level security on 33 tables, a double-entry wallet ledger, in-app chat, dispatch and an admin console.</p>
          <div class="chips"><span class="chip">React</span><span class="chip">Supabase</span><span class="chip">Kotlin</span><span class="chip">Escrow ledger</span><span class="chip">RLS</span></div>
          <span class="more">Read the case study <span class="arw">&rarr;</span></span>
        </div>
        {mock_market()}
      </div>
    </a>

    <a class="card rv" href="work/night-haul.html">
      <div class="glow"></div>
      <div class="card-in">
        <div>
          <div class="kicker">Game &middot; In production</div>
          <h3>Night Haul</h3>
          <p>A silhouette-noir hauling game built in Godot 4, moved off Unreal on purpose when the engine stopped serving the design. Systems work: routes, cargo, risk, and a look built out of light instead of texture.</p>
          <div class="chips"><span class="chip">Godot 4</span><span class="chip">GDScript</span><span class="chip">Systems design</span><span class="chip">Art direction</span></div>
          <span class="more">Read the case study <span class="arw">&rarr;</span></span>
        </div>
        {mock_haul()}
      </div>
    </a>

    <a class="card rv" href="work/small-business-sites.html">
      <div class="glow"></div>
      <div class="card-in">
        <div>
          <div class="kicker">Client work &middot; Kingston</div>
          <h3>Sites for small businesses</h3>
          <p>Fast one- and two-page sites for shops, salons and food spots: real photos, a menu or price list, a map, and a WhatsApp button that opens a chat already half-written. Live in a week, edited by the owner after.</p>
          <div class="chips"><span class="chip">HTML/CSS</span><span class="chip">WordPress</span><span class="chip">Google Business</span><span class="chip">WhatsApp Business</span></div>
          <span class="more">See what's included <span class="arw">&rarr;</span></span>
        </div>
        {mock_shop()}
      </div>
    </a>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv">
    <p class="eyebrow">How I work</p>
    <h2>No mystery, no month of silence.</h2>
  </div>
</div>
<div class="steps">
  <div class="steprow"><div class="wrap"><div class="step rv">
    <div class="n">01</div>
    <div><h3>We talk for twenty minutes</h3></div>
    <p>WhatsApp or a call. I want the actual problem, not a feature list &mdash; who's stuck, what it costs you, what "done" looks like. You leave with a straight answer on whether I'm the right person.</p>
  </div></div></div>
  <div class="steprow"><div class="wrap"><div class="step rv">
    <div class="n">02</div>
    <div><h3>Fixed scope, fixed price</h3></div>
    <p>You get it in writing: what's built, what isn't, the date, the number. Small builds are half up front, half on delivery. No hourly meter running while you think.</p>
  </div></div></div>
  <div class="steprow"><div class="wrap"><div class="step rv">
    <div class="n">03</div>
    <div><h3>You see it while it's being built</h3></div>
    <p>A live link from day one. You watch it fill in and say what's wrong early, when changing it is cheap &mdash; not at the end when it hurts.</p>
  </div></div></div>
  <div class="steprow"><div class="wrap"><div class="step rv">
    <div class="n">04</div>
    <div><h3>Handover you can actually use</h3></div>
    <p>The accounts are in your name, the code is yours, and I show you how to change the things you'll want to change. Two weeks of fixes included after launch.</p>
  </div></div></div>
</div></section>

{band("Got something that needs building?", "Tell me what's broken or what you want to launch. I answer WhatsApp faster than email, and I'll tell you honestly if it's not a job for me.")}
"""
index += foot("")
write("index.html", index)

# ---------------------------------------------------------------- work index

work = head(f"Work — {NAME}", "Case studies: Coronation Market, Night Haul, and small-business sites built in Kingston.", "", "work")
work += f"""
<section class="hero" style="padding-bottom:clamp(30px,5vw,50px)"><div class="wrap">
  <p class="eyebrow">Work</p>
  <h1 style="font-size:clamp(40px,7vw,80px)">Things I built,<br>and what they had to survive.</h1>
  <p class="lead" style="margin-top:24px">Each of these is written up properly &mdash; the constraint, the decision, and what I'd do differently. Not a screenshot gallery.</p>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="cards">
    <a class="card rv" href="work/coronation-market.html">
      <div class="glow"></div>
      <div class="card-in">
        <div>
          <div class="kicker">2024 &ndash; present &middot; Marketplace</div>
          <h3>Coronation Market</h3>
          <p>Vendors, buyers, escrow, delivery. The hard part wasn't the storefront &mdash; it was making sure nobody could see or move a dollar that wasn't theirs, from the database up.</p>
          <div class="chips"><span class="chip">React</span><span class="chip">Supabase / Postgres</span><span class="chip">Kotlin (Android)</span><span class="chip">Double-entry ledger</span><span class="chip">RLS</span><span class="chip">Realtime chat</span></div>
          <span class="more">Read the case study <span class="arw">&rarr;</span></span>
        </div>
        {mock_market()}
      </div>
    </a>
    <a class="card rv" href="work/night-haul.html">
      <div class="glow"></div>
      <div class="card-in">
        <div>
          <div class="kicker">2025 &ndash; present &middot; Game</div>
          <h3>Night Haul</h3>
          <p>Silhouette noir. Hauling runs at night, decisions with consequences, and an engine change made mid-project because the honest answer was that the first one was wrong.</p>
          <div class="chips"><span class="chip">Godot 4</span><span class="chip">GDScript</span><span class="chip">Systems design</span><span class="chip">Lighting-led art</span></div>
          <span class="more">Read the case study <span class="arw">&rarr;</span></span>
        </div>
        {mock_haul()}
      </div>
    </a>
    <a class="card rv" href="work/small-business-sites.html">
      <div class="glow"></div>
      <div class="card-in">
        <div>
          <div class="kicker">Ongoing &middot; Client work</div>
          <h3>Small-business sites &amp; WhatsApp setups</h3>
          <p>The unglamorous work that pays for the rest: a real website, a Google listing that shows up, and a WhatsApp Business account that takes orders without the owner retyping the menu every morning.</p>
          <div class="chips"><span class="chip">Static sites</span><span class="chip">WordPress</span><span class="chip">Google Business Profile</span><span class="chip">WhatsApp catalogue</span></div>
          <span class="more">See what's included <span class="arw">&rarr;</span></span>
        </div>
        {mock_shop()}
      </div>
    </a>
  </div>
</div></section>

{band("Want yours to be the next one?", "Small builds start the same week. Bigger ones start with a conversation.")}
"""
work += foot("")
write("work.html", work)

# ---------------------------------------------------------------- case: coronation

cm = head(f"Coronation Market — case study — {NAME}",
          "How I built a two-sided marketplace with escrow wallets, a double-entry ledger and row-level security across 33 Postgres tables.",
          "../", "work")
cm += f"""
<section class="case-hero"><div class="wrap">
  <a class="back" href="../work.html"><span aria-hidden="true">&larr;</span> All work</a>
  <p class="eyebrow">Case study &middot; Marketplace</p>
  <h1 style="font-size:clamp(40px,7vw,78px)">Coronation Market</h1>
  <p class="lead" style="margin-top:22px">A marketplace for Jamaican vendors and buyers, on the web and on Android. Money goes in, sits in escrow, and only moves when the delivery lands.</p>
  <div class="meta">
    <div><span>Role</span><b>Everything &mdash; design, backend, web, Android</b></div>
    <div><span>Stack</span><b>React, Supabase / Postgres, Kotlin</b></div>
    <div><span>Status</span><b>Live &mdash; web + Google Play</b></div>
    <div><span>Timeline</span><b>2024 &ndash; ongoing</b></div>
  </div>
</div></section>

<section class="sec" style="padding-top:clamp(40px,6vw,70px)"><div class="wrap"><div class="prose">

<h2 style="margin-top:0">The problem</h2>
<p>Selling online in Jamaica has a trust gap on both ends. The buyer doesn't want to send money to a stranger's account and hope. The vendor doesn't want to hand over goods and hope. Most local commerce solves this by not solving it &mdash; a DM, a bank transfer, and a lot of screenshots.</p>
<p>The product had to hold the money in the middle, prove it was holding it, and release it at the right moment. That single requirement decided most of the architecture.</p>

<div class="pull">If the ledger can drift, nothing else you build on top of it matters.</div>

<h2>How the money works</h2>
<p>Every account has a wallet, and every wallet movement is <strong>double-entry</strong> &mdash; each transaction writes matching rows, so at any moment the books either balance or the write failed. There is no "adjust the balance" path anywhere in the codebase; balances are derived, never edited.</p>
<p>Payment status is <strong>append-only</strong>. A database trigger writes every status change into a history table, so an order's payment life &mdash; pending, confirmed, released, refunded &mdash; is a chain you can read back rather than a single field somebody overwrote. When a customer says "I paid," the answer is in the table, with a timestamp.</p>

<div class="panel">
  <h3>Order lifecycle</h3>
  <div class="flow">
    <span class="node">Cart</span><span class="ar">&rarr;</span>
    <span class="node">Order created</span><span class="ar">&rarr;</span>
    <span class="node">Payment + receipt upload</span><span class="ar">&rarr;</span>
    <span class="node">Escrow held</span><span class="ar">&rarr;</span>
    <span class="node">Dispatch</span><span class="ar">&rarr;</span>
    <span class="node">Delivered</span><span class="ar">&rarr;</span>
    <span class="node">Vendor paid out</span>
  </div>
  <p class="small dim" style="margin:18px 0 0">Local rails, not Stripe. Bank transfer and Lynk with a receipt upload, reconciled in the admin console &mdash; because that is what people here actually use.</p>
</div>

<h2>Security that isn't in the front end</h2>
<p>The rule I worked to: if you turned off the entire web app and hit the database directly with a signed-in user's token, you should still only be able to see and touch your own rows.</p>
<p>That meant <strong>row-level security across all 33 tables</strong> &mdash; orders, wallets, ledger entries, chat messages, delivery assignments, receipts. Policies are written per role: a buyer sees their orders, a vendor sees orders containing their products, a dispatcher sees only what's assigned to them, admin sees the console. The front end is a convenience layer, not a security layer.</p>
<ul>
  <li>Order IDs are random rather than sequential, so nobody can guess the next one or count your volume.</li>
  <li>Receipt uploads land in scoped storage with policies matching the order's owner.</li>
  <li>Admin actions are logged as data, not as console output.</li>
</ul>

<h2>One product, two clients</h2>
<div class="grid2">
  <div class="tile"><div class="ic">Web</div><h3>React storefront</h3><p>Browsing, cart, checkout, order tracking, vendor dashboard and the admin console &mdash; the surface where most of the work gets done.</p></div>
  <div class="tile"><div class="ic">Android</div><h3>Kotlin app on Play</h3><p>The client most buyers actually use. Same Postgres, same policies, native where it matters &mdash; notifications, camera for receipts, offline-tolerant lists.</p></div>
</div>
<p>Both talk to the same database with the same rules, so a policy fix ships to both at once. There is no second set of business logic to keep in sync, which is the failure mode I was most worried about.</p>

<h2>The rest of the system</h2>
<div class="grid3">
  <div class="tile"><div class="ic">Chat</div><h3>In-app messaging</h3><p>Buyer to vendor, realtime, attached to the order &mdash; so the conversation and the dispute evidence live in the same place.</p></div>
  <div class="tile"><div class="ic">Dispatch</div><h3>Delivery assignment</h3><p>Orders move to a courier with status transitions that the buyer can see, and that the escrow release depends on.</p></div>
  <div class="tile"><div class="ic">Admin</div><h3>Operations console</h3><p>Confirm payments, resolve disputes, release funds, watch the ledger. Boring on purpose.</p></div>
</div>

<h2>What I'd do differently</h2>
<p>I'd write the ledger's reconciliation report on day one instead of month three. It existed in my head long before it existed as a page, and every time I wanted to verify a balance early on I was writing the same query by hand. The moment I built the report, three small bugs surfaced in an afternoon that I might otherwise have found from a customer.</p>
<p>I'd also have set up the admin console before the storefront. The storefront is the fun part, but every hour of real operations runs through the console, and building it second meant retrofitting things the ops flow needed.</p>

<h2>What it demonstrates</h2>
<ul>
  <li><strong>I can hold money safely.</strong> Escrow, double-entry, append-only history, per-row authorization.</li>
  <li><strong>I can carry a product end to end.</strong> Schema, policies, two clients, admin tooling, Play Store release.</li>
  <li><strong>I build for where it runs.</strong> Local payment rails and patchy connections, not a US-market assumption copy-pasted onto Kingston.</li>
</ul>

</div></div></section>

{band("Need something built to this standard?", "Payments, marketplaces, admin tooling, mobile. Tell me what you're trying to do.")}
"""
cm += foot("../")
write("work/coronation-market.html", cm)

# ---------------------------------------------------------------- case: night haul

nh = head(f"Night Haul — case study — {NAME}",
          "A silhouette-noir hauling game in Godot 4 — systems design, art direction, and why I moved engines mid-project.",
          "../", "work")
nh += f"""
<section class="case-hero"><div class="wrap">
  <a class="back" href="../work.html"><span aria-hidden="true">&larr;</span> All work</a>
  <p class="eyebrow">Case study &middot; Game</p>
  <h1 style="font-size:clamp(40px,7vw,78px)">Night Haul</h1>
  <p class="lead" style="margin-top:22px">You move cargo at night. The route is a decision, the load is a risk, and everything you see is a shape against light. Built in Godot 4, in production.</p>
  <div class="meta">
    <div><span>Role</span><b>Design, systems, implementation</b></div>
    <div><span>Engine</span><b>Godot 4 (moved from Unreal 5)</b></div>
    <div><span>Look</span><b>Silhouette noir</b></div>
    <div><span>Status</span><b>In production</b></div>
  </div>
</div></section>

<section class="sec" style="padding-top:clamp(40px,6vw,70px)"><div class="wrap"><div class="prose">

<h2 style="margin-top:0">The idea</h2>
<p>A hauling game where the interesting choices happen before the drive. Which load, which route, how much risk you're willing to carry for the fee &mdash; and then living with it in the dark, where you can see the shape of a problem long before you can see what it is.</p>

<div class="pull">The dark isn't a mood. It's the mechanic that makes every other decision cost something.</div>

<h2>Silhouette noir</h2>
<p>The art direction is a constraint dressed as a style. Objects read as <strong>shapes against light</strong> rather than as textured models: headlamps, signage, a window, a fire. It gives the game a look that's genuinely its own, and it means a solo developer isn't competing on texture budgets he doesn't have.</p>
<p>Lighting does the work that art assets normally do. What you can see is a design lever &mdash; pull light away and tension appears for free; put a lamp somewhere and you've made a landmark.</p>

<div class="grid3">
  <div class="tile"><div class="ic">Routes</div><h3>Choice with teeth</h3><p>Faster is riskier, and the map is a set of trade-offs rather than a shortest path.</p></div>
  <div class="tile"><div class="ic">Cargo</div><h3>Load as constraint</h3><p>What you carry changes how you drive, what you can afford to lose, and who's interested in it.</p></div>
  <div class="tile"><div class="ic">Risk</div><h3>Pressure, not jumpscares</h3><p>The threat model is being seen and being slow, built out of light and time rather than combat.</p></div>
</div>

<h2>The engine call</h2>
<p>It started in Unreal 5. Unreal is superb at photoreal fidelity, which is precisely the thing this game had decided not to compete on &mdash; and the cost of that fidelity showed up as iteration time, build weight and a lot of machinery I was fighting past rather than using.</p>
<p>I moved it to <strong>Godot 4</strong>. Smaller, faster to iterate, and its lighting and 2D/3D hybrid tooling sit much closer to what silhouette noir actually needs. It cost real weeks to switch.</p>
<p>I include it here on purpose, because it's the kind of decision I'd want to see from someone I was hiring: I noticed the tool was wrong for the design, checked that I wasn't just avoiding a hard part, and paid the switching cost while it was still cheap rather than defending the original choice for another year.</p>

<h2>Where it is</h2>
<p>Pre-production is done: the design document, the core loop, the art direction and the vertical-slice targets are written down and settled. Current work is systems &mdash; routes, cargo, risk, and the night itself &mdash; in Godot 4, in a repo with the design doc versioned next to the code.</p>

<h2>What it demonstrates</h2>
<ul>
  <li><strong>I finish the thinking before I write the code.</strong> Concept source, design doc, then systems.</li>
  <li><strong>I can change my mind expensively.</strong> The engine pivot was the right call and I made it early.</li>
  <li><strong>I design inside constraints.</strong> Solo scope, turned into a look nobody else has.</li>
</ul>

</div></div></section>

{band("Want to talk shop?", "Games, tools, or anything with a systems problem in it — I'm easy to reach.")}
"""
nh += foot("../")
write("work/night-haul.html", nh)

# ---------------------------------------------------------------- case: small business

sb = head(f"Small-business sites — {NAME}",
          "Fast websites, Google listings and WhatsApp Business setups for Kingston shops, salons and food spots.",
          "../", "work")
sb += f"""
<section class="case-hero"><div class="wrap">
  <a class="back" href="../work.html"><span aria-hidden="true">&larr;</span> All work</a>
  <p class="eyebrow">Client work &middot; Kingston</p>
  <h1 style="font-size:clamp(40px,7vw,78px)">Sites for small businesses</h1>
  <p class="lead" style="margin-top:22px">Most shops here don't need an app. They need to be findable, to look like a real business, and to take an order without three rounds of "how much again?"</p>
  <div class="meta">
    <div><span>Typical build</span><b>5 to 7 days</b></div>
    <div><span>Deliverables</span><b>Site, Google listing, WhatsApp setup</b></div>
    <div><span>Ownership</span><b>Every account in your name</b></div>
    <div><span>After launch</span><b>Two weeks of fixes included</b></div>
  </div>
</div></section>

<section class="sec" style="padding-top:clamp(40px,6vw,70px)"><div class="wrap"><div class="prose">

<h2 style="margin-top:0">What actually loses the sale</h2>
<p>I've watched the same three things cost small businesses money over and over. Someone searches your name and finds a Facebook page last updated in 2021. Someone asks the price and waits forty minutes for a reply. Someone wants to order and has to type out the whole menu from a photo.</p>
<p>None of that is a technology problem. It's a setup problem, and it takes about a week to fix properly.</p>

<div class="pull">A website that nobody finds is a business card in a drawer. The listing and the WhatsApp are half the job.</div>

<h2>What you get</h2>
<div class="grid2">
  <div class="tile"><div class="ic">01</div><h3>A site that loads instantly</h3><p>One or two pages, your real photos, what you sell, the prices, the hours, a map, and a phone number that dials on tap. No template bloat, no cookie banner, no plugin that breaks in six months.</p></div>
  <div class="tile"><div class="ic">02</div><h3>A Google listing that shows up</h3><p>Google Business Profile claimed, categories right, hours right, photos in, and a review link you can send to customers in one tap. This is the part that brings walk-ins.</p></div>
  <div class="tile"><div class="ic">03</div><h3>WhatsApp Business, set up properly</h3><p>Catalogue with your items, quick replies for the questions you answer twenty times a day, and an order flow the customer can follow without you typing.</p></div>
  <div class="tile"><div class="ic">04</div><h3>Handover, not hostage</h3><p>Domain, hosting, Google and WhatsApp all in your name and on your phone. I show you how to change a price yourself. You are never stuck waiting on me.</p></div>
</div>

<h2>How the week goes</h2>
<div class="panel">
  <div class="flow">
    <span class="node">Day 1: photos + prices from you</span><span class="ar">&rarr;</span>
    <span class="node">Day 2&ndash;3: site built, live link</span><span class="ar">&rarr;</span>
    <span class="node">Day 4: your changes</span><span class="ar">&rarr;</span>
    <span class="node">Day 5: Google + WhatsApp</span><span class="ar">&rarr;</span>
    <span class="node">Launch</span>
  </div>
  <p class="small dim" style="margin:18px 0 0">You see a live link from day two. Nothing is a surprise at the end.</p>
</div>

<h2>Straight answers to the usual questions</h2>
<h3>Can I edit it myself?</h3>
<p>Yes &mdash; prices, hours and photos, and I'll walk you through it once on a call. Anything structural, message me and small changes are usually same-day.</p>
<h3>What does it cost to keep running?</h3>
<p>The domain is roughly the price of a lunch per month, hosting on a small site is free or close to it, and Google and WhatsApp cost nothing. I'll tell you the exact numbers before you commit to anything.</p>
<h3>What if I already have a site?</h3>
<p>Then we probably don't rebuild it. Often the fix is the listing, the speed and the WhatsApp setup, and I'll say so rather than sell you a rebuild you don't need.</p>

</div></div></section>

{band("Run a business in Kingston?", "Message me on WhatsApp with your business name and what you sell. I'll tell you what I'd do and what it costs, before you pay anything.")}
"""
sb += foot("../")
write("work/small-business-sites.html", sb)

# ---------------------------------------------------------------- services

sv = head(f"Services — {NAME}",
          "What I take on: web apps, Android, marketplaces and payments, small-business sites, and rescue work on projects that stalled.",
          "", "services")
sv += f"""
<section class="hero" style="padding-bottom:clamp(30px,5vw,50px)"><div class="wrap">
  <p class="eyebrow">Services</p>
  <h1 style="font-size:clamp(40px,7vw,80px)">What I take on.</h1>
  <p class="lead" style="margin-top:24px">Fixed scope, fixed price, a date in writing. If your job isn't on this list, ask anyway &mdash; I'd rather tell you it's not for me than take it and go quiet.</p>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="grid2">
    <div class="tile rv"><div class="ic">Build</div><h3>Web applications</h3><p>React front ends on a real backend &mdash; auth, roles, data model, admin. The kind with logged-in users and permissions, not a brochure.</p></div>
    <div class="tile rv"><div class="ic">Build</div><h3>Android apps</h3><p>Kotlin and Java, from a first release to a Play Store listing. Native where it earns its keep.</p></div>
    <div class="tile rv"><div class="ic">Build</div><h3>Marketplaces &amp; payments</h3><p>Two-sided platforms, wallets, escrow, payouts, ledgers and the admin console that keeps them honest. This is where I'm strongest.</p></div>
    <div class="tile rv"><div class="ic">Build</div><h3>Business websites</h3><p>Fast, findable one- and two-page sites with the Google listing and WhatsApp setup done alongside. Live in a week.</p></div>
    <div class="tile rv"><div class="ic">Fix</div><h3>Rescue work</h3><p>A build someone abandoned, an app that won't ship, a site that broke after an update. I'll audit it first and tell you honestly whether to save it or restart it.</p></div>
    <div class="tile rv"><div class="ic">Fix</div><h3>Same-day patches</h3><p>Broken checkout, form that doesn't send, layout wrecked on phones, deploy that won't go. Small, urgent, and priced as one job.</p></div>
  </div>
</div></section>

<section class="sec pricing" id="pricing"><div class="wrap">
  <div class="pricing-intro rv">
    <div>
      <p class="eyebrow">Starting prices</p>
      <h2>Clear numbers before we talk.</h2>
    </div>
    <p class="lead">These are starting investments for a defined first release. The final quote is fixed in writing after scope — no surprise hourly bill.</p>
  </div>

  <div class="price-board">
    <div class="price-board-head">
      <span>What you need</span><span>Starting investment</span><span>Next step</span>
    </div>
    {pricing_row("Same-day patch", 12500, "A broken form, checkout, mobile layout or deployment problem. One clearly defined fix.")}
    {pricing_row("Business website", 85000, "A focused one- or two-page site with your photos, services, location and a direct WhatsApp contact path.", True)}
    {pricing_row("Business launch setup", 125000, "Website plus Google Business Profile and WhatsApp Business setup — designed to help customers find and contact you.")}
    {pricing_row("Android app MVP", 450000, "A first Android release with core screens, backend connection and Play Store-ready delivery.")}
    {pricing_row("Custom web application", 650000, "A real logged-in product: data model, roles, admin and a focused first release.")}
    {pricing_row("Marketplace or payments build", 1250000, "Multi-user platforms, wallets, escrow or payouts. Starts with a paid discovery and technical plan.")}
  </div>

  <div class="price-notes rv">
    <p><b>Currency:</b> JMD is the quoted currency. USD is an approximate reference at J$160 = US$1, rounded for readability.</p>
    <p><b>Payment:</b> Small builds are 50% to begin and 50% at delivery. Larger projects are split into milestones.</p>
    <p><b>Included:</b> A live preview during the build, a proper handover, and two weeks of post-launch fixes.</p>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv">
    <p class="eyebrow">Working with me</p>
    <h2>The parts people usually have to ask about.</h2>
  </div>
  <div class="grid3">
    <div class="tile rv"><div class="ic">Money</div><h3>How I price</h3><p>Fixed price per job wherever I can scope it. Half up front on small builds, the rest on delivery. Hourly only for open-ended work, and I'll say so up front.</p></div>
    <div class="tile rv"><div class="ic">Time</div><h3>Turnaround</h3><p>Small fixes in 24 to 72 hours. A business site in about a week. Anything bigger gets a real schedule with milestones, not a vibe.</p></div>
    <div class="tile rv"><div class="ic">Reach</div><h3>Where I work</h3><p>Based in Kingston, on site around the corporate area. Remote for everyone else &mdash; most of my week is already async.</p></div>
    <div class="tile rv"><div class="ic">After</div><h3>What happens post-launch</h3><p>Two weeks of fixes included on every build. After that, either you run it yourself or we agree a small monthly arrangement. No lock-in either way.</p></div>
    <div class="tile rv"><div class="ic">Ownership</div><h3>Who owns it</h3><p>You do. Code, domain, hosting, accounts &mdash; all in your name from the start, not transferred at the end if you ask nicely.</p></div>
    <div class="tile rv"><div class="ic">Honesty</div><h3>What I'll turn down</h3><p>Work I'd do badly, deadlines I can't hit, and rebuilds you don't need. Saying no early is cheaper for both of us than saying yes and disappearing.</p></div>
  </div>
</div></section>

{band("Describe the job in two sentences.", "That's usually enough for me to tell you whether it's a fit, roughly what it costs, and when I could start.")}
"""
sv += foot("")
write("services.html", sv)

# ---------------------------------------------------------------- about

ab = head(f"About — {NAME}",
          "Software engineer in Kingston, Jamaica. Five years across web, Android and backend, now building under Coronation Market and Software.",
          "", "about")
ab += f"""
<section class="hero" style="padding-bottom:clamp(30px,5vw,50px)"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1 style="font-size:clamp(40px,7vw,80px)">Kingston-based.<br>Finishes things.</h1>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="about-grid">
    <div class="portrait rv"><img src="assets/portrait.jpg" alt="Portrait of {NAME}" width="900" height="900"></div>
    <div class="rv">
      <p class="lead" style="max-width:none; color:#D7D3CA">I'm {NAME} &mdash; a software engineer in Kingston, Jamaica, working under my own company, {LLC}.</p>
      <p class="dim">I've spent about five years shipping production software across web, Android and backend: mobile work in Objective-C, Java and Kotlin, web in JavaScript, Angular, PHP and .NET, and databases in MySQL and Postgres. Agile teams, JIRA boards, code review, the normal machinery of building software with other people.</p>
      <p class="dim">What I care about is the boring, unglamorous end of the work: does the data model hold up, can somebody see a row they shouldn't, does the thing still work on a bad connection in the middle of Half Way Tree. Most software fails there, not in the design.</p>
      <p class="dim">Right now I split my time between Coronation Market &mdash; a live marketplace with real money moving through it &mdash; Night Haul, a game in production, and client work for businesses around Kingston that need a website, a Google listing and a WhatsApp setup that works.</p>
      <p class="dim">If you want the short version: I'd rather tell you the honest thing early than the comfortable thing now.</p>
      <div class="herobtns">
        <a class="btn btn-p" href="contact.html">Get in touch</a>
        <a class="btn btn-g" href="{GH}" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>
  </div>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-head rv"><p class="eyebrow">Experience</p><h2>Where I've worked.</h2></div>
  <div class="about-grid">
    <div class="rv">
      <div class="tl">
        <div class="job">
          <div class="when">2024 &ndash; present</div>
          <h3>Founder &amp; engineer</h3>
          <div class="co">{LLC}</div>
          <p>My own shop. Building Coronation Market end to end, plus client sites, apps and rescue work for businesses in Kingston.</p>
        </div>
        <div class="job">
          <div class="when">2025 &ndash; 2026</div>
          <h3>Software engineer</h3>
          <div class="co">Yardie River Tours</div>
          <p>Web and booking-side work for a Jamaican tour operator.</p>
        </div>
        <div class="job">
          <div class="when">2025 &ndash; 2026</div>
          <h3>Software engineer</h3>
          <div class="co">Gibbo-Trading</div>
          <p>Application development and integration work.</p>
        </div>
        <div class="job">
          <div class="when">2020 &ndash; 2024</div>
          <h3>Software engineer</h3>
          <div class="co">Amber Group</div>
          <p>Four years in a production engineering team &mdash; mobile and web development, code review, Agile delivery on a JIRA board, shipping to real users.</p>
        </div>
      </div>
    </div>
    <div class="rv">
      <div class="skillset">
        <div>
          <h3>Mobile</h3>
          <ul><li>Kotlin</li><li>Java (Android)</li><li>Objective-C</li><li>Google Play releases</li></ul>
        </div>
        <div>
          <h3>Web</h3>
          <ul><li>JavaScript / TypeScript</li><li>React</li><li>Angular</li><li>HTML5 &amp; CSS</li><li>WordPress</li></ul>
        </div>
        <div>
          <h3>Backend &amp; data</h3>
          <ul><li>PHP</li><li>.NET</li><li>PostgreSQL / Supabase</li><li>MySQL</li><li>REST APIs</li><li>Row-level security</li></ul>
        </div>
        <div>
          <h3>Practice</h3>
          <ul><li>Git</li><li>Agile / Scrum</li><li>JIRA</li><li>Code review</li><li>Godot 4</li></ul>
        </div>
      </div>
    </div>
  </div>
</div></section>

{band("Rather just talk?", "WhatsApp is the fastest way to reach me, and I don't mind a question that turns out not to be a job.")}
"""
ab += foot("")
write("about.html", ab)

# ---------------------------------------------------------------- contact

ct = head(f"Contact — {NAME}",
          f"Reach {NAME} in Kingston, Jamaica — WhatsApp {TELP}, email, or GitHub.",
          "", "contact")
ct += f"""
<section class="hero" style="padding-bottom:clamp(30px,5vw,50px)"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1 style="font-size:clamp(40px,7vw,80px)">Let's talk.</h1>
  <p class="lead" style="margin-top:24px">Tell me what you're trying to build or what's broken. Two sentences is enough to start &mdash; I'll come back with questions, a rough number, and whether I'm the right person.</p>
</div></section>

<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="contact-grid">
    <div class="rv">
      <a class="cline" href="https://wa.me/{TEL}" target="_blank" rel="noopener">
        <span class="ic">{WA_SVG}</span>
        <span class="t"><span>Fastest &mdash; usually same day</span><b>WhatsApp {TELP}</b></span>
        <span class="arw">&rarr;</span>
      </a>
      <a class="cline" href="tel:+1{TEL}">
        <span class="ic">&#9742;</span>
        <span class="t"><span>Call</span><b>+1 {TELP}</b></span>
        <span class="arw">&rarr;</span>
      </a>
      <a class="cline" href="mailto:{MAIL}">
        <span class="ic">&#9993;</span>
        <span class="t"><span>Email &mdash; good for detail</span><b>{MAIL}</b></span>
        <span class="arw">&rarr;</span>
      </a>
      <a class="cline" href="{GH}" target="_blank" rel="noopener">
        <span class="ic">&lt;/&gt;</span>
        <span class="t"><span>Code</span><b>github.com/7haTSheep</b></span>
        <span class="arw">&rarr;</span>
      </a>
      <div class="cline" style="cursor:default">
        <span class="ic">&#9679;</span>
        <span class="t"><span>Based in</span><b>Kingston, Jamaica &mdash; remote worldwide</b></span>
      </div>
    </div>
    <div class="rv">
      <div class="panel" style="margin:0">
        <h3>What to send me</h3>
        <p class="dim small">You don't need a spec. This is plenty:</p>
        <ul class="dim small" style="padding-left:18px; line-height:1.7">
          <li>What the business does</li>
          <li>What you want to happen that isn't happening</li>
          <li>Whether anything exists already (a site, an app, a half-built thing)</li>
          <li>When you need it, and roughly what you can spend</li>
        </ul>
        <p class="dim small" style="margin-bottom:0">If it's urgent, say so in the first line &mdash; I triage on that.</p>
      </div>
      <div class="panel">
        <h3>Hours</h3>
        <p class="dim small" style="margin:0">Kingston time (EST, no daylight saving). Messages after hours get answered the next morning; genuinely broken production gets answered whenever.</p>
      </div>
    </div>
  </div>
</div></section>
"""
ct += foot("")
write("contact.html", ct)

# ---------------------------------------------------------------- 404

nf = head(f"Not found — {NAME}", "That page doesn't exist.", "", "")
nf += f"""
<section class="hero"><div class="wrap">
  <p class="eyebrow">404</p>
  <h1 style="font-size:clamp(44px,8vw,90px)">That page took<br>a different route.</h1>
  <p class="lead" style="margin-top:24px">Nothing lives at this address. The work is still where you left it.</p>
  <div class="herobtns">
    <a class="btn btn-p" href="index.html">Back home</a>
    <a class="btn btn-g" href="work.html">See the work</a>
  </div>
</div></section>
"""
nf += foot("")
write("404.html", nf)
print("done")
