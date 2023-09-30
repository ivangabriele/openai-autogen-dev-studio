import subprocess


def run_bash_command(script: str) -> str:
    print(f"[DEBUG] Command: `{script}`...")
    result = subprocess.run(
        script,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )

    output: str
    if result.returncode == 0:
        output = result.stdout.decode("utf-8")
    else:
        output = f"[ERROR] {result.stderr.decode('utf-8')}"

    print(f"[DEBUG] Output: `{script}`...")
    return output
