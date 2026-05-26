# Precision Mini-Lab: FP32 / FP16 / INT8 Stability Check

The Precision Mini-Lab records limited case-level observations of how segmentation masks behave when inference precision changes across FP32, FP16, and INT8.

This section treats numerical precision as an additional observation axis for lightweight segmentation-output stability. It does not replace conventional metrics, and it does not make broad deployment claims.

## Scope separation

LiteRaceSegNet remains the thesis/capstone core. The Precision Mini-Lab is a separated HPLS-Eval follow-up note, not a new official LiteRaceSegNet thesis claim.

## Precision modes

| Precision mode | Explanation | Notes to record |
|---|---|---|
| FP32 | Standard high-precision floating-point inference | Reference setting, model format, backend, execution provider |
| FP16 | Reduced floating-point precision, often faster and lighter on compatible GPUs | GPU support, AMP/conversion path, fallback behavior |
| INT8 | 8-bit integer quantized inference, potentially faster/lighter | Calibration method, calibration data, backend, conversion path, fallback behavior |

## Mask-level observation list

- mask area change
- boundary shape change
- connected component change
- centroid shift
- false-positive regions
- false-negative regions
- visible mask drift
- runtime backend
- fallback status

## Evidence templates

Use the CSV templates under:

```text
tables/evidence-table-template.csv
tables/extended-evidence-table-template.csv
```

The tables are placeholders. Do not fill them with guessed or inferred results. Add measured values only when logs, output masks, and case notes are available.

## Case folder

```text
cases/case-001/
├── inputs/
├── predictions/
├── overlays/
├── metrics/
└── notes.md
```

## What this does not claim

This section is not clinical validation, diagnostic evidence, a complete quantization benchmark, deployment validation, or proof of universal model superiority. Results should be interpreted only as limited case-level observations under the tested model format, runtime backend, calibration setting, and device environment.

This Mini-Lab also does not claim:

- clinical validation
- diagnostic evidence
- complete benchmark coverage
- deployment-ready proof
- hardware-independent conclusions
- universal robustness
- TensorRT INT8 full validation unless logs explicitly prove it
- a replacement for LiteRaceSegNet thesis scope

## Static preview note

If this Mini-Lab is shown in a GitHub Pages page, label any page interaction as:

> Static portfolio preview only. No real inference is performed in this page.
