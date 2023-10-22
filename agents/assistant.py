import autogen

import actions
import agents
from constants import COMMON_LLM_CONFIG
from utils import clean_text
import utils

COMMAND_DISPATCH_DICT = {
    "OPEN": actions.fetch_web_page,
    "READ": actions.read_file,
    "SEARCH": actions.search_web,
    "WRITE": actions.write_file,
}


class Assistant(agents.BaseAgent):
    ceo_user_proxy_agent: autogen.UserProxyAgent

    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Assistant",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                Your are the CEO's assistant.

                You can run commands by replying using a specific syntax: "A_COMMAND [param_1] [param_2]" (without double quotes).
                To run this command, you must reply with the command alone, without any other text. Otherwise it won't work.
                You are expected to use these commands in chain until you can give a well-informed solution to the CEO's requests.
                Each time you run a command, the CEO will run your command and reply to you with its result.

                Here are the available commands:
                - "OPEN [url]" to get the content of a web page as basic markdown.
                - "READ [file_path]" to read the content of a file.
                - "SEARCH [query]" to search the web and get a JSON of ranked results.
                - "WRITE [file_path] [file_content]" to create or edit a file.

                Here is a process example:

                ```md
                1. The CEO asks you "What are the features of SimCity 2000 game?".
                2. You reply "SEARCH SimCity 2000 features".
                3. You receive a message with the JSON of results from the CEO.
                4. You write a first analysis of the results, as well as the most interesting pages URL to visit, in a file
                   by replying "WRITE .oads/ASSISTANT.md [your_analysis_and_tasks_as_mardown]"
                   (replacing the bracketed parameter with your Markdown source).
                6. You receive a message of confirmation from the CEO.
                7. You reply "OPEN [first_url_of_interest]"
                   (replacing the bracketed parameter with the correct URL).
                8. You receive a message with the content of the web page from the CEO.
                9. You analyze the content of the web page and update your analysis and tasks in the file
                   by replying "WRITE .oads/ASSISTANT.md [your_updated_analysis_and_tasks_as_mardown]"
                   (replacing the bracketed parameter with your Markdown source).

                And so on... you repeat steps 7, 8 and 9 until you are done visiting all the URLs of interest.

                Once you are done visiting the URLs of interest, you answer the original CEO's question with your analysis,
                ending the message with "TERMINATE" to end the conversation.
                ```
                """
            ),
        )

    async def start(
        self, ceo_user_proxy_agent: autogen.UserProxyAgent, initial_prompt: str
    ):
        self.ceo_user_proxy_agent = ceo_user_proxy_agent

        self.as_assistant_agent.clear_history()
        self.ceo_user_proxy_agent.clear_history()

        await self._ask(initial_prompt)

    async def _ask(self, message: str):
        await self.as_assistant_agent.a_receive(
            message=utils.clean_text(message),
            request_reply=True,
            sender=self.ceo_user_proxy_agent,
            silent=False,
        )

        last_message: str = self.as_assistant_agent.last_message(
            self.ceo_user_proxy_agent
        )["content"]

        maybe_command_tuple = utils.get_command_from_message(last_message)
        if maybe_command_tuple is None:
            await self._ask_for_ceo_input()

            return

        elif isinstance(maybe_command_tuple, str):
            action_message = maybe_command_tuple

        else:
            command, parameters = maybe_command_tuple

            func = COMMAND_DISPATCH_DICT.get(command)
            if func is None:
                raise ValueError(f"Unknown AI Command: `{command}`.")

            action_message = func(*parameters)

        await self._ask(action_message)

    async def _ask_for_ceo_input(self):
        ceo_message = self.as_assistant_agent.get_human_input("Prompt:\n\n")

        await self._ask(ceo_message)
