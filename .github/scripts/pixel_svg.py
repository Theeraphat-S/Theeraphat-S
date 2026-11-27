"""Shared 16-bit pixel art SVG renderer with crisp bitmap fonts and RPG frames."""

from __future__ import annotations

from html import escape
from typing import Iterable


PALETTE = {
    "canvas": "#0d1117",
    "bg_deep": "#0b1020",
    "bg_panel": "#12182b",
    "bg_inner": "#18213a",
    "bg_slot": "#0f1526",
    "border_dark": "#050811",
    "border_mid": "#2b4570",
    "border_hi": "#58a6ff",
    "border_corner": "#93c5fd",
    "grid_line": "#223052",
    "text_hi": "#f0f6fc",
    "text_mid": "#a9bbd8",
    "text_dim": "#63779c",
    "cyan": "#38bdf8",
    "blue": "#58a6ff",
    "blue_dark": "#1f6feb",
    "emerald": "#3fb950",
    "emerald_hi": "#7ee787",
    "emerald_dark": "#164e2b",
    "gold": "#f59e0b",
    "gold_hi": "#fcd34d",
    "gold_dark": "#5c3908",
    "rose": "#f43f5e",
    "rose_hi": "#fb7185",
    "violet": "#a78bfa",
    "violet_dark": "#3b2c6b",
}


# Fixed-width 5x7 bitmap font for headings, big titles, and numbers
FONT_5X7: dict[str, list[str]] = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01111", "10000", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["01110", "00100", "00100", "00100", "00100", "00100", "01110"],
    "J": ["00111", "00010", "00010", "00010", "10010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10101", "10011", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "Q": ["01110", "10001", "10001", "10001", "10101", "10010", "01101"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "01010", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    "X": ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "Z": ["11111", "00001", "00010", "00100", "01000", "10000", "11111"],
    "0": ["01110", "10001", "10011", "10101", "11001", "10001", "01110"],
    "1": ["00100", "01100", "00100", "00100", "00100", "00100", "01110"],
    "2": ["01110", "10001", "00001", "00110", "01000", "10000", "11111"],
    "3": ["11110", "00001", "00001", "01110", "00001", "00001", "11110"],
    "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
    "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
    "6": ["01110", "10000", "10000", "11110", "10001", "10001", "01110"],
    "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
    "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
    "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"],
    " ": ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
    ".": ["00000", "00000", "00000", "00000", "00000", "01100", "01100"],
    ",": ["00000", "00000", "00000", "00000", "00000", "00100", "01000"],
    ":": ["00000", "01100", "01100", "00000", "01100", "01100", "00000"],
    ";": ["00000", "01100", "01100", "00000", "01100", "00100", "01000"],
    "-": ["00000", "00000", "00000", "11110", "00000", "00000", "00000"],
    "_": ["00000", "00000", "00000", "00000", "00000", "00000", "11111"],
    "+": ["00000", "00100", "00100", "11111", "00100", "00100", "00000"],
    "/": ["00001", "00010", "00010", "00100", "01000", "01000", "10000"],
    "!": ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    "?": ["01110", "10001", "00001", "00110", "00100", "00000", "00100"],
    "@": ["01110", "10001", "10111", "10101", "10110", "10000", "01111"],
    "#": ["01010", "11111", "01010", "01010", "11111", "01010", "00000"],
    "%": ["11001", "11010", "00010", "00100", "01000", "01011", "10011"],
    "&": ["01100", "10010", "10100", "01000", "10101", "10010", "01101"],
    "(": ["00010", "00100", "01000", "01000", "01000", "00100", "00010"],
    ")": ["01000", "00100", "00010", "00010", "00010", "00100", "01000"],
    "[": ["01110", "01000", "01000", "01000", "01000", "01000", "01110"],
    "]": ["01110", "00010", "00010", "00010", "00010", "00010", "01110"],
    ">": ["10000", "01000", "00100", "00010", "00100", "01000", "10000"],
    "<": ["00001", "00010", "00100", "01000", "00100", "00010", "00001"],
    "=": ["00000", "00000", "11111", "00000", "11111", "00000", "00000"],
    "'": ["00100", "00100", "00000", "00000", "00000", "00000", "00000"],
    "*": ["00000", "10101", "01110", "11111", "01110", "10101", "00000"],
    "^": ["00100", "01010", "10001", "00000", "00000", "00000", "00000"],
}


