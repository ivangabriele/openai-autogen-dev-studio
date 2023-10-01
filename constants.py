from autogen import config_list_from_json
import os


COMMON_LLM_CONFIG = {
    # https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    "config_list": config_list_from_json(
        env_or_file="oai_config_list.json",
        file_location=".",
        filter_dict={
            "model": {
                # "gpt_35_turbo_16k",
                # "gpt-3.5-turbo-16k",
                "gpt-4",
            }
        },
    ),
    "functions": [
        {
            "name": "read_file",
            "description": "Read and return a file content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "relative_path": {
                        "type": "string",
                        "description": "Relative path of the file.",
                    },
                },
                "required": ["relative_path"],
            },
        },
        {
            "name": "run_bash_command",
            "description": "Run a bash command and return the output.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "Bash command.",
                    },
                },
                "required": ["command"],
            },
        },
        {
            "name": "run_rust_file",
            "description": "Compile a rust file into `./temp_executable` and execute it.",
            "parameters": {
                "type": "object",
                "properties": {
                    "rust_file_path": {
                        "type": "string",
                        "description": "Rust file path.",
                    },
                },
                "required": ["rust_file_path"],
            },
        },
        {
            "name": "write_file",
            "description": "Write content to a file, creating it if necessary.",
            "parameters": {
                "type": "object",
                "properties": {
                    "relative_path": {
                        "type": "string",
                        "description": "Relative path of the file.",
                    },
                    "file_source": {
                        "type": "string",
                        "description": """Content to write.""",
                    },
                },
                "required": ["relative_path", "file_source"],
            },
        },
    ],
    # "seed": 42,
}

PROJECT_DIRECTORY_NAME = "project"
PROJECT_DIRECTORY_PATH = os.path.join(os.getcwd(), PROJECT_DIRECTORY_NAME)
