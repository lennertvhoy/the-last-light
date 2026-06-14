# The Last Light — Site UI/UX Audit

**Date:** 2026-06-14

**Agent ID:** NA-7 (UI/UX audit slice)

**Evidence folder:**
`/home/ff/Documents/Projects/the-last-light/Evidence/01-ui-ux-audit-2026-06-14/`

**URLs tested:**

- Local: `http://127.0.0.1:3456/`
- Public: `https://lennertvhoy.github.io/the-last-light/`
- Dutch route: `http://127.0.0.1:3456/#/nl/`
- 404 probe: `http://127.0.0.1:3456/#/nonexistent-page`

**Tools used:** Kimi WebBridge (primary), Playwright (mobile viewport screenshots only).

---

## Executive Summary

The Docsify site for *The Last Light* is structurally sound and visually coherent, but
it currently behaves more like a raw manuscript preview than a book landing page or
publisher pitch asset. The biggest risks are **content-quality signals** that undermine
trust: inline editorial comments are visible in the rendered Author's Note, the Dutch
route is broken, and the 404 page offers no recovery path. The visual layer is clean
but under-leveraged for positioning, audience conversion, and publisher/media discovery.

**Bottom line:** fix the visible editorial marks and the Dutch route first; then redesign
the homepage to explain who the book is for and add a publisher/media path.

---

## What Works Already

1. **Clear title and subtitle** — the coverpage immediately states the book's premise.
2. **Responsive layout** — the site adapts to mobile; buttons stack, text reflows, and the
   menu is reachable.
3. **Search works** — Docsify search indexes the manuscript and returns relevant
   chapter/section links.
4. **Sidebar navigation is comprehensive** — all 22 chapters, interludes, epilogue, and 7
   appendices are linked.
5. **Dark theme is readable** — contrast and line length are comfortable on desktop.
6. **Open-source framing is present** — GitHub link and "contribute, critique, remix" copy
   signal openness.
7. **Language switcher exists** — the EN/NL toggle is discoverable (bottom-right fixed
   position).
8. **Public deployment matches local** — GitHub Pages serves the same build as the local
   dev server.

---

## Major Blockers (Fix Before Promotion)

### B1. Inline editorial comments visible to readers

- **Evidence:** `02-bookpage-desktop.png`, `07-bookpage-mobile.png`, browser DOM inspection.
- **Detail:** The Author's Note contains at least seven visible `* edit: ...` annotations
  (e.g., "\* edit: i don't teach schoolchildren...", "\* edit: bit dramatic no?..."). These
  read like private author notes, not finished prose.
- **Impact:** Severely damages trust and publisher readiness; the site does not look like
  a serious book landing page.
- **Root cause:** The canonical manuscript `The-Last-Light.md` still contains cleanup
  markup that was not removed before publication.

### B2. Dutch (`/nl/`) route is broken and confusing

- **Evidence:** `05-nl-coverpage-desktop.png`.
- **Detail:** The NL coverpage still shows the English title, subtitle, body copy, and
  CTAs. The CTA buttons are unstyled text links. Only the disclaimer at the bottom is
  Dutch ("Vertaald door AI. Controleer de originele Engelse versie bij twijfel.").
- **Impact:** Flemish/Dutch visitors land on a page that looks like a rendering bug, not
  a translation.
- **Root cause:** `nl/` holds the old translation of the previous 35-chapter manuscript
  and has not been regenerated or clearly deprecated.

### B3. 404 page is a dead end

- **Evidence:** `11-404-page-desktop.png`.
- **Detail:** Unknown routes show only "404 - Not found" with no link back home, no search
  prompt, and no navigation guidance.
- **Impact:** A shared bad link or typo loses the visitor immediately.

---

## High-Leverage Improvements (Ranked)

1. Scrub the manuscript of editorial markup before rendering. This is the highest-ROI fix
   because it removes the strongest negative signal.
2. Redesign the coverpage above the fold. Add: who the book is for, the core promise,
   social/trust signals, and clearer primary/secondary CTAs.
3. Add a publisher/media package path. A `/publisher` or `/media` route should expose the
   Flemish-market materials, title options, author bio, sample chapters, and
   contact/download CTAs.
4. Fix or retire the Dutch route. Either regenerate a real Dutch translation or replace
   the route with a clear "Dutch edition coming soon" page.
