"""
Module Name: main.py

Short Description:
This program intend to leverage Microsoft Autogen in order to automate software development via AI agents.

Detailed Description:
Microsoft Autogen is a framework that enables development of LLM applications
using multiple agents that can converse with each other to solve task.
AutoGen agents are customizable, conversable, and seamlessly allow human participation.
They can operate in various modes that employ combinations of LLMs, human inputs, and tools.

We use OpenAI API in our case.
"""

import autogen

import actions
import agents
from constants import COMMON_LLM_CONFIG, PROJECT_CONFIG, PROJECT_DIRECTORY_NAME
import utils


# CEO Human Proxy Agent
# Uses shell with human-in-the-loop, meaning the human user can either give their input when asked,
# or ignore step, to let the agent interactions continue from there.
ceo_user_proxy_agent = autogen.UserProxyAgent(
    "CEO",
    code_execution_config={"work_dir": PROJECT_DIRECTORY_NAME},
    human_input_mode="TERMINATE",
    llm_config=COMMON_LLM_CONFIG,
    # is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    # max_consecutive_auto_reply=10,
    system_message=utils.clean_text(
        """
            If there is an "impossible" issue, ask the Product Manager to find an alternative solution.

            Reply TERMINATE if either the task has been solved at full satisfaction or if the team is stuck.
            Otherwise, reply CONTINUE.
        """
    ),
)


COMMON_FUNCTION_MAP = {
    "fetch_web_page": actions.fetch_web_page,
    "read_file": actions.read_file,
    "run_bash_command": actions.run_bash_command,
    "run_rust_file": actions.run_rust_file,
    "search_web": actions.search_web,
    "write_file": actions.write_file,
}

ceo_user_proxy_agent.register_function(
    function_map=COMMON_FUNCTION_MAP,
)

product_owner = agents.ProductOwner()
product_owner.as_assistant_agent.register_function(
    function_map=COMMON_FUNCTION_MAP,
)

quality_analyst = agents.QualityAnalyst()
quality_analyst.as_assistant_agent.register_function(
    function_map=COMMON_FUNCTION_MAP,
)

software_engineer = agents.SoftwareEngineer()
software_engineer.as_assistant_agent.register_function(
    function_map=COMMON_FUNCTION_MAP,
)

user_experience_designer = agents.UserExperienceDesigner()
user_experience_designer.as_assistant_agent.register_function(
    function_map=COMMON_FUNCTION_MAP,
)

group_chat = autogen.GroupChat(
    admin_name="Administrator",
    agents=[
        ceo_user_proxy_agent,
        product_owner.as_assistant_agent,
        quality_analyst.as_assistant_agent,
        software_engineer.as_assistant_agent,
        user_experience_designer.as_assistant_agent,
    ],
    messages=[],
    max_round=100,
)

group_chat_manager = autogen.GroupChatManager(
    groupchat=group_chat, llm_config=COMMON_LLM_CONFIG
)

utils.print_project_config(PROJECT_CONFIG)

if PROJECT_CONFIG["initial_project_description"] is None:
    initial_project_description = product_owner.as_assistant_agent.get_human_input(
        "Product Owner: You didn't specify a project in `env.jsonc`. What do you want us to develop?\n\nCEO: "
    )
else:
    initial_project_description = PROJECT_CONFIG["initial_project_description"]

ceo_user_proxy_agent.initiate_chat(
    recipient=group_chat_manager,
    message=utils.clean_text(initial_project_description),
)
