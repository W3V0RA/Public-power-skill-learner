# 2026-11-08 | AI Power Skill #24 | Value-of-Information Gated Research

**Category:** research systems, decision analysis, and agent orchestration  
**Practice status:** PENDING / UNVERIFIED  
**Core principle:** Acquire information only when a plausible result can change a named decision and the expected improvement is greater than the full cost of learning.

## What the capability is

Value-of-Information Gated Research puts a decision contract in front of every browsing, retrieval, interview, test, or data-purchase request. Before a tool runs, define:

1. the decision and allowed actions;
2. the current preferred action;
3. the possible findings;
4. the best action under each finding;
5. probability and utility estimates;
6. collection cost, delay, privacy exposure, and review burden; and
7. a precommitted `COLLECT`, `SKIP`, or `REFRAME` rule.

The formal quantity is Expected Value of Sample Information (EVSI):

`net information value = expected value after the sample − value of the best current action − collection cost`

Collect only when at least one credible outcome changes the preferred action and net value clears the chosen threshold. Use one consistent unit, such as dollars, hours, risk-adjusted points, or successful outcomes. Label estimates honestly and test sensitivity.

## Why it matters

Generative Artificial Intelligence (AI) makes research abundant. The scarce resource is attention: which answer can improve the next decision?

This pattern prevents an agent from producing polished but decision-irrelevant reports. It also makes stopping legitimate. If every plausible result leads to the same action, more research has no decision value before cost.

## What makes it non-obvious

- **Accuracy is not the same as usefulness.** A true answer can leave the decision unchanged.
- **Information value depends on available actions.** Evidence cannot improve a decision when the action it supports is unavailable or unauthorized.
- **Cost includes more than money.** Add time, delay, privacy exposure, human review, sample bias, and opportunity cost.
- **The switch rule comes first.** Writing it after retrieval invites rationalization.
- **Qualitative gates are valid.** When numbers would be false precision, score decision impact, feasibility, and cost with explicit bands.

## How advanced users differ

| Typical behavior | Advanced behavior |
| --- | --- |
| “Research this topic.” | “Which result changes which action?” |
| Optimize answer quality. | Optimize expected decision improvement per unit cost. |
| Treat every unknown as important. | Rank uncertainties that separate competing actions. |
| Continue until uncertainty is low. | Stop when evidence cannot cross the decision boundary. |
| Count a report as progress. | Count a better-supported decision or justified `SKIP` as progress. |

## Five-part workflow

### 1. Decision

Write one decision and two to four mutually exclusive actions. “Learn about buyers” is not a decision. “Run a pilot, revise the offer, or pause it” is.

### 2. Baseline

Record the current preferred action, dated evidence, assumptions, and utility measure.

### 3. Outcome matrix

For each candidate information source, list mutually exclusive findings, estimated probabilities, and the best action under each finding. If no outcome changes the action, skip that source.

### 4. Total cost

Include cash, time, latency, privacy, review, and execution risk. Use ranges when estimates are weak.

### 5. Gate and receipt

Choose `COLLECT` only when the action can switch and expected net information value is positive. Preserve the contract, evidence, actual decision, and later outcome.

## Ready-to-copy prompt

```text
Act as a decision analyst. Do not research yet.

Decision: [one decision]
Allowed actions: [2-4 mutually exclusive actions]
Current preferred action and evidence: [action, sources, date]
Objective and utility unit: [money, hours, successful outcomes, risk-adjusted points]
Candidate information sources: [queries, tests, files, interviews, connectors]
Constraints: [time, budget, privacy, authority, approvals]

For each information source, return:
1. mutually exclusive plausible outcomes;
2. estimated probability of each outcome, labeled as an estimate;
3. best action and utility under each outcome;
4. whether any outcome changes the current action;
5. total collection cost and risks;
6. gross and net information value, or a qualitative impact × feasibility score;
7. COLLECT, SKIP, or REFRAME;
8. a stop rule and evidence receipt.

Challenge assumptions with optimistic and pessimistic sensitivity cases. If no plausible result changes the action, recommend SKIP. Ask for missing inputs instead of inventing them.
```

## Where to apply it

- **Product discovery:** decide which customer question can alter the next build or pause decision.
- **Sales research:** gate enrichment by whether it can change qualification, discovery, proposal, or close-plan action.
- **Model evaluation:** test only uncertainties that could change the selected model or routing policy.
- **Automation:** stop an agent from calling another tool once the action is stable.
- **Operations:** rank audits, experiments, and monitoring work by expected decision impact and feasibility.

## Tool/Plugin Opportunity

A chat assistant connected to the user's authorized project files can inspect the current decision log, build the matrix, and preserve the receipt. Setup requires the user's own account permissions and an explicit mutation policy. A spreadsheet is sufficient for the calculation; no paid tool is required. Connections do not validate subjective probabilities and never authorize spending, outreach, data collection, or deployment.

## Practice reps

### Rep 1 — Switch test

Pick one research request. Write the current action and three plausible findings. Map each finding to the resulting action.

- **PASS:** at least one credible finding changes the action, or the request is explicitly skipped.
- **FAIL:** the only benefit is “knowing more.”
- **UNVERIFIED:** the mapping was not saved.

### Rep 2 — Qualitative gate

Compare two evidence sources using `decision impact × feasibility − cost`, with low/medium/high bands. Do not retrieve evidence until the matrix exists.

- **PASS:** the selected source has a switch result, bounded cost, and stop rule.
- **FAIL:** selection is based only on breadth, novelty, or confidence.
- **UNVERIFIED:** the matrix was generated but not reviewed against current project evidence.

### Rep 3 — Quantitative capstone

For a real project decision, define two actions and two candidate information sources. Estimate outcome probabilities, outcome-contingent utilities, and total costs. Run optimistic and pessimistic cases.

- **PASS:** the ranking survives the stated sensitivity range, or returns `REFRAME` honestly.
- **FAIL:** mixed units, probabilities that do not sum to one, omitted costs, or no action switch.
- **UNVERIFIED:** arithmetic passes but assumptions lack review or evidence.

## Retention check

1. How does answerability differ from information value?  
2. Why is disagreement sampling useful only after the decision boundary is defined?  
3. Why must the switch rule be precommitted?

Expected answer: answerability asks whether evidence can support a claim; information value asks whether obtaining it can improve the decision. Disagreement matters when resolving it could change the action. Precommitment prevents moving the goalposts after seeing results.

## Daily challenge

In 30 minutes, produce one decision contract with two actions, two candidate information sources, a switch test, total-cost estimate, sensitivity case, and `COLLECT/SKIP/REFRAME` result. Finish when one source is authorized for later collection or all are explicitly skipped. Do not perform spending, outreach, production changes, or publication during the exercise.

## Sources

- United States Geological Survey primer: https://pubs.usgs.gov/publication/70159195
- United States Geological Survey sample-information framework: https://pubs.usgs.gov/publication/70248965
- United States Geological Survey qualitative application: https://pubs.usgs.gov/publication/ofr20261026/full
- National Institute of Standards and Technology measurement guidance: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

Practice remains **PENDING / UNVERIFIED** until objective evidence is recorded.
