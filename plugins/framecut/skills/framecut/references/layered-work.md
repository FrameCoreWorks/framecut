# Layered work

Owner rule (2026-11-17), mandatory. Edit like a working editor: one layer at a time, each closed and checked before the next starts. Never build the whole film in one pass.

## The layers

Each layer is a pass of its own, recorded in the project checkpoint as `layer` next to `stage`.

| # | Layer | Closed when | FrameCut work |
| --- | --- | --- | --- |
| 1 | Assembly | Everything in story order, long, nothing trimmed for rhythm yet | `ingest`, `analyze`, first `add_sequence` |
| 2 | Rough cut | Structure and story work with temporary music and no polish | storyboard revision shown to the user |
| 3 | Fine cut | Timing to the frame, performance choices, music final | `apply` trims and splits, `plan-cuts`, `beats` |
| 4 | Picture lock | The user accepted the board; timing is frozen | acceptance recorded in the project brief |
| 5 | Sound | Dialogue, room tone, music, SFX, ducking, mix to spec | buses, effects, Earshot checks |
| 6 | Colour | One correction, matching, then one look | picture effects, one pass |
| 7 | Captions | Spelling and timing of every super and caption | texts, captions, caption QA |
| 8 | QC | The exported file passes | `render --mode final`, `verify`, `review` |

## Rules

- **Check after every layer.** Look at a short set of frames (at least three per scene, or a contact sheet from `storyboard` or `preview-frame`) and listen where the layer is sound. Say which layer you are on and what the check showed.
- **A fix goes back to its own layer.** A wrong cut is a layer 3 fix, not a caption trick. After the fix, check the layers above it again, because timing changes move captions, sound and motion returns.
- **Do not mix layers.** No colour while the timing still changes, no sound mix on a scene whose cut is open, no captions before picture lock. A change to a lower layer after the upper ones are done is expensive: plan it early.
- **One layer per revision.** Make each layer its own `apply` revision (or its own `render` pass), so it can be undone or switched off and the layer below inspected without it. A render that carries all layers at once is for the final file only.
- **Motion pieces** from FrameMotion are built in their own layers (plan, type, motion, depth, colour, sound, QC). Ask for the piece after its plan is agreed and attach it at layer 3 or later, never as a way to hide a weak cut.
- **Exception.** A very short, simple job (one trim, one caption fix, one format change) may run its layers in one pass. Write the reason into the plan or the board note.

Related: [editor craft](editor-craft.md#working-stages), [storyboard gate](../SKILL.md#storyboard-before-final-rendering).
