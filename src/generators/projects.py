# src/generators/projects.py
import uuid
from datetime import datetime, timedelta
from src.utils.db import get_conn

PROJECT_NAMES = [
    "Q2 Platform Stability",
    "Website Redesign",
    "Growth Experimentation",
    "Customer Retention Initiative",
]

PROJECT_TYPES = ["Sprint", "Campaign", "Ongoing"]

def generate_projects(teams, projects_per_team=3):
    """
    Generates projects for each team.
    Returns a list of dicts with project_id, project_type, team_id.
    """
    conn = get_conn()
    cur = conn.cursor()
    projects = []

    for team in teams:
        for i in range(projects_per_team):
            project_id = str(uuid.uuid4())
            project_type = PROJECT_TYPES[i % len(PROJECT_TYPES)]
            created_at = datetime.now() - timedelta(days=90)

            cur.execute(
                "INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    project_id,
                    team["team_id"],
                    PROJECT_NAMES[i % len(PROJECT_NAMES)],
                    project_type,
                    None,
                    None,
                    created_at,
                ),
            )

            projects.append({
                "project_id": project_id,
                "project_type": project_type,
                "team_id": team["team_id"],
            })

    conn.commit()
    conn.close()
    return projects
