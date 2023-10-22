import re
from typing import List, Tuple

import utils


# AGENT_COMMANDS = {"OPEN", "READ", "RUN", "SEARCH", "TERMINATE", "WRITE"}
def get_command_from_message(message: str) -> Tuple[str, List[str]] | str | None:
    if message == "TERMINATE":
        return "TERMINATE", []

    pattern = re.compile(r"^\s*(OPEN|READ|SEARCH|WRITE)\s*(.*)\s*$")
    match = pattern.search(message)
    if not match:
        return None

    command = utils.ensure_str(match.group(1))
    parameter = utils.ensure_str(match.group(2)).strip()

    if command == "WRITE":
        file_path, *file_content = parameter.split(" ", 1)
        if not file_content:
            return "The WRITE command requires both a file path and file content."

        return command, [file_path, " ".join(file_content)]

    parameters = [parameter]

    return command, parameters
