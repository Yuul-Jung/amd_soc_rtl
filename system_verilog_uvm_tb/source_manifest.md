# Source Manifest
- **과정:** `system_verilog_uvm_tb`
- **검증 DUT:** `Yuul-Jung/amd_soc_rtl/part03/common/rtl/uart_echo_controller.v`
- **검증 DUT Blob SHA:** `28160c34522e47fbd961466651598da063bc74ae`
- **원본 출처:** `amd_soc_rtl` 기본 브랜치(첫 작성 시 확인)
- **접근:** 복사·변경 없이 상대경로 또는 `DUT_PATH` 환경변수로 참조
- **교육용 새 파일:** `tb/ch01/tb_uart_echo_basics.sv`, `scripts/run_ch01.sh`
- **기준 규칙:** `Yuul-Jung/rule_md` @ `d1b8278d41fca8f5e3960736f3ac9d377e462fda`
- **시뮬레이션:** NOT_RUN (작성 환경에서 Icarus Verilog 실행 미실시)

## 제02장 · PWM 코어 재사용
- **검증 DUT:** `part02_1/ch04/rtl/pwm_core.v`
- **DUT 원본 Blob SHA:** `e813f3fb107bd327054d11e0b397817b8e7bd813`
- **원본 유지:** 원본 파일을 읽기 전용으로 참조한다. 기존 RTL·타이밍·포트를 변경하지 않는다.
- **신규 파일:** `tb/ch02/tb_pwm_clock_reset.sv`, `scripts/run_ch02.sh`, `ch02_clock_reset_events_v01.html`.
- **파라미터:** `RESET_PERIOD=8` (TB 인스턴스에서만 지정), 10ns 클록.
- **검증 시점:** 설정 Shadow 저장 t=35ns, Active 적용 t=95ns, 리셋 재인가 t=190ns와 내부 레지스터 초기화 t=195ns.
- **실행 상태:** NOT_RUN (제작 환경에서 Icarus를 실행하지 못해 실제 로그·VCD가 없음). 기대값은 별도 순차/조합 논리 대조.

## 제03장 · PWM 반복 자극 검증
- **검증 DUT:** `part02_1/ch04/rtl/pwm_core.v` (기존 제02장과 동일한 원본)
- **DUT 원본 Blob SHA:** `e813f3fb107bd327054d11e0b397817b8e7bd813`
- **작업 범위:** `system_verilog_uvm_tb/` 내부에서만 TB·HTML·실행 스크립트 작성. 원본은 읽기 전용.
- **신규 파일:** `tb/ch03/tb_pwm_reusable_stimulus.sv`, `scripts/run_ch03.sh`, `ch03_reusable_stimulus_v01.html`
- **TB 설정:** `RESET_PERIOD=8`, `cfg_period=8`, `cfg_duty` 0·2·4·6·8, 10ns 클록, `cfg_polarity=0`, `cfg_enable=1`.
- **학습 문법:** `task`, `function`, `repeat`, `for`, `wait`; 설정 요청·적용·관찰 흐름 분리.
- **검증 수준:** HTML·본문·TB 포트 정적 검증 완료. Icarus 컴파일/실행·VCD·실브라우저는 **NOT_RUN**.
