# Public Power Skill #14 | Process Mining

**Public edition date:** 2026-10-30  
**Status:** Generic educational adaptation; not a private learner transcript or implementation receipt.  
**Level:** Intermediate to advanced. Adjust the difficulty using your private onboarding profile.  
**Project practice:** Use invented data by default; substitute your own real project only with its owner's permission.

## What the capability is

Reconstruct workflow paths from timestamped events, measure stage delays and variants, and compare observed behavior against a declared process.

A reliable implementation begins by declaring the input, the allowed actions, the expected evidence, and the point at which a human or tool must stop. Explain the workflow in terms of observable states rather than promising that a model will always make the correct judgment.

## Why it matters and why it is non-obvious

Dashboards show totals; process mining reveals how work actually moved. Elapsed waiting time is different from hands-on labor, and missing events are not automatically violations.

Advanced operators separate three things that beginners often conflate: plausible output, verified technical operation, and verified real-world outcome. They also keep cost, privacy, and irreversibility visible so that a seemingly convenient automation does not silently create more work or risk.

## Fictional example

A fictional repair intake process reveals that approvals wait many hours even though drafting takes minutes.

A generic way to reason about the example is:

```text
Declared objective -> Permitted input and authority -> Proposed operation
    -> Evidence or outcome check -> PASS / FAIL / UNVERIFIED
    -> Small, reversible follow-up if justified
```

**Failure case to test:** An observed delay is asserted as the proven root cause of lost revenue without further analysis.

## Advanced operating pattern

First, collect an independently observed baseline. Second, choose one narrow intervention and write down which outputs should change. Third, execute only authorized mock or reversible actions. Fourth, inspect the result, its side effects, and at least one negative control. Fifth, document what is still unknown. Never improve a dashboard number by weakening the definition of success.

For any change that touches another person's records, money, account, communication, deployment or permissions, obtain explicit project-specific authorization and respect the platform's own controls. A general-purpose lesson is never approval for consequential actions.

## Tool or plugin opportunity

Start with CSV event logs and Python; PM4Py is an optional open-source library once data quality supports deeper analysis.

Tools are optional. Check that the tool is actually available and connected before describing a task as executed. Prefer what the learner already has and record usage costs only when observed.

## Practice reps

1. **Foundations (5–10 minutes):** Map one workflow into event names with occurrence timestamps.
2. **Intermediate (10–15 minutes):** Calculate a stage-to-stage elapsed-time distribution from synthetic cases.
3. **Applied project (15–20 minutes):** Compare observed paths against an expected path while labeling missing evidence.
4. **Advanced negative control (optional):** Design a bounded trial of an improvement and define a measurable primary outcome.

For a first attempt, do these reps with fictional records. If you wish to apply them to a genuine project, use the private learner workspace produced by the interview and check your authorization boundary.

## Retention check

Does a missing approval event prove approval never happened? Not without establishing log completeness.

For spaced repetition, revisit this skill after two later lessons by applying it to a different synthetic scenario rather than simply rereading the definitions.

## Daily challenge

Create a small process event log and identify one verified delay worth investigating.

**Finish line:** Save the input or fixture, the expected result, actual test observations, and a short conclusion. Mark only supported outcomes `VERIFIED`; otherwise use `FAILED`, `BLOCKED`, or `UNVERIFIED`. Keep learner-specific evidence in private storage, not a public issue or this curriculum.

## Personalization prompt

> Adapt this skill to my current private goal, available tools, approved project scope and time budget. Give me one useful bounded application. Ask only for missing essential context. Do not invent my project details, account access, or measurements. Preserve protected-action approval gates and verify outcomes before claiming improvement.
