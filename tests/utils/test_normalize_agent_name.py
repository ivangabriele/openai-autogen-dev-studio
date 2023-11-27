import utils


def test_normalize_agent_name():
    assert utils.normalize_agent_name("Hello World") == "Hello_World"
    assert (
        utils.normalize_agent_name("OpenAI Autogen Dev Studio")
        == "OpenAI_Autogen_Dev_Studio"
    )
    assert utils.normalize_agent_name("") == ""
    assert utils.normalize_agent_name("No Spaces Here") == "No_Spaces_Here"
