#!/usr/bin/env python3
"""제3부 코드·교재 파일 정합성 정적 검사. RTL 시뮬레이션이 아님."""
from __future__ import annotations
import hashlib
import json
import re
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P3 = ROOT / "part03"
issues = []
verified = 0


def check(condition: bool, message: str):
    global verified
    verified += 1
    if not condition:
        issues.append(message)


course = json.loads((P3 / "course.json").read_text(encoding="utf-8"))
chapters = course["chapters"]
# (변경) 정규 범위는 준비 00장 + 01~31장이다. ch32 이상은 별도 확장이다.
check(len(chapters) == 32, "제3부 00~31장: 32개 페이지가 필요합니다.")
check([x["number"] for x in chapters] == list(range(32)),
      "장 번호가 00~31 연속이어야 합니다.")
check([x["id"] for x in chapters] == [f"ch{i:02d}" for i in range(32)],
      "차시 ID가 ch00~ch31 연속이어야 합니다.")
check(all(not x["file"].startswith("ch32") for x in chapters),
      "32장 이후 확장 자료는 정규 제3부 범위 밖입니다.")
for chapter in chapters:
    page = P3 / chapter["file"]
    check(page.is_file(), "HTML missing " + str(page))
    if page.is_file():
        body = page.read_text(encoding="utf-8")
        check('data-chapter="' + chapter["id"] + '"' in body,
              "HTML data-chapter wrong: " + chapter["file"])
        check(body.count('<section class="section"') >= 5,
              "실습 섹션이 부족함: " + chapter["file"])
        check("../assets/education/site.css" in body,
              "중앙 CSS 누락 " + chapter["file"])
        check("../assets/education/site.js" in body,
              "좌측 탐색 JS 누락 " + chapter["file"])
        # (추가) 누적 실습 인계와 실제 보드 절차 링크가 모든 장에 존재해야 한다.
        check('id="cumulative-lab"' in body,
              "Cumulative learning section missing: " + chapter["file"])
        check('field_lab_v01.html#' in body,
              "Board procedure link missing: " + chapter["file"])

# (추가) 누적 프로젝트 4단계와 Basys3 실습 안내서는 31장 전체의 공통 선수자료다.
check((P3 / "PROJECT_LAB_00_31.md").is_file(),
      "Cumulative project map missing")
check((P3 / "field_lab_v01.html").is_file(),
      "Board practice guide missing")
check((P3 / "index.html").is_file(), "index.html missing")
if (P3 / "index.html").is_file():
    index_html = (P3 / "index.html").read_text(encoding="utf-8")
    for chapter in chapters:
        check(chapter["file"] in index_html,
              "INDEX navigation missing: " + chapter["file"])

# (추가) href/src의 실제 상대경로 및 페이지 내 앵커를 검사한다.
# HTML 내 CSS 이미지 URL은 속성 링크가 아니므로 비공개 원본 주소도 별도로 거부한다.
class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == "id" and value:
                self.ids.add(value)
            if name in ("href", "src") and value:
                self.urls.append(value)


link_checks = 0
for page in [P3 / "index.html", P3 / "field_lab_v01.html",
             *(P3 / ch["file"] for ch in chapters)]:
    if not page.is_file():
        continue
    body = page.read_text(encoding="utf-8")
    parser = LocalLinks()
    parser.feed(body)
    check(
        "https://raw.githubusercontent.com/Yuul-Jung/amd_soc/main/part03/assets/hero-bookshelf.jpg"
        not in body,
        "Private hero image URL: " + str(page)
    )
    for raw in parser.urls:
        if raw.startswith("//"):
            continue
        url = urlsplit(raw)
        if url.scheme:
            continue
        if not url.path:
            if url.fragment:
                link_checks += 1
                check(unquote(url.fragment) in parser.ids,
                      f"Broken in-page anchor: {page} -> {raw}")
            continue
        link_checks += 1
        target = (page.parent / unquote(url.path)).resolve()
        check(target.is_relative_to(ROOT) and target.is_file(),
              f"Broken relative link: {page} -> {raw}")
        # (추가) 다른 HTML의 섹션을 가리키는 경우 해당 앵커까지 실재 확인한다.
        if target.is_relative_to(ROOT) and target.is_file() and (
                target.suffix.lower() == ".html" and url.fragment):
            target_parser = LocalLinks()
            target_parser.feed(target.read_text(encoding="utf-8"))
            check(unquote(url.fragment) in target_parser.ids,
                  f"Broken cross-page anchor: {page} -> {raw}")

