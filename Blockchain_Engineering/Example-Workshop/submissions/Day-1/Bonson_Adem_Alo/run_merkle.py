"""
Day 1 — Demo: build Merkle Tree and show tamper detection
Student: Bonson Adem Alo

Run with:
    python run_merkle.py
"""

from merkle_tree import build_tree_levels, merkle_root


def short(h: str, n: int = 16) -> str:
    return h[:n]


def print_levels(title, blocks):
    print(f"\n=== {title} ===")
    print(f"Blocks: {blocks}")
    levels = build_tree_levels(blocks)
    labels = ["Leaves", "Non-leaf", "Root"]
    for i, level in enumerate(levels):
        label = labels[i] if i < len(labels) else f"Level {i}"
        print(f"{label}: {[short(h) for h in level]}")
    print(f"Merkle root: {short(merkle_root(blocks))}")


if __name__ == "__main__":
    original = ["Block1", "Block2", "Block3", "Block4"]
    tampered = ["Block1", "Block2", "Block3_TAMPERED", "Block4"]

    print_levels("Original tree", original)
    print_levels("After tampering Block3", tampered)

    root_a = merkle_root(original)
    root_b = merkle_root(tampered)
    print("\n=== Integrity check ===")
    print(f"Roots match? {root_a == root_b}")
    print("Conclusion: changing one leaf changes the Merkle root.")
