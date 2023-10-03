from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Literal, Optional


# https://api.search.brave.com/app/documentation/web-search/responses#MetaUrl
@dataclass
class MetaUrl:
    scheme: str
    netloc: str
    hostname: str
    favicon: str
    path: str


# https://api.search.brave.com/app/documentation/web-search/responses#Profile
@dataclass
class Profile:
    name: str
    long_name: str
    url: str
    img: str


# https://api.search.brave.com/app/documentation/web-search/responses#Query
@dataclass
class Query:
    original: str
    show_strict_warning: bool
    altered: Optional[str]
    safesearch: Optional[bool]
    is_navigational: bool
    is_geolocal: Optional[bool]
    local_decision: Optional[str]
    local_locations_idx: Optional[int]
    is_trending: Optional[bool]
    is_news_breaking: bool
    ask_for_location: Optional[bool]
    language: Optional[str]
    spellcheck_off: bool
    country: str
    bad_results: bool
    should_fallback: bool
    lat: Optional[str]
    long: Optional[str]
    postal_code: str
    city: str
    state: str
    header_country: str
    more_results_available: bool
    custom_location_label: Optional[str]
    reddit_cluster: Optional[str]


# https://api.search.brave.com/app/documentation/web-search/responses#ResultReference
@dataclass
class ResultReference:
    type: str
    index: int
    all: bool


# https://api.search.brave.com/app/documentation/web-search/responses#MixedResponse
@dataclass
class MixedResponse:
    type: Literal["mixed"]
    main: List[ResultReference]
    top: List[ResultReference]
    side: List[ResultReference]


@dataclass
class Result:
    title: str
    url: str
    is_source_local: bool
    is_source_both: bool
    description: str
    page_age: Optional[str]
    page_fetched: Optional[str]
    profile: Profile
    language: str
    family_friendly: bool


# TODO Check if there are other subtypes.
class SearchResultSubtype(Enum):
    CREATIVE_WORK = "creative_work"
    GENERIC = "generic"


# https://api.search.brave.com/app/documentation/web-search/responses#SearchResult
@dataclass
class SearchResult(Result):
    type: Literal["search_result"]
    # subtype: SearchResultSubtype
    subtype: str
    meta_url: MetaUrl
    deep_results: Optional[Any]
    schemas: Optional[List[List[Any]]]
    thumbnail: Optional[Any]
    age: Optional[str]
    language: str
    restaurant: Optional[Any]
    locations: Optional[Any]
    video: Optional[Any]
    movie: Optional[Any]
    faq: Optional[Any]
    qa: Optional[Any]
    book: Optional[Any]
    rating: Optional[Any]
    article: Optional[Any]
    product: Optional[Any]
    product_cluster: Optional[List[Any]]
    cluster_type: Optional[str]
    cluster: Optional[List[Any]]
    creative_work: Optional[Any]
    music_recording: Optional[Any]
    review: Optional[Any]
    software: Optional[Any]
    content_type: Optional[str]
    # TODO Check that Data for AI is enabled.
    extra_snippets: Optional[List[str]]


# https://api.search.brave.com/app/documentation/web-search/responses#Search
@dataclass
class Search:
    type: Literal["search"]
    results: List[SearchResult]
    family_friendly: bool


# https://api.search.brave.com/app/documentation/web-search/responses#WebSearchApiResponse
@dataclass
class WebSearchApiResponse:
    type: Literal["search"]
    discussions: Optional[Any]
    faq: Optional[Any]
    infobox: Optional[Any]
    locations: Optional[Any]
    mixed: MixedResponse
    news: Optional[Any]
    query: Query
    videos: Optional[Any]
    web: Search
