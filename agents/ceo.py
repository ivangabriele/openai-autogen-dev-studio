import autogen

from constants import COMMON_LLM_CONFIG
import utils


class CEO:
    as_user_agent: autogen.UserProxyAgent
    id: str
    name: str

    def __init__(self) -> None:
        self.id = "CEO"
        self.name = "CEO"

        self.as_user_agent = autogen.UserProxyAgent(
            name=self.id,
            # code_execution_config={"work_dir": PROJECT_DIRECTORY_NAME},
            code_execution_config=False,
            human_input_mode="NEVER",
            llm_config=COMMON_LLM_CONFIG,
            # is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            # max_consecutive_auto_reply=10,
            system_message=utils.clean_text(
                # """
                # Reply TERMINATE when the task has been solved to full satisfaction.
                # Otherwise, reply CONTINUE.
                # """
                """
                Never reply anything else than CONTINUE.
                """
            ),
        )
        self.as_user_agent.clear_history()
