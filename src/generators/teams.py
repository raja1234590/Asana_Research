# generators/teams.py
import uuid
from datetime import datetime
from src.utils.db import get_conn

TEAM_DISTRIBUTION = {
    "Engineering": 0.55,
    "Marketing": 0.25,
    "Ops": 0.20,
}

TEAM_NAMES = {
    "Engineering": ["Backend Platform", "Frontend Experience", "Infra"],
    "Marketing": ["Growth Marketing", "Brand Strategy"],
    "Ops": ["Customer Operations"],
}

def generate_teams(org_id, total=20):
    conn = get_conn()
    cur = conn.cursor()
    teams = []

    for function, ratio in TEAM_DISTRIBUTION.items():
        count = int(total * ratio)
        for i in range(count):
            team_id = str(uuid.uuid4())
            name = TEAM_NAMES[function][i % len(TEAM_NAMES[function])]

            cur.execute(
                "INSERT INTO teams VALUES (?, ?, ?, ?, ?)",
                (team_id, org_id, name, function, datetime.now()),
            )
            teams.append({"team_id": team_id, "function": function})

    conn.commit()
    conn.close()
    return teams
