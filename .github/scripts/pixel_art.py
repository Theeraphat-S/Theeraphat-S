"""Pixel art data for build_pixel_assets.py: ASCII sprites and hand-drawn scene fragments.

Sprites are rows of palette keys; "." is transparent. Scene fragments are raw SVG
elements on the hero/footer pixel grid and are pasted into the frame unchanged.
"""

# Pinto App logo, downsampled from the 240px source to a 40x40 grid with 5 colors.
PINTO_LOGO_PALETTE = {"A": "#fffff1", "B": "#e8e8df", "D": "#2ecc71", "E": "#6fb292", "F": "#54817e"}
PINTO_LOGO = [
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDDDDDDDFFDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDDDEFFFFFEEFDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDFEFDDDDDDFBFDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDEFDDDDDDDDEEDFFEFDDDFFFDDDDDDDDDDDD",
    "DDDDDEFEBBBBBEFFFDFAAEDDFAABFDDDDFFDDDDD",
    "DDDDDFFAAAAAAABFBFFAAEDDFAAAFDDDFAAEDDDD",
    "DDDDDBFAAAAAAAABFEFEEFDDEAAABFDDFAAEDDDD",
    "DDDDEEFAABFFEAAAFFDFFDDDEAAAAFDDEAAEDDDD",
    "DDDDFFFAABFDDEAAEFFAAEDDBAAAABFDEAAFDDDD",
    "DDDDDFFAABFDDEAAEDEAAEDFBAABAAEFBAAFDDDD",
    "DDDDDDFAABEEBAAAFDEAAEDFAAAFAAAFAAAFDDDD",
    "DDDDDDFAAAAAAAABFDEAAEDFAABFEAABAAAFDDDD",
    "DDDDDDFAAAAAAAEFDDEAAEDFAABDFAAAAABFDDDD",
    "DDDDDDFAABEEFFDDDDEAAEDEAAEDDEAAAABDDDDD",
    "DDDDDDFAABDDDDDDDDEAAEDEAAEDDFBAAAEDDDDD",
    "DDDDDDFAABDDDDDDDDEAAEDEAAFDDDFAAAEDDDDD",
    "DDDDDDFBBEDDDDDDDDFBBFDFFFDDDDFBAAFDDDDD",
    "DDDDDDDDFDDDDDDDDDDFFDDDDDDDDDDFFFDDDDDD",
    "DDDDDDDDDFFFFFFFEEEFDDDDDDDDDDDDDDDDDDDD",
    "DDDDDFEBBBAAAAAAAAAEDDDDFBBFDDDDDDDDDDDD",
    "DDDDDEAAAAAAAAAAAAAFDDDDDEAABFDDDDDDDDDD",
    "DDDDDFAAAAAAAABEEFFDDDFFFFFBABFDDDDDDDDD",
    "DDDDDDFFFFFAAAEDDDDDFEBAABFFEABFDDDDDDDD",
    "DDDDDDDDDDFBAAEDDDDFBBEEEBAEFEAEDDDDDDDD",
    "DDDDDDDDDDFBAAEDDDFBEFBBBEEBFFBBFDDDDDDD",
    "DDDDDDDDDDDBAABDDDBBEEEEBBEEBFEAFDDDDDDD",
    "DDDDDDDDDDDEAABDDFAEEEEEEEEEAFFBFDDDDDDD",
    "DDDDDDDDDDDEAABFDFBEBBBBEEEEBFDFDDDDDDDD",
    "DDDDDDDDDDDEAAAFDFBFABBEBBBEBFFEFDDDDDDD",
    "DDDDDDDDDDDFAAAFDFBEEBBEBBEEBFFEFDDDDDDD",
    "DDDDDDDDDDDFAAAFDDEAEBFEEEEBEDDDDDDDDDDD",
    "DDDDDDDDDDDFAAAFDDFBBEBEBBABFDDDDDDDDDDD",
    "DDDDDDDDDDDFAAAFDDDFEAAABBEFDDDDDDDDDDDD",
    "DDDDDDDDDDDDFEFDDDDDDFFEFFDDDDDDDDDDDDDD",
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
    "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
]

