# Precision Mini-Lab Experiment Matrix

**Purpose:** define planned and future FP32 / FP16 / INT8 segmentation-output stability experiments.  
**Status:** matrix/template until measured masks and logs are added.  
**Claim boundary:** pilot output-stability observations only unless a stronger evidence level is explicitly documented.

---

## 1. Experiment ID format

Recommended format:

```text
PML-[precision]-[hardware]-[backend]-[case_set]-[sequence]
```

Examples:

```text
PML-FP32-CPU-ORT-CS01-001
PML-FP16-GPU-TORCH-CS01-001
PML-INT8-CPU-ORT-CS01-001
PML-INT8-GPU-TRT-CS01-001
PML-INT8-NPU-FUTURE-CS01-001
```

---

## 2. Required experiment fields

| Field | Required? | Notes |
|---|---|---|
| `experiment_id` | yes | Unique row ID. |
| `case_set_id` | yes | Case collection being tested. |
| `case_id` | yes for result rows | Individual case ID. |
| `reference_precision` | yes | Usually FP32. |
| `target_precision` | yes | FP32, FP16, INT8, mixed, or future. |
| `model_format` | yes | `.pt`, `.onnx`, TensorRT engine, OpenVINO IR, etc. |
| `runtime_backend` | yes | PyTorch, ONNX Runtime, TensorRT, OpenVINO, vendor runtime. |
| `hardware_lane` | yes | CPU, GPU, possible NPU, possible TPU. |
| `calibration_policy` | required for INT8 | Record method and data. |
| `threshold_policy` | yes | Fixed threshold or threshold sweep. |
| `fallback_status` | yes | none, fallback_detected, unknown, unsupported. |
| `status` | yes | planned, measured_case, incomplete, future_protocol. |

---

## 3. Minimum viable pilot matrix

| Matrix ID | Experiment purpose | Reference path | Target path | Hardware lane | Required metrics | Status |
|---|---|---|---|---|---|---|
| PM-00 | Case manifest and threshold policy | n/a | n/a | n/a | case tags, threshold, preprocessing | planned |
| PM-01 | FP32 CPU reference | FP32 CPU | n/a | CPU | reference mask area, components, logs | planned |
| PM-02 | FP32 CPU vs FP32 GPU consistency | FP32 CPU | FP32 GPU | CPU/GPU | mask IoU, boundary IoU, centroid shift | planned |
| PM-03 | FP32 reference vs FP16 GPU | FP32 CPU or GPU | FP16 GPU | GPU | area drift, boundary drift, components, fallback | planned |
| PM-04 | FP32 reference vs INT8 CPU | FP32 reference | INT8 CPU backend | CPU | area drift, boundary drift, calibration, fallback | planned |
| PM-05 | FP32 reference vs INT8 GPU | FP32 reference | INT8 TensorRT or equivalent | GPU | area drift, boundary drift, calibration, fallback | future_protocol |
| PM-06 | FP32 reference vs possible NPU | FP32 reference | NPU runtime target | possible NPU | conversion log, fallback, output drift | future_protocol |
| PM-07 | FP32 reference vs possible TPU | FP32 reference | TPU runtime target | possible TPU | conversion log, fallback, output drift | future_protocol |
| PM-08 | Threshold sensitivity | FP32 reference | FP16/INT8 target across thresholds | selected | drift curve, threshold note | future_protocol |
| PM-09 | Calibration sensitivity | FP32 reference | INT8 with calibration variants | CPU/GPU | drift by calibration set | future_protocol |

---

## 4. Domain-aware expansion matrix

| Domain group | Case examples | FP32 reference | FP16 target | INT8 target | Main risk to inspect |
|---|---|---|---|---|---|
| DG-01 clear medium damage | case IDs TBD | required | optional | optional | sanity-check stability. |
| DG-02 small/thin damage | case IDs TBD | required | recommended | recommended | small-region loss and boundary erosion. |
| DG-03 noisy texture | case IDs TBD | required | recommended | recommended | target-only false-positive regions. |
| DG-04 low contrast/shadow | case IDs TBD | required | recommended | recommended | reference-only loss and centroid shift. |
| DG-05 wet/reflective surface | case IDs TBD | required | optional | recommended | false-positive expansion. |
| DG-06 unusual camera angle | case IDs TBD | required | optional | optional | scale and boundary instability. |

