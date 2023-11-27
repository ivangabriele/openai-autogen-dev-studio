"""
Module Name: main.py

Short Description:
OADS intends to leverage Microsoft Autogen to automate software development via AI agents.

Detailed Description:
TODO Write a detailed description of the program.
"""

import asyncio

import agents
from constants import (
    PROJECT_CONFIG,
)
from core import Core
import utils


ceo = agents.CEO()
planner = agents.Planner()

product_owner = agents.ProductOwner(ceo=ceo, planner=planner)
software_engineer = agents.SoftwareEngineer(ceo=ceo, planner=planner)
user_experience_designer = agents.UserExperienceDesigner(ceo=ceo, planner=planner)

utils.print_project_config(PROJECT_CONFIG)

core = Core(
    product_owner=product_owner,
    team_agents=[
        user_experience_designer,
        software_engineer,
    ],
)

if __name__ == "__main__":
    asyncio.run(
        core.start(
            initial_message="Develop the API of a multipayer variation of the SimCity 2000 game. In Node.js, using Typescript.",
        )
    )