# Left panel of the hero banner: night city window, desk, developer and cat (280x92 grid).
HERO_SCENE = """
<rect x="5" y="5" width="96" height="82" fill="#10172b"/>
<rect x="13" y="5" width="1" height="53" fill="#141e36"/>
<rect x="25" y="5" width="1" height="53" fill="#141e36"/>
<rect x="37" y="5" width="1" height="53" fill="#141e36"/>
<rect x="49" y="5" width="1" height="53" fill="#141e36"/>
<rect x="61" y="5" width="1" height="53" fill="#141e36"/>
<rect x="73" y="5" width="1" height="53" fill="#141e36"/>
<rect x="85" y="5" width="1" height="53" fill="#141e36"/>
<rect x="97" y="5" width="1" height="53" fill="#141e36"/>
<rect x="9" y="9" width="50" height="32" fill="#050811"/>
<rect x="10" y="10" width="48" height="30" fill="#2b4570"/>
<rect x="11" y="11" width="46" height="28" fill="#080d1c"/>
<rect x="11" y="21" width="46" height="10" fill="#0d152d"/>
<rect x="11" y="31" width="46" height="8" fill="#131f40"/>
<path d="M16 14h2v1h-2zM15 15h2v1h-2zM15 16h2v1h-2zM16 17h2v1h-2z" fill="#fcd34d" shape-rendering="crispEdges"/>
<g class="twinkle-a">
<rect x="26" y="14" width="1" height="1" fill="#e2e8f0"/>
<rect x="39" y="13" width="1" height="1" fill="#e2e8f0"/>
<rect x="51" y="16" width="1" height="1" fill="#e2e8f0"/>
<rect x="32" y="19" width="1" height="1" fill="#e2e8f0"/>
</g>
<g class="twinkle-b">
<rect x="21" y="20" width="1" height="1" fill="#7dd3fc"/>
<rect x="45" y="18" width="1" height="1" fill="#7dd3fc"/>
<rect x="54" y="13" width="1" height="1" fill="#7dd3fc"/>
<rect x="36" y="15" width="1" height="1" fill="#7dd3fc"/>
</g>
<rect x="12" y="27" width="7" height="12" fill="#17254a"/>
<rect x="19" y="23" width="8" height="16" fill="#1e305e"/>
<rect x="27" y="29" width="6" height="10" fill="#152142"/>
<rect x="33" y="21" width="9" height="18" fill="#223668"/>
<rect x="42" y="25" width="7" height="14" fill="#1a2952"/>
<rect x="49" y="28" width="7" height="11" fill="#162347"/>
<rect x="14" y="30" width="1" height="1" fill="#38bdf8"/>
<rect x="16" y="33" width="1" height="1" fill="#fcd34d"/>
<rect x="21" y="26" width="1" height="1" fill="#fcd34d"/>
<rect x="24" y="28" width="1" height="1" fill="#38bdf8"/>
<rect x="22" y="32" width="1" height="1" fill="#38bdf8"/>
<rect x="29" y="32" width="1" height="1" fill="#38bdf8"/>
<rect x="35" y="24" width="1" height="1" fill="#38bdf8"/>
<rect x="38" y="24" width="1" height="1" fill="#fcd34d"/>
<rect x="36" y="28" width="1" height="1" fill="#7ee787"/>
<rect x="39" y="31" width="1" height="1" fill="#38bdf8"/>
<rect x="44" y="28" width="1" height="1" fill="#fcd34d"/>
<rect x="46" y="32" width="1" height="1" fill="#38bdf8"/>
<rect x="51" y="31" width="1" height="1" fill="#38bdf8"/>
<rect x="53" y="34" width="1" height="1" fill="#fcd34d"/>
<rect class="beacon" x="37" y="20" width="1" height="1" fill="#f43f5e"/>
<rect x="33" y="11" width="1" height="28" fill="#1b2b4d" opacity="0.8"/>
<rect x="8" y="40" width="52" height="2" fill="#2b4570"/>
<rect x="8" y="41" width="52" height="1" fill="#18233d"/>
<rect x="68" y="11" width="26" height="15" fill="#060913"/>
<rect x="69" y="12" width="24" height="13" fill="#223052"/>
<rect x="70" y="13" width="22" height="11" fill="#11192e"/>
<path d="M78 15h6v1h-6zM77 16h1v1h-1zM84 16h1v1h-1zM76 17h1v1h-1zM80 17h2v1h-2zM85 17h1v1h-1zM76 18h1v1h-1zM80 18h2v1h-2zM85 18h1v1h-1zM76 19h1v1h-1zM85 19h1v1h-1zM77 20h2v1h-2zM83 20h2v1h-2z" fill="#38bdf8" shape-rendering="crispEdges"/>
<path d="M78 16h6v1h-6zM77 17h1v1h-1zM79 17h1v1h-1zM82 17h1v1h-1zM84 17h1v1h-1zM77 18h3v1h-3zM82 18h3v1h-3zM77 19h1v1h-1zM79 19h1v1h-1z" fill="#e2e8f0" shape-rendering="crispEdges"/>
<path d="M82 19h1v1h-1z" fill="#f43f5e" shape-rendering="crispEdges"/>
<path d="M84 19h1v1h-1z" fill="#3fb950" shape-rendering="crispEdges"/>
<rect x="5" y="58" width="96" height="2" fill="#3a5282"/>
<rect x="5" y="60" width="96" height="4" fill="#212e4d"/>
<rect x="5" y="64" width="96" height="23" fill="#0a0f1d"/>
<rect x="8" y="64" width="90" height="1" fill="#1f6feb" opacity="0.7"/>
<rect x="9" y="66" width="14" height="19" fill="#050811"/>
<rect x="10" y="67" width="12" height="17" fill="#18213a"/>
<rect x="12" y="69" width="8" height="6" fill="#0d1426"/>
<rect class="pulse-cyan" x="13" y="71" width="6" height="1" fill="#38bdf8"/>
<rect class="pulse-green" x="13" y="73" width="4" height="1" fill="#3fb950"/>
<rect x="12" y="78" width="8" height="4" fill="#12182b"/>
<rect x="27" y="53" width="4" height="4" fill="#1e293b"/>
<rect x="23" y="56" width="12" height="2" fill="#334155"/>
<rect x="13" y="34" width="33" height="20" fill="#050811"/>
<rect x="14" y="35" width="31" height="18" fill="#2b4570"/>
<rect x="15" y="36" width="29" height="16" fill="#0c1c36"/>
<rect x="17" y="38" width="8" height="1" fill="#a78bfa"/>
<rect x="17" y="40" width="11" height="1" fill="#38bdf8"/>
<rect x="18" y="42" width="9" height="1" fill="#7ee787"/>
<rect x="18" y="44" width="7" height="1" fill="#fcd34d"/>
<rect x="17" y="46" width="10" height="1" fill="#58a6ff"/>
<rect class="cursor" x="17" y="48" width="3" height="1" fill="#f0f6fc"/>
<rect x="31" y="37" width="10" height="14" fill="#050811"/>
<rect x="32" y="38" width="8" height="12" fill="#162847"/>
<rect x="32" y="38" width="8" height="3" fill="#3fb950"/>
<rect x="33" y="42" width="6" height="2" fill="#38bdf8"/>
<rect x="33" y="45" width="6" height="2" fill="#2b4570"/>
<rect x="33" y="48" width="4" height="1" fill="#fcd34d"/>
<rect x="35" y="56" width="16" height="2" fill="#0f172a"/>
<rect x="36" y="55" width="14" height="1" fill="#38bdf8"/>
<rect x="36" y="57" width="14" height="1" fill="#1f6feb"/>
<path d="M52 51h4v1h-4zM56 52h1v1h-1zM56 53h1v1h-1zM53 54h2v1h-2zM56 54h1v1h-1zM56 55h1v1h-1z" fill="#94a3b8" shape-rendering="crispEdges"/>
<path d="M52 52h4v1h-4z" fill="#92400e" shape-rendering="crispEdges"/>
<path d="M52 53h4v1h-4zM52 54h1v1h-1zM55 54h1v1h-1zM52 55h4v1h-4zM52 56h4v1h-4z" fill="#f0f6fc" shape-rendering="crispEdges"/>
<path d="M52 57h4v1h-4z" fill="#cbd5e1" shape-rendering="crispEdges"/>
<g class="steam-a"><rect x="53" y="48" width="1" height="2" fill="#93c5fd" opacity="0.7"/><rect x="55" y="46" width="1" height="2" fill="#cbd5e1" opacity="0.6"/></g>
<g class="steam-b"><rect x="54" y="45" width="1" height="2" fill="#93c5fd" opacity="0.5"/></g>
<path d="M76 41h5v1h-5zM75 42h2v1h-2zM81 42h1v1h-1zM75 43h2v1h-2zM81 43h1v1h-1zM75 44h2v1h-2zM81 44h1v1h-1zM75 45h2v1h-2zM81 45h1v1h-1zM75 46h2v1h-2zM81 46h1v1h-1zM75 47h2v1h-2zM81 47h1v1h-1zM75 48h2v1h-2zM81 48h1v1h-1zM74 49h3v1h-3zM81 49h1v1h-1zM73 50h2v1h-2zM81 50h1v1h-1zM72 51h2v1h-2zM72 52h9v1h-9zM75 53h4v1h-4zM76 54h2v1h-2zM74 55h6v1h-6z" fill="#050811" shape-rendering="crispEdges"/>
<path d="M77 42h4v1h-4zM77 43h4v1h-4zM77 44h4v1h-4zM77 45h4v1h-4zM77 46h1v1h-1zM80 46h1v1h-1zM77 47h4v1h-4zM77 48h4v1h-4zM77 49h4v1h-4zM75 50h6v1h-6zM74 51h7v1h-7z" fill="#1e293b" shape-rendering="crispEdges"/>
<path d="M78 46h2v1h-2z" fill="#38bdf8" shape-rendering="crispEdges"/>
<g class="dev-bob">
<path d="M66 35h6v1h-6zM64 36h2v1h-2zM72 36h2v1h-2zM63 37h1v1h-1zM74 37h1v1h-1zM63 38h1v1h-1zM74 38h1v1h-1zM62 39h1v1h-1zM75 39h1v1h-1zM62 40h1v1h-1zM62 41h1v1h-1zM62 42h1v1h-1zM63 43h1v1h-1zM74 43h1v1h-1zM64 44h2v1h-2zM72 44h2v1h-2zM63 45h2v1h-2zM73 45h2v1h-2zM62 46h2v1h-2zM74 46h2v1h-2zM61 47h1v1h-1zM75 47h1v1h-1zM61 48h1v1h-1zM75 48h1v1h-1zM61 49h1v1h-1zM75 49h1v1h-1zM60 50h1v1h-1zM75 50h1v1h-1zM61 51h4v1h-4zM74 51h2v1h-2zM64 52h1v1h-1zM74 52h1v1h-1zM64 53h3v1h-3zM71 53h3v1h-3zM65 54h1v1h-1zM72 54h1v1h-1z" fill="#050811" shape-rendering="crispEdges"/>
<path d="M66 36h6v1h-6zM64 37h10v1h-10zM64 38h3v1h-3zM70 38h4v1h-4zM63 39h3v1h-3zM72 39h3v1h-3zM63 40h2v1h-2zM74 40h1v1h-1zM63 41h1v1h-1zM74 41h1v1h-1zM63 42h1v1h-1zM74 42h1v1h-1z" fill="#1e263d" shape-rendering="crispEdges"/>
<path d="M67 38h3v1h-3zM66 39h1v1h-1zM70 39h2v1h-2zM68 41h2v1h-2z" fill="#38bdf8" shape-rendering="crispEdges"/>
<path d="M67 39h3v1h-3z" fill="#93c5fd" shape-rendering="crispEdges"/>
<path d="M65 40h2v1h-2zM71 40h3v1h-3zM64 41h3v1h-3zM70 41h1v1h-1zM73 41h1v1h-1zM64 42h10v1h-10zM64 43h3v1h-3zM70 43h4v1h-4zM66 44h6v1h-6zM61 50h4v1h-4z" fill="#f2c6a0" shape-rendering="crispEdges"/>
<path d="M67 40h4v1h-4zM67 41h1v1h-1zM71 41h2v1h-2z" fill="#7dd3fc" shape-rendering="crispEdges"/>
<path d="M67 43h3v1h-3z" fill="#d49b72" shape-rendering="crispEdges"/>
<path d="M65 45h8v1h-8zM64 46h10v1h-10zM62 47h4v1h-4zM68 47h7v1h-7zM62 48h3v1h-3zM68 48h7v1h-7zM62 49h13v1h-13zM65 50h10v1h-10zM65 51h9v1h-9zM65 52h9v1h-9z" fill="#1f6feb" shape-rendering="crispEdges"/>
<path d="M66 47h2v1h-2zM65 48h3v1h-3z" fill="#58a6ff" shape-rendering="crispEdges"/>
<path d="M67 53h4v1h-4zM66 54h6v1h-6z" fill="#162038" shape-rendering="crispEdges"/>
</g>
<path d="M88 48h1v1h-1zM93 48h1v1h-1zM87 49h1v1h-1zM89 49h1v1h-1zM92 49h1v1h-1zM94 49h1v1h-1zM87 50h1v1h-1zM94 50h1v1h-1zM87 51h1v1h-1zM94 51h1v1h-1zM87 52h1v1h-1zM94 52h1v1h-1zM88 53h1v1h-1zM93 53h1v1h-1zM88 54h1v1h-1zM93 54h1v1h-1zM95 54h1v1h-1zM87 55h1v1h-1zM94 55h2v1h-2zM87 56h1v1h-1zM94 56h1v1h-1zM87 57h1v1h-1zM89 57h1v1h-1zM92 57h1v1h-1zM94 57h1v1h-1z" fill="#050811" shape-rendering="crispEdges"/>
<path d="M88 49h1v1h-1zM93 49h1v1h-1zM88 50h6v1h-6zM88 51h1v1h-1zM90 51h2v1h-2zM93 51h1v1h-1zM88 52h2v1h-2zM91 52h3v1h-3zM89 53h4v1h-4zM89 54h4v1h-4zM88 55h6v1h-6zM88 56h6v1h-6zM88 57h1v1h-1zM93 57h1v1h-1z" fill="#334155" shape-rendering="crispEdges"/>
<path d="M89 51h1v1h-1zM92 51h1v1h-1z" fill="#fcd34d" shape-rendering="crispEdges"/>
<path d="M90 52h1v1h-1z" fill="#fb7185" shape-rendering="crispEdges"/>
"""

