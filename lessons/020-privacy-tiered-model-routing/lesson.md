# 2026-10-31 | AI Power Skill #20 | Privacy-Tiered Model Routing

**Category:** Model routing, privacy, local artificial intelligence, and verification  
**Practice status:** PENDING until the learner retains objective evidence  
**Core principle:** Classify data before selecting a model. Route each request to no model, a local model, or an approved cloud model according to sensitivity and task requirements.

## What the capability is

Privacy-tiered model routing is a deterministic admission step that runs before inference. It minimizes the payload, assigns a sensitivity tier, and chooses an eligible execution route.

| Tier | Example | Route |
|---|---|---|
| T0: Public | Published marketing copy | Approved local or cloud model |
| T1: Internal | Nonpublic process notes without personal data | Approved provider or local model |
| T2: Sensitive | Customer details, personal information, exact addresses | Local-only or specifically approved protected provider |
| T3: Restricted | Credentials, payment data, private keys | No model |

A routing decision should contain categories rather than matched values:

```json
{
  "policy_version": "2026-10-31",
  "data_tier": "T2_sensitive",
  "route": "local_only",
  "reasons": ["personal_information"],
  "decision": "ALLOW_LOCAL"
}
```

The sequence is:

1. Validate request size and shape.
2. Remove fields the task does not need.
3. Classify sensitivity with deterministic rules.
4. Select no-model, local-only, or approved-cloud.
5. Verify the route's actual endpoint and capabilities.
6. Run inference with a bounded output schema and tool policy.
7. Validate the output independently.
8. Record a privacy-safe receipt.

## Why it matters

A system prompt that says “protect sensitive data” runs after the data has already reached the model. Pre-egress routing makes the decision before transmission.

The pattern also avoids an unhelpful all-or-nothing choice between local and cloud. A workflow can use deterministic code for restricted fields, a local model for narrow extraction, and an approved cloud model for a sanitized reasoning step.

Useful metrics include:

- Requests blocked before egress
- Fields removed before inference
- Local versus cloud task success rate
- Cost per verified outcome by route
- Classifier false-positive and false-negative findings
- Policy-version drift

## What makes it non-obvious

### A product name does not prove the route

Some tools support both local and cloud models. Verify the endpoint, model identifier, network behavior, and cloud setting. “Using a local-model tool” is not evidence that the request remained local.

### Compatibility is usually partial

An OpenAI-compatible endpoint may implement only a subset of fields, tools, state, vision, or reasoning behavior. Probe the specific features the workflow needs.

### Structured output is still untrusted

A schema reduces shape errors. The application must still parse the response, check business rules, verify facts, and control actions independently.

### Classification is imperfect

Pattern rules can catch obvious contact information, payment numbers, addresses, and token-like strings. They may miss sensitive meaning and block benign text. Combine deterministic rules with narrow input fields, user guidance, sampled review, and fail-closed behavior.

### Local does not mean automatically safe

A local server can be exposed to a network, retain logs, use an untrusted model, or run on a compromised machine. Restricted data may belong in deterministic handling rather than any language model.

### Denial must happen before side effects

A blocked request should not consume quota, populate a cache, create a provider log, or invoke a tool. Test those counters explicitly.

## Typical versus advanced use

| Typical | Advanced |
|---|---|
| Pick one model globally | Select from policy-eligible routes per request |
| Put privacy rules in a prompt | Minimize and classify before inference |
| Treat all local-tool traffic as local | Verify endpoint, model, and cloud-disabled state |
| Log rejected prompts for debugging | Log reason categories without matched values |
| Test only allowed requests | Prove denied requests make zero downstream calls |
| Route by price alone | Optimize cost within privacy eligibility |

## Immediate applications

| Workflow | Useful boundary |
|---|---|
| Consulting discovery | Keep public examples cloud-eligible; protect client-sensitive notes |
| Sales operations | Remove unnecessary contact and commercial fields before reasoning |
| Marketplace automation | Separate public listing copy from identity and settlement records |
| Decision support | Use local summarization without confusing it with action approval |
| Travel assistant | Route ordinary trip context to the approved provider and sensitive free text to manual-only |

