---
description: >
  Core software engineering principles that apply to all code, in any language, in any project.
  These are non-negotiable defaults — deviate only when there is a specific, articulated reason.
applyTo: "**"
---

# Software Engineering Defaults

These principles apply to **all code you write or modify**, regardless of project or language. They complement project-specific instructions (which may override or extend them) and domain-specific skills (architecture-patterns, refactor, dignified-python, python-testing-patterns).

## 1. Separation of Concerns

Every module, class, or function should have **one reason to change**. When you notice a unit doing two unrelated things (e.g., UI rendering AND hardware I/O, config parsing AND business logic), split them.

- **State ownership:** Each piece of mutable state should have exactly one owner. Other code reads it via accessor or receives it as an argument — never reaches in and mutates it.
- **Side-effect isolation:** Pure logic (compute, transform, decide) lives in functions with no side effects. I/O, network calls, and hardware commands live in thin wrappers at the boundary. This makes the logic testable without mocking the world.
- **Thin entry points, thick modules:** CLI scripts, API handlers, and UI callbacks should be thin dispatchers. They parse input, call a module, and format output. The real logic lives in importable, testable modules.

## 2. Deep Modules Over Shallow Modules

A **deep module** provides a lot of functionality behind a simple interface. A **shallow module** has an interface nearly as complex as its implementation — it adds indirection without hiding complexity.

- **Measure depth by leverage, not lines of code.** A module is deep when callers get significant capability per unit of interface they must learn. A one-method class wrapping a one-line operation is shallow.
- **The deletion test.** Imagine deleting the module. If complexity vanishes, it was a pass-through (shallow — remove it). If complexity reappears across N callers, it was earning its keep (deep — keep it).
- **One adapter = hypothetical seam. Two adapters = real seam.** Don't introduce an abstraction boundary unless something actually varies across it. A `UserRepositoryInterface` with exactly one implementation and no tests using a fake is premature.
- **Interfaces include more than the type signature.** An interface is everything a caller must know: types, invariants, error modes, ordering constraints, performance characteristics. Reducing that surface area is the goal.

## 3. Fail Fast, Fail Loud

- **Validate at system boundaries** — where external input enters (CLI args, config files, API requests, sensor data). Once validated, trust the data internally; don't re-validate at every layer.
- **Use strict parsing over lenient defaults.** A config key typo should raise an error, not silently fall back to a default. Prefer explicit "key not found" errors over `dict.get(key, some_default)` for required fields.
- **Crash > silent corruption.** An `AssertionError` that stops a run is better than a subtle numerical bug that wastes hours of compute. Use assertions for invariants.
- **Define errors out of existence.** Design interfaces so invalid states cannot be constructed. A function that accepts `NonEmptyList` doesn't need to handle the empty case. A `Money` type that rejects negatives at construction means no downstream code ever checks for negative amounts. Prevention beats detection.

## 4. Explicitness Over Magic

- **No hidden state.** Global mutable state, module-level singletons mutated at runtime, and monkey-patching make code unpredictable. Pass dependencies explicitly.
- **No stringly-typed interfaces.** Prefer enums, dataclasses, or typed dicts over raw strings/dicts for structured data that crosses function boundaries.
- **Name things for what they mean,** not how they're implemented. `target_position` > `vec3`, `is_gripper_closed` > `flag2`.

## 5. Conceptual Integrity

A system should feel like one mind designed it. Consistent naming, consistent error handling, consistent patterns throughout.

- **Match the conventions already in the codebase.** When adding code, adopt the existing style — don't introduce a second way of doing the same thing. If the project uses Result types for errors, don't add try-catch in new code. If routes are in `kebab-case`, don't add a `camelCase` one.
- **One pattern per concern.** If the codebase has a way to do config, logging, validation, or error handling — use it. Don't invent a parallel system.
- **This matters especially with agent-generated code,** which tends to introduce stylistic drift. Actively resist it.

## 6. DRY — but Don't Over-Abstract

- **Duplicate code is a signal, not a sin.** Two occurrences in nearby code may be coincidence. Three occurrences, or two in distant modules, warrant extraction.
- **Don't create abstractions for one-time operations.** A helper function used once adds indirection without reducing complexity. Inline it.
- **Prefer composition over inheritance.** Mixins and deep class hierarchies make code hard to trace. Compose small objects with clear interfaces.

## 7. Reversibility

Prefer decisions that are easy to change. When unsure between two approaches, pick the one that's cheapest to reverse.

- **Isolate decisions behind interfaces.** The choice of database, queue, or external service should live behind a seam so it can be swapped without rewriting business logic.
- **Avoid lock-in at the core.** Framework-specific decorators and ORM models belong at the edges, not in the domain layer.
- **Small, reversible steps over big bets.** A feature flag is cheaper than a rewrite. A thin adapter is cheaper than a migration.

## 8. Coupling and Cohesion

- **High cohesion:** Things that change together should live together (same module/file). If editing feature X requires touching 5 files, the code is poorly cohesioned.
- **Low coupling:** Modules should interact through narrow, stable interfaces. Passing a whole object when you only need two fields creates unnecessary coupling.
- **Dependency direction:** High-level policy should not depend on low-level detail. Both should depend on abstractions (interfaces/protocols). A training script should not import from a hardware driver; both should talk through a shared interface.

## 9. Defensive Design for Long-Running Processes

- **Idempotent operations where possible.** If a process can crash and restart, repeated execution of the same step should produce the same result.
- **Checkpoint and resume.** Any process that runs longer than a few minutes should save progress so it can resume from the last good state, not restart from scratch.
- **Resource cleanup.** Use context managers (`with` statements) and finally blocks. Don't rely on graceful shutdown — assume the process can die at any point.

## 10. Testing and Testability

- **Write code that is testable by design.** If a function is hard to test, that's a design smell — it probably has too many responsibilities or hidden dependencies.
- **Test behavior, not implementation.** Assert on outputs and observable effects, not on internal method calls or data structure shapes that might change.
- **Keep test setup minimal.** If a test needs 50 lines of setup, the code under test probably needs refactoring — not a more elaborate test fixture.

## 11. Language Defaults

Default to **Python** or **TypeScript** for all new projects unless there is a specific, articulated reason to use something else.

- **Python** — APIs (FastAPI), AI/ML, data processing, scripting, automation, agents
- **TypeScript** — Frontend (React), full-stack web apps, serverless functions, CLI tools

Choose based on where the project's gravity sits: if it's primarily backend/AI/data, start with Python. If it's primarily UI or full-stack web, start with TypeScript. Don't mix both in the same service without good reason.

Plain HTML/CSS/JS is always fine for simple local dashboards and single-file tools — no framework required.

If a project genuinely needs a systems language (distributable binary, extreme performance, no-runtime-dependency CLI), evaluate Go or Rust at that point — don't pre-commit to one.
