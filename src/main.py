from src.utils.db import init_db
from src.generators.organizations import generate_organizations
from src.generators.teams import generate_teams
from src.generators.users import generate_users
from src.generators.team_memberships import generate_team_memberships
from src.generators.projects import generate_projects
from src.generators.sections import generate_sections
from src.generators.tasks import generate_tasks
from src.generators.comments import generate_comments
from src.generators.custom_fields import generate_custom_fields
from src.generators.tags import generate_tags, generate_task_tags


def main():
    
    init_db()

    
    org = generate_organizations()

    
    teams = generate_teams(org["organization_id"])

    
    team_function_map = {
        team["team_id"]: team["function"]
        for team in teams
    }

   
    users = generate_users(org["organization_id"])

    
    generate_team_memberships(teams, users)

   
    projects = generate_projects(teams)

   
    sections = generate_sections(projects)

    
    tasks = generate_tasks(projects, sections, users, team_function_map)

   
    generate_comments(tasks, users)

    
    generate_custom_fields(projects)

   
    tag_ids = generate_tags()
    generate_task_tags(tasks, tag_ids)

    print("Asana seed database generated successfully")


if __name__ == "__main__":
    main()