## Practical routing contract

```json
{
  "request_type": "narrow task",
  "policy_version": "version",
  "input_fields": ["required fields only"],
  "data_tier": "T0_public | T1_internal | T2_sensitive | T3_restricted",
  "forbidden_data": ["credentials", "payment_data"],
  "allowed_routes": ["no_model", "local_only", "approved_cloud"],
  "selected_route": "route",
  "required_capabilities": ["structured_output"],
  "negative_control": "known-sensitive mutation",
  "expected_blocked_side_effects": 0,
  "output_validator": "schema and independent checks"
}
```

## Practice reps

### Rep 1: Classify before choosing

Assign a tier and route:

1. Published product description: T0, approved local or cloud.
2. Internal workflow notes without personal details: T1, approved provider or local after minimization.
3. Sales note with a person's phone number: T2, local-only or a specifically approved protected route.
4. Pasted private key: T3, no model.

PASS means routing becomes more restrictive as sensitivity rises. FAIL means every input goes to one provider. UNVERIFIED means the route label exists but the actual endpoint cannot be observed.

### Rep 2: Build a route table

Use this prompt in an existing implementation workspace:

```text
Inspect one current model-assisted workflow. Do not modify production.

Return:
1. The exact fields that can enter inference.
2. Fields the task does not need.
3. T0 through T3 classification rules.
4. Allowed route for each tier.
5. Exact endpoint and capability requirements.
6. What must happen before quota, cache, log, provider, or tool access.
7. One ordinary allowed fixture.
8. One known-sensitive blocked fixture.
9. PASS, FAIL, and UNVERIFIED evidence.

Do not reveal sensitive values. Record reason categories only. Do not add a provider, subscription, database, or scheduler.
```

### Rep 3: Add the decisive negative control

Keep an allowed fixture unchanged except for one inserted sensitive field. Prove the route changes to local-only or no-model and that quota, cache, provider, and tool counters remain zero.

Also prove the ordinary fixture still reaches the approved route with only the documented fields.

## Evidence table

| Claim | PASS | FAIL | UNVERIFIED |
|---|---|---|---|
| Classification | Versioned rule runs before inference | Rule runs after egress | Order unavailable |
| Local-only | Local endpoint, model, and cloud-disabled state observed | External route used | Product name only |
| Blocked request | Zero downstream calls | Any downstream call | Counters unavailable |
| Allowed request | Only minimal eligible fields leave | Extra fields leave | Payload cannot be inspected |
| Output | Schema and independent checks pass | Invalid output accepted | Only model confidence exists |

## Retention check

How does privacy-tier routing differ from confidence-gated model cascading?

Confidence gating escalates an uncertain result. Privacy-tier routing decides which models may see the request. Privacy eligibility comes first.

Does a privacy-safe route authorize an external action?

No. Identity, authority, policy, payload, and approval evidence remain separate requirements.

What is the best counterfactual?

Insert one sensitive field while keeping the task constant. The route must become more restrictive and forbidden side effects must remain zero.

## Tool/Plugin Opportunity

| Option | Unlocks | Setup | Use case |
|---|---|---|---|
| Ollama | Local models and OpenAI-compatible local endpoints | Install, download a model, size hardware, harden the endpoint, and verify cloud is disabled when required | Local extraction before a sanitized downstream task |
| GitHub | Versioned policy, tests, review, and receipts | Repository access required | Keep routing rules beside the owning workflow |
| Existing coding assistant | Fixture design and implementation help | Do not paste restricted data | Generate synthetic tests and review the route contract |

Ollama is optional. Install it only when a verified task benefits from local inference.

## Daily challenge

Choose one real workflow and produce:

- One versioned T0-T3 route table
- One minimized payload definition
- One verified endpoint decision
- One allowed fixture
- One blocked fixture expected to produce zero downstream calls
- PASS, FAIL, or UNVERIFIED evidence for each claim

Practice remains PENDING until the evidence is retained.
