# Public Power Skill Learner 🧠

A free, copyable, **general-purpose** way to learn one advanced Artificial Intelligence (AI) skill at a time, practice it on a project you choose, and track verified progress. Designed to adapt to your goals instead of assuming a particular job, business, or technology stack.

**This repository is a public educational edition, not a mirror of any learner's personal projects.** Its lessons and scenarios use fictional examples. No external systems are contacted during setup.

## Quick start (five minutes)

1. Fork this repository into your own GitHub account, or download its source code. To keep your personal learning records confidential, create a **private fork or separate private copy** if your platform supports it.
2. Install Python 3.10 or later. No paid AI subscription or extra Python package is needed to run the interview and local checks.
3. Run `python3 scripts/interview.py` and answer the onboarding questions. Press Enter to skip a question; the tool makes conservative defaults.
4. Open your generated `.local/learning-plan.md` and `.local/automation-prompt.md` (never commit `.local/`). Copy the latter into your preferred AI assistant and adapt it to the tool access you actually have.
5. Choose one skill from [the catalog](INDEX.md). Complete three practice reps, record evidence, and only mark a project action complete when checked against the expected outcome.
6. Optionally create a recurring task **in a service that actually supports scheduling**. GitHub alone does not schedule an AI assistant or grant access to your other accounts.

## What the learner does

**Track A: Learn.** One new, dated skill lesson with plain-language explanation, an advanced technique, optional tool opportunity, 2–4 increasing-difficulty exercises, a retention check, and a practical challenge.

**Track B: Apply.** Choose one authorized project. Inspect its baseline, propose the smallest useful change, test it in a safe environment, and record the result. **Never treat generating a plan or a green unit test as proof of business impact.**

Public repository updates contain only generic curriculum and safe examples. Personal projects, notes, outcomes, contacts, and credentials belong in your own private workspace.

## Direct links

- [Implementation instructions](docs/IMPLEMENTATION.md)
- [Interactive onboarding interview](docs/INTERVIEW.md)
- [Safe AI automation prompt](templates/automation-prompt.md)
- [Learning plan template](templates/learning-plan.md)
- [Curriculum and retained branches](INDEX.md)
- [Privacy, authorization and publication safeguards](docs/PRIVACY_AND_SAFETY.md)
- [Contributor guidance](CONTRIBUTING.md)
- [License](LICENSE), MIT for original reusable material here

## Local verification

```bash
python3 scripts/validate_public.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs the same checks when installed in a GitHub repository. These tests validate structure and common leak indicators, not the truth of all lesson content. Review all proposed public changes before publishing them.

## Branch convention

`main` is the searchable public curriculum. Every skill has a **retained** branch named `skill/NNN-topic-slug` for independent history and future experiments. Do not delete branches automatically. Public lesson adaptation is deliberately independent from any person's private history; never merge a private repo into this repo.

## Limitations

This project doesn't train or modify model weights, guarantee skill retention, run paid AI calls by itself, create recurring ChatGPT tasks, or have access to any of your accounts. Integrations and consequential operations require your separate authorization. Use fictional data by default. Where a safe action cannot be independently verified, record `PENDING` or `UNVERIFIED`.