# Left half of the footer: city skyline, save crystal and campfire (280x50 grid).
FOOTER_SCENE = """
<rect x="7" y="25" width="7" height="15" fill="#111a33"/>
<rect x="14" y="21" width="9" height="19" fill="#152142"/>
<rect x="36" y="26" width="8" height="14" fill="#111a33"/>
<rect x="56" y="22" width="10" height="18" fill="#162347"/>
<rect x="68" y="27" width="8" height="13" fill="#121b36"/>
<rect x="16" y="25" width="1" height="1" fill="#38bdf8"/>
<rect x="20" y="29" width="1" height="1" fill="#fcd34d"/>
<rect x="59" y="26" width="1" height="1" fill="#38bdf8"/>
<rect x="63" y="30" width="1" height="1" fill="#7ee787"/>
<rect x="71" y="31" width="1" height="1" fill="#fcd34d"/>
<rect class="tw-a" x="10" y="10" width="1" height="1" fill="#93c5fd"/>
<rect class="tw-b" x="28" y="8" width="1" height="1" fill="#93c5fd"/>
<rect class="tw-a" x="44" y="12" width="1" height="1" fill="#93c5fd"/>
<rect class="tw-b" x="62" y="9" width="1" height="1" fill="#93c5fd"/>
<rect class="tw-a" x="75" y="14" width="1" height="1" fill="#93c5fd"/>
<g class="float-gem">
<path d="M23 15h2v1h-2zM22 16h1v1h-1zM25 16h1v1h-1zM21 17h1v1h-1zM26 17h1v1h-1zM20 18h1v1h-1zM27 18h1v1h-1zM20 19h1v1h-1zM27 19h1v1h-1zM21 20h1v1h-1zM26 20h1v1h-1zM22 21h1v1h-1zM25 21h1v1h-1zM23 22h2v1h-2z" fill="#1f6feb" shape-rendering="crispEdges"/>
<path d="M23 16h2v1h-2zM22 17h1v1h-1zM25 17h1v1h-1zM21 18h2v1h-2zM25 18h2v1h-2z" fill="#f0f6fc" shape-rendering="crispEdges"/>
<path d="M23 17h2v1h-2zM23 18h2v1h-2zM21 19h6v1h-6zM22 20h4v1h-4zM23 21h2v1h-2z" fill="#38bdf8" shape-rendering="crispEdges"/>
</g>
<rect x="16" y="31" width="16" height="3" fill="#2b4570"/>
<rect x="18" y="34" width="12" height="5" fill="#18213a"/>
<rect x="7" y="39" width="72" height="6" fill="#12182b"/>
<rect x="7" y="39" width="72" height="1" fill="#38bdf8" opacity="0.6"/>
<g class="fire">
<path d="M50 33h2v1h-2zM49 34h1v1h-1zM52 34h1v1h-1zM48 35h1v1h-1zM53 35h1v1h-1zM47 36h1v1h-1zM50 36h2v1h-2zM54 36h1v1h-1z" fill="#fcd34d" shape-rendering="crispEdges"/>
<path d="M50 34h2v1h-2zM50 35h2v1h-2z" fill="#fffbeb" shape-rendering="crispEdges"/>
<path d="M49 35h1v1h-1zM52 35h1v1h-1zM48 36h2v1h-2zM52 36h2v1h-2zM48 37h2v1h-2zM52 37h2v1h-2z" fill="#f59e0b" shape-rendering="crispEdges"/>
<path d="M50 37h2v1h-2z" fill="#f43f5e" shape-rendering="crispEdges"/>
<path d="M47 38h8v1h-8z" fill="#78350f" shape-rendering="crispEdges"/>
</g>
<rect x="69" y="24" width="1" height="15" fill="#475569"/>
<rect x="66" y="24" width="4" height="1" fill="#475569"/>
<rect class="fire" x="65" y="25" width="3" height="3" fill="#fcd34d"/>
"""

