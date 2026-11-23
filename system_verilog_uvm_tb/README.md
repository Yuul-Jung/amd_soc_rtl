# RTL Testbench · SystemVerilog · UVM 검증 학습안내서

- **전체 편성:** 독립 6부, 총 24장/48시간, 한 장은 60분 × 2회로 진행
- **발행:** [INDEX](index.html) / [제01장](ch01_testbench_basics_v01.html) / [제02장](ch02_clock_reset_events_v01.html) / [제03장](ch03_reusable_stimulus_v02.html) / [제04장](ch04_pass_fail_automation_v02.html) / [제05장](ch05_verification_types_v02.html) / [제06장](ch06_arrays_queues_packages_v02.html) / [전체 편성](CURRICULUM.md)
- **원본 RTL:** 제01장은 `part03/common/rtl/uart_echo_controller.v`, 제02~03장은 `part02_1/ch04/rtl/pwm_core.v`를 읽기 전용 DUT로 사용
- **목표:** 문법 → Testbench → Self-checking → SVA/Coverage → UVM → Regression/CI
- **상태:** 제01~06장 HTML·교육용 TB·실행 스크립트 발행. 제04장 RTL 시뮬레이션은 **NOT_RUN** (제작 환경에 Icarus 실행기 없음).

## 규칙
- 정본 [rule_md](https://github.com/Yuul-Jung/rule_md) / [HTML STANDARD](https://github.com/Yuul-Jung/rule_md/blob/d1b8278d41fca8f5e3960736f3ac9d377e462fda/web/education-html/STANDARD.md)
- 기존 `amd_soc_rtl`의 `AGENTS.md`와 [공통 코드 스타일](https://github.com/Yuul-Jung/rule_md/blob/d1b8278d41fca8f5e3960736f3ac9d377e462fda/common/code-style-rules.md) 적용
- 원본 수정 금지, 공개 보안 점검, 실행 기록 기반으로만 PASS 표기, 장별 `_vNN.html` 사용

## 제01~06장 실행 (Ubuntu)
```bash
# 기존 저장소 루트 내부의 독립 과정 폴더에서 실행
cd system_verilog_uvm_tb
sudo apt update
sudo apt install -y iverilog
bash scripts/run_ch01.sh
bash scripts/run_ch02.sh
bash scripts/run_ch03.sh
bash scripts/run_ch04.sh
bash scripts/run_ch05.sh
bash scripts/run_ch06.sh
```

별도 복제 저장소에서도 실행할 수 있습니다.
```bash
DUT_PATH=/실제/RTL/경로/uart_echo_controller.v bash scripts/run_ch01.sh
DUT_PATH=/실제/RTL/경로/pwm_core.v bash scripts/run_ch03.sh
```

`.build/`는 로컬 생성물이며 GitHub에 올리지 않습니다. 온라인 학습안내서는 `index.html`로 시작합니다.

## HTML 레이아웃·내비게이션 보정
- 제03~06장 `_v02.html`: 누락된 `<main class="content" id="main-content">` 영역을 복구하고, 좌측 세부 절 탐색이 `main section[id]`를 정상 식별하도록 수정.
- INDEX와 `course.json`을 최신 발행 장에 맞춰 동기화. 디자인·기존 RTL·실습 코드 변경 없음.
- 실제 GitHub Pages HTTP 접속은 별도로 확인해야 하며, 저장소 파일 존재를 공개 사이트 정상 구동과 혼동하지 않는다.

## 좌측 목차 체계
`PART(부) → CHAPTER(장) → SECTION(절)`의 계층을 사용합니다. 현재 페이지의 PART는 상단에 한 번만 표시하고, 해당 PART의 CHAPTER 아래 현재 장 SECTION을 들여씁니다. 전체 6개 PART와 24장 편성은 INDEX에서 확인할 수 있습니다. 공통 스타일의 로컬 확장으로 `assets/site.js`와 `assets/site.css`에서 구현합니다.
