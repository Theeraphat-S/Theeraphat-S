"""Make Platane/snk contribution-snake SVGs match the pixel-art style.

snk draws rounded, anti-aliased cells. This rewrites them in place to square,
crisp-edged pixels: rounded corners are removed and geometricPrecision becomes
crispEdges. Safe to run more than once.

    python .github/scripts/crisp_snake.py assets/github-snake.svg assets/github-snake-dark.svg
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def crispify(svg: str) -> str:
    svg = svg.replace("shape-rendering:geometricPrecision", "shape-rendering:crispEdges")
    svg = re.sub(r'\s(rx|ry)="[^"]*"', "", svg)
    if 'shape-rendering="crispEdges"' not in svg[:300]:
        svg = svg.replace("<svg ", '<svg shape-rendering="crispEdges" ', 1)
    return svg


def main(paths: list[str]) -> int:
    if not paths:
        print("usage: crisp_snake.py SVG [SVG ...]", file=sys.stderr)
        return 2
    for name in paths:
        path = Path(name)
        path.write_text(crispify(path.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        print(f"crisped {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
