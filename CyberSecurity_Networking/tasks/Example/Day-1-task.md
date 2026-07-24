# Task: Understanding Password Hashing

## Objective

The goal of this task is to help you understand why passwords should never be stored in plain text, how hashing works at a basic level, and why adding a salt improves security.

## Background

When users create accounts, systems must store credentials in a way that limits damage if a database is leaked. A **hash function** turns a password into a fixed-length digest that is hard to reverse. Storing hashes (ideally with a unique **salt** per user) is a core cybersecurity practice for protecting authentication data.

## Task Instructions

### Part 1: Understanding the Basics

1. **Research**:

   - Look up the definition of a cryptographic hash function.
   - Understand the terms: plain text, hash digest, salt, and rainbow table.
   - Find out why unsalted hashes are weaker than salted hashes.

2. **Summarize**:
   - Write a short paragraph (100–150 words) explaining password hashing and why it is used in secure systems.

### Part 2: Hashing in Practice

1. **Hash Plain Passwords**:

   - Choose 3 sample passwords (do **not** use real personal passwords).
   - Hash each one with SHA-256 and record the digests.

2. **Add a Salt**:

   - For the same 3 passwords, generate a unique salt for each.
   - Hash `salt + password` (or `password + salt`) and record the new digests.

3. **Compare**:

   - Show that two users with the same password get **different** salted hashes when salts differ.

4. **Structured Representation**:
   - Present a table with: password, salt (if any), and hash digest (truncated digests are fine).

### Part 3: Verification

1. **Login Check Simulation**:

   - Write a small function that verifies a login attempt by hashing the provided password with the stored salt and comparing it to the stored hash.
   - Show one successful match and one failed match.

2. **Write-Up**:
   - Write a short explanation (100–150 words) on how hashing and salting help protect users if a password database is stolen.

## Deadline

- Submit your completed task by 12PM Tomorrow.

## Resources

- [Cryptographic hash function – Wikipedia](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Salt (cryptography) – Wikipedia](https://en.wikipedia.org/wiki/Salt_(cryptography))
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

Good luck!
