# Installation and implementation instructions

## 1. Copy safely

Fork or download this public repository. If your answers or projects are private, create a **private** learner workspace rather than placing personal notes in a public fork. Do not place access tokens in commands, Markdown, issue comments or commits.

## 2. Requirements

- Python 3.10+ for the local interview and curriculum verification, with no third-party dependency.
- Git, optionally, for retaining lesson branches and tracked changes.
- An AI assistant of your choice for the educational lesson and any optional coding help.
- A separate scheduled-task feature if you want recurring runs. The repository itself does not run a background agent.
- Optional GitHub connection and project-specific tools, only after you authorize them in that product.

## 3. Run the guided interview

```bash
python3 scripts/interview.py
```

It creates `.local/profile.json`, `.local/learning-plan.md`, and `.local/automation-prompt.md`. The `.local/` directory is ignored by Git. The interview does not call any external service or send your answers anywhere. The profile may still contain sensitive information, so protect the device and do not upload it as an attachment to a public issue.

If you prefer conversational setup, copy [the interview guide](INTERVIEW.md) into your assistant. The interview is optional; conservative defaults work for a first session.

## 4. Take the first lesson

Start with [Skill #1](../lessons/001-shadow-mode-and-promotion-gates/lesson.md) or ask your assistant to select a topic based on your goals. Practice with fictional examples first. Retain the verified outcomes privately.

## 5. Optional recurring delivery

Paste `.local/automation-prompt.md` into a recurring task in an assistant **that supports scheduling**. Set the recurrence yourself and confirm the task exists. If recurring tasks are unavailable, use the same prompt manually each session. Never claim automation is active because a file was generated.

## 6. Optional project application (Track B)

By default, application is **dry-run only**. You can allow bounded work in your own project by specifying: exact project/repository, allowed write operations, branch policy, test requirements, release permissions, spending ceiling, external communications policy and actions requiring a human confirmation. Run the existing test suite and compare the known baseline before changing anything. Record all actual commits and remote readbacks in your private records, not this public repository.

## 7. Maintain a public curriculum safely

Each general-purpose skill can be maintained on `skill/NNN-title` and integrated into `main` after content and privacy checks. Learner-specific examples must remain in private repos. Do not mirror full private Git histories. Check external-source licensing before redistributing any third-party material.

## 8. What success looks like

A dated lesson, 2–4 exercises, a retention prompt, one testable challenge, an accurate application receipt, no unauthorized side effects, and a clear next step. Unverified outcomes stay unverified.
