import autogen

import agents
from constants import COMMON_LLM_CONFIG
from utils import clean_text


class ProductOwner(agents.BaseAgent):
    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Product_Owner",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Product Owner.

                You manage a team including a Software Engineer and a User Experience Designer.

                You role is to plan, organize and tell your agents what to do.

                Rules:
                - Keep it short. Get to the point. Be straightforward. Specify your recipient's name.
                - Use a `BOARD.json` file to plan and keep track of ALL the steps you and your team makes.
                  ALWAYS check for its content when you start.
                """
            ),
        )
