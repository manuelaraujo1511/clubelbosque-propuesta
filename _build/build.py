# Generador de páginas: une la plantilla común con el cuerpo de cada página.
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
U = "https://clubelbosque.com.co/wp-content/uploads/"

HEAD = """<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#12261a">
<meta name="robots" content="noindex, nofollow, noarchive">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="@U/{og}">
<meta property="og:type" content="website">
<link rel="icon" href="@U/2020/08/cropped-icon-512-192x192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
{extra_head}
</head>
<body data-page="{slug}"{body_attr}>
<main id="main">
"""

FOOT = """
</main>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

def build(slug, title, desc, body, og="2020/03/f_entrada-compressor-1.jpg", extra_head="", body_attr=""):
    html = HEAD.format(title=title, desc=desc, og=og, slug=slug, extra_head=extra_head, body_attr=body_attr) + body + FOOT
    html = html.replace("@U/", U)
    out = ROOT / ("index.html" if slug == "index" else f"{slug}.html")
    out.write_text(html, encoding="utf-8")
    print("ok", out.name, len(html))

import pages  # noqa: E402  (define PAGES)
for p in pages.PAGES:
    build(**p)
