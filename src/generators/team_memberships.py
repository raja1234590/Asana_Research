from datetime import timedelta
from src.utils.db import get_conn
from src.utils.dates import weekday_biased_timestamp


def generate_team_memberships(teams, users):
    conn = get_conn()
    cur = conn.cursor()

    for idx, user_id in enumerate(users):
        
        assigned = teams[idx % len(teams): (idx % len(teams)) + 2]

        for team in assigned:
            joined_at = weekday_biased_timestamp(120)

            cur.execute(
                "INSERT INTO team_memberships VALUES (?, ?, ?, ?)",
                (
                    team["team_id"],
                    user_id,
                    joined_at,
                    "Lead" if idx % 10 == 0 else "Member",  
                ),
            )

    conn.commit()
    conn.close()
