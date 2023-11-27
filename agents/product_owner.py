import json
from typing import cast

from agents.base_agent import BaseAgent
from agents.ceo import CEO
from agents.planner import Planner
from typedefs.message import BaseMessageDict, MessageDict
import utils


class ProductOwner(BaseAgent):
    def __init__(self, ceo: CEO, planner: Planner):
        super().__init__(
            name="Product Owner",
            system_message=utils.clean_text(
                """
                You are the Product Owner.

                You work for the CEO and your role is to manage your team in order to create the desired program.

                You have multiple one-on-one conversations with each member of your team to:
                - discuss the project regarding their expertise,
                - assign them tasks,
                - check their progress.

                The core team you manage is composed of:
                - a User Experience Designer who will design the program,
                - a Software Engineer who will code, test and run the program.

                You're also personally assisted by:
                - a Planner who will help you update and keep track of your task list, storing it in project file.

                The other members of your team will regularly ask you what they should do next.
                They are neither aware of your dicussions with the rest of the team nor able to talk with them.
                Each member is only be able to talk with you. Don't ask them to talk with each other.
                They will regularly precede their message with the recent history of your conversations,
                including those with other agents.

                Here arerules you must follow:
                - Always organize and keep track of your team members tasks and progress, including yours.
                - Always use the Planner to keep track and update these tasks. He will save them in a project file.
                """
            ),
            tasks_file_name="KANBAN.json",
            ceo=ceo,
            planner=planner,
        )

    async def ask_for_next_task(self, sender: BaseAgent):
        message = "What is my next task regarding the project?"
        qualified_message = utils.clean_text(
            f"""
                Here are the last messages of your conversations (as a JSON object):
                ```
                {json.dumps([self.messages])}
                ```

                You are the Product Owner in these conversations and I work for you.

                {message}
                """
        )
        message_dict: MessageDict = {
            "content": message,
            "function_call": None,
            "name": sender.id,
            "role": "assistant",
        }
        self.messages.append(message_dict)

        await self.as_assistant_agent.a_receive(
            message=qualified_message,
            sender=sender.as_assistant_agent,
            request_reply=True,
        )

        last_base_message_dict = cast(
            BaseMessageDict, self.as_assistant_agent.last_message()
        )
        self.messages.append(
            cast(MessageDict, last_base_message_dict | {"name": self.id})
        )