5. Improve sidebar scannability. Stop forcing link text to ALL CAPS; widen or wrap labels
   so chapter titles are not truncated.
6. Enhance the 404 page. Add a home link, search prompt, and suggested starting chapters.
7. Add trust signals. Author photo/bio, endorsements, institutional affiliations,
   speaking topics, newsletter signup.
8. Add an "About this project / Manifesto" page. Explain the book's open-source intent and
   how to engage.
9. Polish mobile details. Prevent the language switcher from overlapping body text; ensure
   tap targets are large enough.
10. Visual polish. After structure and copy are fixed, refine spacing, typography scale,
    and the coverpage background.

---

## Page-by-Page Findings

### Coverpage (`/`)

- **Works:** Title, subtitle, hook, and CTAs are centered and legible.
- **Gap:** It does not answer "Who is this for?" or "Why should I read it now?" The value
  proposition is abstract.
- **Gap:** No publisher, media, or classroom entry points.
- **Gap:** The background is plain dark; the page feels like a placeholder rather than a
  book launch asset.
- **Evidence:** `01-coverpage-desktop.png`, `06-coverpage-mobile.png`,
  `12-public-live-coverpage-desktop.png`.

### Book page (`/#/The-Last-Light`)

- **Works:** Full manuscript loads, headings render, pagination moves between chapters.
- **Gap:** Editorial markup visible in Author's Note (B1).
- **Gap:** Sidebar link labels are truncated and in ALL CAPS, making the table of contents
  hard to scan.
- **Gap:** There is no "download EPUB/PDF" or "buy" CTA for readers who want the book
  offline.
- **Evidence:** `02-bookpage-desktop.png`, `03-chapter1-desktop.png`,
  `04-chapter1-scrolled-desktop.png`, `10-sidebar-forced-open-desktop.png`,
  `07-bookpage-mobile.png`.

### Dutch route (`/#/nl/`)

- **Works:** The route loads and the language switcher flips to EN.
- **Gap:** Content is still English; CTA buttons are unstyled text (B2).
- **Evidence:** `05-nl-coverpage-desktop.png`.

### 404 page

- **Gap:** Bare "404 - Not found" with no recovery path (B3).
- **Evidence:** `11-404-page-desktop.png`.

---

## Mobile Findings

- **Viewport tested:** 390 × 844 px (iPhone-style).
- **Responsive behavior:** The coverpage reflows correctly; buttons stack; the menu button
  is visible and opens the sidebar.
- **Strength:** Text size and line length remain readable.
- **Issue:** The fixed EN/NL switcher overlaps body text when scrolling
  (`07-bookpage-mobile.png`).
- **Issue:** The sidebar consumes most of the screen when open; closing it requires
  tapping the menu button again or tapping the content area, which is not obvious.
- **Issue:** Chapter titles in the sidebar are heavily truncated, more so than on desktop.
- **Evidence:** `06-coverpage-mobile.png`, `07-bookpage-mobile.png`, `08-menu-mobile.png`.

---

## Accessibility Findings

- **Landmarks:** The page uses `main`, `complementary`, and `navigation` roles.
- **Search:** The search input has an accessible label ("Search text").
- **Headings:** The main manuscript has a logical H1 → H2 → H3 structure.
- **Issues found:**
  - The Docsify "View source on Github" link at top right has no visible text
    (icon-only).
  - The language switcher is injected by JS as a bare `<a>` with flag emoji text; it
    lacks an accessible name describing its purpose.
  - The coverpage and book page may contain duplicate H1s because Docsify keeps the
    coverpage in the DOM alongside the book content.
  - Sidebar links are rendered in ALL CAPS, which can be harder to read for some users
    and is read letter-by-letter by some screen readers.

---

## Copy / Content Findings

1. **Editorial markup in manuscript** (B1) — must be cleaned.
2. **Coverpage copy is accurate but generic.** It does not differentiate the book from
   other AI-ethics titles.
3. **No clear audience labels.** The site mentions "classrooms, professionals, and
   governance" but does not speak directly to any of them.
4. **Dutch disclaimer is honest but alarming.** "Vertaald door AI" is a trust hit; if the
   translation is AI-generated and unreviewed, the route should not be public-facing.
5. **README.md vs. coverpage:** The repo README is more informative than the site
   coverpage; the site should borrow from it.

---

## Suggested Information Architecture

