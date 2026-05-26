#!/usr/bin/env python3
"""Placeholder utility for future boundary-metric logging.

This file exists to document the intended metric boundary. It does not claim a
validated Boundary IoU / Boundary F1 protocol until the protocol, masks, logs,
and implementation details are supplied.
"""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(description="Precision Mini-Lab boundary-metric placeholder.")
    parser.add_argument("--case-id", default="case-XXX", help="Case ID to mention in the placeholder message.")
    args = parser.parse_args()

    print(f"Boundary metrics placeholder for {args.case_id}")
    print("No boundary metric is computed here yet.")
    print("Define the dilation radius, thresholding policy, ground-truth availability, and runtime logs before recording evidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