# ---------------------------------------------------------------------------
# 16x16 section heading icons (rendered at 2x = 32px in the README).
# ---------------------------------------------------------------------------

ICON_QUESTS_PALETTE = {"A": "#f59e0b", "C": "#fcd34d", "B": "#fde68a", "D": "#5c3908", "R": "#f43f5e"}
ICON_QUESTS = [  # quest scroll with a red "!" marker
    "................",
    ".AAAAAAAAAAAAAA.",
    "ACCCCCCCCCCCCCCA",
    ".AAAAAAAAAAAAAA.",
    "..ABBBBBBBBBBA..",
    "..ABDDDDBBRRBA..",
    "..ABBBBBBBRRBA..",
    "..ABDDDDDBRRBA..",
    "..ABBBBBBBRRBA..",
    "..ABDDDDBBBBBA..",
    "..ABBBBBBBRRBA..",
    "..ABDDDDDBBBBA..",
    "..ABBBBBBBBBBA..",
    ".AAAAAAAAAAAAAA.",
    "ACCCCCCCCCCCCCCA",
    ".AAAAAAAAAAAAAA.",
]

ICON_SKILLS_PALETTE = {"A": "#1f6feb", "B": "#f0f6fc", "C": "#38bdf8", "D": "#58a6ff", "E": "#f59e0b", "F": "#fcd34d"}
ICON_SKILLS = [  # gem on a gold ring
    "................",
    ".......AA.......",
    "......ABBA......",
    ".....ACCCCD.....",
    "....ACBBBBCD....",
    "...ACBCCCCBCD...",
    "...ACBCCCCBCD...",
    "....ACBBBBCD....",
    ".....ACCCCD.....",
    "..EE..AAAA..EE..",
    ".EFFE......EFFE.",
    "..EE..FFFF..EE..",
    ".....FEEEEF.....",
    "....FEBBBBEF....",
    ".....FEEEEF.....",
    "......FFFF......",
]

