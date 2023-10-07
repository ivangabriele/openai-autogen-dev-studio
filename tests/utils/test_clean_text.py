import utils


def test_clean_text():
    assert (
        utils.clean_text(
            """
            A todo list:
            - Do this.
            - And do that.
            """
        )
        == "A todo list:\n- Do this.\n- And do that."
    )

    assert utils.clean_text("  Hello   World  ") == "Hello World"

    assert utils.clean_text("Hello") == "Hello"

    assert utils.clean_text("") == ""

    assert utils.clean_text("   ") == ""
