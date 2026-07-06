#!/usr/bin/env python3
"""
learnlog — publish your learning writeups the honest way, across platforms.

One tiny CLI for TryHackMe, HackTheBox, LeetCode (and generic notes). It removes
the friction of keeping a "build in public" log — scaffolds the entry, fills the
date, updates the index, commits and pushes — while YOU write the real content.

It will not fake a commit: `publish` refuses any entry that still contains template
placeholders. No empty commits, no gamed green squares.

Zero dependencies — Python 3.8+ and git.

Usage:
    python learnlog.py new <platform> <slug>       Scaffold an entry
    python learnlog.py publish <platform> <slug>   Guard, index, commit, push
    python learnlog.py platforms                    List supported platforms
    python learnlog.py list                         List your entries
    python learnlog.py --help

Platforms: thm (TryHackMe), htb (HackTheBox), leetcode (LeetCode), generic
"""

from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENTRIES = ROOT / "entries"
TEMPLATES = ROOT / "templates"
README = ROOT / "README.md"

PLATFORMS = {
    "thm": ("TryHackMe", "tryhackme.md", "https://tryhackme.com/room/{slug}",
            ("tryhackme", "try")),
    "htb": ("HackTheBox", "hackthebox.md", "https://app.hackthebox.com/machines/{slug}",
            ("hackthebox", "htb")),
    "leetcode": ("LeetCode", "leetcode.md", "https://leetcode.com/problems/{slug}/",
                 ("lc", "leet")),
    "generic": ("General", "generic.md", "", ("gen", "note", "notes")),
}

PLACEHOLDERS = [
    "<2-3 sentences", "<concept", "<approach", "<one thing", "<your notes",
    "<intuition", "<complexity", "<what tripped", "<recon", "<foothold",
    "<privilege", "<what it covers", "<summary",
]


def _die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def _slugify(text: str) -> str:
    return "-".join(text.lower().split()).replace("_", "-")


def _resolve_platform(key: str) -> str:
    key = key.lower()
    if key in PLATFORMS:
        return key
    for canon, (_n, _t, _u, aliases) in PLATFORMS.items():
        if key in aliases:
            return canon
    _die(f"unknown platform '{key}'. Run: python learnlog.py platforms")


def _ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    return input(f"{prompt}{suffix}: ").strip() or default


def cmd_new(platform: str, slug: str) -> None:
    platform = _resolve_platform(platform)
    name, tmpl_file, url_pat, _ = PLATFORMS[platform]
    slug = _slugify(slug)

    dest_dir = ENTRIES / platform
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{slug}.md"
    if dest.exists():
        _die(f"{dest.relative_to(ROOT)} already exists — edit it, or pick another slug.")

    print(f"Scaffolding a {name} entry. Answer a few quick questions:\n")
    title = _ask("Title", slug.replace("-", " ").title())
    level = _ask("Difficulty / level", "Easy")
    topics = _ask("Topics / tags (comma-separated)", "")
    url = _ask("URL", url_pat.format(slug=slug) if url_pat else "")

    tmpl_path = TEMPLATES / tmpl_file
    template = tmpl_path.read_text(encoding="utf-8") if tmpl_path.exists() else _fallback()
    content = (
        template.replace("<title>", title)
        .replace("<url>", url)
        .replace("<YYYY-MM-DD>", date.today().isoformat())
        .replace("<difficulty>", level)
        .replace("<topics>", topics)
        .replace("<platform>", name)
    )
    dest.write_text(content, encoding="utf-8")
    print(f"\n✔ Created {dest.relative_to(ROOT)}")
    print("  Write your real notes in it, then:")
    print(f"      python learnlog.py publish {platform} {slug}")


