import subprocess

from constants import PROJECT_DIRECTORY_PATH


def run_bash_command(command: str) -> str:
    print(f"[DEBUG] Command: `{command}`...")
    result = subprocess.run(
        command,
        cwd=PROJECT_DIRECTORY_PATH,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    output: str
    if result.returncode == 0:
        output = result.stdout.decode("utf-8")
    else:
        output = f"[ERROR] {result.stderr.decode('utf-8')}"

    print(f"[DEBUG] Output: `{command}`...")
    return output
