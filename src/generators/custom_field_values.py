import uuid
import random
from src.utils.db import get_conn

ENUM_VALUES = {
    "Priority": ["Low", "Medium", "High", "Urgent"],
    "Risk Level": ["Low", "Medium", "High"],
}

def generate_custom_field_values(tasks, fields):
    conn = get_conn()
    cur = conn.cursor()

    for task_id in tasks:
        for field in fields:
           
            if random.random() < 0.7:
                value_id = str(uuid.uuid4())

                if field["field_type"] == "enum":
                    cur.execute(
                        "INSERT INTO custom_field_values VALUES (?, ?, ?, ?, ?)",
                        (
                            value_id,
                            field["field_id"],
                            task_id,
                            random.choice(ENUM_VALUES[field["name"]]),
                            None,
                        ),
                    )

                elif field["field_type"] == "number":
                    cur.execute(
                        "INSERT INTO custom_field_values VALUES (?, ?, ?, ?, ?)",
                        (
                            value_id,
                            field["field_id"],
                            task_id,
                            None,
                            random.randint(1, 13),
                        ),
                    )

    conn.commit()
    conn.close()
