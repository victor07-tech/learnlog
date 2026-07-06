# Blue

**Platform:** TryHackMe
**Link:** https://tryhackme.com/room/blue
**Date:** 2026-07-06
**Difficulty:** Easy
**Topics:** windows, smb, eternalblue, ms17-010

---

## What it covers

Blue is a beginner Windows room built around EternalBlue (MS17-010), a critical SMBv1 vulnerability. It teaches the full basic path: scan, identify a known vulnerability, exploit it for a shell, and understand why the box was exploitable in the first place.

## Concepts I learned

- SMB (Server Message Block) is a Windows file/printer-sharing protocol; older SMBv1 has serious, well-documented flaws.
- MS17-010 / EternalBlue is a remote code execution bug in SMBv1 that lets an attacker run code on an unpatched host without credentials.
- Why patch management matters — this whole box is exploitable only because a single security update was missing.

## Tools used

- `nmap` — port scan and version detection to find open SMB (445) and fingerprint the OS.
- Metasploit — used the MS17-010 scanner module to confirm the vuln, then the matching exploit module to get a shell.

## My approach (high level)

1. **Enumeration** — scanned the target, found SMB open on 445 and an older Windows version, which is a classic EternalBlue signal.
2. **Confirm** — used the MS17-010 auxiliary scanner to verify the host was actually vulnerable before firing anything.
3. **Foothold** — ran the matching exploit module conceptually: it abuses the SMBv1 flaw to execute code and return a session.
4. **Post-exploitation** — upgraded to a fuller shell and confirmed access at a high privilege level.

## Key takeaway

One missing patch (MS17-010) fully compromised the host. In the real world, timely patching and disabling legacy SMBv1 would have prevented the entire attack chain.

## Where I got stuck

Remembering to confirm the vulnerability with the scanner module *before* launching the exploit — checking first avoids wasting time firing exploits at a patched target.