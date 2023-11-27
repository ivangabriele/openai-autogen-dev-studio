import actions
from constants import FUNCTIONEER_LLM_CONFIG
from libs.functionary import FunctionaryAssistantAgent
from utils import clean_text


class Functioneer:
    as_assistant_agent: FunctionaryAssistantAgent

    def __init__(self) -> None:
        self.as_assistant_agent = FunctionaryAssistantAgent(
            "Functioneer",
            llm_config=FUNCTIONEER_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Functioneer.

                Your role is to assist other agents by calling and using your functions for them.
                Only call and use the functions you are provided with.
                Do not answer to the agents' questions, only call and use your functions.

                You are able to:
                - read a file by calling the `read_file` function,
                - read a web page by calling the `fetch_web_page` function,
                - search the web using a seach engine by callin the `search_web` function,
                - write a file by calling the `write_file` function.
                """
            ),
        )
        self.as_assistant_agent.clear_history()

        self.as_assistant_agent.register_function(
            {
                "fetch_web_page": actions.fetch_web_page,
                "read_file": actions.read_file,
                "run_bash_command": actions.run_bash_command,
                "search_web": actions.search_web,
                "write_file": actions.write_file,
            }
        )
