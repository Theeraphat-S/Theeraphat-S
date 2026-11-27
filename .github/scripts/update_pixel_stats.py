"""Fetch GitHub profile statistics and generate assets/pixel-stats.svg."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from pixel_svg import (
    PALETTE,
    render_pixel_bar,
    render_pixel_text,
    render_rpg_window,
    render_sprite,
    text_width,
    wrap_svg,
)

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"

GRAPHQL_QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      restrictedContributionsCount
      totalPullRequestContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
    pullRequests(states: [OPEN, CLOSED, MERGED]) {
      totalCount
    }
    repositories(
      first: 100
      ownerAffiliations: OWNER
      isFork: false
      orderBy: { field: PUSHED_AT, direction: DESC }
    ) {
      nodes {
        languages(first: 10, orderBy: { field: SIZE, direction: DESC }) {
          edges {
            size
            node {
              name
              color
            }
          }
        }
      }
    }
  }
}
"""

TROPHY_SPRITE = [
    "...YYYYYY...",
    "..YGGGGGGY..",
    ".YYGYYYYGYY.",
    ".Y.YGGGGY.Y.",
    ".Y.YGGGGY.Y.",
    "..YYGGGGYY..",
    "....YYYY....",
    "....YGGY....",
    "...YYYYYY...",
    "..YGGGGGGY..",
]

CRYSTAL_SPRITE = [
    "....CC....",
    "...CBBc...",
    "..CBWWBc..",
    ".CBBWWBBc.",
    ".CBBBBBBc.",
    "..CBCCBc..",
    "...CBBc...",
    "....CC....",
]

DEFAULT_SEED_DATA = {
    # Snapshot of real values from 2026-11-28, used only for offline previews (--seed).
    "commits": 426,
    "contributions": 488,
    "prs": 53,
    "active_days": 58,
    "languages": [
        {"name": "Dart", "pct": 39.42, "color": "#00B4AB"},
        {"name": "TypeScript", "pct": 22.51, "color": "#3178c6"},
        {"name": "JavaScript", "pct": 17.13, "color": "#f1e05a"},
        {"name": "GDScript", "pct": 8.94, "color": "#355570"},
        {"name": "Python", "pct": 7.56, "color": "#3572A5"},
    ],
    "synced_at": "2026-11-28",
}


def count_active_days(days: list[dict]) -> int:
    """Return how many calendar days had at least one contribution."""
    return sum(1 for day in days if day["contributionCount"] > 0)


