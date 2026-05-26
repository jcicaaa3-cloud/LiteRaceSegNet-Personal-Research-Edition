# Precision Mini-Lab Protocol

**Subprogram:** HPLS-Eval / Precision Mini-Lab  
**Purpose:** FP32 / FP16 / INT8 segmentation-output stability pilot  
**Status:** additive protocol; not part of the original LiteRaceSegNet thesis/capstone claim

The Precision Mini-Lab studies how segmentation masks change when the same input and model are evaluated under different inference precision modes and runtime backends.

---

## 1. Scope

This protocol compares target outputs against a FP32 reference output.

Primary precision modes:

| Mode | Role | Notes |
|---|---|---|
| FP32 | Reference path | Preferred reference because it is usually the least compressed inference path. |
| FP16 | Reduced floating-point target | Often GPU-oriented. Must record whether native FP16, mixed precision, or converted model was used. |
| INT8 | Quantized target | Requires calibration/conversion details. Must not be claimed unless logs prove INT8 execution. |

This protocol records output stability. It does not replace conventional segmentation metrics and does not claim deployment validation.

---

## 2. Required inputs

A valid experiment row requires:

- input image path or case ID;
- FP32 reference mask path;
- target mask path;
- model identifier, checkpoint, or exported model path;
- preprocessing and resizing policy;
- threshold policy;
- runtime backend;
- hardware device;
- precision mode;
- fallback status;
- log path or notes explaining runtime verification.

If any of these is missing, mark the experiment as incomplete.

---

## 3. Case selection

A minimum pilot should include at least three case types:

1. **Medium/clear damage:** validates that the comparison pipeline works.
2. **Thin or small damage:** tests small-object disappearance, component loss, and boundary erosion.
3. **Noisy or low-contrast road:** tests target-only false-positive region growth and boundary ambiguity.

A stronger mini-lab should tag cases by:

- damage scale;
- boundary sharpness;
- lighting;
- road surface material;
- wet/dry condition;
- camera angle;
- resolution;
- blur/noise.

---

## 4. Reference-path protocol

For each input case:

1. Run the model using the FP32 reference path.
2. Save raw output if available.
3. Save binary mask using the selected threshold.
4. Save overlay image if available.
5. Save runtime log.
6. Record model format, backend, device, threshold, and preprocessing.

The FP32 reference is not automatically ground truth. It is the anchor used to measure output drift under target paths.

---

## 5. Target-path protocol

For each target path:

1. Run the same input case under the target precision/backend.
2. Use the same preprocessing and threshold policy as the reference path.
3. Save target output mask.
4. Save target overlay.
5. Save runtime logs.
6. Record whether the intended backend/precision was actually used.
7. Compute metrics against the FP32 reference.

Target paths may include:

| Target path | Required evidence |
|---|---|
| FP16 GPU | GPU name, runtime backend, precision mode, AMP/conversion notes, fallback status. |
| INT8 CPU | model export format, quantization method, calibration set, runtime backend, fallback status. |
| INT8 GPU/TensorRT | TensorRT or provider logs proving INT8 execution, calibration method, fallback status. |
| Possible NPU | device/runtime logs and model-conversion details. Future protocol until proven. |
| Possible TPU | device/runtime logs and model-conversion details. Future protocol until proven. |

---

## 6. Threshold and resizing policy

Threshold and resizing can create artificial drift. Record them explicitly.

Required fields:

- threshold value;
- whether threshold is fixed or tuned;
- whether masks are resized;
- resize method;
- output resolution;
- reference resolution;
- target resolution.

Recommended default:

```text
Use the same fixed threshold for FP32, FP16, and INT8 outputs.
If output sizes differ, resize target masks to the reference mask size using nearest-neighbor interpolation and record this fact.
```

Do not tune the threshold separately for each precision mode unless the experiment is explicitly a threshold-sensitivity analysis.

---

## 7. INT8 calibration policy

For INT8 experiments, record:

- quantization method: dynamic, static, QAT, PTQ, TensorRT calibration, OpenVINO quantization, or other;
- calibration dataset ID;
- number of calibration images;
- calibration preprocessing;
- whether calibration cases overlap with evaluation cases;
- converter version if known;
- unsupported operations and fallback behavior;
- activation and weight quantization mode if known.

