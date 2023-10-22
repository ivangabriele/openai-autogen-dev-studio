import utils


def test_get_command_from_message():
    # Test with a valid command and parameters
    message1 = "SEARCH weather in Paris"
    assert utils.get_command_from_message(message1) == (
        "SEARCH",
        ["weather in Paris"],
    )

    # Test with a valid command and no parameters
    message2 = "TERMINATE"
    assert utils.get_command_from_message(message2) == (
        "TERMINATE",
        [],
    )

    # Test with a message containing no command
    message4 = "Some random message without a command"
    assert utils.get_command_from_message(message4) is None

    # Test with a message containing command but not at the start
    message5 = "Message with SEARCH command in the middle"
    assert utils.get_command_from_message(message5) is None

    # Test with a message containing only the command and no other text
    message7 = "OPEN"
    assert utils.get_command_from_message(message7) == (
        "OPEN",
        [],
    )

    # Test with a message containing command followed by parameters, but with extra whitespace
    message8 = "  READ  dir/file_path.txt  "
    assert utils.get_command_from_message(message8) == (
        "READ",
        ["dir/file_path.txt"],
    )
