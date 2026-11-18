# 제3부 00~31장 — 누적형 RTL·보드 실습 작업 규약

## 0. 기준 문서
- 공통 작업 원칙: `../rule_md/AGENTS.md`
- 교재 표준: `../rule_md/web/education-html/STANDARD.md` (확정 기준, 임의 재디자인 금지)
- FPGA/SoC 설계: `../rule_md/fpga-soc/MBV_SOC_rules.md`
- 코드 규칙: `../rule_md/code/code-development-rules.md`
- 교육과정: `TECHTREE_00_31.md`
- **누적 프로젝트·보드 절차: `PROJECT_LAB_00_31.md` 및 `field_lab_v01.html`**
- 상위 합의: `Yuul-Jung/soc`의 `CURRICULUM.md`, `MIGRATION.md`, `VALIDATION.md`, `COLLABORATION.md`

## 1. 반드시 반영할 4원칙

| 원칙 | 각 장에 반드시 있어야 할 구성 |
|---|---|
| **체계화** | 이전 장 코드/안정 기준선, 이번 장 변경 범위, 입력/출력/자원, 검증 Gate, 다음 장으로 넘기는 파일 |
| **순서화** | 준비 → RTL/TB → Python 정답 → 통합 → Vivado 합성/구현 → 보드/GUI/실제 결과 → 회귀 |
| **구조화** | 실제 모듈명 기반 UART·Controller·NPU Core·AXI·CPU·표시 계층 및 Top 순수 Shell |
| **시각화** | 이전 블록/추가 블록/출력 간 화살표, 실제 신호명과 같은 도식, 보드에서 관찰할 LED/FND/UART |

**작성된 HTML만으로 실습 완료로 판정하지 않는다.** 설명/개념도와 실제 RTL/Bitstream은 구분한다.

## 2. 누적 4단계

- 00~12: `mini_npu`의 기존 4분류 원형 **보존**. 기존 ch01~ch10 원본 RTL과 과거 PASS 로그 보존.
- 13~19: 4PE·Dense·MLP·타일 누산을 하나의 10분류 공통 NPU 프로젝트에 **누적**. 새 코어/Top은 실제 로컬 구현을 우선 확인.
- 20~27: 검증된 10분류 코어와 제1부 MicroBlaze V 설계를 가져와 **독립** SoC 프로젝트에서 AXI IP·BD·Vitis C를 누적. 성공 XPR 원본 변경 금지.
- 28~31: 27장 공통 SoC를 기준선으로 각기 다른 응용을 **분기**. 모터 보호/보안 인증을 AI가 수행한다고 주장하지 않는다.
- 32장 이후 과제는 이번 과정의 범위 밖.

장 번호마다 별도 Vivado 프로젝트를 새로 만들지 않는다. 명백한 시스템 경계에서만 독립 프로젝트/복제본을 만든다. 이미 존재하는 로컬 작업이 있다면 그 실제 경로/RTL/검증 기록을 먼저 대조하고 **중복 생성하지 않는다.**

## 3. HTML 실습 절차 필수 항목

각 장의 `<section id="cumulative-lab">`에는 다음을 유지한다.
1. 이전 장에서 유지할 실제 RTL·블록
2. 새로 추가/수정할 RTL·Controller·입출력
3. VS Code 명령/TB 및 예상 출력
4. **실제 Vivado/Vitis GUI 단계**, 필요한 장에서는 Bitstream/ELF/Program Device
5. Basys3에 보내는 테스트 입력·UART 응답·LED/FND 출력의 관찰 기준
6. 다음 장에서 재사용할 소스/비트스트림/로그와 Git SHA

보드 확인이 그 장에서 불가능한 경우에는 후속 통합 장으로 연결하고 실제 보드 PASS를 적지 않는다. GUI 경로나 사용자 Top/BD/주소/핀은 실제 Vivado 소스와 불일치하면 게시 전 수정한다. 교재 본문에는 제작 메모와 검증 담당자 대화 내용을 넣지 않는다.

## 4. 검증·안전·승인

- `HOST_MODEL_PASS` ≠ `RTL_SIM_PASS` ≠ `SYNTH_TIMING_PASS` ≠ `BOARD_PASS` ≠ `WEB_PASS`.
- RTL이 없는 장에는 실제 코드·시뮬레이션·보드 성공을 주장하지 않는다.
- 사용자 Top에는 기능 로직을 넣지 않는다. 실제 변수/모듈명과 도식을 일치시킨다.
- 비트 폭·Overflow·Bias 중복·AXI 핸드셰이크·Reset/CDC·외부 3.3V 전압·안전 인터록을 실제 코드/공식 자료로 확인한다.
- 이미 결정된 13~19장 연산 구조나 31장 범위를 다시 승인 요청하지 않는다. 다만 안전/보안·돌이킬 수 없는 데이터 손실·성공 원본 파괴나 명세 충돌은 사용자 확인을 우선한다.
- 검증 로그와 source SHA를 확보하기 전까지 완성으로 판정하지 않는다.

## 5. 작업 종료 보고

매 장마다 `이전 결과 → 추가 RTL → 시험 벡터 → 시뮬레이션 → 합성/보드 → 인계` 표를 남긴다. GitHub 반영은 작업자 역할·승인 범위를 따른다.
