# daejhonneldenton.store

Static personal site for **Daejhonnel Denton**, software engineer in Kingston, Jamaica,
trading as **Coronation Market and Software**.

No build step, no dependencies. Plain HTML, one stylesheet, one small script.
Open `index.html` in a browser and it works.

## Pages

| File | What it is |
|---|---|
| `index.html` | Home — hero, stats, three featured projects, how I work |
| `work.html` | Work index |
| `work/coronation-market.html` | Case study — marketplace, escrow, RLS |
| `work/night-haul.html` | Case study — Godot 4 game |
| `work/small-business-sites.html` | Case study — client site + WhatsApp packages |
| `services.html` | What I take on, pricing and turnaround |
| `about.html` | Bio, experience timeline, skills |
| `contact.html` | WhatsApp, phone, email, GitHub |
| `404.html` | Not-found page (GitHub Pages serves this automatically) |

`build.py` regenerates every page from one template. Edit `build.py`, run
`python3 build.py`, and all pages update together — that is where the nav,
footer and shared copy live.

## Publishing on GitHub Pages

1. Push this folder to the repo `7haTSheep/7haTSheep.github.io` (a GitHub *user
   site* repo — the name must match the account name exactly).
2. Repo → **Settings → Pages** → Source: *Deploy from a branch* → `main` / `/ (root)`.
3. The site appears at `https://7haTSheep.github.io/` within a minute or two.

## Pointing daejhonneldenton.store at it

The domain is registered at **Squarespace**. A `CNAME` file containing
`daejhonneldenton.store` is already in this repo, so GitHub Pages will claim it
as soon as DNS resolves.

In Squarespace: **Domains -> daejhonneldenton.store -> DNS Settings ->
Custom Records**. Delete any existing A record on `@` that Squarespace added
(it points at their parking page), then add:

| Host | Type  | Value                  |
|------|-------|------------------------|
| @    | A     | 185.199.108.153        |
| @    | A     | 185.199.109.153        |
| @    | A     | 185.199.110.153        |
| @    | A     | 185.199.111.153        |
| www  | CNAME | 7haTSheep.github.io    |

Then in the repo: **Settings -> Pages -> Custom domain** ->
`daejhonneldenton.store` -> Save. Wait for the DNS check to go green, then
tick **Enforce HTTPS** (the certificate can take up to an hour to issue).

DNS propagation is usually minutes, occasionally a few hours. Until it
resolves, the site is still live at `7haTSheep.github.io`.

## Editing

- Copy, links, project blurbs: `build.py`
- Colours, type, layout: `assets/site.css` (all colours are CSS variables at the top)
- Scroll animations: `assets/site.js`
- Portrait: `assets/portrait.jpg` (square, 900×900)
