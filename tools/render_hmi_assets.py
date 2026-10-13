#!/usr/bin/env python3
"""Build PNGs from versioned UCS SVG sources.
Preview contains demo labels; use BACKGROUND ONLY for EBPro picture layers.
Run: python -m pip install cairosvg; python tools/render_hmi_assets.py
"""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"designs/resource-manager"

def main():
    try:
        import cairosvg
    except ImportError as exc:
        raise SystemExit("Install cairosvg: python -m pip install cairosvg") from exc
    names=("resource-manager-light","resource-manager-background-only")
    for name in names:
        src=DIR/f"{name}.svg"
        dst=DIR/f"{name}.png"
        cairosvg.svg2png(url=str(src),write_to=str(dst),output_width=1600,output_height=900)
        print(f"Rendered {dst.relative_to(ROOT)}")

if __name__=="__main__":
    main()
