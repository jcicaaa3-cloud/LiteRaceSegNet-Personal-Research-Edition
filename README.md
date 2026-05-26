# LiteRaceSegNet Personal Research Edition

This repository is **LiteRaceSegNet Personal Research Edition**. It includes the **v15.2 research extension layer** for lightweight road-damage semantic segmentation, HPLS-Eval, Precision Mini-Lab, and segmentation-output stability analysis.

Start here:

1. `README_START_HERE.md` — shortest reading route.
2. `index.html` — static GitHub Pages entry.
3. `docs/research_extension_v15_2.md` — research-extension charter.
4. `pages/output-stability.html` and `docs/output_stability_metrics.md` — metric definitions.
5. `hpls-eval/precision-mini-lab/experiment_matrix.md` — planned FP32 / FP16 / INT8 comparison matrix.

## Current public identity

| Field | Value |
|---|---|
| Project | LiteRaceSegNet Personal Research Edition |
| Edition | v15.2 Personal Research Edition |
| Core | Lightweight road-damage semantic segmentation |
| Extension | HPLS-Eval / Precision Mini-Lab |
| Protocol | FP32 / FP16 / INT8 segmentation-output stability comparison |
| Boundary | Static portfolio; no raw dataset, checkpoint, credential bundle, browser inference, or upload flow |

## Repository purpose

LiteRaceSegNet remains the core road-damage segmentation project. The v15.2 extension layer adds a separate follow-up research program for output-stability analysis under precision, runtime, hardware, and domain shifts.

The extension asks practical research questions:

- Does mask area drift after precision/backend conversion?
- Does boundary IoU drift when comparing a target mask against an FP32 reference?
- Do connected components split, merge, disappear, or appear as small target-only regions?
- Does the centroid shift when output masks change?
- Did the runtime actually use the intended backend, or did it fall back silently?

## What is new in this public portal merged package

- New public `README.md`, `README_START_HERE.md`, and `README_PUBLIC.md` for v15.2 first-entry clarity.
- New static GitHub Pages structure with card navigation, quick facts, dark mode, and KO / JA / EN language panel.
- New output-stability, HPLS-Eval, Precision Mini-Lab, repository-scope, license/scope, and QA pages.
- Research-extension docs and result templates remain available under `docs/` and `hpls-eval/`.
- The public surface is kept focused on the current Personal Research Edition entry and selected public-safe references.

## How to read measured values

This package does not relabel old measurements as new v15.2 measurements. Any value not newly measured under the v15.2 extension protocol should remain `TBD`, `planned`, `template`, or `protocol`.

If historical reference evidence is imported later, label it as historical reference evidence and keep its original measurement context visible. Do not present it as a new v15.2 measurement.

## Claim boundary

Allowed claim:

> LiteRaceSegNet Personal Research Edition provides a static research-portfolio package and a structured v15.2 follow-up protocol for segmentation-output stability analysis.

Not allowed:

- clinical validation;
- diagnostic evidence;
- deployment readiness;
- complete quantization benchmark;
- hardware-independent robustness;
- universal model superiority;
- measured v15.2 results without actual logs and artifacts.

## Public release scope

Included: static pages, public documentation, research-extension protocol files, metric definitions, result templates, selected source references, selected diagrams, license/scope notes, and the HPLS-Eval / Precision Mini-Lab extension structure.

Excluded: raw private datasets, checkpoints, pretrained weights, `.env` files, `.pem` files, cloud credentials, local machine artifacts, nested ZIP files, and temporary folders.

## GitHub Pages deployment

Use root deployment:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```

Expected entry point:

```text
index.html
```
