"""
검색 기능을 담당하는 모듈입니다.

키워드 검색, 유사도 검색, 하이브리드 검색을 제공합니다.
"""

from typing import Dict, List

import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_resource
def load_embedding_model():
    """
    문장 임베딩 모델을 한 번만 로드합니다.
    """
    return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def keyword_search(query: str, archives: List[Dict]) -> List[Dict]:
    """
    검색어가 제목 또는 본문에 포함된 아카이브를 반환합니다.
    """
    normalized_query = query.strip().lower()

    if not normalized_query:
        return []

    results = []

    for archive in archives:
        title = archive["title"].lower()
        content = archive["content"].lower()

        if normalized_query in title or normalized_query in content:
            result = archive.copy()
            result["search_type"] = "키워드 검색"
            result["similarity"] = 1.0
            results.append(result)

    return results


def semantic_search(
    query: str,
    archives: List[Dict],
    threshold: float = 0.5,
) -> List[Dict]:
    """
    검색어와 저장된 텍스트 간 의미적 유사도를 계산하여 관련 결과를 반환합니다.
    """
    query = query.strip()

    if not query or not archives:
        return []

    model = load_embedding_model()

    archive_texts = [
        f"{archive['title']} {archive['content']}"
        for archive in archives
    ]

    query_embedding = model.encode([query])
    archive_embeddings = model.encode(archive_texts)

    scores = cosine_similarity(query_embedding, archive_embeddings)[0]

    results = []

    for archive, score in zip(archives, scores):
        if score >= threshold:
            result = archive.copy()
            result["similarity"] = float(score)
            result["search_type"] = "유사도 검색"
            results.append(result)

    results.sort(key=lambda item: item["similarity"], reverse=True)

    return results


def hybrid_search(
    query: str,
    archives: List[Dict],
    threshold: float = 0.5,
) -> List[Dict]:
    """
    키워드 검색 결과를 우선 반환하고,
    키워드 검색 결과가 없을 때 유사도 검색을 수행합니다.
    """
    keyword_results = keyword_search(query, archives)

    if keyword_results:
        return keyword_results

    return semantic_search(query, archives, threshold=threshold)