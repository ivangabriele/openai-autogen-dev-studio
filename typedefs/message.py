from typing import Any, Optional, TypedDict


class BaseMessageDict(TypedDict):
    content: str
    function_call: Optional[Any]
    role: str


class MessageDict(BaseMessageDict):
    name: str
