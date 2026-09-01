#!/usr/bin/env python3
"""Generate qr.png for every team member from the `aliases:` short link.

For each `content/authors/<slug>/_index.md` that declares
`aliases: ["/flastname"]`, writes `content/authors/<slug>/qr.png`:
a QR code pointing at https://sps-lab.org/flastname with the lab icon in the
centre and the researcher's name + short link underneath.

The short link is derived from the folder name by ONE rule, so every member
gets a uniform link:  drop the dots and hyphens.
    p.-aristidou -> /paristidou      i.v.-nadal -> /ivnadal

Usage (from anywhere):
    python3 content/authors/make_qr.py --add-alias   # insert missing `aliases:` lines
    python3 content/authors/make_qr.py               # write missing qr.png files
    python3 content/authors/make_qr.py --check       # verify aliases follow the rule, no collisions, qr.png present
    python3 content/authors/make_qr.py p.-aristidou m.-jafari   # restrict to selected folders
    python3 content/authors/make_qr.py --force       # regenerate existing qr.png too

Requires: pip install "qrcode[pil]"   (Pillow + qrcode)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont
from qrcode.constants import ERROR_CORRECT_H

HERE = Path(__file__).resolve().parent            # content/authors
ROOT = HERE.parent.parent                          # repo root
ICON = ROOT / "assets" / "media" / "icon.png"      # lab icon (single-colour RGBA)
SITE = "https://sps-lab.org"
SITE_SHORT = "sps-lab.org"

# Brand colours lifted from assets/media/logo.png
NAVY = (27, 54, 93)      # #1B365D  - QR modules + name
TEAL = (0, 127, 163)     # #007FA3  - icon + short link
GREY = (132, 132, 132)   # #848484  - original icon colour (unused, kept for reference)
WHITE = (255, 255, 255)

FONT_BOLD = "/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf"

# Output geometry (px)
W = 1200                  # canvas width
QR_W = 1000               # rendered QR width (incl. quiet zone)
PAD_TOP = 60
GAP_NAME = 40             # QR -> name
GAP_URL = 12              # name -> url
PAD_BOTTOM = 70
NAME_PT = 78
URL_PT = 48
ICON_FRAC = 0.22          # icon plate width as fraction of the QR width (<30% keeps ECC-H happy)


def read_frontmatter(md: Path) -> tuple[str, str] | None:
    """Return (title, alias) from a Hugo YAML frontmatter, or None if no alias."""
    text = md.read_text(encoding="utf-8-sig")  # some files carry a BOM
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    fm = m.group(1)
    title = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
    alias = re.search(r'^aliases:\s*\[\s*["\']?(/[^"\'\s\]]+)["\']?\s*\]', fm, re.M)
    if not (title and alias):
        return None
    return title.group(1).strip(), alias.group(1).strip()


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default(size)  # Pillow >= 10.1


def tinted_icon(size: int) -> Image.Image:
    """The lab icon recoloured to TEAL, using its alpha channel as the mask."""
    icon = Image.open(ICON).convert("RGBA")
    icon.thumbnail((size, size), Image.LANCZOS)
    tint = Image.new("RGBA", icon.size, TEAL + (255,))
    tint.putalpha(icon.getchannel("A"))
    return tint


def fit_text(draw: ImageDraw.ImageDraw, text: str, font_path: str, pt: int, max_w: int) -> ImageFont.FreeTypeFont:
    """Shrink the font until `text` fits in max_w."""
    while pt > 24:
        f = load_font(font_path, pt)
        if draw.textlength(text, font=f) <= max_w:
            return f
        pt -= 4
    return load_font(font_path, pt)


def make_qr(title: str, alias: str, out: Path) -> None:
    url = SITE + alias

    # Integer module size so every module is crisp and equal (resampling a QR
    # to an arbitrary size makes uneven modules that some decoders reject).
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=1, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    n = qr.modules_count + 2 * qr.border
    qr.box_size = max(1, QR_W // n)
    code = qr.make_image(fill_color=NAVY, back_color=WHITE).convert("RGB")
    side = code.width  # <= QR_W

    # Centre plate + icon
    plate = int(side * ICON_FRAC)
    px = (side - plate) // 2
    d = ImageDraw.Draw(code)
    d.rounded_rectangle([px, px, px + plate, px + plate], radius=plate // 6, fill=WHITE)
    icon = tinted_icon(int(plate * 0.78))
    code.paste(icon, (px + (plate - icon.width) // 2, px + (plate - icon.height) // 2), icon)

    # Text block
    tmp = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    name_font = fit_text(tmp, title, FONT_BOLD, NAME_PT, W - 120)
    url_text = SITE_SHORT + alias
    url_font = fit_text(tmp, url_text, FONT_REG, URL_PT, W - 120)
    name_h = name_font.getbbox(title)[3]
    url_h = url_font.getbbox(url_text)[3]

    H = PAD_TOP + QR_W + GAP_NAME + name_h + GAP_URL + url_h + PAD_BOTTOM
    canvas = Image.new("RGB", (W, H), WHITE)
    canvas.paste(code, ((W - side) // 2, PAD_TOP + (QR_W - side) // 2))
    d = ImageDraw.Draw(canvas)
    y = PAD_TOP + QR_W + GAP_NAME
    d.text((W // 2, y), title, font=name_font, fill=NAVY, anchor="ma")
    y += name_h + GAP_URL
    d.text((W // 2, y), url_text, font=url_font, fill=TEAL, anchor="ma")

    out.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out, optimize=True)


def short_alias(folder: str) -> str:
    """The uniform short link for an author folder: `p.-aristidou` -> `/paristidou`."""
    return "/" + re.sub(r"[.\-]", "", folder).lower()


def add_alias(md: Path) -> bool:
    """Insert `aliases: ["/flastname"]` after the title line if the file has none."""
    raw = md.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    if re.search(r"^aliases:", text, re.M):
        return False
    alias = short_alias(md.parent.name)
    block = (f"\n# Short link: {SITE}{alias} (rendered into public/_redirects by the Netlify plugin)\n"
             f'aliases: ["{alias}"]\n')
    new, n = re.subn(r"^(title:[^\n]*\n)", lambda m: m.group(1) + block, text, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"{md}: no `title:` line to anchor the alias on")
    md.write_bytes((b"\xef\xbb\xbf" if bom else b"") + new.encode("utf-8"))
    return True


def check(dirs: list[Path]) -> int:
    """Report aliases that break the rule, collide, or lack a qr.png. Returns problem count."""
    problems = 0
    seen: dict[str, str] = {}
    for d in dirs:
        md = d / "_index.md"
        if not md.is_file():
            continue
        fm = read_frontmatter(md)
        if not fm:
            print(f"MISSING  {d.name}: no `aliases:` (run --add-alias)"); problems += 1; continue
        _, alias = fm
        want = short_alias(d.name)
        if alias != want:
            print(f"DRIFT    {d.name}: alias {alias} but the rule gives {want}"); problems += 1
        if alias in seen:
            print(f"COLLIDE  {d.name}: {alias} already used by {seen[alias]}"); problems += 1
        seen[alias] = d.name
        if not (d / "qr.png").is_file():
            print(f"NO-QR    {d.name}: qr.png missing (run without --check)"); problems += 1
    # Netlify hand-written redirects must not shadow a short link
    toml = ROOT / "netlify.toml"
    if toml.is_file():
        for m in re.finditer(r'^\s*from\s*=\s*"([^"]+)"', toml.read_text(encoding="utf-8"), re.M):
            if m.group(1) in seen:
                print(f"COLLIDE  netlify.toml redirect {m.group(1)} shadows {seen[m.group(1)]}"); problems += 1
    print("check: OK" if not problems else f"check: {problems} problem(s)")
    return problems


def main(argv: list[str]) -> int:
    force = "--force" in argv
    slugs = [a for a in argv if not a.startswith("--")]
    dirs = [HERE / s for s in slugs] if slugs else sorted(p for p in HERE.iterdir() if p.is_dir())

    if "--add-alias" in argv:
        for d in dirs:
            md = d / "_index.md"
            if md.is_file() and add_alias(md):
                print(f"alias  {d.name:<22} {short_alias(d.name)}")
        return 0
    if "--check" in argv:
        return 1 if check(dirs) else 0

    n = 0
    for d in dirs:
        md = d / "_index.md"
        if not md.is_file():
            print(f"skip {d.name}: no _index.md", file=sys.stderr)
            continue
        fm = read_frontmatter(md)
        if not fm:
            print(f"skip {d.name}: no `aliases:` short link in frontmatter", file=sys.stderr)
            continue
        title, alias = fm
        out = d / "qr.png"
        if out.exists() and not force:
            print(f"keep {out.relative_to(ROOT)} (use --force to regenerate)")
            continue
        make_qr(title, alias, out)
        print(f"wrote {out.relative_to(ROOT)}  ->  {SITE}{alias}")
        n += 1
    print(f"{n} QR code(s) written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
