#!/usr/bin/env python3
"""
Descarga todas las fotos y el video del sitio original (clubelbosque.com.co)
a la carpeta assets/media/ y reescribe los HTML/JS para usarlos localmente.
Así el sitio funciona sin depender del servidor actual.

Uso:  python3 descargar_medios.py
"""
import pathlib, re, urllib.request, urllib.parse

BASE = "https://clubelbosque.com.co/wp-content/uploads/"
ROOT = pathlib.Path(__file__).resolve().parent
DEST = ROOT / "assets" / "media"
files = list(ROOT.glob("*.html")) + [ROOT / "assets/js/main.js"]

pat = re.compile(re.escape(BASE) + r"([0-9]{4}/[0-9]{2}/[^\"'\s)]+)")
urls = set()
for f in files:
    urls.update(pat.findall(f.read_text(encoding="utf-8")))
# imágenes que main.js arma por concatenación (U + "ruta")
js = (ROOT / "assets/js/main.js").read_text(encoding="utf-8")
urls.update(re.findall(r'"(20[0-9]{2}/[0-9]{2}/[^"]+\.(?:jpe?g|png|mp4))"', js))

print(f"{len(urls)} archivos por descargar…")
for rel in sorted(urls):
    out = DEST / urllib.parse.unquote(rel)
    if out.exists():
        continue
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(BASE + rel, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            out.write_bytes(r.read())
        print("  ✓", rel)
    except Exception as e:
        print("  ✗", rel, e)

for f in files:
    t = f.read_text(encoding="utf-8")
    prefix = "../media/" if f.suffix == ".js" else "assets/media/"
    if f.suffix == ".js":
        t = t.replace(f'var U = "{BASE}"', 'var U = "assets/media/"')
    else:
        t = t.replace(BASE, prefix)
    f.write_text(t, encoding="utf-8")
print("Listo: el sitio ahora usa los archivos de assets/media/")
