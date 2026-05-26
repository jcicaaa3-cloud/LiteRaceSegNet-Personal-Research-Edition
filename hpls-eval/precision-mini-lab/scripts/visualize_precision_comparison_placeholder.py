#!/usr/bin/env python3
"""Placeholder for static precision-comparison visualization.

This script does not perform real inference and does not create fake output
masks. It is a reminder that visual comparisons must be built from existing,
measured FP32 / FP16 / INT8 predictions.
"""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Precision Mini-Lab visualization placeholder.")
    parser.add_argument("--case-id", default="case-XXX", help="Case ID to mention in the placeholder message.")
    args = parser.parse_args()

    print(f"Visualization placeholder for {args.case_id}")
    print("Static portfolio preview only. No real inference is performed in this page or script.")
    print("Use measured predictions only: fp32, fp16, int8, overlays, boundary-diff maps, and metric logs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
