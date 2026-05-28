---
name: typescript-standards
description: >-
  Production TypeScript coding standards for modern strict-mode TypeScript (5.x+).
  Use when writing, reviewing, or refactoring TypeScript to ensure adherence to strict mode,
  discriminated unions, Zod validation, proper error handling, and modern patterns.
  Trigger on "make this typesafe", "TypeScript best practices", "improve these types",
  "strict mode", "type narrowing", "Zod schema", or any TypeScript code quality question.
  Not framework-specific — applies to React, Node, serverless, CLI, or any TS project.
---

# TypeScript Coding Standards

Production-quality TypeScript patterns for strict-mode TypeScript 5.x+.

## When to Use This Skill

- Writing or reviewing TypeScript code
- "Make this typesafe" / "improve these types"
- Choosing between type patterns (union vs enum, interface vs type)
- Validation at boundaries (Zod, runtime checks)
- Error handling patterns
- Any TypeScript code quality question

## Strict Mode — Non-Negotiable

Every `tsconfig.json` must include `"strict": true`. This enables:
- `strictNullChecks` — no implicit `null`/`undefined`
- `noImplicitAny` — no untyped variables
- `strictFunctionTypes` — correct function variance
- `noUncheckedIndexedAccess` — array/object access returns `T | undefined`

If inheriting a non-strict codebase, enable strict incrementally per-file with `// @ts-strict` or via `strictNullChecks` first, then full `strict`.

## Type Design

### Discriminated Unions Over Enums

Discriminated unions are the idiomatic way to model variants in TypeScript. They give exhaustive checking, work with pattern matching, and serialize cleanly.

```typescript
// GOOD — discriminated union
type Result =
  | { status: "success"; data: User }
  | { status: "error"; error: string }
  | { status: "loading" };

function handle(result: Result) {
  switch (result.status) {
    case "success": return result.data;  // TS knows .data exists
    case "error": throw new Error(result.error);
    case "loading": return null;
    // No default — TS will error if a variant is added and not handled
  }
}

// AVOID — string enums add runtime overhead for no benefit
enum Status { Success = "success", Error = "error" }
```

Use `const` objects when you need runtime values AND type safety:

```typescript
const HTTP_METHOD = {
  GET: "GET",
  POST: "POST",
  PUT: "PUT",
  DELETE: "DELETE",
} as const;

type HttpMethod = (typeof HTTP_METHOD)[keyof typeof HTTP_METHOD];
```

### Prefer `type` Over `interface` (Unless Extending)

`type` is more versatile (unions, intersections, mapped types). Use `interface` only when you need declaration merging or class `implements`.

```typescript
// Prefer type for data shapes
type User = {
  id: string;
  email: string;
  name: string;
};

// Use interface when a class implements it
interface Repository<T> {
  findById(id: string): Promise<T | null>;
  save(entity: T): Promise<T>;
}
```

### Narrow, Don't Assert

Use type narrowing (guards, `in`, `instanceof`, discriminants) instead of `as` assertions.

```typescript
// BAD — assertion hides bugs
const user = response.data as User;

// GOOD — narrowing proves safety
if (isUser(response.data)) {
  const user = response.data;  // TS knows this is User
}

// Type guard function
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "email" in value
  );
}
```

### Use `unknown` Over `any`

`any` disables type checking entirely. `unknown` forces you to narrow before using.

```typescript
// BAD
function parse(input: any) {
  return input.name;  // No error, but could crash
}

// GOOD
function parse(input: unknown) {
  if (typeof input === "object" && input !== null && "name" in input) {
    return (input as { name: string }).name;
  }
  throw new Error("Invalid input");
}

// BETTER — use Zod (see Validation section)
```

## Validation at Boundaries

Validate external data (API responses, user input, config, env vars) at the system boundary using Zod. Trust the types internally after validation.

```typescript
import { z } from "zod";

// Define schema once — derives both runtime validation and static type
const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(1),
  role: z.enum(["admin", "user", "viewer"]),
});

type User = z.infer<typeof UserSchema>;

// At the boundary: validate
function handleRequest(body: unknown): User {
  return UserSchema.parse(body);  // Throws ZodError if invalid
}

// Inside the system: trust the type, no re-validation
function processUser(user: User) {
  // user.role is guaranteed to be "admin" | "user" | "viewer"
}
```

### Environment Variables

```typescript
const EnvSchema = z.object({
  DATABASE_URL: z.string().url(),
  API_KEY: z.string().min(1),
  PORT: z.coerce.number().default(3000),
  NODE_ENV: z.enum(["development", "production", "test"]).default("development"),
});

export const env = EnvSchema.parse(process.env);
```

## Error Handling

### Result Pattern Over Try-Catch Everywhere

For expected failures (validation, not-found, business rule violations), use a Result type. Reserve `try-catch` for unexpected errors at the boundary.

```typescript
type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function findUser(id: string): Result<User, "not-found" | "db-error"> {
  const user = db.get(id);
  if (!user) return { ok: false, error: "not-found" };
  return { ok: true, value: user };
}

// Caller handles both cases — can't forget
const result = findUser("123");
if (!result.ok) {
  // result.error is typed as "not-found" | "db-error"
  return;
}
// result.value is User
```

### Custom Error Classes

When you need error hierarchies (rare — prefer Result for business logic):

```typescript
class AppError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly statusCode: number = 500,
  ) {
    super(message);
    this.name = this.constructor.name;
  }
}

class NotFoundError extends AppError {
  constructor(resource: string, id: string) {
    super(`${resource} ${id} not found`, "NOT_FOUND", 404);
  }
}
```

## Module Patterns

### Barrel Exports — Use Sparingly

Barrel files (`index.ts` re-exporting everything) cause bundle bloat and circular dependency issues. Use them only at package boundaries, not within a package.

```typescript
// BAD — barrel inside a feature
// features/users/index.ts
export * from "./service";
export * from "./repository";
export * from "./types";
export * from "./validation";

// GOOD — import directly
import { UserService } from "./features/users/service";
```

### Colocation Over Separation

Group by feature/domain, not by file type.

```
# BAD — by file type
src/
  controllers/
  services/
  repositories/
  types/

# GOOD — by feature
src/
  users/
    service.ts
    repository.ts
    types.ts
    routes.ts
  orders/
    service.ts
    repository.ts
    types.ts
    routes.ts
```

## Async Patterns

### Always Await — No Floating Promises

```typescript
// BAD — promise result silently discarded
saveUser(user);

// GOOD
await saveUser(user);

// If intentionally fire-and-forget, be explicit
void saveUser(user);  // eslint: no-floating-promises allows void
```

### Prefer `Promise.all` for Independent Operations

```typescript
// BAD — sequential when they could be parallel
const user = await getUser(id);
const orders = await getOrders(id);

// GOOD — parallel
const [user, orders] = await Promise.all([
  getUser(id),
  getOrders(id),
]);
```

## Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| Variables, functions | `camelCase` | `getUserById` |
| Types, interfaces, classes | `PascalCase` | `UserService` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_RETRY_COUNT` |
| Files | `kebab-case` | `user-service.ts` |
| Boolean variables | `is`/`has`/`should` prefix | `isActive`, `hasPermission` |
| Type parameters | Single uppercase or descriptive | `T`, `TInput`, `TOutput` |

Do not prefix interfaces with `I` (`IUserService`) or types with `T` (`TUser`). The type system makes these obvious.
