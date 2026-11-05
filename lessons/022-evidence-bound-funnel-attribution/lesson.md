# 2026-11-04 | AI Power Skill #22 | Evidence-Bound Funnel Attribution

**Category:** Data analysis; research and go-to-market systems  
**Difficulty:** Advanced  
**Practice status:** PENDING until the learner retains objective evidence  
**Core principle:** Attribution is scoped evidence, not causal truth. Preserve first and last attributable touches at a verified outcome boundary, and keep clicks, inquiries, qualification, meetings, and revenue separate.

## What the capability is

Evidence-bound funnel attribution connects bounded acquisition evidence to progressively stronger business outcomes:

```text
touch -> visit -> inquiry accepted -> qualified -> meeting held -> proposal -> won revenue
```

The receipt should identify its taxonomy version, scope, first touch, last touch, objective outcome, and the fact that it is not a causal claim.

```json
{
  "taxonomy_version": "1.0",
  "scope": "page_session",
  "first_touch": {
    "source": "professional-network",
    "medium": "organic",
    "campaign": "operations-series",
    "content": "post-07",
    "landing_path": "/"
  },
  "last_touch": {
    "source": "newsletter",
    "medium": "email",
    "campaign": "follow-up",
    "landing_path": "/contact/"
  },
  "outcome": "inquiry_accepted",
  "causal_claim": false
}
```

Google's campaign guidance defines standardized UTM parameters for source, medium, campaign, campaign ID, source platform, content, and term. See [URL builders](https://support.google.com/analytics/answer/10917952) and [manual tagging](https://support.google.com/analytics/answer/11242870).

## Why it matters

- Clicks and impressions are weak evidence; qualified and commercial outcomes are stronger.
- Explicit scope prevents first-user, session, and event attribution from being compared as if they were identical.
- A standardized taxonomy allows campaigns and content variants to be compared over time.
- Normalized receipts give AI systems better inputs than screenshots or free-text analytics summaries.
- Privacy-minimized session storage can carry campaign context within a page session without creating a persistent identity graph. See [MDN sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage).

## What makes it non-obvious

1. **Attribution is not causation.** A tagged link does not prove it caused the outcome.
2. **Scope changes the answer.** User, session, and event dimensions can credit different interactions.
3. **Missing data must remain missing.** Direct or private-message traffic should not be reassigned for convenience.
4. **First and last touch answer different questions.** Preserve both without giving either automatic causal credit.
5. **Taxonomy drift breaks analysis.** Case, spelling, and campaign formats must be standardized.
6. **A browser click is not a lead.** Require a server or CRM receipt for the outcome.
7. **Collecting more can reduce safety.** Full referrer URLs and arbitrary queries often add risk without useful signal.

## Typical versus advanced use

| Typical | Advanced |
|---|---|
| Optimize clicks | Compare effort or cost per verified outcome |
| Store one last-click field | Preserve first touch, last touch, scope, and missingness |
| Use free-text campaign names | Use a versioned taxonomy |
| Store the complete referrer | Retain only external host and landing path |
| Accept every query parameter | Allowlist standardized campaign fields |
| Count form clicks as leads | Require server acceptance and CRM readback |
| Credit one campaign with revenue | Separate attribution evidence from causal claims |
| Summarize raw analytics with AI | Normalize events before AI reasoning |

## Immediate applications

| Workflow | First useful receipt | Decision enabled |
|---|---|---|
| Consulting website | Campaign touch attached to accepted inquiry | Which content produces qualified problems |
| Sales operations | Source attached through qualified, meeting, proposal, and won/lost | Effort per verified commercial outcome |
| Marketplace | Listing/referral touch attached to completed transaction | Which supply and demand channels work |
| Decision support | Recommendation context attached to accepted/rejected decision | Which evidence patterns improve decisions |
| Product onboarding | Acquisition touch attached to activated retained use | Which distribution surfaces produce value |

## Attribution contract

```json
{
  "taxonomy_version": "<version>",
  "allowed_fields": ["source", "medium", "campaign", "id", "source_platform", "content", "term", "referrer_host", "landing_path"],
  "scope": "page_session",
  "first_touch_rule": "first attributable touch in session",
  "last_touch_rule": "most recent attributable touch in session",
  "missing_state": "direct_or_unavailable",
  "forbidden_data": ["personal_information", "full_referrer_url", "secrets", "payment_data"],
  "outcome_states": ["inquiry_accepted", "qualified", "meeting_held", "proposal_sent", "won", "lost"],
  "causal_claim": false
}
```