# Proportional 6px-tall crisp pixel font (4px standard, 5px M/W/@/%, 1-3px narrow punctuation)
FONT_4X6: dict[str, list[str]] = {
    "A": ["0110", "1001", "1001", "1111", "1001", "1001"],
    "B": ["1110", "1001", "1110", "1001", "1001", "1110"],
    "C": ["0111", "1000", "1000", "1000", "1000", "0111"],
    "D": ["1110", "1001", "1001", "1001", "1001", "1110"],
    "E": ["1111", "1000", "1110", "1000", "1000", "1111"],
    "F": ["1111", "1000", "1110", "1000", "1000", "1000"],
    "G": ["0111", "1000", "1011", "1001", "1001", "0111"],
    "H": ["1001", "1001", "1111", "1001", "1001", "1001"],
    "I": ["111", "010", "010", "010", "010", "111"],
    "J": ["0011", "0001", "0001", "1001", "1001", "0110"],
    "K": ["1001", "1010", "1100", "1010", "1001", "1001"],
    "L": ["1000", "1000", "1000", "1000", "1000", "1111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001"],
    "N": ["1001", "1101", "1011", "1001", "1001", "1001"],
    "O": ["0110", "1001", "1001", "1001", "1001", "0110"],
    "P": ["1110", "1001", "1001", "1110", "1000", "1000"],
    "Q": ["0110", "1001", "1001", "1011", "1010", "0101"],
    "R": ["1110", "1001", "1001", "1110", "1010", "1001"],
    "S": ["0111", "1000", "0110", "0001", "0001", "1110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100"],
    "U": ["1001", "1001", "1001", "1001", "1001", "0110"],
    "V": ["1001", "1001", "1001", "1001", "0110", "0110"],
    "W": ["10001", "10001", "10101", "10101", "11011", "10001"],
    "X": ["1001", "1001", "0110", "0110", "1001", "1001"],
    "Y": ["1001", "1001", "0110", "0010", "0010", "0010"],
    "Z": ["1111", "0001", "0010", "0100", "1000", "1111"],
    "0": ["0110", "1001", "1011", "1101", "1001", "0110"],
    "1": ["010", "110", "010", "010", "010", "111"],
    "2": ["0110", "1001", "0010", "0100", "1000", "1111"],
    "3": ["1110", "0001", "0110", "0001", "0001", "1110"],
    "4": ["0010", "0110", "1010", "1111", "0010", "0010"],
    "5": ["1111", "1000", "1110", "0001", "0001", "1110"],
    "6": ["0111", "1000", "1110", "1001", "1001", "0110"],
    "7": ["1111", "0001", "0010", "0100", "0100", "0100"],
    "8": ["0110", "1001", "0110", "1001", "1001", "0110"],
    "9": ["0110", "1001", "0111", "0001", "0001", "1110"],
    " ": ["00", "00", "00", "00", "00", "00"],
    ".": ["0", "0", "0", "0", "0", "1"],
    ",": ["00", "00", "00", "00", "01", "10"],
    ":": ["0", "1", "0", "0", "1", "0"],
    "-": ["000", "000", "111", "000", "000", "000"],
    "+": ["000", "010", "111", "010", "000", "000"],
    "/": ["001", "001", "010", "010", "100", "100"],
    "%": ["11001", "11010", "00100", "00100", "01011", "10011"],
    "#": ["01010", "11111", "01010", "11111", "01010", "00000"],
    "&": ["0100", "1010", "0100", "1011", "1001", "0111"],
    "!": ["1", "1", "1", "1", "0", "1"],
    "(": ["01", "10", "10", "10", "10", "01"],
    ")": ["10", "01", "01", "01", "01", "10"],
    "'": ["1", "1", "0", "0", "0", "0"],
    ">": ["100", "010", "001", "010", "100", "000"],
    "@": ["01110", "10001", "10111", "10101", "10000", "01111"],
    "[": ["11", "10", "10", "10", "10", "11"],
    "]": ["11", "01", "01", "01", "01", "11"],
    "_": ["0000", "0000", "0000", "0000", "0000", "1111"],
}


