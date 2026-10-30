# Public Power Skill #13 | Just-in-Time Tool Discovery

**Public edition date:** 2026-10-30  
**Status:** Generic educational adaptation; not a private learner transcript or implementation receipt.  
**Level:** Intermediate to advanced. Adjust the difficulty using your private onboarding profile.  
**Project practice:** Use invented data by default; substitute your own real project only with its owner's permission.

## What the capability is

Expose only the tools needed for the current task after checking version, side effects, permissions and tenant scope. Discoverable does not mean executable.

A reliable implementation begins by declaring the input, the allowed actions, the expected evidence, and the point at which a human or tool must stop. Explain the workflow in terms of observable states rather than promising that a model will always make the correct judgment.

## Why it matters and why it is non-obvious

Shorter tool context can reduce confusion, but dynamic loading adds latency. Tool descriptions are not security policies; enforce authorization in the executor.

Advanced operators separate three things that beginners often conflate: plausible output, verified technical operation, and verified real-world outcome. They also keep cost, privacy, and irreversibility visible so that a seemingly convenient automation does not silently create more work or risk.

## Fictional example

A fictional research-only task may load search and note-drafting tools, but not the message-sending operation.

A generic way to reason about the example is:

```text
Declared objective -> Permitted input and authority -> Proposed operation
    -> Evidence or outcome check -> PASS / FAIL / UNVERIFIED
    -> Small, reversible follow-up if justified
```

**Failure case to test:** A malicious tool description labels a write operation as read-only, and the executor accepts the claim.

## Advanced operating pattern

First, collect an independently observed baseline. Second, choose one narrow intervention and write down which outputs should change. Third, execute only authorized mock or reversible actions. Fourth, inspect the result, its side effects, and at least one negative control. Fifth, document what is still unknown. Never improve a dashboard number by weakening the definition of success.

For any change that touches another person's records, money, account, communication, deployment or permissions, obtain explicit project-specific authorization and respect the platform's own controls. A general-purpose lesson is never approval for consequential actions.

## Tool or plugin opportunity

Use a local tool catalog and a deterministic eligibility filter. Introduce runtime-native deferred loading only where explicitly supported.

Tools are optional. Check that the tool is actually available and connected before describing a task as executed. Prefer what the learner already has and record usage costs only when observed.

## Practice reps

1. **Foundations (5–10 minutes):** List the tools a task needs now and those it should never invoke.
2. **Intermediate (10–15 minutes):** Build a tiny catalog with versions, side effects and required permissions.
3. **Applied project (15–20 minutes):** Select the smallest eligible tool set for three synthetic objectives.
4. **Advanced negative control (optional):** Use a misleading description as a negative control and verify the executor denies the write.

For a first attempt, do these reps with fictional records. If you wish to apply them to a genuine project, use the private learner workspace produced by the interview and check your authorization boundary.

## Retention check

Does knowing a tool exists grant authority to call it? No.

For spaced repetition, revisit this skill after two later lessons by applying it to a different synthetic scenario rather than simply rereading the definitions.

## Daily challenge

Demonstrate a tool-discovery gate that rejects an unauthorized action.

**Finish line:** Save the input or fixture, the expected result, actual test observations, and a short conclusion. Mark only supported outcomes `VERIFIED`; otherwise use `FAILED`, `BLOCKED`, or `UNVERIFIED`. Keep learner-specific evidence in private storage, not a public issue or this curriculum.

## Personalization prompt

> Adapt this skill to my current private goal, available tools, approved project scope and time budget. Give me one useful bounded application. Ask only for missing essential context. Do not invent my project details, account access, or measurements. Preserve protected-action approval gates and verify outcomes before claiming improvement.
