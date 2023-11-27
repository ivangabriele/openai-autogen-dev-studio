import json
from typing import List
import autogen

import actions
from constants import COMMON_LLM_CONFIG
import typedefs
from utils import clean_text
import utils


class Planner:
    as_assistant_agent: autogen.AssistantAgent

    def __init__(self) -> None:
        self.as_assistant_agent = autogen.AssistantAgent(
            "Planner",
            llm_config=COMMON_LLM_CONFIG
            | {
                "functions": [
                    actions.UpdateTasksAction.get_description(),
                ]
            },
            system_message=clean_text(
                """
                You are the Planner.

                Your role is to update the task list using the `update_tasks` function call.
                """
            ),
        )

        self.as_assistant_agent.register_function(
            {
                "update_tasks": actions.UpdateTasksAction.run,
            }
        )

    @staticmethod
    def get_current_tasks_as_message(file_name: str) -> str:
        try:
            tasks_as_json = utils.read_file(file_name)
            tasks: List[typedefs.TaskDict] = json.loads(tasks_as_json)
            tasks_as_message = "\n".join(
                [
                    f"{task['index']}. [{'x' if task['is_done'] else ' '}] {task['description']}"
                    for task in tasks
                ]
            )

            return tasks_as_message

        except FileNotFoundError:
            return "No task yet."
