# Public Power Skill #01 | Shadow Mode and Promotion Gates

**Public edition date:** 2026-10-30  
**Status:** Generic educational adaptation; not a private learner transcript or implementation receipt.  
**Level:** Intermediate to advanced. Adjust the difficulty using your private onboarding profile.  
**Project practice:** Use invented data by default; substitute your own real project only with its owner's permission.

## What the capability is

Run an agent against realistic inputs without allowing it to make real-world changes. Preserve the action it would have taken, then compare the decision with independent evidence before expanding authority.

A reliable implementation begins by declaring the input, the allowed actions, the expected evidence, and the point at which a human or tool must stop. Explain the workflow in terms of observable states rather than promising that a model will always make the correct judgment.

## Why it matters and why it is non-obvious

A successful tool call is not proof that a business objective succeeded. Shadow evaluation is useful both for risk reduction and for collecting labeled decisions. Different capabilities can earn different levels of autonomy.

Advanced operators separate three things that beginners often conflate: plausible output, verified technical operation, and verified real-world outcome. They also keep cost, privacy, and irreversibility visible so that a seemingly convenient automation does not silently create more work or risk.

## Fictional example

A fictional help desk classifies incoming requests and drafts replies, but cannot send them. Reviewers compare drafts against documented policy and record disagreements.

A generic way to reason about the example is:

```text
Declared objective -> Permitted input and authority -> Proposed operation
    -> Evidence or outcome check -> PASS / FAIL / UNVERIFIED
    -> Small, reversible follow-up if justified
```

**Failure case to test:** One plausible draft is treated as permission to enable autonomous sending.

## Advanced operating pattern

First, collect an independently observed baseline. Second, choose one narrow intervention and write down which outputs should change. Third, execute only authorized mock or reversible actions. Fourth, inspect the result, its side effects, and at least one negative control. Fifth, document what is still unknown. Never improve a dashboard number by weakening the definition of success.

For any change that touches another person's records, money, account, communication, deployment or permissions, obtain explicit project-specific authorization and respect the platform's own controls. A general-purpose lesson is never approval for consequential actions.

## Tool or plugin opportunity

A spreadsheet or structured JSON Lines file is sufficient for a small pilot. A Git-hosted test harness can version examples and the promotion policy.

Tools are optional. Check that the tool is actually available and connected before describing a task as executed. Prefer what the learner already has and record usage costs only when observed.

## Practice reps

1. **Foundations (5–10 minutes):** Choose a recurring workflow and identify the proposed action, external side effect, and verified success condition.
2. **Intermediate (10–15 minutes):** Run five synthetic cases in recommendation-only mode. Save the proposal, supporting facts, and expected outcome.
3. **Applied project (15–20 minutes):** Create a promotion gate with minimum sample, critical failures, evidence quality, and explicit approval rules.
4. **Advanced negative control (optional):** Add intentionally unsafe cases and prove they are rejected before any authority expands.

For a first attempt, do these reps with fictional records. If you wish to apply them to a genuine project, use the private learner workspace produced by the interview and check your authorization boundary.

## Retention check

If a model returns a polished answer, did it necessarily complete the objective? No: evaluate the requested end state independently.

For spaced repetition, revisit this skill after two later lessons by applying it to a different synthetic scenario rather than simply rereading the definitions.

## Daily challenge

Produce one dated shadow-run report with independent labels and a no-side-effect verification.

**Finish line:** Save the input or fixture, the expected result, actual test observations, and a short conclusion. Mark only supported outcomes `VERIFIED`; otherwise use `FAILED`, `BLOCKED`, or `UNVERIFIED`. Keep learner-specific evidence in private storage, not a public issue or this curriculum.

## Personalization prompt

> Adapt this skill to my current private goal, available tools, approved project scope and time budget. Give me one useful bounded application. Ask only for missing essential context. Do not invent my project details, account access, or measurements. Preserve protected-action approval gates and verify outcomes before claiming improvement.
