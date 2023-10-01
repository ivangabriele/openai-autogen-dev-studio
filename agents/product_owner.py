import select
from typing import TYPE_CHECKING
from autogen import AssistantAgent
from agents.base_agent import BaseAgent
from constants import COMMON_LLM_CONFIG

from utils import clean_text


if TYPE_CHECKING:
    from autogen import UserProxyAgent
    from agents.software_engineer import SoftwareEngineer


class ProductOwner(BaseAgent):
    ceo_user_proxy_agent: "UserProxyAgent"
    software_engineer: "SoftwareEngineer"

    def __init__(self) -> None:
        self.is_product_owner = True

        self.as_assistant_agent = AssistantAgent(
            "Product_Owner",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Product Owner.

                You manage a team of agents consisting of:
                - a Quality Analyst: check and run unit/e2e tests,
                - a Software Engineer: write code and unit/e2e tests,
                - a User Experience Designer: online research, program design.

                You are the sole responsible of the CEO's satisfaction,
                You plan and tell who does what and when.

                You exploit your agents' expertise to the fullest, asking regularly for their input.

                Go to the point. Forget social conventions. Prefix your messages with you recipient's name.

                However, before starting anything else, ask your Software Engineer to give you a brief
                about the current environment and existing source code. It should start by running `ls -la`.

                The CEO can help when your team is stuck.
                """
            ),
        )

    def attach_agents(
        self,
        software_engineer: "SoftwareEngineer",
    ):
        self.software_engineer = software_engineer

    def ask_software_engineer(self, message: str):
        return self.software_engineer.ask(
            sender=self.as_assistant_agent, message=message
        )
