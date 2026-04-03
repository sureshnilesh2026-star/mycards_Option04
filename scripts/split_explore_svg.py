"""Split content-explore-products.svg into heading + banners (Banner Option 2 rail)."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = root / "assets" / "content-explore-products.svg"
heading_out = root / "assets" / "content-explore-products-heading.svg"
banners_out = root / "assets" / "content-explore-products-banners.svg"

lines = src.read_text(encoding="utf-8").splitlines(keepends=True)
assert lines[0].strip().startswith("<svg"), lines[0][:80]
open_tag = lines[0].strip()
# Replace root dimensions for heading fragment
heading_open = open_tag.replace('height="148" viewBox="0 0 427 148"', 'height="22" viewBox="0 0 427 22"')
path_line = lines[1]
heading_svg = heading_open + "\n" + path_line + "</svg>\n"
heading_out.write_text(heading_svg, encoding="utf-8")

# Banners: lines index 2 .. 23 (0-based) are content before <defs>; wrap with translate
body = "".join(lines[2:24])  # through closing </g> of clip2
defs_and_close = "".join(lines[24:])  # <defs>..."</svg>\n"

# After translate(0,-22), banner art spans y≈-34..126+shadow and x past 427 (decor); use inclusive viewBox so nothing is cropped.
banners_open = (
    '<svg width="520" height="180" viewBox="-8 -36 520 180" fill="none" '
    'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n'
    '<g transform="translate(0,-22)">\n'
)
banners_svg = banners_open + body + "</g>\n" + defs_and_close
banners_out.write_text(banners_svg, encoding="utf-8")

print("wrote", heading_out.name, "and", banners_out.name)
