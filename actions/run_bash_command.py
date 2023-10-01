import subprocess

from constants import PROJECT_DIRECTORY_PATH
import utils


def run_bash_command(command: str) -> str:
    utils.debug("Command", command)
    utils.debug("In", PROJECT_DIRECTORY_PATH)
    result = subprocess.run(
        command,
        cwd=PROJECT_DIRECTORY_PATH,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    output: str
    if result.returncode == 0:
        output = f"{result.stdout.decode('utf-8')}{result.stderr.decode('utf-8')}"
    else:
        output = f"[ERROR] {result.stderr.decode('utf-8')}"

    utils.debug("Output", output, True)
    return output