def cmd_publish(platform: str, slug: str) -> None:
    platform = _resolve_platform(platform)
    name = PLATFORMS[platform][0]
    slug = _slugify(slug)
    path = ENTRIES / platform / f"{slug}.md"
    if not path.exists():
        _die(f"{path.relative_to(ROOT)} not found. Create it: python learnlog.py new {platform} {slug}")

    text = path.read_text(encoding="utf-8")
    left = [p for p in PLACEHOLDERS if p in text]
    if left:
        _die("this entry still has template placeholders — fill in your real notes "
             "before publishing. No empty/fake commits.")

    _update_index(platform, name, slug, text)
    _git("add", "-A")
    _git("commit", "-m", f"Add {name} writeup: {slug}")
    print("\nCommitted. Pushing…")
    try:
        _git("push")
        print("✔ Pushed. Honest green box earned. 🟩")
    except SystemExit:
        print("Commit done, but push failed — check your remote/auth, then run: git push")


def _update_index(platform: str, name: str, slug: str, text: str) -> None:
    if not README.exists():
        return
    title = slug.replace("-", " ").title()
    level = "—"
    topics = "—"
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.lower().startswith("**difficulty"):
            level = line.split("**", 2)[-1].lstrip(": ").strip() or "—"
        elif line.lower().startswith("**topics") or line.lower().startswith("**tags"):
            topics = line.split("**", 2)[-1].lstrip(": ").strip() or "—"

    rel = f"entries/{platform}/{slug}.md"
    row = f"| {date.today().isoformat()} | {name} | [{title}]({rel}) | {level} | {topics} |"

    lines = README.read_text(encoding="utf-8").splitlines()

    def _is_separator(s: str) -> bool:
        return ("|" in s and "-" in s
                and set(s.replace("|", "").replace("-", "").replace(":", "").strip()) == set())

    header_idx = -1
    for i, line in enumerate(lines):
        low = line.lower()
        if line.lstrip().startswith("|") and "date" in low and (
                "title" in low or "room" in low or "machine" in low):
            if i + 1 < len(lines) and _is_separator(lines[i + 1]):
                header_idx = i
                break

    out, inserted = list(lines), False
    if header_idx != -1:
        out.insert(header_idx + 2, row)
        inserted = True
    if inserted:
        README.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"✔ Added index row for {name}: {title}")
    else:
        print("note: no log table found in README — add the row manually.")


def cmd_platforms() -> None:
    print("Supported platforms:\n")
    for key, (name, _t, _u, aliases) in PLATFORMS.items():
        al = ", ".join(dict.fromkeys((key,) + aliases))
        print(f"  {name:<12} → {al}")


def cmd_list() -> None:
    if not ENTRIES.exists() or not any(ENTRIES.rglob("*.md")):
        print("No entries yet. Create one: python learnlog.py new <platform> <slug>")
        return
    print("Entries:")
    for pdir in sorted(ENTRIES.iterdir()):
        if pdir.is_dir():
            files = sorted(pdir.glob("*.md"))
            if files:
                name = PLATFORMS.get(pdir.name, (pdir.name,))[0]
                print(f"  {name}:")
                for f in files:
                    print(f"    - {f.stem}")


def _git(*args: str) -> None:
    try:
        subprocess.run(["git", *args], cwd=ROOT, check=True)
    except FileNotFoundError:
        _die("git is not installed or not on PATH.")
    except subprocess.CalledProcessError as e:
        _die(f"git {' '.join(args)} failed (exit {e.returncode}).")


def _fallback() -> str:
    return ("# <title>\n\n**Platform:** <platform>\n**Date:** <YYYY-MM-DD>\n\n"
            "## Notes\n\n<your notes here>\n")


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__)
        return
    cmd, rest = args[0], args[1:]
    if cmd == "new":
        if len(rest) < 2:
            _die("usage: python learnlog.py new <platform> <slug>")
        cmd_new(rest[0], rest[1])
    elif cmd == "publish":
        if len(rest) < 2:
            _die("usage: python learnlog.py publish <platform> <slug>")
        cmd_publish(rest[0], rest[1])
    elif cmd == "platforms":
        cmd_platforms()
    elif cmd == "list":
        cmd_list()
    else:
        _die(f"unknown command '{cmd}'. Try --help.")


if __name__ == "__main__":
    main()
