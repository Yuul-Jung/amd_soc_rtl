# system_verilog_uvm_tb 작업 규칙

1. 중앙 정본: https://github.com/Yuul-Jung/rule_md (특히 `AGENTS.md`).
2. HTML: https://github.com/Yuul-Jung/rule_md/blob/d1b8278d41fca8f5e3960736f3ac9d377e462fda/web/education-html/STANDARD.md
3. 코드: `code/code-development-rules.md`, `common/code-style-rules.md`, 구조도: `common/flowchart-rules.md`.
4. 원본 `part01/`, `part02*/`, `part03/`의 RTL·XPR·BD·테스트 및 기존 교재는 절대 수정하지 않는다.
5. 검증용 TB·스크립트는 독립 폴더에만 작성, 실제 DUT 포트와 정확히 일치시킨다.
6. 실행하지 않은 RTL_SIM은 반드시 NOT_RUN, 교육용 예상 출력은 실제 로그와 구별한다.
7. INDEX는 발행된 장만 링크, 계획된 장에 깨진 링크 금지. 각 장별 버전 `_vNN.html`.
8. 1장 2시간은 60분 단위 두 구간으로 구성, 코드·실행 결과·구문별 풀이·검증 순서 유지.
9. 민감정보·계정·로컬 절대경로·토큰·비공개 소스를 공개 결과물에 포함하지 않는다.
