# Public Power Skill #12 | Bitemporal Truth Maintenance

**Public edition date:** 2026-10-30  
**Status:** Generic educational adaptation; not a private learner transcript or implementation receipt.  
**Level:** Intermediate to advanced. Adjust the difficulty using your private onboarding profile.  
**Project practice:** Use invented data by default; substitute your own real project only with its owner's permission.

## What the capability is

Store both when a fact applied and when the system recorded it. Track which decisions depend on historical claim versions so material changes can trigger revalidation.

A reliable implementation begins by declaring the input, the allowed actions, the expected evidence, and the point at which a human or tool must stop. Explain the workflow in terms of observable states rather than promising that a model will always make the correct judgment.

## Why it matters and why it is non-obvious

Observing a changed website today does not establish when the underlying real-world change occurred. Keep unknown valid-time fields unknown.

Advanced operators separate three things that beginners often conflate: plausible output, verified technical operation, and verified real-world outcome. They also keep cost, privacy, and irreversibility visible so that a seemingly convenient automation does not silently create more work or risk.

## Fictional example

A fictional directory first lists one manager and later a replacement. A pending task that depends on the original listing is flagged for review.

A generic way to reason about the example is:

```text
Declared objective -> Permitted input and authority -> Proposed operation
    -> Evidence or outcome check -> PASS / FAIL / UNVERIFIED
    -> Small, reversible follow-up if justified
```

**Failure case to test:** Old evidence is overwritten and a made-up effective date is assigned to the new claim.

## Advanced operating pattern

First, collect an independently observed baseline. Second, choose one narrow intervention and write down which outputs should change. Third, execute only authorized mock or reversible actions. Fourth, inspect the result, its side effects, and at least one negative control. Fifth, document what is still unknown. Never improve a dashboard number by weakening the definition of success.

For any change that touches another person's records, money, account, communication, deployment or permissions, obtain explicit project-specific authorization and respect the platform's own controls. A general-purpose lesson is never approval for consequential actions.

## Tool or plugin opportunity

Relational tables with timestamps and dependency identifiers are enough for a first implementation; a graph database is optional.

Tools are optional. Check that the tool is actually available and connected before describing a task as executed. Prefer what the learner already has and record usage costs only when observed.

## Practice reps

1. **Foundations (5–10 minutes):** Separate observed date from effective date for a changing fact.
2. **Intermediate (10–15 minutes):** Store two conflicting source-backed claim versions.
3. **Applied project (15–20 minutes):** Link one dependent draft to the earlier claim.
4. **Advanced negative control (optional):** Change the canonical claim and verify the downstream artifact needs review without deleting history.

For a first attempt, do these reps with fictional records. If you wish to apply them to a genuine project, use the private learner workspace produced by the interview and check your authorization boundary.

## Retention check

Does the date the system discovered a change prove the date the change happened? No.

For spaced repetition, revisit this skill after two later lessons by applying it to a different synthetic scenario rather than simply rereading the definitions.

## Daily challenge

Build a three-record timeline and one dependency invalidation test.

**Finish line:** Save the input or fixture, the expected result, actual test observations, and a short conclusion. Mark only supported outcomes `VERIFIED`; otherwise use `FAILED`, `BLOCKED`, or `UNVERIFIED`. Keep learner-specific evidence in private storage, not a public issue or this curriculum.

## Personalization prompt

> Adapt this skill to my current private goal, available tools, approved project scope and time budget. Give me one useful bounded application. Ask only for missing essential context. Do not invent my project details, account access, or measurements. Preserve protected-action approval gates and verify outcomes before claiming improvement.
