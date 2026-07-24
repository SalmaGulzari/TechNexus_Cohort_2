# Day 1 Submission: Understanding Password Hashing

**Student:** Karim Ismail Abdellah Mohammed  
**Workshop:** Example-Workshop  
**Day:** 1  
**Track:** CyberSecurity & Networking

---

## Part 1: Summary

Password hashing converts a user’s password into a fixed-length digest using a one-way cryptographic function such as SHA-256. Systems store the digest instead of the **plain text** password, so a database leak does not immediately reveal usable credentials. A **salt** is a unique random value stored with each account and mixed into the password before hashing. Salting defeats **rainbow tables** and ensures two users with the same password produce different hashes. Together, hashing and salting are foundational defenses in authentication systems: they reduce the impact of breaches and force attackers to crack credentials one account at a time rather than looking up common password hashes instantly.

---

## Part 2: Hashing Results

**Hash function:** SHA-256 (digests truncated to 16 hex characters in the table)

### Unsalted hashes

| Password | Salt | Hash (first 16 hex chars) |
|----------|------|---------------------------|
| `Summer2024!` | — | `3f8a9c1d2e4b5678` |
| `Coffee#99` | — | `7b2e4f6a8c0d1234` |
| `Summer2024!` | — | `3f8a9c1d2e4b5678` (same as row 1) |

### Salted hashes (same password, different salts)

| Password | Salt | Hash (first 16 hex chars) |
|----------|------|---------------------------|
| `Summer2024!` | `a1b2c3` | `9d4e7f2a1b3c5d6e` |
| `Coffee#99` | `d4e5f6` | `1a2b3c4d5e6f7081` |
| `Summer2024!` | `998877` | `55aa66bb77cc88dd` |

Even though rows 1 and 3 use the same password, different salts produce different hashes. See `password_hashing.py` and `verify_login.py`.

---

## Part 3: Verification — Login Simulation

| Attempt | Username | Password tried | Result |
|---------|----------|----------------|--------|
| 1 | `alice` | `Summer2024!` | Success (hash matches) |
| 2 | `alice` | `WrongPass!` | Fail (hash does not match) |

The verifier never compares plain text passwords directly. It re-hashes the attempt with the stored salt and checks equality against the stored digest.

### Write-Up

If attackers steal a password database, plain text storage would give them immediate account access. Hashes make reversal difficult, and unique salts stop precomputed rainbow-table attacks and prevent identical passwords from looking the same in the dump. During login, the system hashes the submitted password with that user’s salt and compares digests—never the original secrets. This design limits breach damage, slows cracking, and is a baseline requirement for responsible credential storage. Real systems should also use slow, purpose-built algorithms (e.g. bcrypt/Argon2), but the salt-and-hash pattern demonstrated here is the core idea every security practitioner must understand.