ICON_STATS_PALETTE = {"A": "#f59e0b", "B": "#fcd34d", "C": "#1f6feb"}
ICON_STATS = [  # trophy
    "................",
    "..AAAAAAAAAAAA..",
    ".ABBBBBBBBBBBBA.",
    ".AABABBBBBBABAA.",
    ".A.ABBBBBBBBA.A.",
    ".A.ABBBBBBBBA.A.",
    "..AABBBBBBBBAA..",
    "....AABBBBAA....",
    "......AAAA......",
    "......ABBA......",
    ".....AAAAAA.....",
    "....ABBBBBBA....",
    "...AAAAAAAAAA...",
    "..CCCCCCCCCCCC..",
    ".CCCCCCCCCCCCCC.",
    "................",
]

ICON_SNAKE_PALETTE = {"A": "#3fb950", "B": "#7ee787", "K": "#050811", "W": "#f0f6fc", "R": "#f43f5e"}
ICON_SNAKE = [  # S-shaped snake, head top-right with forked tongue
    "..........AAAA..",
    ".........ABBBBA.",
    ".........ABWKBA.",
    ".........ABBBBAR",
    "..........ABBA.R",
    "...AAAAAA.ABBA..",
    "..ABBBBBBAABBA..",
    ".ABBAAAABBBBA...",
    ".ABA....AAAA....",
    ".ABBAAAAAAAA....",
    "..ABBBBBBBBBA...",
    "...AAAAAAAABBA..",
    "...........ABA..",
    "..AAAAAAAAABBA..",
    ".ABBBBBBBBBBA...",
    "..AAAAAAAAAA....",
]

