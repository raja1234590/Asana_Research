# src/generators/custom_fields.py
import uuid
from src.utils.db import get_conn
from src.utils.dates import weekday_biased_timestamp

def generate_custom_fields(projects):
    conn = get_conn()
    cur = conn.cursor()
    fields = []

    for project in projects:
        for name, field_type in [
            ("Priority", "enum"),
            ("Risk Level", "enum"),
            ("Effort", "number"),
        ]:
            field_id = str(uuid.uuid4())

            cur.execute(
                "INSERT INTO custom_field_definitions VALUES (?, ?, ?, ?, ?)",
                (
                    field_id,
                    project["project_id"],
                    name,
                    field_type,
                    weekday_biased_timestamp(200),
                ),
            )

            fields.append({
                "field_id": field_id,
                "field_type": field_type,
                "name": name,
            })

    conn.commit()
    conn.close()
    return fields
