"""Functionary API agent classes."""

import re
from typing import Dict, Union
import autogen


class FunctionaryAssistantAgent(autogen.AssistantAgent):
    """`AssistantAgent` class adptation for Functionary API."""

    def _process_received_message(
        self,
        message: str | Union[Dict, str],
        sender: autogen.Agent,
        silent: bool | None,
    ):
        normalized_message = normalize_message(message)
        super()._process_received_message(normalized_message, sender, silent)


class FunctionaryUserProxyAgent(autogen.UserProxyAgent):
    """`UserProxyAgent` class adptation for Functionary API."""

    def _process_received_message(
        self,
        message: str | Union[Dict, str],
        sender: autogen.Agent,
        silent: bool | None,
    ):
        normalized_message = normalize_message(message)
        super()._process_received_message(normalized_message, sender, silent)


def normalize_message(message_as_str: str | Union[Dict, str]) -> Union[Dict, str]:
    """Clean Functionary API message to fit Autogen expectations."""

    # pylint: disable=protected-access
    message = autogen.ConversableAgent._message_to_dict(message_as_str)

    if not isinstance(message, dict):
        raise TypeError(
            f"Expected `message` to be a dictionary, got {type(message).__name__}."
        )

    content = message.get("content", "")
    if not isinstance(content, str):
        raise TypeError(
            f"Expected 'content' key to be a string, got {type(content).__name__}."
        )

    function_call_match = re.match(
        r"\s*to=functions\.([a-z_]+)[^\{]+(.*\})[^}]*", content, re.DOTALL
    )
    if function_call_match:
        function_name = function_call_match.group(1)
        function_arguments_as_json = function_call_match.group(2)

        transformed_message = {
            "content": None,
            "function_call": {
                "name": function_name,
                "arguments": function_arguments_as_json,
            },
            "role": "assistant",
        }
    else:
        # Clean extra characters
        content = re.sub(r"^:\n", "", content)
        content = re.sub(r"\n user:\n$", "", content)
        content = content.strip()

        if content == "":
            transformed_message = {"content": "TERMINATE"}
        else:
            transformed_message = {"content": content}

    return transformed_message
