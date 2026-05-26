# HPLS-Eval Extension Plan v15.2

**Layer:** additive research extension  
**Parent package:** LiteRaceSegNet v15.2 Personal Research Edition  
**Core rule:** keep LiteRaceSegNet thesis/capstone materials clearly separated; add HPLS-Eval as a follow-up research lane.

---

## 1. Plan summary

HPLS-Eval v15.2 expands from a simple follow-up note into a structured research program for segmentation-output stability under precision, runtime, hardware, and domain shifts.

The extension adds:

- research questions;
- experiment matrix;
- output-stability metrics;
- FP32 / FP16 / INT8 pilot protocol;
- CPU / GPU / possible NPU / possible TPU future matrix;
- result-recording templates;
- claim-boundary rules;
- a static auxiliary Pages entry point.

---

## 2. New document map

| File | Role |
|---|---|
| `../docs/research_extension_v15_2.md` | Top-level extension charter. |
| `../docs/hpls_eval_research_program.md` | Program design for HPLS-Eval. |
| `../docs/precision_mini_lab_protocol.md` | FP32 / FP16 / INT8 pilot protocol. |
| `../docs/domain_hardware_shift_matrix.md` | Hardware and domain shift matrix. |
| `../docs/output_stability_metrics.md` | Metric definitions and formulas. |
| `../docs/claim_boundary_for_extension.md` | Claim-control rules. |
| `precision-mini-lab/experiment_matrix.md` | Precision Mini-Lab experiment matrix. |
| `precision-mini-lab/result_template.md` | Result recording template. |

---

## 3. Implementation phases

### Phase A: Protocol layer

Add protocol and metric documents.

Deliverables:

- `docs/research_extension_v15_2.md`
- `docs/hpls_eval_research_program.md`
- `docs/precision_mini_lab_protocol.md`
- `docs/output_stability_metrics.md`
- `docs/claim_boundary_for_extension.md`

Status: additive only.

### Phase B: Experiment matrix

Add experiment rows for FP32, FP16, INT8, CPU, GPU, possible NPU, and possible TPU paths.

Deliverable:

- `hpls-eval/precision-mini-lab/experiment_matrix.md`

Status: planned rows must stay marked `planned` or `future_protocol` until measured.

### Phase C: Result-recording structure

Add a reusable result template and CSV templates.

Deliverables:

- `hpls-eval/precision-mini-lab/result_template.md`
- `hpls-eval/precision-mini-lab/tables/precision-mini-lab-matrix-template.csv`
- `hpls-eval/precision-mini-lab/tables/output-stability-results-template.csv`

Status: templates only unless filled with measured values.

### Phase D: Lightweight metric script

Add a small utility script for comparing binary reference and target masks.

Deliverable:

- `hpls-eval/precision-mini-lab/scripts/compute_output_stability_metrics_v15_2.py`

Status: helper script; measured results require actual masks and logs.

### Phase E: Public auxiliary page

Add a static page that points reviewers to the research extension without modifying root `index.html`.

Deliverable:

- `research_extension.html`

Status: auxiliary navigation page only.

---

## 4. Work items

| ID | Work item | Output | Completion rule |
|---|---|---|---|
| HPLS-EXT-01 | Define extension charter | `docs/research_extension_v15_2.md` | File exists and separates core vs extension. |
| HPLS-EXT-02 | Define HPLS-Eval program | `docs/hpls_eval_research_program.md` | Research questions and work packages defined. |
| HPLS-EXT-03 | Define Precision Mini-Lab protocol | `docs/precision_mini_lab_protocol.md` | FP32/FP16/INT8 protocol and fallback policy defined. |
| HPLS-EXT-04 | Define output metrics | `docs/output_stability_metrics.md` | Metrics include area, boundary, components, centroid, FP/FN-style regions. |
| HPLS-EXT-05 | Define hardware/domain matrix | `docs/domain_hardware_shift_matrix.md` | CPU/GPU/NPU/TPU and domain tags included. |
| HPLS-EXT-06 | Define claim boundary | `docs/claim_boundary_for_extension.md` | Allowed/prohibited claims and evidence levels defined. |
| HPLS-EXT-07 | Build experiment matrix | `precision-mini-lab/experiment_matrix.md` | Planned rows and future rows defined. |
| HPLS-EXT-08 | Build result template | `precision-mini-lab/result_template.md` | Required metadata and metrics fields included. |
| HPLS-EXT-09 | Add metric helper | `scripts/compute_output_stability_metrics_v15_2.py` | Script reads two masks and emits JSON metrics. |
| HPLS-EXT-10 | Add static extension page | `research_extension.html` | No external libraries or JavaScript required. |

---

## 5. Measurement readiness checklist

Before running a Precision Mini-Lab experiment, confirm:

- input cases are selected and have provenance notes;
- reference FP32 path is chosen;
- threshold policy is fixed;
- target backend is available;
- conversion/calibration steps are documented for INT8;
- outputs will be saved as masks;
- backend logs will be saved;
- fallback status will be recorded;
- metric output path is defined;
- result template will be filled without guessed values.

---

## 6. Result folder recommendation

Use the existing case layout and add measured artifacts only when available:

```text
precision-mini-lab/cases/case-001/
├── inputs/
├── predictions/
│   ├── fp32_reference_mask.png
│   ├── fp16_target_mask.png
│   └── int8_target_mask.png
├── overlays/
│   ├── fp32_vs_fp16_overlay.png
│   └── fp32_vs_int8_overlay.png
├── metrics/
│   ├── fp32_vs_fp16_metrics.json
│   └── fp32_vs_int8_metrics.json
└── notes.md
```

Do not add private datasets or unreviewed images to a public export.

---

## 7. Claim-control checkpoint

Every HPLS-Eval page or result should answer:

1. Is this a protocol, pilot result, small case-set result, or benchmark-level result?
2. Was the reference mask FP32 output or ground truth?
3. Was the target precision actually verified?
4. Was fallback status recorded?
5. Are old LiteRaceSegNet thesis claims still separated from this extension?

If any answer is unclear, label the result as incomplete.
