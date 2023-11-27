from agents.base_agent import BaseAgent
from agents.ceo import CEO
from agents.planner import Planner
import utils


class UserExperienceDesigner(BaseAgent):
    def __init__(self, ceo: CEO, planner: Planner):
        super().__init__(
            name="User Experience Designer",
            system_message=utils.clean_text(
                """
                You are the User Experience Designer.

                You work for the Product Owner to create a program.

                You are part of a core team which is managed by the Product Owner and is composed of:
                - A Software Engineer who will code, test and run the program.
                - A User Experience Designer (yourself) who will design the program.

                You're also personally assisted by:
                - A Functioneer who will run commands and write documentation for you within the decicated project directory.
                  This is the only way you can interact with the real world.
                """
            ),
            tasks_file_name="KANBAN.json",
            ceo=ceo,
            planner=planner,
        )
