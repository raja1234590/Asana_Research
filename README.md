# Asana RL Seed Data Simulation

This repository contains a realistic, research-grade seed dataset generator for simulating an **Asana-like enterprise workspace**, designed for reinforcement learning (RL) environments that model real-world project management workflows.

The dataset represents a **B2B SaaS organization** with teams, users, projects, tasks, comments, custom fields, and tags, following documented industry patterns and constraints.

---

##  Objective

The goal of this project is to generate **high-quality, realistic seed data** that avoids synthetic shortcuts and can be reliably used to evaluate and train AI agents performing computer-use tasks (e.g., navigating dashboards, assigning tasks, updating statuses).

Key principles:
- Realistic distributions (not uniform randomness)
- Strong temporal consistency
- Strict relational integrity
- Methodology-driven generation (schema + data logic aligned)

---

##  Database Schema

The schema is defined in `schema.sql` and includes the following core entities:

- Organizations / Workspaces  
- Teams  
- Users  
- Team Memberships  
- Projects  
- Sections  
- Tasks & Subtasks  
- Comments  
- Custom Field Definitions & Values  
- Tags & Task-Tag associations  

Foreign key constraints are enforced using SQLite.

---

##  Data Generation Methodology (Summary)

Each table is generated according to a documented strategy:

- **Organizations**  
  - UUIDv4 identifiers  
  - Company names inspired by public B2B SaaS sources (YC / Crunchbase-style)  
  - Created 2–5 years in the past  

- **Teams**  
  - Functional split: ~55% Engineering, 25% Marketing, 20% Ops  
  - Template-based names (e.g., Backend Platform, Growth Marketing)  

- **Users**  
  - Census-style names (via Faker)  
  - Role distribution: ~75% ICs, 15% Managers, 10% Leads  
  - ~92% active users to simulate churn  

- **Projects**  
  - Types: Sprint, Campaign, Ongoing  
  - Names derived from Asana templates and GitHub project boards  

- **Tasks**  
  - Task names follow domain-specific patterns  
  - 15% unassigned tasks  
  - Completion rates vary by project type  
  - Due dates follow realistic planning horizons  
  - Creation times biased toward Mon–Wed  

- **Comments, Tags, Custom Fields**  
  - Added only where logically consistent  
  - Scoped correctly to tasks and projects  

All temporal fields are guaranteed to be logically valid (e.g., tasks are never completed before creation).



