# ComfyUI – Save Video Last Frame

A tiny ComfyUI custom node that takes a `VIDEO` input, extracts its **last frame**, and saves it as a PNG into ComfyUI's **input** directory (so it can be reused by other nodes/workflows right away).

## Node

**Save Video Last Frame (to input)** — category: `video`

| Input | Type | Description |
|-------|------|-------------|
| `video` | `VIDEO` | The video to read the last frame from |
| `filename_prefix` | `STRING` | Prefix for the saved file (default `last_frame`) |

| Output | Type | Description |
|--------|------|-------------|
| `image` | `IMAGE` | The last frame, usable downstream |
| `filename` | `STRING` | The saved file name |

The file is written to whatever ComfyUI reports as its active input directory
(`folder_paths.get_input_directory()`), auto-numbered to avoid overwriting:
`last_frame_00001.png`, `last_frame_00002.png`, …

## Installation

Clone into your ComfyUI `custom_nodes` folder and restart ComfyUI:

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/ahmedbana/ComfyUI-SaveVideoLastFrame.git
```

Then fully restart ComfyUI (custom nodes are only scanned at startup) and
search for **"Save Video Last Frame"**.

## Requirements

Uses only libraries ComfyUI already ships with (`numpy`, `Pillow`,
`folder_paths`, and the ComfyUI `VIDEO` API). No extra dependencies.

## License

MIT
