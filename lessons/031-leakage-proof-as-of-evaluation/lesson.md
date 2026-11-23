# 2026-11-22 | AI Power Skill #31 | Leakage-Proof As-Of Evaluation

**Category:** data analysis; evaluation and guardrails; go-to-market systems  
**Learner practice status:** PENDING

## Core principle

A fact can be true and still be unavailable to a decision.

Leakage-proof as-of evaluation reconstructs exactly what an Artificial Intelligence (AI) system could know at a historical decision cutoff. Each fact carries:

- **Occurrence time:** when the event happened.
- **Knowledge time:** when the system could actually use the evidence.

Evidence is eligible only when both times are at or before the cutoff. This prevents future information from making a model, agent, forecast, or business experiment look better than it would have performed live.

Scikit-learn’s official guidance describes data leakage as using information unavailable at prediction time, which produces overly optimistic evaluation. Its time-series cross-validator trains on earlier data and tests on later data because ordinary cross-validation can accidentally train on the future. See [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) and [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html).

## 1. What the capability is

The capability is a repeatable decision replay:

1. declare an exact decision cutoff;
2. include only evidence known by then;
3. train or calibrate on earlier windows;
4. evaluate on later windows;
5. test that post-cutoff evidence is rejected.

It applies beyond time-series forecasting. Sales stages, research findings, labels, corrected records, user feedback, catalog ratings, and agent memories all arrive over time.

## 2. Why it matters

Random splits and current database rows can create false confidence. A historical record may now contain a meeting note, corrected status, or enrichment value that did not exist when the decision was made.

Leakage can produce:

- inflated model metrics;
- false product validation;
- unreliable pipeline forecasts;
- unsafe agent promotion;
- prospect scores that collapse in production; and
- recommendations that quietly use later outcomes as inputs.

The business cost is a decision made with imaginary foresight.

## 3. What makes it non-obvious

Sorting by the event date is not enough. Imagine an agreement that occurred Friday but was not received until Monday. A Friday evaluation cannot count it, even though an ordinary report assigns it to Friday.

Other subtle leaks include:

- backfilled fields with no availability timestamp;
- preprocessing fit on the full dataset;
- labels that overlap a prediction window;
- later reviews or ratings used in earlier recommendation tests;
- thresholds changed after outcomes are visible;
- repeated organizations counted as separate evidence; and
- memory snapshots containing facts from after the simulated decision.

## 4. How advanced users work differently

| Typical approach | Advanced approach |
|---|---|
| One timestamp | Occurrence and knowledge timestamps |
| Random split | Walk-forward replay |
| Current row values | Values available at the cutoff |
| Tune and score together | Precommit rules; reserve future windows |
| Trust a strong metric | Inject post-cutoff negative controls |
| Enter totals manually | Derive totals from eligible receipts |

Advanced users also leave a gap when an action or label overlaps the boundary. They prefer a slightly worse honest metric over a better leaked metric.

## 5. Where to use it immediately

- **Lead scoring:** exclude meetings, stages, and enrichment learned after the score time.
- **Forecasting:** replay each forecast using the pipeline snapshot then available.
- **Product experiments:** count only evidence known before the review cutoff.
- **Recommendation systems:** exclude later feedback and catalog changes from earlier decisions.
- **Research agents:** freeze the evidence set before the go/no-go decision.
- **Autonomous agents:** promote only on traces and outcomes produced after the training window.

## Minimal contract

```json
{
  "decision_cutoff_at": "2026-11-20T23:59:59Z",
  "evidence": [
    {
      "receipt_id": "opaque-receipt",
      "subject_token": "opaque-subject",
      "occurred_at": "2026-11-18T16:00:00Z",
      "known_at": "2026-11-18T16:05:00Z"
    }
  ]
}
```

Eligibility requires both timestamps at or before the cutoff, a unique receipt identifier, and no duplicate subject for the same outcome. Use synthetic or opaque identifiers in evaluation artifacts.

## Tool/Plugin Opportunity

**Option:** GitHub plus the repository’s existing test runner.  
**Unlocks:** versioned evaluation rules, negative-control tests, reviewable changes, and reproducible evidence.  
**Setup:** requires a GitHub repository and permission to create a branch or pull request. No paid AI service is inherently required.  
**Example:** add a test that inserts a synthetic receipt one second after the decision cutoff and requires the verifier to reject it.

## Practice reps

### Rep 1 — Label availability

Take ten historical facts. Add occurrence and knowledge timestamps, choose a cutoff, and mark each fact eligible or ineligible.

**Pass:** a fact that happened before but became known after the cutoff is excluded.

### Rep 2 — Walk forward

Split four weekly windows. Train or configure on earlier weeks and evaluate on the next week. Compare the result with a random split and explain any difference.

**Pass:** every feature has a defensible availability time.

### Rep 3 — Negative-control capstone

Create a fictional receipt ledger for a scoring or validation decision. Derive the total from eligible unique subjects. Add a receipt one second after the cutoff.

**Pass:** the original ledger verifies, the future receipt fails, and no real personal data is present.

## Retention check

How do occurrence time and knowledge time differ? What rule must be frozen before the protected outcome window? What receipt connects an aggregate metric to its source evidence?

A strong answer: **the rule is precommitted, every counted fact was known by the cutoff, and every aggregate is traceable to eligible evidence.**

## Daily challenge

Choose one real scoring, forecasting, or validation decision. Write the exact cutoff, the two timestamps required on each fact, one post-cutoff negative control, and the decision threshold. Run the negative control today. The challenge remains PENDING until future evidence is actually rejected.

## Implementation notes

Start in dry-run mode. Do not modify production scores or send external messages. Store only sanitized test records. A green unit test proves the guard behaves on its test cases; it does not prove revenue impact, model quality, or production correctness.