for n in range(1, 11):
    chapter = P3 / f"ch{n:02d}"
    manifest = chapter / "validation/source_sha256.txt"
    check(manifest.is_file(), f"CH{n:02d}: 검증 원본 해시 누락")
    if not manifest.is_file():
        continue
    # 원본 기록에는 의존성 장의 이전 소스 SHA도 포함돼 있으므로 모두 확인한다.
    for line in manifest.read_text().splitlines():
        entry = line.split(maxsplit=1)
        if len(entry) != 2:
            issues.append(f"Invalid manifest line: {manifest.name}");continue
        expected, filename = entry
        filepath = ROOT / filename.strip().lstrip("*")
        check(filepath.is_file(), f"source missing {filename}")
        if filepath.is_file():
            got = hashlib.sha256(filepath.read_bytes()).hexdigest()
            check(got == expected, f"SOURCE_SHA256_MISMATCH {filename}")
    check((chapter / "scripts/run_sim.sh").is_file(),
          f"CH{n:02d} test script missing")

# 전체 UART→DSP/BRAM→NPU 경로의 필수 인스턴스 이름/모듈 선언 존재.
files = [
    "common/rtl/uart_rx.v", "common/rtl/uart_tx.v",
    "common/rtl/uart_core.v", "common/rtl/uart_echo_controller.v",
    "mini_npu/rtl/uart_npu_command_controller.v",
    "mini_npu/rtl/npu_dsp_mac_lane.v",
    "mini_npu/rtl/npu_engine4.v",
    "mini_npu/rtl/npu_reset_controller.v",
    "mini_npu/rtl/npu_display_controller.v",
    "mini_npu/rtl/basys3_npu_top.v",
    "mini_npu/tb/tb_npu_uart.sv",
    "mini_npu/tb/tb_npu_engine4.sv",
    "mini_npu/scripts/run_demo.sh",
    "mini_npu/scripts/run_engine.sh",
    "mini_npu/scripts/run_batch_00_12.sh",
]
for path in files:
    check((P3 / path).is_file(), "Missing integration file: " + path)
top = (P3 / "mini_npu/rtl/basys3_npu_top.v").read_text()
check("always" not in top and "assign" not in top and "function" not in top,
      "Top contains functional logic")
engine = (P3 / "mini_npu/rtl/npu_engine4.v").read_text()
lane = (P3 / "mini_npu/rtl/npu_dsp_mac_lane.v").read_text()
check("npu_dsp_mac_lane lane0" in engine and "npu_dsp_mac_lane lane3" in engine,
      "Four DSP accumulation lanes not instantiated")
check("dsp_multiplier" in lane, "Original DSP multiplier absent")

xdc = (P3 / "mini_npu/constraints/basys3_npu.xdc").read_text()
pins = re.findall(r"PACKAGE_PIN\s+([A-Z][0-9]+)", xdc)
check(len(pins) == len(set(pins)), "XDC duplicates physical pins")
for wire in ["clk", "btnC", "uart_rxd", "uart_txd"]:
    check(f"get_ports {wire}" in xdc, f"Missing XDC port {wire}")
check("create_clock" in xdc and "-period 10.000" in xdc,
      "100MHz clock constraint missing")

# 실행 대상 문자열과 실제 본문에 민감한 값을 직접 넣지 않는다.
for unsafe in ("AKIA", "ghp_", "BEGIN PRIVATE KEY", "sk-proj-"):
    check(unsafe not in engine and unsafe not in top,
          f"Possible secret detected: {unsafe}")

out = P3 / "validation/static_audit.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({
    "kind": "STATIC_AUDIT_ONLY",
    "checks": verified,
    "link_checks": link_checks,
    "errors": issues,
    "rtl_simulation": "NOT_EXECUTED_BY_THIS_SCRIPT",
    "synthesis": "NOT_RUN",
    "board": "NOT_RUN"
}, ensure_ascii=False, indent=2) + "\n")
if issues:
    for message in issues:
        print("STATIC_FAIL", message)
    raise SystemExit(1)
print(f"STATIC_AUDIT_PASS checks={verified} links={link_checks} chapters={len(chapters)} "
      "scope=files,hashes,links,hierarchy,XDC")