def _glyph_for(ch: str, font: str) -> list[str]:
    if font == "5x7":
        return FONT_5X7.get(ch, FONT_5X7[" "])
    return FONT_4X6.get(ch, FONT_4X6[" "])


def text_width(text: str, scale: int = 1, spacing: int = 1, font: str = "5x7") -> int:
    """Return pixel width of a rendered string in grid units."""
    if not text:
        return 0
    upper = text.upper()
    total = 0
    for idx, ch in enumerate(upper):
        glyph = _glyph_for(ch, font)
        total += len(glyph[0]) * scale
        if idx < len(upper) - 1:
            total += spacing * scale
    return total


def render_pixel_text(
    text: str,
    x: int,
    y: int,
    color: str,
    scale: int = 1,
    spacing: int = 1,
    font: str = "5x7",
    shadow_color: str | None = None,
    shadow_dx: int = 1,
    shadow_dy: int = 1,
    extra_cls: str = "",
) -> str:
    """Render pixel-grid text as merged horizontal SVG path commands."""
    path_cmds: list[str] = []
    upper = text.upper()
    gx = x
    for ch in upper:
        glyph = _glyph_for(ch, font)
        glyph_w = len(glyph[0])
        for row_idx, row in enumerate(glyph):
            col = 0
            while col < glyph_w:
                if row[col] == "1":
                    run = 1
                    while col + run < glyph_w and row[col + run] == "1":
                        run += 1
                    px = gx + col * scale
                    py = y + row_idx * scale
                    pw = run * scale
                    ph = scale
                    path_cmds.append(f"M{px} {py}h{pw}v{ph}h-{pw}z")
                    col += run
                else:
                    col += 1
        gx += (glyph_w + spacing) * scale

    if not path_cmds:
        return ""
    d_attr = "".join(path_cmds)
    cls_attr = f' class="{extra_cls}"' if extra_cls else ""
    out: list[str] = []
    if shadow_color:
        out.append(
            f'<path d="{d_attr}" transform="translate({shadow_dx},{shadow_dy})" '
            f'fill="{shadow_color}" shape-rendering="crispEdges"/>'
        )
    out.append(
        f'<path{cls_attr} d="{d_attr}" fill="{color}" shape-rendering="crispEdges"/>'
    )
    return "\n  ".join(out)


def render_sprite(
    grid: Iterable[str],
    palette: dict[str, str],
    x: int = 0,
    y: int = 0,
    scale: int = 1,
) -> str:
    """Compile an ASCII pixel matrix into merged SVG paths per palette color."""
    cmds_by_color: dict[str, list[str]] = {}
    for row_idx, row in enumerate(grid):
        col = 0
        width = len(row)
        while col < width:
            ch = row[col]
            color = palette.get(ch)
            if not color:
                col += 1
                continue
            run = 1
            while col + run < width and row[col + run] == ch:
                run += 1
            px = x + col * scale
            py = y + row_idx * scale
            pw = run * scale
            ph = scale
            cmds_by_color.setdefault(color, []).append(f"M{px} {py}h{pw}v{ph}h-{pw}z")
            col += run

    paths: list[str] = []
    for color, cmds in cmds_by_color.items():
        paths.append(
            f'<path d="{"".join(cmds)}" fill="{color}" shape-rendering="crispEdges"/>'
        )
    return "\n  ".join(paths)