---

## 5. Detailed planned rows

| Experiment ID | Case set | Reference precision/backend | Target precision/backend | Hardware | Model format | Calibration | Threshold | Output artifacts | Status | Evidence cap |
|---|---|---|---|---|---|---|---|---|---|---|
| PML-FP32-CPU-REF-CS01-001 | CS01 | FP32 / CPU | n/a | CPU | TBD | n/a | fixed TBD | ref masks, logs | planned | Level 1 if measured |
| PML-FP32-GPU-CHECK-CS01-001 | CS01 | FP32 / CPU | FP32 / GPU | CPU/GPU | TBD | n/a | fixed TBD | masks, overlays, metrics, logs | planned | Level 2 if multiple cases |
| PML-FP16-GPU-TORCH-CS01-001 | CS01 | FP32 reference | FP16 / PyTorch CUDA or equivalent | GPU | TBD | n/a | fixed TBD | masks, overlays, metrics, logs | planned | Level 2 if multiple cases |
| PML-INT8-CPU-ORT-CS01-001 | CS01 | FP32 reference | INT8 / ONNX Runtime CPU | CPU | ONNX TBD | static/dynamic TBD | fixed TBD | masks, overlays, metrics, calibration note, logs | planned | Level 2 if multiple cases |
| PML-INT8-GPU-TRT-CS01-001 | CS01 | FP32 reference | INT8 / TensorRT | GPU | TensorRT engine TBD | calibration TBD | fixed TBD | masks, overlays, metrics, TRT logs | future_protocol | capped until logs prove INT8 |
| PML-INT8-NPU-FUTURE-CS01-001 | CS01 | FP32 reference | INT8 or vendor mode / NPU runtime | possible NPU | vendor format TBD | TBD | fixed TBD | conversion logs, masks, metrics | future_protocol | capped until real device logs |
| PML-INT8-TPU-FUTURE-CS01-001 | CS01 | FP32 reference | quantized TPU runtime | possible TPU | TPU-compatible format TBD | TBD | fixed TBD | compiler logs, masks, metrics | future_protocol | capped until real device logs |

---

## 6. Execution checklist per row

For each experiment row:

- [ ] Confirm case IDs and input files.
- [ ] Confirm model checkpoint or export.
- [ ] Record preprocessing and input resolution.
- [ ] Record threshold policy.
- [ ] Generate or locate FP32 reference mask.
- [ ] Generate target mask.
- [ ] Save runtime/conversion logs.
- [ ] Record fallback status.
- [ ] Compute output-stability metrics.
- [ ] Create overlay or visual difference note.
- [ ] Fill `result_template.md`.
- [ ] Assign evidence level.

---

## 7. Naming convention for outputs

Recommended paths:

```text
cases/<case-id>/predictions/<experiment-id>_mask.png
cases/<case-id>/overlays/<experiment-id>_overlay.png
cases/<case-id>/metrics/<experiment-id>_metrics.json
cases/<case-id>/notes.md
```

Do not use output filenames that imply validation or deployment readiness unless the evidence level supports that wording.

---

## 8. Fallback-status policy

| Status | Meaning | Reporting action |
|---|---|---|
| `none` | Intended backend and precision are verified. | Metrics may be interpreted under that target path. |
| `fallback_detected` | Runtime used another provider or precision for some/all operations. | Report as fallback; do not claim target precision/hardware fully ran. |
| `unknown` | Logs are unavailable or unclear. | Mark result incomplete or cap evidence level. |
| `unsupported` | Target path could not run. | Record as unsupported; no output-stability metric unless output exists. |

---

## 9. Success criteria for the pilot

The pilot is complete when at least one target path has:

- FP32 reference masks;
- target precision masks;
- saved runtime logs;
- fallback status;
- output-stability metrics;
- visual overlays or qualitative notes;
- result template filled with no guessed values.

Even then, the result remains a pilot observation unless the case set and hardware coverage are expanded.
