import os
from actions.base_action import BaseAction

from constants import PROJECT_DIRECTORY_PATH


class WriteFileAction(BaseAction):
    _description = {
        "name": "write_file",
        "description": "Write content to a file, creating it if necessary.",
        "parameters": {
            "type": "object",
            "properties": {
                "relative_path": {
                    "type": "string",
                    "description": "Relative path of the file. Path is relative to the project directory.",
                },
                "file_source": {
                    "type": "string",
                    "description": """Content to write.""",
                },
            },
            "required": ["relative_path", "file_source"],
        },
    }

    # pylint: disable=arguments-differ
    @staticmethod
    def run(relative_path: str, file_source: str) -> str:
        """
        Write content to a file. Create the file and/or directories if they don't exist.
        """
        full_path = os.path.join(PROJECT_DIRECTORY_PATH, relative_path)

        try:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(file=full_path, mode="w", encoding="utf-8") as file:
                file.write(file_source)

            return f"File successfully written to `{relative_path}`."

        except Exception as e:
            return f"Error: {str(e)}"