# ---------------------------------------------------------------------------
# 7x7 button and card-header glyphs.
# ---------------------------------------------------------------------------

GLYPH_PLAY_PALETTE = {"A": "#7ee787", "B": "#fcd34d", "C": "#38bdf8"}
GLYPH_PLAY = ["AA....", "AAAA..", "AAABB.", "AAACCC", "AAABB.", "AAAA..", "AA...."]

GLYPH_APPLE_PALETTE = {"A": "#38bdf8"}
GLYPH_APPLE = ["...AA..", "..AA...", ".AAAAA.", "AAAAAAA", "AAAAA..", "AAAAAAA", ".AA.AA."]

GLYPH_DOC_PALETTE = {"A": "#fb7185", "B": "#f0f6fc"}
GLYPH_DOC = ["AAAAA..", "ABBBAA.", "ABBBBBA", "ABBAABA", "ABBBBBA", "ABBBBBA", "AAAAAAA"]

GLYPH_MAIL_PALETTE = {"A": "#f59e0b", "B": "#fcd34d", "C": "#f0f6fc"}
GLYPH_MAIL = ["AAAAAAA", "ABCCCBA", "ABBCBBA", "ABBBBBA", "ABBBBBA", "ABBBBBA", "AAAAAAA"]

GLYPH_PHONE_PALETTE = {"A": "#050811", "B": "#1f6feb", "C": "#38bdf8", "D": "#f0f6fc"}
GLYPH_PHONE = ["AAAAA", "ABBBA", "ABCBA", "ABBBA", "ABBBA", "ABDBA", "AAAAA"]

GLYPH_LEAF_PALETTE = {"A": "#050811", "B": "#7ee787", "C": "#f0f6fc"}
GLYPH_LEAF = ["...AA..", "..ABBA.", ".ABCBA.", "ABBBBBA", "..ABAA.", ".ABAA..", ".AA...."]

GLYPH_DB_PALETTE = {"A": "#050811", "B": "#fcd34d"}
GLYPH_DB = [".AAAAA.", "ABBBBBA", ".AAAAA.", "ABBBBBA", ".AAAAA.", "ABBBBBA", ".AAAAA."]

# ---------------------------------------------------------------------------
# NCD Screening emblem: heart with an EKG trace (32x32 card, 3x in the README).
# ---------------------------------------------------------------------------

HEART_PALETTE = {"B": "#050811", "C": "#f43f5e", "D": "#fb7185"}
HEART = [  # placed at (7, 7) inside the card
    "..BBBB....BBBB..",
    ".BCCCCB..BCCCCB.",
    "BCCCCCCBBCCCCCCB",
    "BCDDCCCCCCCCCCCB",
    "BCDCCCCCCCCCCCCB",
    "BCCCCCCCCCCCCCCB",
    "BCCCCCCCCCCCCCCB",
    "BCCCCCCCCCCCCCCB",
    ".BCCCCCCCCCCCCB.",
    "..BCCCCCCCCCCB..",
    "...BCCCCCCCCB...",
    "....BCCCCCCB....",
    ".....BCCCCB.....",
    "......BCCB......",
    ".......BB.......",
]
# EKG trace pixels in card coordinates: flat line, sharp QRS spike, flat line.
EKG_TRACE = (
    [(x, 12) for x in range(4, 12)]
    + [(12, 11), (12, 10), (13, 9), (13, 8), (14, 9), (14, 10), (14, 11), (14, 12),
       (14, 13), (15, 14), (15, 15), (16, 14), (16, 13)]
    + [(x, 12) for x in range(17, 28)]
)

GLYPH_PLUS_PALETTE = {"A": "#050811", "B": "#7ee787"}
GLYPH_PLUS = ["AAAAA", "AABAA", "ABBBA", "AABAA", "AAAAA"]

# ---------------------------------------------------------------------------
# Inventory tech icons (7px tall). Each entry is either a hand-drawn sprite
# ("sprite", rows, palette) or a lettered badge ("badge", letters, shape, bg, fg)
# drawn with MINI_FONT. Badge shapes: "square" (corners cut) or "circle".
# ---------------------------------------------------------------------------

