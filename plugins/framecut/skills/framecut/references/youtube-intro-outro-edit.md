# YouTube intro and outro in the edit

Read this when a YouTube video's opening or ending is being cut: where the hook, the title sting and the outro sit, how long each may be and what the last 20 seconds must leave free. The graphics themselves (stings, bumpers, lower thirds, end-screen backgrounds, Shorts openers) are built in FrameMotion (FrameMotion: `skills/framemotion/references/youtube-intro-outro.md`, with recipes and concepts); without FrameMotion, use the user's own graphics or a plain title card.

Facts checked on 2026-11-18. Official rules link to YouTube Help; measured numbers name who measured them; the rest is editing practice and is marked as inference.

## Platform facts that shape the cut

| Fact | Number | Source |
| --- | --- | --- |
| End screen | Last 5 to 20 s of a video at least 25 s long; up to 4 elements on 16:9 | [YouTube Help: Add end screens](https://support.google.com/youtube/answer/6388789) |
| During the end screen | Card teasers and the channel watermark are hidden | same |
| Watermark "End of video" | Shows for the last 15 s | [YouTube Help: Channel branding](https://support.google.com/youtube/answer/10456525) |
| Info cards | Up to 5, each at a chosen time | [YouTube Help: Info cards](https://support.google.com/youtube/answer/6140493) |
| Retention "Intro" | A typical intro is about 30 s; 50% or more still watching at 30 s counts as above typical | [YouTube Help: Content tab analytics tips](https://support.google.com/youtube/answer/12942217) |
| Chapters | First timestamp 00:00, at least three, each at least 10 s | [YouTube Help: Video chapters](https://support.google.com/youtube/answer/9884579) |
| Shorts | Square or vertical, up to 3 min; no end screen, a Related video link instead; call to action in the final 5 s | [YouTube Help: Shorts](https://support.google.com/youtube/answer/10059070), [YouTube Blog 2026-07-14](https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide) |
| Loudness | About -14 LUFS integrated; louder videos are turned down, quieter ones are not raised (measured, not published by YouTube) | [Umbrella Creators 2026-10-20](https://umbrellacreators.com/blog/how-to-normalize-audio-for-youtube), [QuickVeed 2026-11-01](https://quickveed.com/blogs/loudness-lufs-for-youtube-and-podcasts) |

YouTube's own opening advice: grab attention first, make clear what the video is, tease the rest, show branding later ([Creator Playbook, first 15 seconds](https://blog.youtube/news-and-events/this-is-first-of-series-of-posts)); say within the first five seconds what the viewer will see ([Four tips to hook your viewers](https://blog.youtube/creator-and-artist-stories/four-tips-to-hook-your-viewers-on)).

## Opening order

1. **Hook or cold open, 5 to 15 s.** The strongest moment, the finished result, the verdict or the question, cut from the footage ([moment roles](moment-roles-and-clips.md) picks it). No logo, no black frame, no slow fade in.
2. **Title sting, 1.5 to 3 s** (or none). Placed on a sound accent right after the hook's last line; the first word after it starts at least 0.2 s after the sting's hit.
3. **Content.** The promise made in the hook is answered before the 30 s mark, or the hook's question is clearly being worked on.

A returning series may use a 1 to 2 s bumper after the hook instead of a sting. A video for new viewers from search may drop the sting entirely and use a lower third with the channel name in the first minute (inference: compare new and returning viewers in the key moments report before deciding).

Chapters: 00:00 names the hook's topic, not "Intro"; every chapter at least 10 s.

## Ending order

1. **Last content beat.** The final tip, reveal or result. Do not announce the end ("that's all for today") before it (inference: viewers leave on an announced ending).
2. **Bridge, 2 to 4 s.** One spoken line naming the next video and why it follows; this is the cut where the outro begins.
3. **End-screen window, 15 to 20 s** (minimum 5 s). Keep the picture simple: the speaker in the left two thirds, a quiet b-roll or FrameMotion's end-screen background. Nothing important where YouTube draws its elements (right side and lower centre; measured element sizes on 1920 x 1080: video boxes 620 x 349 to 862 x 485, subscribe circle 296 x 296, per [Mark Studios](https://www.markstudios.com/tools/youtube-end-screen-template)).
4. **Out.** Music resolves or a 1 to 2 s logo bumper; no dead air, no long black.

Cards belong earlier in the video, at the moment the related topic comes up; a card inside the end-screen window loses its teaser.

## Sound at the joins

- J-cut the first word of the content under the sting's tail only when the sting has no voice of its own; otherwise leave the 0.2 s gap.
- Keep a sting's short-term loudness within about 2 LU of the speech around it (inference; measure on the exported file).
- Under the end-screen window, keep speech or a music bed about 15 to 20 dB under dialogue level if both play; the outro must not jump in level.
- Whole video about -14 LUFS integrated, true peak at or below -1 dBTP, measured on the delivered file ([editor craft](editor-craft.md#sound-for-editors)).

## Shorts

No intro: frame 0 is the hook. End on a frame that loops cleanly back to the start and put the call to the related video in the final 5 s. Keep text and faces inside the vertical safe zone ([platform caption specs](platform-caption-specs.md)); for YouTube Shorts the interface covers about 309 px at the top and 380 px at the bottom of a 1080 x 1920 frame (measured by [Kreatli](https://kreatli.com/safe-zone-checker/youtube-safe-zone-checker)), with the button column on the right.

## Layers

These decisions belong to the layers in [layered work](layered-work.md): hook choice and the place of the sting in the rough cut; exact joins and the 0.2 s gap in the fine cut; the end-screen window length before picture lock; levels at the joins in the sound layer; QC of the exported file checks that the video is at least 25 s when an end screen is planned, that the window is at least 5 s, that the first frame is not black and that no caption or lower third sits under the end-screen area.
