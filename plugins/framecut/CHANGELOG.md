# Changelog

## 0.1.0 (2026-11-12)

First release of FrameCut, a complete standalone video editing plugin, which Creative Studio can also use as its editing companion.

- One skill, `framecut`: interview and standalone brief, media analysis, draft transcription and script alignment, typed edit operations on one versioned project, full storyboard before the final render, review records and delivery readiness.
- Edit engine `framecut.py` with 14 modules: cuts, crossfades and dips, speed and freeze frames, J/L cuts, per-format framing, keyframes, 13 versioned picture and audio effects, word-timed captions, music ducked under speech, loudness targets, long renders as resumable jobs.
- Captions and subtitles method (`captions/CAPTIONS.md`) with readability defaults, platform caption specs, talking-head formats and the `captions.py` tool (check, convert, build, contract import, burn-in).
- Editor craft, editor handoff (EDL, OTIO, CSV, relink map), moment roles and clips, data-led feedback.
- First setup: tool check (Python, Pillow, FFmpeg with libass, PyWhisperCpp and the pinned Whisper tiny model, optional OpenTimelineIO) and one numbered question offering FrameMotion, Toolbox (Earshot, shader transitions), Open Assets and Creative Studio; nothing is installed without the user's pick.
- Bundled fonts (OFL), its own board composer and caption renderer, so FrameCut needs no other plugin.
- Shared `framecore-task-result/1` contract schema, byte-identical with Studio, FrameMotion, Toolbox and Open Assets.
- Tests: 8 suites (engine, editor, development commands, pixel effects, scripted edits, audit, editor export, captions).
