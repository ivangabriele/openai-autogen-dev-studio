from autogen import config_list_from_json
from jsonc_parser.parser import JsoncParser
import os
from typedefs import ProjectConfig

import utils


PROJECT_CONFIG: ProjectConfig = JsoncParser.parse_file("./env.jsonc")

COMMON_LLM_CONFIG = {
    # https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    "config_list": [utils.get_model_config_as_dict(PROJECT_CONFIG)],
    "functions": [
        {
            "name": "fetch_web_page",
            "description": "Fetch a web page and return its content as text and Markdown links.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "Url to fetch from.",
                    },
                },
                "required": ["url"],
            },
        },
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
            "name": "search_web",
            "description": "Search for a text query using Brave search engine and return results as JSON.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Query to search.",
                    },
                },
                "required": ["query"],
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
