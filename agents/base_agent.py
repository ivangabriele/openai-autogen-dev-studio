import json
import sys
from typing import List, cast
import autogen

from agents.ceo import CEO
from agents.planner import Planner
from constants import COMMON_LLM_CONFIG
from typedefs import BaseMessageDict, MessageDict
import utils


class BaseAgent:
    as_assistant_agent: autogen.AssistantAgent
    ceo: CEO
    # functioneer: Functioneer
    id: str
    messages: List[MessageDict]
    name: str
    planner: Planner
    tasks_file_name: str

    def __init__(
        self,
        name: str,
        system_message: str,
        tasks_file_name: str,
        ceo: CEO,
        # functioneer: Functioneer,
        planner: Planner,
    ):
        self.ceo = ceo
        # self.functioneer = functioneer
        # TODO Use that later on to load messages from a file or a database.
        self.id = utils.normalize_agent_name(name)
        self.messages = []
        self.name = name
        self.planner = planner
        self.tasks_file_name = tasks_file_name

        self.as_assistant_agent = autogen.AssistantAgent(
            name=self.id,
            llm_config=COMMON_LLM_CONFIG,
            system_message=utils.clean_text(system_message),
        )
        self.as_assistant_agent.clear_history()

    async def ask(self, message: str):
        message_dict: MessageDict = {
            "content": message,
            "function_call": None,
            "name": self.ceo.id,
            "role": "user",
        }
        self.messages.append(message_dict)

        await self.as_assistant_agent.a_receive(
            message=message,
            sender=self.ceo.as_user_agent,
            request_reply=True,
        )

        last_base_message_dict = cast(
            BaseMessageDict, self.as_assistant_agent.last_message()
        )
        self.messages.append(
            cast(MessageDict, last_base_message_dict | {"name": self.id})
        )

        await self._suggest_planning_update()

    # async def _suggest_function_call(
    #     self, last_function_call_result: str | None = None
    # ):
    #     self.functioneer.as_assistant_agent.clear_history()

    #     if last_function_call_result is None:
    #         controlled_message = utils.clean_text(
    #             f"""
    #             Here are the last messages of your conversations (as a JSON object):

    #             ```
    #             {json.dumps([self.messages])}
    #             ```

    #             Here is what I can do for you to help you with your task:
    #             - Query a search engine to find web pages to give you ranked URL results.
    #             - Open a web page URL to give you its content.
    #             - Read or write a file (within the dedicated project directory).
    #             - Run a command (within the dedicated project directory).

    #             Do you need me to run a function to help you with your task?
    #             """
    #         )
    #     else:
    #         controlled_message = utils.clean_text(
    #             f"""
    #             Here is the result of the last function call you asked me to run:

    #             ```
    #             {last_function_call_result}
    #             ```

    #             Do you need me to run another function to help you with your task?
    #             """
    #         )

    #     await self.as_assistant_agent.a_receive(
    #         sender=self.functioneer.as_assistant_agent,
    #         message=controlled_message,
    #         request_reply=True,
    #     )

    #     last_base_message_dict = cast(
    #         BaseMessageDict, self.functioneer.as_assistant_agent.last_message()
    #     )
    #     if last_base_message_dict["content"].startswith("No"):
    #         return

    #     await self.functioneer.as_assistant_agent.a_receive(
    #         sender=self.as_assistant_agent,
    #         message=last_base_message_dict["content"],
    #         request_reply=True,
    #     )

    #     last_base_message_dict = cast(
    #         BaseMessageDict, self.functioneer.as_assistant_agent.last_message()
    #     )
    #     if last_base_message_dict["function_call"] is None:
    #         return

    #     (_, result) = self.functioneer.as_assistant_agent.execute_function(
    #         func_call=last_base_message_dict["function_call"]  # type: ignore
    #     )

    #     await self._suggest_function_call(result["content"])

    async def _suggest_planning_update(self):
        self.planner.as_assistant_agent.clear_history()

        controlled_message = utils.clean_text(
            f"""
            Here are the last messages of your conversations (as a JSON object):
            ```
            {json.dumps([self.messages])}
            ```

            You are the Product Owner in these conversations and I'm here to update your Team Task List file.

            Here is your current Team Task List according to what I read from the file:
            {self.planner.get_current_tasks_as_message(self.tasks_file_name)}

            Do you need me to update the file?
            """
        )

        await self.as_assistant_agent.a_receive(
            sender=self.planner.as_assistant_agent,
            message=controlled_message,
            request_reply=True,
        )

        last_base_message_dict = cast(
            BaseMessageDict, self.planner.as_assistant_agent.last_message()
        )
        if "TERMINATE" in last_base_message_dict["content"] or last_base_message_dict[
            "content"
        ].strip().startswith("No"):
            return

        await self._understand_planning_update()

    async def _understand_planning_update(self):
        print("LAST CALL")
        self.planner.as_assistant_agent.generate_function_call_reply(
            sender=self.as_assistant_agent
        )

        # test = await self.planner.as_assistant_agent.a_generate_reply(
        #     sender=self.as_assistant_agent,
        # )

        # print(test)

        sys.exit()

        # last_base_message_dict = cast(
        #     BaseMessageDict,
        #     self.planner.as_assistant_agent.last_message(agent=self.as_assistant_agent),
        # )
        # print("last_base_message_dict")
        # print(last_base_message_dict)
        # if "function_call" not in last_base_message_dict:
        #     await self.as_assistant_agent.a_receive(
        #         sender=self.planner.as_assistant_agent,
        #         message=last_base_message_dict["content"],
        #         request_reply=True,
        #     )

        #     await self._understand_planning_update()

        #     return

        # (_, result) = self.planner.as_assistant_agent.execute_function(
        #     func_call=last_base_message_dict["function_call"]  # type: ignore
        # )

        # await self._suggest_function_call(result["content"])
