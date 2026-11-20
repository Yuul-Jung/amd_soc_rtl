# 제1부 교수용 해설서 11장 · 1:1 검증 기록

- 기준 저장소: `Yuul-Jung/amd_soc_rtl`, `main` 시작 SHA `cb057474a9e2cefe9834ebf253e384e5ef5bb511`
- 기준 정책: `Yuul-Jung/soc`의 CURRICULUM/MIGRATION/VALIDATION/COLLABORATION + `rule_md` 교육 HTML 표준.
- 매핑: **P1-01~10** = `part01/legacy/pages/soc/01..10`, **P1-11** = `part01/chapters/11_user_top_io_remap.html`.
- 제출: `easy01/ch01_teacher_v02.html` ~ `ch11_teacher_v02.html` 총 11개, 장별 1개.
- 원본 변경: 없음. 구 41장 11절을 P1-11로 오인하지 않음.
- 07~10장의 `_1_` C 코드 해설 자료 본문과 그림을 각 해당 장에 통합함.
- 기존 학생용 이미지 159개 `<img>` 참조 유지; 04장의 원본 SVG 3개도 보존하고 각 장별 교육용 구조도 보강.
- 코드 블록의 내용 있는 각 줄을 원문 그대로 재표시하고 쉬운 역할 설명을 추가함. AXI/C/RTL 해설은 원본 자료에 근거.

## 실제 정적 검증
- Git Tree에 해당 11개 모두 존재: **PASS**.
- 새로운 해설서 안의 `<img>`, `<script src>`, `<link href>` 대상 자산 경로: **누락 0건 PASS**.
- 각 HTML 상대 `href` 링크가 Git Tree 안에 존재: **누락 0건 PASS**.
- `section` 개시·종료, ID 중복: **11/11 PASS**.
- 코드 복사 버튼·모바일 목차·이미지 화질 등 실제 브라우저 동작: **NOT_RUN**.
- Vivado, Vitis, 실물 Basys3 신규 실행: **NOT_RUN**.

## 판정
기존 학습안내서·그림·소스 원문 보존과 정적 파일 링크 기준 **조건부 통과**. 이전 원본의 하드웨어 성공과 이번 해설서 제작의 성공을 구분. GitHub Pages 별도 게시/시각 확인은 **미검증**.
