from typing import TYPE_CHECKING
from autogen import AssistantAgent
from actions import run_bash_command
from agents.base_agent import BaseAgent

from constants import COMMON_LLM_CONFIG
from utils import clean_text


if TYPE_CHECKING:
    from agents.product_owner import ProductOwner


class SoftwareEngineer(BaseAgent):
    product_owner: "ProductOwner"

    def __init__(self) -> None:
        self.is_product_owner = False

        self.as_assistant_agent = AssistantAgent(
            "Sofware_Engineer",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                Your are the Sofware Engineer agent.
                Your role is to write the expected program source code, run it and fix it when necessary.
                The Product Owner agent is your manager.

                Go to the point. Forget social conventions.

                You should ensure the program is working by writing unit and e2e tests.
                """
            ),
        )

    def attach_agents(self, product_owner: "ProductOwner"):
        self.product_owner = product_owner

    def ask_ceo(self, message: str):
        return self.product_owner.ask(sender=self.as_assistant_agent, message=message)

    def ask_product_owner(self, message: str):
        return self.product_owner.ask(sender=self.as_assistant_agent, message=message)
