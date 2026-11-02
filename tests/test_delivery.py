import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_delivery.py"
spec = importlib.util.spec_from_file_location("check_delivery", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class DeliveryTests(unittest.TestCase):
    def make_pptx(self, path, slide_xml):
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("[Content_Types].xml", "<Types/>")
            zf.writestr("ppt/presentation.xml", "<p:presentation xmlns:p='http://schemas.openxmlformats.org/presentationml/2006/main'/>")
            for index, xml in enumerate(slide_xml, 1):
                zf.writestr(f"ppt/slides/slide{index}.xml", xml)

    def test_valid_slide_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "a.pptx"
            self.make_pptx(path, ["<p:sld xmlns:p='http://schemas.openxmlformats.org/presentationml/2006/main'><p:sp/></p:sld>"])
            self.assertEqual(mod.inspect_pptx(path, 1), [])

    def test_missing_slide_and_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "a.pptx"
            self.make_pptx(path, ["<p:sld xmlns:p='http://schemas.openxmlformats.org/presentationml/2006/main'/>"])
            result = mod.inspect_pptx(path, 2)
            self.assertTrue(any("Expected 2" in x for x in result))
            self.assertTrue(any("no drawing" in x for x in result))

    def test_missing_file(self):
        self.assertTrue(mod.inspect_pptx('/unreachable/file.pptx'))


if __name__ == '__main__':
    unittest.main()
