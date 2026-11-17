# 2026-11-16 | AI Power Skill #28 | Consumer-Driven Contract Testing for Agent Tools

**Category:** Connectors and external integrations; Model Context Protocol; coding agents; evaluation and guardrails  
**Practice status:** PENDING

## Core principle

Make each consumer define the smallest executable request and response it
actually depends on. Require both the consumer and provider to verify that same
interaction before either side changes.

```text
consumer behavior → executable interaction → provider verification → release gate
```

## What the capability is

Consumer-driven contract testing records an integration as executable examples
owned by the consuming system.

For one interaction, capture:

- consumer and provider roles;
- business intent;
- method and route or tool name;
- exact request the consumer emits;
- minimum response fields it reads;
- allowed additive fields;
- important error or authorization outcomes; and
- contract version and retirement rule.

Verify the example twice:

1. The real consumer emits the request and can use the response.
2. The provider accepts the request and guarantees the required response.

This is narrower than an OpenAPI document. A provider schema describes many
possible states. A consumer contract protects one active dependency.

## Why it matters

Agent systems depend on independently changing boundaries: tool servers,
catalogs, Customer Relationship Management connectors, email providers,
research services and deployment adapters.

Provider tests can remain green while a consumer breaks because a required
field disappears, an enum changes, a denial becomes an empty success or an
identity field changes meaning. End-to-end tests may catch this only after both
systems are deployed together.

Consumer-driven contracts create fast boundary evidence before merge. They are
especially useful when coding agents can update clients and providers in
separate changes.

## What makes it non-obvious

### The consumer owns the requirement

The provider knows what it can return. Only the consumer knows what it uses.

### Smaller is better

Do not freeze the entire provider response. Require used fields and permit
unrelated additive fields.

### Examples must execute

A JSON snippet in documentation becomes stale. Both test environments must
load and validate the same artifact.

### Denials belong in the contract set

Test forbidden, missing-resource, rate-limit and unavailable states so they
cannot be mistaken for successful empty results.

### Compatibility is not functional truth

A matching shape does not prove ranking quality, payment correctness, factual
accuracy or a business outcome. Keep those tests separate.

### Retirement needs evidence

Remove an old field only after every supported consumer has stopped using it.

## Advanced versus typical use

| Typical approach | Advanced approach |
|---|---|
| Provider publishes one large schema | Consumer publishes minimal used interactions |
| Examples live in documentation | The same examples run in both test suites |
| Test only success | Test success, denial and unavailable states |
| Freeze complete responses | Require used fields and allow additions |
| Depend on deployed end-to-end tests | Verify both sides before merge |
| Treat green contracts as product success | Separate compatibility from outcomes |
| Record live traffic | Use synthetic data and no credentials |

## Contract example

```json
{
  "contract_version": "1.0",
  "consumer": "workflow-orchestrator",
  "provider": "capability-catalog",
  "interaction": "find eligible capabilities",
  "request": {
    "intent": "score inbound leads",
    "constraints": {"min_trust_tier": "T2"}
  },
  "response": {
    "candidates": [
      {
        "capability_id": "example.lead-scoring",
        "version": "1.0.0",
        "trust": {"tier": "T2"}
      }
    ]
  }
}
```

## Practical workflow

1. Choose one boundary where components change independently.
2. Inspect the real consumer request builder and response parser.
3. Normalize volatile values and replace private data with synthetic values.
4. Keep only fields that affect consumer behavior.
5. Test the actual consumer against the example.
6. Validate or replay the same example in the provider test environment.
7. Delete or corrupt one required field; the checks must fail.
8. Keep tenant, authorization, business logic and outcome tests separate.
9. Gate compatibility before merge, not automatically before deployment.
10. Version the interaction and retire it only with consumer evidence.

## Ready-to-copy prompt

```text
Inspect the real consumer adapter, provider route and models, current tests and
authorization boundary.

Create one minimal consumer-driven contract for an existing interaction.

Requirements:
1. Derive expectations from actual consumer behavior.
2. Use a sanitized synthetic request and response.
3. Verify the consumer emits the request and consumes the response.
4. Verify the provider accepts the request and guarantees required fields.
5. Allow additive provider fields.
6. Add a deliberate breaking negative control.
7. Keep authorization, business logic and outcomes as separate tests.
8. Do not call live services or add paid infrastructure.
9. Report exact files, tests and limitations.

Return VERIFIED, FAILED or UNVERIFIED. A fixture alone is not completion.
```

## Tool/Plugin Opportunity

**GitHub Actions plus Pact (optional)**

- **Unlocks:** Automatic consumer/provider compatibility checks. Pact can
  generate, exchange and replay contracts at larger scale.
- **Setup:** GitHub Actions requires a repository workflow. Pact requires a
  language library; a broker is optional.
- **Concrete use:** Block a catalog change that removes an identity field an
  agent client consumes.
- **Cost:** A local shared-contract pattern can use existing tests and no paid
  service. Add hosted tooling only when multiple repositories justify it.

## Practice reps

### Rep 1 — Minimum response

Inspect one connector response and list only the fields your workflow reads.

- **PASS:** The contract is smaller than the provider schema.
- **FAIL:** You copied the full documentation.
- **UNVERIFIED:** You did not inspect the actual consumer.

### Rep 2 — Denial states

Define a customer-record interaction that can read and draft but cannot send.
Include missing record, suppressed contact and forbidden send states.

- **PASS:** A forbidden send cannot look like an empty success.
- **FAIL:** Only the happy path is executable.
- **UNVERIFIED:** A prompt is the only enforcement.

### Rep 3 — Two-sided capstone

Create one catalog search example. Verify a real client request builder and
parser. Verify provider request/response models against the same artifact.
Delete `capability_id` as a negative control.

- **PASS:** Both sides accept the valid interaction and reject the broken one.
- **FAIL:** The fixture can break without a failing test.
- **UNVERIFIED:** Only a standalone JSON validator runs.

## Retention check

1. Why does a schema not prove the consumer calls the provider correctly?
2. What deliberate mutation proves a contract test is sensitive?
3. Why does a valid request shape not authorize an action?

**Expected answer:** Schema, compatibility and authorization answer different
questions. A useful contract exercises the real client, rejects a controlled
breaking change and preserves independent authorization checks.

## Daily challenge

Choose one connector and write one executable interaction with:

- consumer and provider;
- business intent;
- exact request;
- minimum response;
- one allowed additive field;
- one denial or unavailable state; and
- one breaking mutation.

Run the real consumer against it. Keep practice **PENDING** until the provider
independently verifies the same interaction.
