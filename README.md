# CapBox

소프트웨어공학 과제용 프로젝트입니다.

---

## 개발 기간

2026.05.17 ~ 2026.06.07

---

## 기술 스택

- Python
- Streamlit
- Pillow
- SQLite
- OCR 라이브러리
- 유사도 검색 라이브러리

---

## 실행 방법

### 1. 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. Streamlit 앱 실행

```bash
streamlit run app.py
```

실행 후 브라우저에서 CapBox 웹앱 화면을 확인할 수 있습니다.

---

## 현재 구현 상태

2026-05-21 기준 구현 상태는 다음과 같습니다.

- Streamlit 기본 화면 구성
- 서비스 제목 및 설명 표시
- 이미지 업로드 UI 구현
- 업로드 이미지 미리보기 구현
- OCR 결과 확인 영역 배치
- 저장 목록 영역 배치
- 검색 영역 배치

아직 OCR, SQLite 저장, 유사도 검색 기능은 실제 로직과 연결되지 않았으며, 이후 단계에서 순차적으로 구현할 예정입니다.

---

## 프로젝트 구조

```text
capbox/
├── README.md
├── requirements.txt
├── app.py
├── db.py
├── ocr_utils.py
├── search_utils.py
│
├── docs/
│   ├── 01_requirements.md
│   ├── 02_design.md
│   ├── 03_implementation.md
│   ├── 04_test_plan.md
│   ├── 05_quality_management.md
│   ├── 06_lessons_learned.md
│   └── discussion/
│       ├── 2026-05-17_topic_selection.md
│       ├── 2026-05-19_scope_and_requirements.md
│       ├── 2026-05-20_design_discussion.md
│       └── 2026-05-21_app_structure.md
│
├── screenshots/
│
└── report/
    └── final_report.pdf
```

---

## 프로세스 적용 방식

본 프로젝트는 다음 순서에 따라 진행합니다.

1. 요구사항 분석
2. 시스템 설계
3. 기본 화면 구현
4. OCR 기능 구현
5. 데이터 저장 기능 구현
6. 검색 기능 구현
7. 테스트
8. 품질 관리
9. 회고 및 교훈 정리
10. 최종 보고서 작성

각 단계의 결과물은 `docs/` 폴더에 문서로 정리하고, 주요 논의 내용은 `docs/discussion/` 폴더에 날짜별로 기록합니다.