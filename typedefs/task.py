from typing import TypedDict


class TaskDict(TypedDict):
    index: int
    description: str
    is_done: bool
