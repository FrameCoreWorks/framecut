#!/usr/bin/env python3
"""Validate the FrameCut repository and run its test suites.

--fast runs only the quick suites (captions, editor export, editor, pixel); a release runs the full check.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zipfile

from package import ROOT, PLUGIN, build, source_files

CONTRACT_SHA = 'e7cc0f4e612395768e8c8c6cf2a033a555bc69b4c8ea5ca45c4db019a342897a'
STUDIO_SKILLS = ('opencut-video-studio', 'caption-studio', 'hyperframes-workflow', 'remotion-video-production')
FAST = ('captions_test.py', 'edit_export_test.py', 'framecut_editor_test.py', 'framecut_pixel_test.py')
COPIES = ('skills/framecut/assets/captions/render.py', 'skills/framecut/assets/board/board_compose.py')
# Descriptions present FrameCut as a standalone plugin (owner decision 2026-11-12).
NOT_IN_DESCRIPTIONS = re.compile(r'moved (out )?(of|from)|former(ly)? (a )?(module|part)|extracted from|split (out )?from', re.I)


def require(condition, message):
    if not condition:
        raise SystemExit(f'FAIL: {message}')


def frontmatter(text):
    require(text.startswith('---\n'), 'SKILL.md needs frontmatter')
    block = text.split('---', 2)[1]
    return dict(re.findall(r'^(\w+): ?"?(.*?)"?$', block, re.M))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fast', action='store_true')
    fast = parser.parse_args().fast
    files = source_files()
    for name, content in files.items():
        if name.endswith('.json'):
            json.loads(content)
    manifests = [json.loads(files[p]) for p in ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json')]
    version = manifests[0]['version']
    require(all(m['version'] == version and m['name'] == 'framecut' for m in manifests), 'Manifest identity differs')
    require(re.fullmatch(r'\d+\.\d+\.\d+', version), 'Expected release SemVer')
    require(manifests[0]['extensions']['com.openai']['interface'] == manifests[1]['interface'], 'Portable and Codex presentation differ')
    market = json.loads((ROOT / '.claude-plugin/marketplace.json').read_text())
    require(market['name'] == 'framecut' and len(market['plugins']) == 1, 'Marketplace must hold only FrameCut')
    entry = market['plugins'][0]
    require(entry['name'] == 'framecut' and entry['version'] == version, 'Marketplace identity differs')
    require((ROOT / entry['source']).resolve() == PLUGIN, 'Marketplace points outside the plugin')
    caps = json.loads(files['capabilities.json'])
    require(caps['plugin'] == {'name': 'framecut', 'version': version}, 'capabilities.json identity differs')
    require(hashlib.sha256(files['contracts/framecore-task.schema.json']).hexdigest() == CONTRACT_SHA == caps['contract_schema']['sha256'],
            'Shared contract schema drifted from Studio, FrameMotion, Toolbox and Open Assets')
    skills = sorted(p for p in files if p.endswith('/SKILL.md') and p.startswith('skills/'))
    require(skills == ['skills/framecut/SKILL.md'], f'Exactly one skill expected, found {skills}')
    meta = frontmatter(files['skills/framecut/SKILL.md'].decode())
    require(meta.get('name') == 'framecut' and meta.get('description'), 'Invalid skill metadata')
    agent = files['skills/framecut/agents/openai.yaml'].decode()
    short = re.search(r'short_description: "(.+)"', agent).group(1)
    require('display_name: "FrameCut"' in agent and 25 <= len(short) <= 64, 'Skill interface metadata')
    descriptions = [meta['description'], entry['description'], *(m['description'] for m in manifests),
                    manifests[1]['interface']['longDescription'], market['description']]
    require(not any(NOT_IN_DESCRIPTIONS.search(d) for d in descriptions), 'A description presents FrameCut as taken out of another plugin')
    for copy in COPIES:
        readme = (PLUGIN / copy).parent / 'README.md'
        recorded = re.findall(r'`([0-9a-f]{64})`', readme.read_text())
        require(len(recorded) >= 2 and hashlib.sha256(files[copy]).hexdigest() == recorded[-1], f'{copy} differs from its recorded hash')
    for path in [*ROOT.glob('*.md'), *ROOT.glob('docs/*.md'), *PLUGIN.rglob('*.md')]:
        text = path.read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)\s]+)\)', text):
            if '://' in link or link.startswith(('#', 'mailto:')):
                continue
            require((path.parent / link.split('#')[0]).exists(), f'Broken local link: {path.relative_to(ROOT)}: {link}')
    for name, content in files.items():
        if name.endswith(('.md', '.py', '.json', '.yaml')) and name not in ('CHANGELOG.md', 'NOTICE', *(str(Path(c).parent / 'README.md') for c in COPIES)):
            text = content.decode('utf-8', 'replace')
            for old in STUDIO_SKILLS:
                require(old not in text, f'Old Studio skill name {old} in {name}')
    print(f'Source: {len(files)} files, version {version}', flush=True)
    for test in sorted((PLUGIN / 'tests').glob('*_test.py')):
        if fast and test.name not in FAST:
            continue
        subprocess.run([sys.executable, str(test)], cwd=PLUGIN, check=True, capture_output=True)
        print(f'PASS {test.name}', flush=True)
    with tempfile.TemporaryDirectory() as temp:
        one, two = build(Path(temp) / 'one'), build(Path(temp) / 'two')
        require(one.read_bytes() == two.read_bytes(), 'Archive is not reproducible')
        with zipfile.ZipFile(one) as archive:
            names = archive.namelist()
        require('plugin.json' in names and 'skills/framecut/SKILL.md' in names, 'Archive root files missing')
    print('PASS: manifests, contract, copies, links, tests and reproducible archive' + (' (fast subset)' if fast else ''))


if __name__ == '__main__':
    main()
