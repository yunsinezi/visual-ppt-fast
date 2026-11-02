import importlib.util
import unittest
from pathlib import Path

path = Path(__file__).resolve().parents[1] / 'scripts' / 'check_workflow.py'
spec = importlib.util.spec_from_file_location('check_workflow', path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def example(stage='style_await_selection'):
    return {'stage':stage,'preview_images':[f'previews/style-{i:02d}.png' for i in range(1,9)],'representative_slide_id':'slide-03','preview_slide_copy':'固定文案','aspect_ratio':'16:9','previews_displayed':True,'selected_style':None,'branch':None}


class FlowTests(unittest.TestCase):
    def test_style_gate_accepts_eight(self):
        self.assertEqual(mod.validate(example()), [])

    def test_branch_is_not_allowed_before_style(self):
        p=example('brief'); p['branch']='B'
        self.assertTrue(mod.validate(p))

    def test_route_blocks_incomplete_previews(self):
        p=example('route'); p['preview_images'].pop();p['selected_style']=2
        self.assertTrue(mod.validate(p))

    def test_route_requires_selected_style(self):
        self.assertTrue(mod.validate(example('route')))

    def test_route_valid_after_selection(self):
        p=example('route');p['selected_style']=3
        self.assertEqual(mod.validate(p), [])

    def test_make_b_after_style(self):
        p=example('make_B');p['selected_style']=5;p['branch']='B'
        self.assertEqual(mod.validate(p), [])

    def test_previews_must_be_displayed(self):
        p=example('route');p['previews_displayed']=False;p['selected_style']=1
        self.assertTrue(mod.validate(p))


if __name__ == '__main__':
    unittest.main()
