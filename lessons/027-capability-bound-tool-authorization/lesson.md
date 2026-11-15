# 2026-11-14 | AI Power Skill #27 | Capability-Bound Tool Authorization

**Category:** Model Context Protocol, tool calling, agents and security  
**Practice status:** PENDING

## Core principle

A model may recommend a tool call. It must not grant itself permission to make
that call.

Before a protected action, bind authorization to the exact audience,
capability, operation, resource scope and expiration. Enforce that binding at
the tool boundary.

```text
model proposes → policy grants → broker validates → tool executes
```

## What the capability is

Capability-bound authorization separates three questions:

1. Which tool can perform the task?
2. Is the current subject allowed to perform it?
3. Does the presented grant match this exact dispatch?

A useful authorization envelope contains:

- Authorization identifier and trusted issuer
- Audience or receiving tool
- Capability
- Allowed operations
- Minimum scopes
- Tenant or workspace where applicable
- Expiration
- Approval or policy-decision reference

The envelope is authorization metadata, not a raw provider password or access
token. A production system should make it tamper-evident and issue it outside
model-editable tool arguments.

## Why it matters

Tool-using assistants can cross important boundaries: repositories, customer
records, communications, deployments and payments. Without binding, a valid
grant may be misused:

- at a different tool;
- for a wider operation;
- in another tenant;
- after it expires; or
- by an intermediary forwarding it to another service.

Audience and scope solve different problems. Audience says where authority may
be redeemed. Scope says what may happen there. A secure call generally needs
both.

## What makes it non-obvious

### Selection is not authority

A router finding a capable tool does not prove that the current user or agent
may invoke it.

### Prompt instructions are not enforcement

“Only read files” is useful guidance, but it does not prevent a compromised or
mistaken call. The receiver must validate a machine-readable grant.

### The model cannot approve itself

The model can request an operation. A trusted policy boundary must issue the
grant. Model-generated `authorized: true` metadata is only another untrusted
claim.

### Inbound tokens should not be passed downstream

An intermediary should obtain separate downstream authority intended for the
upstream service. Reusing the caller's token can create a confused-deputy
failure.

### Declarative validation is not cryptographic proof

Checking fields catches accidental and many malicious mismatches. It does not
authenticate the issuer unless the envelope is signed, introspected or obtained
through a trusted channel.

## Advanced versus typical use

| Typical approach | Advanced approach |
|---|---|
| The model selects and invokes | Selection, policy and enforcement are separate |
| Reuse one broad token | Issue short-lived, audience-bound authority |
| Put permission in a prompt | Validate at the tool boundary |
| Check identity only | Check subject, audience, operation and resource scope |
| Treat scope as destination | Keep scope and audience separate |
| Forward the caller token | Obtain a distinct downstream credential |
| Approve once indefinitely | Expire and recheck the grant |
| Log misuse afterward | Reject before any external action |

## Authorization contract

```json
{
  "authorization_id": "grant-123",
  "issuer": "trusted-policy-boundary",
  "audience": "capability:document.inspect",
  "capability_id": "document.inspect",
  "operations": ["inspect"],
  "scopes": ["tool:invoke", "document:read"],
  "workspace_id": "workspace-a",
  "expires_at": "2026-11-15T02:00:00Z",
  "approval_reference": "approval-987"
}
```

## Practical workflow

1. Inventory each tool's audience, operations and data domain.
2. Let the model request authority; never let it grant authority.
3. Minimize the grant to one audience and the smallest operation set.
4. Store the grant outside ordinary prompt context.
5. Validate audience, capability, operation, scope, resource and expiration.
6. Reject mismatch before creating a runtime or external action.
7. Obtain separate downstream credentials for other services.
8. Retain a non-secret decision receipt; never log raw tokens.
9. Expire grants quickly and recheck high-consequence actions.

Useful denial results include:

- `AUTHORIZATION_REQUIRED`
- `WRONG_AUDIENCE`
- `OPERATION_NOT_GRANTED`
- `SCOPE_INSUFFICIENT`
- `RESOURCE_MISMATCH`
- `AUTHORIZATION_EXPIRED`
- `ISSUER_UNVERIFIED`

## Ready-to-copy prompt

```text
Inspect the planner, router, policy engine, approval boundary, tool broker,
tenant/resource model and runtime dispatch.

Design the smallest capability-bound authorization increment.

Requirements:
1. Separate tool selection from authorization.
2. Bind each grant to issuer, audience, capability, operation, minimum scopes,
   resource scope, expiration and approval evidence.
3. Keep the grant outside model-editable arguments and ordinary prompt context.
4. Validate it immediately before dispatch.
5. Fail closed on missing, expired, widened or wrong-audience grants.
6. Never pass an inbound token to a different downstream service.
7. Preserve independent approval, budget, privacy and recovery controls.
8. Prove denied calls create no runtime or external action.
9. Do not claim issuer authentication unless signing or trusted issuance exists.

Return VERIFIED, FAILED or UNVERIFIED with exact evidence.
```

## Tool/Plugin Opportunity

**Model Context Protocol implementation plus an OAuth-compatible authorization
server**

- **Unlocks:** Resource indicators, audience-bound tokens and narrow scopes.
- **Setup:** Usually requires an authorization-server connection and protected
  resource metadata.
- **Concrete use:** Give an assistant temporary read access to one workspace
  without granting write access or authority at another server.
- **Limit:** The integration must still validate audience, scope and resource on
  every protected request.

Start with existing platform authorization where possible. Do not add paid
infrastructure before the workflow needs live credentials.

## Practice reps

### Rep 1 — Audience and scope

For one tool, write one audience, one read scope, one write scope and one
operation that must be rejected.

- **PASS:** Audience and scope are separate.
- **FAIL:** A broad label such as `admin` is the complete contract.
- **UNVERIFIED:** The provider's behavior was not inspected.

### Rep 2 — Draft but do not send

Design a grant that can read one customer record and draft a response, but
cannot send it or read another account.

- **PASS:** Sending and cross-account reuse fail before external action.
- **FAIL:** Prompt instructions are the only restriction.
- **UNVERIFIED:** No enforcement-point test exists.

### Rep 3 — Protected tool capstone

Test an exact grant, missing grant, wrong audience, wider operation, expiration,
cross-workspace reuse and an obsolete worker.

- **PASS:** Only the exact current grant reaches runtime once.
- **FAIL:** Any mismatch creates an external action.
- **UNVERIFIED:** Only an isolated parser was tested.

## Retention check

1. Why is tool discovery not authorization?
2. Why are audience and scope separate?
3. Why does valid authorization not replace approval, worker freshness or
   compensation?

**Expected answer:** These controls answer different questions. Discovery finds
capability, authorization limits authority, approval confirms a protected
decision, fencing rejects stale workers and compensation handles partial work.

## Daily challenge

Choose one real connector and create a five-minute authorization contract with:

- one audience;
- one capability;
- one allowed operation;
- one denied operation;
- minimum scopes;
- workspace binding;
- expiration;
- approval reference; and
- negative tests for wrong audience and operation widening.

Do not use a live credential or execute the real side effect. Record practice as
PENDING until evidence exists.
