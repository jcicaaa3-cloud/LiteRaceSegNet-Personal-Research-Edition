# Manifest: Research Extension Layer v15.2

**Package:** LiteRaceSegNet v15.2 Personal Research Edition
**Layer type:** additive research-extension package
**Generated:** 2026-05-26

This manifest lists files included in the research-extension layer. It does not change the claim boundary of the main LiteRaceSegNet project.

## Core public files

The following files define the main public review surface:

- `README.md`
- `README_KO.md`
- root `index.html`
- existing GitHub Pages files
- existing polished docs
- existing README/HTML assets
- existing manifests and changelogs

## Research-extension files

| File | Purpose | Replaces existing file? | SHA-256 |
|---|---|---:|---|
| `docs/claim_boundary_for_extension.md` | Claim boundary and evidence-level rules. | No | `e122ce5fb356f2fef86ade9850b1eed18b8075758dca56db865bc7245af2c000` |
| `docs/domain_hardware_shift_matrix.md` | Domain and hardware-shift matrix, including CPU/GPU/NPU/TPU future protocol. | No | `cd9072de33bdd473ba806a7311d53d53015ab4c29fcab220a990210705058ff7` |
| `docs/hpls_eval_research_program.md` | HPLS-Eval research program design. | No | `ff83ea0bd0ae64637201ca2a04404db20f381da0fc74693d07fd1d55de5a3624` |
| `docs/output_stability_metrics.md` | Formal output-stability metric definitions. | No | `04c28a8bcbcfe3379b72d9f580525404a3c46fc6bc75575d733c35f68b1b50e9` |
| `docs/precision_mini_lab_protocol.md` | FP32 / FP16 / INT8 Precision Mini-Lab protocol. | No | `a108c2a3ae92c47a95a500c77f07d035da9d2aa320b3ee22ef1a085c26a3a1ea` |
| `docs/research_extension_v15_2.md` | Top-level research-extension charter. | No | `4e28be33aeeadb5018aaa94b224a67bbe48ee7dd923118808169be451764a2aa` |
| `hpls-eval/extension_plan_v15_2.md` | HPLS-Eval implementation plan. | No | `fbb4631bfb612e77e8d9ae9137949f51a1fd480e04502d9c8f0e42020850672d` |
| `hpls-eval/precision-mini-lab/experiment_matrix.md` | Precision Mini-Lab experiment matrix. | No | `541cf88e8442035f369b25a6ef1e37583bd16110e79f1101dec1c3cf345a9887` |
| `hpls-eval/precision-mini-lab/result_template.md` | Result-recording template. | No | `5aaf13608acc77539573ed22d027bd286d3b6ef113936c1bfeafa4477dfe7c47` |
| `hpls-eval/precision-mini-lab/scripts/README_output_stability_metrics_v15_2.md` | Usage notes for metric helper script. | No | `e1ecc558bb25bbc6a4aedea53b1aa53a8fe13901c42220a6ec5ab3ffa800598c` |
| `hpls-eval/precision-mini-lab/scripts/compute_output_stability_metrics_v15_2.py` | Mask-comparison metric helper script. | No | `c5e493b34e6f82304f67016c4af7bb131cc79e7a75bcf707b4765874b5c840cc` |
| `hpls-eval/precision-mini-lab/tables/output-stability-results-template.csv` | CSV result template. | No | `fe75fdfca60d12bfbed6b5d8ddd94e50780ad49a93fa5e177d8b723f40daf561` |
| `hpls-eval/precision-mini-lab/tables/precision-mini-lab-matrix-template.csv` | CSV matrix template. | No | `7712393b03a10ec612deb188288782b5de7693c20299717248cb6bac23ca66c9` |
| `research_extension.html` | Static auxiliary GitHub Pages page for the extension. | No | `d97dd34a1aabd4a7973e6fba2a76bcb3741a6ff90be2088f51ba91c7b6c61fd1` |

## Required files from user request

- `docs/research_extension_v15_2.md`
- `docs/hpls_eval_research_program.md`
- `docs/precision_mini_lab_protocol.md`
- `docs/domain_hardware_shift_matrix.md`
- `docs/output_stability_metrics.md`
- `docs/claim_boundary_for_extension.md`
- `hpls-eval/extension_plan_v15_2.md`
- `hpls-eval/precision-mini-lab/experiment_matrix.md`
- `hpls-eval/precision-mini-lab/result_template.md`
- `MANIFEST_RESEARCH_EXTENSION.md`

## Additional support files

- `research_extension.html`: auxiliary GitHub Pages page; root `index.html` remains unchanged.
- `hpls-eval/precision-mini-lab/scripts/compute_output_stability_metrics_v15_2.py`: optional metric helper script.
- CSV templates under `hpls-eval/precision-mini-lab/tables/`: optional structured recording aids.

## Application rule

Add these files to the repository as new files only. Do not stage modifications to protected original files.

## Rollback

Rollback is deletion of the files listed in this manifest. No original file should need restoration because the extension is additive-only.
