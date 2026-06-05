# CapBox

CapBox는 스크린샷 이미지에서 텍스트를 추출하고, 추출된 텍스트를 저장한 뒤 나중에 검색어로 다시 찾을 수 있도록 돕는 웹 기반 아카이빙 서비스입니다.

본 프로젝트는 소프트웨어공학 과제인 **“프로세스에 입각한 바이브코딩의 효과 분석”**을 위해 진행되었습니다.  
AI로 바이브코딩하며, 요구사항 분석, 설계, 구현, 테스트, 품질 관리, 회고 과정을 문서와 커밋 기록으로 남기는 것을 목표로 하였습니다.

---

## 1. 프로젝트 개요

일상적으로 사용자는 쇼핑 정보, 과제 안내, 일정, 게시글, 메모 등을 스크린샷으로 저장합니다.  
하지만 시간이 지나면 어떤 스크린샷에 어떤 정보가 있었는지 다시 찾기 어렵습니다.

CapBox는 이러한 문제를 해결하기 위해 스크린샷 속 텍스트를 OCR로 추출하고, 저장된 텍스트를 나중에 키워드 검색과 유사도 검색으로 다시 찾을 수 있도록 합니다.

---

## 2. 주요 기능

- 스크린샷 이미지 업로드
- 파일 선택 및 드래그 앤 드롭 방식의 이미지 업로드
- 이미지 미리보기
- OCR을 통한 텍스트 추출
- OCR 결과 확인 및 수정
- SQLite 기반 텍스트 저장
- 저장된 아카이브 목록 조회
- 키워드 검색
- 유사도 검색
- 하이브리드 검색
- 빈 입력 및 검색 결과 없음 예외 처리

---

## 3. 기술 스택

| 구분 | 사용 기술 |
|---|---|
| 언어 | Python |
| 웹 프레임워크 | Streamlit |
| OCR | EasyOCR |
| 데이터베이스 | SQLite |
| 이미지 처리 | Pillow |
| 유사도 검색 | sentence-transformers, scikit-learn |
| 버전 관리 | Git, GitHub |

---

## 4. 실행 방법

### 4.1 패키지 설치

```bash
pip install -r requirements.txt
```

### 4.2 Streamlit 앱 실행

```bash
streamlit run app.py
```

실행 후 브라우저에서 CapBox 화면이 열립니다.

---

## 5. 사용 방법

1. 스크린샷 이미지를 업로드합니다.
2. 업로드된 이미지를 확인합니다.
3. OCR 실행 버튼을 눌러 이미지 속 텍스트를 추출합니다.
4. 추출된 텍스트를 확인하고 필요한 경우 수정합니다.
5. 제목과 함께 텍스트를 저장합니다.
6. 저장된 아카이브 목록에서 내용을 확인합니다.
7. 키워드 검색, 유사도 검색, 하이브리드 검색으로 저장된 내용을 다시 찾습니다.

---

## 6. 프로젝트 구조

```text
capbox/
├── README.md
├── requirements.txt
├── app.py
├── db.py
├── ocr_utils.py
├── search_utils.py
├── capbox.db
├── docs/
│   ├── 01_requirements.md
│   ├── 02_design.md
│   ├── 03_implementation.md
│   ├── 04_test_plan.md
│   ├── test_result.md
│   ├── 05_quality_management.md
│   ├── 06_lessons_learned.md
│   └── discussion/
├── screenshots/
└── report/
    └── report_draft.md
```

---

## 7. 주요 파일 설명

| 파일 | 역할 |
|---|---|
| `app.py` | Streamlit 화면 및 전체 사용자 흐름 제어 |
| `ocr_utils.py` | OCR 텍스트 추출 기능 |
| `db.py` | SQLite 저장 및 조회 기능 |
| `search_utils.py` | 키워드 검색, 유사도 검색, 하이브리드 검색 기능 |
| `requirements.txt` | 실행에 필요한 패키지 목록 |
| `docs/` | 요구사항, 설계, 테스트, 품질관리, 회고 문서 |
| `screenshots/` | 실행 화면 캡처 |
| `report/` | 최종 보고서 초안 및 결과물 |

---

## 8. 개발 프로세스 문서

본 프로젝트는 다음과 같은 소프트웨어공학 프로세스에 따라 진행되었습니다.

| 단계 | 문서 |
|---|---|
| 요구사항 분석 | `docs/01_requirements.md` |
| 설계 | `docs/02_design.md` |
| 구현 기록 | `docs/03_implementation.md` |
| 테스트 계획 | `docs/04_test_plan.md` |
| 테스트 결과 | `docs/test_result.md` |
| 품질 관리 | `docs/05_quality_management.md` |
| 회고 | `docs/06_lessons_learned.md` |

또한 `docs/discussion/` 폴더에는 날짜별 토의 기록을 정리하였습니다.

---

## 9. 실행 화면 캡처

`screenshots/` 폴더에는 기능 구현 단계별 실행 화면을 저장하였습니다.

| 파일 | 내용 |
|---|---|
| `2026-05-21_basic_layout.png` | 기본 화면 구성 |
| `2026-05-22_ocr_result.png` | OCR 텍스트 추출 결과 |
| `2026-05-23_save_success.png` | 저장 성공 화면 |
| `2026-05-24_keyword_search_empty.png` | 검색 결과 없음 화면 |
| `2026-05-26_keyword_search_success.png` | 키워드 검색 성공 화면 |
| `2026-05-26_similarity_search_result.png` | 유사도 검색 결과 화면 |
| `2026-05-28_hybrid_search_result.png` | 하이브리드 검색 결과 화면 |

---

## 10. 바이브코딩 활용 방식

본 프로젝트에서는 바이브코딩을 다음과 같은 방식으로 활용하였습니다.

- 프로젝트 아이디어 구체화
- MVP 범위 조정
- 요구사항 문서 작성 보조
- Streamlit UI 코드 초안 작성
- OCR, DB, 검색 기능 구현 보조
- 테스트 케이스 작성 보조
- 품질관리 문서 작성 보조
- 최종 보고서 구성 보조

바이브코딩은 구현 속도를 높이는 데 효과적이었지만, OCR 오인식이나 유사도 검색 품질 문제처럼 실제 데이터 기반 검증이 필요한 부분도 있었습니다.  
따라서 본 프로젝트에서는 AI가 생성한 결과를 그대로 사용하는 것이 아니라, 테스트와 품질관리 과정을 통해 검토하고 개선하였습니다.

---

## 11. 프로젝트 기간

```text
2026.05.17 ~ 2026.06.05
```

---

## 12. GitHub Repository

```text
https://github.com/gitaehee/capbox
```