# HPLS-Eval

**HPLS-Eval** is a separated GitHub-only personal research follow-up track for observing lightweight segmentation-output behavior under practical inference conditions.

It does not replace or expand the original LiteRaceSegNet thesis claim. LiteRaceSegNet remains focused on lightweight road-damage semantic segmentation, boundary degradation, boundary-aware architecture, ablation, and baseline comparison.

## v15.2 Personal Research Edition

LiteRaceSegNet remains the thesis/capstone core. v15.2 adds a separated personal research extension for deployment-oriented segmentation-output stability notes.

## Main subsection

```text
precision-mini-lab/
```

The Precision Mini-Lab records limited case-level observations of how segmentation masks behave when inference precision changes across FP32, FP16, and INT8.

## Why this track exists

Lightweight segmentation models are often described using FP32 accuracy, parameter count, FLOPs, and runtime. Those values are useful, but segmentation outputs can also shift when inference precision, runtime backend, or conversion path changes. HPLS-Eval keeps these observations separate from the thesis core so they can be documented cautiously.

## Claim boundary

This section is not clinical validation, diagnostic evidence, a complete quantization benchmark, deployment validation, or proof of universal model superiority. Results should be interpreted only as limited case-level observations under the tested model format, runtime backend, calibration setting, and device environment.

## Local preview

Open the static page:

```text
hpls-eval/index.html
```

This page is a static portfolio preview only. No real inference is performed in the page.
