"""Builds www/index.html: the game page with both images embedded.

Run from the repo root:  python3 tools/build.py
Edit src/index.template.html (game code and styling) or swap the images in assets/, then run this.
"""
import base64
from pathlib import Path

root = Path(__file__).resolve().parent.parent


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode((root / path).read_bytes()).decode()


html = (root / "src" / "index.template.html").read_text(encoding="utf-8")
html = html.replace("__ENV__", data_uri("assets/env.jpg", "image/jpeg"))
html = html.replace("__TARGET__", data_uri("assets/target.png", "image/png"))

out = root / "www" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")
