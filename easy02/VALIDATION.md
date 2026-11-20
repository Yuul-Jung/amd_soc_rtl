# 제02장 교수용 60분×2 해설서 — 적대적 검증 (2026-11-20)

## 검토 대상 및 기준
- 원본: `part01/legacy/pages/soc/02_clock_reset_processor_system_reset.html` (Git Blob SHA `8e5ecbfeb4c38c5fad150b5092bdc3bd5a69840d`)
- 원본 이전 실험 근거: `part01/legacy/validation/SOC02_VALIDATION.txt` (Blob SHA `895bcdbb86e0b61d6a045d9178d813609a241963`)
- 규칙: `AGENTS.md`, `rule_md/web/education-html/STANDARD.md`, `rule_md/fpga-soc/MBV_SOC_rules.md`
- 제01장 연속성: `soc01_mb_bram.bd` 내 기존 CPU·16 KiB Local BRAM을 보존하고 `clk_wiz_1`와 `rst_clk_wiz_1_100M`의 외부 연결 진행.

## 결과
| 파일 | 역할 | 정적 판정 |
|---|---|---|
| `easy02/ch02_hour01_teacher_v01.html` | 60분: 프로젝트 인계 → Clock 100 MHz → 외부 포트 → Processor System Reset → 신호 경로 | PASS |
| `easy02/ch02_hour02_teacher_v01.html` | 60분: XDC 1행씩 → Validate → HDL Wrapper → Synthesis/Implementation/Bitstream → Timing·Warning | PASS |
| `easy02/index.html` | 제02장 각 교시 탐색 및 제01장·제03장 연결 | PASS |
| `easy01/index.html` | 기존 제01장 안내에 제02장 1·2교시 링크 추가 | PASS |

## 적대적 검증 — 오류·혼동 방지

1. **P0 전기·핀:** Basys3 Clock W5/100 MHz, Reset BTNC U18, LVCMOS33, `clk`/`btnC`의 BD/XDC 이름 대응을 원본과 대조. 수업 중 실제 핀은 재확인(PASS: 문서 일치, 실물 새 검증 없음).
2. **P1 설계 인스턴스:** `clk_wiz_1/clk_in1`, `clk_out1`, `locked`, `rst_clk_wiz_1_100M/dcm_locked`, `ext_reset_in`, `mb_reset`, `microblaze_riscv_0/Clk`·`Reset` 이름이 원본 02장과 대응(PASS: 문서 대조).
3. **P1 Reset 극성:** BTNC Active-High와 `peripheral_aresetn` 등 Active-Low 신호를 구분. 일반 버튼 디바운싱을 Processor System Reset이 전부 처리한다고 설명하지 않음(PASS: 문서 대조).
4. **P1 중복 제약:** 원본 02장 최종 실행 기준의 `create_clock`는 `-add`를 제거하고 `-period 10.00`을 보존함. 중간 상태에서 Clock 제약을 주석 처리한 것을 최종 해결책으로 제시하지 않음(PASS).
5. **P1 성공 범위:** `Validation successful`·Bitstream 생성과 실제 C/ELF/보드 실행을 구분. 원본의 WNS +1.372 ns, Critical Warning 0·일반 Warning 5건은 과거 실행 기록임을 명시(PASS).
6. **P2 HTML 구조:** HTML·head·body·header·main·aside·nav·section·table·svg·figure·pre·script 여닫힘 수가 일치, 모든 `href="#..."` 목차 대상 존재(PASS).
7. **P2 탐색·코드:** INDEX/이전·다음 상대경로, 원본 이미지 `../part01/legacy/images/soc02_vivado_final_2024_2.png` 경로 표기, `data-copy`의 XDC/Tcl 코드와 JavaScript 복사 핸들러 존재(PASS: 정적 점검).
8. **P2 예제/실행 기록:** 공식 매뉴얼 그림·원본 실제 GUI 캡처·교육용 SVG 개념도·과거 측정값을 서로 구분(PASS).

## 미검증 항목 및 제한
- GitHub API를 통한 정적 파일 존재/코드/목차 확인과 실제 브라우저에서의 이미지·폰트·반응형 레이아웃 렌더링은 다름. **실브라우저 320/390/768/1024/1366/1920 px 검사 NOT_RUN**.
- 코드 복사 버튼, 메뉴 닫기(Escape), 키보드 접근성의 **실제 상호작용 테스트 NOT_RUN**.
- 새 Vivado 2024.2 실행, 합성·구현·비트스트림 재생성, 보드 프로그램, 실제 C 실행 **NOT_RUN**. 원본의 성공 기록을 이번 수행 성공으로 보고하지 않음.
- 2교시 Synthesis·Implementation·Bitstream 수행 시간은 도구·PC 환경에 따라 변한다. 수업 시간 편성은 운영 예시이며 실측 소요시간 보증 아님.
- GitHub Pages 배포·실접속 화면 **NOT_RUN**.

## 판정
- **정적 HTML·원본 설정 정합성: 조건부 통과**
- **실제 브라우저/실물/새 도구 실행: 미검증**
- 원본 `soc`, `amd_soc`, `part01/legacy`, 성공 RTL/C/XDC/XPR/BD/Wrapper는 수정하지 않음.
