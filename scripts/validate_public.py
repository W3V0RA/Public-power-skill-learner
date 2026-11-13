#!/usr/bin/env python3
"""Structural and generic leakage heuristics for this public educational repository."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors=[]
    cat=json.loads((ROOT/'catalog.json').read_text())
    rows=cat.get('lessons',[])
    if cat.get('visibility_intent') != 'public': errors.append('not declared public')
    if [r.get('number') for r in rows] != list(range(1,27)):
        errors.append('expected contiguous public lessons #1-#26')
    if len({r.get('branch') for r in rows}) != len(rows):
        errors.append('duplicate branches')
    forbidden_patterns=[
      (r'-----BEGIN (?:RSA|OPENSSH|EC|PRIVATE) KEY-----','private key'),
      (r'gh[pousr]_[A-Za-z0-9]{20,}','GitHub token-like value'),
      (r'sk-[A-Za-z0-9]{20,}','secret key-like value'),
      (r'(?i)(password|api[_ -]?key|access[_ -]?token)\s*[:=]\s*["\']?[A-Za-z0-9_+./=-]{18,}','credential-like assignment'),
      (r'\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b','email address in instructional material'),
    ]
    for r in rows:
        if not re.fullmatch(r'skill/\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*',r.get('branch','')):
            errors.append(f'bad branch in skill {r.get("number")}')
        rel=Path(r.get('path',''))
        if rel.is_absolute() or '..' in rel.parts or rel.parts[0]!='lessons':
            errors.append(f'unsafe lesson path {rel}');continue
        f=ROOT/rel
        if not f.is_file(): errors.append(f'missing lesson {rel}');continue
        txt=f.read_text(encoding='utf-8')
        if len(txt.split())<250:errors.append(f'lesson too brief {rel}')
        if 'Practice reps' not in txt or 'Retention check' not in txt or 'Daily challenge' not in txt:
            errors.append(f'incomplete lesson structure {rel}')
        if r.get('sha256')!=__import__('hashlib').sha256(f.read_bytes()).hexdigest():
            errors.append(f'digest mismatch {rel}')
    tracked = ['README.md','SKILL.md','AGENTS.md','CONTRIBUTING.md','docs/IMPLEMENTATION.md','docs/INTERVIEW.md','docs/PRIVACY_AND_SAFETY.md','templates/automation-prompt.md','templates/learning-plan.md']
    tracked += [r['path'] for r in rows]
    for path in tracked:
        data=(ROOT/path).read_text(encoding='utf-8')
        for pat,label in forbidden_patterns:
            if re.search(pat,data):errors.append(f'{path}: potential {label}')
    return errors

if __name__=='__main__':
    problems=validate()
    if problems:
        print('FAIL: '+ '\n'.join(problems));sys.exit(1)
    print('PASS: public structure and generic leakage heuristics. Manual privacy review is still required.')
