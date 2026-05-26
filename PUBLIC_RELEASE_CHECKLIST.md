# Public Release Checklist

## Public surface

- [ ] `README.md` starts with `LiteRaceSegNet Personal Research Edition`.
- [ ] `README_START_HERE.md` is present at repository root.
- [ ] `index.html` is the GitHub Pages entry point.
- [ ] Browser title, hero, navigation, repository description, and landing cards use v15.2 Personal Research Edition identity.

## Research extension

- [ ] `docs/research_extension_v15_2.md` is present.
- [ ] `docs/hpls_eval_research_program.md` is present.
- [ ] `docs/precision_mini_lab_protocol.md` is present.
- [ ] `docs/output_stability_metrics.md` is present.
- [ ] `docs/domain_hardware_shift_matrix.md` is present.
- [ ] `docs/claim_boundary_for_extension.md` is present.
- [ ] `hpls-eval/precision-mini-lab/experiment_matrix.md` is present.
- [ ] `hpls-eval/precision-mini-lab/result_template.md` is present.
- [ ] `hpls-eval/precision-mini-lab/scripts/compute_output_stability_metrics_v15_2.py` is present.

## Safety and privacy

- [ ] No nested ZIP files.
- [ ] No `.pem`, `.env`, `.pt`, `.pth`, `.ckpt`, `.onnx`, `.pkl`, `id_rsa`, or `id_ed25519` files.
- [ ] No raw private dataset.
- [ ] No checkpoint or pretrained-weight bundle.
- [ ] No local machine path traces.
- [ ] No credential bundle.

## GitHub Pages

- [ ] Deploy from branch: `main`.
- [ ] Folder: `/root`.
- [ ] Expected entry: `index.html`.
- [ ] `.nojekyll` is present.
