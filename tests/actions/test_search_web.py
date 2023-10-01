import pytest
import actions


def test_search_web():
    results = actions.search_web("new york times")

    assert len(results) == 1
    assert results[0]["link"] == "https://www.nytimes.com/international/"
    assert results[0]["title"] == "Breaking News, US News, World News, Videos"
    assert results[0]["description"].startswith(
        "The New York Times seeks the truth and helps people understand the world."
    )
