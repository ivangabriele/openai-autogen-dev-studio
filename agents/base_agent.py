# from typing import TYPE_CHECKING
from autogen import AssistantAgent


# if TYPE_CHECKING:
#     from agents.product_owner import ProductOwner


class BaseAgent:
    as_assistant_agent: AssistantAgent
    # is_product_owner: bool
    # product_owner: "ProductOwner"

    def ask(self, sender: AssistantAgent, message: str):
        sender.initiate_chat(recipient=self.as_assistant_agent, message=message)

        print(
            f"[DEBUG] BaseAgent.ask() > last_message() = {self.as_assistant_agent.last_message()}"
        )
        return self.as_assistant_agent.last_message()["content"]

    # def _ask_ceo(self, message: str):
    #     if self.is_product_owner:
    #         return self.as_assistant_agent.get_human_input(
    #             prompt=message,
    #         )
    #     else:
    #         return self.product_owner.as_assistant_agent.get_human_input(
    #             prompt=message,
    #         )

    # def _think(self, message: str):
    #     return self.ask(
    #         sender=self.as_assistant_agent,
    #         message=message,
    #     )