MINI_FONT = {  # 3x5 letters for badges
    "A": ["010", "101", "111", "101", "101"],
    "C": ["111", "100", "100", "100", "111"],
    "E": ["111", "100", "110", "100", "111"],
    "G": ["111", "100", "101", "101", "111"],
    "J": ["001", "001", "001", "101", "111"],
    "M": ["101", "111", "101", "101", "101"],
    "N": ["101", "111", "111", "101", "101"],
    "O": ["111", "101", "101", "101", "111"],
    "P": ["111", "101", "111", "100", "100"],
    "Q": ["111", "101", "101", "111", "001"],
    "R": ["110", "101", "110", "101", "101"],
    "S": ["111", "100", "111", "001", "111"],
    "T": ["111", "010", "010", "010", "010"],
    "W": ["101", "101", "111", "111", "101"],
    "Y": ["101", "101", "010", "010", "010"],
    "3": ["111", "001", "111", "001", "111"],
    "5": ["111", "100", "111", "001", "111"],
    "+": ["000", "010", "111", "010", "000"],
    "#": ["101", "111", "101", "111", "101"],
}

_W = "#f0f6fc"
_K = "#050811"
_RIBBON = [".....AA", "A...AAA", "AA.AA.A", ".AAA..A", "AA.AA.A", "A...AAA", ".....AA"]
_CIRCLE_DOT = ["..AAA..", ".AAAAA.", "AAAWAAA", "AAWWWAA", "AAAWAAA", ".AAAAA.", "..AAA.."]

