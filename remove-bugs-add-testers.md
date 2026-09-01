# Plan: Clean up intentional bugs and add testable string helpers

## Context
The repo has 3 intentional bugs in `calculator.py` baked in for CI rework testing. These keep triggering auto-fixers, which is annoying. We want to remove them and add a new string utilities module with proper test coverage so the repo remains useful for CI testing workflows.

## Step 1: Fix the 3 bugs in `calculator.py`
- **Line 3**: Remove unused `import os`
- **Line 19**: Fix `multiply` to return `a * b` instead of `a + b`
- **Line 32**: Fix `power` to return `base ** exp` instead of `f"{base}^{exp}"`

## Step 2: Create `strings.py` with string manipulation functions
- `is_palindrome(s)` — check if a string reads the same forwards and backwards (case-insensitive, ignoring spaces/punctuation)
- `reverse(s)` — reverse a string
- `capitalize_words(s)` — capitalize the first letter of each word
- `count_vowels(s)` — count vowels in a string
- `is_anagram(a, b)` — check if two strings are anagrams of each other
- `truncate(s, max_len, suffix="...")` — truncate a string to max length with suffix

## Step 3: Create `test_strings.py` with tests for all string functions
- Tests for each function with edge cases (empty strings, single chars, unicode, mixed case)
- Include the new test file in the CI workflow

## Step 4: Update CI workflow to run tests on both test files
- Update `.github/workflows/test.yml` to run `pytest -v` (discovers all test files) instead of just `test_calculator.py`
- Update lint and typecheck workflows to include `strings.py`

## Step 5: Add `test_power` to `test_calculator.py`
- Currently missing test coverage for the `power` function

## Files to modify
- `calculator.py` — fix bugs
- `test_calculator.py` — add `test_power`
- `strings.py` — new file
- `test_strings.py` — new file
- `.github/workflows/test.yml` — broaden test discovery
- `.github/workflows/typecheck.yml` — add `strings.py`

## Verification
- `ruff check .` — passes lint
- `mypy calculator.py strings.py --strict` — passes type check
- `pytest -v` — all tests pass
