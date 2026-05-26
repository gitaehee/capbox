import streamlit as st
from PIL import Image

from db import init_db, save_archive, get_all_archives
from ocr_utils import extract_text_from_image
from search_utils import keyword_search, semantic_search


st.set_page_config(
    page_title="CapBox",
    page_icon="📦",
    layout="wide",
)


def main():
    init_db()

    st.title("📦 CapBox")
    st.subheader("스크린샷 텍스트 아카이빙 서비스")

    st.markdown(
        """
        CapBox는 스크린샷 이미지에서 텍스트를 추출하고,
        나중에 검색어로 저장된 내용을 다시 찾을 수 있도록 돕는 웹앱입니다.
        """
    )

    st.divider()

    if "ocr_text" not in st.session_state:
        st.session_state.ocr_text = ""

    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.header("1. 스크린샷 업로드")

        uploaded_file = st.file_uploader(
            "스크린샷 이미지를 업로드하세요.",
            type=["png", "jpg", "jpeg"],
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, caption="업로드한 이미지", use_container_width=True)

            if st.button("OCR 실행"):
                with st.spinner("이미지에서 텍스트를 추출하는 중입니다..."):
                    extracted_text = extract_text_from_image(image)

                if extracted_text:
                    st.session_state.ocr_text = extracted_text
                    st.success("텍스트 추출이 완료되었습니다.")
                else:
                    st.session_state.ocr_text = ""
                    st.warning(
                        "이미지에서 텍스트를 추출하지 못했습니다. "
                        "직접 입력하거나 다른 이미지를 사용해주세요."
                    )
        else:
            st.info("아직 업로드된 이미지가 없습니다.")

    with right_col:
        st.header("2. OCR 결과 확인")

        edited_text = st.text_area(
            "추출된 텍스트를 확인하고 필요하면 수정하세요.",
            value=st.session_state.ocr_text,
            height=300,
            placeholder="OCR 실행 후 이미지 속 텍스트가 여기에 표시됩니다.",
        )

        title = st.text_input(
            "저장 제목",
            placeholder="예: 과제 안내 스크린샷",
        )

        if st.button("저장하기"):
            try:
                save_archive(title, edited_text)
                st.success("아카이브가 저장되었습니다.")
                st.session_state.ocr_text = ""
                st.rerun()
            except ValueError as error:
                st.warning(str(error))

    st.divider()

    st.header("3. 저장된 아카이브 목록")

    archives = get_all_archives()

    if not archives:
        st.info("아직 저장된 항목이 없습니다.")
    else:
        for archive in archives:
            with st.expander(f"{archive['title']}  |  {archive['created_at']}"):
                st.write(archive["content"])

    st.divider()

    st.header("4. 검색")

    search_type = st.radio(
        "검색 방식",
        ["키워드 검색", "유사도 검색"],
        horizontal=True,
    )

    search_query = st.text_input(
        "검색어를 입력하세요.",
        placeholder="예: 바이브코딩 과제 조건",
    )

    if st.button("검색하기"):
        if not search_query.strip():
            st.warning("검색어를 입력해주세요.")
        else:
            archives = get_all_archives()

            if search_type == "키워드 검색":
                search_results = keyword_search(search_query, archives)
            else:
                with st.spinner("유사도 검색을 수행하는 중입니다..."):
                    search_results = semantic_search(search_query, archives)

            if not search_results:
                st.info("관련 결과가 없습니다.")
            else:
                st.success(f"{len(search_results)}개의 결과를 찾았습니다.")

                for result in search_results:
                    if "similarity" in result:
                        title = (
                            f"{result['title']}  |  "
                            f"유사도: {result['similarity']:.3f}  |  "
                            f"{result['created_at']}"
                        )
                    else:
                        title = f"{result['title']}  |  {result['created_at']}"

                    with st.expander(title):
                        st.write(result["content"])


if __name__ == "__main__":
    main()