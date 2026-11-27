# Rebuilding a client's reel 1:1 from a reference

How FrameCut rebuilds a reel a client supplies as the pattern ("make ours exactly like this one"): the same cuts, rhythm, camera, shot sizes, captions and shot layout, with the client's own or fictional characters and new dialogue in the user's language. Source: a real client job handed over by the owner on 2026-11-27 (a 3D sample with dialogue, 16 shots, 9:16, 23 s; result about 90 % of the reference). Prices and model names below were observed on that date and change; check them before quoting.

The rebuild runs the usual [layered work](layered-work.md): breakdown and dialogue table are the plan, the reference's cut times are the assembly, voice and mix are the sound layer, captions come last.

## Limits (always)

- **Rights.** Rebuild a reference only when the client owns it or has the right to commission the copy, and say so in the plan. Without that, use the reference only as a technique card (FrameMotion: `skills/framemotion/references/reference-style-rebuild.md`): technique yes, the work itself no.
- **Characters** are the client's own or fictional. No likeness of a real or famous person; no logo, brand mark or mascot copied 1:1 from the reference.
- **The reference's soundtrack** may be reused only after a warning before publication: its music is probably licensed to someone else and Content ID can block or claim the reel. Offer original or CC0 music matched to the reference as the safe option.
- **Paid steps** (start frames, video clips, voices, stem separation) run one at a time, each after the user's yes with its cost stated. No spare takes "just in case"; check the provider balance first.
- **A finished generated clip is not patched** (no masks or picture overlays over a defect). A defect means a new generation, after the user's yes. Replacing a clip's sound is allowed.
- **No new shots.** Do not invent framings the reference does not have; a deviation from these rules needs the user's yes.

## Choosing the route (before any paid step)

Added from the handover's section 13 (2026-11-27; its section 12, which introduces Recast, was not received). Prices are fal list prices seen on 2026-11-27.

| What changes | Route | Cost seen |
| --- | --- | --- |
| Only the person; the reference's sound stays | **Recast** (person swap on the reference video, cuts and motion kept 1:1) | about USD 0.05 per second (unit assumed, see below) |
| The person and a new target-language dialogue | **Recast**, then a voice (section 4), then video-to-video lip-sync; test one shot first | see lip-sync below |
| Scenery, props or framings | **Start frames and clips** (sections 2 and 3; Seedream 5.5 edit at about USD 0.03 per frame is a cheaper frame model than the one above) | see costs |

- **Recast takes no audio.** Inputs: the video, up to 4 photos of the people, a prompt, 768p or 1080p, `enhance_realism`. It always returns the original sound. Prompt: empty or one plain sentence ("Replace the person on the left with reference 1"), never an elaborate one.
- **Lip-sync on fal** (2026-11-27): HeyGen v3 precision USD 0.10/s, sync-3 USD 8/min, Sync 2 Pro USD 5/min, VEED lipsync v2 USD 0.07 per unit, LatentSync USD 0.005/s (the weakest).
- **VEED dubbing pro** (USD 0.18/s) clones the original speaker's voice: never on someone else's footage or a celebrity's; use it only for a voice the client owns.
- **23 s, 16 shots, no retakes:** A) Seedream 5.5 edit + reference-to-video clips + ElevenLabs ≈ 0.06 + 0.48 + 1.60 + 0.25 ≈ USD 2.40. B) Recast + ElevenLabs + HeyGen lip-sync ≈ 0.06 + 1.15 + 0.25 + lip-sync ≈ USD 3.75 (lip-sync on the whole reel) or ≈ USD 2.95 (only the shots with speech). With retakes both come to about USD 3 to 4: A usually needs 30 to 50 % clip retakes and frame fixes (props, captions, continuity); B needs almost none, since set, props and motion come from the original. B means far less work and fewer approval rounds at a similar cost.
- **Unconfirmed:** Recast's price unit (a second was assumed) and lip-sync on cartoon-style 3D faces. A 5 s test costs about USD 1 and runs only after the user's yes.

## 1. Break the reference down (free)

1. Ask for the MP4 file itself; links to Instagram and similar sites need a login and fail.
2. `ffprobe`: resolution, frame rate, duration.
3. Cut points with `ffmpeg -vf "scdet=threshold=10"` or PySceneDetect. The list of cut times is the edit's spine.
4. One still per shot (`ref-01.jpg` to `ref-NN.jpg`) and a contact sheet of them for the user's yes.
5. Dialogue with Whisper and word timestamps: who says what, when. Table: shot, time, character, line in the source language, line in the target language.
6. Translate naturally, not word for word ("Big tips" becomes "dawał duże napiwki", not a literal phrase), and get the user's yes on the table before any paid clip.

## 2. Start frames (paid)

- A character sheet for every character first, then one start frame per shot, edited from the reference still. Model used: fal `nano-banana-pro/edit`, 2K, 9:16, about USD 0.15 per frame. Inputs: the reference still, the character sheet and the first approved frame; the prompt starts "Recreate image 1 exactly… replace the characters…".
- A contact sheet of all frames for the user's yes.
- **Continuity:** after every prop change (a photo on a phone screen, a tablecloth, cutlery, car keys) check all frames again. Defects seen: a bare table in four shots, a phone lying screen-up with the photo still showing.

## 3. Video clips (paid)

