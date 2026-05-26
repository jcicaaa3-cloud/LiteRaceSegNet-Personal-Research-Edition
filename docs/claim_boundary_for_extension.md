# Claim Boundary for the Research Extension

**Applies to:** HPLS-Eval, Precision Mini-Lab, hardware-shift matrix, output-stability metrics, and any auxiliary GitHub Pages research-extension page.

This file prevents the new research extension from being misread as a replacement for the original LiteRaceSegNet thesis/capstone claim.

---

## 1. Core separation rule

LiteRaceSegNet remains the road-damage segmentation thesis/capstone core. The research extension is a separated follow-up program for output-stability analysis.

The extension may add new protocols, matrices, templates, scripts, and measured results. It must not rewrite the original claim history or imply that future pilot observations retroactively change the original thesis evidence.

---

## 2. Allowed claims

Allowed without measured results:

```text
This repository includes an additive research-extension protocol for HPLS-Eval, Precision Mini-Lab, hardware-shift planning, and segmentation-output stability analysis.
```

Allowed with case-level measured results:

```text
For the tested case, model export, runtime backend, threshold, and hardware path, the target precision output showed measured mask drift relative to the FP32 reference.
```

Allowed with multiple documented cases:

```text
In a small documented case set, the extension observed output-stability patterns under the tested backend and precision settings.
```

Allowed with documented hardware logs:

```text
The result was measured on the recorded hardware/backend path, with fallback status reported.
```

---

## 3. Prohibited claims

Do not claim:

- clinical validation;
- diagnostic evidence;
- medical usefulness;
- deployment readiness;
- production safety;
- complete quantization benchmark coverage;
- universal FP16 or INT8 robustness;
- hardware-independent robustness;
- superiority over all baselines;
- NPU/TPU validation without actual device/conversion logs;
- TensorRT INT8 validation without logs proving INT8 execution;
- that FP32 reference disagreement automatically means incorrect prediction;
- that the extension replaces the original LiteRaceSegNet thesis/capstone scope.

---

## 4. Evidence levels

| Level | Name | Evidence required | Allowed description |
|---|---|---|---|
| 0 | Protocol only | Design documents, matrices, templates | “Planned research-extension protocol.” |
| 1 | Single-case pilot | One input, reference mask, target mask, metrics, backend note | “Case-level pilot observation.” |
| 2 | Small case set | Multiple cases with masks, metrics, logs, fallback status | “Small case-set output-stability observation.” |
| 3 | Cross-backend/hardware evaluation | Multiple cases across documented hardware/backends with repeated logs | “Limited cross-backend output-stability evaluation.” |
| 4 | External validation / benchmark | External dataset, independent validation, repeated hardware study, documented methodology | Not claimed unless separately completed. |

Any result with missing backend/fallback status should be capped at Level 1 or marked incomplete.

---

## 5. Safe wording templates

### Protocol-level wording

```text
This file defines the protocol for comparing segmentation-output stability across FP32, FP16, and INT8 paths.
```

### Case-level wording

```text
For case [case_id], the [target_precision] output under [runtime_backend] was compared against the FP32 reference output. The observed mask area drift was [value], boundary IoU drift was [value], and fallback status was [status]. This is a case-level pilot observation only.
```

### Hardware-shift wording

```text
This hardware lane is marked as future protocol until a real device run, conversion log, output mask, and fallback status are available.
```

### Incomplete-result wording

```text
This row is incomplete because [missing field] is not available. It should not be used for performance, deployment, or robustness claims.
```

---

## 6. Unsafe wording examples

Do not use:

```text
The model is stable across all hardware.
The model is ready for deployment.
The INT8 model has been fully validated.
The precision results prove real-world robustness.
The extension is the new official thesis result.
The output is clinically meaningful.
```

---

## 7. Conditions for stronger future claims

To move beyond pilot language, future work would need:

- clearly defined dataset and split;
- documented model version and export process;
- reproducible preprocessing and threshold policy;
- repeated runs and variance reporting;
- multiple hardware/backend paths with logs;
- calibration details for INT8;
- provenance-reviewed inputs and masks;
- ground truth if correctness metrics are claimed;
- independent review or external benchmark if generalization is claimed.

Until those conditions are met, extension results remain limited observations.

---

## 8. Public-page disclaimer

Any public auxiliary page for this extension should include:

```text
This page describes an additive research-extension program. It does not replace the LiteRaceSegNet core material and does not claim clinical validation, diagnostic evidence, deployment readiness, or complete hardware/quantization benchmarking.
```

---

## 9. Relationship to placeholders

Placeholders are allowed only as placeholders. Do not convert `TBD`, `planned`, `future_protocol`, or `unsupported` into measured claims.

Every number must be traceable to saved masks, logs, or explicitly documented calculations.
