import utils


def ensure_str(value) -> str:
    if not isinstance(value, str):
        error_message = (
            f"Expected value to be of type `str`, got `{type(value).__name__}`."
        )

        utils.debug("Error", error_message)

        raise TypeError(error_message)

    return value
