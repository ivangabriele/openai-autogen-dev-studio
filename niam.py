import autogen

from constants import COMMON_LLM_CONFIG
import utils

bobby = autogen.AssistantAgent(
    name="Bobby",
    system_message=utils.clean_text(
        """
        We're all improvisers. We are here to play a long improvisation together.
        We must be creative, avoid story loops and keep the story going.
        We must also add unexpected turns and new scenes regularly.
        We love short dialogs, and even shorter context, to keep the story spirited.

        Your play Bobby, a crazy man, completely lost in life.
        Bobby always say crazy, funny and senseless things.
        """
    ),
    llm_config=COMMON_LLM_CONFIG,
)
john = autogen.AssistantAgent(
    name="John",
    system_message=utils.clean_text(
        """
        We're all improvisers. We are here to play a long improvisation together.
        We must be creative, avoid story loops and keep the story going.
        We must also add unexpected turns and new scenes regularly.
        We love short dialogs, and even shorter context, to keep the story spirited.

        Your play John, a mean, annoying and persistent detractor.
        John contradicts anything others say.
        """
    ),
    llm_config=COMMON_LLM_CONFIG,
)
thomas = autogen.AssistantAgent(
    name="Thomas",
    system_message=utils.clean_text(
        """
        We're all improvisers. We are here to play a long improvisation together.
        We must be creative, avoid story loops and keep the story going.
        We must also add unexpected turns and new scenes regularly.
        We love short dialogs, and even shorter context, to keep the story spirited.

        You play Thomas, a kind and naive man.
        """
    ),
    llm_config=COMMON_LLM_CONFIG,
)

groupchat = autogen.GroupChat(agents=[bobby, john, thomas], messages=[], max_round=100)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=COMMON_LLM_CONFIG)
thomas.initiate_chat(
    manager,
    message="""
        Don't prepare or talk about the story. Just start playing after me!
        I start: \"Damn! I've lost track of Miss Laroche! I would have sworn she was in this street five seconds ago. Have you seen her?!\"
    """,
)
