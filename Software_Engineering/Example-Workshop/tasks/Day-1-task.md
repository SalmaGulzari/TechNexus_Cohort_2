# Task: Understanding Unit Testing

## Objective

The goal of this task is to help you understand the basic concept of unit testing, why it matters in software engineering, and how to write simple tests that catch bugs early.

## Background

Unit testing is a software testing practice where individual units of code—usually functions or methods—are tested in isolation. Each test checks that a small piece of logic behaves as expected for given inputs. Unit tests help developers catch regressions, document intended behavior, and refactor code with more confidence.

## Task Instructions

### Part 1: Understanding the Basics

1. **Research**:

   - Look up the definition of a unit test.
   - Understand the terms: test case, assertion, test suite, and test runner.
   - Find out why unit tests are important in software development.

2. **Summarize**:
   - Write a short paragraph (100–150 words) explaining what unit testing is and why it is used in software engineering.

### Part 2: Writing Your First Tests

1. **Function Under Test**:

   - Write a small function that takes a list of numbers and returns their average.
   - Handle the empty-list case by returning `0` (or raising a clear error—state your choice).

2. **Test Cases**:

   - Write at least **4** test cases covering:
     - A normal list (e.g. `[2, 4, 6]`)
     - A single-element list
     - A list with negative numbers
     - An empty list

3. **Run the Tests**:

   - Use any simple test approach you prefer (e.g. Python’s `unittest` / `pytest`, JavaScript’s built-in `assert`, or manual checks with clear pass/fail output).
   - Confirm that all tests pass for the correct implementation.

4. **Visual / Structured Representation**:
   - Present your results in a simple table or list showing each test case, its input, expected output, and actual result (Pass/Fail).

### Part 3: Verification

1. **Introduce a Bug**:

   - Intentionally change your average function so it is wrong (e.g. divide by `len(list) - 1`, or skip the last element).
   - Re-run your tests and show which tests fail.
   - Explain how the failing tests helped you detect the problem.

2. **Write-Up**:
   - Write a short explanation (100–150 words) on how unit tests help maintain code quality and prevent bugs from reaching production.

## Deadline

- Submit your completed task by 12PM Tomorrow.

## Resources

- [Unit Testing – Wikipedia](https://en.wikipedia.org/wiki/Unit_testing)
- [What is Unit Testing? (IBM)](https://www.ibm.com/topics/unit-testing)
- [pytest Getting Started](https://docs.pytest.org/en/stable/getting-started.html) (optional, if using Python)

---

Good luck!
