# Output Stability Metric Helper

This folder adds `compute_output_stability_metrics_v15_2.py`, a small helper for the HPLS-Eval / Precision Mini-Lab research-extension layer.

It compares a reference binary mask, usually FP32 output, against a target binary mask, such as FP16 or INT8 output.

## Metrics produced

- mask area reference and target;
- mask area drift in pixels and percent;
- mask IoU against reference;
- mask IoU drift;
- boundary IoU against reference;
- boundary IoU drift;
- connected component count for reference and target;
- connected component delta;
- centroid shift;
- target-only region area;
- reference-only region area.

## Example

```bash
python hpls-eval/precision-mini-lab/scripts/compute_output_stability_metrics_v15_2.py \
  --ref-mask hpls-eval/precision-mini-lab/cases/case-001/predictions/fp32_reference_mask.png \
  --target-mask hpls-eval/precision-mini-lab/cases/case-001/predictions/int8_target_mask.png \
  --case-id case-001 \
  --experiment-id PML-INT8-CPU-ORT-CS01-001 \
  --target-precision INT8 \
  --runtime-backend "ONNX Runtime CPU" \
  --fallback-status TBD \
  --output-json hpls-eval/precision-mini-lab/cases/case-001/metrics/PML-INT8-CPU-ORT-CS01-001_metrics.json
```

If target and reference mask sizes differ, add:

```bash
--resize-target-nearest
```

and record that resize policy in the result template.

## Claim boundary

This helper computes mask-comparison metrics only. It does not perform clinical validation, diagnostic evaluation, deployment certification, or complete quantization benchmarking.
