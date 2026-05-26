# Output Stability Metrics

**Scope:** mask-level comparison between a reference segmentation output and a target segmentation output  
**Primary use:** Precision Mini-Lab FP32 / FP16 / INT8 pilot and HPLS-Eval hardware/runtime shift analysis

---

## 1. Notation

Let:

```text
M_ref = binary reference mask, usually FP32 output
M_tgt = binary target mask, such as FP16 or INT8 output
G     = optional ground-truth mask, if available
H, W  = image height and width
eps   = small constant to avoid division by zero
```

The reference mask is not automatically ground truth. It is the anchor for output-stability comparison.

All masks must have the same resolution before metric calculation. If resizing is required, record the resize method.

---

## 2. Required metrics

### 2.1 Mask area

```text
A_ref = sum(M_ref)
A_tgt = sum(M_tgt)
```

`sum()` counts foreground pixels.

### 2.2 Mask area drift

Absolute drift:

```text
mask_area_drift_px = A_tgt - A_ref
```

Relative drift:

```text
mask_area_drift_pct = 100 * (A_tgt - A_ref) / max(A_ref, eps)
```

Interpretation:

- positive drift means target foreground area increased;
- negative drift means target foreground area decreased;
- very small `A_ref` can make percentage drift unstable, so report absolute drift too.

### 2.3 Mask IoU against reference

```text
mask_iou_against_ref = intersection(M_ref, M_tgt) / union(M_ref, M_tgt)
```

If both masks are empty, record `not_applicable` or `1.0_empty_agreement`, depending on the reporting policy. Do not hide empty-mask cases.

### 2.4 Mask IoU drift

```text
mask_iou_drift = 1 - mask_iou_against_ref
```

Higher drift means less agreement with the reference output.

### 2.5 Boundary mask

A simple boundary can be extracted as:

```text
B(M) = M AND NOT erosion(M)
```

A tolerance radius may be applied by dilating boundaries before comparison.

### 2.6 Boundary IoU against reference

```text
boundary_iou_against_ref = IoU(dilate(B(M_ref), r), dilate(B(M_tgt), r))
```

where `r` is the boundary tolerance radius in pixels. Record the radius.

### 2.7 Boundary IoU drift

```text
boundary_iou_drift = 1 - boundary_iou_against_ref
```

Boundary IoU drift is useful because two masks can have similar area but different contours.

### 2.8 Connected component count

Using 8-connectivity unless otherwise specified:

```text
cc_ref = number_of_connected_components(M_ref)
cc_tgt = number_of_connected_components(M_tgt)
cc_delta = cc_tgt - cc_ref
```

Interpretation:

- positive delta may indicate fragmentation or new noise components;
- negative delta may indicate merge or disappearance of small components.

### 2.9 Centroid shift

Foreground centroid:

```text
C(M) = mean coordinates of foreground pixels in M
```

Centroid shift:

```text
centroid_shift_px = EuclideanDistance(C(M_ref), C(M_tgt))
```

If either mask is empty, record `not_applicable` and explain why.

Recommended normalized form:

```text
centroid_shift_norm = centroid_shift_px / sqrt(H^2 + W^2)
```

### 2.10 Target-only and reference-only regions

Target-only region:

```text
R_target_only = M_tgt AND NOT M_ref
```

Reference-only region:

```text
R_reference_only = M_ref AND NOT M_tgt
```

Record:

```text
target_only_region_area_px = sum(R_target_only)
reference_only_region_area_px = sum(R_reference_only)
```

Interpretation:

- target-only region approximates output expansion relative to reference;
- reference-only region approximates output loss relative to reference.

These are not the same as false positives and false negatives against ground truth unless `G` is used.

---

## 3. Optional ground-truth metrics

If a ground-truth mask `G` is available, report conventional metrics separately:

- IoU against ground truth;
- Dice/F1 against ground truth;
- precision and recall against ground truth;
- false-positive pixels against ground truth;
- false-negative pixels against ground truth.

Do not mix ground-truth metrics with FP32-reference stability metrics.

Recommended naming:

```text
mask_iou_against_ref
mask_iou_against_gt
fp_region_area_against_ref
fp_region_area_against_gt
```

---

## 4. Recommended qualitative observation fields

