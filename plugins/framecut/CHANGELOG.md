# Changelog

## 0.1.4 (2026-11-17)

- **Earshot through FrameMotion** (owner approval 2026-11-17 after the FrameMotion, Studio and FrameCut cooperation test of 2026-11-17): FrameMotion 0.3.0 bundles Earshot, but FrameCut said Earshot came only through Toolbox, so with FrameCut and FrameMotion and no Toolbox the sound work fell back to FrameCut's own mix. `SKILL.md` and the companion reference now use FrameMotion's bundled copy when Toolbox is absent; both copies share one engine in `~/.framecore-works/earshot`.
- **Motion return formats**: the FrameMotion section asks for straight alpha as ProRes 4444 in a .mov and opaque pieces as H.264, because FrameCut reads no VP9 alpha (seen in the test: a VP9 WebM with alpha was ingested with `has_alpha: false`).

## 0.1.3 (2026-11-14)

- **Fixed welcome on a bare invocation** (owner request and approval 2026-11-14): `skills/framecut/assets/startup-welcome.en.md` holds the approved English text (what FrameCut does, six capabilities, storyboard approval before the final render, three numbered examples, closing question; no link to another plugin). `SKILL.md` embeds the same text in a "Welcome" section: output it alone, copied exactly in English or translated in full, then ask the first missing standalone-brief question after the answer. `tests/welcome_test.py` checks the embedded copy is byte-identical to the asset.

## 0.1.2 (2026-11-13)

- **Captions readable on a phone** (owner test 2026-11-13): the renderer keeps captions at least 4.5 % of the frame height in a vertical film and 4 % in a landscape one, and reports `caption_size_raised` when a sequence asked for less; the readability reference says to shorten or split a cue instead of shrinking it.
- **Whisper base for non-English speech**: first setup offers the pinned multilingual base model (SHA-256 recorded) next to tiny, because tiny garbles Polish words and word times.

## 0.1.1 (2026-11-13)

- **Music for reels and social films** (owner decision 2026-11-13): a bed composed in code comes first, because platforms mute or claim library music even under CC BY; the user is warned before someone else's track is used; about -14 LUFS with the peak below -1 dB.
- Installation guide: FrameCut's only marketplace is `framecut`; Creative Studio 1.180.0 installs it from there as a dependency; how to replace an older `framecut@framecore-works` copy. The Studio install route says which marketplaces to add first.
- The readable hold rule is credited to FrameMotion's motion craft, not to Studio.
- Repository check prints the end of a failing test's output.

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