TECH_ICONS = {
    # Languages
    "DART": ("sprite", ["...A...", "..ABA..", ".ABBBA.", "ABBBBBA", ".ABBBA.", "..ABA..", "...A..."],
             {"A": "#0175c2", "B": "#13b9fd"}),
    "TYPESCRIPT": ("badge", "TS", "square", "#3178c6", _W),
    "JAVASCRIPT": ("badge", "JS", "square", "#f7df1e", _K),
    "GO": ("badge", "GO", "square", "#00add8", _W),
    "JAVA": ("sprite", ["..A.A..", ".A.A...", "BBBBB..", "BCCCBBB", "BCCCB.B", "BCCCBBB", ".BBB..."],
             {"A": "#f89820", "B": "#5382a1", "C": _W}),
    "KOTLIN": ("sprite", ["CCCCCCC", "CCCCCC.", "BBBBB..", "BBBB...", "BBBBB..", "AAAAAA.", "AAAAAAA"],
               {"A": "#7f52ff", "B": "#c711e1", "C": "#e44857"}),
    "PYTHON": ("sprite", ["..BBB..", "..B.B..", "BBBBBY.", "BBB.YYY", ".BYYYYY", "..Y.Y..", "..YYY.."],
               {"B": "#3776ab", "Y": "#ffd43b"}),
    "C++": ("badge", "C+", "square", "#00599c", _W),
    "C": ("badge", "C", "square", "#3949ab", _W),
    "C#": ("badge", "C#", "square", "#68217a", _W),
    "RUBY": ("sprite", [".......", ".AAAAA.", "ABBABBA", "AAAAAAA", ".ABBBA.", "..ABA..", "...A..."],
             {"A": "#9b111e", "B": "#e0115f"}),
    "BASH": ("sprite", ["AAAAAAA", "AGAAAAA", "AAGAAAA", "AAAGAAA", "AAGAAAA", "AGAGGGA", "AAAAAAA"],
             {"A": "#3b4252", "G": "#7ee787"}),
    # Frontend & cross-platform
    "FLUTTER": ("sprite", ["....LL.", "...LL..", "..LL...", ".LL.LL.", "..LLL..", "...DD..", "....D.."],
                {"L": "#47c5fb", "D": "#0569a6"}),
    "REACT": ("sprite", ["A.....A", ".A.A.A.", "..AAA..", "AAABAAA", "..AAA..", ".A.A.A.", "A.....A"],
              {"A": "#61dafb", "B": _W}),
    "VUE": ("sprite", ["GGDDDGG", ".GGDGG.", ".GGDGG.", "..GGG..", "..GGG..", "...G...", "......."],
            {"G": "#41b883", "D": "#35495e"}),
    "TAURI": ("badge", "T", "circle", "#ffc131", _K),
    "WORDPRESS": ("badge", "W", "circle", "#21759b", _W),
    "HTML": ("badge", "5", "square", "#e34f26", _W),
    "CSS": ("badge", "3", "square", "#1572b6", _W),
    # Backend, cloud & DB
    "NODE.JS": ("badge", "N", "circle", "#3c873a", _W),
    "SPRING": ("sprite", ["...AA..", "..ABBA.", ".ABCBA.", "ABBBBBA", "..ABAA.", ".ABAA..", ".AA...."],
               {"A": "#2f6b1f", "B": "#6db33f", "C": _W}),
    "FIREBASE": ("sprite", ["...Y...", "..YY...", "..YOY..", ".YOOY..", ".YOOOY.", "YOORROY", ".OOOOO."],
                 {"Y": "#ffca28", "O": "#ffa000", "R": "#f57c00"}),
    "DOCKER": ("sprite", [".......", "..C....", "CCCC...", "BBBBBBB", "BBBBBB.", ".BBBB..", "......."],
               {"C": "#9fd3ff", "B": "#2496ed"}),
    "CLOUDFLARE": ("sprite", [".......", "...OO..", "..OOOO.", ".OOOOOO", "OOOOOOO", "YYYYYY.", "......."],
                   {"O": "#f38020", "Y": "#faae40"}),
    "AZURE": ("badge", "A", "square", "#0078d4", _W),
    "POSTGRESQL": ("badge", "PG", "square", "#336791", _W),
    "SUPABASE": ("sprite", ["....G..", "...GG..", "..GGG..", ".GGGGG.", "..GGG..", "..GG...", "..G...."],
                 {"G": "#3ecf8e"}),
    "MYSQL": ("badge", "MY", "square", "#00758f", "#f29111"),
    "SQLITE": ("badge", "SQ", "square", "#0f80cc", _W),
    # Tools, engines & creative
    "GIT": ("sprite", ["...A...", "..AAA..", ".AWAAA.", "AAAWAAA", ".AAWWA.", "..AAA..", "...A..."],
            {"A": "#f05032", "W": _W}),
    "GITHUB": ("sprite", ["..WWW..", ".WKWKW.", "WWKKKWW", "WKKKKKW", "WWKKKWW", ".WK.KW.", "..WWW.."],
               {"W": _W, "K": _K}),
    "GITLAB": ("sprite", [".......", "R.....R", "RO...OR", "ROOOOOR", ".ROYOR.", "..RYR..", "...R..."],
               {"R": "#e24329", "O": "#fc6d26", "Y": "#fca326"}),
    "BITBUCKET": ("sprite", [".......", "BBBBBBB", ".BBBBB.", ".BBWBB.", "..BBB..", "..BBB..", "......."],
                  {"B": "#2684ff", "W": _W}),
    "VS CODE": ("sprite", _RIBBON, {"A": "#007acc"}),
    "VISUAL STUDIO": ("sprite", _RIBBON, {"A": "#865fc5"}),
    "ANDROID STUDIO": ("sprite", [".......", ".G...G.", "..GGG..", ".GGGGG.", ".GKGKG.", ".GGGGG.", "......."],
                       {"G": "#3ddc84", "K": _K}),
    "ECLIPSE": ("sprite", ["..PPP..", ".PPPPPO", "PWWWWPO", "PPPPPPO", "PWWWWPO", ".PPPPPO", "..PPP.."],
                {"P": "#4b3f8f", "W": _W, "O": "#f7941e"}),
    "POSTMAN": ("sprite", _CIRCLE_DOT, {"A": "#ff6c37", "W": _W}),
    "SWAGGER": ("sprite", ["..GGG..", ".KGGGK.", "GKGGGKG", "KGGKGGK", "GKGGGKG", ".KGGGK.", "..GGG.."],
                {"G": "#85ea2d", "K": "#173647"}),
    "CMAKE": ("sprite", ["...B...", "..BBR..", "..BBR..", ".BBGRR.", ".BGGGR.", "GGGGGGR", "......."],
              {"B": "#1f6feb", "R": "#e4002b", "G": "#4caf50"}),
    "UBUNTU": ("sprite", ["..OOO..", ".OWWWO.", "OWOOOWO", "OWOOOWO", "OWOOOWO", ".OWWWO.", "..OOO.."],
               {"O": "#e95420", "W": _W}),
    "WINDOWS": ("sprite", ["BBB.BBB", "BBB.BBB", "BBB.BBB", ".......", "BBB.BBB", "BBB.BBB", "BBB.BBB"],
                {"B": "#00a4ef"}),
    "UNITY": ("sprite", ["...W...", ".WWWWW.", "LLWWWDD", "LLLLDDD", "LLLLDDD", ".LLLDD.", "...LD.."],
              {"W": _W, "L": "#a9bbd8", "D": "#63779c"}),
    "GODOT": ("sprite", [".B...B.", ".BBBBB.", "BWWBWWB", "BWKBKWB", "BBBBBBB", "BBWBWBB", ".BBBBB."],
              {"B": "#478cbf", "W": _W, "K": _K}),
    "ROBLOX STUDIO": ("sprite", ["...B...", "..BBB..", ".BBBBB.", "BBB.BBB", ".BBBBB.", "..BBB..", "...B..."],
                      {"B": "#00a2ff"}),
    "FIGMA": ("sprite", ["..RROO.", "..RROO.", "..PPBB.", "..PPBB.", "..GG...", "..GG...", "......."],
              {"R": "#f24e1e", "O": "#ff7262", "P": "#a259ff", "B": "#1abcfe", "G": "#0acf83"}),
    "PHOTOSHOP": ("badge", "PS", "square", "#001e36", "#31a8ff"),
    "PREMIERE PRO": ("badge", "PR", "square", "#00005b", "#9999ff"),
    "AFTER EFFECTS": ("badge", "AE", "square", "#00005b", "#9999ff"),
}
