# 2026-11-12 | AI Power Skill #26 | Write-Ahead Compensation Ledgers for Agent Workflows

**Category:** automation, agents, distributed workflows and guardrails  
**Practice status:** PENDING

## Core principle

Before an automated worker performs a side effect that might need to be undone,
persist the compensation intent. Then perform the forward action and retain its
receipt.

~~~text
register compensation → perform action → retain receipt
                                      ↘ failure: compensate proven completions
~~~

If the workflow crosses an action that cannot be meaningfully undone, stop
calling later recovery a rollback. Mark an irreversible frontier and route
failure to explicit manual recovery.

## What the capability is

A write-ahead compensation ledger is a durable record for multi-step workflows
that span services or data stores where one database transaction cannot protect
the entire operation.

Classify every side-effecting step:

- **Retry-only:** No committed external effect is expected.
- **Compensable:** A domain-specific counteraction exists.
- **Irreversible:** No truthful automatic undo exists.

For compensable steps, retain a stable step identifier, forward and compensation
actions, a separate compensation idempotency key, registration state, forward
completion receipt and compensation completion receipt.

The Saga and compensating-transaction patterns coordinate local transactions
and run domain-specific counteractions when later steps fail. Compensation is
eventually consistent, may itself fail, and should be resumable and idempotent.

## Why it matters

An automated workflow might create a record, reserve a resource, generate an
artifact and publish it. A later exception does not cause every external system
to forget what already happened.

Write-ahead ledgers provide durable recovery, proof of which steps completed,
retry-safe compensation, explicit partial-completion states and a truthful
boundary between automatic recovery and manual repair.

## What makes it non-obvious

### Register before executing

If a worker performs the forward action and crashes before recording its
compensation, recovery lacks the instruction it needs.

### Compensation is not a snapshot restore

Restoring old data can overwrite valid concurrent changes. A compensation is a
domain action such as cancelling one reservation.

### Unknown is not completed

A crash after an external call but before a receipt produces an ambiguous
outcome. Reconcile it using the forward idempotency key before compensating.

### Compensation can fail

The compensation command needs its own idempotency key, status and receipt.

### Reverse order is only a default

Dependencies or business rules can require priority recovery or parallel
counteractions.

### Irreversible actions need a frontier

Sending, publishing, disclosing or settling cannot be honestly described as
undone. Complete validation and approval before the frontier.

## Advanced versus typical use

| Typical workflow | Advanced workflow |
|---|---|
| Add undo logic after failure | Register compensation first |
| Roll back only local data | Apply domain-specific counteractions |
| Compensate attempted steps | Compensate receipt-confirmed steps |
| Retry blindly | Use a compensation idempotency key |
| Assume reverse order | Encode dependencies |
| Claim everything rolled back | Mark the irreversible frontier |
| Store one status | Store forward and compensation receipts |
| Let any worker recover | Check current ownership and authority |

## Practical contract

~~~json
{
  "workflow_id": "job-id",
  "step_id": "reserve-resource",
  "forward_action": "resource.reserve",
  "reversibility": "compensable",
  "compensation_action": "resource.release",
  "compensation_idempotency_key": "job:reserve:release",
  "state": "registered",
  "forward_receipt": null,
  "compensation_receipt": null
}
~~~

Useful states include REGISTERED, FORWARD_COMPLETED, FORWARD_UNVERIFIED,
COMPENSATING, COMPENSATED, IRREVERSIBLE_FRONTIER_CROSSED and
MANUAL_RECOVERY_REQUIRED.

## Implementation workflow

1. Inventory every external mutation.
2. Classify it as retry-only, compensable or irreversible.
3. Persist compensation before a compensable forward action.
4. Recheck current authority before executing.
5. Retain the forward receipt.
6. Reconcile ambiguous outcomes.
7. Plan recovery from proven completions.
8. Record compensation receipts.
9. Stop automatic rollback claims at the irreversible frontier.

## Where to use it

- Multi-service onboarding
- Content production and publication
- Customer Relationship Management automation
- Infrastructure staging and deployment
- Inventory or booking workflows
- Agent-driven document processing
- Long-running approval workflows

## Ready-to-copy prompt

~~~text
Inspect the workflow, side effects, retries, approvals, idempotency controls and
durable checkpoints.

Design the smallest write-ahead compensation ledger.

1. Inventory external mutations.
2. Classify each as retry-only, compensable or irreversible.
3. Register compensation before the forward call.
4. Use separate forward and compensation idempotency keys.
5. Store forward and compensation receipts.
6. Treat ambiguous forward outcomes as UNVERIFIED.
7. Compensate only proven completions.
8. Define dependency-aware recovery order.
9. Mark the irreversible frontier.
10. After the frontier, require manual recovery rather than claiming rollback.
11. Preserve access, policy, budget, approval and ownership controls.
12. Test missing registration, conflicting receipts and false rollback claims.

Do not execute live side effects during the design exercise.
~~~

## Practice reps

### Rep 1 — Classify three steps

Choose a workflow and mark each step retry-only, compensable or irreversible.
Name the real counteraction for each compensable step.

- **PASS:** Every side effect has an honest classification.
- **FAIL:** “Undo it” is the only counteraction.
- **UNVERIFIED:** The external system was not inspected.

### Rep 2 — Build a recovery ledger

Model: create task → update status → prepare message → send message.

Register compensation for task creation and status update. Treat message
sending as the irreversible frontier.

- **PASS:** Failure before send produces a receipt-backed plan.
- **FAIL:** The plan claims a sent message was rolled back.
- **UNVERIFIED:** Required receipts are missing.

### Rep 3 — Crash matrix

Simulate a crash before the forward call, after the call but before the receipt,
after the receipt and after the irreversible frontier.

- **PASS:** The results are respectively not-run, unverified, compensable and
  manual-recovery-required.
- **FAIL:** Every case becomes the same retry.
- **UNVERIFIED:** The ledger was not persisted or tested.

## Retention check

1. Why does the compensation need its own idempotency key?
2. What belongs before an irreversible frontier?
3. Why must a stale worker be unable to change the ledger?

**Expected answer:** Forward and recovery commands are distinct operations.
Approval and validation must finish before the point of no return. An obsolete
worker must not change current recovery evidence.

## Tool/Plugin Opportunity

**GitHub**

- **Unlocks:** Versioned workflow contracts, tests, review and remote receipts.
- **Setup:** Requires a connected account and repository permission.
- **Use case:** Add a compensation ledger beside an existing durable workflow.
- **Limit:** It cannot perform or verify a third-party business counteraction.

No new paid software is required for the pattern itself.

## Daily challenge

In 30 minutes, create one side-effect inventory, one reversibility class per
step, one write-ahead compensation record, separate forward and compensation
idempotency keys, one ambiguous-outcome rule, one irreversible frontier, one
manual-recovery state and PASS, FAIL or UNVERIFIED for every assertion.

Keep the exercise in dry-run mode. Practice remains **PENDING** until evidence is retained.
