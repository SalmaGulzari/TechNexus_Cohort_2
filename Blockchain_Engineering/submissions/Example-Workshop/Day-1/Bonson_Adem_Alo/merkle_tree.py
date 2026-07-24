"""
Day 1 — Simple Merkle Tree builder
Student: Bonson Adem Alo
Track: Blockchain Engineering
"""

import hashlib


def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def merkle_root(blocks):
    """Build a Merkle root from a list of data blocks (strings)."""
    if not blocks:
        return None

    level = [sha256_hex(block) for block in blocks]

    while len(level) > 1:
        next_level = []
        # If odd number of nodes, duplicate the last one
        if len(level) % 2 == 1:
            level.append(level[-1])
        for i in range(0, len(level), 2):
            combined = level[i] + level[i + 1]
            next_level.append(sha256_hex(combined))
        level = next_level

    return level[0]


def build_tree_levels(blocks):
    """Return all levels of the Merkle Tree (leaves → root)."""
    if not blocks:
        return []

    levels = []
    level = [sha256_hex(block) for block in blocks]
    levels.append(level)

    while len(level) > 1:
        if len(level) % 2 == 1:
            level = level + [level[-1]]
        next_level = []
        for i in range(0, len(level), 2):
            next_level.append(sha256_hex(level[i] + level[i + 1]))
        level = next_level
        levels.append(level)

    return levels
