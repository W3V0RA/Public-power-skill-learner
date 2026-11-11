# 2026-11-10 | AI Power Skill #25 | Stale-Worker Fencing for Autonomous Agents

**Category:** agents, automation, distributed workflows and guardrails  
**Practice status:** PENDING

## Core principle

A lease timeout allows work to be reassigned. It does not stop the old worker
from resuming later. Give each lease generation a monotonically increasing
fencing token and require the resource being changed to reject an older token.

```text
claim 7 → pause → recover → claim 8 → token 7 rejected → token 8 accepted
```

## What the capability is

Stale-worker fencing protects a shared job, record, file, browser session or
deployment from late commands issued by a superseded worker.

A useful lease binds:

- Resource identifier
- Holder identity
- Scope
- Expiration
- Monotonic fencing token

The worker presents the token with each mutation. The authoritative resource
accepts the command only when the job is active, the owner matches and the token
is current. Policy, approval, tenant and budget checks remain separate.

Kubernetes Lease objects support heartbeats and leader election with holder,
renewal, duration and transition fields. The AWS DynamoDB Lock Client similarly
uses conditional updates and changing record-version numbers. These systems
illustrate an important lesson: coordination state must change across ownership
generations, and writes must be conditional on current state.

Primary references:

- https://kubernetes.io/docs/concepts/architecture/leases/
- https://kubernetes.io/docs/reference/kubernetes-api/coordination/lease-v1/
- https://aws.amazon.com/blogs/database/building-distributed-locks-with-the-dynamodb-lock-client/
- https://research.google/pubs/the-chubby-lock-service-for-loosely-coupled-distributed-systems/

## Why it matters

Agent workflows pause unpredictably during model calls, browser operations,
external tools and network failures. A retry can begin while the original
attempt is merely delayed. Without fencing, the old attempt may overwrite a
newer checkpoint, mark a job complete, send a duplicate action or promote an
obsolete artifact.

Leases improve availability. Fencing protects correctness after recovery.

## What makes it non-obvious

### Expiration does not revoke a running process

The coordinator can decide that a lease expired, but a paused worker may never
observe that decision.

### Identity is not generation

A stable worker name can acquire the same job twice. Both executions have the
same identity, so the lease needs a generation number.

### Random identifiers do not establish order

A random identifier can uniquely name a lease but usually cannot prove which
lease is newer. Fencing needs a monotonic sequence or comparable revision.

### Worker-side clock checks are weak

The resource boundary should compare persisted state atomically immediately
before mutation. A worker's local clock or cached lease is not authoritative.

### Idempotency is complementary

Idempotency deduplicates the same logical command. Fencing rejects a command
from an obsolete generation, even when it has a different command identifier.

### Freshness is not authorization

A current token does not authorize spending, publishing, production release,
customer contact or private-data access.

## Advanced versus typical use

| Typical use | Advanced use |
|---|---|
| Set a timeout | Assign a monotonic generation |
| Check worker identity | Check identity and generation |
| Retry after expiry | Fence the old attempt first |
| Trust cancellation | Assume the old worker may resume |
| Validate at the worker | Validate at the resource boundary |
| Record stale writes | Reject them before mutation |
| Use one global token | Scope tokens to one resource |
| Treat lease as permission | Recheck policy and approval |

## Immediate applications

| Workflow | Fenced resource | Rejected stale action |
|---|---|---|
| Coding agent | Branch or deployment candidate | Old run promotes obsolete code |
| Sales automation | Account-action record | Overlapping run sends again |
| Research agent | Decision packet | Late report replaces a newer decision |
| Marketplace worker | Listing or transaction | Old eligibility decision is committed |
| Browser agent | Session or form workflow | Delayed tab submits after handoff |
| Data pipeline | Dataset partition | Old job overwrites a newer output |

## Minimal command contract

```json
{
  "resource_id": "job-123",
  "holder_id": "worker-a",
  "fencing_token": 8,
  "command_id": "stable-idempotency-key",
  "expected_state_version": 17,
  "scope": ["checkpoint:write"]
}
```

