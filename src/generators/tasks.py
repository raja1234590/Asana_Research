# src/generators/tasks.py
import uuid
from datetime import timedelta
from src.utils.db import get_conn
from src.utils.dates import weekday_biased_timestamp

TASK_NAMES = {
    "Engineering": "Auth – Fix – Token refresh bug",
    "Marketing": "Product Launch – Email Sequence",
    "Ops": "Customer Support – Process Review",
}

COMPLETION_RATE = {
    "Sprint": 0.80,
    "Campaign": 0.60,
    "Ongoing": 0.45,
}

def generate_tasks(projects, project_sections, users, team_function_map):
    conn = get_conn()
    cur = conn.cursor()
    tasks = []

    for project in projects:
        team_function = team_function_map[project["team_id"]]
        completed_count = int(50 * COMPLETION_RATE[project["project_type"]])

        for i in range(50):
            created = weekday_biased_timestamp(30 + i)
            completed = i < completed_count
            completed_at = created + timedelta(days=7) if completed else None

            assignee = users[i % len(users)] if i % 100 >= 15 else None  # 15% unassigned

            task_id = str(uuid.uuid4())

            cur.execute(
                "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    task_id,
                    project["project_id"],
                    project_sections[project["project_id"]][2 if completed else 0],
                    None,
                    TASK_NAMES[team_function],
                    "",
                    assignee,
                    created.date(),
                    completed,
                    created,
                    completed_at,
                ),
            )

            tasks.append(task_id)

    conn.commit()
    conn.close()
    return tasks
