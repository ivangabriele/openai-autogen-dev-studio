from dataclasses import asdict
from typing import Any, Dict, Optional

from typedefs import ProjectConfig


def get_model_config_as_dict(project_config: ProjectConfig) -> Optional[Dict[str, Any]]:
    """Return the dictionary representation of the selected model configuration."""

    model_config = next(
        (
            config_dict
            for config_dict in project_config.models
            if config_dict.model == project_config.current_model
        ),
        None,
    )

    return asdict(model_config) if model_config else None
