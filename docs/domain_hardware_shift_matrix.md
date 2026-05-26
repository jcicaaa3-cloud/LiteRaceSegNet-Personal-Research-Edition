# Domain and Hardware Shift Matrix

**Scope:** future protocol for segmentation-output stability under domain, precision, runtime, and hardware shifts  
**Applies to:** HPLS-Eval and Precision Mini-Lab  
**Claim boundary:** planned or measured observations only; no hardware-independent robustness claim

---

## 1. Why this matrix exists

Road-damage segmentation can be sensitive to both visual-domain conditions and execution-path conditions. A model may produce a stable-looking output in one environment and a visibly different output when the input domain or hardware/backend path changes.

This matrix separates four shift axes:

1. **Domain shift:** scene and image conditions.
2. **Precision shift:** FP32, FP16, INT8.
3. **Runtime shift:** PyTorch, ONNX Runtime, TensorRT, OpenVINO, or other backend.
4. **Hardware shift:** CPU, GPU, possible NPU, possible TPU.

---

## 2. Domain-shift axes

| Domain axis | Example tags | Why it matters | Stability metrics to inspect |
|---|---|---|---|
| Damage size | `small`, `medium`, `large` | Small regions can disappear under threshold or quantization. | mask area drift, component count, reference-only region. |
| Damage shape | `thin`, `wide`, `fragmented`, `irregular` | Thin/fragmented regions are boundary-sensitive. | boundary IoU drift, connected components. |
| Lighting | `bright`, `shadow`, `night`, `low_contrast` | Low contrast can amplify false positives/negatives. | target-only and reference-only region area. |
| Weather/surface | `dry`, `wet`, `reflective`, `dusty` | Reflections and texture can change confidence maps. | mask IoU, false-positive region. |
| Road material | `asphalt`, `concrete`, `patched`, `mixed_texture` | Texture mismatch may alter boundary predictions. | boundary IoU, component count. |
| Camera geometry | `front`, `angled`, `wide`, `low_height` | Perspective changes object scale and boundary sharpness. | centroid shift, mask area drift. |
| Image quality | `sharp`, `blur`, `compression`, `low_resolution` | Blurring and compression can erase small edges. | boundary IoU drift, small-region retention. |

---

## 3. Hardware/runtime axes

| Hardware lane | Runtime examples | Precision examples | Status rule | Main risk |
|---|---|---|---|---|
| CPU | PyTorch CPU, ONNX Runtime CPU, OpenVINO CPU | FP32, INT8 if supported | Can be measured when logs and masks exist. | Slower runtime, different operator kernels, quantization fallback. |
| GPU | PyTorch CUDA, ONNX Runtime CUDA, TensorRT | FP32, FP16, INT8 if supported | Can be measured when device/backend logs exist. | Mixed precision drift, unsupported op fallback, TensorRT conversion mismatch. |
| Possible NPU | OpenVINO NPU, vendor SDK, mobile/edge runtime | Often INT8 or mixed precision | Future protocol until real device logs exist. | Operator support limits, forced quantization, hidden fallback. |
| Possible TPU | Edge TPU or Cloud TPU style path | Often quantized or compiler-constrained | Future protocol until conversion and execution logs exist. | Model conversion restrictions, shape/operator constraints. |

---

## 4. Matrix template

Use this table to define planned and measured rows.

| Matrix ID | Domain tag group | Precision path | Runtime backend | Hardware lane | Required outputs | Status |
|---|---|---|---|---|---|---|
| DHS-00 | baseline clear damage | FP32 reference | PyTorch or ONNX Runtime | CPU | mask, log, threshold note | planned |
| DHS-01 | baseline clear damage | FP32 reference vs FP16 target | PyTorch CUDA or equivalent | GPU | masks, overlays, metrics, log | planned |
| DHS-02 | baseline clear damage | FP32 reference vs INT8 target | ONNX Runtime / TensorRT / OpenVINO | CPU/GPU | masks, calibration note, metrics, fallback note | planned |
| DHS-03 | small/thin damage | FP32 vs FP16 | GPU backend | GPU | small-region retention, boundary metrics | planned |
| DHS-04 | small/thin damage | FP32 vs INT8 | quantized backend | CPU/GPU | component change, reference-only region | planned |
| DHS-05 | low contrast/shadow | FP32 vs FP16 | GPU backend | GPU | target-only and reference-only regions | planned |
| DHS-06 | wet/reflective surface | FP32 vs INT8 | quantized backend | CPU/GPU | false-positive region, boundary metrics | planned |
| DHS-07 | mixed road texture | FP32 vs FP16/INT8 | selected backend | CPU/GPU | mask IoU, component count | planned |
| DHS-08 | selected domain set | FP32 vs NPU target | vendor runtime | possible NPU | conversion log, fallback status, masks | future_protocol |
| DHS-09 | selected domain set | FP32 vs TPU target | TPU compiler/runtime | possible TPU | conversion log, fallback status, masks | future_protocol |

---

## 5. CPU/GPU/NPU/TPU comparison protocol

### Required common fields

Every hardware comparison row must record:

- device name or hardware lane;
- runtime backend;
- execution provider;
- precision mode;
- model format;
- input resolution;
- threshold policy;
- reference mask path;
- target mask path;
- fallback status;
- log evidence.

### CPU protocol

CPU is the default reproducibility lane. Use it for FP32 reference and optional INT8 quantized backend if supported.

Minimum evidence:

```text
CPU model or runner description
runtime backend
precision mode
mask outputs
logs
fallback status
```

### GPU protocol

GPU is the main FP16 lane and possible INT8 acceleration lane.

Minimum evidence:

```text
GPU model
runtime backend
precision mode
provider logs
mask outputs
fallback status
```

### Possible NPU protocol

NPU rows remain future protocol unless all of the following exist:

- device/runtime name;
- conversion command or configuration;
- supported operator report or log;
- actual output mask;
- fallback status;
- metrics against FP32 reference.

### Possible TPU protocol

TPU rows remain future protocol unless all of the following exist:

- compiler/runtime path;
- conversion log;
- supported shape/operator confirmation;
- actual output mask;
- fallback status;
- metrics against FP32 reference.

---

## 6. Drift interpretation by matrix cell

| Observation | Possible interpretation | Required caution |
|---|---|---|
| Large mask area increase | Target path may introduce false-positive expansion. | Check threshold, preprocessing, and resolution alignment. |
| Large mask area decrease | Target path may erase weak/small damage regions. | Check small-region retention and calibration. |
| Boundary IoU drop with similar area | Output shape changed while area stayed similar. | Use overlays; area alone is insufficient. |
| Component count increase | Fragmentation or noise components may appear. | Inspect target-only regions. |
| Component count decrease | Small components may merge or disappear. | Inspect reference-only regions. |
| Large centroid shift | Prediction moved spatially. | Verify input alignment and resize policy. |
| Fallback detected | Intended precision/hardware claim may be invalid. | Report fallback before metrics interpretation. |

---

## 7. Reporting format

For each matrix cell, use this wording pattern:

```text
Under [domain tags], [model format], [runtime backend], [hardware lane], and [precision mode],
the target mask was compared against the FP32 reference using [threshold policy].
The observed output-stability metrics were [metrics].
This is a [evidence level] result and does not imply hardware-independent robustness.
```

---

## 8. Future expansion

Future work may add:

- repeated runs for latency and variance;
- power measurement when supported;
- calibration-set sensitivity for INT8;
- threshold-sensitivity curves;
- per-domain drift summaries;
- cross-backend agreement analysis;
- small-object retention analysis;
- failure-case gallery.

These remain future protocol until measured.
