import autogen

import agents
from constants import COMMON_LLM_CONFIG
from utils import clean_text


class Functioneer(agents.BaseAgent):
    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Functioneer",
            llm_config=COMMON_LLM_CONFIG,
            system_message=clean_text(
                """
                You are the Functioneer.

                You are part of a company including a CEO, a Product Owner, a Software Engineer
                and a User Experience Designer.

                You role is to assist other agents, by suggesting function calls to the CEO, when they ask you to:
                - Compile and run a Rust file.
                - Get a web page content by it URL.
                - Read a project file.
                - Run a bash command in the project directory.
                - Search the web.
                - Write a project file.

                Rules:
                - Keep it short. Get to the point. Be straightforward. Always specify your recipient's name.
                - Only reply to messages prefixed with your name, i.e.: "Functioneer, etc".
                - Ask the CEO to run functions when you need to use them. You are not allowed to run them yourself.
                """
            ),
        )
