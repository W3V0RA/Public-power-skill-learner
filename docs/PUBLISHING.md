# Publishing the independent public repository

The target name is `public-power-skill-learner`, visibility PUBLIC. Before pushing, confirm you own the target repository and the GitHub connection can write it. The importer must not create another repository or force-push an existing one. If the remote has commits, stop and reconcile rather than overwriting. Check all branches and Git history for private source objects, paths, messages, or data before publication.

1. Review every file and run `python3 scripts/validate_public.py` plus `python3 -m unittest discover -s tests -v`.
2. Verify separate public Git root; this history must not share private Git object ancestry.
3. Publish `main` and every retained `skill/NNN-slug` branch to the empty PUBLIC target.
4. Read back exact remote branch names, HEAD SHAs, lesson paths and content digests.
5. Report the public update as `NOT SYNCED` until those readbacks succeed.

The public MIT license applies to original reusable content committed here only, not to external proprietary or personal material. Changes to paid accounts, scheduling, deployments, outreach, or a learner's private project always require that learner's authorization.