def fetch_github_stats(username: str, token: str) -> dict:
    """Query GitHub GraphQL API for user stats and language distribution."""
    now = dt.datetime.now(dt.timezone.utc)
    one_year_ago = now - dt.timedelta(days=365)
    payload = json.dumps(
        {
            "query": GRAPHQL_QUERY,
            "variables": {
                "login": username,
                "from": one_year_ago.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            },
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        GITHUB_GRAPHQL_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Theeraphat-S-Pixel-Stats/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub GraphQL HTTP {exc.code}: {detail}") from exc

    if "errors" in body:
        raise RuntimeError(f"GitHub GraphQL errors: {body['errors']}")

    user = body["data"]["user"]
    if not user:
        raise RuntimeError(f"GitHub user '{username}' not found")

    cc = user["contributionsCollection"]
    cal = cc["contributionCalendar"]
    days = [day for week in cal["weeks"] for day in week["contributionDays"]]
    active_days = count_active_days(days)

    lang_totals: dict[str, dict] = {}
    for repo in user["repositories"]["nodes"]:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            color = edge["node"]["color"] or PALETTE["cyan"]
            size = edge["size"]
            if name not in lang_totals:
                lang_totals[name] = {"size": 0, "color": color}
            lang_totals[name]["size"] += size

    total_bytes = sum(item["size"] for item in lang_totals.values()) or 1
    sorted_langs = sorted(
        lang_totals.items(), key=lambda kv: kv[1]["size"], reverse=True
    )[:5]
    languages = [
        {
            "name": name,
            "pct": round(item["size"] * 100.0 / total_bytes, 2),
            "color": item["color"],
        }
        for name, item in sorted_langs
    ]

    commits = cc["totalCommitContributions"] + cc["restrictedContributionsCount"]
    prs = user["pullRequests"]["totalCount"]
    contributions = cal["totalContributions"]

    return {
        "commits": commits,
        "contributions": contributions,
        "prs": prs,
        "active_days": active_days,
        "languages": languages,
        "synced_at": now.strftime("%Y-%m-%d"),
    }


def build_stats_svg(data: dict) -> str:
    """Render the 16-bit Cyber-Midnight RPG stats card SVG."""
    w, h = 280, 95
    parts: list[str] = [
        # Left RPG Window: Adventurer Record
        render_rpg_window(2, 2, 132, 75),
        # Right RPG Window: Language Mastery
        render_rpg_window(138, 2, 140, 75),
        # Bottom Sync Bar
        render_rpg_window(2, 79, 276, 14, fill=PALETTE["bg_deep"], with_rivets=False),
    ]

    # Left Header + Trophy Sprite
    parts.append(
        '<g class="bob">\n  '
        + render_sprite(
            TROPHY_SPRITE,
            {"Y": PALETTE["gold"], "G": PALETTE["gold_hi"]},
            x=9,
            y=8,
            scale=1,
        )
        + "\n  </g>"
    )
    parts.append(
        render_pixel_text(
            "ADVENTURER RECORD",
            24,
            10,
            PALETTE["gold_hi"],
            scale=1,
            spacing=1,
            font="5x7",
            shadow_color=PALETTE["border_dark"],
        )
    )
    parts.append(
        f'<rect x="9" y="20" width="118" height="1" fill="{PALETTE["grid_line"]}"/>'
    )

    stat_rows = [
        ("COMMITS (1Y)", str(data["commits"]), PALETTE["cyan"]),
        ("CONTRIBUTIONS", str(data["contributions"]), PALETTE["emerald_hi"]),
        ("PULL REQUESTS", str(data["prs"]), PALETTE["blue"]),
        ("ACTIVE DAYS (1Y)", str(data["active_days"]), PALETTE["gold_hi"]),
    ]
    for idx, (label, val, val_color) in enumerate(stat_rows):
        ry = 25 + idx * 12
        parts.append(
            f'<rect x="9" y="{ry}" width="118" height="10" fill="{PALETTE["bg_slot"]}"/>'
        )
        parts.append(
            f'<rect x="9" y="{ry}" width="2" height="10" fill="{val_color}"/>'
        )
        parts.append(
            render_pixel_text(
                label, 14, ry + 2, PALETTE["text_mid"], scale=1, spacing=1, font="4x6"
            )
        )
        vw = text_width(val, scale=1, spacing=1, font="5x7")
        parts.append(
            render_pixel_text(
                val,
                124 - vw,
                ry + 2,
                val_color,
                scale=1,
                spacing=1,
                font="5x7",
                shadow_color=PALETTE["border_dark"],
            )
        )

    # Right Header + Crystal Sprite
    parts.append(
        '<g class="pulse">\n  '
        + render_sprite(
            CRYSTAL_SPRITE,
            {
                "C": PALETTE["blue_dark"],
                "B": PALETTE["cyan"],
                "c": PALETTE["blue"],
                "W": PALETTE["text_hi"],
            },
            x=145,
            y=9,
            scale=1,
        )
        + "\n  </g>"
    )
    parts.append(
        render_pixel_text(
            "REPO LANGUAGES",
            158,
            10,
            PALETTE["cyan"],
            scale=1,
            spacing=1,
            font="5x7",
            shadow_color=PALETTE["border_dark"],
        )
    )
    parts.append(
        f'<rect x="145" y="20" width="126" height="1" fill="{PALETTE["grid_line"]}"/>'
    )

    langs = data.get("languages", [])[:5]
    max_pct = max((float(item["pct"]) for item in langs), default=100.0) or 100.0
    for idx, lang in enumerate(langs):
        ly = 24 + idx * 10
        color = lang.get("color") or PALETTE["cyan"]
        if color.lower() in {"#355570", "#000000", "#111111"}:
            color = "#60a5fa"
        name = str(lang["name"])[:10]
        pct = float(lang["pct"])
        pct_text = f"{pct:.1f}%"

        # Color square icon
        parts.append(f'<rect x="145" y="{ly+2}" width="4" height="4" fill="{color}"/>')
        parts.append(
            render_pixel_text(
                name, 152, ly + 1, PALETTE["text_hi"], scale=1, spacing=1, font="4x6"
            )
        )
        # Pixel progress bar
        parts.append(
            render_pixel_bar(
                206,
                ly + 1,
                39,
                6,
                ratio=pct / max_pct,
                fill=color,
                hi=PALETTE["text_hi"],
                segmented=True,
            )
        )
        pw = text_width(pct_text, scale=1, spacing=1, font="4x6")
        parts.append(
            render_pixel_text(
                pct_text,
                271 - pw,
                ly + 1,
                PALETTE["text_mid"],
                scale=1,
                spacing=1,
                font="4x6",
            )
        )

    # Bottom Sync Status Strip
    sync_left = "AUTO-SYNCED VIA GITHUB ACTIONS"
    sync_right = f'UPDATED {data["synced_at"]}'
    parts.append(
        render_pixel_text(
            sync_left, 8, 83, PALETTE["text_dim"], scale=1, spacing=1, font="4x6"
        )
    )
    rw = text_width(sync_right, scale=1, spacing=1, font="4x6")
    parts.append(
        render_pixel_text(
            sync_right,
            272 - rw,
            83,
            PALETTE["emerald_hi"],
            scale=1,
            spacing=1,
            font="4x6",
        )
    )

    styles = """
    @keyframes bob {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-1px); }
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.72; }
    }
    .bob { animation: bob 2.4s steps(2, end) infinite; }
    .pulse { animation: pulse 2s steps(2, end) infinite; }
    @media (prefers-reduced-motion: reduce) {
      .bob, .pulse { animation: none; }
    }"""

    return wrap_svg(
        w,
        h,
        px_scale=3,
        title="Theeraphat-S GitHub Player Stats",
        desc="Auto-updated GitHub commits, contributions, pull requests, active days, and top languages by code size across owned repositories.",
        body="\n  ".join(parts),
        styles=styles,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Pixel RPG GitHub Stats SVG.")
    parser.add_argument("--user", default="Theeraphat-S", help="GitHub username")
    parser.add_argument(
        "--output",
        default=str(SCRIPT_DIR.parent.parent / "assets" / "pixel-stats.svg"),
        help="Output SVG file path",
    )
    parser.add_argument(
        "--seed",
        action="store_true",
        help="Use seeded baseline stats if GITHUB_TOKEN is unavailable (local preview).",
    )
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("METRICS_TOKEN")
    if token:
        data = fetch_github_stats(args.user, token)
    elif args.seed:
        data = DEFAULT_SEED_DATA
    else:
        print(
            "Error: GITHUB_TOKEN or METRICS_TOKEN must be set (pass --seed for offline preview).",
            file=sys.stderr,
        )
        return 1

    # Fingerprint the numbers (not the sync date) so a day with no new activity
    # leaves the file untouched and the workflow makes no commit.
    stats_only = {k: v for k, v in data.items() if k != "synced_at"}
    fingerprint = f"<!-- stats:{json.dumps(stats_only, sort_keys=True)} -->"
    out_path = Path(args.output)
    if out_path.exists() and fingerprint in out_path.read_text(encoding="utf-8"):
        print(f"Stats unchanged; kept {out_path}")
        return 0

    svg_content = build_stats_svg(data).replace("</svg>\n", f"  {fingerprint}\n</svg>\n")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(svg_content, encoding="utf-8", newline="\n")
    print(f"Generated {out_path} ({len(svg_content)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
