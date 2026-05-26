# Precision Mini-Lab Result Template

Use this template for each measured Precision Mini-Lab result. Leave unknown fields as `TBD`. Do not infer or guess numeric values.

---

## 1. Result metadata

| Field | Value |
|---|---|
| Result ID | TBD |
| Experiment ID | TBD |
| Case ID | TBD |
| Case set ID | TBD |
| Date | TBD |
| Operator / author | TBD |
| Repository/package version | LiteRaceSegNet v15.2 Personal Research Edition |
| Evidence level | Level 0 / Level 1 / Level 2 / Level 3 / Level 4 |
| Result status | planned / incomplete / measured_case / measured_case_set / fallback_detected / unsupported / future_protocol |

---

## 2. Claim-boundary banner

```text
This result is part of the HPLS-Eval / Precision Mini-Lab research extension.
It is a segmentation-output stability observation under the documented model, input, runtime backend, precision mode, threshold, and hardware path.
It does not replace the original LiteRaceSegNet thesis/capstone claim and does not claim clinical validation, diagnostic evidence, deployment readiness, or complete quantization benchmarking.
```

---

## 3. Model and runtime metadata

| Field | Reference path | Target path |
|---|---|---|
| Model identifier | TBD | TBD |
| Checkpoint/export path | TBD | TBD |
| Model format | TBD | TBD |
| Precision mode requested | FP32 | TBD |
| Precision mode verified | TBD | TBD |
| Runtime backend | TBD | TBD |
| Execution provider | TBD | TBD |
| Hardware lane | CPU/GPU/etc. TBD | CPU/GPU/NPU/TPU/etc. TBD |
| Device name | TBD | TBD |
| Input resolution | TBD | TBD |
| Output resolution | TBD | TBD |
| Threshold policy | TBD | TBD |
| Resize policy | TBD | TBD |
| Fallback status | TBD | TBD |
| Runtime/conversion log path | TBD | TBD |

---

## 4. INT8 calibration metadata

Complete this section only for INT8 or quantized target paths.

| Field | Value |
|---|---|
| Quantization method | dynamic / static / PTQ / QAT / TensorRT calibration / OpenVINO / other / TBD |
| Calibration dataset ID | TBD |
| Number of calibration cases | TBD |
| Calibration preprocessing | TBD |
| Calibration/evaluation overlap | yes / no / TBD |
| Converter/runtime version | TBD |
| Unsupported operation notes | TBD |
| Fallback notes | TBD |

---

## 5. Case metadata

| Field | Value |
|---|---|
| Input image path | TBD |
| Ground-truth mask path, if available | TBD / not_available |
| Case domain tags | small / medium / large / thin / noisy / shadow / wet / low_contrast / etc. |
| Damage-size category | TBD |
| Lighting condition | TBD |
| Surface condition | TBD |
| Camera/resolution note | TBD |
| Privacy/provenance status | reviewed / needs_review / TBD |

---

## 6. Output artifacts

| Artifact | Path |
|---|---|
| FP32 reference mask | TBD |
| Target mask | TBD |
| Difference overlay | TBD |
| Boundary overlay | TBD |
| Metric JSON | TBD |
| Runtime log | TBD |
| Conversion/calibration log | TBD |
| Notes file | TBD |

---

## 7. Output-stability metrics

| Metric | Value | Notes |
|---|---:|---|
| `mask_area_ref_px` | TBD | foreground pixels in reference mask |
| `mask_area_target_px` | TBD | foreground pixels in target mask |
| `mask_area_drift_px` | TBD | target minus reference |
| `mask_area_drift_pct` | TBD | percent relative to reference area |
| `mask_iou_against_ref` | TBD | IoU between reference and target masks |
| `mask_iou_drift` | TBD | `1 - mask_iou_against_ref` |
| `boundary_iou_against_ref` | TBD | boundary IoU with stated radius |
| `boundary_iou_drift` | TBD | `1 - boundary_iou_against_ref` |
| `boundary_tolerance_px` | TBD | radius used for boundary comparison |
| `connected_components_ref` | TBD | 8-connected unless noted |
| `connected_components_target` | TBD | 8-connected unless noted |
| `connected_component_delta` | TBD | target minus reference |
| `centroid_ref_x` | TBD | x coordinate |
| `centroid_ref_y` | TBD | y coordinate |
| `centroid_target_x` | TBD | x coordinate |
| `centroid_target_y` | TBD | y coordinate |
| `centroid_shift_px` | TBD | Euclidean shift |
| `centroid_shift_norm` | TBD | normalized by image diagonal |
| `target_only_region_area_px` | TBD | target foreground not in reference |
| `reference_only_region_area_px` | TBD | reference foreground missing from target |

---

## 8. Optional ground-truth metrics

Use only if a ground-truth mask exists.

| Metric | Reference path | Target path | Notes |
|---|---:|---:|---|
| IoU against ground truth | TBD | TBD | optional |
| Dice/F1 against ground truth | TBD | TBD | optional |
| Precision against ground truth | TBD | TBD | optional |
| Recall against ground truth | TBD | TBD | optional |
| False-positive area against ground truth | TBD | TBD | optional |
| False-negative area against ground truth | TBD | TBD | optional |

---

## 9. Runtime observations

| Field | Value |
|---|---|
| Requested backend/precision | TBD |
| Verified backend/precision | TBD |
| Fallback detected? | yes / no / unknown |
| Unsupported operations | TBD |
| Average latency, if measured | TBD |
| Number of warmup runs | TBD |
| Number of timed runs | TBD |
| Timing caution | single run / repeated / not_measured |

---

## 10. Qualitative visual observations

| Observation | Value | Notes |
|---|---|---|
| Visible boundary drift | none / mild / moderate / severe / TBD | TBD |
| Boundary thickening | yes / no / TBD | TBD |
| Boundary erosion | yes / no / TBD | TBD |
| Small-region loss | yes / no / TBD | TBD |
| Small-region fragmentation | yes / no / TBD | TBD |
| New noise components | yes / no / TBD | TBD |
| Large target-only region | yes / no / TBD | TBD |
| Large reference-only region | yes / no / TBD | TBD |
| Drift location | edge / center / shadow / reflective / texture / unknown | TBD |

---

## 11. Short interpretation

Write a cautious interpretation using measured values only.

```text
For case [case_id], the [target_precision] target output under [runtime_backend] and [hardware_lane]
was compared against the FP32 reference output using [threshold_policy].
The measured mask area drift was [value], mask IoU against reference was [value],
boundary IoU drift was [value], connected component delta was [value], and fallback status was [status].
This result is classified as [evidence_level] and should be interpreted as [case-level pilot / small case-set observation / etc.].
```

---

## 12. Limitations

- Ground truth available? yes / no / TBD.
- Number of cases: TBD.
- Number of hardware paths: TBD.
- Number of repeated runs: TBD.
- Calibration completeness: TBD.
- Fallback status completeness: TBD.
- Domain coverage: TBD.

---

## 13. Claim statement to use

Select one:

```text
Protocol only: no measured result is claimed.
```

```text
Measured case-level pilot: this result records output-stability metrics for one case under documented runtime conditions.
```

```text
Measured small case-set observation: this result summarizes multiple cases under documented runtime conditions.
```

Do not use benchmark, validation, deployment, clinical, diagnostic, or universal-robustness wording unless a separate evidence package supports it.
