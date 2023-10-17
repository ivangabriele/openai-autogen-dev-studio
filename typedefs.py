from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ModelConfig:
    api_base: Optional[str]
    api_key: str
    api_type: Optional[str]
    api_version: Optional[str]
    model: str


@dataclass
class UserAgentConfig:
    current_model: Optional[str]


@dataclass
class ProjectConfig:
    brave_search_api_key: str
    current_model: str
    initial_project_description: Optional[str]
    models: List[ModelConfig]
    user_proxy_agent: UserAgentConfig