If these details are missing, the result should be labeled as an incomplete INT8 pilot rather than a quantization benchmark.

---

## 8. Metrics

Minimum metrics are defined in `docs/output_stability_metrics.md`:

- mask area drift;
- mask IoU against FP32 reference;
- boundary IoU against FP32 reference;
- boundary IoU drift;
- connected component count change;
- centroid shift;
- target-only region area;
- reference-only region area;
- runtime backend;
- fallback status.

Recommended qualitative observations:

- boundary thickening;
- boundary erosion;
- small-region disappearance;
- small-region fragmentation;
- new isolated noise components;
- large false-positive connected region;
- large false-negative region;
- visual drift concentrated at edges;
- visual drift concentrated in low-contrast surface areas.

---

## 9. Hardware-shift protocol

### CPU lane

Use CPU as a reproducible baseline and as a check for backend conversion.

Record:

- CPU model if available;
- runtime backend;
- number of threads if controlled;
- model format;
- precision mode;
- latency only if repeated measurements are available.

### GPU lane

Use GPU for FP16 and acceleration-oriented comparisons.

Record:

- GPU model;
- CUDA/driver or backend version if available;
- runtime backend;
- precision path;
- fallback status;
- whether operations actually ran on GPU.

### Possible NPU lane

Treat NPU as future protocol unless a real device, model conversion, and logs exist.

Record when available:

- device name;
- NPU runtime or SDK;
- supported operators;
- conversion logs;
- fallback to CPU/GPU if any;
- model input/output format;
- precision mode.

### Possible TPU lane

Treat TPU as future protocol unless model conversion and execution logs exist.

Record when available:

- TPU device or service;
- compiler/converter;
- supported operations;
- quantization requirements;
- fallback or unsupported layers;
- model input/output format.

---

## 10. Execution order

| Step | Action | Output |
|---|---|---|
| 1 | Create case manifest | Case IDs and domain tags. |
| 2 | Define reference path | FP32 backend, threshold, output size. |
| 3 | Generate FP32 masks | Reference masks and logs. |
| 4 | Generate FP16 masks | Target masks and logs where supported. |
| 5 | Generate INT8 masks | Target masks and calibration/conversion logs where supported. |
| 6 | Compute metrics | JSON/CSV metrics. |
| 7 | Create overlays | Visual difference evidence. |
| 8 | Fill result template | Case-level report. |
| 9 | Assign evidence level | Claim-boundary classification. |

---

## 11. Result-status labels

Use these labels consistently:

| Label | Meaning |
|---|---|
| `planned` | Protocol row exists but no run has been made. |
| `incomplete` | Some files/logs exist, but required fields are missing. |
| `measured_case` | One case has masks, metrics, and logs. |
| `measured_case_set` | Multiple cases have masks, metrics, and logs. |
| `fallback_detected` | Intended backend/precision was not fully used. |
| `unsupported` | Runtime or device did not support the requested mode. |
| `future_protocol` | The row is only a design for future hardware. |

---

## 12. Claim boundary

Allowed:

```text
This Precision Mini-Lab defines and applies a pilot protocol for comparing segmentation-output stability across FP32, FP16, and INT8 under documented runtime conditions.
```

Allowed only when measured:

```text
For the tested case and backend, the INT8 target output showed X% mask-area drift and Y boundary-IoU drift relative to the FP32 reference.
```

Not allowed:

```text
The model is deployment-ready across hardware.
The model is clinically validated.
The INT8 model is universally stable.
This is a complete quantization benchmark.
```

---

## 13. Minimal viable pilot

The smallest useful pilot is:

```text
3 cases × 1 FP32 reference path × 1 FP16 or INT8 target path
```

Minimum outputs:

- 3 FP32 reference masks;
- 3 target masks;
- 3 metric JSON files or one combined CSV;
- 3 overlays or visual notes;
- backend/fallback notes;
- one filled result template.

This is still a pilot observation, not a benchmark.
