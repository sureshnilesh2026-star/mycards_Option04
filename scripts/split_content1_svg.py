from pathlib import Path

root = Path(__file__).resolve().parent.parent / "assets"
src = root / "content1-design.svg"
lines = src.read_text(encoding="utf-8").splitlines(keepends=True)
defs = "".join(lines[101:185])
top_inner = "".join(lines[1:49])
explore_inner = "".join(lines[49:71])
bottom_inner = "".join(lines[71:101])

NS = ' fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"'
top_svg = (
    f'<svg width="436" height="291" viewBox="0 0 436 291"{NS}>\n'
    f"{top_inner}{defs}</svg>\n"
)
explore_svg = (
    f'<svg width="448" height="130" viewBox="0 0 448 130"{NS}>\n'
    f'<g transform="translate(-12 -293)">\n'
    f"{explore_inner}</g>\n"
    f"{defs}</svg>\n"
)
bottom_svg = (
    f'<svg width="436" height="320" viewBox="0 0 436 320"{NS}>\n'
    f'<g transform="translate(0 -443)">\n'
    f"{bottom_inner}</g>\n"
    f"{defs}</svg>\n"
)
(root / "content1-slice-top.svg").write_text(top_svg, encoding="utf-8")
(root / "content1-slice-explore.svg").write_text(explore_svg, encoding="utf-8")
(root / "content1-slice-bottom.svg").write_text(bottom_svg, encoding="utf-8")
print("ok", len(top_svg), len(explore_svg), len(bottom_svg))
