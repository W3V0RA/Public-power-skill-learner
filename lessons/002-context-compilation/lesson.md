# Public Power Skill #02 | Context Compilation

**Public edition date:** 2026-10-30  
**Status:** Generic educational adaptation; not a private learner transcript or implementation receipt.  
**Level:** Intermediate to advanced. Adjust the difficulty using your private onboarding profile.  
**Project practice:** Use invented data by default; substitute your own real project only with its owner's permission.

## What the capability is

Compile a concise task-specific packet before a model reasons. Include authoritative facts, freshness, constraints, tool access and required output, while excluding obsolete or distracting material.

A reliable implementation begins by declaring the input, the allowed actions, the expected evidence, and the point at which a human or tool must stop. Explain the workflow in terms of observable states rather than promising that a model will always make the correct judgment.

## Why it matters and why it is non-obvious

More context is not always better. Memory stores information, retrieval finds candidate evidence, and context compilation decides which fragments become the current working inputs.

Advanced operators separate three things that beginners often conflate: plausible output, verified technical operation, and verified real-world outcome. They also keep cost, privacy, and irreversibility visible so that a seemingly convenient automation does not silently create more work or risk.

## Fictional example

A fictional equipment support team must answer a question about one model. The compiler selects the exact manual revision and warranty policy, not the entire equipment catalog.

A generic way to reason about the example is:

```text
Declared objective -> Permitted input and authority -> Proposed operation
    -> Evidence or outcome check -> PASS / FAIL / UNVERIFIED
    -> Small, reversible follow-up if justified
```

**Failure case to test:** A newer informal note silently overrides an approved policy without an authority rule.

## Advanced operating pattern

First, collect an independently observed baseline. Second, choose one narrow intervention and write down which outputs should change. Third, execute only authorized mock or reversible actions. Fourth, inspect the result, its side effects, and at least one negative control. Fifth, document what is still unknown. Never improve a dashboard number by weakening the definition of success.

For any change that touches another person's records, money, account, communication, deployment or permissions, obtain explicit project-specific authorization and respect the platform's own controls. A general-purpose lesson is never approval for consequential actions.

## Tool or plugin opportunity

Use local Markdown files and a small script to assemble packets; introduce indexed retrieval only after measuring missing-context failures.

Tools are optional. Check that the tool is actually available and connected before describing a task as executed. Prefer what the learner already has and record usage costs only when observed.

## Practice reps

1. **Foundations (5–10 minutes):** Define five facts your current task requires and three categories of information it must exclude.
2. **Intermediate (10–15 minutes):** Create a packet with source, observed date, authority, unresolved conflicts and output format.
3. **Applied project (15–20 minutes):** Compare answers using an all-documents prompt and your compiled packet with the same evaluator.
4. **Advanced negative control (optional):** Introduce a conflicting outdated note and verify it is not quietly promoted as current truth.

For a first attempt, do these reps with fictional records. If you wish to apply them to a genuine project, use the private learner workspace produced by the interview and check your authorization boundary.

## Retention check

What is the difference between storage and current model context? Storage is retained knowledge; context is the selected input for this task.

For spaced repetition, revisit this skill after two later lessons by applying it to a different synthetic scenario rather than simply rereading the definitions.

## Daily challenge

Save a reusable context-packet template and one comparison result.

**Finish line:** Save the input or fixture, the expected result, actual test observations, and a short conclusion. Mark only supported outcomes `VERIFIED`; otherwise use `FAILED`, `BLOCKED`, or `UNVERIFIED`. Keep learner-specific evidence in private storage, not a public issue or this curriculum.

## Personalization prompt

> Adapt this skill to my current private goal, available tools, approved project scope and time budget. Give me one useful bounded application. Ask only for missing essential context. Do not invent my project details, account access, or measurements. Preserve protected-action approval gates and verify outcomes before claiming improvement.
