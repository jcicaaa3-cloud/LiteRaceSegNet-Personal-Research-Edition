#!/usr/bin/env python3
"""
Compute segmentation-output stability metrics between a reference mask and a target mask.

This helper is intended for the LiteRaceSegNet v15.2 HPLS-Eval / Precision Mini-Lab
research-extension layer. It compares binary target masks against a reference mask,
usually an FP32 output mask.

It does not perform clinical validation, diagnostic evaluation, or deployment certification.

Dependencies:
  - Python 3.9+
  - numpy
  - pillow

Example:
  python compute_output_stability_metrics_v15_2.py \
    --ref-mask cases/case-001/predictions/fp32_reference_mask.png \
    --target-mask cases/case-001/predictions/int8_target_mask.png \
    --case-id case-001 \
    --experiment-id PML-INT8-CPU-ORT-CS01-001 \
    --output-json cases/case-001/metrics/PML-INT8-CPU-ORT-CS01-001_metrics.json
"""

from __future__ import annotations

import argparse
import json
import math
from collections import deque
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import numpy as np
from PIL import Image


def load_binary_mask(path: Path, threshold: int = 128) -> np.ndarray:
    """Load a grayscale image as a boolean foreground mask."""
    if not path.exists():
        raise FileNotFoundError(f"Mask not found: {path}")
    img = Image.open(path).convert("L")
    arr = np.asarray(img)
    return arr >= threshold


def resize_mask_nearest(mask: np.ndarray, size_hw: Tuple[int, int]) -> np.ndarray:
    """Resize a boolean mask to (height, width) using nearest-neighbor interpolation."""
    h, w = size_hw
    img = Image.fromarray((mask.astype(np.uint8) * 255), mode="L")
    resized = img.resize((w, h), resample=Image.Resampling.NEAREST)
    return np.asarray(resized) >= 128


def iou(a: np.ndarray, b: np.ndarray) -> Optional[float]:
    """Intersection-over-union for boolean masks. Returns None if both masks are empty."""
    inter = np.logical_and(a, b).sum(dtype=np.int64)
    union = np.logical_or(a, b).sum(dtype=np.int64)
    if union == 0:
        return None
    return float(inter / union)


def erode_3x3(mask: np.ndarray) -> np.ndarray:
    """Binary erosion with a 3x3 square structuring element using numpy only."""
    padded = np.pad(mask, 1, mode="constant", constant_values=False)
    out = np.ones_like(mask, dtype=bool)
    for dy in range(3):
        for dx in range(3):
            out &= padded[dy:dy + mask.shape[0], dx:dx + mask.shape[1]]
    return out


def dilate_3x3(mask: np.ndarray, iterations: int = 1) -> np.ndarray:
    """Binary dilation with a 3x3 square structuring element using numpy only."""
    out = mask.astype(bool)
    for _ in range(max(0, iterations)):
        padded = np.pad(out, 1, mode="constant", constant_values=False)
        new = np.zeros_like(out, dtype=bool)
        for dy in range(3):
            for dx in range(3):
                new |= padded[dy:dy + out.shape[0], dx:dx + out.shape[1]]
        out = new
    return out


def boundary_mask(mask: np.ndarray) -> np.ndarray:
    """Return a one-pixel-ish inner boundary mask."""
    if not mask.any():
        return np.zeros_like(mask, dtype=bool)
    return np.logical_and(mask, np.logical_not(erode_3x3(mask)))


def boundary_iou(ref: np.ndarray, target: np.ndarray, radius: int = 1) -> Optional[float]:
    """Tolerant boundary IoU using dilated boundary masks."""
    b_ref = boundary_mask(ref)
    b_tgt = boundary_mask(target)
    if radius > 0:
        b_ref = dilate_3x3(b_ref, iterations=radius)
        b_tgt = dilate_3x3(b_tgt, iterations=radius)
    return iou(b_ref, b_tgt)


def connected_components_count(mask: np.ndarray) -> int:
    """Count 8-connected components in a binary mask without scipy/skimage."""
    h, w = mask.shape
    visited = np.zeros_like(mask, dtype=bool)
    count = 0
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]
    ys, xs = np.where(mask)
    foreground = set(zip(ys.tolist(), xs.tolist()))
    for start in list(foreground):
        y0, x0 = start
        if visited[y0, x0] or not mask[y0, x0]:
            continue
        count += 1
        q: deque[Tuple[int, int]] = deque([(y0, x0)])
        visited[y0, x0] = True
        while q:
            y, x = q.popleft()
            for dy, dx in neighbors:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not visited[ny, nx]:
                    visited[ny, nx] = True
                    q.append((ny, nx))
    return count


def centroid(mask: np.ndarray) -> Optional[Tuple[float, float]]:
    """Return (x, y) centroid of foreground pixels, or None if mask is empty."""
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return None
    return float(xs.mean()), float(ys.mean())


def safe_round(value: Optional[float], digits: int = 6) -> Optional[float]:
    if value is None or not np.isfinite(value):
        return None
    return round(float(value), digits)


