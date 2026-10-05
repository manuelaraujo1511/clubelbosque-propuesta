# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Proposal/prototype for a new website for Club Campestre El Bosque (Silvania, Cundinamarca). Static site: plain HTML + CSS + vanilla JS, no dependencies, no package manager, no tests, no lint. All content and code comments are in Spanish (`lang="es-CO"`); keep it that way. `LEEME.md` is the client-facing readme.

`propuesta.html` is the sales document (audit of the current site, before/after, roadmap) and is the entry point for presentations. `asociados.html` is a DEMO member portal with fake data.

## Commands

- View: open `index.html` directly in a browser (no server needed). Needs internet — images/video load from `https://clubelbosque.com.co/wp-content/uploads/`.
- Regenerate HTML pages: `python3 _build/build.py` (writes all root `*.html` files).
- Make media local: `python3 descargar_medios.py` — downloads every referenced upload into `assets/media/` and rewrites URLs in root `*.html` and `assets/js/main.js`.

## Architecture

**Root `*.html` files are generated output.** Source lives in `_build/`:
- `build.py` holds the shared `<head>` template (fonts, meta, `noindex`) and footer script tag, and `build(slug, title, desc, body, og, extra_head, body_attr)` which writes `{slug}.html` (`index` → `index.html`).
- `pages.py` lists the pages; each `p_*.py` exports a dict per page (`p_rest.py` holds several small pages and the `hero()`/`card()` helpers).
- In page bodies, `@U/` is a placeholder replaced with the remote uploads base URL.

Edit the `_build/p_*.py` sources, then rebuild — direct edits to root HTML get overwritten by the next build. Caveat: `descargar_medios.py` rewrites only the generated files, not `_build/`, so rebuilding after running it reverts to remote URLs (rerun the download script afterwards).

**Shared chrome is injected at runtime by `assets/js/main.js`**, not present in the HTML: header with mega-menus (`NAV` array), mobile menu, footer, floating WhatsApp button, accessibility panel (state in `localStorage`), mobile bottom bar, and the "propuesta" badge (marked to remove for production). The current page is identified by `<body data-page="slug">`. Navigation/menu changes go in `NAV` in `main.js`. `main.js` also has its own `U` base URL and WhatsApp number `WA`, and wires generic behaviors via classes/data attributes: `.reveal` scroll animations, counters, hero video toggle, tabs, sports filter, venue thumbnails, lightbox, prototype forms (validate + show confirmation only, no backend), portal schedule selection.

**Styles**: single `assets/css/styles.css`, organized by commented sections (tokens, buttons, header, hero, cards, salones, portal, propuesta, responsive, etc.), including a high-contrast accessibility mode.

**Not for indexing**: `robots.txt`, `_headers` (Netlify/Cloudflare-style `X-Robots-Tag`), and the head template all block indexing — this is a proposal, not the live site.

## Pending content (per LEEME.md)

Texts for natación, hospedaje and sauna/turco, current boards (juntas), affiliation fees, and the main WhatsApp number are unvalidated placeholders awaiting the club's confirmation.
