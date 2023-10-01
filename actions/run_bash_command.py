import os
import pty

from constants import PROJECT_DIRECTORY_PATH
import utils


def run_bash_command(command: str) -> str:
    utils.debug("Command", command)
    utils.debug("In", PROJECT_DIRECTORY_PATH)

    def reader(fd):
        output = b""
        while True:
            try:
                data = os.read(fd, 1024)
                if not data:
                    break
                output += data
            except OSError:
                break
        return output.decode("utf-8")

    pid, fd = pty.fork()
    if pid == 0:
        os.chdir(PROJECT_DIRECTORY_PATH)
        os.execlp("bash", "bash", "-c", command)
    else:
        output = reader(fd)
        _, ret_code = os.wait()
        if ret_code != 0:
            utils.debug("Error", f"Command failed with return code {ret_code}", True)
            output = f"[ERROR] Command failed with return code {ret_code}\n{output}"

        utils.debug("Output", output, True)
        return output
