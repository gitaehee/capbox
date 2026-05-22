import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path("capbox.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    """
    archive 테이블을 생성합니다.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS archive (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def save_archive(title: str, content: str):
    """
    OCR 결과 텍스트를 DB에 저장합니다.
    """
    title = title.strip()
    content = content.strip()

    if not content:
        raise ValueError("저장할 텍스트가 비어 있습니다.")

    if not title:
        title = content[:20] + "..." if len(content) > 20 else content

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO archive (title, content, created_at)
            VALUES (?, ?, ?)
            """,
            (title, content, created_at),
        )
        conn.commit()


def get_all_archives():
    """
    저장된 아카이브 목록을 최신순으로 조회합니다.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT id, title, content, created_at
            FROM archive
            ORDER BY id DESC
            """
        )
        rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "created_at": row[3],
        }
        for row in rows
    ]