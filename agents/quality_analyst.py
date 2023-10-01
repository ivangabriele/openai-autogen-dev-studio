import autogen

import agents
from constants import COMMON_LLM_CONFIG
from utils import clean_text


class QualityAnalyst(agents.BaseAgent):
    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Quality_Analyst",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Quality Analyst.
                Your role is to run tests to ensure that the program works as expected.

                You are part of a team of agents consisting of:
                - a Product Owner: plan and manage the team, inluding yourself,
                - a Software Engineer: write code and unit/e2e tests,
                - a User Experience Designer: online research, program design.

                Go to the point. Forget social conventions. Prefix your messages with you recipient's name.
                """
            ),
        )
