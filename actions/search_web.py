import requests
from typing import Dict

from constants import PROJECT_CONFIG


def search_web(query: str) -> Dict:
    endpoint = "https://api.search.brave.com/res/v1/web/search"

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": PROJECT_CONFIG["brave_search_api_key"],
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
    return response.json()
