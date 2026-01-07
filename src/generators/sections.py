import uuid
from src.utils.db import get_conn

SECTION_TEMPLATES = ["To Do", "In Progress", "Done", "Backlog"]

def generate_sections(projects):
    conn = get_conn()
    cur = conn.cursor()

    project_sections = {}

    for project in projects:
        project_sections[project["project_id"]] = []

        for pos, name in enumerate(SECTION_TEMPLATES):
            section_id = str(uuid.uuid4())

            cur.execute(
                "INSERT INTO sections VALUES (?, ?, ?, ?)",
                (
                    section_id,
                    project["project_id"],
                    name,
                    pos,
                ),
            )
            project_sections[project["project_id"]].append(section_id)

    conn.commit()
    conn.close()
    return project_sections
