import json
import pytest

import actions

# from unittest.mock import Mock


def test_successful_search():
    result_as_json = actions.search_web("new york times")
    result = json.loads(result_as_json)

    first_result = result["search_results"][0]
    assert first_result["title"].startswith("The New York Times")
    assert first_result["url"] == "https://www.nytimes.com"
    assert first_result["description"].startswith("Live news")


# def test_network_exception(mocker):
#     mocker.patch("requests.get", side_effect=Exception("Network error"))

#     with pytest.raises(Exception):
#         result = search_web("sample query")
