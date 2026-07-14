# Active Directory Basics (Practices)

**Platform:** TryHackMe  
**Link:** https://tryhackme.com/room/winadbasics  
**Date:** 2026-07-14  
**Difficulty:** Easy  
**Topics:** Active Directory Administration, OUs, User Management, Delegation, Computer Management, Group Policy (GPO)

---

## What it covers

This practical section focused on performing common Active Directory administration tasks in a Windows Domain environment. I practiced managing Organizational Units (OUs), users, delegation, computers, and learned how Group Policy Objects (GPOs) are used to centrally manage users and computers.

---

## Concepts I learned

- Deleted an Organizational Unit (OU) after removing accidental deletion protection.
- Compared the company's organizational chart with Active Directory and updated users accordingly.
- Learned **Delegation**, where a user can be given limited administrative permissions without becoming a Domain Admin.
- Reset another user's password using delegated permissions through PowerShell.
- Forced a user to change their password at the next logon for better security.
- Learned the **Principle of Least Privilege** by giving only the permissions required for a specific task.
- Organized computers into **Workstations** and **Servers** OUs instead of leaving everything in the default Computers container.
- Understood why different OUs allow different security policies to be applied.
- Learned that a **Group Policy Object (GPO)** is a collection of policies that can be linked to OUs or the domain.
- Understood the GPO workflow:
  - Create GPO
  - Configure policies
  - Link it to an OU or Domain
  - Apply policies to users or computers
- Learned that policies can be refreshed immediately using `gpupdate /force`.

---

## Tools used

- **Active Directory Users and Computers (ADUC)** — Managed OUs, users, and computers.
- **Group Policy Management (GPMC)** — Created and linked Group Policy Objects (GPOs).
- **Windows PowerShell** — Reset user passwords and forced password changes.
- **Remote Desktop (RDP)** — Logged into different domain user accounts for testing.

---

## My approach (high level)

I focused on understanding how a Windows administrator manages a real company instead of just completing the lab. I related each task to a real business scenario, such as delegating password resets to IT support, organizing computers into different OUs, and applying policies centrally using GPOs instead of configuring each computer manually.

---

## Key takeaway

The biggest lesson was understanding how **Group Policy Objects (GPOs)** work.

> **OU = Who receives the policy**  
> **GPO = What policy is applied**  
> **Link = Connects the GPO to the OU or Domain**

This showed me how administrators can manage hundreds or thousands of computers from a central location.

---

## Where I got stuck

- I initially found **Group Policy Objects (GPOs)** confusing, especially the relationship between OUs and GPOs.
- I also wondered whether I needed to memorize PowerShell commands, but I learned that understanding the purpose of the commands is more important than memorizing their syntax at this stage.
- The concept became much clearer after using real-world company examples and understanding why GPOs are linked to specific OUs.