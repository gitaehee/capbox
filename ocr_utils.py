import easyocr
import numpy as np
import streamlit as st
from PIL import Image


@st.cache_resource
def load_reader():
    """
    EasyOCR Reader를 한 번만 로드하기 위한 함수입니다.
    모델 로딩 시간이 오래 걸릴 수 있으므로 Streamlit cache를 사용합니다.
    """
    return easyocr.Reader(["ko", "en"], gpu=False)


def extract_text_from_image(image: Image.Image) -> str:
    """
    업로드된 이미지에서 텍스트를 추출합니다.

    Args:
        image: PIL Image 객체

    Returns:
        추출된 텍스트 문자열
    """
    if image is None:
        return ""

    reader = load_reader()

    image_array = np.array(image)

    results = reader.readtext(image_array, detail=0)

    extracted_text = "\n".join(results).strip()

    return extracted_text