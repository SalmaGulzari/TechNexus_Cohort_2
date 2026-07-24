"""
Day 1 — Unit tests for average()
Student: Bilal Oyeleke Soliu

Run with:
    python test_average.py
"""

from average import average


def run_tests():
    tests = [
        {
            "name": "Normal list",
            "input": [2, 4, 6],
            "expected": 4.0,
        },
        {
            "name": "Single-element list",
            "input": [10],
            "expected": 10.0,
        },
        {
            "name": "List with negatives",
            "input": [-2, 4, -6],
            "expected": sum([-2, 4, -6]) / 3,
        },
        {
            "name": "Empty list",
            "input": [],
            "expected": 0,
        },
    ]

    passed = 0
    failed = 0

    print("Running unit tests for average()\n")

    for test in tests:
        try:
            actual = average(test["input"])
            # Allow small floating-point tolerance
            ok = abs(actual - test["expected"]) < 1e-9
        except Exception as exc:
            actual = f"Error: {exc}"
            ok = False

        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1

        print(f"[{status}] {test['name']}")
        print(f"       input:    {test['input']}")
        print(f"       expected: {test['expected']}")
        print(f"       actual:   {actual}\n")

    print(f"Results: {passed} passed, {failed} failed out of {len(tests)}")
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    raise SystemExit(0 if success else 1)
