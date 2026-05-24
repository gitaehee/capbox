"""
검색 기능을 담당하는 모듈입니다.

현재 단계에서는 키워드 기반 검색을 제공합니다.
이후 단계에서 유사도 기반 검색으로 확장할 예정입니다.
"""


def keyword_search(query: str, archives: list[dict]) -> list[dict]:
    """
    검색어가 제목 또는 본문에 포함된 아카이브를 반환합니다.

    Args:
        query: 사용자가 입력한 검색어
        archives: 저장된 아카이브 목록

    Returns:
        검색어가 포함된 아카이브 목록
    """
    normalized_query = query.strip().lower()

    if not normalized_query:
        return []

    results = []

    for archive in archives:
        title = archive["title"].lower()
        content = archive["content"].lower()

        if normalized_query in title or normalized_query in content:
            results.append(archive)

    return results