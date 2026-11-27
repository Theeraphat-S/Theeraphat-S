"""Build every static pixel-art SVG used by README.md.

Run from the repository root:

    python .github/scripts/build_pixel_assets.py

pixel-stats.svg is not built here; update_pixel_stats.py regenerates it daily.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import pixel_art as art
from pixel_svg import (
    PALETTE,
    render_pixel_text,
    render_rpg_window,
    render_sprite,
    text_width,
    wrap_svg,
)

P = PALETTE
DARK = P["border_dark"]

BLINK_CSS = """
    @keyframes blink {
      0%, 49% { opacity: 1; }
      50%, 100% { opacity: 0.15; }
    }"""


def text(s: str, x: int, y: int, color: str, font: str = "5x7", scale: int = 1, shadow: bool = False) -> str:
    return render_pixel_text(
        s, x, y, color, scale=scale, spacing=1, font=font,
        shadow_color=DARK if shadow else None, shadow_dx=scale, shadow_dy=scale,
    )


def rect(x: int, y: int, w: int, h: int, fill: str, extra: str = "") -> str:
    extra = f" {extra}" if extra else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{extra}/>'


# ---------------------------------------------------------------------------
# Hero banner
# ---------------------------------------------------------------------------

HERO_FACTS = [
    # (label, label color, value) — keep these factual; they are what visitors read.
    ("SHIPPED", P["emerald_hi"], "PINTO SUPER APP"),
    ("BUILT", P["cyan"], "NCD SCREENING APP"),
    ("STACK", P["gold_hi"], "FLUTTER / GO / SPRING"),
]


def build_hero() -> str:
    parts = [
        render_rpg_window(2, 2, 102, 88, fill="#0c1222"),
        render_rpg_window(108, 2, 170, 88),
        art.HERO_SCENE,
        text("PLAYER // OVEN", 115, 8, P["gold_hi"], font="4x6"),
        rect(225, 7, 46, 8, P["bg_slot"]),
        rect(228, 9, 3, 4, P["emerald"], 'class="blink"'),
        text("ONLINE", 235, 8, P["emerald_hi"], font="4x6"),
        text("THEERAPHAT", 115, 18, P["text_hi"], scale=2, shadow=True),
        text("SRIMONTHA", 115, 35, P["border_corner"], shadow=True),
        text("// @THEERAPHAT-S", 173, 35, P["text_dim"]),
        rect(115, 45, 156, 10, P["bg_slot"]),
        rect(115, 45, 2, 10, P["cyan"]),
        text("CLASS: MOBILE & SUPER-APP ENG", 120, 47, P["cyan"], font="4x6"),
    ]
    for i, (label, color, value) in enumerate(HERO_FACTS):
        y = 58 + i * 7
        parts.append(rect(115, y + 1, 3, 3, color))
        parts.append(text(label, 121, y, color, font="4x6"))
        if 160 + text_width(value, font="4x6") > 271:
            raise ValueError(f"hero fact too wide: {value}")
        parts.append(text(value, 160, y, P["text_hi"], font="4x6"))
    prompt = "> READY TO BUILD NEXT QUEST"
    parts += [
        rect(115, 79, 156, 1, P["grid_line"]),
        text(prompt, 115, 81, P["text_hi"], font="4x6"),
        rect(115 + text_width(prompt, font="4x6") + 3, 81, 3, 6, P["cyan"], 'class="blink"'),
    ]
    styles = BLINK_CSS + """
    @keyframes twinkleA { 0%, 100% { opacity: 1; } 50% { opacity: 0.25; } }
    @keyframes twinkleB { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
    @keyframes steamRise {
      0%, 100% { transform: translateY(0px); opacity: 0.75; }
      50% { transform: translateY(-2px); opacity: 0.25; }
    }
    @keyframes devBob { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(1px); } }
    .cursor, .blink, .beacon { animation: blink 1.1s steps(1, end) infinite; }
    .twinkle-a, .pulse-cyan { animation: twinkleA 2.6s steps(2, end) infinite; }
    .twinkle-b, .pulse-green { animation: twinkleB 3.1s steps(2, end) infinite; }
    .steam-a { animation: steamRise 2.2s steps(2, end) infinite; }
    .steam-b { animation: steamRise 2.2s steps(2, end) infinite 1.1s; }
    .dev-bob { animation: devBob 1.8s steps(1, end) infinite; }
    @media (prefers-reduced-motion: reduce) {
      .cursor, .blink, .beacon, .twinkle-a, .twinkle-b, .pulse-cyan, .pulse-green,
      .steam-a, .steam-b, .dev-bob { animation: none; }
    }"""
    return wrap_svg(
        280, 92, 3,
        "Theeraphat Srimontha (Oven) — Mobile & Super-App Engineer",
        "Pixel hero banner: a developer coding at night beside an RPG status panel listing "
        "shipped work (Pinto super app, NCD screening app) and stack (Flutter, Go, Spring).",
        "\n  ".join(parts), styles,
    )


# ---------------------------------------------------------------------------
# Footer and divider
# ---------------------------------------------------------------------------

def build_footer() -> str:
    line2 = "THANKS FOR VISITING - SAY HELLO"
    parts = [
        render_rpg_window(2, 2, 276, 46, fill="#0b1121"),
        art.FOOTER_SCENE,
        render_rpg_window(84, 8, 186, 34, fill=P["bg_inner"], hi=P["cyan"], with_rivets=False),
        text("SAVE POINT // LET'S BUILD", 92, 15, P["gold_hi"], shadow=True),
        text(line2, 92, 27, P["text_mid"], font="4x6"),
        rect(92 + text_width(line2) + 3, 27, 3, 6, P["cyan"], 'class="blink"'),
    ]
    styles = BLINK_CSS + """
    @keyframes floatGem { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-2px); } }
    @keyframes fireGlow { 0%, 100% { opacity: 1; } 50% { opacity: 0.78; } }
    .float-gem { animation: floatGem 2.4s steps(2, end) infinite; }
    .fire, .tw-a { animation: fireGlow 1.6s steps(2, end) infinite; }
    .tw-b { animation: fireGlow 2.3s steps(2, end) infinite 0.7s; }
    .blink { animation: blink 1.1s steps(1, end) infinite; }
    @media (prefers-reduced-motion: reduce) {
      .float-gem, .fire, .tw-a, .tw-b, .blink { animation: none; }
    }"""
    return wrap_svg(
        280, 50, 3, "Save Point — thanks for visiting",
        "Pixel save-point banner: thanks for visiting, say hello.",
        "\n  ".join(parts), styles,
    )


def build_divider() -> str:
    gem_outer = ["...A...", "..A.A..", ".A...A.", "A.....A", ".A...A.", "..A.A..", "...A..."]
    gem_inner = [".......", "...B...", "..B.B..", ".BB.BB.", "..B.B..", "...B...", "......."]
    gem_core = [".......", ".......", "...C...", "...C...", "...C...", ".......", "......."]
    parts = [
        rect(6, 3, 122, 1, P["grid_line"]),
        rect(152, 3, 122, 1, P["grid_line"]),
        rect(24, 3, 84, 1, P["border_mid"]),
        rect(172, 3, 84, 1, P["border_mid"]),
        rect(116, 3, 12, 1, P["blue"]),
        rect(152, 3, 12, 1, P["blue"]),
        render_sprite(gem_outer, {"A": P["blue"]}, 136, 0),
        render_sprite(gem_inner, {"B": P["cyan"]}, 136, 0),
        render_sprite(gem_core, {"C": P["text_hi"]}, 136, 0),
    ]
    return wrap_svg(280, 7, 3, "Section divider", "Pixel section divider with a crystal.", "\n  ".join(parts))


# ---------------------------------------------------------------------------
# Heading icons
# ---------------------------------------------------------------------------

def build_icon(title: str, grid: list[str], palette: dict[str, str]) -> str:
    return wrap_svg(16, 16, 2, title, f"16x16 pixel icon: {title}", render_sprite(grid, palette))


# ---------------------------------------------------------------------------
# Buttons
# ---------------------------------------------------------------------------

def build_button(
    label: str, title: str, glyph: list[str], glyph_pal: dict[str, str],
    mid: str, hi: str, fill: str, width: int | None = None,
) -> str:
    """15px-tall pixel button; text is 4x6 with a 1px drop shadow and 6px side padding."""
    gw = len(glyph[0])
    tw = text_width(label, font="4x6")
    content = gw + 4 + tw
    pad = 7
    w = width or content + 2 * pad
    if content + 2 * pad > w:
        raise ValueError(f"button label {label!r} needs {content + 2 * pad}px, has {w}px")
    gx = (w - content) // 2
    tx = gx + gw + 4
    parts = [
        render_rpg_window(0, 0, w, 15, fill=fill, outer=DARK, hi=hi, mid=mid, with_rivets=False),
        render_sprite(glyph, glyph_pal, gx, 4),
        text(label, tx, 5, P["text_hi"], font="4x6", shadow=True),
    ]
    return wrap_svg(w, 15, 2, title, f"Pixel button: {label}", "\n  ".join(parts))


# ---------------------------------------------------------------------------
# Project cards
# ---------------------------------------------------------------------------

def build_pinto_card() -> str:
    """48x48 grid shown at 2x (96px): green quest frame around the pixelated Pinto logo."""
    parts = [
        render_rpg_window(0, 0, 48, 48, fill=art.PINTO_LOGO_PALETTE["D"], mid=P["emerald_dark"],
                          hi=P["emerald_hi"], corner=P["gold_hi"]),
        render_sprite(art.PINTO_LOGO, art.PINTO_LOGO_PALETTE, 4, 4),
    ]
    return wrap_svg(48, 48, 2, "Pinto App", "Pinto App logo in a pixel quest frame.", "\n  ".join(parts))


def build_ncd_card() -> str:
    """32x32 grid shown at 3x (96px): heart with an EKG trace."""
    heart_px = {(7 + c, 7 + r) for r, row in enumerate(art.HEART) for c, ch in enumerate(row) if ch == "C" or ch == "D"}
    inside = [(x, y) for x, y in art.EKG_TRACE if (x, y) in heart_px]
    outside = [(x, y) for x, y in art.EKG_TRACE if (x, y) not in heart_px]

    def dots(points: list[tuple[int, int]], color: str) -> str:
        d = "".join(f"M{x} {y}h1v1h-1z" for x, y in points)
        return f'<path d="{d}" fill="{color}"/>'

    parts = [
        render_rpg_window(0, 0, 32, 32, fill=P["bg_panel"], mid="#4c1d3d", hi=P["rose_hi"], corner=P["gold_hi"]),
        render_sprite(art.HEART, art.HEART_PALETTE, 7, 7),
        dots(outside, P["cyan"]),
        dots(inside, P["text_hi"]),
        render_sprite(art.GLYPH_PLUS, art.GLYPH_PLUS_PALETTE, 23, 23),
    ]
    return wrap_svg(32, 32, 3, "NCD Screening", "Pixel heart with an EKG trace for NCD Screening.", "\n  ".join(parts))


# ---------------------------------------------------------------------------
# Skill tree (core stack)
# ---------------------------------------------------------------------------

CORE_STACK = [
    # (title, glyph, glyph palette, accent, accent dark, [(tech, what it is used for)])
    ("MOBILE CLIENT", art.GLYPH_PHONE, art.GLYPH_PHONE_PALETTE, P["cyan"], P["blue_dark"],
     [("FLUTTER", "IOS + ANDROID"), ("DART", "APP LOGIC")]),
    ("BACKEND CORE", art.GLYPH_LEAF, art.GLYPH_LEAF_PALETTE, P["emerald_hi"], P["emerald_dark"],
     [("GO", "MICROSERVICES"), ("SPRING BOOT", "BACKEND APIS")]),
    ("CLOUD & DATA", art.GLYPH_DB, art.GLYPH_DB_PALETTE, P["gold_hi"], P["gold_dark"],
     [("SUPABASE", "SQL + AUTH"), ("FIREBASE", "APP SERVICES")]),
]


def build_skill_tree() -> str:
    h = 86
    parts = [
        render_rpg_window(2, 2, 276, h - 4),
        text("EQUIPPED CORE STACK", 10, 8, P["cyan"], shadow=True),
    ]
    right = "PRODUCTION LOADOUT"
    parts.append(text(right, 271 - text_width(right, font="4x6"), 9, P["text_dim"], font="4x6"))
    parts.append(rect(9, 18, 262, 1, P["grid_line"]))

    for i, (title, glyph, gpal, accent, accent_dark, items) in enumerate(CORE_STACK):
        x = 9 + i * 89
        parts.append(render_rpg_window(x, 22, 84, 56, fill=P["bg_inner"], hi=accent, mid=accent_dark, with_rivets=False))
        parts.append(render_sprite(glyph, gpal, x + 6, 28))
        parts.append(text(title, x + 6 + len(glyph[0]) + 3, 29, accent, font="4x6"))
        parts.append(rect(x + 6, 38, 72, 1, P["grid_line"]))
        for j, (tech, role) in enumerate(items):
            y = 42 + j * 17
            if text_width(tech) > 66 or text_width(role, font="4x6") > 66:
                raise ValueError(f"skill tree text too wide: {tech} / {role}")
            parts.append(rect(x + 6, y + 2, 3, 3, accent))
            parts.append(text(tech, x + 12, y, P["text_hi"]))
            parts.append(text(role, x + 12, y + 9, P["text_mid"], font="4x6"))
    return wrap_svg(
        280, h, 3, "Core Stack Skill Tree",
        "Core technologies: Flutter and Dart for mobile, Go and Spring Boot for backend services, "
        "Supabase and Firebase for cloud and data.",
        "\n  ".join(parts),
    )


# ---------------------------------------------------------------------------
# Full inventory
# ---------------------------------------------------------------------------

INVENTORY = [
    ("LANGUAGES", P["cyan"], ["DART", "TYPESCRIPT", "JAVASCRIPT", "GO", "JAVA", "KOTLIN",
                              "PYTHON", "C++", "C", "C#", "RUBY", "BASH"]),
    ("FRONTEND & CROSS-PLATFORM", P["blue"], ["FLUTTER", "REACT", "VUE", "TAURI", "WORDPRESS", "HTML", "CSS"]),
    ("BACKEND, CLOUD & DB", P["emerald_hi"], ["NODE.JS", "SPRING", "FIREBASE", "DOCKER", "CLOUDFLARE", "AZURE",
                                              "POSTGRESQL", "SUPABASE", "MYSQL", "SQLITE"]),
    ("TOOLS, ENGINES & CREATIVE", P["gold_hi"], ["GIT", "GITHUB", "GITLAB", "BITBUCKET", "VS CODE",
                                                 "VISUAL STUDIO", "ANDROID STUDIO", "ECLIPSE", "POSTMAN",
                                                 "SWAGGER", "CMAKE", "UBUNTU", "WINDOWS", "UNITY", "GODOT",
                                                 "ROBLOX STUDIO", "FIGMA", "PHOTOSHOP", "PREMIERE PRO",
                                                 "AFTER EFFECTS"]),
]


BADGE_MASKS = {
    "square": lambda w: ["." + "A" * (w - 2) + "."] + ["A" * w] * 5 + ["." + "A" * (w - 2) + "."],
    "circle": lambda w: ["..AAA..", ".AAAAA.", "AAAAAAA", "AAAAAAA", "AAAAAAA", ".AAAAA.", "..AAA.."],
}


def tech_icon(name: str) -> tuple[list[str], dict[str, str]]:
    """Return a 7px-tall sprite and palette for an inventory item (see pixel_art.TECH_ICONS)."""
    spec = art.TECH_ICONS[name]
    if spec[0] == "sprite":
        return spec[1], spec[2]
    _, letters, shape, bg, fg = spec
    if shape == "circle" and len(letters) != 1:
        raise ValueError(f"circle badge {name!r} fits one letter")
    w = 7 if len(letters) == 1 else 9
    grid = [list(row) for row in BADGE_MASKS[shape](w)]
    starts = [2] if len(letters) == 1 else [1, 5]
    for ch, sx in zip(letters, starts):
        for r, bits in enumerate(art.MINI_FONT[ch]):
            for c, bit in enumerate(bits):
                if bit == "1":
                    grid[1 + r][sx + c] = "B"
    return ["".join(row) for row in grid], {"A": bg, "B": fg}


def build_inventory() -> str:
    chip_h, row_pitch, gap, left, right = 12, 14, 3, 9, 271
    body: list[str] = [
        text("FULL INVENTORY // ALL TOOLS & STACKS", 10, 8, P["gold_hi"], shadow=True),
        rect(9, 18, 262, 1, P["grid_line"]),
    ]
    y = 22
    for label, accent, items in INVENTORY:
        body.append(rect(9, y, 2, 6, accent))
        body.append(text(label, 14, y, accent, font="4x6"))
        y += 9
        x = left
        for item in items:
            icon, icon_pal = tech_icon(item)
            iw = len(icon[0])
            w = 4 + iw + 3 + text_width(item) + 4
            if x + w > right:
                x = left
                y += row_pitch
            body += [
                rect(x, y, w, chip_h, DARK),
                rect(x + 1, y + 1, w - 2, chip_h - 2, P["bg_inner"]),
                rect(x + 1, y + 1, w - 2, 1, accent, 'opacity="0.5"'),
                render_sprite(icon, icon_pal, x + 4, y + 3),
                text(item, x + 4 + iw + 3, y + 3, P["text_hi"]),
            ]
            x += w + gap
        y += row_pitch + 4
    h = y + 3
    parts = [render_rpg_window(2, 2, 276, h - 4)] + body
    return wrap_svg(
        280, h, 3, "Full Inventory — Languages, Frameworks, Databases, Tools, and Engines",
        "Complete technology inventory as pixel item chips, each with a small pixel logo.",
        "\n  ".join(parts),
    )


# ---------------------------------------------------------------------------

def build_all() -> dict[str, str]:
    return {
        "hero-pixel-banner.svg": build_hero(),
        "pixel-footer.svg": build_footer(),
        "pixel-divider.svg": build_divider(),
        "pixel-icon-quests.svg": build_icon("Quest Log", art.ICON_QUESTS, art.ICON_QUESTS_PALETTE),
        "pixel-icon-skills.svg": build_icon("Skill Tree", art.ICON_SKILLS, art.ICON_SKILLS_PALETTE),
        "pixel-icon-stats.svg": build_icon("Player Stats", art.ICON_STATS, art.ICON_STATS_PALETTE),
        "pixel-icon-snake.svg": build_icon("Contribution Snake", art.ICON_SNAKE, art.ICON_SNAKE_PALETTE),
        "btn-google-play.svg": build_button("GOOGLE PLAY", "Google Play", art.GLYPH_PLAY, art.GLYPH_PLAY_PALETTE,
                                           P["emerald_dark"], P["emerald_hi"], "#112822", width=94),
        "btn-app-store.svg": build_button("APP STORE", "App Store", art.GLYPH_APPLE, art.GLYPH_APPLE_PALETTE,
                                          P["blue_dark"], P["cyan"], "#111d36", width=94),
        "btn-srs-pdf.svg": build_button("SRS DOC (PDF)", "SRS document (PDF)", art.GLYPH_DOC, art.GLYPH_DOC_PALETTE,
                                        "#5e1b3c", P["rose_hi"], "#261325", width=94),
        "btn-email.svg": build_button("EMAIL: THEERAPHAT.SM@GMAIL.COM", "Email Theeraphat Srimontha",
                                      art.GLYPH_MAIL, art.GLYPH_MAIL_PALETTE, "#784f12", P["gold_hi"], P["bg_inner"]),
        "pixel-pinto-card.svg": build_pinto_card(),
        "pixel-ncd-card.svg": build_ncd_card(),
        "pixel-skill-tree.svg": build_skill_tree(),
        "pixel-inventory.svg": build_inventory(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build static pixel-art SVG assets.")
    parser.add_argument("--out-dir", default=str(SCRIPT_DIR.parent.parent / "assets"))
    args = parser.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, svg in build_all().items():
        (out / name).write_text(svg, encoding="utf-8", newline="\n")
        print(f"wrote {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
