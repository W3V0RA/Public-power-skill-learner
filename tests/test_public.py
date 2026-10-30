import importlib.util
import pathlib
import tempfile
import unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('public_validator',ROOT/'scripts/validate_public.py')
v=importlib.util.module_from_spec(sp);sp.loader.exec_module(v)
si=importlib.util.spec_from_file_location('interview',ROOT/'scripts/interview.py')
i=importlib.util.module_from_spec(si);si.loader.exec_module(i)

class PublicTests(unittest.TestCase):
    def test_catalog_and_safety(self):
        self.assertEqual(v.validate(),[])
    def test_interview_defaults_to_dry_run(self):
        self.assertEqual(i.normalized({'application_mode':'authorized_project_writes'})['application_mode'],'dry_run')
    def test_interview_unrecognized_permission_fails_closed(self):
        self.assertEqual(i.normalized({'application_mode':'auto_write_everything'})['application_mode'],'dry_run')
    def test_interview_generates_private_plan(self):
        p=i.normalized({'goal':'Improve a fictional workflow','project':'Sample sandbox'})
        self.assertIn('No background task',i.make_plan(p))
        self.assertIn('dry-run mode',i.make_task_prompt(p))
    def test_profile_is_gitignored(self):
        self.assertIn('.local/',(ROOT/'.gitignore').read_text())
    def test_independent_public_origin(self):
        import json
        c=json.loads((ROOT/'catalog.json').read_text())
        self.assertEqual(c['origin'],'independent_generic_public_edition')
    def test_original_public_license_exists(self):
        self.assertTrue((ROOT/'LICENSE').read_text().startswith('MIT License'))

if __name__=='__main__':unittest.main()
