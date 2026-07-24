"""
Day 1 — Password hashing helpers (SHA-256 + salt)
Student: Karim Ismail Abdellah Mohammed
Track: CyberSecurity & Networking

Note: SHA-256 is used here for learning. Production systems should use
bcrypt, scrypt, or Argon2 with proper work factors.
"""

import hashlib
import secrets


def hash_password(password, salt=None):
    """Return SHA-256 hex digest of password, optionally salted."""
    material = f"{salt}{password}" if salt is not None else password
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def generate_salt(length: int = 8) -> str:
    """Generate a random hex salt."""
    return secrets.token_hex(length // 2)


# Example stored credentials for the demo (salted)
STORED_USERS = {
    "alice": {
        "salt": "a1b2c3d4",
        "password_hash": None,  # filled below
    }
}

STORED_USERS["alice"]["password_hash"] = hash_password(
    "Summer2024!", STORED_USERS["alice"]["salt"]
)
