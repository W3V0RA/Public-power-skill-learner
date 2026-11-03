# 2026-11-02 | AI Power Skill #21 | Delivered-Artifact Probes for Coding Agents

**Category:** Coding agents; evaluation, verification, and guardrails  
**Difficulty:** Advanced  
**Practice status:** PENDING until the learner retains objective evidence  
**Core principle:** Approve the artifact produced by the build or generator, not merely the source an agent edited.

## What the capability is

A delivered-artifact probe is a deterministic check placed after a compiler, builder, generator, renderer, or migration planner and before promotion.

```text
source -> transformation -> delivered artifact -> probe -> release gate
```

Examples include testing rendered HTML instead of only a component, generated SQL instead of only a schema model, an OpenAPI document instead of only route source, or a compiled policy bundle instead of only a prompt.

An effective probe records:

- the exact source commit and producer command;
- the artifact type and locator;
- required and forbidden invariants;
- how ambiguity is handled;
- one known-bad negative control;
- which promotion step failure blocks.

## Why it matters

Source can be correct while delivery is wrong. Configuration, environment variables, code generation, caching, bundling, or framework upgrades can change semantics after source tests pass. A green build proves that a tool completed; it does not prove that the artifact preserves the intended business meaning.

Current Next.js documentation explains that pages can be prerendered at build time and that static generation emits HTML during `next build`. That output is the relevant artifact for a rendered promise. See [Next.js production guidance](https://nextjs.org/docs/app/guides/production-checklist) and [Static Site Generation](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation). npm documents script sequencing that can place a semantic probe after a build. See [npm scripts](https://docs.npmjs.com/cli/v11/using-npm/scripts/).

## What makes it non-obvious

1. **The transformation boundary is the target.** Test where meaning can change, not only where source is convenient.
2. **Build success is not semantic success.** A compiler can exit zero while emitting the wrong public copy, schema, route, or policy.
3. **Negative controls are essential.** Mutate one required invariant and prove the gate fails.
4. **Artifact discovery must fail closed.** Zero or multiple matches should stop the gate rather than select one arbitrarily.
5. **Artifact proof is not production proof.** Keep source, build, preview, production, served output, and business outcome as separate evidence states.
6. **Small probes are better.** Use the simplest parser that proves the invariant; avoid unnecessary services and test infrastructure.

## How advanced users apply it differently

| Typical | Advanced |
|---|---|
| Review the diff | Bind the diff to an exact generated artifact |
| Run tests only before build | Run semantic probes after transformation |
| Assert the good value exists | Reject conflicting values and ambiguity |
| Trust a green build | Require a domain-specific artifact contract |
| Test only good output | Inject a known-bad artifact and require failure |
| Treat preview as production | Record every release stage separately |

## Where to use it

| Workflow | Delivered artifact | Useful first invariant |
|---|---|---|
| Marketing site | Prerendered HTML | Offer, duration, destination, and disclaimer remain aligned |
| Multi-tenant agent | Compiled policy bundle | Tenant, authority, tool allowlist, and evaluator coverage survive compilation |
| Marketplace | Generated settlement schema | Identity, entitlement, fee, and approval fields are required |
| Decision support | Generated decision packet | Sources, time, uncertainty, and approval state remain attached |
| Sales operations | Customer-ready account brief | Correct organization, fresh sources, allowed fields, and receipts are present |

## Artifact contract template

```json
{
  "artifact_type": "rendered_html | migration_sql | policy_bundle | openapi | report",
  "producer": "exact build or generator command",
  "source_commit": "immutable identifier",
  "artifact_locator": "manifest, route, path, or semantic markers",
  "required_invariants": ["must be true"],
  "forbidden_invariants": ["must not be true"],
  "ambiguity_rule": "fail on zero or multiple matches",
  "negative_control": "known-bad mutation",
  "promotion_binding": "step blocked by failure",
  "completion_evidence": ["probe output", "artifact identity", "release receipt"]
}
```

## Ready-to-copy prompt

```text
Inspect the current repository, base branch, active changes, release policy, and latest verified build before editing.

Identify one important invariant currently tested only in source. Find the transformation boundary between that source and the artifact a user or downstream system receives.

Implement the smallest dependency-free artifact probe that:
1. runs after the existing build or generator;
2. identifies the exact artifact;
3. asserts required and forbidden invariants;
4. fails on zero or multiple matches;
5. includes one known-bad negative control;
6. blocks the existing promotion path on failure;
7. changes no runtime permissions or business thresholds;
8. records commit, paths, commands, results, rollback, and release state.

Return PASS, FAIL, or UNVERIFIED for each claim. Do not infer production or business outcome from a source test or preview.
```

## Practice reps

### Rep 1: Identify the boundary — 5 minutes

Fill in: source, transformation, delivered artifact, required invariant, forbidden invariant, and promotion step.

**PASS:** the artifact is what a user or machine consumes.  
**FAIL:** the artifact is merely another source file.  
**UNVERIFIED:** output cannot be tied to a producer and commit.

### Rep 2: Specify the detector — 10 minutes

Define one required assertion, one forbidden assertion, one ambiguity failure, one known-bad mutation, and the command that must exit nonzero.

**PASS:** the mutation fails.  
**FAIL:** good and bad artifacts both pass.  
**UNVERIFIED:** no executed evidence exists.

### Rep 3: Fictional booking-page capstone — 15 minutes

A fictional consultancy stores a 30-minute discovery-call duration in configuration and renders it on a homepage and contact page. Design a post-build probe that:

- discovers both generated pages by independent markers;
- extracts visible text rather than searching source;
- requires “About 30 minutes” on both;
- rejects any other numeric duration;
- fails on zero or multiple page matches;
- mutates one artifact to 20 minutes and proves rejection;
- runs before deployment.

Do not add a browser service if generated HTML is sufficient.

## Expected evidence

| Claim | PASS | FAIL | UNVERIFIED |
|---|---|---|---|
| Artifact identity | Tied to exact commit and producer | Wrong or unknown build | Identity unavailable |
| Invariant | Required value present; conflict absent | Missing or conflicting value | Artifact unavailable |
| Ambiguity | Zero/multiple matches fail | Arbitrary match accepted | Match count absent |
| Negative control | Known-bad mutation exits nonzero | Mutation passes | Not executed |
| Promotion | Failure blocks release | Release continues | Policy unobservable |
| Production | Deployed and served output read back | Wrong artifact served | Only preview evidence exists |

## Retention check

**Executable promise contracts:** A source contract makes a promise machine-checkable; an artifact probe verifies the transformed output. Use both.

**Visual regression:** Prefer deterministic artifact parsing for text, schema, metadata, and policy. Use visual checks when appearance or layout is the invariant.

**Metamorphic testing:** Keep the pipeline constant, mutate one business invariant, and require the result to flip from PASS to FAIL.

## Tool/Plugin Opportunity

| Option | Unlocks | Setup | Use case |
|---|---|---|---|
| GitHub | Versioned probes, reviews, remote receipts | Repository connection required | Bind tests to exact commits |
| Existing deployment provider | Preview and production state | Existing project connection required | Separate preview from production |
| Browser or HTTP client | Served-output verification | Public or authorized access required | Confirm the deployed page serves the contracted output |

No new paid tool is required.

## Daily challenge

Complete all three reps in about 30 minutes. Finish with one evidence row containing the source commit, producer, artifact locator, required and forbidden invariants, executed negative control, promotion state, and separate production state.

Practice remains **PENDING** until that evidence is retained.
