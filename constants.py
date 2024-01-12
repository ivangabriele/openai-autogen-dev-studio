import os
import time
from typing import Dict
from dataclasses import asdict
from dacite import from_dict
from jsonc_parser.parser import JsoncParser

from typedefs import ProjectConfig
from utils.get_model_config_as_dict import get_model_config_as_dict

PROJECT_CONFIG_AS_DICT = JsoncParser.parse_file("./env.jsonc")
PROJECT_CONFIG: ProjectConfig = from_dict(
    data_class=ProjectConfig, data=PROJECT_CONFIG_AS_DICT
)

DEFAULT_REQUEST_TIMEOUT = 60
IS_OPEN_SOURCE_LLM = PROJECT_CONFIG.functionary_model is None
PROJECT_DIRECTORY_NAME = "project"
PROJECT_DIRECTORY_PATH = os.path.join(os.getcwd(), PROJECT_DIRECTORY_NAME)

COMMON_LLM_CONFIG = {
    # https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    "config_list": [get_model_config_as_dict(PROJECT_CONFIG)],
    "request_timeout": 600,
    "seed": int(time.time()),
}

FUNCTIONS = [
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
]


FUNCTIONEER_LLM_CONFIG: Dict = COMMON_LLM_CONFIG | {
    "config_list": [
        COMMON_LLM_CONFIG
        if PROJECT_CONFIG.functionary_model is None
        else asdict(PROJECT_CONFIG.functionary_model)
    ],
    "functions": FUNCTIONS,
}
