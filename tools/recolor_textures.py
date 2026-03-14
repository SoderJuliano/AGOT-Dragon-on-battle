#!/usr/bin/env python3
"""
Dragon on Battle — Dragon Rider's Plate Texture Recolor
=======================================================
Converts Valyrian Blackfyre armor textures to a polished steel + gold palette:
  - Neutral dark areas  (original Blackfyre black)  → polished blue-grey steel
  - Warm/red accent areas (original Blackfyre crimson) → rich dark gold

Writes output as uncompressed RGBA8 DDS (accepted by CK3).

Usage:
    python3 recolor_textures.py
"""

import struct, os, sys
import numpy as np
from PIL import Image

# ──────────────────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────────────────
AGOT = "/home/julianosoder/Downloads/AGOT/CK3AGOT-45-0-4-27-1771613315/AGOT"
MOD  = "/home/julianosoder/Documentos/AGOT - Dragon on battle"

BODY_SRC  = f"{AGOT}/gfx/models/portraits/m_clothes/agot/valyrian/war_02/valyrian_blackfyre_02_diffuse.dds"
HEAD_SRC  = f"{AGOT}/gfx/models/portraits/m_headgear/agot/valyrian/war_03_high/male_headgear_secular_valyrian_war_blackfyre_03_high_diffuse.dds"

BODY_DST  = f"{MOD}/gfx/models/portraits/m_clothes/agot/valyrian/war_02/dob_dragon_rider_body_diffuse.dds"
HEAD_DST  = f"{MOD}/gfx/models/portraits/m_headgear/agot/valyrian/war_03_high/dob_dragon_rider_headgear_diffuse.dds"

os.makedirs(os.path.dirname(BODY_DST), exist_ok=True)
os.makedirs(os.path.dirname(HEAD_DST), exist_ok=True)


# ──────────────────────────────────────────────────────────────────────────────
# DDS Writer: Uncompressed RGBA8
# ──────────────────────────────────────────────────────────────────────────────
def write_dds_rgba8(path: str, arr: np.ndarray):
    """
    Write a numpy RGBA uint8 array as an uncompressed RGBA8 DDS file.
    CK3 accepts uncompressed DDS — larger than DXT5 but fully compatible.
    """
    h, w = arr.shape[:2]
    assert arr.shape[2] == 4, "Expected RGBA array"
    assert arr.dtype == np.uint8

    DDSD_CAPS         = 0x00000001
    DDSD_HEIGHT       = 0x00000002
    DDSD_WIDTH        = 0x00000004
    DDSD_PITCH        = 0x00000008
    DDSD_PIXELFORMAT  = 0x00001000
    flags = DDSD_CAPS | DDSD_HEIGHT | DDSD_WIDTH | DDSD_PITCH | DDSD_PIXELFORMAT

    DDPF_ALPHAPIXELS  = 0x00000001
    DDPF_RGB          = 0x00000040
    pf_flags = DDPF_ALPHAPIXELS | DDPF_RGB

    DDSCAPS_TEXTURE   = 0x00001000
    pitch             = w * 4   # 4 bytes per pixel

    with open(path, 'wb') as f:
        f.write(b'DDS ')                        # magic
        f.write(struct.pack('<I', 124))          # dwSize of header
        f.write(struct.pack('<I', flags))
        f.write(struct.pack('<I', h))
        f.write(struct.pack('<I', w))
        f.write(struct.pack('<I', pitch))        # dwPitchOrLinearSize
        f.write(struct.pack('<I', 0))            # dwDepth
        f.write(struct.pack('<I', 1))            # dwMipMapCount (1 = no mipmaps)
        f.write(b'\x00' * 44)                   # dwReserved1[11]
        # DDS_PIXELFORMAT (32 bytes)
        f.write(struct.pack('<I', 32))           # dwSize
        f.write(struct.pack('<I', pf_flags))
        f.write(struct.pack('<I', 0))            # dwFourCC (0 = uncompressed)
        f.write(struct.pack('<I', 32))           # dwRGBBitCount
        f.write(struct.pack('<I', 0x000000FF))   # dwRBitMask
        f.write(struct.pack('<I', 0x0000FF00))   # dwGBitMask
        f.write(struct.pack('<I', 0x00FF0000))   # dwBBitMask
        f.write(struct.pack('<I', 0xFF000000))   # dwABitMask
        # Caps
        f.write(struct.pack('<I', DDSCAPS_TEXTURE))
        f.write(struct.pack('<I', 0))            # dwCaps2
        f.write(struct.pack('<I', 0))            # dwCaps3
        f.write(struct.pack('<I', 0))            # dwCaps4
        f.write(struct.pack('<I', 0))            # dwReserved2
        # Pixel data (RGBA8, top→bottom, left→right)
        f.write(arr.tobytes())

    size_kb = os.path.getsize(path) // 1024
    print(f"  Saved: {path}  ({w}×{h}, {size_kb} KB)")


