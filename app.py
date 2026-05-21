import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="CapBox",
    page_icon="📦",
    layout="wide",
)


def main():
    st.title("📦 CapBox")
    st.subheader("스크린샷 텍스트 아카이빙 서비스")

    st.markdown(
        """
        CapBox는 스크린샷 이미지에서 텍스트를 추출하고,
        나중에 검색어로 저장된 내용을 다시 찾을 수 있도록 돕는 웹앱입니다.

        현재 단계에서는 전체 기능 구현 전,
        화면 구조와 이미지 업로드 흐름을 먼저 구성합니다.
        """
    )

    st.divider()

    left_col, right_col = st.columns([1, 1])

    with left_col:
        st.header("1. 스크린샷 업로드")

        uploaded_file = st.file_uploader(
            "스크린샷 이미지를 업로드하세요.",
            type=["png", "jpg", "jpeg"],
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="업로드한 이미지", use_container_width=True)
        else:
            st.info("아직 업로드된 이미지가 없습니다.")

    with right_col:
        st.header("2. OCR 결과 확인")

        st.text_area(
            "추출된 텍스트가 이곳에 표시될 예정입니다.",
            value="",
            height=250,
            placeholder="OCR 기능 구현 후 이미지 속 텍스트가 여기에 표시됩니다.",
        )

        st.text_input(
            "저장 제목",
            placeholder="예: 과제 안내 스크린샷",
        )

        st.button("저장하기", disabled=True)

    st.divider()

    st.header("3. 저장된 아카이브 목록")
    st.info("DB 저장 기능 구현 후 저장된 텍스트 목록이 표시됩니다.")

    st.divider()

    st.header("4. 검색")
    st.text_input(
        "검색어를 입력하세요.",
        placeholder="예: 바이브코딩 과제 조건",
    )
    st.button("검색하기", disabled=True)
    st.info("검색 기능 구현 후 유사한 아카이브 결과가 표시됩니다.")


if __name__ == "__main__":
    main()