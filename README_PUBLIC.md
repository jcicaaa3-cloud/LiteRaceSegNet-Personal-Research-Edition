# LiteRaceSegNet Personal Research Edition

**v15.2 Personal Research Edition** is a static research-portfolio package for lightweight road-damage semantic segmentation and a follow-up output-stability research program.

The core project remains LiteRaceSegNet. The extension layer adds HPLS-Eval, Precision Mini-Lab, and a planned FP32 / FP16 / INT8 segmentation-comparison protocol. This is a public research package, not a browser inference service.

## Public navigation

| Entry | Purpose |
|---|---|
| `index.html` | GitHub Pages overview and navigation. |
| `pages/architecture.html` | LiteRaceSegNet core architecture summary. |
| `pages/output-stability.html` | Output-stability metrics and interpretation. |
| `pages/hpls-eval.html` | HPLS-Eval follow-up program. |
| `pages/precision-mini-lab.html` | FP32 / FP16 / INT8 pilot protocol. |
| `pages/repository.html` | Repository map and included/excluded material. |
| `pages/license.html` | Public release scope and claim boundary. |
| `pages/qa-guide.html` | Review and presentation Q&A. |

## Research-extension scope

The v15.2 layer records protocols and templates for:

- mask area drift;
- boundary IoU drift;
- connected component delta;
- centroid shift;
- target-only and reference-only regions;
- runtime backend and execution provider;
- fallback status;
- CPU / GPU / possible NPU / possible TPU hardware-shift protocol.

## Evidence rule

Measured values must be tied to logs, masks, settings, hardware, runtime backend, and case IDs. Unmeasured rows stay `TBD`, `planned`, `template`, or `future_protocol`.

Historical evidence may be referenced only with its original context. It must not be presented as a new v15.2 measurement.

## Public surface rule

The current first-entry files use Personal Research Edition naming so the public surface stays focused and reviewer-friendly.
