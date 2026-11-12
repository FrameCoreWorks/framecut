# FrameCut

Video editing from your own footage to a finished, reviewed film: interview, media analysis, draft transcription, cuts and highlights, captions and subtitles, music under speech, loudness, a full storyboard before the final render, and EDL, OTIO and CSV handoff to an editor.

FrameCut works on its own, with its own short brief, and as the editing companion of [FrameCore Works Creative Studio](https://github.com/FrameCoreWorks/framecore-works-creative-studio). With Studio, Studio keeps the brief, idea, copy, board acceptance and delivery; FrameCut does the analysis, edit, captions, mix, render and its QA.

- One skill: [`skills/framecut/SKILL.md`](skills/framecut/SKILL.md), with the [captions and subtitles method](skills/framecut/captions/CAPTIONS.md) and the [editor craft](skills/framecut/references/editor-craft.md).
- Edit engine: [`assets/framecut/`](skills/framecut/assets/framecut/README.md) (`framecut.py`, Python, Pillow and FFmpeg).
- Shared task contract with Studio, FrameMotion, Toolbox and Open Assets: [`contracts/framecore-task.schema.json`](contracts/framecore-task.schema.json).

Requirements depend on the host: without code execution FrameCut writes the edit plan, the storyboard and an Edit Pack for an editor; with Python 3.10+, Pillow and FFmpeg/FFprobe (libass) it edits and renders. Speech-to-text uses PyWhisperCpp with the multilingual Whisper tiny model, installed only after you agree. No account or API key is needed.

In Claude Code: `/plugin install framecut --marketplace FrameCoreWorks/framecut`. Other hosts: [INSTALL.md](https://github.com/FrameCoreWorks/framecut/blob/main/INSTALL.md).

Licence: Apache-2.0, third-party notices in [NOTICE](NOTICE). Changes: [CHANGELOG](CHANGELOG.md).
