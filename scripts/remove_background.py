#!/usr/bin/env python3
"""Remove the green-screen background from an image in app/assets/images."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "app/assets/images"

# Chroma-key thresholds: how much greener than R/B a pixel must be.
HARD_GREEN = 36
SOFT_GREEN = 14
GREEN_HUE_MIN = 50
GREEN_HUE_MAX = 105
SCREEN_SAT = 100
SOFT_SAT = 75


def greenness(r: int, g: int, b: int) -> int:
    return g - max(r, b)


def clamp(value: int) -> int:
    return max(0, min(255, value))


def key_alpha(r: int, g: int, b: int, h: int, s: int, v: int) -> int:
    score = greenness(r, g, b)
    # Keep dark leather and shadows even when they pick up a green cast.
    if max(r, g, b) < 110 and score < 25:
        return 255
    if v < 55 and s < 90:
        return 255

    hue_green = GREEN_HUE_MIN <= h <= GREEN_HUE_MAX

    if hue_green and s >= SCREEN_SAT and v >= 50:
        return 0
    if g > 80 and score >= HARD_GREEN and s >= SOFT_SAT:
        return 0

    rgb_alpha = 255
    if score > SOFT_GREEN and s >= SOFT_SAT:
        t = (score - SOFT_GREEN) / (HARD_GREEN - SOFT_GREEN)
        rgb_alpha = int(255 * (1.0 - t))

    hue_alpha = 255
    if hue_green and s > SOFT_SAT and v > 45:
        t = (s - SOFT_SAT) / (SCREEN_SAT - SOFT_SAT)
        hue_alpha = int(255 * (1.0 - t))

    return clamp(min(rgb_alpha, hue_alpha))


def despill(r: int, g: int, b: int, h: int, s: int, alpha: int) -> tuple[int, int, int]:
    if alpha == 0:
        return r, g, b
    max_rb = max(r, b)
    pull = 0.85
    if GREEN_HUE_MIN <= h <= GREEN_HUE_MAX:
        pull = 0.95
    if g > max_rb:
        g = int(g - (g - max_rb) * pull)
    if s > 20 and GREEN_HUE_MIN <= h <= GREEN_HUE_MAX:
        # Shift leftover green toward the neighbor luminance.
        g = int((g + max_rb) / 2)
    return r, clamp(g), b


def remove_green_screen(src: Path, dst: Path) -> Path:
    image = Image.open(src).convert("RGBA")
    hsv = image.convert("RGB").convert("HSV")
    rgba_bytes = bytearray(image.tobytes())
    hsv_bytes = hsv.tobytes()

    for i in range(image.size[0] * image.size[1]):
        rgba_i = i * 4
        hsv_i = i * 3
        r, g, b = rgba_bytes[rgba_i], rgba_bytes[rgba_i + 1], rgba_bytes[rgba_i + 2]
        h, s, v = hsv_bytes[hsv_i], hsv_bytes[hsv_i + 1], hsv_bytes[hsv_i + 2]
        alpha = key_alpha(r, g, b, h, s, v)
        r, g, b = despill(r, g, b, h, s, alpha)
        rgba_bytes[rgba_i] = r
        rgba_bytes[rgba_i + 1] = g
        rgba_bytes[rgba_i + 2] = b
        rgba_bytes[rgba_i + 3] = alpha

    keyed = Image.frombytes("RGBA", image.size, bytes(rgba_bytes))
    rgb = keyed.convert("RGB")
    alpha = keyed.getchannel("A").filter(ImageFilter.MinFilter(3))
    alpha = alpha.filter(ImageFilter.GaussianBlur(radius=0.6))
    rgb.putalpha(alpha)

    dst.parent.mkdir(parents=True, exist_ok=True)
    rgb.save(dst, "PNG")
    return dst


def image_filename(value: str) -> Path:
    filename = Path(value).name
    if not filename or filename in {".", ".."}:
        raise argparse.ArgumentTypeError("informe apenas o nome do arquivo")
    return IMAGES_DIR / filename


def default_output(src: Path) -> Path:
    return IMAGES_DIR / f"{src.stem}_no_bg.png"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "src",
        type=image_filename,
        help="nome do arquivo de entrada em app/assets/images",
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=image_filename,
        help="nome do arquivo de saída; padrão: <entrada>_no_bg.png",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = args.output or default_output(args.src)
    output = remove_green_screen(args.src, output_path)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
