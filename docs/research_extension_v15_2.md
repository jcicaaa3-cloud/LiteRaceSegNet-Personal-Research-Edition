# LiteRaceSegNet v15.2 Research Extension Layer

**Status:** additive research-extension layer  
**Package identity:** LiteRaceSegNet v15.2 Personal Research Edition  
**Scope:** HPLS-Eval, Precision Mini-Lab, hardware-shift observation, and segmentation-output stability  
**Core material rule:** this layer keeps the existing LiteRaceSegNet project material separate from follow-up evaluation notes and does not expand the public claim beyond the documented scope.

This file defines a follow-up research program that sits alongside the LiteRaceSegNet thesis/capstone core.

---

## 1. Positioning

LiteRaceSegNet remains the thesis/capstone core for lightweight road-damage semantic segmentation. The core project should continue to be interpreted around model design, boundary-aware segmentation, evidence organization, CPU/GPU evidence structure, and careful portfolio documentation.

The research extension layer adds a separate evaluation track:

```text
LiteRaceSegNet core
  └── thesis/capstone road-damage segmentation project

HPLS-Eval extension
  └── separated follow-up program for output stability under precision, runtime, hardware, and domain shifts

Precision Mini-Lab
  └── pilot FP32 / FP16 / INT8 segmentation-output stability protocol
```

The extension does **not** upgrade the original thesis claim. It creates a structured path for future measurements.

---

## 2. Research motivation

A lightweight segmentation model may look acceptable when reported only with conventional metrics such as mIoU, Dice/F1, parameter count, FLOPs, or average runtime. However, deployment-oriented use can introduce additional shifts:

- precision shift: FP32 to FP16 or INT8;
- runtime shift: PyTorch to ONNX Runtime, TensorRT, OpenVINO, or another backend;
- hardware shift: CPU to GPU, possible NPU, or possible TPU;
- threshold shift: different binarization or confidence thresholds;
- domain shift: lighting, weather, surface texture, road material, camera angle, and damage size distribution.

The extension asks whether the **shape and location of the segmentation output** remain stable under those shifts.

---

## 3. Research questions

### RQ1: Mask-area stability

When the same input is evaluated under FP32, FP16, and INT8, how much does the predicted foreground mask area change?

Primary observations:

- absolute mask area drift in pixels;
- relative mask area drift in percent;
- small-mask sensitivity when the reference foreground area is small.

### RQ2: Boundary stability

Do the predicted damage boundaries remain stable, or do they shift, thicken, fragment, or disappear under lower precision or backend conversion?

Primary observations:

- boundary IoU against the FP32 reference;
- boundary IoU drift;
- visible boundary thickening or erosion;
- boundary-sensitive false-positive and false-negative regions.

### RQ3: Connected-region stability

Does the number of connected foreground regions change under precision or hardware shift?

Primary observations:

- connected component count under the FP32 reference;
- connected component count under target precision/backend;
- component split, merge, deletion, and noise appearance;
- small-component retention.

### RQ4: Spatial-location stability

When the foreground mask changes, does the center of mass of the predicted damage region shift?

Primary observations:

- centroid shift in pixels;
- normalized centroid shift relative to image diagonal;
- centroid undefined cases when one mask has no foreground.

### RQ5: Runtime and fallback transparency

Does the runtime actually use the intended backend and precision, or does it silently fall back to another path?

Primary observations:

- runtime backend;
- execution provider;
- model format;
- precision mode;
- fallback status;
- conversion or calibration logs;
- latency only when measured and repeated.

### RQ6: Complementary value

Can output-stability metrics complement the existing LiteRaceSegNet core evaluation without replacing or inflating the original thesis/capstone claim?

Primary observations:

- whether the extension adds useful diagnostic information about output behavior;
- whether it remains clearly separated from the original claim;
- whether claim boundaries are preserved in every result report.

---

## 4. Experimental unit

Each experiment row should be defined by the following tuple:

```text
(model checkpoint or export,
 input case,
 reference precision/backend,
 target precision/backend,
 hardware device,
 runtime backend,
 threshold policy,
 calibration policy,
 output mask,
 log evidence)
```

The smallest valid experiment compares one target output against a FP32 reference output for the same input case.

---

## 5. Reference and target outputs

### Reference output

The reference output is usually the FP32 segmentation mask from the most stable available path, such as PyTorch FP32 or ONNX Runtime FP32. It is not automatically ground truth. It is the comparison anchor for output-stability analysis.

### Target output

The target output is a mask from a shifted condition, for example:

- FP16 GPU inference;
- INT8 ONNX Runtime inference;
- TensorRT INT8 inference, if logs prove it;
- OpenVINO CPU/NPU inference, if logs prove it;
- possible Edge TPU/NPU/TPU path, if model conversion and logs prove it.

### Optional ground truth

If ground-truth masks are available, the result may additionally report conventional segmentation metrics against ground truth. These must be clearly separated from reference-output stability metrics.

---

## 6. Primary evaluation axes

| Axis | Required fields | Why it matters |
|---|---|---|
| Output shape | mask area drift, boundary IoU drift, connected component change | Captures visible segmentation instability that may not be obvious from runtime alone. |
| Spatial alignment | centroid shift, target-only region, reference-only region | Detects location-level changes and mask movement. |
| Runtime path | backend, execution provider, precision, model format, fallback status | Prevents false claims about acceleration or quantization. |
| Domain context | lighting, surface, damage size, camera angle, weather, image resolution | Helps explain when output drift is caused by scene conditions rather than precision alone. |
| Evidence quality | logs, masks, overlays, case notes, repeated runs | Controls whether the result is a plan, pilot observation, or measured evidence. |

---

## 7. Required metrics

The extension uses the definitions in [`output_stability_metrics.md`](output_stability_metrics.md). Minimum metrics for a case-level result:

