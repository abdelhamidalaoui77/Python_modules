*This project has been created as part of the 42 curriculum by alamrani42.*

# Born2beRoot

## Description

Born2beRoot is a system administration project whose goal is to introduce the fundamentals of **virtualization, Linux server administration, and security hardening**. The project consists of creating and configuring a minimal Linux server inside a virtual machine, following strict rules related to security, user management, services, and monitoring.

The objective is not only to obtain a working system, but to **understand why each technical choice is made**, and to be able to justify those choices during evaluation.

---

## Project Goals

* Understand virtualization and hypervisors
* Install and configure a minimal Linux server (no GUI)
* Apply security best practices (firewall, SSH, sudo, MAC systems)
* Manage users and permissions correctly
* Secure disk storage using encryption and LVM
* Automate system monitoring using cron

---

## Instructions

### Virtual Machine Setup

* Hypervisor: **VirtualBox** (or **UTM** on Apple Silicon)
* Operating System: **Debian (latest stable)**
* No graphical interface installed
* Snapshots are forbidden

### Services and Configuration

Only essential services are installed and enabled:

* **SSH** — remote administration (port 4242, key-based access supported)
* **cron** — task scheduling (monitoring script)
* **ufw** — firewall management
* **AppArmor** — Mandatory Access Control

Unnecessary services and graphical components are intentionally excluded to reduce the attack surface.

* SSH enabled on port **4242**
* Root login via SSH disabled
* Firewall enabled at startup
* Strong password policy enforced
* `sudo` configured with logging and restrictions
* AppArmor enabled at boot

### Monitoring

A Bash script named `monitoring.sh` runs at startup and every 10 minutes using `cron`. It displays system information (CPU, RAM, disk usage, network, users, sudo usage) to all terminals using `wall`.

---

## Security Policies

Security hardening is applied at multiple levels:

* **Firewall (UFW)** restricts incoming traffic to SSH only
* **SSH hardening** disables root login and enforces non-default port usage
* **Password policy** enforces complexity, expiration, and retry limits
* **AppArmor** confines applications using mandatory access control profiles

These layered controls reduce the impact of misconfiguration or compromise.

---

## Technical Choices and Justifications

### Operating System Choice: Debian vs Rocky Linux

**Debian** was chosen for this project.

* Debian is community-driven, stable, and well-documented
* Uses conservative package versions with long-term security support
* Better suited for learning system administration fundamentals

**Rocky Linux** is an enterprise-focused, RHEL-compatible distribution designed for production environments with strict compliance requirements.

**Conclusion:** Debian is more appropriate for Born2beRoot due to its simpler learning curve and flexibility.

---

### Security Framework: AppArmor vs SELinux

* **AppArmor** (Debian): Path-based Mandatory Access Control, profile-oriented, easier to configure and debug
* **SELinux** (Rocky): Label-based Mandatory Access Control, system-wide, more powerful but significantly more complex

**Conclusion:** AppArmor fits Debian’s philosophy and allows controlled learning without excessive configuration complexity.

---

### Firewall: UFW vs firewalld

* **UFW**: Simple, rule-based firewall interface for iptables, designed for Debian/Ubuntu
* **firewalld**: Zone-based, dynamic firewall manager used in enterprise environments (Rocky/RHEL)

**Conclusion:** UFW is sufficient and appropriate for a minimal Debian server with a single exposed service (SSH).

---

### Virtualization Tool: VirtualBox vs UTM

* **VirtualBox**: Cross-platform, mature, widely documented hypervisor
* **UTM**: QEMU-based virtualization tool designed for Apple Silicon (M1/M2)

**Conclusion:** VirtualBox is the standard choice, while UTM is used when hardware compatibility requires it.

---

## Storage Design: LVM and Disk Encryption

### Partitioning Strategy

In Linux, a partition is a logical division of a physical storage drive (like an SSD or HDD) that acts as an independent section for storing files, allowing you to organize data, run multiple operating systems (dual-boot), or separate system files from user data for easier backups and management, all mounted as folders (mount points) rather than drive letters (like C: in Windows). Key partitions include the root (/) for the OS, /home for user files, and a swap partition for virtual memory. 

The disk is partitioned using a minimal and secure layout:

* A separate `/boot` partition (unencrypted) required for system startup
* The remaining disk is encrypted using **LUKS**
* Inside the encrypted container, **LVM** is used to create logical volumes

Logical volumes typically include:

* `/` (root filesystem)
* `/home`
* `swap`
* `/root`
* `/tmp`
* `/srv`
* `/var`
* `/var/log`

This approach provides:

* Protection of data at rest (encryption)
* Flexibility to resize or add logical volumes (LVM)
* Clear separation between boot and encrypted data

- Disk partitions are encrypted using **LUKS** to protect data at rest
- **LVM (Logical Volume Manager)** is used on top of encrypted partitions to allow flexible storage management

This design separates **security (encryption)** from **storage flexibility (LVM)**.

---

## User and Privilege Management

User management follows the principle of **least privilege**:

* The `root` account exists but **cannot log in via SSH**
* A dedicated user (`alamrani42`) is created for daily administration
* This user belongs to:

  * `sudo` — for controlled privilege escalation
  * `user42` — project-required group

All administrative actions are performed using `sudo`, not direct root access.

Sudo is configured with:

* Limited password attempts
* Logging of commands and I/O
* A secure execution PATH

This ensures accountability, traceability, and reduced risk of misuse.

* Root account exists but cannot be accessed via SSH
* A dedicated user (`alamrani42`) is created and added to `sudo` and `user42` groups
* Privilege escalation is done using `sudo`, not direct root login
* All sudo actions are logged in `/var/log/sudo/`

---

## Why No Graphical Interface

A graphical interface is unnecessary and harmful on a server:

* Increases attack surface
* Consumes system resources
* Adds services unrelated to server operation

Servers are designed to be administered remotely via SSH and automation tools.

---

## Resources

### Documentation and Learning Resources

* Debian Documentation: [https://www.debian.org/doc/](https://www.debian.org/doc/)
* AppArmor: [https://apparmor.net/](https://apparmor.net/)
* SELinux (Red Hat): [https://www.redhat.com/en/topics/linux/what-is-selinux](https://www.redhat.com/en/topics/linux/what-is-selinux)
* UFW Guide: [https://www.zenarmor.com/docs/network-security-tutorials/how-to-set-up-a-firewall-with-ufw-on-debian](https://www.zenarmor.com/docs/network-security-tutorials/how-to-set-up-a-firewall-with-ufw-on-debian)
* SSH Configuration: [https://www.zenarmor.com/docs/linux-tutorials/how-to-configure-and-enable-ssh-in-ubuntu](https://www.zenarmor.com/docs/linux-tutorials/how-to-configure-and-enable-ssh-in-ubuntu)
* Disk Encryption (LUKS): [https://www.zenarmor.com/docs/linux-tutorials/linux-disk-encryption-with-luks](https://www.zenarmor.com/docs/linux-tutorials/linux-disk-encryption-with-luks)
* Cron Jobs: [https://linuxhandbook.com/crontab/](https://linuxhandbook.com/crontab/)

### AI Usage

AI was used as a **learning assistant** to:

* Clarify system administration concepts
* Validate understanding of security mechanisms
* Help structure explanations for documentation

All configuration, commands, and implementation decisions were performed manually and fully understood before use.

---

## Conclusion

This project provides a solid foundation in Linux system administration by combining virtualization, security, automation, and disciplined configuration. Born2beRoot emphasizes understanding over automation and prepares students for real-world server environments.