def render_rpg_window(
    x: int,
    y: int,
    w: int,
    h: int,
    fill: str = PALETTE["bg_panel"],
    outer: str = PALETTE["border_dark"],
    hi: str = PALETTE["border_hi"],
    mid: str = PALETTE["border_mid"],
    corner: str = PALETTE["border_corner"],
    with_rivets: bool = True,
) -> str:
    """Render a classic 16-bit SNES/GBA beveled pixel RPG window frame."""
    rects = [
        f'<rect x="{x+1}" y="{y}" width="{w-2}" height="{h}" fill="{outer}"/>',
        f'<rect x="{x}" y="{y+1}" width="{w}" height="{h-2}" fill="{outer}"/>',
        f'<rect x="{x+1}" y="{y+1}" width="{w-2}" height="{h-2}" fill="{mid}"/>',
        f'<rect x="{x+1}" y="{y+1}" width="{w-3}" height="1" fill="{hi}"/>',
        f'<rect x="{x+1}" y="{y+1}" width="1" height="{h-3}" fill="{hi}"/>',
        f'<rect x="{x+2}" y="{y+2}" width="{w-4}" height="{h-4}" fill="{outer}"/>',
        f'<rect x="{x+3}" y="{y+3}" width="{w-6}" height="{h-6}" fill="{fill}"/>',
    ]
    if with_rivets:
        rects.extend(
            [
                f'<rect x="{x+1}" y="{y+1}" width="2" height="2" fill="{corner}"/>',
                f'<rect x="{x+w-3}" y="{y+1}" width="2" height="2" fill="{corner}"/>',
                f'<rect x="{x+1}" y="{y+h-3}" width="2" height="2" fill="{corner}"/>',
                f'<rect x="{x+w-3}" y="{y+h-3}" width="2" height="2" fill="{corner}"/>',
            ]
        )
    return "\n  ".join(rects)


def render_pixel_bar(
    x: int,
    y: int,
    w: int,
    h: int,
    ratio: float,
    fill: str,
    hi: str,
    track: str = PALETTE["bg_slot"],
    border: str = PALETTE["border_dark"],
    segmented: bool = True,
) -> str:
    """Render a crisp pixel progress/HP/EXP bar with optional segment notches."""
    ratio = max(0.0, min(1.0, ratio))
    inner_w = max(0, w - 2)
    fill_w = max(1 if ratio > 0 else 0, round(inner_w * ratio))
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{border}"/>',
        f'<rect x="{x+1}" y="{y+1}" width="{inner_w}" height="{h-2}" fill="{track}"/>',
    ]
    if fill_w > 0:
        parts.append(
            f'<rect x="{x+1}" y="{y+1}" width="{fill_w}" height="{h-2}" fill="{fill}"/>'
        )
        parts.append(
            f'<rect x="{x+1}" y="{y+1}" width="{fill_w}" height="1" fill="{hi}"/>'
        )
    if segmented and inner_w >= 12:
        for sx in range(x + 5, x + 1 + inner_w - 2, 5):
            parts.append(
                f'<rect x="{sx}" y="{y+1}" width="1" height="{h-2}" fill="{border}" opacity="0.55"/>'
            )
    return "\n  ".join(parts)


def wrap_svg(
    view_w: int,
    view_h: int,
    px_scale: int,
    title: str,
    desc: str,
    body: str,
    styles: str = "",
) -> str:
    """Wrap body elements inside a crisp-edged responsive SVG document."""
    width = view_w * px_scale
    height = view_h * px_scale
    style_block = f"\n  <style>\n{styles}\n  </style>" if styles.strip() else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {view_w} {view_h}" width="{width}" height="{height}" '
        f'shape-rendering="crispEdges" role="img" aria-label="{escape(title)}">\n'
        f"  <title>{escape(title)}</title>\n"
        f"  <desc>{escape(desc)}</desc>{style_block}\n"
        f"  {body}\n"
        f"</svg>\n"
    )
