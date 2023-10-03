import dataclasses
from typing import SupportsIndex
from termcolor import colored
from typedefs import ProjectConfig
import utils


def print_project_config(project_config: ProjectConfig):
    project_config_as_dict = dataclasses.asdict(project_config)

    print()
    _print_separator()
    print(colored("OADS Configuration", "yellow"))
    print()

    current_model = project_config_as_dict["current_model"]

    for key, value in project_config_as_dict.items():
        if key == "models" and isinstance(value, list):
            print("models:")
            for model_config in value:
                is_selected = model_config["model"] == current_model
                _print_model_config(model_config, is_selected)
        else:
            _print_key_value(key, str(value))

    _print_separator()
    print()


def _pad_key(key: str, length: SupportsIndex) -> str:
    return f"{key}:".ljust(length, " ")


def _print_model_config(model_config: dict, is_selected: bool):
    color = "yellow" if is_selected else "dark_grey"
    attrs = [] if is_selected else ["dark"]

    for model_key, model_value in model_config.items():
        formatted_value = (
            utils.mask_secret(model_value) if model_key in ["api_key"] else model_value
        )
        print(
            colored(
                f"\t{_pad_key(model_key, 24)} {formatted_value}", color, attrs=attrs
            )
        )

    print()


def _print_key_value(key: str, value: str):
    if key == "brave_search_api_key":
        print(f"{_pad_key(key, 32)} {utils.mask_secret(value)}")
    else:
        print(f"{_pad_key(key, 32)} {value}")


def _print_separator():
    print(colored("-" * 80, "yellow"))
