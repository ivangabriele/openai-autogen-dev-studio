from dataclasses import asdict
from typing import Any, Dict, Optional

from typedefs import ProjectConfig


def get_model_config_as_dict(
    project_config: ProjectConfig, custom_current_model: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Return the dictionary representation of the selected model configuration."""

    current_model = custom_current_model or project_config.current_model

    model_config = next(
        (
            config_dict
            for config_dict in project_config.models
            if config_dict.model == current_model
        ),
        None,
    )

    return asdict(model_config) if model_config else None