def compute_metrics(
    ref: np.ndarray,
    target: np.ndarray,
    *,
    boundary_radius: int,
) -> Dict[str, Any]:
    if ref.shape != target.shape:
        raise ValueError(f"Mask shapes differ: ref={ref.shape}, target={target.shape}")

    h, w = ref.shape
    diag = math.sqrt(h * h + w * w)
    eps = 1e-9

    area_ref = int(ref.sum(dtype=np.int64))
    area_target = int(target.sum(dtype=np.int64))
    area_drift = area_target - area_ref
    area_drift_pct = 100.0 * area_drift / max(area_ref, eps)

    mask_iou = iou(ref, target)
    b_iou = boundary_iou(ref, target, radius=boundary_radius)

    cc_ref = connected_components_count(ref)
    cc_target = connected_components_count(target)

    c_ref = centroid(ref)
    c_target = centroid(target)
    if c_ref is None or c_target is None:
        centroid_shift_px = None
        centroid_shift_norm = None
    else:
        centroid_shift_px = math.sqrt((c_ref[0] - c_target[0]) ** 2 + (c_ref[1] - c_target[1]) ** 2)
        centroid_shift_norm = centroid_shift_px / diag if diag > 0 else None

    target_only = np.logical_and(target, np.logical_not(ref))
    reference_only = np.logical_and(ref, np.logical_not(target))

    return {
        "image_height": h,
        "image_width": w,
        "mask_area_ref_px": area_ref,
        "mask_area_target_px": area_target,
        "mask_area_drift_px": area_drift,
        "mask_area_drift_pct": safe_round(area_drift_pct),
        "mask_iou_against_ref": safe_round(mask_iou),
        "mask_iou_drift": safe_round(None if mask_iou is None else 1.0 - mask_iou),
        "boundary_iou_against_ref": safe_round(b_iou),
        "boundary_iou_drift": safe_round(None if b_iou is None else 1.0 - b_iou),
        "boundary_tolerance_px": boundary_radius,
        "connected_components_ref": cc_ref,
        "connected_components_target": cc_target,
        "connected_component_delta": cc_target - cc_ref,
        "centroid_ref_x": safe_round(None if c_ref is None else c_ref[0]),
        "centroid_ref_y": safe_round(None if c_ref is None else c_ref[1]),
        "centroid_target_x": safe_round(None if c_target is None else c_target[0]),
        "centroid_target_y": safe_round(None if c_target is None else c_target[1]),
        "centroid_shift_px": safe_round(centroid_shift_px),
        "centroid_shift_norm": safe_round(centroid_shift_norm),
        "target_only_region_area_px": int(target_only.sum(dtype=np.int64)),
        "reference_only_region_area_px": int(reference_only.sum(dtype=np.int64)),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute output-stability metrics for two segmentation masks.")
    parser.add_argument("--ref-mask", required=True, type=Path, help="Reference binary/grayscale mask path, usually FP32 output.")
    parser.add_argument("--target-mask", required=True, type=Path, help="Target binary/grayscale mask path, such as FP16 or INT8 output.")
    parser.add_argument("--threshold", type=int, default=128, help="Threshold for converting grayscale masks to binary foreground.")
    parser.add_argument("--boundary-radius", type=int, default=1, help="Tolerance radius in pixels for boundary IoU.")
    parser.add_argument("--resize-target-nearest", action="store_true", help="Resize target mask to reference shape using nearest-neighbor interpolation if shapes differ.")
    parser.add_argument("--case-id", default="TBD", help="Case ID to store in JSON output.")
    parser.add_argument("--experiment-id", default="TBD", help="Experiment ID to store in JSON output.")
    parser.add_argument("--reference-precision", default="FP32", help="Reference precision label.")
    parser.add_argument("--target-precision", default="TBD", help="Target precision label.")
    parser.add_argument("--runtime-backend", default="TBD", help="Runtime backend label for target path.")
    parser.add_argument("--fallback-status", default="TBD", help="Fallback status: none, fallback_detected, unknown, unsupported, TBD.")
    parser.add_argument("--output-json", type=Path, help="Optional output JSON path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ref = load_binary_mask(args.ref_mask, threshold=args.threshold)
    target = load_binary_mask(args.target_mask, threshold=args.threshold)

    resize_policy = "none"
    if ref.shape != target.shape:
        if not args.resize_target_nearest:
            raise ValueError(
                f"Mask shapes differ: ref={ref.shape}, target={target.shape}. "
                "Use --resize-target-nearest to resize target mask to reference shape."
            )
        target = resize_mask_nearest(target, ref.shape)
        resize_policy = "target_resized_to_reference_nearest"

    metrics = compute_metrics(ref, target, boundary_radius=args.boundary_radius)
    result = {
        "case_id": args.case_id,
        "experiment_id": args.experiment_id,
        "reference": {
            "mask_path": str(args.ref_mask),
            "precision": args.reference_precision,
        },
        "target": {
            "mask_path": str(args.target_mask),
            "precision": args.target_precision,
            "runtime_backend": args.runtime_backend,
            "fallback_status": args.fallback_status,
        },
        "threshold": args.threshold,
        "resize_policy": resize_policy,
        "metrics": metrics,
        "claim_boundary": "case-level pilot observation only unless expanded with documented case-set evidence",
    }

    text = json.dumps(result, indent=2, ensure_ascii=False)
    print(text)

    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
