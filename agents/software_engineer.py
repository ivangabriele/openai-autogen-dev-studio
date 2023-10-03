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

                You are part of a team inluding a CEO and a User Experience Designer.

                Your role is to write the expected program source code.

                The CEO is your manager.

                Rules:
                - Keep it short. Get to the point. Be straightforward. Specify your recipient's name.
                - Use `search_web()` and `fetch_web_page()` functions for programming documentation research.
                - ALWAYS write unit/e2e tests to check that your code works.
                - NEVER run the program directly, run it via e2e tests.
                - Use a `TECH.json` file to keep track of your work. ALWAYS check for its content when you start.
               """
            ),
        )
