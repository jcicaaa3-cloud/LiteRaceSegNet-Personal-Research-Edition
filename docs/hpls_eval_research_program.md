# HPLS-Eval Research Program

**Program type:** separated follow-up research line  
**Attached project:** LiteRaceSegNet v15.2 Personal Research Edition  
**Core principle:** preserve LiteRaceSegNet as the thesis/capstone road-damage segmentation core while using HPLS-Eval for cautious output-stability research.

HPLS-Eval is treated here as the repository’s deployment-oriented evaluation lane. It studies how segmentation outputs behave when inference precision, runtime backend, hardware, and scene domain conditions change.

---

## 1. Program charter

HPLS-Eval exists to answer one practical question:

> When the same LiteRaceSegNet-style segmentation model is moved across precision modes, runtime backends, and hardware paths, does the predicted road-damage mask remain stable enough to describe the output behavior honestly?

This is not a deployment certification program. It is a structured evidence-collection program.

---

## 2. Separation from the LiteRaceSegNet core

| Area | LiteRaceSegNet core | HPLS-Eval extension |
|---|---|---|
| Primary role | Thesis/capstone road-damage segmentation project | Follow-up output-stability evaluation program |
| Primary evidence | Architecture, segmentation metrics, ablation, baseline comparison, evidence pipeline | Output drift, backend/precision logs, hardware/runtime notes, case-level stability observations |
| Claim level | Existing project-specific claim boundary | New extension-level claim boundary only |
| File location | Existing root, docs, scripts, demos | `hpls-eval/`, `docs/*extension*`, Precision Mini-Lab |
| Risk | Overwriting core material could confuse the public review scope | Must remain additive and separated |

---

## 3. Research work packages

### WP1: Scope and instrumentation

Goal: define what must be recorded before a stability result can be trusted.

Required records:

- model identifier or checkpoint/export path;
- input image or case identifier;
- preprocessing and threshold policy;
- runtime backend;
- execution provider;
- hardware device;
- precision mode;
- fallback status;
- output mask path;
- log path.

Deliverables:

- `hpls-eval/extension_plan_v15_2.md`
- `hpls-eval/precision-mini-lab/experiment_matrix.md`

### WP2: Output-stability metrics

Goal: define metrics that compare masks across precision/backend/hardware paths.

Required metrics:

- mask area drift;
- mask IoU against FP32 reference;
- boundary IoU drift;
- connected component count change;
- centroid shift;
- target-only and reference-only region area;
- runtime backend and fallback status.

Deliverable:

- `docs/output_stability_metrics.md`

### WP3: Precision Mini-Lab

Goal: run a pilot comparison between FP32, FP16, and INT8 outputs.

Target comparisons:

```text
FP32 reference -> FP16 target
FP32 reference -> INT8 target
FP32 CPU reference -> FP32 GPU target, if both are available
FP32/FP16/INT8 -> backend-specific outputs, when logs prove the path
```

Deliverables:

- `docs/precision_mini_lab_protocol.md`
- `hpls-eval/precision-mini-lab/result_template.md`
- `hpls-eval/precision-mini-lab/tables/output-stability-results-template.csv`

### WP4: Hardware-shift observation

Goal: plan comparisons across CPU, GPU, possible NPU, and possible TPU paths without claiming unsupported hardware validation.

Hardware lanes:

- CPU: reference and lightweight deployment baseline;
- GPU: acceleration and FP16 lane;
- possible NPU: future edge-accelerator protocol only unless device logs exist;
- possible TPU: future protocol only unless model conversion and device logs exist.

Deliverable:

- `docs/domain_hardware_shift_matrix.md`

### WP5: Domain/context shift

Goal: record whether output drift becomes more visible under scene changes.

Domain axes:

- lighting: bright, shadow, night, low contrast;
- weather/surface: dry, wet, reflective, noisy texture;
- road material: asphalt, concrete, mixed texture;
- damage type: pothole, crack-like boundary, patch, thin fragment;
- object scale: small, medium, large;
- camera: angle, resolution, blur.

Deliverable:

- domain-shift section inside `docs/domain_hardware_shift_matrix.md`

### WP6: Reporting and claim control

