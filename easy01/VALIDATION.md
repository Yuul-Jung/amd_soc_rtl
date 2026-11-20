# 제01장 교수용 60분×2 해설서 — 적대적 검증 기록 (2026-11-20)

## 기준
- 저장소: `Yuul-Jung/amd_soc_rtl`; 작업 기준 `main`: `006d3c607fbf47c0a405b3571b2246bc098a511e`
- 정본 학습안내서: `part01/legacy/pages/soc/01_microblaze_bram_minimal_soc.html` (Blob `2284fb1fd2189126fef3e7637e77a833c2422639`)
- 원본 보존: `part01/legacy`, 기존 `easy01/ch01_microblaze_bram_teacher_v01.html` 변경 없음
- 규칙: `AGENTS.md`, `rule_md/web/education-html/STANDARD.md`, `rule_md/fpga-soc/MBV_SOC_rules.md`

## 산출물
| 파일 | 역할 | 정적 점검 |
|---|---|---|
| `easy01/ch01_hour01_teacher_v01.html` | 1교시: CPU/BRAM 원리, IP와 메모리 경로, Vivado 프로젝트/BD 생성 | PASS |
| `easy01/ch01_hour02_teacher_v01.html` | 2교시: MicroBlaze V IP, 16KiB BRAM, Block Automation, XDC 줄별 설명, BD 저장 | PASS |
| `easy01/index.html` | 1·2교시 및 01장 통합본 탐색 | PASS |

## 독립 정적 점검
1. 각 HTML의 필수 `html/head/body/section/table/svg` 여닫힘 수: 일치(PASS).
2. 장별 절 탐색 `href="#..."`에 대응하는 `id`: 누락 없음(PASS).
3. 1교시 주요 문자열: `soc01_microblaze_bram.xpr`, `soc01_mb_bram.bd`, ILMB, DLMB, 100MHz 포함(PASS).
4. 2교시 주요 문자열: `Run Block Automation`, `16 KB`, `clk_wiz`, `W5`, `U18`, `create_clock` 포함(PASS).
5. 2교시 XDC 복사 버튼과 스크립트: 정적 연결 확인(PASS), 브라우저 실제 복사는 미실행.
6. 기존 사진 경로를 `../part01/legacy/images/common/`으로 유지하고 1·2교시 및 INDEX 링크 연결(PASS: 경로 문법/문자열).
7. 01장 교육 경계: BD 저장까지. 외부 Clock/Reset과 Validate, Synthesis, Bitstream은 02장으로 이동해 구형 Markdown 자료의 장 경계와 혼합하지 않음(PASS).
8. 원본 HTML, RTL, C, XDC, XPR, BD와 기본 성공 프로젝트는 이번 작업에서 **수정하지 않음**.

## 반례 확인 및 잔여 제한
- 혼동 위험 P1: 기존 `docs/soc01.md`에 남아 있는 01장 합성/구현 절차를 그대로 이식할 경우 최신 HTML과 충돌한다. **미반영**하고 최신 학습안내서 장 경계를 기준으로 했다.
- P2: 기존 교수용 통합본은 독립적으로 보존하며 60분×2 파일로 분할. 원본을 덮어쓰지 않았음.
- 브라우저 320/390/768/1024/1366/1920px 실측, 복사 버튼·Escape·모바일 메뉴 실동작, 이미지 실제 렌더링: **미검증**.
- Vivado 2024.2 재실행, RTL 시뮬레이션, 합성, 실물 Basys3 측정: **미실행**. 기존 제1부 검증 이력의 대체가 아님.
- 최종 GitHub Pages 온라인 배포 및 접속 점검: **미검증**.

## 최종 판정
- **교수용 교재 본문/정적 연결: 조건부 통과**
- **실제 브라우저/개발 도구/보드 재현: 미검증**
- 새 실습 증거가 없는 부분을 PASS로 선언하지 않음.
