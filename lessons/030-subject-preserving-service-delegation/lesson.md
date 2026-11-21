2026-11-20 | AI Power Skill #30 | Subject-Preserving Service Delegation

**Category:** agents and multi-agent systems; external integrations; structured tool calling; authorization and guardrails

## Core principle

When one service acts for a person through another service, keep two identities:

- **Actor:** the service or agent authenticating the transport request.
- **Subject:** the person, tenant, or workspace the actor is representing.

A service credential proves who is calling. It does not automatically prove whom that caller may represent.

## What the capability is

Subject-preserving service delegation is a contract for carrying authenticated user context across service boundaries without pretending the user made the transport request.

```json
{
  "actor": {"type": "service", "id": "planning-agent"},
  "subject": {
    "tenant_id": "fictional-tenant",
    "workspace_id": "fictional-workspace",
    "principal_id": "fictional-owner"
  },
  "authority": ["catalog:read", "identity:project"],
  "resource": "tool-catalog",
  "purpose": "find a tool for an approved objective",
  "expires_at": "short-lived timestamp",
  "correlation_id": "trace-example"
}
```

The downstream service should allow the request only when the actor may perform the operation **and** may represent the stated subject for that resource and purpose.

OAuth 2.0 Token Exchange, Request for Comments (RFC) 8693, provides a formal model for subject and actor tokens and an `act` claim. The mental model is useful even when a system begins with an application-level envelope instead of exchanged tokens.

## Why it matters

A user often authenticates to an application, while the application calls search, billing, retrieval, or automation services with its own credential. If the downstream service sees only the application, the system risks:

1. mixing tenant context;
2. granting a service overly broad authority;
3. producing incomplete audit logs;
4. applying the wrong entitlements, limits, or approvals.

This pattern makes multi-user AI systems easier to reason about and test.

## What makes it non-obvious

Two tempting shortcuts are unsafe:

- Forwarding the user bearer token to every service spreads credentials and trust.
- Using only the service token erases the user subject.

The better pattern authenticates the service as actor, carries the subject as validated context, and requires a separate projection permission when actor and subject differ. A subject field supplied by a client is not proof; the upstream service must derive it from an authenticated principal.

## How advanced users apply it differently

| Typical implementation | Advanced implementation |
|---|---|
| One token represents every identity | Actor and subject remain distinct |
| Copies identity fields from client input | Derives subject from authenticated server-side context |
| Any connected service can project a user | Projection requires an explicit, narrow permission |
| Accepts partial identity | Fails closed on incomplete or mismatched identity |
| Logs only the service caller | Logs actor, subject, resource, purpose, and trace ID |
| Treats a successful request as end-to-end proof | Separates contract, authorization, and real-user workflow evidence |

## Where to use it immediately

- **Sales automation:** actor = enrichment agent; subject = authorized seller and account scope.
- **Research assistant:** actor = research service; subject = requesting workspace and user.
- **Marketplace discovery:** actor = planning service; subject = authenticated owner and tenant.
- **Email or calendar agent:** actor = automation; subject = mailbox/calendar owner and approved purpose.
- **Multi-tenant software:** actor = application backend; subject = tenant, workspace, and end user.

## Implementation pattern

1. Authenticate the user at the owner-facing boundary.
2. Build an immutable subject from the authenticated principal.
3. Authenticate the service actor downstream.
4. Require both operation authority and projection authority.
5. Validate tenant/workspace relationships and reject partial subjects.
6. Record actor, subject, resource, purpose, and correlation ID.
7. Test missing scope, tenant mismatch, partial subject, and unauthorized operation.
8. Run a signed-in end-to-end probe before claiming the user workflow works.

## Tool/Plugin Opportunity

**Option:** GitHub for versioned contracts and negative-control tests; optionally, an identity provider supporting OAuth 2.0 Token Exchange.

**Unlocks:** GitHub makes the envelope and denial cases reviewable. Token exchange can later issue short-lived, audience-bound delegated tokens.

**Setup:** GitHub requires repository access. Token exchange requires identity-provider configuration, keys, audience rules, and deployment work.

**Concrete use case:** a planning service searches a catalog for an authenticated owner. The catalog sees the planning service as actor, the owner as subject, and rejects projection without the required permission.

## Practice reps

Practice is **PENDING** until evidence is recorded.

### Rep 1 — Label the identities

For “an AI drafts a customer follow-up,” write the actor, subject, resource, purpose, operation, and expiration.

### Rep 2 — Negative-control matrix

Predict allow or deny for:

1. valid actor + valid subject + projection authority;
2. valid actor + valid subject − projection authority;
3. subject from another tenant;
4. partial subject;
5. unauthorized operation.

Expect one allow and four denials.

### Rep 3 — Service-boundary capstone

Trace one authenticated user request through an application and a downstream service. Mark where user authentication, service authentication, subject derivation, projection authorization, and evidence occur. Produce a contract fixture, two negative controls, an exact-head test receipt, and one signed-in end-to-end probe.

## Retention check

1. Why is operation authority insufficient to represent an arbitrary tenant?
2. Which trace invariant fails when a service actor is present but the human subject disappears?
3. How can a consumer-owned contract require identity fields without freezing every provider field?

Answers: delegation is a separate authority; actor/subject continuity failed; validate the consumer’s minimum required fields while permitting compatible additive provider data.

## Today’s challenge

Write a six-field delegation card for one automation: actor, subject, authority, resource, purpose, and expiry. Add: “This request must fail when ___.” Use it to review one real service boundary today.

## Clean-room implementation exercise

Add an optional subject envelope to a fictional catalog request. Derive it server-side, require a projection permission downstream, and add tests proving that incomplete subjects and actors without projection authority are rejected. Do not enable production mutation until the learner explicitly authorizes it.

## Learning ledger

| Date | Skill | Practice | Evidence | Next step |
|---|---|---|---|---|
| 2026-11-20 | Subject-Preserving Service Delegation | PENDING | None supplied | Complete the delegation card and negative-control matrix |

**Practice status:** PENDING. Publishing this lesson does not prove that any learner completed the exercises.
