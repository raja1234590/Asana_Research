import uuid
from src.utils.db import get_conn
from src.utils.dates import weekday_biased_timestamp

COMMENT_TEMPLATES = [
    "Please clarify acceptance criteria.",
    "Blocked due to dependency.",
    "Implemented, ready for review.",
]

def generate_comments(tasks, users):
    conn = get_conn()
    cur = conn.cursor()

    for idx, task_id in enumerate(tasks):
        if idx % 2 == 0:  # ~50% tasks have comments
            cur.execute(
                "INSERT INTO comments VALUES (?, ?, ?, ?, ?)",
                (
                    str(uuid.uuid4()),
                    task_id,
                    users[idx % len(users)],
                    COMMENT_TEMPLATES[idx % len(COMMENT_TEMPLATES)],
                    weekday_biased_timestamp(10),
                ),
            )

    conn.commit()
    conn.close()
