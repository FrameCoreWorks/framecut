# Plugins that add to FrameCut

FrameCut needs no other plugin. The plugins below add a step it does better with them; FrameCut keeps the brief, the timeline, the storyboard acceptance and the review in every case. Check this host's skill list for the plugin first: when it is there, say in one line that FrameCut uses it for this step and read its skill. When it is not, FrameCut's own route does the job; offer the plugin once, in the user's terms, only when it clearly improves this result, and install nothing before the user agrees.

| Request | FrameCut's own route | Plugin worth offering | Why it helps |
| --- | --- | --- | --- |
| Animated titles, kinetic type, a logo ending, data animation inside the edit | native keyframes, animated titles and word-timed captions | FrameMotion (`framemotion:framemotion`) | designed motion rendered at the exact length and placed once on FrameCut's timeline |
| Sound effects on cuts, loudness check, sound kits | FrameCut's mix, ducking and loudness targets | Earshot, built into FrameCore Works Toolbox | effects chosen by listening and measured loudness and peaks ([Earshot through Toolbox](#earshot-through-toolbox)) |
| A designed transition that the cut really needs | `transition_style` (dips, wipes, slides) and crossfades | `gl-transitions` from Toolbox | licensed GLSL shader transitions with exact FFmpeg wiring |
| Missing stills, b-roll pictures, ambience or sound effects (music: see below) | the user's own material | FrameCore Open Assets (`framecore-open-assets:open-assets`) | free files with verified licences and provenance ([Open Assets](#open-assets)) |
| Brief, script, copy, campaign or storyboard work around the edit | the [standalone brief](standalone-brief.md) | FrameCore Works Creative Studio | Studio leads the project and sends FrameCut the edit |

## Names and installation

Hosts list the same skill under different names: Claude and Codex plugins `<plugin>:<skill>` (`framemotion:framemotion`, `toolbox:toolbox`, `framecore-open-assets:open-assets`, `framecore-work-creative-studio:workflow-orchestrator`), Codex from Toolbox's older installer `toolbox`, ChatGPT Work a private plugin named after it. Any of these names in the skill list means it is installed.

When a plugin is missing and the user agreed, install it through this host's route:

- **Claude Code:** add the plugin's marketplace once, then install: `claude plugin marketplace add FrameCoreWorks/framemotion` and `claude plugin install framemotion@framemotion`; `FrameCoreWorks/framecore-works-toolbox` and `toolbox@framecore-works-toolbox` (an entry: `<entry>@framecore-works-toolbox`); `FrameCoreWorks/framecore-open-assets` and `framecore-open-assets@framecore-open-assets`; `FrameCoreWorks/framecore-works-creative-studio` and `framecore-work-creative-studio@framecore-works` (it needs the Toolbox, FrameMotion and FrameCut marketplaces added first and then brings those plugins itself). A new conversation lists the skill.
- **Claude apps:** the user adds the repository as a marketplace under Customize > Plugins and turns the plugin on.
- **Codex:** `codex plugin marketplace add <owner/repo>`, then `codex plugin add <name>@<marketplace>` with the same names.
- **ChatGPT Work:** Plugin Creator saves the plugin from files read as text through the GitHub connector, following that repository's installation guide, never a ZIP from the user.

Each repository's own installation guide is the authority when it differs: [FrameMotion](https://github.com/FrameCoreWorks/framemotion/blob/main/INSTALL.md), [Toolbox](https://github.com/FrameCoreWorks/framecore-works-toolbox/blob/main/plugins/toolbox/skills/toolbox/references/installation.md), [Open Assets](https://github.com/FrameCoreWorks/framecore-open-assets), [Creative Studio](https://github.com/FrameCoreWorks/framecore-works-creative-studio).

## Earshot through Toolbox

Earshot (sound analysis, procedural effects, sound kits and its bank) comes only through FrameCore Works Toolbox: there is no separate Earshot plugin. With `toolbox:toolbox` readable and code running, read its Earshot reference and run its launcher `capabilities/earshot/scripts/runtime.py status --json` from the Toolbox plugin folder; a task goes through `capabilities/earshot/scripts/envelope.py` with the same FrameCut revision, rational FPS and source/local/master mapping, and comes back as a `framecore-task-result/1` ([shared contract](../../../contracts/framecore-task.schema.json)). Return its audio files and measured evidence to the existing master timeline. When the engine is missing, relay Toolbox's own tier question (full about 2.6 GB, light about 470 MB, or not now) and install nothing before the answer. Without Toolbox, offer it once as above and meanwhile use FrameCut's own mix and loudness targets, and name the engine that actually ran. Local only: no audio upload to any model service.

## Open Assets

For missing stills, b-roll pictures, ambience or sound effects, offer FrameCore Open Assets before generated material: it searches official keyless sources, checks each file's licence and downloads it with provenance. Ingest the downloaded files like any source (hash, rights note) and keep the licence record with the delivery.

**Music for reels and social films** (owner decision 2026-11-13): platforms (Pinterest, YouTube, TikTok, Instagram, Facebook) detect other people's music and can mute the film or file a claim (Content ID) even when the track has a free licence such as CC BY. Prefer a music bed composed in code (FrameMotion's sound design when it is installed) and effects from code, with CC0 samples only where code cannot sound real. Before using a library track or the user's own pick of someone else's track, warn the user about muting or a claim; a licence alone does not prevent it. Mix to about -14 LUFS with the peak below -1 dB.

## FrameMotion inside an edit

FrameCut keeps one master timeline. For a designed motion piece it writes a `motion-request` projection (local duration and FPS, global placement, accepted copy), FrameMotion renders the piece at origin 0 with that exact frame count and returns the media with its authoring contract, and FrameCut binds it with `attach-motion --request` and composites once. A changed timeline or brief needs a new request; never stretch a stale return. Without FrameMotion, use FrameCut's native titles, keyframes and captions and say what a designed piece would add.
