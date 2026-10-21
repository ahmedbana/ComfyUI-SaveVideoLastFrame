import os

import numpy as np
from PIL import Image

import folder_paths


class SaveVideoLastFrame:
    """Save the last frame of a VIDEO as a PNG into ComfyUI's input directory."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "video": ("VIDEO",),
                "filename_prefix": ("STRING", {"default": "last_frame"}),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image", "filename")
    FUNCTION = "save_last_frame"
    OUTPUT_NODE = True
    CATEGORY = "video"

    def save_last_frame(self, video, filename_prefix="last_frame", prompt=None, extra_pnginfo=None):
        # images: float tensor [frames, H, W, C] in range [0, 1]
        images = video.get_components().images
        if images is None or images.shape[0] == 0:
            raise ValueError("The input video has no frames.")

        last = images[-1]
        array = (255.0 * last.cpu().numpy()).clip(0, 255).astype(np.uint8)
        img = Image.fromarray(array)

        input_dir = folder_paths.get_input_directory()
        os.makedirs(input_dir, exist_ok=True)

        # Find a non-colliding filename like last_frame_00001.png
        counter = 1
        while True:
            filename = f"{filename_prefix}_{counter:05d}.png"
            full_path = os.path.join(input_dir, filename)
            if not os.path.exists(full_path):
                break
            counter += 1

        img.save(full_path, compress_level=4)

        # Returned "images" lets this node feed downstream nodes and show a preview.
        results = [{"filename": filename, "subfolder": "", "type": "input"}]
        return {
            "ui": {"images": results},
            "result": (last.unsqueeze(0), filename),
        }


NODE_CLASS_MAPPINGS = {
    "SaveVideoLastFrame": SaveVideoLastFrame,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveVideoLastFrame": "Save Video Last Frame (to input)",
}
