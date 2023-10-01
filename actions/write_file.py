import os

from constants import PROJECT_DIRECTORY_PATH


def write_file(relative_path: str, file_source: str) -> str:
    """
    Write content to a file. Create the file and/or directories if they don't exist.
    """
    full_path = os.path.join(PROJECT_DIRECTORY_PATH, relative_path)

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as file:
            file.write(file_source)

        return f"Done."
    except Exception as e:
        return f"Error: {str(e)}"
