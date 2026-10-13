#!/usr/bin/env python3
"""Builds dark_mode.svg and light_mode.svg, the neofetch-style card in README.md.

Run it from anywhere after `gh auth login`:  python3 scripts/build_card.py
The GitHub numbers are read live; everything else is the INFO list below.
"""
import json
import subprocess
from datetime import date
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER = "raushan2015"
WIDTH = 58  # characters in one line of the right column

THEMES = {
    "dark": dict(bg="#161b22", text="#c9d1d9", key="#ffa657", value="#a5d6ff", dots="#616e7f"),
    "light": dict(bg="#f6f8fa", text="#24292f", key="#953800", value="#0a3069", dots="#c2cfde"),
}


def stats():
    year_query = "y{y}: contributionsCollection(from:\"{y}-01-01T00:00:00Z\", to:\"{y}-12-31T23:59:59Z\") {{ totalCommitContributions restrictedContributionsCount }}"
    years = " ".join(year_query.format(y=y) for y in range(2017, date.today().year + 1))
    query = f"""{{ user(login:"{USER}") {{
        followers {{ totalCount }}
        repositories(first:100, ownerAffiliations:OWNER) {{ totalCount nodes {{ stargazerCount }} }}
        {years} }} }}"""
    out = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], check=True, capture_output=True, text=True)
    user = json.loads(out.stdout)["data"]["user"]
    commits = sum(v["totalCommitContributions"] + v["restrictedContributionsCount"] for k, v in user.items() if k.startswith("y2"))
    return dict(
        repos=user["repositories"]["totalCount"],
        stars=sum(r["stargazerCount"] for r in user["repositories"]["nodes"]),
        followers=user["followers"]["totalCount"],
        commits=commits,
    )


def info(s):
    """One entry per line: ('title', text), ('row', key, value), ('pair', k1, v1, k2, v2) or None for a gap."""
    return [
        ("title", "raushan@chaudhary"),
        ("row", "OS", "Linux, macOS, Windows"),
        ("row", "Host", "Global Information Career Academy, Japan"),
        ("row", "Kernel", "Infrastructure Engineer / Full-Stack Developer"),
        ("row", "Shell", "Bash, PowerShell"),
        None,
        ("row", "Languages.Code", "TypeScript, JavaScript, Python, Java"),
        ("row", "Languages.Stack", "Node.js, Next.js, React, Electron, Expo"),
        ("row", "Languages.Data", "PostgreSQL, Redis, SQLite, MinIO"),
        ("row", "Languages.Real", "English, Japanese, Nepali, Hindi"),
        None,
        ("row", "Homelab.Run", "Docker, Nginx, Pi-hole, Plex"),
        ("row", "Homelab.Network", "DNS, VPN, Firewall, SSL/TLS"),
        None,
        ("title", "Projects"),
        ("row", "TECHSHAN", "Server management panel with AI"),
        ("row", "TECHSHAN.Link", "https://techshan.app"),
        ("row", "TECHSHAN-IMS", "Multi-tenant ERP and inventory system"),
        ("row", "TECHSHAN-IMS.Link", "https://ims.techshan.app"),
        None,
        ("title", "Contact"),
        ("row", "Email", "mail@raushan7.com.np"),
        ("row", "Website", "raushan7.com.np"),
        ("row", "LinkedIn", "linkedin.com/in/raushan2015"),
        ("row", "Instagram", "raushan.2015"),
        None,
        ("title", "GitHub Stats"),
        ("pair", "Repos", f"{s['repos']}", "Stars", f"{s['stars']}"),
        ("pair", "Commits", f"{s['commits']:,}", "Followers", f"{s['followers']}"),
    ]


def row(key, value, width=WIDTH):
    dots = "." * (width - len(key) - len(value) - 3)
    if "." in key:
        head, tail = key.split(".", 1)
        key_svg = f'<tspan class="key">{escape(head)}</tspan>.<tspan class="key">{escape(tail)}</tspan>'
    else:
        key_svg = f'<tspan class="key">{escape(key)}</tspan>'
    return f'{key_svg}:<tspan class="dots"> {dots} </tspan><tspan class="value">{escape(value)}</tspan>'


def line(entry):
    kind = entry[0]
    if kind == "title":
        return f'{escape(entry[1])} <tspan class="dots">{"-" * (WIDTH - len(entry[1]) - 1)}</tspan>'
    if kind == "row":
        return row(entry[1], entry[2])
    half = (WIDTH - 3) // 2
    return row(entry[1], entry[2], half) + '<tspan class="dots"> | </tspan>' + row(entry[3], entry[4], WIDTH - 3 - half)


def build(theme, s):
    c = THEMES[theme]
    art = (ROOT / "assets" / f"ascii-{theme}.txt").read_text().rstrip("\n").split("\n")
    entries = info(s)
    height = max(len(art) * 15 + 40, len(entries) * 20 + 40)
    art_y = (height - len(art) * 15) // 2 + 11
    info_y = (height - len(entries) * 20) // 2 + 15
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" font-family="Consolas,Menlo,\'DejaVu Sans Mono\',\'Liberation Mono\',monospace" width="985px" height="{height}px" viewBox="0 0 985 {height}">',
        "<style>",
        f".key {{fill: {c['key']};}} .value {{fill: {c['value']};}} .dots {{fill: {c['dots']};}}",
        "text, tspan {white-space: pre;}",
        "</style>",
        f'<rect width="985" height="{height}" fill="{c["bg"]}" rx="15"/>',
        f'<text x="15" y="{art_y}" fill="{c["text"]}" font-size="13px" xml:space="preserve">',
    ]
    out += [f'<tspan x="15" y="{art_y + i * 15}">{escape(a)}</tspan>' for i, a in enumerate(art)]
    out += ["</text>", f'<text x="440" y="{info_y}" fill="{c["text"]}" font-size="15px" xml:space="preserve">']
    out += [f'<tspan x="440" y="{info_y + i * 20}">{line(e)}</tspan>' for i, e in enumerate(entries) if e]
    out += ["</text>", "</svg>"]
    (ROOT / f"{theme}_mode.svg").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    numbers = stats()
    for name in THEMES:
        build(name, numbers)
    print("built dark_mode.svg and light_mode.svg:", numbers)
