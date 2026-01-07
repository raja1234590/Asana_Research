
import uuid
import random
from datetime import datetime, timedelta
from src.utils.db import get_conn


ORGANIZATION_CATALOG = [
    ("Nimbus Labs", "nimbuslabs.com"),
    ("Atlas Systems", "atlassystems.io"),
    ("Helix Software", "helixsoft.ai"),
    ("Vertex Cloud", "vertexcloud.com"),
    ("Pulse Analytics", "pulseanalytics.io"),
    ("Orbit Platforms", "orbitplatforms.com"),
]

def generate_organizations():
    conn = get_conn()
    cur = conn.cursor()

    org_name, org_domain = random.choice(ORGANIZATION_CATALOG)

    
    cur.execute(
        "SELECT organization_id FROM organizations WHERE domain = ?",
        (org_domain,),
    )
    row = cur.fetchone()

    if row:
        conn.close()
        return {"organization_id": row[0]}

    org_id = str(uuid.uuid4())

   
    created_at = datetime.now() - timedelta(
        days=random.randint(365 * 2, 365 * 5)
    )

    cur.execute(
        "INSERT INTO organizations VALUES (?, ?, ?, ?)",
        (org_id, org_name, org_domain, created_at),
    )

    conn.commit()
    conn.close()

    return {"organization_id": org_id}
