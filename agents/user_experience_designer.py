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

                You are part of a team including a CEO and a Software Engineer.

                Your role is to design the program UI and UX.

                The CEO is your manager. You are the first to answer him.

                Rules:
                - Keep it short. Get to the point. Be straightforward. Specify your recipient's name.
                - Use `search_web()` and `fetch_web_page()` functions for UI & UX research.
                - Use a `DESIGN.md` file to keep a memo of your analyses. ALWAYS check for its content when you start.
                """
            ),
        )
