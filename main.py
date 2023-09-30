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

from autogen import GroupChat, GroupChatManager, UserProxyAgent
from agents import ProductOwner, SoftwareEngineer
from constants import FULL_LLM_CONFIG
import utils


# CEO Human Proxy Agent
# Uses shell with human-in-the-loop, meaning the human user can either give their input when asked,
# or ignore step, to let the agent interactions continue from there.
ceo_user_proxy_agent = UserProxyAgent(
    "CEO",
    # code_execution_config={"work_dir": "coding"},
    code_execution_config={"work_dir": "coding"},
    human_input_mode="NEVER",
    llm_config=FULL_LLM_CONFIG,
    # is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    # max_consecutive_auto_reply=10,
    system_message=utils.clean_text(
        """
            For coding tasks, only use the functions you have been provided with.
            Always provide the full absolute path of the files you create or edit in your messages.

            Reply TERMINATE if the task has been solved at full satisfaction.
            Otherwise, reply CONTINUE, or the reason why the task is not solved yet.
        """
    ),
)

product_owner = ProductOwner()
software_engineer = SoftwareEngineer()

product_owner.attach_agents(software_engineer=software_engineer)
software_engineer.attach_agents(product_owner=product_owner)


def run_shell_script(script):
    return ceo_user_proxy_agent.execute_code_blocks([("sh", script)])


def software_engineer_ask_ceo(message: str):
    software_engineer.as_assistant_agent.initiate_chat(
        recipient=ceo_user_proxy_agent, message=message
    )

    print(
        f"[DEBUG] software_engineer_ask_ceo() > last_message() = {software_engineer.as_assistant_agent.last_message()}"
    )
    return software_engineer.as_assistant_agent.last_message()["content"]


ceo_user_proxy_agent.register_function(
    function_map={
        # "product_owner_ask_software_engineer": product_owner.ask_software_engineer,
        "run_shell_script": run_shell_script,
        # "software_engineer_ask_ceo": software_engineer.ask_ceo,
        # "software_engineer_ask_product_owner": software_engineer.ask_product_owner,
    },
)
product_owner.as_assistant_agent.register_function(
    function_map={
        "run_shell_script": run_shell_script,
    },
)
software_engineer.as_assistant_agent.register_function(
    function_map={
        "run_shell_script": run_shell_script,
    },
)

group_chat = GroupChat(
    admin_name="Administrator",
    agents=[
        ceo_user_proxy_agent,
        product_owner.as_assistant_agent,
        software_engineer.as_assistant_agent,
    ],
    messages=[],
    max_round=100,
)

group_chat_manager = GroupChatManager(groupchat=group_chat, llm_config=FULL_LLM_CONFIG)

ceo_user_proxy_agent.initiate_chat(
    # recipient=product_owner.as_assistant_agent,
    recipient=group_chat_manager,
    message=utils.clean_text(
        """
        Product Owner, develop and run a CLI snake game. In Rust.
        """,
    ),
)
