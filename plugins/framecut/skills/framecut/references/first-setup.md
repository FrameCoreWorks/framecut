# First setup

FrameCut is complete on its own and needs no other plugin. Other FrameCore Works plugins can add to it; they are offered once, as a question, and installed only on the user's answer (owner decision 2026-11-12: the plugins stay standalone and complement each other when installed together; none requires another).

## When to run it

- In the conversation that installed FrameCut, as the installation guide's last step.
- When the user asks to configure FrameCut ("Configure FrameCut", in their language), or the host runs the plugin's setup action.
- Not on a bare invocation, a greeting or a direct task: those start the brief or the task. A direct task in the installing message is done first; setup is offered after it.
- **With Creative Studio**: when `framecore-work-creative-studio` is in the skill list and its own first setup runs in this conversation, Studio's setup already shows these plugins; skip step 3 here and say in one line that they are in Studio's list.

## Steps

The user is assumed to know nothing about plugins or terminals: say in one plain sentence what each step does, show no command unless asked, and report each result in one line.

1. **What can run here.** Say what FrameCut can do on this host: with no code execution, an edit plan, storyboard and editor handoff (Edit Pack); with code execution, the full edit and render. Where code runs, run `python3 assets/framecut/framecut.py capabilities` and report it in plain words.
2. **Tools for editing, one question if something is missing.** The edit needs Python 3.10+ with Pillow and FFmpeg/FFprobe with libass, libx264, AAC, `xfade` and `loudnorm` ([the tool table](#tools)). Speech-to-text needs PyWhisperCpp and the multilingual Whisper tiny model; for speech that is not English (Polish included) offer the base model in the same question, because tiny turns non-English words into near-misses and shifts word times by up to a second (owner test 2026-11-13); an editor's OTIO file needs OpenTimelineIO. When something is missing, list it in one message with what it is for and what will be written, and install only after the user's yes, into a folder of this conversation (`S=${TMPDIR:-/tmp}/framecore-session`: a venv in `$S/python/framecut`, the model in `$S/models`, `FRAMECORE_WHISPER_MODEL` pointing to it). Never change the system Python or a project lockfile, and keep anything that already works.
3. **Plugins that add to FrameCut, one question.** Check the skill list for each plugin below under any of its [names by host](companion-plugins.md#names-and-installation). Show the ones that are not installed as one numbered list, short enough to read on a phone, one line each on what it adds to FrameCut, then ask: "Which numbers do you want? You can say all, none, or ask about one number." Say in the same message what will be written: the chosen plugins through this host's plugin manager, Toolbox first when an entry needs it; nothing is uploaded. When everything is installed, say so in one line and skip the question.
4. **Install what was picked**, one by one, through the host routes in [names and installation](companion-plugins.md#names-and-installation), and report each as installed, waiting for the user's step (Claude apps, Work without Plugin Creator) or not available on this host. Earshot's engine is a separate step: after Toolbox is installed, relay Toolbox's own tier question ([Earshot through Toolbox](companion-plugins.md#earshot-through-toolbox)). A new conversation lists newly installed skills.
5. **Done.** Say in one line that setup is finished and how to start: send the footage and say what the film is for, or call FrameCut for its brief.

The picked numbers are the consent for those items only. Never install anything that was not picked, never repeat a declined offer in later conversations unless the user asks, and keep FrameCut's own route for every step whose plugin is missing.

## The list

1. **FrameMotion**: designed motion inside the edit (animated titles, kinetic type, data animation, logo endings, shader transitions) rendered and placed on FrameCut's timeline.
2. **FrameCore Works Toolbox**: Earshot for sound (effects placed on the cuts, sound kits, loudness check before delivery), and `rife-interpolate` for smooth slow motion and frame-rate changes of footage (RIFE, downloads its program once after your yes).
3. **FrameCore Open Assets**: free stills, b-roll pictures, music, ambience and sound effects with verified licences and provenance.
4. **FrameCore Works Creative Studio**: briefs, scripts, copy, storyboards, campaigns and prompts around the edit; with it, Studio leads the project and FrameCut edits.

## Tools

| Tool | Needed for | Check | Pinned source |
| --- | --- | --- | --- |
| Python 3.10+ and Pillow | every edit, storyboard and render | `framecut.py capabilities` | host Python or a session venv |
| FFmpeg and FFprobe with libass, libx264, AAC, `xfade`, `loudnorm` | decode, cut, captions, mix, encode | `ffmpeg -hide_banner -filters` lists `ass` and `subtitles` | host package manager |
| PyWhisperCpp | draft speech-to-text and word times | `python -c "import pywhispercpp.model"` | PyPI `pywhispercpp==1.5.1` in a venv |
| Whisper tiny (multilingual, `ggml-tiny.bin`) | the model PyWhisperCpp reads | SHA-256 `be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21` | `https://huggingface.co/ggerganov/whisper.cpp/resolve/5359861c739e955e79d9a303bcbc70fb988958b1/ggml-tiny.bin` |
| Whisper base (multilingual, `ggml-base.bin`, 148 MB), for non-English speech | a more accurate draft transcript | SHA-256 `60ed5bc3dd14eea856493d334349b405782ddcaf0028d4b5df4088345fba2efe` | `https://huggingface.co/ggerganov/whisper.cpp/resolve/5359861c739e955e79d9a303bcbc70fb988958b1/ggml-base.bin` |
| OpenTimelineIO (optional) | `.otio` round-trip check for an editor | `python -c "import opentimelineio"` | PyPI `opentimelineio==0.18.1` in a venv |

An English-only `*.en` model is not a substitute for the multilingual one. A hash mismatch is a blocker: keep the file, report it and do not use it.

## Evidence

Record what ran on which host. The tool check, the question and installs on Claude apps, Codex and ChatGPT Work are NOT_RUN until a run on that host is reported.
