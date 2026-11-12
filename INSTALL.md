# Install FrameCut

This is the complete installation procedure for the assistant performing a user-requested installation. FrameCut is one plugin with one skill, `framecut`. Creative Studio, FrameMotion, Toolbox and Open Assets are optional; FrameCut never requires them.

## Paste this prompt

Paste the repository link into the agent with one sentence, in any language. The same sentence works in ChatGPT Work, Codex and Claude Code:

```text
Install FrameCut for me from https://github.com/FrameCoreWorks/framecut
Read its installation guide for this app first, then explain each step in plain words.
```

The request is the installation consent. The assistant follows the section for its host below, says in one plain sentence what each step does, shows no command unless asked, and after installing runs the [first setup](#first-setup).

## Before you install

1. Resolve `main` (or the requested release) once to a full commit and use that commit for every file.
2. Look for an existing FrameCut installation first and update it instead of creating a second copy. A Creative Studio of version 1.178.1 or older carries its own editing skill `opencut-video-studio`; that is not a conflict, but say that a newer Studio hands editing to FrameCut.
3. Keep the whole `plugins/framecut/` folder together: the skill reads its references, engine, fonts and scripts by relative paths. Never install only `SKILL.md`.

## Claude Code

```text
/plugin marketplace add FrameCoreWorks/framecut
/plugin install framecut@framecut
```

The marketplace is named `framecut` and holds exactly this plugin. When Creative Studio's marketplace (`framecore-works`) also lists FrameCut, install it from one marketplace only; two installed copies both stay enabled, so remove one with `claude plugin uninstall`. A new session lists the skill as `framecut:framecut`.

## Claude apps (claude.ai, desktop)

Where the workspace supports repository marketplaces (Customize > Plugins), add `FrameCoreWorks/framecut` and enable **FrameCut**. The apps do not install plugin dependencies, so a Studio user enables FrameCut by hand. Editing needs the app's code execution with FFmpeg; without it FrameCut plans the edit, shows the storyboard and writes an Edit Pack. App installation and rendering: NOT_RUN.

## Codex

Where Codex has its own plugin manager (`codex plugin marketplace --help` prints its commands):

```sh
codex plugin marketplace add FrameCoreWorks/framecut
codex plugin add framecut@framecut
```

`codex plugin list` then shows FrameCut `installed, enabled`; a new session loads the skill. Update with `codex plugin marketplace upgrade framecut` and the same `codex plugin add`. Without a plugin manager, use the host's native plugin flow with the complete `plugins/framecut` folder. Codex installation: NOT_RUN.

## ChatGPT Work

ChatGPT Work saves plugins only through OpenAI's **Plugin Creator** (side menu > Plugins > search `Plugin Creator` > the one by OpenAI > Install; then start a new Work conversation, type `@`, select **Plugin Creator** and paste the prompt). Without Plugin Creator's create and update tools in the conversation, save nothing and give the user these steps.

1. Search Plugin Creator's saved plugins for FrameCut: none means a first installation, otherwise update that identity with its current release guard. Never create a duplicate.
2. List `plugins/framecut/` recursively at the pinned commit through the GitHub connector; each entry carries its git blob `sha`. Write every file under `/mnt/data/framecut/<path>` in code execution: text files as their exact text, binary files (fonts) from their base64 content. The `tests/` folder is not needed at run time and may be left out. Never ask the user to download or upload a ZIP, and treat a failed download in code execution as expected: copy the files through the connector instead.
3. Check every file against its git blob hash (`sha1(b'blob <size>\0' + bytes)`), re-read any mismatch, and zip the folder only when all match.
4. `create_plugin` (first installation) or `update_plugin` with the release guard, then read back the saved manifests and `skills/framecut/SKILL.md`. Report the save, the file check and the first setup separately.

The package is small (about 2.5 MB, about 110 files, most of it fonts). Whether the Work sandbox has FFmpeg with libass and can install PyWhisperCpp is checked by the first setup in each session. ChatGPT Work installation: NOT_RUN.

## First setup

Right after installing, in the same conversation, the skill runs its [first setup](plugins/framecut/skills/framecut/references/first-setup.md): it says what FrameCut can do on this host, checks the editing tools (Python, Pillow, FFmpeg with libass, PyWhisperCpp and the pinned Whisper tiny model) and asks before installing anything missing, then asks once, as one numbered list, whether to add the plugins that extend FrameCut (FrameMotion for designed motion, Toolbox for Earshot sound and shader transitions, Open Assets for licensed media, Creative Studio for briefs and campaigns). Only the picked numbers are installed; FrameCut works fully without any of them. Later the user can say "Configure FrameCut". With Creative Studio running its own setup, Studio's list covers these plugins and FrameCut does not ask again.

## With Creative Studio

Creative Studio routes editing, captions and subtitles to FrameCut. Install FrameCut beside Studio from either marketplace; Studio's installation guides add it in the companion setup.
