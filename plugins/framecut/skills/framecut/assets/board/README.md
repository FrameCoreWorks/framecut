# Board composer

`board_compose.py` lays out storyboard panels as numbered contact-sheet pages (PNG) and one PDF, with exact labels under each frame. FrameCut's `storyboard` command calls it; it can also run on its own:

```sh
python3 board_compose.py board.json --out-dir boards/
```

Panels support `id`, `time`, `image`, `camera`, `action`, `audio` and `super`, plus the board's `language` and localized `labels`. It needs Python 3 and Pillow, and uses the bundled Inter fonts (`../fonts/inter`).

| Source | Source SHA-256 | This copy SHA-256 | Change |
| --- | --- | --- | --- |
| Creative Studio 1.178.1 (main `bc3724ea`), `skills/storyboard-board-architect/scripts/board_compose.py` | `dd612344109e1252ddd6644fff3d42c5aa9385db5a1c76e2f2759d7542a05355` | `04dfb0d65f81ca1534bc142f31ea54e4b8a36db6799b76580bb879d2d0278373` | font folder points at FrameCut's bundled fonts |

A repository check compares the copy with the recorded hash.
