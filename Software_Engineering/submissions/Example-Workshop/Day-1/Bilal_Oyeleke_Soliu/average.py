"""
Day 1 — Function under test
Student: Bilal Oyeleke Soliu
"""


def average(numbers):
    """Return the average of a list of numbers.

    Empty-list handling: returns 0.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# --- Intentionally buggy version (used for Part 3 verification) ---
# Uncomment to demonstrate failing tests:
#
# def average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / (len(numbers) - 1)
