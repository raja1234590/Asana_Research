
import uuid
from src.utils.db import get_conn

TAG_NAMES = [
    "urgent",
    "blocked",
    "backend",
    "frontend",
    "high-priority",
    "low-priority",
]

def generate_tags():
    conn = get_conn()
    cur = conn.cursor()
    tag_ids = {}

    for tag in TAG_NAMES:
        
        cur.execute(
            "SELECT tag_id FROM tags WHERE name = ?",
            (tag,),
        )
        row = cur.fetchone()

        if row:
            tag_ids[tag] = row[0]
            continue

        tag_id = str(uuid.uuid4())
        cur.execute(
            "INSERT INTO tags VALUES (?, ?)",
            (tag_id, tag),
        )
        tag_ids[tag] = tag_id

    conn.commit()
    conn.close()
    return tag_ids


def generate_task_tags(tasks, tag_ids):
    conn = get_conn()
    cur = conn.cursor()

    for idx, task_id in enumerate(tasks):
        
        tags = list(tag_ids.values())[idx % len(tag_ids):][:2]

        for tag_id in tags:
            cur.execute(
                "INSERT OR IGNORE INTO task_tags VALUES (?, ?)",
                (task_id, tag_id),
            )

    conn.commit()
    conn.close()