1. `mask_area_ref_px`
2. `mask_area_target_px`
3. `mask_area_drift_px`
4. `mask_area_drift_pct`
5. `mask_iou_against_ref`
6. `boundary_iou_against_ref`
7. `boundary_iou_drift`
8. `connected_components_ref`
9. `connected_components_target`
10. `connected_component_delta`
11. `centroid_shift_px`
12. `target_only_region_area_px`
13. `reference_only_region_area_px`
14. `runtime_backend`
15. `fallback_status`

Latency, power, memory, and throughput are optional unless measured with repeated runs and documented hardware details.

---

## 8. Execution sequence

### Stage 0: Protect the public scope

- Do not edit the existing README, Korean README, root HTML, existing Pages, existing assets, or manifests.
- Add new files only.
- Record the extension files in `MANIFEST_RESEARCH_EXTENSION.md`.

### Stage 1: Select cases

Create a small case set that includes:

- at least one clear medium/large damage region;
- at least one small or thin damage region;
- at least one visually noisy surface;
- at least one case likely to create boundary ambiguity;
- optional shifted-domain cases such as shadow, wet surface, low contrast, or unusual camera angle.

### Stage 2: Define the reference path

Record:

- model checkpoint or exported model;
- model input size;
- preprocessing and normalization;
- FP32 runtime backend;
- threshold policy;
- output mask path;
- run log path.

### Stage 3: Run target paths

Run the same cases under target conditions:

- FP16 if GPU support is available;
- INT8 if conversion and calibration are available;
- CPU/GPU variants if both are available;
- NPU/TPU variants only as future protocol unless a real device and conversion log exist.

### Stage 4: Verify runtime and fallback

A result is incomplete if it does not identify the actual runtime path. Record:

- provider name;
- model format;
- precision mode;
- device name;
- conversion command or configuration;
- calibration dataset, if INT8;
- fallback status.

### Stage 5: Compute output-stability metrics

Compare target masks against the FP32 reference mask. Use fixed threshold and aligned resolution. If resolution differs, record the resize policy.

### Stage 6: Create visual overlays

For each target path, create an overlay or difference map:

- reference foreground;
- target foreground;
- target-only region;
- reference-only region;
- boundary difference if possible.

### Stage 7: Fill the result template

Use `hpls-eval/precision-mini-lab/result_template.md`. Leave unknown values as `TBD`; do not infer measurements from screenshots or expectations.

### Stage 8: Assign evidence level

Use the evidence levels defined in [`claim_boundary_for_extension.md`](claim_boundary_for_extension.md). A single case is a pilot observation, not a benchmark.

---

## 9. Result artifact layout

Suggested additive layout:

```text
hpls-eval/precision-mini-lab/
├── experiment_matrix.md
├── result_template.md
├── cases/
│   └── case-001/
│       ├── inputs/
│       ├── predictions/
│       ├── overlays/
│       ├── metrics/
│       └── notes.md
├── tables/
│   ├── precision-mini-lab-matrix-template.csv
│   └── output-stability-results-template.csv
└── scripts/
    ├── compute_output_stability_metrics_v15_2.py
    └── README_output_stability_metrics_v15_2.md
```

---

## 10. Evidence-level policy

| Evidence level | Meaning | Allowed wording |
|---|---|---|
| Level 0 | Protocol or template only | “Planned evaluation protocol.” |
| Level 1 | Single case with saved masks and logs | “Case-level pilot observation.” |
| Level 2 | Multiple cases with consistent logs | “Small case-set observation.” |
| Level 3 | Repeated runs across documented hardware/backends | “Limited cross-backend output-stability evaluation.” |
| Level 4 | External benchmark, independent validation, deployment conditions | Not claimed by this extension unless separately performed. |

---

## 11. Claim boundary

This extension may claim that it defines a protocol and records case-level output-stability observations. It may not claim clinical validation, diagnostic evidence, deployment readiness, complete quantization benchmarking, hardware-independent robustness, or general model superiority.

The core LiteRaceSegNet research remains intact and separate. The extension is a follow-up research line, not a replacement thesis.

---

## 12. Cross-document map

| File | Role |
|---|---|
| `docs/hpls_eval_research_program.md` | Research program design for HPLS-Eval. |
| `docs/precision_mini_lab_protocol.md` | FP32 / FP16 / INT8 pilot protocol. |
| `docs/domain_hardware_shift_matrix.md` | Domain and hardware shift planning matrix. |
| `docs/output_stability_metrics.md` | Metric definitions and formulas. |
| `docs/claim_boundary_for_extension.md` | Allowed and prohibited claims. |
| `hpls-eval/extension_plan_v15_2.md` | HPLS-Eval implementation plan. |
| `hpls-eval/precision-mini-lab/experiment_matrix.md` | Precision Mini-Lab experiment matrix. |
| `hpls-eval/precision-mini-lab/result_template.md` | Result recording template. |
| `research_extension.html` | Static GitHub Pages auxiliary page for this extension. |

---

## 13. Non-goals

This extension does not:

- replace existing README or HTML files;
- rename or revive unrelated development labels;
- add new measured results without logs;
- claim clinical or diagnostic validity;
- certify deployment safety;
- claim a complete hardware benchmark;
- hide placeholders by filling them with guessed values.

---

## 14. Immediate next actions

1. Choose 3 to 5 representative input cases.
2. Generate FP32 reference masks and logs.
3. Run FP16 and INT8 target paths only where the backend is verifiable.
4. Compute output-stability metrics with the provided script or equivalent implementation.
5. Fill `result_template.md` for each experiment row.
6. Keep all results under HPLS-Eval or Precision Mini-Lab, not inside the original LiteRaceSegNet thesis claim.
