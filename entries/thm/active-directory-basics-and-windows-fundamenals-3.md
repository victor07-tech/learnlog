# Active Directory Basics & Windows Fundamentals 3

**Platform:** TryHackMe  
**Link:** https://tryhackme.com/room/winadbasics  
**Date:** 2026-07-13  
**Difficulty:** Easy  
**Topics:** Windows Security, Active Directory, Windows Domains, Domain Controller, Users, Machine Accounts, Security Groups, Organizational Units (OU)

---

## What it covers

This room introduced the core concepts of Active Directory and how Windows domains are used to centrally manage users, computers, and security in enterprise environments. I also learned about built-in Windows security features such as Microsoft Defender, Firewall, TPM, BitLocker, and Volume Shadow Copy Service (VSS), and why they are important for protecting systems.

---

## Concepts I learned

- **Windows Defender** protects Windows from malware using real-time scanning.
- **Windows Firewall** controls incoming and outgoing network traffic.
- **Microsoft Defender SmartScreen** warns or blocks malicious websites and applications.
- **TPM (Trusted Platform Module)** securely stores cryptographic keys and works with BitLocker.
- **BitLocker** encrypts the entire drive to protect data if a device is lost or stolen.
- **Volume Shadow Copy Service (VSS)** creates restore snapshots of the system that can be used to recover from problems.
- **Living Off The Land (LOTL)** is a technique where attackers abuse legitimate Windows tools like PowerShell or CMD to avoid detection.
- **Windows Domain** is a centralized way to manage users, computers, and resources in an organization.
- **Active Directory (AD)** is Microsoft's directory service that stores information about users, computers, groups, and other network objects.
- **Domain Controller (DC)** is the Windows Server that runs Active Directory and authenticates users and devices.
- **Active Directory Domain Services (AD DS)** is the core service that stores and manages Active Directory objects.
- **User Accounts** can represent either people or services running on Windows.
- **Machine Accounts** are automatically created when a computer joins the domain and always end with a `$`.
- **Security Groups** simplify permission management by assigning permissions to groups instead of individual users.
- **Organizational Units (OUs)** organize users and computers into departments so policies can be applied consistently.
- **Difference between OUs and Security Groups**
  - OUs are used for **policies**.
  - Security Groups are used for **permissions**.

---

## Tools used

- **Windows Security** — Explored built-in Windows protection features.
- **Windows Defender Firewall** — Learned how Windows controls network traffic.
- **Active Directory Users and Computers (ADUC)** — Used to manage users, computers, groups, and OUs in Active Directory.
- **TryHackMe Windows Lab** — Practiced navigating a Windows Domain Controller environment.

---

## My approach (high level)

Instead of memorizing definitions, I focused on understanding how Windows security and Active Directory work in a real company. I related concepts to a startup environment (departments, employees, permissions, and policies) so I could understand why organizations use Active Directory and how administrators manage large enterprise networks.

---

## Key takeaway

The biggest lesson today was understanding the difference between **Organizational Units (OUs)** and **Security Groups**:

- **OU = Policies (Departments)**
- **Security Group = Permissions (Resource Access)**

This is one of the most important Active Directory concepts and will be useful in future penetration testing and Active Directory attacks.

---

## Where I got stuck

- I initially confused **Domain**, **Active Directory**, and **Domain Controller**.
- I also found it difficult to understand the difference between **Security Groups** and **Organizational Units (OUs)**.
- The concepts of **Service Users**, **Machine Accounts**, and **VSS** were confusing at first, but understanding them through real-world examples made everything much clearer.