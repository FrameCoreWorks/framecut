# Verification: FrameCut 0.1.0 (2026-11-12)

Separate evidence scopes. Nothing here is a ChatGPT Work, Codex or Claude app result.

| Scope | Result |
| --- | --- |
| Repository check (`python3 tools/check.py`) | PASS: manifests and marketplace identity, shared contract SHA-256 `e7cc0f4e…897a`, renderer and board copy hashes, every local Markdown link, no stale skill names, 8 Python test suites (captions, edit export, audit, development, editor, pixel, script, framecut) with FFmpeg built with libass and Pillow 12.3, reproducible archive |
| File comparison with Creative Studio `main` `bc3724ea` (1.178.1, `tools/compare_studio.py`) | 54 source files: 34 identical, 19 adapted (paths, names, standalone wording), 1 replaced (`agents/openai.yaml`, the captions guide has no skill of its own), 0 missing |
| `claude plugin validate --strict` (Claude Code 2.1.322) | PASS for `plugins/framecut` and the marketplace |
| Claude Code install from the local marketplace in an empty config | PASS: `framecut@framecut` 0.1.0 installed and enabled |
| Headless Claude Code, plugin loaded with `--plugin-dir`, read-only tools | 2 cases, 5 turns, about 23 s: (1) bare `/framecut:framecut` gave the two-line introduction and the first standalone-brief question in Polish; (2) a Polish request for a 30-second Instagram reel with captions from a 20-minute interview answered with the analysis, transcription, moments, storyboard-before-render and caption safe-zone order |
| fontTools missing-glyph check | NOT_RUN in the cloud container (fontTools not installed); CI installs it from `requirements-ci.txt` |
| ChatGPT Work, Codex, Claude apps | NOT_RUN |
| A rendered film from the installed plugin | NOT_RUN in this release; the edit, caption and render code paths are covered by the test suites |
