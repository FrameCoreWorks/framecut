# FrameCut

Video editing for **Claude, Codex and ChatGPT Work**, maintained by FrameCore Works. FrameCut turns your own footage into a finished, reviewed film: it asks what the film is for, analyses the material, transcribes speech, shows the whole film as a storyboard, then cuts, captions, mixes and renders it, and hands an editor EDL, OTIO and CSV files when you want to finish elsewhere.

**Current plugin version: 0.1.5.** FrameCut is a complete standalone plugin: it needs no other plugin, starts with its own short brief and takes a film from the footage to the delivered MP4 with subtitle files. It also works as the editing companion of [FrameCore Works Creative Studio](https://github.com/FrameCoreWorks/framecore-works-creative-studio) when both are installed: then Studio keeps the brief, idea, copy, board acceptance and delivery, and FrameCut does the analysis, edit, captions, mix, render and QA. Plugins complement each other through the shared `framecore-task-result/1` contract also used by FrameMotion, Toolbox and Open Assets.

## What it does

- **Highlights and clips** from a long recording, interview or podcast, each a complete thought with a hook.
- **Full edits** of footage, screen recordings, photos and mixed material, in several aspect ratios from one timeline.
- **Captions and subtitles**: word-timed captions burned in, SRT and VTT files, readability and platform safe-zone checks, translations as separate approved text.
- **Sound**: J/L cuts, music lowered under speech, loudness targets, and with Earshot (from Toolbox or FrameMotion), effects placed on the cuts.
- **Storyboard first**: the whole film as numbered contact sheets for your corrections before the final render.
- **Handoff**: EDL, OTIO and CSV shot lists for DaVinci Resolve, Premiere and other editors.

## Start here

- [Installation](INSTALL.md) for Claude Code, the Claude apps, Codex and ChatGPT Work
- [The skill](plugins/framecut/skills/framecut/SKILL.md), its [captions method](plugins/framecut/skills/framecut/captions/CAPTIONS.md) and [editor craft](plugins/framecut/skills/framecut/references/editor-craft.md)
- [Plugin changelog](plugins/framecut/CHANGELOG.md)
- [Development rules](AGENTS.md) and the latest [handover](docs/handover-2026-11-12.md)

## What it needs

No account and no API key. Without code execution FrameCut plans the edit, shows the storyboard and writes an Edit Pack for an editor. With Python 3.10+, Pillow and FFmpeg/FFprobe with libass it edits and renders. Speech-to-text uses PyWhisperCpp with the multilingual Whisper tiny model, installed for the conversation only after you agree. Nothing is uploaded.

## Licence

Apache-2.0. Bundled fonts keep their OFL licence; see [NOTICE](plugins/framecut/NOTICE).
