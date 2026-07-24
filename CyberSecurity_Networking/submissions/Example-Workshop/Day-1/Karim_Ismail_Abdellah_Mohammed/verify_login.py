"""
Day 1 — Demo: hash passwords and verify login attempts
Student: Karim Ismail Abdellah Mohammed

Run with:
    python verify_login.py
"""

from password_hashing import STORED_USERS, generate_salt, hash_password


def verify_login(username: str, password_attempt: str) -> bool:
    user = STORED_USERS.get(username)
    if not user:
        return False
    attempt_hash = hash_password(password_attempt, user["salt"])
    return attempt_hash == user["password_hash"]


def main():
    samples = ["Summer2024!", "Coffee#99", "Summer2024!"]

    print("=== Unsalted hashes ===")
    for pwd in samples:
        digest = hash_password(pwd)
        print(f"password={pwd!r}  hash={digest[:16]}...")

    print("\n=== Salted hashes (unique salt each time) ===")
    for pwd in samples:
        salt = generate_salt()
        digest = hash_password(pwd, salt)
        print(f"password={pwd!r}  salt={salt}  hash={digest[:16]}...")

    print("\n=== Login verification ===")
    ok = verify_login("alice", "Summer2024!")
    bad = verify_login("alice", "WrongPass!")
    print(f"alice + correct password -> {'SUCCESS' if ok else 'FAIL'}")
    print(f"alice + wrong password   -> {'SUCCESS' if bad else 'FAIL'}")


if __name__ == "__main__":
    main()
