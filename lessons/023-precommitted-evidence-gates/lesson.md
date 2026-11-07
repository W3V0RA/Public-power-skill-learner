# 2026-11-06 | AI Power Skill #23 | Precommitted Evidence Gates for AI-Assisted Experiments

**Category:** Evaluation and guardrails; agents; product research  
**Difficulty:** Advanced  
**Practice status:** PENDING  
**Core principle:** AI may collect and challenge evidence, but a versioned deterministic gate—not an after-the-fact narrative—decides whether an experiment passes, continues, pivots, stops, or remains unverified.

## What the capability is

A precommitted evidence gate is a machine-checkable contract created before outcomes are interpreted:

    hypothesis -> frozen outcome rules -> evidence collection
               -> sanitized snapshot -> deterministic evaluator -> decision

It defines outcomes, receipts, deduplication, missingness, review points, integrity holds, deviations, and final states.

## Why it matters

- Stops criteria from moving after results appear.
- Prevents persuasive AI summaries from becoming proof.
- Preserves unknown separately from zero.
- Separates early signals from final evaluation.
- Retains negative results as reusable evidence.
- Gives each experiment a decision boundary.

Open Science Framework guidance recommends deciding in advance what counts as evidence and using explicit if/then criteria. See [OSF guidance](https://help.osf.io/article/626-simplifying-the-preregistration-process).

## What makes it non-obvious

1. A metric name is not a receipt definition.
2. Engagement and stated preference are not purchase commitments.
3. Missing evidence remains unknown.
4. Repeated peeking changes interpretation.
5. Deviations are useful when retained and disclosed.
6. A deterministic rule does not establish causality or statistical significance.

## Typical versus advanced use

| Typical | Advanced |
|---|---|
| Ask AI if results look promising | Freeze the gate and ask AI to challenge inputs |
| Count views | Require primary-outcome receipts |
| Treat missing analytics as zero | Preserve null and return UNVERIFIED |
| Stop when results look favorable | Use fixed review points |
| Change criteria after weak results | Disclose a deviation and version the next test |
| Let a summary decide | Use a deterministic evaluator |

## Immediate applications

| Workflow | Gate | Objective evidence |
|---|---|---|
| Product validation | Build, pivot, or stop | Qualified conversations and commitments |
| Outreach | Promote a sequence | Qualified outcomes per eligible send |
| Agent release | Promote a capability | Evaluator coverage, safety, rollback |
| Marketplace | Expand a loop | Eligible completed transactions |
| Decision support | Adopt a workflow | Accepted decisions with outcome readback |

## Decision contract

    {
      "hypothesis": "<falsifiable claim>",
      "policy_version": "<immutable version>",
      "review_points": ["<fixed date or sample boundary>"],
      "primary_outcomes": ["<objective outcome>"],
      "receipt_requirements": ["<independent proof>"],
      "deduplication_unit": "<business decision unit>",
      "missing_state": null,
      "integrity_holds": ["policy incident", "broken instrumentation"],
      "deviation_rule": "retain original and disclose change",
      "decision_states": ["NOT_LAUNCHED", "UNVERIFIED", "CONTINUE", "PASS", "PIVOT_OR_STOP"],
      "causal_claim": false
    }

## Ready-to-copy prompt

    Reconcile the live experiment, canonical system, authorized channels,
    instrumentation, outcome receipts, and review date.

    Create a precommitted evidence gate:
    1. State one falsifiable hypothesis.
    2. Define primary outcomes and exact receipts.
    3. Define the deduplication unit.
    4. Preserve unknown as null.
    5. Separate secondary signals from primary outcomes.
    6. Define fixed review points.
    7. Treat early threshold crossing as non-final.
    8. Hold interpretation after policy or instrumentation incidents.
    9. Require deviation review when criteria change.
    10. Use a deterministic evaluator.
    11. Separate business rules from causal/statistical claims.
    12. Record PASS, FAIL, or UNVERIFIED.

    Do not publish, send outreach, collect payment, modify customer records,
    or generate synthetic conversion events.

## Practice reps

### Rep 1: Evidence ladder — 5 minutes

Classify a page view, positive comment, qualified buyer meeting, price preference, and written pilot commitment.

**PASS:** each stops at its evidence boundary.  
**FAIL:** engagement becomes commitment.  
**UNVERIFIED:** the receipt is inaccessible.

### Rep 2: Freeze a gate — 10 minutes

Write the hypothesis, review point, two outcomes, receipt rules, deduplication unit, missing-state rule, integrity hold, deviation rule, and final states.

**PASS:** independent evaluators reach the same state.  
**FAIL:** persuasive prose changes the answer.  
**UNVERIFIED:** required evidence is missing.

### Rep 3: Fictional service experiment — 15 minutes

Build a sanitized snapshot for a fictional automation-safety service. Include unknown analytics, a duplicated organization, early threshold crossing, a policy incident, and a disclosed deviation. Run the frozen evaluator.

## Expected evidence

| Claim | PASS | FAIL | UNVERIFIED |
|---|---|---|---|
| Policy | Versioned before interpretation | Rewritten after results | History unavailable |
| Outcomes | Exact receipts | Vanity metric substituted | Receipt inaccessible |
| Missingness | Null remains null | Unknown becomes zero | Source unclear |
| Deduplication | Decision unit verified | Duplicate counted | Reconciliation unavailable |
| Early signal | Non-final | Called success | Review point unknown |
| Deviation | Retained and disclosed | Hidden | History unavailable |
| Decision | Reproducible evaluator | Narrative overrides | Inputs incomplete |

## Retention check

- Proof-of-Problem Agents collect problem evidence; the gate controls the business decision.
- Bitemporal Truth Maintenance keeps occurrence time separate from knowledge time.
- Evidence-Bound Funnel Attribution explains the route, not the outcome.

## Tool/Plugin Opportunity

| Option | Unlocks | Setup | Use |
|---|---|---|---|
| GitHub | Versioned policies and evaluators | Repository access | Keep rules beside the experiment |
| Existing analytics | Secondary exposure evidence | Current instrumentation | Confirm traffic without calling it demand |
| Existing CRM | Qualification receipts | Field mapping | Verify unique decision units |
| ChatGPT/Codex | Reconciliation and contradiction search | Minimized inputs | Build sanitized snapshots |

No new paid tool is required.

## Daily challenge

Produce one versioned gate, one sanitized snapshot, one deterministic result, one missing-evidence fixture, one early-signal fixture, one deviation fixture, and PASS / FAIL / UNVERIFIED for every claim.

Practice remains **PENDING** until evidence is retained.
