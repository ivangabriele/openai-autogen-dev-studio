import pytest
from actions import run_bash_command


def test_run_bash_command_success():
    output = run_bash_command("echo hello")

    assert output.strip() == "hello"


def test_run_bash_command_failure():
    output = run_bash_command("nonexistent_command")

    assert "[ERROR]" in output