Useful outcomes include:

- `ACCEPTED`
- `DUPLICATE_NOOP`
- `STALE_FENCE_REJECTED`
- `NOT_CURRENT_OWNER`
- `LEASE_NOT_ACTIVE`
- `STATE_VERSION_CONFLICT`
- `POLICY_OR_APPROVAL_REQUIRED`

## Implementation workflow

1. Name the exact mutable resource.
2. Reuse or create a monotonically increasing claim generation.
3. Return that token with the lease.
4. Present it on every mutation.
5. Lock or conditionally compare persisted state before writing.
6. Preserve idempotency, isolation, policy, approval and budget gates.
7. Test pause, expiry, recovery, reacquisition and late completion.

## Ready-to-copy prompt

```text
Inspect the current lease, retry, persistence and mutation paths before editing.
Design the smallest backward-compatible stale-worker fence.

Requirements:
1. Name the exact resource.
2. Use a monotonically increasing token chosen by the coordinator.
3. Return the token on claim.
4. Present it on every standard state-changing worker call.
5. Compare it atomically with current persisted state.
6. Reject a stale token even when worker identity is unchanged.
7. Preserve idempotency, isolation, policy, approval and budget rules.
8. Add stale-token, wrong-owner and inactive-state negative controls.
9. Keep a rollback anchor and report tests actually run.
10. Do not activate production or external side effects.
```

## Practice reps

### Rep 1 — Race map, 5 minutes

Map `claim → pause → expire → recover → reassign → old worker returns` for one
workflow. Name the exact stale mutation.

- **PASS:** Resource and mutation are explicit.
- **FAIL:** The answer only says the agent may be wrong.
- **UNVERIFIED:** The real retry path was not inspected.

### Rep 2 — Same-identity fixture, 10 minutes

Create two claims for one resource using the same worker name. Give them tokens
11 and 12. Attempt a checkpoint with 11 after 12 is current.

- **PASS:** Token 11 fails before mutation; token 12 succeeds.
- **FAIL:** The system accepts both because the identity matches.
- **UNVERIFIED:** The test runs only against a mock unrelated to the real boundary.

### Rep 3 — Governed workflow capstone, 15 minutes

Combine:

- An idempotency key for duplicate logical commands
- A fencing token for execution generation
- An expected state version for optimistic concurrency
- A separate approval reference for a protected action

Simulate one duplicate, one stale generation, one state conflict and one missing
approval.

- **PASS:** Each failure has a different explicit outcome and no forbidden
  mutation occurs.
- **FAIL:** One generic retry handles every case.
- **UNVERIFIED:** The resulting state cannot be read back.

## Retention check

1. Why does idempotency not replace fencing?
2. Why does a matching worker identity not prove freshness?
3. What authority does a current fence token still not grant?

**Expected answer:** Idempotency deduplicates one logical command; fencing rejects
an obsolete execution. Stable identities can span generations. Freshness does
not grant policy, approval, spending, publication or data-access authority.

## Tool/Plugin Opportunity

**GitHub connection** can inspect current retry and mutation paths, hold the
implementation on a focused branch, run checks and retain review evidence.

- **Setup:** A repository connection and write permission are required.
- **Unlocks:** Versioned code, tests, review and rollback evidence.
- **Concrete use:** Add a stale-generation negative control beside an existing
  durable worker.
- **Limit:** Repository checks do not prove live production behavior or grant
  release authority.

No new paid service is required.

## Daily challenge

In 30 minutes, produce one resource-scoped lease with:

- A monotonic token source
- A current-token fixture
- A same-identity stale-token fixture
- A wrong-owner fixture
- An inactive-state fixture
- An idempotency key
- A separate approval or policy check
- PASS, FAIL or UNVERIFIED for every result

Finish only when the stale command is rejected at the resource boundary before
mutation. Practice remains **PENDING** until evidence is retained.