# ──────────────────────────────────────────────────────────────────────────────
# Color Transform: Blackfyre → Polished Steel + Gold
# ──────────────────────────────────────────────────────────────────────────────
def recolor_blackfyre_to_steel_gold(arr: np.ndarray) -> np.ndarray:
    """
    Per-pixel transformation:
      - Neutral dark pixels (original Blackfyre black)    → polished steel grey-blue
      - Warm/red pixels     (original Blackfyre crimson)  → rich dark gold
      - Blend determined by how dominant the red channel is vs green+blue
      - Slight overall brightness boost to simulate polished sheen
    """
    rgb  = arr[:, :, :3].astype(np.float32)
    alpha = arr[:, :, 3:4]                       # keep alpha unchanged

    R, G, B = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]

    # ── Colorimetric analysis ────────────────────────────────────────────────
    brightness  = np.maximum(np.maximum(R, G), B)           # 0–255
    # "redness": how much R exceeds the dominant cool channel
    redness     = (R - np.maximum(G, B)).astype(np.float32)  # can be negative

    # Weight: 0 = pure steel, 1 = pure gold
    # Starts blending when redness > 5, fully gold when redness > 50
    redness_w   = np.clip((redness - 5.0) / 45.0, 0.0, 1.0)

    # ── Steel target colour (cool blue-grey, slightly boosted) ───────────────
    # brightness preserved proportionally; cool channel (B) amplified
    steel_R = brightness * 0.75 + 38.0     # slightly cool-shifted R
    steel_G = brightness * 0.80 + 40.0
    steel_B = brightness * 0.92 + 47.0     # boosted blue for cold steel

    # ── Gold target colour (warm, slightly elevated) ─────────────────────────
    gold_R  = brightness * 0.85 + 55.0     # rich warm red component
    gold_G  = brightness * 0.65 + 42.0     # moderate green
    gold_B  = brightness * 0.04 + 7.0      # very little blue for gold

    # ── Per-channel blend ────────────────────────────────────────────────────
    w      = redness_w                     # (H, W) array
    out_R  = steel_R * (1 - w) + gold_R * w
    out_G  = steel_G * (1 - w) + gold_G * w
    out_B  = steel_B * (1 - w) + gold_B * w

    # ── Polish sheen: subtle highlight on the brightest areas ────────────────
    # Simulate specular micro-variation: push highlights up a touch
    sheen  = np.clip((brightness / 255.0) ** 0.65, 0.0, 1.0) * 14.0   # 0–14 extra
    out_R  = out_R + sheen
    out_G  = out_G + sheen * 0.95
    out_B  = out_B + sheen * 0.90                                        # steel stays cool

    # ── Clamp and pack ───────────────────────────────────────────────────────
    out_R  = np.clip(out_R, 0, 255).astype(np.uint8)
    out_G  = np.clip(out_G, 0, 255).astype(np.uint8)
    out_B  = np.clip(out_B, 0, 255).astype(np.uint8)

    result = np.dstack([out_R, out_G, out_B, alpha[:,:,0]])
    return result.astype(np.uint8)


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────
def process(src: str, dst: str, label: str):
    print(f"\n[{label}]")
    print(f"  Reading : {src}")
    img = Image.open(src)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    arr = np.array(img)

    # Quick stats before
    rgb = arr[:,:,:3].astype(np.float32)
    print(f"  Before → median brightness={np.median(rgb.max(axis=2)):.1f}  "
          f"median redness={np.median(rgb[:,:,0]-np.maximum(rgb[:,:,1],rgb[:,:,2])):.1f}")

    out = recolor_blackfyre_to_steel_gold(arr)

    rgb2 = out[:,:,:3].astype(np.float32)
    print(f"  After  → median brightness={np.median(rgb2.max(axis=2)):.1f}  "
          f"R/G/B mean={rgb2[:,:,0].mean():.0f}/{rgb2[:,:,1].mean():.0f}/{rgb2[:,:,2].mean():.0f}")

    write_dds_rgba8(dst, out)


if __name__ == '__main__':
    process(BODY_SRC, BODY_DST, "Body Armor")
    process(HEAD_SRC, HEAD_DST, "Headgear")
    print("\nDone. Both recolored textures written.")
