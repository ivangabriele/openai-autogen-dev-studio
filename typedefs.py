from typing import List, Optional, TypedDict


class ModelConfig(TypedDict):
    model: str
    api_key: str
    api_base: Optional[str]
    api_type: Optional[str]
    api_version: Optional[str]


class ProjectConfig(TypedDict):
    brave_search_api_key: str
    current_model: str
    initial_project_description: Optional[str]
    models: List[ModelConfig]
