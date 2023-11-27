import os

from actions.base_action import BaseAction

from constants import PROJECT_DIRECTORY_PATH


class ReadFileAction(BaseAction):
    _description = {
        "name": "read_file",
        "description": "Read and return a file content.",
        "parameters": {
            "type": "object",
            "properties": {
                "relative_path": {
                    "type": "string",
                    "description": "Relative path of the file. Path is relative to the project directory.",
                },
            },
            "required": ["relative_path"],
        },
    }

    # pylint: disable=arguments-differ
    @staticmethod
    def read_file(relative_path: str) -> str:
        """
        Read content from a file and return it.
        """

        full_path = os.path.join(PROJECT_DIRECTORY_PATH, relative_path)

        with open(file=full_path, mode="r", encoding="utf-8") as file:
            return file.read()
