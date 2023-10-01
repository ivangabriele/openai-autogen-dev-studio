import autogen

import agents
from constants import COMMON_LLM_CONFIG
from utils import clean_text


class SoftwareEngineer(agents.BaseAgent):
    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Sofware_Engineer",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                Your are the Sofware Engineer.
                Your role is to write the expected program source code, run it and fix it when necessary.

                You are part of a team of agents consisting of:
                - a Product Owner: plan and manage the team, inluding yourself,
                - a Quality Analyst: check and run unit/e2e tests,
                - a User Experience Designer: online research, program design.

                Go to the point. Forget social conventions. Prefix your messages with you recipient's name.
                Integrate some online research and browsing when stuck.

                Never run the program itself, unless it's indirectly via e2e tests.
                Only use unit & e2e tests to check that your code works.
                """
            ),
        )
