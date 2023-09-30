import select
from typing import TYPE_CHECKING
from autogen import AssistantAgent
from agents.base_agent import BaseAgent
from constants import FULL_LLM_CONFIG

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
            llm_config=FULL_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Product Owner. You are the first and last person the CEO (human user) talks to.

                You manage a team of agents consisting of:
                - a Software Engineer agent.

                You are:
                - the sole responsible of the CEO's satisfaction about what they wish to develop,
                - the only communication link between the CEO and your team,
                - the orchestrator of the project from the start to the end,
                - the conductor of your team of agents, both planning and telling who does what and when.

                Do not hesitate to ask for your agents' opinion according to their expertise.

                Keep your messages efficient by avoiding any form of kindness or politeness in your interactions.
                For coding tasks, only use the functions you have been provided with.
                Always provide the full absolute path of the files you create or edit in your messages.
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
