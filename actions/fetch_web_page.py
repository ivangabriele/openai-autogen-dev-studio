import re
from typing import List
import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def fetch_web_page(url: str) -> str:
    try:
        response = requests.get(url, timeout=60)

        if response.status_code != 200:
            return (
                f"Failed to get content from {url}, status code: {response.status_code}"
            )

        soup = BeautifulSoup(response.text, "html.parser")

        body_tag = soup.body if soup.body else soup
        for tag in body_tag.find_all(True):
            if tag.name != "a":
                if tag.name == "script" or tag.name == "style":
                    tag.extract()
                else:
                    tag.unwrap()
        if soup.html:
            soup.html.unwrap()

        markdown_lines = _extract_content(body_tag)

        markdown_source = " ".join(markdown_lines)
        markdown_source = re.sub(r"\s+", " ", markdown_source)
        markdown_source = re.sub(r"\n{3,}", "\n\n", markdown_source)
        markdown_lines = markdown_source.split("\n")
        clean_markdown_lines = [
            markdown_line.strip() for markdown_line in markdown_lines
        ]
        markdown_source = "\n".join(clean_markdown_lines)

        return markdown_source

    except Exception as e:
        return f"An error occurred: {e}"


def _extract_content(tag: Tag, markdown_lines: List[str] = []) -> List[str]:
    for child in tag.children:
        if isinstance(child, NavigableString):
            if child.strip():  # Only non-empty strings
                parent_tag = child.find_parent("a")
                if parent_tag:
                    href = parent_tag.get("href", "")
                    markdown_lines.append(f"[{child.strip()}]({href})")
                else:
                    markdown_lines.append(child.strip())
        elif isinstance(child, Tag):
            _extract_content(tag=child, markdown_lines=markdown_lines)

    return markdown_lines
