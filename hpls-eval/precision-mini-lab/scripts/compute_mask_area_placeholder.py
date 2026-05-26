#!/usr/bin/env python3
"""Placeholder utility for Precision Mini-Lab mask-area logging.

This script is intentionally small and conservative. It does not run inference,
does not create predictions, and does not fabricate precision results. Use it
only on prediction masks that were produced by a documented FP32 / FP16 / INT8
runtime setup.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Precision Mini-Lab mask-area placeholder.")
    parser.add_argument("--note", action="store_true", help="Print the intended usage note.")
    args = parser.parse_args()

    print("Precision Mini-Lab mask-area placeholder")
    print("No inference is performed and no metrics are fabricated.")
    print("Attach real prediction-mask files and measured logs before using this as evidence.")
    if args.note:
        print("Suggested fields: case_id, precision_mode, mask_area_pixels, reference_area_pixels, mask_area_ratio.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
