# learnlog

> Publish your learning writeups the **honest** way — across TryHackMe, HackTheBox, LeetCode, and general notes. A CLI *and* a one-click web app.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)

**🔗 Live app:** https://victor07-tech.github.io/learnlog/

Built by [@victor07-tech](https://github.com/victor07-tech) for people learning security and coding in public. Scaffold an entry, write your real notes, and it commits + pushes + updates the index below. **You write every word** — it just removes the git friction.

## Honest by design

It refuses to publish an entry that still contains template placeholders. No empty commits, no gamed green squares — a contribution graph that's obviously faked fools no one who matters. The point is to make *real* documentation effortless.

## Two ways to use it

- **CLI** — `python learnlog.py new thm blue` → write notes → `python learnlog.py publish thm blue`
- **Web app** — open the [live app](https://victor07-tech.github.io/learnlog/), paste a GitHub token once, write, click Publish.

## Use it yourself (any GitHub user)

Your token stays in your browser and is sent only to GitHub — nobody else sees it, and your writeups go to *your* repo, not anyone else's.

1. Create a fine-grained token → <https://github.com/settings/tokens?type=beta>
   - Repository access: **Only select repositories** → your writeups repo
   - Permissions → **Contents: Read and write**
2. Open the [live app](https://victor07-tech.github.io/learnlog/), paste the token, click **Save**.
3. Enter **your** owner and repo, pick a platform, write, click **Publish**.

## Supported platforms

| Platform | Keys |
|----------|------|
| TryHackMe | `thm`, `tryhackme` |
| HackTheBox | `htb`, `hackthebox` |
| LeetCode | `leetcode`, `lc` |
| General | `generic`, `note` |

## Log

| Date | Platform | Title | Difficulty | Topics |
|------|----------|-------|-----------|--------|
| 2026-07-08 | TryHackMe | [Windows Fundamentals 3](entries/thm/windows-fundamentals-3.md) | easy | — |
| 2026-07-06 | TryHackMe | [Blue](entries/thm/blue.md) | Easy | windows, smb, eternalblue |

## A note on etiquette

For CTF/box platforms, writeups explain **concepts and approach** — not flags or exact answers. The templates nudge you that way on purpose.

## License

[MIT](LICENSE) — use it, fork it, adapt it. A ⭐ is appreciated if it helps you.
