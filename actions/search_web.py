from typing import Union
from dacite import from_dict
import json
import requests

from actions.search_web_types import WebSearchApiResponse

from constants import PROJECT_CONFIG


def search_web(query: str) -> str:
    brave_search_api_result_or_error = _fetch_brave_search_api(query)

    # If it's an `str`, that means it's an error
    if isinstance(brave_search_api_result_or_error, str):
        return brave_search_api_result_or_error
    else:
        brave_search_api_result = brave_search_api_result_or_error

    # Simplify the data
    simplified_response_data = {
        "search_results": [
            {
                "title": result.title,
                "description": result.description,
                "url": result.url,
            }
            for result in brave_search_api_result.web.results
        ]
    }

    return json.dumps(simplified_response_data)


def _fetch_brave_search_api(query: str) -> Union[WebSearchApiResponse, str]:
    endpoint = "https://api.search.brave.com/res/v1/web/search"

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": PROJECT_CONFIG.brave_search_api_key,
    }

    # Commentted values represent the default value
    # https://api.search.brave.com/app/documentation/web-search/query
    params = {
        "q": query,
        # "country": "US",
        # "search_lang": "en",
        # "ui_lang": "en_US",
        # "count": 20,
        # The zero based offset that indicates number of search results per page (count)
        # to skip before returning the result.
        # The default is 0 and the maximum is 9.
        # "offset": 0,
        "safesearch": "moderate",
        # "freshness": None,
        # "text_decorations": "true",
        "result_filter": "web",
        # "goggles_id": None,
        "units": "metric",
        "extra_snippets": "true",
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.reason}"

    response_dict = json.loads(response.text)
    response_data = from_dict(data_class=WebSearchApiResponse, data=response_dict)

    return response_data