| Field | Values or notes |
|---|---|
| `visible_boundary_drift` | none, mild, moderate, severe, TBD |
| `boundary_thickening` | yes/no/TBD |
| `boundary_erosion` | yes/no/TBD |
| `small_region_loss` | yes/no/TBD |
| `small_region_fragmentation` | yes/no/TBD |
| `new_noise_components` | yes/no/TBD |
| `large_target_only_region` | yes/no/TBD |
| `large_reference_only_region` | yes/no/TBD |
| `drift_location` | edge, center, shadow region, reflective region, texture region, unknown |
| `human_review_note` | short visual description |

Qualitative labels should not replace numeric metrics.

---

## 5. Runtime and fallback metrics

Output stability must be interpreted with runtime evidence.

Required runtime fields:

| Field | Example |
|---|---|
| `runtime_backend` | PyTorch, ONNX Runtime, TensorRT, OpenVINO, vendor runtime |
| `execution_provider` | CPU, CUDA, TensorRT, OpenVINO CPU, OpenVINO NPU, etc. |
| `hardware_lane` | CPU, GPU, possible NPU, possible TPU |
| `precision_mode_requested` | FP32, FP16, INT8 |
| `precision_mode_verified` | FP32, FP16, INT8, mixed, unknown |
| `fallback_status` | none, fallback_detected, unknown, unsupported |
| `model_format` | `.pt`, `.onnx`, TensorRT engine, OpenVINO IR, etc. |
| `calibration_status` | not_applicable, static_int8, dynamic_int8, unknown |

Latency fields are optional:

- `latency_mean_ms`;
- `latency_median_ms`;
- `latency_p95_ms`;
- `num_warmup_runs`;
- `num_timed_runs`.

Latency should not be reported from a single unverified run as a benchmark.

---

## 6. Summary statistics for a case set

For a small case set, report:

- number of cases;
- median mask area drift percentage;
- maximum absolute mask area drift percentage;
- median mask IoU against reference;
- minimum mask IoU against reference;
- median boundary IoU against reference;
- minimum boundary IoU against reference;
- number of cases with component count change;
- number of cases with centroid shift above threshold;
- number of cases with fallback detected.

Report domain-tag breakdown only when the case count is sufficient to make the breakdown meaningful.

---

## 7. Suggested result-table columns

```text
result_id
experiment_id
case_id
case_domain_tags
reference_precision
target_precision
model_format
runtime_backend
execution_provider
hardware_lane
threshold
resize_policy
mask_area_ref_px
mask_area_target_px
mask_area_drift_px
mask_area_drift_pct
mask_iou_against_ref
mask_iou_drift
boundary_iou_against_ref
boundary_iou_drift
boundary_tolerance_px
connected_components_ref
connected_components_target
connected_component_delta
centroid_ref_x
centroid_ref_y
centroid_target_x
centroid_target_y
centroid_shift_px
centroid_shift_norm
target_only_region_area_px
reference_only_region_area_px
fallback_status
evidence_level
notes
```

---

## 8. Interpretation rules

1. Do not call the target output “wrong” solely because it differs from FP32. Use ground truth if correctness is being judged.
2. Do not call a model hardware-stable unless multiple documented hardware lanes have been measured.
3. Do not claim INT8 stability if INT8 fallback status is unknown.
4. Report both absolute and relative area drift.
5. Use boundary metrics for thin or irregular damage regions.
6. Preserve empty-mask cases instead of silently dropping them.
7. Keep qualitative observations separate from measured metrics.

---

## 9. Minimal JSON schema

A metric JSON file may use this structure:

```json
{
  "result_id": "TBD",
  "experiment_id": "TBD",
  "case_id": "TBD",
  "reference": {
    "mask_path": "TBD",
    "precision": "FP32",
    "runtime_backend": "TBD"
  },
  "target": {
    "mask_path": "TBD",
    "precision": "TBD",
    "runtime_backend": "TBD",
    "fallback_status": "TBD"
  },
  "metrics": {
    "mask_area_ref_px": "TBD",
    "mask_area_target_px": "TBD",
    "mask_area_drift_px": "TBD",
    "mask_area_drift_pct": "TBD",
    "mask_iou_against_ref": "TBD",
    "boundary_iou_against_ref": "TBD",
    "boundary_iou_drift": "TBD",
    "connected_components_ref": "TBD",
    "connected_components_target": "TBD",
    "connected_component_delta": "TBD",
    "centroid_shift_px": "TBD",
    "target_only_region_area_px": "TBD",
    "reference_only_region_area_px": "TBD"
  },
  "claim_boundary": "case-level pilot observation only"
}
```
