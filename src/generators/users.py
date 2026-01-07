
import uuid
from faker import Faker
from datetime import datetime, timedelta
from src.utils.db import get_conn

fake = Faker()

def generate_users(org_id, total=500):
    conn = get_conn()
    cur = conn.cursor()
    users = []

    for i in range(total):
        ratio = i / total

        if ratio < 0.75:
            role = "IC"
        elif ratio < 0.90:
            role = "Manager"
        else:
            role = "Lead"

        active = i < int(0.92 * total)

        user_id = str(uuid.uuid4())
        name = fake.name()
        joined = datetime.now() - timedelta(days=fake.random_int(30, 1000))

        email = f"{name.replace(' ', '.').lower()}.{user_id[:8]}@nimbuslabs.com"

        cur.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                user_id,
                org_id,
                name,
                email,
                role,
                joined,
                active,
            ),
        )
        users.append(user_id)

    conn.commit()
    conn.close()
    return users
