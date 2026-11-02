#!/usr/bin/env python3
"""Fast structural inspection of a delivered PPTX. Not a visual or playback test."""
import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

SLIDE_RE = re.compile(r"^ppt/slides/slide([0-9]+)\.xml$")
DRAWING_TAGS = {
    "{http://schemas.openxmlformats.org/presentationml/2006/main}sp",
    "{http://schemas.openxmlformats.org/presentationml/2006/main}pic",
    "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame",
    "{http://schemas.openxmlformats.org/presentationml/2006/main}grpSp",
    "{http://schemas.openxmlformats.org/presentationml/2006/main}cxnSp",
}


def inspect_pptx(path, expected=None):
    path = Path(path)
    errors = []
    if not path.is_file() or path.stat().st_size == 0:
        return ["PPTX does not exist or is empty"]
    try:
        with zipfile.ZipFile(path) as zf:
            if zf.testzip() is not None:
                errors.append("PPTX ZIP contains a corrupt member")
            names = zf.namelist()
            if "ppt/presentation.xml" not in names or "[Content_Types].xml" not in names:
                errors.append("Not a valid PPTX package: missing presentation metadata")
            slides = sorted((int(m.group(1)), n) for n in names if (m := SLIDE_RE.match(n)))
            if not slides:
                errors.append("PPTX has no slide XML files")
            if expected is not None and len(slides) != expected:
                errors.append(f"Expected {expected} slides, found {len(slides)}")
            for index, member in slides:
                try:
                    root = ET.fromstring(zf.read(member))
                    shapes = [node for node in root.iter() if node.tag in DRAWING_TAGS]
                    if not shapes:
                        errors.append(f"Slide {index} appears to have no drawing objects")
                except ET.ParseError:
                    errors.append(f"Slide {index} has invalid XML")
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(f"Cannot read PPTX: {exc}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", help="PPTX path")
    parser.add_argument("--expected", type=int, help="Expected number of slides")
    args = parser.parse_args()
    errors = inspect_pptx(args.pptx, args.expected)
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        return 1
    print("PASS: readable PPTX structure and expected nonempty slide count; visual QA not tested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
