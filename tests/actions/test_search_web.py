import json
import pytest
import requests

import actions
from actions.search_web_types import WebSearchApiResponse
from dacite import from_dict

mock_response_data = (
    {
        "query": {
            "original": "new york times",
            "show_strict_warning": False,
            "is_navigational": True,
            "is_news_breaking": False,
            "spellcheck_off": True,
            "country": "us",
            "bad_results": False,
            "should_fallback": False,
            "postal_code": "",
            "city": "",
            "header_country": "",
            "more_results_available": True,
            "state": "",
        },
        "mixed": {
            "type": "mixed",
            "main": [
                {"type": "web", "index": 0, "all": False},
            ],
            "top": [],
            "side": [],
        },
        "type": "search",
        "web": {
            "type": "search",
            "results": [
                {
                    "title": "The New York Times - Breaking News, US News, World News and Videos",
                    "url": "https://www.nytimes.com",
                    "is_source_local": False,
                    "is_source_both": False,
                    "description": "Live news, investigations, opinion, photos and video by the journalists of The <strong>New</strong> <strong>York</strong> <strong>Times</strong> from more than 150 countries around the world. Subscribe for coverage of U.S. and international news, politics, business, technology, science, health, arts, sports and more.",
                    "profile": {
                        "name": "NYTimes",
                        "url": "https://www.nytimes.com",
                        "long_name": "The New York Times",
                        "img": "https://imgs.search.brave.com/QojRukNhANGMB07cpjolIw83smuIdLYOtKfWBt5_-5s/rs:fit:32:32:1/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvMGFlZWRkYmVh/YWFhZmFjYjM4MWYy/NTQzZmExMTIwN2Nm/NGJmZjgwYTRhYjI5/OTliM2JkYmI2MWY0/M2RlOGFlMi93d3cu/bnl0aW1lcy5jb20v",
                    },
                    "language": "en",
                    "family_friendly": True,
                    "type": "search_result",
                    "subtype": "generic",
                    "meta_url": {
                        "scheme": "https",
                        "netloc": "nytimes.com",
                        "hostname": "www.nytimes.com",
                        "favicon": "https://imgs.search.brave.com/QojRukNhANGMB07cpjolIw83smuIdLYOtKfWBt5_-5s/rs:fit:32:32:1/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvMGFlZWRkYmVh/YWFhZmFjYjM4MWYy/NTQzZmExMTIwN2Nm/NGJmZjgwYTRhYjI5/OTliM2JkYmI2MWY0/M2RlOGFlMi93d3cu/bnl0aW1lcy5jb20v",
                        "path": "",
                    },
                    "thumbnail": {
                        "src": "https://imgs.search.brave.com/fbwq0nGsoN39AQGCpJeyJMKZ6VllcueTX4PTqDWaNbk/rs:fit:200:200:1/g:ce/aHR0cHM6Ly9zdGF0/aWMwMS5ueXQuY29t/L3ZpLWFzc2V0cy9p/bWFnZXMvc2hhcmUv/MTIwMHg2NzVfbmFt/ZXBsYXRlLnBuZw",
                        "original": "https://static01.nyt.com/vi-assets/images/share/1200x675_nameplate.png",
                        "logo": False,
                    },
                    "age": "1 week ago",
                    "extra_snippets": [
                        "The earthquakes on Feb. 8 killed more than 50,000 people in southern Turkey and damaged hundreds of thousands of buildings.Nicole Tung for The New York Times · Many still mourn the loss of family and friends.Nicole Tung for The New York Times",
                        'Across the city, abandoned apartment towers with missing walls line roads.Nicole Tung for The New York Times · “We are living in dust, we are dying in dust"— Mehmet Icer, 48, an unemployed bus driver. His wife cooked dinner over a fire.Nicole Tung for The New York Times',
                        "Construction has officially begun at a number of sites. But during a recent tour of Antakya, the damaged city was still being dismantled.Nicole Tung for The New York Times · The residents who remain live in the shadow of their former homes and face an uncertain future.Nicole Tung for The New York Times",
                        "New York Times CookingRecipes, advice and inspiration for any occasion.",
                    ],
                },
            ],
            "family_friendly": True,
        },
    },
)


def test_successful_search(mocker):
    # Mock the requests.get function
    mocker.patch.object(
        requests,
        "get",
        return_value=mocker.Mock(
            status_code=200,
            text=json.dumps(mock_response_data[0]),
        ),
    )

    result_as_json = actions.search_web("new york times")
    result = json.loads(result_as_json)

    first_result = result["search_results"][0]
    assert first_result["title"].startswith("The New York Times")
    assert first_result["url"] == "https://www.nytimes.com"
    assert first_result["description"].startswith("Live news")
