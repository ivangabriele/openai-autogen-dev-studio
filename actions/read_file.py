import os

from constants import PROJECT_DIRECTORY_PATH


def read_file(relative_path: str) -> str:
    """
    Read content from a file and return it.
    """
    full_path = os.path.join(PROJECT_DIRECTORY_PATH, relative_path)
    with open(full_path, "r") as file:
        return file.read()
