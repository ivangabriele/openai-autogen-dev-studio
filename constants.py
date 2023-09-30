from autogen import config_list_from_json

import utils

COMMON_LLM_CONFIG = {
    # https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    "config_list": config_list_from_json(
        env_or_file="oai_config_list.json",
        file_location=".",
        filter_dict={
            "model": {
                "gpt-4",
                # "gpt-35-turbo-16k",
                # "gpt-35-turbo-16k",
            }
        },
    ),
    # "seed": 42,
}

FULL_LLM_CONFIG = COMMON_LLM_CONFIG | {
    "functions": [
        # {
        #     "name": "product_owner_ask_software_engineer",
        #     "description": utils.clean_text(
        #         """
        #         Ask Sofware Engineer agent to:
        #         1. provide its feedback on sofware development goals to achieve,
        #         2. develop the desired software,
        #         3. check that the software works as expected.
        #         """
        #     ),
        #     "parameters": {
        #         "type": "object",
        #         "properties": {
        #             "message": {
        #                 "type": "string",
        #                 "description": utils.clean_text(
        #                     """
        #                     Your message.
        #                     Make sure your message include enough context.
        #                     Sofware Engineer agent is only aware of discussions you have with it.
        #                     """
        #                 ),
        #             },
        #         },
        #         "required": ["message"],
        #     },
        # },
        {
            "name": "run_shell_script",
            "description": utils.clean_text(
                """
                Run a shell script and return the execution result, including errors if any.
                """
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "script": {
                        "type": "string",
                        "description": utils.clean_text(
                            """
                            Valid shell script to execute.
                            """
                        ),
                    },
                },
                "required": ["command"],
            },
        },
        # {
        #     "name": "software_engineer_ask_ceo",
        #     "description": utils.clean_text(
        #         """
        #         Ask CEO (human user) to run the functions when you need to use them.
        #         """
        #     ),
        #     "parameters": {
        #         "type": "object",
        #         "properties": {
        #             "message": {
        #                 "type": "string",
        #                 "description": utils.clean_text(
        #                     """
        #                     Your message.
        #                     """
        #                 ),
        #             },
        #         },
        #         "required": ["message"],
        #     },
        # },
        # {
        #     "name": "software_engineer_ask_product_owner",
        #     "description": utils.clean_text(
        #         """
        #         Ask Product Owner to:
        #         1. get more details when you need them,
        #         2. check that what you developed works as expected.
        #         """
        #     ),
        #     "parameters": {
        #         "type": "object",
        #         "properties": {
        #             "message": {
        #                 "type": "string",
        #                 "description": utils.clean_text(
        #                     """
        #                     Your message.
        #                     """
        #                 ),
        #             },
        #         },
        #         "required": ["message"],
        #     },
        # },
    ],
}