```text
/
├── /start              (coverpage + value proposition)
├── /read               (the book, current /The-Last-Light)
├── /about              (author, project intent, manifesto)
├── /publisher          (media kit, samples, title options, contact)
├── /classroom          (teaching guides, appendices, slide requests)
├── /nl/                (Dutch edition — hidden until ready, or "coming soon")
├── /contribute         (CONTRIBUTING.md rendered)
└── /404                (helpful 404)
```

Keep `/` as the entry point but make it a true landing page rather than a Docsify
coverpage.

---

## Suggested Homepage Structure

1. **Hero:** Title + subtitle + one-sentence promise + primary CTA ("Start reading") +
   secondary CTA ("For publishers" / "For educators").
2. **Social proof:** Endorsements, download/reader counts, or institutional logos (when
   available).
3. **What you'll learn:** 3–4 concrete takeaways tied to the book's themes (agency,
   conscious delegation, governance, staying human).
4. **Audience paths:** Cards for readers, teachers, professionals, policymakers,
   publishers.
5. **Sample content:** Link to Author's Note + Chapter 1.
6. **Trust/author block:** Author bio + photo + contact/newsletter.
7. **Open-source note:** Contribute, critique, remix.

---

## Suggested CTAs

- Primary: **"Read the book"** / **"Start with Chapter 1"**
- Secondary: **"Download sample for publishers"** / **"Media kit"**
- Secondary: **"Use in class"** / **"Teaching guide"**
- Tertiary: **"View on GitHub"** / **"Contribute"**
- Newsletter: **"Get the delegation newsletter"** (if list exists)

---

## Suggested Backlog Items

- **BL-012:** Scrub canonical manuscript of visible `* edit:`, `TODO`, and `VERIFY` markup
  before site render.
- **BL-013:** Redesign `/` coverpage as a book landing page with audience paths and
  publisher/media entry points.
- **BL-014:** Add a `/publisher` route and link it from the coverpage.
- **BL-015:** Fix or hide the Dutch (`/nl/`) route until a real translation is ready.
- **BL-016:** Improve 404 page with home link, search, and suggested chapters.
- **BL-017:** Improve sidebar typography (sentence case, less truncation, better mobile
  handling).
- **BL-018:** Add author bio and trust signals to the site.
- **BL-019:** Fix fixed-position language switcher overlap on mobile.
- **BL-020:** Add accessible labels to icon-only links and the language switcher.

---

## Do Not Do Yet

- Do **not** add animations, gradients, or decorative effects before the message and
  structure are clear.
- Do **not** commission a full visual rebrand before the manuscript markup is cleaned.
- Do **not** add a paywall, store, or donation flow before publisher positioning is
  decided.
- Do **not** rewrite the manuscript voice in this slice; only remove editorial scaffolding.
- Do **not** delete the `nl/` route without a user decision; hide or clearly deprecate it.

---

## Acceptance Criteria for the Next Implementation Slice

The next slice should be one of the following, with direct browser verification:

1. **Manuscript cleanup slice:**
   - No visible `* edit:` strings in rendered Author's Note or Chapter 1.
   - `python3 scripts/check_state_docs.py` still passes.
   - Evidence: screenshot of cleaned book page.

2. **Homepage redesign slice:**
   - Coverpage contains title, subtitle, promise, audience paths, and publisher/media CTAs.
   - Mobile coverpage screenshot shows readable stacked CTAs.
   - Evidence: desktop + mobile screenshots.

3. **Dutch route decision slice:**
   - Either `/nl/` renders a real Dutch translation or a clear "coming soon" page.
   - No unstyled buttons or English body copy on the Dutch route.
   - Evidence: screenshot of resolved Dutch route.

---

## Method Notes

- **Local server:** `npx docsify serve . --port 3456`
- **WebBridge coverage:** coverpage, book page, chapter navigation, search, sidebar, NL
  route, 404 route, public live site.
- **Playwright usage:** Used only for mobile viewport screenshots (390 × 844) because Kimi
  WebBridge cannot resize the user's browser window programmatically. WebBridge was used
  for all interactive inspection and desktop screenshots.
- **Mobile limitation:** True touch interactions, device fonts, and performance were not
  tested on a physical device; findings are based on emulated viewport and CSS inspection.

---

## Audit Verdict

The site is **functional but not yet launch-ready as a book landing page**. Clean the
manuscript, fix the Dutch route, and redesign the homepage as the next three slices.
