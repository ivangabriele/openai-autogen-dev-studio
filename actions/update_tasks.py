import json
from typing import List

from actions.base_action import BaseAction
from actions.write_file import WriteFileAction
import typedefs


class UpdateTasksAction(BaseAction):
    _description = {
        "name": "update_tasks",
        "description": "Update the entire task list file by replacing it with the new tasks.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "Tasks file name.",
                },
                "tasks_as_strs": {
                    "type": "array",
                    "description": "List of tasks.",
                    "items": {
                        "type": "string",
                    },
                },
            },
            "required": ["updated_tasks"],
        },
    }

    # pylint: disable=arguments-differ
    @staticmethod
    def run(file_name: str, tasks_as_strs: List[str]) -> str:
        """
        Write content to a file. Create the file and/or directories if they don't exist.
        """

        tasks = [
            (index, UpdateTasksAction.get_task_from_task_as_str)
            for index, item in enumerate(tasks_as_strs)
        ]
        tasks_as_json = json.dumps(tasks)

        return WriteFileAction.run(relative_path=file_name, file_source=tasks_as_json)

    @staticmethod
    def get_task_from_task_as_str(tasks_as_str: str, index: int) -> typedefs.TaskDict:
        return {
            "index": index,
            "description": tasks_as_str,
            "is_done": False,
        }
