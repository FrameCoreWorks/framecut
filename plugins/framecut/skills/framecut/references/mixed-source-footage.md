# Mixed-source footage: client film, phone clips and AI video in one edit

How FrameCut takes in footage from different sources (a client's camera files, phone clips, a talking head, clips from AI video generators, generated stills) and prepares them so motion graphics can sit on top: ingest checks, conform, stabilising, cutting AI clips, the talking-head layout and the sound edit. The compositing core (layer stack, mattes, alpha, text over moving pictures, matching generated and real, 2.5D parallax, concepts with a named wow and the common compositing mistakes) is one page in FrameMotion (FrameMotion: `skills/framemotion/references/mixed-media-compositing.md`); this page does not repeat it.

Owner request 2026-11-18. Facts with a number carry a source link; lines marked *(inferred)* are working judgement. Every recipe runs on local FFmpeg without accounts or keys; paid generators appear only as a source of material.

## Ingest check

Probe every file before it enters a sequence (FrameCut's `ingest` and `analyze` record most of this; this command shows the rest):

```bash
ffprobe -v error -select_streams v:0 \
  -show_entries stream=codec_name,width,height,sample_aspect_ratio,r_frame_rate,avg_frame_rate,pix_fmt,color_transfer,color_primaries,color_space:stream_side_data=rotation \
  -of default=nw=1 clip.mov
```

| Field | Problem when | Fix |
| --- | --- | --- |
| `r_frame_rate` vs `avg_frame_rate` | They differ: variable frame rate. Phone cameras vary the rate by default and may drop to 24 fps in low light ([Dolby on iPhone capture](https://professionalsupport.dolby.com/s/article/Using-an-Apple-iPhone-12-captured-Dolby-Vision-content-as-a-source-in-a-Dolby-Vision-production?language=en_US)) | Conform to a constant rate before editing |
| `color_transfer` | `arib-std-b67` (HLG) or `smpte2084` (PQ): HDR. iPhone HDR is 10-bit HEVC with an HLG base layer and BT.2020 primaries (same source) | Tone-map to Rec.709 SDR before any graphics |
| `color_transfer` empty or `unknown` | Untagged: players guess and colours shift between sources | Tag Rec.709 on the conformed file |
| Frame rate differs between sources | 24 fps AI clips in a 25 or 30 fps edit judder | Choose the timeline rate (below) |
| Rotation side data, odd `sample_aspect_ratio` | Picture turns or stretches on export | Bake rotation and `setsar=1` in the conform |
| Audio sample rate not 48 kHz | Drift and resampling at mix | Resample to 48 kHz in the conform |

## Conform recipes

**Timeline frame rate.** Use the rate of the main footage (usually the talking head or the client's camera) *(inferred)*. Generated clips are 24 fps for Veo 3.1 and Runway Gen-4 ([Google](https://ai.google.dev/gemini-api/docs/veo), [Runway](https://help.runwayml.com/hc/en-us/articles/37327109429011-Creating-with-Gen-4-Video)). In a 25 fps edit either play every frame at 25 (the clip runs 25/24, about 4 % faster, usually unnoticed without speech) or let `fps=25` repeat one frame per second *(inferred)*; in a 30 fps edit `fps=30` repeats frames in a pattern that judders on slow pans, so use such clips in short cuts or on mostly static shots. Motion-interpolated frames (`minterpolate`) create warping on faces and hands and are a last resort; RIFE through Toolbox's `rife-interpolate` does better on camera footage ([smoothing and slow motion](companion-plugins.md#smoothing-and-slow-motion)), but on AI clips check the frames, since their warping grows.

**VFR to CFR, size and tags** (tested with FFmpeg 6.1):

```bash
ffmpeg -i phone.mov -vf "fps=30,scale=1920:1080:flags=lanczos,setsar=1" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -ar 48000 phone_cfr.mp4
```

**HDR (HLG or PQ) to SDR Rec.709.** Linearise, map primaries, tone-map, then apply the 709 curve; re-tagging alone gives a washed-out picture. Hable keeps shadow and highlight detail at the cost of slightly darker overall ([ffmpeg tonemap](https://ffmpeg.org/ffmpeg-filters.html#tonemap-1)). Needs a build with `zscale` (Linux builds usually have it; check `ffmpeg -filters | grep zscale`):

```bash
ffmpeg -i hdr.mov -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,\
tonemap=tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" \
  -c:v libx264 -crf 18 -c:a copy sdr.mp4
```

Grade colour only after this; FrameCut's colour rules apply ([editor craft](editor-craft.md#colour-for-editors)). A display shows sRGB and phone-viewed Rec.709 near gamma 2.2 while Rec.709 masters target 2.4 (BT.1886) ([The Post Flow](https://thepostflow.com/post-production/why-do-your-exports-look-different-on-your-iphone/)); judge looks on the device class the film is for.

**Reframe a 16:9 talking head to 9:16** with the face in the upper third and room for captions below *(inferred)*; FrameCut's per-format framing does this natively, or:

```bash
ffmpeg -i talk.mp4 -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920:flags=lanczos,setsar=1" talk_916.mp4
```

## Stabilise client footage

Only when graphics must sit on the picture or the shake hurts the cut; otherwise shake is part of the material. Two passes with vid.stab, values and limits in FrameMotion's page (section 6). Stabilise before the edit's colour layer, because `optzoom` crops and that changes framing.

## AI clips in the edit

- **Cut the clean range.** Watch each generated clip at full speed and frame by frame; mark where identity drift, morphing or background swim starts and use only what comes before *(inferred: usually the first 2 to 4 s of an 8 s clip carry the most stable frames)*. Record the range in the edit note.
- **Hide the drift point.** End the clip on a cut, a cutaway or a FrameMotion wipe placed at the frame where drift starts; never on a slow dissolve, which shows both faces at once.
- **Flicker.** `deflicker=size=5:mode=pm` on the clip before colour ([ffmpeg](https://ffmpeg.org/ffmpeg-filters.html#deflicker)).
- **Generated audio** (Veo always generates sound) is a draft: mute it or replace it in the sound layer unless the user wants it.
- **Speed.** Speed changes on AI clips magnify warping; prefer cutting shorter to slowing down *(inferred)*.

## Talking head with motion pieces

- Lower thirds on the side the person looks away from, clear of the mouth and chin, held long enough to read twice *(inferred)*; captions stay under them, inside the platform safe zone ([platform caption specs](platform-caption-specs.md)).
- Motion pieces come from FrameMotion as ProRes 4444 with straight alpha, attached with `attach-motion` at layer 3 or later ([layered work](layered-work.md)); a picture lock change after attachment sends the piece back to FrameMotion for a new duration.
- Text behind the speaker, a matte cut-out or a tracked label are FrameMotion builds on the conformed and stabilised plate FrameCut hands over.

## Sound and sync

- **Lip-sync limits.** Viewers detect sound about 45 ms early or 125 ms late, and accept about 90 ms early or 185 ms late ([ITU-R BT.1359](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1359-0-199802-S!!PDF-E.pdf)); EBU R37 sets the end-to-end broadcast limit at 40 ms early and 60 ms late ([EBU R37](https://tech.ebu.ch/docs/r/r037.pdf)). Aim for zero; at 25 fps one frame is 40 ms, so a one-frame slip of sound before picture is already at the limit.
- **Variable-frame-rate phone clips drift** against their own sound; conform first, then check sync at the start and end of each long clip.
- **Ducking.** Music under speech follows [editor craft](editor-craft.md#sound-for-editors) and FrameCut's `duck_db` on the music bus. A quick sidechain duck in FFmpeg (threshold 0.125, ratio 2, attack 20 ms and release 250 ms are the defaults; [ffmpeg](https://ffmpeg.org/ffmpeg-filters.html#sidechaincompress)):

  ```bash
  ffmpeg -i music.wav -i voice.wav -filter_complex \
    "[1:a]asplit[vo][sc];[0:a][sc]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[m];\
     [m][vo]amix=inputs=2:normalize=0[a]" -map "[a]" mix.wav
  ```

- **Motion accents** land 1 to 2 frames before the sound peak; loudness is measured on the encoded file.

## Where it happens in the editing layers

| Editing layer ([layered work](layered-work.md)) | Mixed-source work in it |
| --- | --- |
| 1 Assembly | Ingest check, conform (CFR, HDR to SDR, tags, 48 kHz), stabilise where needed, AI clean ranges marked |
| 2 Rough cut | Order of real and generated shots; where motion pieces will go, as plain placeholders |
| 3 Fine cut | Cuts at AI drift points, J and L cuts on the talking head, FrameMotion pieces attached |
| 4 Picture lock | Timing frozen; FrameMotion builds final pieces to these durations |
| 5 Sound | Replace generator audio, dialogue, room tone, ducking, sync checked against the limits above |
| 6 Colour | One correction per source to match, then one look over all, after HDR was mapped in layer 1 |
| 7 Captions | Captions clear of lower thirds and inside the platform safe zone |
| 8 QC | Frame checks every 0.5 s, drift points, sync at start and end, `verify` on the delivered file |

## Common mistakes (editing side)

- Editing a variable-frame-rate phone clip directly: sync slips and overlays drift.
- Re-tagging HDR as Rec.709 instead of tone-mapping it.
- Leaving untagged files in a mixed edit, so each player guesses the colour.
- Keeping an AI clip past its drift point, or dissolving across it.
- Slowing an AI clip down to fill time.
- Leaving the generator's own audio under the edit by accident.
- Colour-matching before the HDR conform, or grading each source with its own look.
- Captions and lower thirds stacked in the same corner.
- Attaching motion pieces before picture lock and not rebuilding them after a timing change.

Concepts with a named wow and the compositing mistakes are in FrameMotion's page. The commands here ran on synthetic clips with FFmpeg 6.1 in the Claude cloud sandbox on 2026-11-18; they were not run on real client footage (`NOT_RUN`).
