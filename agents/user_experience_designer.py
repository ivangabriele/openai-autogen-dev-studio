import autogen

import agents
from constants import COMMON_LLM_CONFIG
from utils import clean_text


class UserExperienceDesigner(agents.BaseAgent):
    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "User_Experience_Designer",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the User Experience Designer.
                Your role is to ensure the best user experience possible for the program being developed.

                You are part of a team of agents consisting of:
                - a Product Owner: plan and manage the team, inluding yourself,
                - a Quality Analyst: check and run unit/e2e tests,
                - a Software Engineer: write code and unit/e2e tests.

                Go to the point. Forget social conventions. Prefix your messages with you recipient's name.
                Integrate some online research and browsing in your thinking process.
                """
            ),
        )
