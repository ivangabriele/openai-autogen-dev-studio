import subprocess

from constants import PROJECT_DIRECTORY_PATH


def run_bash_command(script: str) -> str:
    print(f"[DEBUG] Command: `{script}`...")
    result = subprocess.run(
        script,
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

    print(f"[DEBUG] Output: `{script}`...")
    return output
