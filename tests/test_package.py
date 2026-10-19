import unittest,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class Package(unittest.TestCase):
 def test_entry(self):
  s=(R/'SKILL.md').read_text('utf8');self.assertIn('name: thinking-collaboration',s);self.assertIn('不固定问卷',s)
 def test_method_boundaries(self):
  s=(R/'references/methods.md').read_text('utf8');self.assertIn('目标收敛',s);self.assertIn('证据思维',s);self.assertIn('用户决定',s)
 def test_public_payload(self):
  self.assertFalse(any(x.suffix.lower() in ['.mp4','.m4a']for x in R.rglob('*')));self.assertEqual(json.loads((R/'manifest.json').read_text('utf8'))['version'],'1.0.0')