Goal: prevent extension results from being misread as stronger claims than they are.

Deliverable:

- `docs/claim_boundary_for_extension.md`

---

## 4. HPLS-Eval research questions

| ID | Question | Minimum evidence required |
|---|---|---|
| HPLS-RQ1 | Does precision shift change mask area? | FP32 reference mask, target mask, area drift metrics. |
| HPLS-RQ2 | Does precision shift alter boundaries more than interiors? | Boundary IoU or equivalent boundary comparison. |
| HPLS-RQ3 | Do small damage regions disappear, split, merge, or appear under target precision? | Connected component count and visual overlay. |
| HPLS-RQ4 | Does hardware/backend shift cause different output masks even at the same precision? | Same model/input under documented backend/hardware paths. |
| HPLS-RQ5 | Do fallback paths invalidate claimed precision or hardware mode? | Backend logs and fallback status. |
| HPLS-RQ6 | Which domain conditions produce the most visible output drift? | Case tags and drift metrics across tagged cases. |

---

## 5. Recommended case-set design

A minimal case set should include at least 3 cases:

| Case type | Why include it | Expected risk |
|---|---|---|
| Clear medium damage | Sanity-check case | Low-to-medium drift. |
| Thin/small damage | Tests small-object loss | High false-negative and component-loss risk. |
| Noisy or low-contrast road | Tests boundary ambiguity | High false-positive and boundary-drift risk. |

A stronger pilot should include 10 to 30 cases tagged by domain factors. A benchmark-level claim would require more, but benchmark-level claims are outside this extension unless separately performed.

---

## 6. Measurement policy

HPLS-Eval records only measured or explicitly planned values.

Use:

- numeric values only when produced by saved masks/logs;
- `TBD` for unmeasured values;
- `not_applicable` when a metric cannot be computed;
- `unsupported` when a hardware lane was not actually run;
- `fallback_detected` when the target backend silently used another execution path.

Do not use expected speedup, expected accuracy, or assumed stability as evidence.

---

## 7. Analysis plan

### Per-case analysis

For each target path:

1. Compare target mask to FP32 reference mask.
2. Compute output-stability metrics.
3. Inspect overlay for boundary drift, target-only regions, and reference-only regions.
4. Record runtime backend and fallback status.
5. Assign evidence level.

### Across-case analysis

For a case set:

1. Summarize median and maximum area drift.
2. Summarize median and minimum mask IoU against reference.
3. Summarize median and minimum boundary IoU against reference.
4. Count cases with component deletion, split, merge, or new noise components.
5. Separate results by domain tags and backend/hardware path.

### Reporting format

Use cautious wording:

```text
Under the tested model export, case set, backend, threshold, and hardware path,
this pilot observed [metric] drift relative to the FP32 reference.
```

Do not write:

```text
The model is robust across all devices.
```

---

## 8. Program outputs

| Output | Location | Purpose |
|---|---|---|
| Extension charter | `docs/research_extension_v15_2.md` | Defines the overall research-extension layer. |
| HPLS plan | `hpls-eval/extension_plan_v15_2.md` | Converts program into repo-level tasks. |
| Precision protocol | `docs/precision_mini_lab_protocol.md` | Defines FP32/FP16/INT8 protocol. |
| Experiment matrix | `hpls-eval/precision-mini-lab/experiment_matrix.md` | Defines planned and future experiments. |
| Result template | `hpls-eval/precision-mini-lab/result_template.md` | Standardizes result recording. |
| Metric definitions | `docs/output_stability_metrics.md` | Prevents metric ambiguity. |
| Claim boundary | `docs/claim_boundary_for_extension.md` | Controls public interpretation. |
| Static page | `research_extension.html` | GitHub Pages auxiliary page for navigation. |

---

## 9. Review checklist

Before publishing any HPLS-Eval result, verify:

- the result is under HPLS-Eval or Precision Mini-Lab, not presented as the original thesis core;
- every numeric value has a mask/log source;
- backend and precision are documented;
- fallback status is not blank;
- `TBD` is used instead of guessed values;
- the claim boundary section is included;
- case images and masks have acceptable provenance and privacy status;
- no private datasets, tokens, checkpoints, or local machine paths are introduced into the public export.
