# Public Power Skill #06 | Capability-Graph Orchestration

**Public edition date:** 2026-10-30  
**Status:** Generic educational adaptation; not a private learner transcript or implementation receipt.  
**Level:** Intermediate to advanced. Adjust the difficulty using your private onboarding profile.  
**Project practice:** Use invented data by default; substitute your own real project only with its owner's permission.

## What the capability is

Model each tool as a state transition with declared preconditions, outputs, side effects and failures. Plan objectives as valid paths through those transitions.

A reliable implementation begins by declaring the input, the allowed actions, the expected evidence, and the point at which a human or tool must stop. Explain the workflow in terms of observable states rather than promising that a model will always make the correct judgment.

## Why it matters and why it is non-obvious

Names of products and tools are not plans. The planner must find prerequisite states first and must not invent missing prerequisites.

Advanced operators separate three things that beginners often conflate: plausible output, verified technical operation, and verified real-world outcome. They also keep cost, privacy, and irreversibility visible so that a seemingly convenient automation does not silently create more work or risk.

## Fictional example

A fictional customer-support request moves from identified customer to verified entitlement to approved solution to a draft response.

A generic way to reason about the example is:

```text
Declared objective -> Permitted input and authority -> Proposed operation
    -> Evidence or outcome check -> PASS / FAIL / UNVERIFIED
    -> Small, reversible follow-up if justified
```

**Failure case to test:** A communication tool runs despite the missing verified recipient prerequisite.

## Advanced operating pattern

First, collect an independently observed baseline. Second, choose one narrow intervention and write down which outputs should change. Third, execute only authorized mock or reversible actions. Fourth, inspect the result, its side effects, and at least one negative control. Fifth, document what is still unknown. Never improve a dashboard number by weakening the definition of success.

For any change that touches another person's records, money, account, communication, deployment or permissions, obtain explicit project-specific authorization and respect the platform's own controls. A general-purpose lesson is never approval for consequential actions.

## Tool or plugin opportunity

Start with a JSON capability registry and a simple graph traversal; only later evaluate workflow engines if actual scale requires them.

Tools are optional. Check that the tool is actually available and connected before describing a task as executed. Prefer what the learner already has and record usage costs only when observed.

## Practice reps

1. **Foundations (5–10 minutes):** List the initial and final states of one process.
2. **Intermediate (10–15 minutes):** Draw four intermediary states and the capability responsible for each transition.
3. **Applied project (15–20 minutes):** Write an input/output contract for each edge, including failure behavior.
4. **Advanced negative control (optional):** Remove one prerequisite and show that the planner refuses to improvise it.

For a first attempt, do these reps with fictional records. If you wish to apply them to a genuine project, use the private learner workspace produced by the interview and check your authorization boundary.

## Retention check

Can the model proceed when a required state is unknown? No; it must satisfy or fail the prerequisite.

For spaced repetition, revisit this skill after two later lessons by applying it to a different synthetic scenario rather than simply rereading the definitions.

## Daily challenge

Produce a tested five-step capability graph from a synthetic objective.

**Finish line:** Save the input or fixture, the expected result, actual test observations, and a short conclusion. Mark only supported outcomes `VERIFIED`; otherwise use `FAILED`, `BLOCKED`, or `UNVERIFIED`. Keep learner-specific evidence in private storage, not a public issue or this curriculum.

## Personalization prompt

> Adapt this skill to my current private goal, available tools, approved project scope and time budget. Give me one useful bounded application. Ask only for missing essential context. Do not invent my project details, account access, or measurements. Preserve protected-action approval gates and verify outcomes before claiming improvement.
