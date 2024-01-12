import os


PROJECT_DIRECTORY_NAME = "project"
PROJECT_DIRECTORY_PATH = os.path.join(os.getcwd(), PROJECT_DIRECTORY_NAME)


def read_file(relative_path: str) -> str:
    """
    Read content from a file and return it.
    """

    full_path = os.path.join(PROJECT_DIRECTORY_PATH, relative_path)

    with open(file=full_path, mode="r", encoding="utf-8") as file:
        return file.read()