## Ready-to-copy prompt

```text
Inspect the live acquisition workflow, analytics, CRM fields, privacy rules, and objective outcome receipts before editing.

Design the smallest evidence-bound attribution layer using existing infrastructure.

Requirements:
1. Define a versioned campaign taxonomy and allowed fields.
2. Preserve first and last attributable touches with explicit scope.
3. Exclude full referrer URLs, arbitrary queries, personal data, secrets, payment data, and unbounded text.
4. Keep direct/unavailable as an honest missing state.
5. Bind attribution to a server- or CRM-confirmed outcome, not a click.
6. Keep inquiry, qualification, meeting, proposal, won, and lost separate.
7. Add negative controls for invalid fields, sensitive values, internal navigation, and visitor-facing reflection.
8. Preserve consent, authorization, suppression, and current delivery behavior.
9. Report PASS, FAIL, or UNVERIFIED and do not claim causality without an experiment.

Do not add a paid analytics service, persistent identity graph, database, scheduler, or outreach action.
```

## Practice reps

### Rep 1: Separate scope and outcome — 5 minutes

Label the scope and strongest claim for a tagged landing-page visit, accepted inquiry, qualified CRM record, and recorded revenue.

**PASS:** every claim stops at its evidence boundary.  
**FAIL:** a tagged click is called causal revenue.  
**UNVERIFIED:** scope or receipt is missing.

### Rep 2: Build a naming taxonomy — 10 minutes

Define approved values for source and medium, a campaign format, and a stable content identifier. Create two links that differ only in content identifier.

**PASS:** content is comparable without fragmenting the campaign.  
**FAIL:** capitalization or naming varies.  
**UNVERIFIED:** taxonomy version or owner is absent.

### Rep 3: Fictional service-business capstone — 15 minutes

Map landing-page evidence through accepted inquiry, qualification, held meeting, proposal, and won/lost. Include one direct/unavailable fixture, one malformed or sensitive campaign fixture, and one counterexample where engagement creates no qualified outcome.

Choose one decision metric: operator minutes per qualified outcome, cost per qualified outcome, or qualified-to-won rate. Do not claim causal lift.

## Expected evidence

| Claim | PASS | FAIL | UNVERIFIED |
|---|---|---|---|
| Taxonomy | Versioned values used consistently | Free-text variants | Source unavailable |
| First/last touch | Rules and scope explicit | Unpredictable overwrites | Readback unavailable |
| Privacy | Allowlist and sensitive-value rejection pass | Full URL or private data retained | Payload unobservable |
| Outcome | Server/CRM receipt proves state | Click treated as outcome | State unavailable |
| Missingness | Direct/unavailable preserved | Missing data reassigned | Logic unknown |
| Causal language | Evidence, not causation | Cause claimed without experiment | Experiment absent |
| Business value | Verified outcome measured against effort/cost | Vanity metric alone | Sample insufficient |

## Retention check

- **Bitemporal truth:** record touch time and outcome time separately.
- **Evidence-chain auditing:** close the chain with the strongest objective receipt, not an AI summary.
- **Counterfactual testing:** causal claims require a valid holdout or randomized intervention.

## Tool/Plugin Opportunity

| Option | Unlocks | Setup | Use |
|---|---|---|---|
| Google Campaign URL Builder | Consistent tagged links | No new account | Standardize campaign links |
| Existing analytics | Session and event reports | Current property and taxonomy | Compare traffic and verified events |
| GitHub | Versioned taxonomy and validators | Repository access | Keep rules beside the workflow |
| CRM | Qualified and commercial outcomes | Field mapping and readback | Join acquisition evidence to outcomes |

No new paid tool is required.

## Daily challenge

Create one versioned taxonomy, one tagged-link pair, one first/last-touch scope, one outcome map, one privacy negative control, one direct/unavailable fixture, and one metric tied to qualified or won outcomes.

Practice remains **PENDING** until the evidence is retained.
