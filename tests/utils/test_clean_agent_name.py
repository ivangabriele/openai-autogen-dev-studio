import utils


def test_clean_agent_name():
    assert utils.clean_agent_name("Hello_World") == "Hello World"
    assert (
        utils.clean_agent_name("OpenAI_Autogen_Dev_Studio")
        == "OpenAI Autogen Dev Studio"
    )
    assert utils.clean_agent_name("") == ""
    assert utils.clean_agent_name("No_Underscores_Here") == "No Underscores Here"
