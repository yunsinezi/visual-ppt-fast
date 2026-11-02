#!/usr/bin/env python3
"""Validate style-before-branch declaration only; not proof of actual image generation."""
import argparse
import json
import re
from pathlib import Path

STAGES = ('brief', 'style_generate', 'style_await_selection', 'route', 'make_A', 'make_B', 'qa', 'delivered')
STYLE_PATTERN = re.compile(r'^previews/style-0[1-8]\.png$')


def validate(data):
    stage = data.get('stage')
    if stage not in STAGES:
        return ['invalid stage']
    errors = []
    if stage in STAGES[2:]:
        paths = data.get('preview_images')
        if not isinstance(paths, list) or len(paths) != 8 or len(set(paths)) != 8 or any(not isinstance(p, str) or not STYLE_PATTERN.fullmatch(p) for p in paths):
            errors.append('requires 8 distinct numbered style previews')
        if not data.get('representative_slide_id') or not data.get('preview_slide_copy') or not data.get('aspect_ratio'):
            errors.append('shared representative slide content required')
        if data.get('previews_displayed') is not True:
            errors.append('previews must be displayed before route')
    if stage in STAGES[:3] and data.get('branch') in ('A', 'B'):
        errors.append('A/B cannot be selected before style gate')
    if stage in STAGES[3:] and data.get('selected_style') not in range(1,9):
        errors.append('selected_style 1..8 required before route')
    if stage in STAGES[4:]:
        if data.get('branch') not in ('A','B'):
            errors.append('branch A or B is required')
        if stage == 'make_A' and data.get('branch') != 'A':
            errors.append('make_A requires A')
        if stage == 'make_B' and data.get('branch') != 'B':
            errors.append('make_B requires B')
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('manifest')
    args = ap.parse_args()
    data = json.loads(Path(args.manifest).read_text(encoding='utf8'))
    errors = validate(data)
    if errors:
        print('\n'.join('FAIL: '+err for err in errors))
        return 1
    print('PASS: structural style-first declarations (visuals not verified)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
