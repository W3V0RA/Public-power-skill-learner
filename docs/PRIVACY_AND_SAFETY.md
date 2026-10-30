# Public publishing and authorization policy

## Separation by design

This public Git repository has its own root and history. It contains independently written instructional content and invented scenarios only. **Never merge, rebase, cherry-pick, or import raw objects from anyone's private repository.** Public examples must not contain client data, financial figures tied to a real person or business, addresses, email addresses, phone numbers, private domain names, production URLs, source commits, proprietary architecture, security findings, private project names or private task instructions.

Public lessons share **topic and sequence** with an associated private learner only when explicitly authorized; private personal context, Git links, change receipts and user history must not cross the boundary.

## Safe publication checklist

1. Rewrite the lesson in a neutral way, not a simple find-and-replace of names.
2. Confirm all example entities, email addresses, source code and numbers are fictional or independently permitted for publication.
3. Confirm the Git commit message, branch name, workflow logs and file metadata reveal no private content.
4. Run `python3 scripts/validate_public.py` and `python3 -m unittest discover -s tests -v`.
5. Review the diff and the entire reachable branch history; a removed secret in a newer commit may still exist in earlier objects.
6. If uncertain, mark the public update `BLOCKED` and continue only in private.

The included tests are an initial lint gate. They cannot guarantee all sensitive or proprietary material is detected. Do not put private names into a public denylist file because that would expose them.

## Permission and budget rules

- All external writes require the individual learner's explicit project-level authorization and must respect service confirmation prompts.
- No outreach, purchases, account creation, deployment, permission or credential changes, or destructive operations based on a generic tutorial.
- No automatic raw mirroring of private files into GitHub.
- Do not claim a project improved because an agent generated a patch or completed mock tests.
- Do not connect a new provider or start paid usage without consent.

## Failure states

Use `VERIFIED`, `FAILED`, `UNVERIFIED`, `BLOCKED`, or `PENDING` accurately. If public writeback fails, keep an artifact privately and clearly label it NOT SYNCED rather than claiming publication.
