---
name: tdd
description: >-
  Test-driven development with a red-green-refactor loop. Builds features or fixes bugs
  one vertical slice at a time. Use when user wants to build features or fix bugs using TDD,
  mentions "red-green-refactor", "test-first", "write tests for this", wants integration tests,
  or asks for test-driven development. Works with any language — Python, TypeScript, Go, etc.
  For language-specific test tooling (pytest, vitest, jest), defer to language-specific skills.
---

# Test-Driven Development

TDD is not "write all tests, then write all code." It is a vertical slicing discipline that applies to any language.

## Philosophy

Tests verify **behavior through public interfaces**, not implementation details. A good test reads like a specification — "user can checkout with valid cart" tells you what capability exists. These tests survive refactors because they don't care about internal structure.

**Good tests** are integration-style: they exercise real code paths through public APIs. They describe _what_ the system does, not _how_ it does it.

**Bad tests** are coupled to implementation: they mock internal collaborators, test private methods, or verify through external means (like querying a database directly instead of using the interface). Warning sign: your test breaks when you refactor, but behavior hasn't changed. If you rename an internal function and tests fail, those tests were testing implementation, not behavior.

## Anti-Pattern: Horizontal Slices

**DO NOT write all tests first, then all implementation.** This is "horizontal slicing" — treating RED as "write all tests" and GREEN as "write all code."

This produces poor tests because:
- Tests written in bulk test *imagined* behavior, not *actual* behavior
- You test the *shape* of things (data structures, function signatures) rather than user-facing behavior
- Tests become insensitive to real changes — they pass when behavior breaks
- You commit to test structure before understanding the implementation

## The Correct Approach: Vertical Slices (Tracer Bullets)

One test, one implementation, repeat. Each test responds to what you learned from the previous cycle.

```
WRONG (horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
```

## Workflow

### 1. Planning

When exploring the codebase, use the project's domain glossary (`CONTEXT.md`) so that test names and interface vocabulary match the project's language, and respect ADRs in the area you're touching.

Before writing any code:

- Confirm with user what interface changes are needed
- Confirm which behaviors to test (prioritize — you can't test everything)
- Identify opportunities for deep modules (small interface, deep implementation)
- Design interfaces for testability
- List the behaviors to test (not implementation steps)
- Get user approval on the plan

Ask: "What should the public interface look like? Which behaviors are most important to test?"

### 2. Tracer Bullet

Write ONE test that confirms ONE thing about the system:

```
RED:   Write test for first behavior → test fails
GREEN: Write minimal code to pass → test passes
```

This is the tracer bullet — proves the path works end-to-end.

### 3. Incremental Loop

For each remaining behavior:

```
RED:   Write next test → fails
GREEN: Minimal code to pass → passes
```

Rules:
- One test at a time
- Only enough code to pass current test
- Don't anticipate future tests
- Keep tests focused on observable behavior

### 4. Refactor

After all tests pass, look for refactoring opportunities:

- Extract duplication
- Deepen modules (move complexity behind simple interfaces)
- Apply SOLID principles where natural
- Consider what new code reveals about existing code
- Run tests after each refactor step

**Never refactor while RED.** Get to GREEN first.

## Mocking Guidelines

- **Mock at seams, not internals.** Mock the external dependencies your module talks to (databases, APIs, file systems), not internal collaborators within the module.
- **If you need to mock an internal function to test, the design needs work** — the module probably has too many responsibilities.
- **Prefer in-memory fakes over mocks** when the interface is simple. A dict-backed `InMemoryUserRepo` is more readable and less brittle than a mock with 10 configured return values.
- **Never mock what you don't own** by name. Wrap third-party libraries behind your own interface, then mock that interface.

## Per-Cycle Checklist

```
[ ] Test describes behavior, not implementation
[ ] Test uses public interface only
[ ] Test would survive internal refactor
[ ] Code is minimal for this test
[ ] No speculative features added
```

## After the Feature Is Done

Ask: **what would have prevented the bugs you found?** If the answer involves architectural change (no good test seam, tangled callers, hidden coupling), hand off to the `refactor` or `architecture-patterns` skill with the specifics. Make the recommendation _after_ the feature is in, not before — you have more information now.