- Model used: fal `minimax-h3-turbo/reference-to-video`, 1080p, 2 s, about USD 0.05 per second (about USD 0.10 per shot). Inputs: the start frame and the reference shot as `reference_video_urls`.
- **One shot at a time**, each after the user's yes.
- Start the prompt with: "Copy only the character motion, facial expression, timing and camera of Video 1. Ignore and do NOT copy any subtitles, captions, words or letters…". Without it the model paints the reference's captions into the picture.
- Describe props explicitly ("puts the phone down SCREEN-DOWN"). "The photo never changes" kept the photo on screen after the phone was put down.
- Target-language lines: one 2 s clip per line, "fast, snappy Polish" (or the language in use). Phonetic spelling only for foreign words ("moo-STAN-ga"); not for native letters such as Polish Ł ("wad-ny" came out as "wadny"). Prefer short common words ("duże" over "wielkie").
- The model's voice often lands 0.2 to 0.3 s after the mouth: measure with Whisper and shift the sound.
- Check the last 0.5 s (a pasted copy of the input frame sometimes appears) and a strip of 4 frames per second.

## 4. Voices

- The video model's own voices were judged artificial by the client. What worked: ElevenLabs `eleven_v4` text-to-speech with audio tags and a library voice in the target language, about 50 to 80 credits (USD 0.02 to 0.03) per line. Chosen tone: `[confident] [warmly] [slightly raspy voice]`; not a dreamy whisper or sighs.
- Test one line first with three voices side by side (original plus variants), then voice the rest.
- **Fit to the mouth:** Whisper word boundaries, then time-stretch each phrase with Rubber Band to the mouth's span, tempo limit 1.45, optional manual boundaries. The owner's script for this (`fit3.py`) is not in the repository; follow these steps. An off-screen voice needs no fitting; a longer line fits by slowing the reaction shot slightly (1.2x).
- Rejected in that job: ElevenLabs speech-to-speech, Seed TTS 3.0 (tragic male reads), Seed Audio with the reference's English timbre (accent).
- In a shell loop over lines, give every `python` and `ffmpeg` call `</dev/null` (ffmpeg also `-nostdin`), or they eat the loop's input.

## 5. Sound and mix

- **Option A, the reference's own bed:** remove the voices with fal `sam-audio/separate` (prompt "people speaking", about USD 0.05) and keep the residual. Licence and Content ID warning before publication (see Limits).
- **Option B, own music:** original or CC0 music matched to the reference (Open Assets, see [plugins that add to FrameCut](companion-plugins.md#open-assets)).
- Voice chain: high-pass 90 Hz, EQ matched to the spectrum of the reference's voices (1/3 octave, 70 % strength, at most ±5 dB; the owner's `eq_match.py` is not in the repository), de-esser, 2.5:1 compression, no reverb, a warm tone.
- Music sits about at the voice's level, as in the reference, without ducking.
- Loudness in two passes: measure, apply one fixed gain to -14 LUFS, then `alimiter` at 0.78 (true peak below -1 dBFS). Not dynamic `loudnorm`, which changes the voice-to-music balance.

## 6. Edit on the reference's cut times

- A shot list drives the render (file, in, out, caption text); the owner's `montaz-vN.py` is not in the repository, FrameCut's own timeline does the same.
- Cut on the reference's cut times. Per-shot tempo 1.07 to 1.15 (picture and voice together); a longer target-language line borrows time from a shot without dialogue.
- A line may run into the next shot when the reference does that.
- Captions are added in the edit, never generated in the clip: ASS, a heavy display face (Montserrat ExtraBold 64 in that job), glow and a small pop, 1 to 2 words, never over a face. FrameCut's [Captions](../captions/CAPTIONS.md) and [readability defaults](readability-defaults.md) apply.
- Preview at 540p plus a side-by-side: reference | ours, with our sound.

## 7. 60 fps with RIFE (free)

- Toolbox's `rife-interpolate` ([smoothing and slow motion](companion-plugins.md#smoothing-and-slow-motion)). The job used the original `rife-ncnn-vulkan` 20221029 with model `rife-v4.6`; Toolbox pins the TNTwise fork with `rife-v4.26` by default and keeps `rife-v4.6` as the lighter choice. Both are MIT.
- Interpolate each shot separately: render the edit without captions, take the cut frames from `scdet`, run RIFE per segment, join, then add captions and sound. The owner's `rife-v6.sh` is not in the repository; the launcher does the same per shot.
- In the cloud without a graphics card it runs on the CPU (Mesa's software Vulkan driver): about 1.5 s per frame at 540x960, about 35 minutes for 23 s. A Mac is much faster.
- Not ffmpeg `minterpolate` (it tears edges).

## 8. Delivery

- Client preview: 540x960 with a watermark scaled to the frame (`overlay` sized 540x960; a horizontal-only watermark script does not do this).
- The final without the watermark only after the client accepts.
- Version names rise (`v1`, `v2`, ...); old versions stay.

## Costs seen (16 shots, 2026-11-27)

| Step | Cost |
| --- | --- |
| Start frames | 16 × 0.15 ≈ USD 2.4 |
| Video clips | 16 × 0.10 plus 30 to 50 % retakes ≈ USD 2.2 to 2.5 |
| Voices | ≈ USD 0.2 |
| Stem separation | ≈ USD 0.05 |
| Total | ≈ USD 5 to 6 |

## Checklist

1. Reference breakdown and target-language dialogue table: user's yes.
2. Character sheet: yes.
3. Start frames and contact sheet: yes.
4. Prop continuity check across all frames.
5. Video clips one at a time, each with a yes.
6. Voices: one-line test, choice, then all lines.
7. Music (reference bed with warning, or own) and mix.
8. Edit on the reference's cut times, 540p preview, side-by-side: yes.
9. 60 fps with RIFE, when the brief asks for it.
10. 540p watermarked export to the client.
11. Final without watermark after acceptance.

## Evidence

Owner's client handover, 2026-11-27: the process above produced the delivered sample (`PASS_REPORTED`). FrameCut's own run of this page: `NOT_RUN`.
