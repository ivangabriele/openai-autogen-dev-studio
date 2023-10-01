import io
import sys
from typing import Any
from termcolor import colored


def debug(subject: str, output: Any, is_multine: bool = False):
    output_as_str = _capture_print_output(output)
    if is_multine:
        left_padded_output_as_str = "\n".join(
            ["    " + line for line in output_as_str.split("\n")]
        )

        print(colored(f"[DEBUG] {subject}:", "cyan"))
        print(colored(left_padded_output_as_str, "dark_grey"))
    else:
        print(colored(f"[DEBUG] {subject}: `{output_as_str}`", "cyan"))


def _capture_print_output(output: Any) -> str:
    captured_output = io.StringIO()
    sys.stdout = captured_output
    print(output)
    sys.stdout = sys.__stdout__
    print_output = captured_output.getvalue()

    return print_output.strip()
