# LiteRaceSegNet Personal Research Edition

이 저장소는 **LiteRaceSegNet Personal Research Edition**입니다. v15.2 연구 확장 레이어를 포함하며, 핵심 주제는 경량 road-damage semantic segmentation, HPLS-Eval, Precision Mini-Lab, 그리고 segmentation-output stability analysis입니다.

## 먼저 볼 파일

1. `README_START_HERE.md` — 전체 읽는 순서.
2. `index.html` — GitHub Pages용 첫 화면.
3. `docs/research_extension_v15_2.md` — 연구 확장 구조.
4. `docs/output_stability_metrics.md` — output-stability metric 정의.
5. `hpls-eval/precision-mini-lab/result_template.md` — 결과 기록 템플릿.

## 해석 기준

LiteRaceSegNet 본체는 road-damage segmentation의 core로 유지합니다. HPLS-Eval과 Precision Mini-Lab은 별도 후속 연구 축입니다. 새로 측정하지 않은 값은 measured라고 쓰지 않고 `TBD`, `planned`, `template`, `protocol` 상태로 둡니다.

## 공개 범위

이 패키지는 static portfolio입니다. raw dataset, checkpoint, pretrained weight, credential, browser inference, upload flow, API call은 포함하지 않습니다.
