"""
Module Name: main.py

Short Description:
This program intends to leverage Microsoft Autogen to automate software development via AI agents.

Detailed Description:
Microsoft Autogen is a framework that enables the development of LLM (Lifelong Learning Machines) applications
using multiple agents capable of conversing with each other to solve tasks.
Autogen agents are customizable, conversable, and can seamlessly incorporate human participation.
These agents can operate in various modes, utilizing combinations of LLMs, human input, and other tools.
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
        You are the CEO.

        You are assisted by a Product Owner who will try his best to achieve your goals with the team under his orders.
        Your are the only agent allowed to run functions.

        Rules:
        - Keep it short. Get to the point. Be straightforward. Always specify your recipient's name.
        - Only reply to messages prefixed with your name, i.e.: "CEO, etc".
        - Only communicate with the Product Owner, and nobody else.

        Reply TERMINATE when the task has been solved to full satisfaction.
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


functioneer = agents.Functioneer()
# functioneer.as_assistant_agent.register_function(
#     function_map=COMMON_FUNCTION_MAP,
# )

product_owner = agents.ProductOwner()
# product_owner.as_assistant_agent.register_function(
#     function_map=COMMON_FUNCTION_MAP,
# )

software_engineer = agents.SoftwareEngineer()
# software_engineer.as_assistant_agent.register_function(
#     function_map=COMMON_FUNCTION_MAP,
# )

user_experience_designer = agents.UserExperienceDesigner()
# user_experience_designer.as_assistant_agent.register_function(
#     function_map=COMMON_FUNCTION_MAP,
# )

group_chat = autogen.GroupChat(
    admin_name="Administrator",
    agents=[
        ceo_user_proxy_agent,
        functioneer.as_assistant_agent,
        product_owner.as_assistant_agent,
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

if PROJECT_CONFIG.initial_project_description is None:
    initial_project_description = ceo_user_proxy_agent.get_human_input(
        "You didn't specify a project in `env.jsonc`. What do you want us to develop?\nRequest: "
    )
else:
    initial_project_description = PROJECT_CONFIG.initial_project_description

ceo_user_proxy_agent.initiate_chat(
    recipient=group_chat_manager,
    message=utils.clean_text(
        f"Product Owner, I want your team to achieve these goals:\n- {initial_project_description}"
    ),
)
