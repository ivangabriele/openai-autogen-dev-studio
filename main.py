"""
Module Name: main.py

Short Description:
This program intends to leverage Microsoft Autogen to automate software development via AI agents.

Detailed Description:
Microsoft Autogen is a framework that enables the development of LLM (Lifelong Learning Machines) applications
using multiple agents capable of conversing with each other to solve tasks.
Autogen agents are customizable, conversable, and can seamlessly incorporate human participation.
These agents can operate in various modes, utilizing combinations of LLMs, human input, and other tools.
"""

import asyncio
import autogen

import agents
from constants import (
    CEO_LLM_CONFIG,
    PROJECT_CONFIG,
)
import utils


# CEO Human Proxy Agent
# Uses shell with human-in-the-loop, meaning the human user can either give their input when asked,
# or ignore step, to let the agent interactions continue from there.
ceo_user_proxy_agent = autogen.UserProxyAgent(
    "CEO",
    # code_execution_config={"work_dir": PROJECT_DIRECTORY_NAME},
    code_execution_config=False,
    human_input_mode="TERMINATE",
    llm_config=CEO_LLM_CONFIG,
    # is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    # max_consecutive_auto_reply=10,
    system_message=utils.clean_text(
        """
        You are the CEO.

        You are assisted by a Product Owner who will try his best to achieve your goals with the team under his orders.
        Your are the only agent allowed to run functions.

        Rules:
        - Keep it short. Get to the point. Be straightforward. Always specify your recipient's name.
        - Only reply to messages prefixed with your name, i.e.: "CEO, etc".
        - Only communicate with the Product Owner, and nobody else.

        Reply TERMINATE when the task has been solved to full satisfaction.
        Otherwise, reply CONTINUE.
        """
    ),
)


assistant = agents.Assistant()
functioneer = agents.Functioneer()
software_engineer = agents.SoftwareEngineer()


utils.print_project_config(PROJECT_CONFIG)


if __name__ == "__main__":
    asyncio.run(
        assistant.start(
            ceo_user_proxy_agent=ceo_user_proxy_agent,
            initial_prompt="What are the best Ubuntu features?",
        )
    )
