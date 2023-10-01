from typing import Dict, Optional

from typedefs import ModelConfig, ProjectConfig


def get_model_config_as_dict(project_config: ProjectConfig) -> Optional[ModelConfig]:
    """Return the dictionary representation of the selected model configuration."""

    return next(
        (
            config_dict
            for config_dict in project_config["models"]
            if config_dict["model"] == project_config["current_model"]
        ),
        None,
    )
