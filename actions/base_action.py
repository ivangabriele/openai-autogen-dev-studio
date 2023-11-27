from typing import Any, Dict, List, TypedDict


class ActionDesciptionParametersDict(TypedDict):
    type: "object"
    properties: Dict[str, Any]
    required: List[str]


class ActionDesciptionDict(TypedDict):
    name: str
    description: str
    parameters: ActionDesciptionParametersDict


class BaseAction:
    _description: ActionDesciptionDict

    @classmethod
    def get_description(cls):
        return cls._description

    @staticmethod
    def run(*args, **kwargs):
        pass
