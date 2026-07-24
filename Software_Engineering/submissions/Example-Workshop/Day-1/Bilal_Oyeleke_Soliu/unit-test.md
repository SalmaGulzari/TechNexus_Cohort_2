# Day 1 Submission: Understanding Unit Testing

**Student:** Bilal Oyeleke Soliu  
**Workshop:** Example-Workshop  
**Day:** 1

---

## Part 1: Summary

Unit testing is a software engineering practice where individual pieces of code—usually functions or methods—are tested in isolation to confirm they behave as expected. A **test case** defines a specific input and expected output. An **assertion** checks whether the actual result matches that expectation. Related test cases are grouped into a **test suite**, and a **test runner** executes them and reports pass/fail results.

Unit tests matter because they catch bugs early, document how code is supposed to work, and make refactoring safer. Instead of manually checking every change, developers can re-run automated tests and quickly see if something broke. In team projects, unit tests also act as a safety net: if one person’s change breaks another feature, failing tests surface the problem before the code reaches production. Overall, unit testing improves code quality, reduces debugging time, and builds confidence when shipping updates.

---

## Part 2: Test Results (Correct Implementation)

| Test Case              | Input           | Expected | Actual | Result |
|------------------------|-----------------|----------|--------|--------|
| Normal list            | `[2, 4, 6]`     | `4.0`    | `4.0`  | Pass   |
| Single-element list    | `[10]`          | `10.0`   | `10.0` | Pass   |
| List with negatives    | `[-2, 4, -6]`   | `-1.333…`| `-1.333…` | Pass |
| Empty list             | `[]`            | `0`      | `0`    | Pass   |

**Empty-list choice:** Return `0` when the list is empty.

All 4 tests passed with the correct `average()` implementation. See `average.py` and `test_average.py`.

---

## Part 3: Verification — Introducing a Bug

I intentionally changed the function to divide by `len(numbers) - 1` instead of `len(numbers)`. After re-running the tests:

| Test Case              | Input           | Expected | Actual (buggy) | Result |
|------------------------|-----------------|----------|----------------|--------|
| Normal list            | `[2, 4, 6]`     | `4.0`    | `6.0`          | Fail   |
| Single-element list    | `[10]`          | `10.0`   | Error / invalid| Fail   |
| List with negatives    | `[-2, 4, -6]`   | `-1.333…`| `-2.0`         | Fail   |
| Empty list             | `[]`            | `0`      | `0`            | Pass   |

The failing tests immediately showed that the average was wrong for normal and negative lists, and that a single-element list broke entirely (division by zero). Without these tests, the bug might have gone unnoticed until a user hit those cases.

### Write-Up: Why Unit Tests Protect Data Quality

Unit tests help maintain code quality by continuously checking that small pieces of logic still work after changes. When a developer introduces a bug—accidentally or while experimenting—failing tests pinpoint the broken behavior quickly, before the code is merged or deployed. This reduces the chance of defects reaching production, where they are harder and more expensive to fix. Tests also act as living documentation: new teammates can read them to understand expected inputs and outputs. Over time, a solid suite of unit tests makes refactoring safer, speeds up debugging, and supports reliable releases. In short, unit testing is a practical defense against regressions and a core habit for professional software engineering.
