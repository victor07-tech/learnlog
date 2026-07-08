# Windows Fundamentals 3

**Platform:** TryHackMe  
**Link:** https://tryhackme.com/room/windows-fundamentals-3  
**Date:** 2026-07-08  
**Difficulty:** Easy  
**Topics:** Windows Security, Microsoft Defender, Firewall, Windows Update

---

## What it covers

This room introduces the core security features built into Windows that help protect the operating system and user data. It explains how Windows Defender, Windows Firewall, Windows Update, and other security components work together to defend against malware and unauthorized access.

---

## Concepts I learned

- **Windows Update**
  - Keeps Windows secure by installing security patches, bug fixes, and feature updates.
  - Microsoft usually releases updates on **Patch Tuesday** (the second Tuesday of each month).

- **Windows Security**
  - A central dashboard to manage Windows security features.
  - Includes Virus & Threat Protection, Firewall & Network Protection, App & Browser Control, and Device Security.

- **Microsoft Defender Antivirus**
  - Built-in antivirus that scans for malware and other threats.
  - Supports Quick Scan, Full Scan, and Custom Scan.

- **Threat History**
  - Shows recently detected threats.
  - Quarantined files are isolated so they cannot run.
  - Allowed threats should only be used when you completely trust the file.

- **Real-time Protection**
  - Continuously monitors files and programs to stop malware before it executes.

- **Cloud-delivered Protection**
  - Uses Microsoft's cloud intelligence to detect newly discovered threats more quickly.

- **Controlled Folder Access**
  - Helps protect important folders from ransomware by allowing only trusted applications to modify protected files.

- **Exclusions**
  - Allows specific files or folders to be skipped during antivirus scans.
  - Should only be used for trusted files because excluded items are not scanned.

- **Windows Defender Firewall**
  - Controls incoming and outgoing network traffic.
  - Supports Domain, Private, and Public firewall profiles.

---

## Tools used

- **Windows Security** – Managed antivirus, firewall, and device protection settings.
- **Microsoft Defender Antivirus** – Performed malware detection and system scans.
- **Windows Defender Firewall** – Managed network access and firewall profiles.
- **Windows Update** – Installed security updates and operating system patches.

---

## My approach (high level)

I explored each Windows security component to understand its purpose instead of simply memorizing menu options. I focused on how the different features work together to reduce attack surfaces, prevent malware execution, and keep Windows systems updated and protected.

---

## Key takeaway

Windows security is built from multiple layers. Antivirus, firewall, regular updates, and ransomware protection work together, and keeping these features enabled greatly improves a system's security.

---

## Where I got stuck

Initially, I was confused by the differences between quarantine, exclusions, and allowed threats. After exploring each feature, I understood that quarantine isolates malicious files, exclusions skip scanning for trusted items, and allowed threats let a specific detected file run intentionally.