#!/usr/bin/env python3
"""Local onboarding interview. No network, no external services, no third-party dependencies."""
from __future__ import annotations
import json
from pathlib import Path

QUESTIONS = [
 ('goal','What outcome would you like to improve in the next 30-90 days?', 'Learn one useful AI workflow'),
 ('project','What project can be used for safe practice (fictional name is fine)?', 'Fictional sandbox'),
 ('experience','Experience with AI, coding, and data (beginner/intermediate/advanced)?', 'beginner'),
 ('domain','What kind of work or hobby are you improving?', 'general productivity'),
 ('tools','What tools do you already have?', 'an AI assistant and text editor'),
 ('session_minutes','Minutes available for each lesson (15/30/45/60)?', '30'),
 ('cadence','Preferred cadence (manual/daily/every_other_day/weekly)?', 'manual'),
 ('budget','Budget (free_only/existing_tools/capped with separate approval)?', 'free_only'),
 ('application_mode','Application mode (dry_run/drafts/authorized_project_writes)?', 'dry_run'),
 ('privacy_rule','Any material that should never leave your environment?', 'synthetic content only'),
 ('success_metric','How will you measure a real improvement?', 'fewer verified errors'),
 ('retention_method','Preferred retention (quiz/debug/build/capstone)?', 'short quizzes and practical builds'),
]


def normalized(raw: dict) -> dict:
    defaults = {k:d for k,_,d in QUESTIONS}
    result = {k: str(raw.get(k, d)).strip() or d for k,d in defaults.items()}
    if result['experience'] not in ('beginner','intermediate','advanced'):
        result['experience']='beginner'
    if result['application_mode'] not in ('dry_run','drafts','authorized_project_writes'):
        result['application_mode']='dry_run'
    # Guided setup is not permission to write external systems.
    if result['application_mode']=='authorized_project_writes':
        result['application_mode']='dry_run'
        result['permission_notice']='Project-specific authorization is still required before enabling writes.'
    try: minutes=int(result['session_minutes'])
    except ValueError: minutes=30
    result['session_minutes']=max(10,min(minutes,90))
    result['profile_version']=1
    return result


def make_plan(p:dict)->str:
    return f"""# Your private Power Skill learning plan

Goal: {p['goal']}
Practice project: {p['project']}
Experience: {p['experience']}
Domain: {p['domain']}
Tools: {p['tools']}
Time: {p['session_minutes']} minutes; cadence: {p['cadence']}
Budget: {p['budget']}
Application mode: {p['application_mode']} (external writes require additional explicit authorization)
Privacy: {p['privacy_rule']}
Outcome measure: {p['success_metric']}
Retention preference: {p['retention_method']}

## First learning loop

1. Choose one advanced capability that directly addresses the goal and fits the time budget.
2. Teach the concept using fictional data, then work through 2-4 increasing-difficulty reps.
3. Create one reversible or simulated artifact, record its baseline and test results.
4. Return VERIFIED, FAILED or UNVERIFIED with one concrete next step.

No background task, account connection, external write, or paid usage is activated by this plan.
"""


def make_task_prompt(p:dict)->str:
    return ('Teach me one advanced AI skill per session. Customize it to this private context: '
            f'Goal: {p["goal"]}; project: {p["project"]}; background: {p["experience"]}; '
            f'tools: {p["tools"]}; time: {p["session_minutes"]} minutes; '
            f'privacy: {p["privacy_rule"]}; success measure: {p["success_metric"]}. '
            'Include a clear explanation, non-obvious insight, real project application, optional tool opportunity, '
            '2-4 practice reps, retention check and one testable challenge. '
            'Stay in dry-run mode until I explicitly authorize an exact project and write scope. '
            'Never claim tool calls, external updates, scheduling or business outcomes without independent evidence.\n')


def main():
    print('Public Power Skill Learner: private, local onboarding (press Enter to use the default).')
    answers = {}
    for key,question,default in QUESTIONS:
        try: value=input(f'{question}\n  [{default}]: ')
        except EOFError: value=''
        answers[key]=value or default
    p=normalized(answers)
    root=Path(__file__).resolve().parents[1]
    out=root/'.local';out.mkdir(exist_ok=True)
    (out/'profile.json').write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8')
    (out/'learning-plan.md').write_text(make_plan(p),encoding='utf-8')
    (out/'automation-prompt.md').write_text(make_task_prompt(p),encoding='utf-8')
    print('Created .local/profile.json, .local/learning-plan.md and .local/automation-prompt.md')
    print('No network call, scheduled task, or project write was performed.')

if __name__=='__main__':main()
