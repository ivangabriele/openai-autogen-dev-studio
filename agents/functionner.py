import autogen

import agents
from constants import FUNCTIONEER_LLM_CONFIG
from utils import clean_text


class Functioneer(agents.BaseAgent):
    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Functioneer",
            llm_config=FUNCTIONEER_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Functioneer.

                Your role is to reply to agents' requests with the result of the command they asked you to run.
                """
            ),
        )
