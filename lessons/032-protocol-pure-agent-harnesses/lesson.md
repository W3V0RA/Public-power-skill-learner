# 2026-11-24 | AI Power Skill #32 | Protocol-Pure Agent Harnesses

**Category:** Model Context Protocol (MCP), coding agents, evaluation, and connector reliability  
**Status:** Educational; practice **PENDING** until evidenced.

## Core principle

When software parses an Artificial Intelligence (AI) agent's output, the answer channel is a protocol—not a console. Reserve standard output (`stdout`) for the machine-readable response, send logs to standard error (`stderr`), and fail closed if anything contaminates the protocol channel.

## What the capability is

A **protocol-pure agent harness** wraps a model runner, tool server, benchmark subject, or command-line agent and assigns every byte one purpose:

| Channel | Allowed content |
| --- | --- |
| Standard input | One bounded request |
| Standard output | Only the validated answer or wire protocol |
| Standard error | Logs and diagnostics |
| Exit status | Success or contract failure |

The harness validates the request, captures the subject's output streams separately, rejects accidental writes to `stdout`, validates the returned answer, and emits no answer bytes when the contract fails.

## Why it matters

An agent can reason correctly and still deliver an invalid artifact. A startup banner, debug print, progress line, warning, or import notice can make a correct response unparsable. If a wrapper “fixes” the stream by taking the last line or extracting the first JSON object, it creates false passes and hides the integration defect.

Protocol purity gives you four separate verdicts instead of one vague result:

1. Did the process run?
2. Was the protocol channel clean?
3. Did the response satisfy its schema?
4. Was the answer semantically correct and authorized?

This distinction improves benchmark reproducibility, connector reliability, and debugging speed.

## What makes it non-obvious

Terminals often display `stdout` and `stderr` together, so a session can look correct to a person while being invalid to a parser. Capturing streams separately is also not enough. A robust harness must bound input and output, reject blank or NUL-containing text, sanitize exceptions, and guarantee that a failed exchange writes nothing to the answer channel.

The harness proves transport conformance only. It does not prove that an answer is true, safe, authorized, or useful. Those remain separate checks.

## How advanced users apply it differently

| Typical user | Advanced user |
| --- | --- |
| Strips banners until parsing works | Rejects unexpected protocol bytes |
| Tests only the clean case | Injects banners, exceptions, blanks, NULs, and size violations |
| Merges logs and answers | Captures streams independently |
| Uses exit code as the verdict | Scores transport, schema, meaning, and side effects separately |
| Loads arbitrary commands from input | Passes an already trusted handler |
| Calls a unit test a benchmark pass | Claims only the property actually verified |

## The five-stage pattern

1. **Admit:** read one bounded request; reject invalid input before invocation.
2. **Isolate:** capture `stdout` and `stderr` independently.
3. **Invoke:** call only a trusted, predefined handler.
4. **Validate:** reject channel contamination, invalid return types, blanks, NULs, oversize responses, and exceptions.
5. **Emit:** write only the validated answer to `stdout`; write diagnostics to `stderr`; on failure, return non-zero with no answer bytes.

The critical invariant is: **failure produces no protocol answer**.

## Immediate applications

- **Coding-agent evaluation:** prevent build logs from being counted as the delivered answer.
- **MCP servers:** keep JSON-RPC on `stdout` and diagnostics on `stderr`.
- **Research exports:** separate provenance warnings from structured rows.
- **Sales operations:** ensure lead-scoring jobs emit only the agreed record schema.
- **Automation:** make piped commands deterministic and safe to parse.

## Tool/Plugin Opportunity

**Options:** GitHub, Python's built-in process/stream primitives, and the MCP Inspector.

**Unlocks:** versioned contracts and negative controls, independent stream capture, and realistic MCP transport testing.

**Setup:** GitHub requires a repository connection. Python adds no paid dependency. The Inspector requires a local Node.js environment and is optional until the adapter is a true MCP server.

**Concrete use case:** wrap a fictional support agent's one-shot benchmark handler, inject a startup `print()`, and require zero answer bytes plus a non-zero exit status.

## Practice reps

### Rep 1 — Classify every byte

Take a command that emits an answer, startup line, timing, and an error. Assign each item to request, answer, diagnostic, or failure signal.

**Pass:** there is no miscellaneous-output category.

### Rep 2 — Prove the negative control

Wrap an echo handler. Verify a clean exact response, then add `print("starting")` inside the handler.

**Pass:** the noisy run fails closed, emits nothing on `stdout`, and reports a sanitized diagnostic on `stderr`. The wrapper must not take the last line.

### Rep 3 — Benchmark capstone

Connect the harness to an isolated fictional agent and run one exact-output probe plus one ambiguity probe. Record request bytes, answer bytes, diagnostics, exit status, version, and prohibited side effects.

**Pass:** protocol purity and semantic correctness are scored separately; production remains unchanged.

## Retention check

- From **Schema-First Agent Design**, define the response contract before execution.
- From **Metamorphic Testing**, verify that changing log level cannot change answer bytes.
- From **Agent Trace Conformance Testing**, prove the real handler path executed.

A schema-valid object preceded by one banner line is still an invalid protocol transcript.

## Daily challenge

Take one command whose output another program consumes. Capture its output streams separately, inject a startup print, and make the test pass only when the harness rejects the run with **zero answer-channel bytes**.

## Implementation safety

Use an already trusted handler. Do not let prompt text select shell commands or import arbitrary code. Keep identity, authorization, tool access, content evaluation, and business eligibility outside this narrow transport boundary. Start in a dry-run or test-only path; require review and evidence before production mutation.

## Learning ledger

| Date | Skill | Practice | Evidence needed | Next step |
| --- | --- | --- | --- | --- |
| 2026-11-24 | Protocol-Pure Agent Harnesses | PENDING | Clean run plus contamination negative control with captured streams and exit status | Run Rep 2 on a local fictional handler |

**Sequence:** #31 Leakage-Proof As-Of Evaluation → **#32 Protocol-Pure Agent Harnesses**.
