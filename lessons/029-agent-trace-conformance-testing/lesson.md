# 2026-11-18 | AI Power Skill #29 | Agent Trace Conformance Testing

**Category:** Multi-agent systems; coding agents; evaluation, guardrails and observability  
**Practice status:** PENDING

## Core principle

An agent diagram or successful answer does not prove the intended orchestration ran. Convert the required topology into executable rules, capture a durable trace at real dispatch and outcome boundaries, and fail when the trace cannot prove the required routes, dependencies, authority gates, and terminal state.

```text
intended topology → emitted trace → conformance gate → eligible result
```

## What the capability is

Agent trace conformance testing compares one observed execution with a machine-readable orchestration contract.

A useful trace records:

- one trace identifier;
- ordered events or spans;
- step, capability, and assigned role at dispatch;
- parent or dependency relationships;
- accepted outcome status;
- approvals or policy decisions where relevant;
- retry or repair identity; and
- one terminal state after all required evidence.

The checker then asks whether each required step ran exactly once, preserved its planned identity, waited for its dependencies, stayed inside its authority, and completed before terminal success.

OpenTelemetry provides shared trace and Generative Artificial Intelligence terminology. W3C Trace Context defines interoperable propagation of trace identity across services. Your application still needs its own topology rules.

References:

- https://opentelemetry.io/docs/specs/semconv/gen-ai/
- https://opentelemetry.io/docs/specs/semconv/how-to-write-conventions/
- https://www.w3.org/TR/trace-context-1/

## Why it matters

Multi-agent workflows can appear successful while silently bypassing their design:

- a reviewer is the builder under another label;
- implementation starts before research;
- a fallback model is used without disclosure;
- an approval or verifier is skipped;
- a retry resumes with stale context; or
- a single flat path produces a plausible answer while the expected agent graph never ran.

Trace conformance makes orchestration claims testable. It improves debugging, auditability, connector safety, client trust, and provider-neutral model routing.

## What makes it non-obvious

### Logs are not conformance

Logs show activity. A conformance gate determines whether the activity satisfied the intended graph.

### Planned routing is not executed routing

Record identity where the orchestrator actually dispatches work. When available, separate requested model policy from the resolved provider and model.

### A model cannot certify its own lineage

A statement such as “independent review completed” is not review evidence. Require a separately originated verifier operation tied to the artifact reviewed.

### Workflows are graphs

One synthesis step may depend on several researchers. Use links or explicit dependency identifiers when a simple parent-child tree cannot express the relationship.

### Sampling can remove proof

Verbose telemetry may be sampled. Preserve a compact conformance receipt for gated runs.

### Telemetry can leak content

Prefer identifiers, hashes, status, policy decisions, and counts. Do not record prompts, credentials, personal data, or customer content unless a reviewed requirement justifies it.

### Conformance is not correctness

The expected agents can execute in the expected order and still produce a poor result. Keep output-quality, security, and business-outcome checks separate.

## Advanced versus typical use

| Typical approach | Advanced approach |
|---|---|
| Show an orchestration diagram | Compile it into executable invariants |
| Trust configured role names | Compare planned and observed identity at dispatch |
| Check that events exist | Check count, order, dependencies and terminal rules |
| Let the model report review | Require an independently originated verifier event |
| Store every prompt | Store minimal identities, hashes and decisions |
| Test only valid traces | Mutate, flatten, duplicate and substitute traces |
| Treat conformance as success | Keep result quality and release approval separate |

## Example contract

```json
{
  "trace_contract_version": "1.0",
  "required_steps": [
    {"step_key": "inspect", "agent": "scout", "depends_on": []},
    {"step_key": "implement", "agent": "builder", "depends_on": ["inspect"]},
    {"step_key": "verify", "agent": "reviewer", "depends_on": ["implement"]}
  ],
  "minimum_distinct_agents": 3,
  "terminal_rule": "success_after_all_required_outcomes"
}
```

## Practical workflow

1. Pick one orchestration claim worth proving.
2. Define required steps, identities, dependencies, approvals, retries, and terminal state.
3. Emit events at real dispatch and accepted-outcome boundaries.
4. Preserve trace identity across services and tools.
5. Record requested and resolved routing separately when observable.
6. Reject missing, duplicate, foreign, reordered, or substituted evidence.
7. Add negative controls for agent substitution and dependency flattening.
8. Preserve a compact receipt without private content.
9. Keep deployment and external-action approval separate.

## Ready-to-copy prompt

```text
Inspect the real orchestration runtime, persisted events, plan model, agent and
capability registry, approval boundary, tests, and repository rules.

Implement one small trace-conformance gate.

Requirements:
1. Define the intended graph and terminal rule.
2. Emit evidence at real dispatch and accepted outcome boundaries.
3. Bind events to trace, step, capability, assigned agent, and dependencies.
4. Avoid prompts, credentials, personal data, and customer content.
5. Fail closed on missing, duplicate, foreign, reordered, or substituted data.
6. Add negative controls for route substitution and dependency flattening.
7. Keep conformance separate from output quality and deployment approval.
8. Report exact files, tests, limitations, and rollback.
```

## Tool/Plugin Opportunity

**OpenTelemetry plus a repository continuous-integration workflow**

- **Unlocks:** Provider-neutral traces, cross-service trace propagation, and automated topology checks.
- **Setup:** Start with existing persisted events and no paid service. Add an exporter or trace backend only when distributed live traces and retention justify it.
- **Concrete use:** Prove that a scout completed before a builder and that an independent reviewer finished before success.
- **Limitations:** Standards do not define application-specific topology; sampling and inaccessible provider internals can limit evidence.

## Practice reps

### Rep 1 — Write invariants

Turn one three-role workflow into five rules: required roles, dispatch order, dependency, authority boundary, and terminal state.

- **PASS:** Each rule can be evaluated from events.
- **FAIL:** Rules depend on interpreting prose.
- **UNVERIFIED:** The workflow emits no real events.

### Rep 2 — Break the trace

Create a valid synthetic trace, then remove the reviewer outcome, substitute the builder for the scout, and dispatch implementation before inspection finishes.

- **PASS:** Every mutation produces a distinct failure.
- **FAIL:** Only the final answer is checked.
- **UNVERIFIED:** The checker is not automated.

### Rep 3 — Real runtime capstone

Instrument one workflow to emit step, capability, assigned agent, dependencies, status, and trace ID. Require at least two distinct agents and validate the three mutations from Rep 2.

- **PASS:** The real runtime emits the evidence and rejects flattened or substituted traces.
- **FAIL:** Only a hand-written fixture passes.
- **UNVERIFIED:** Hosted behavior was not exercised.

## Retention check

1. How does an intended capability graph differ from an execution trace?
2. Which mutation tests dependency enforcement?
3. Why is a screenshot of several agent names weak evidence?

**Expected answer:** The graph states what should run; the trace records what ran. Reordering a dependent dispatch tests dependency enforcement. A screenshot lacks durable identity, sequence, artifact lineage, and reproducible verification.

## Daily challenge

Write a seven-line trace contract for one current workflow: trace ID, required steps, assigned roles, dependencies, authority rule, terminal rule, and one mutation that must fail. Run it against a real or locally simulated execution. Keep practice **PENDING** until events come from the actual workflow boundary.

## Learning ledger

- Lesson: #29 Agent Trace Conformance Testing
- Date: 2026-11-18
- Practice: PENDING
- Project mutation: DISABLED by default; enable only with the learner's explicit authorization
- Evidence required: real runtime trace, passing valid case, failing negative controls, and a durable receipt
