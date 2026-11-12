#!/usr/bin/env python3
"""Compare FrameCut with the editing and caption files of a Creative Studio checkout, file by file.

python3 tools/compare_studio.py /path/to/framecore-works-creative-studio [--json out.json]
Prints counts of identical, adapted (path or wording edits) and missing files.
"""
import argparse, hashlib, json, sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1] / 'plugins/framecut'
MAP = [('skills/opencut-video-studio/SKILL.md', 'skills/framecut/SKILL.md'),
       ('skills/opencut-video-studio/', 'skills/framecut/'),
       ('skills/caption-studio/SKILL.md', 'skills/framecut/captions/CAPTIONS.md'),
       ('skills/caption-studio/agents/openai.yaml', None),
       ('skills/caption-studio/assets/captions/', 'skills/framecut/assets/captions/'),
       ('skills/caption-studio/', 'skills/framecut/'),
       ('tests/', 'tests/')]
TESTS = {'captions_test.py', 'edit_export_test.py', 'fixtures/voice-over.srt', 'fixtures/motion-score.json'}


def target(rel):
    for src, dst in MAP:
        if rel == src or (src.endswith('/') and rel.startswith(src)):
            return None if dst is None else (dst if not src.endswith('/') else dst + rel[len(src):])
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('studio', type=Path)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    package = args.studio / 'plugins/framecore-work-creative-studio'
    sources = [p for d in ('skills/opencut-video-studio', 'skills/caption-studio') for p in (package / d).rglob('*') if p.is_file()]
    sources += [package / 'tests' / t for t in TESTS] + sorted((package / 'tests').glob('framecut*_test.py'))
    rows = []
    for path in sorted(sources):
        rel = path.relative_to(package).as_posix()
        dst = target(rel)
        if dst is None:
            rows.append({'studio': rel, 'framecut': None, 'status': 'replaced', 'note': 'replaced by FrameCut\'s own agents/openai.yaml'})
            continue
        mine = PLUGIN / dst
        if not mine.exists():
            rows.append({'studio': rel, 'framecut': dst, 'status': 'missing'})
            continue
        same = hashlib.sha256(path.read_bytes()).digest() == hashlib.sha256(mine.read_bytes()).digest()
        rows.append({'studio': rel, 'framecut': dst, 'status': 'identical' if same else 'adapted'})
    counts = {s: sum(r['status'] == s for r in rows) for s in ('identical', 'adapted', 'replaced', 'missing')}
    print(json.dumps({'studio_files': len(rows), **counts}))
    for r in rows:
        if r['status'] != 'identical':
            print(f"{r['status']:9} {r['studio']} -> {r['framecut']}")
    if args.json:
        args.json.write_text(json.dumps({'counts': counts, 'files': rows}, indent=1) + '\n')
    return 1 if counts['missing'] else 0


if __name__ == '__main__':
    sys.exit(main())
