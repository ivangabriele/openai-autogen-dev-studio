import actions


def test_fetch_web_page_success():
    web_page_text = actions.fetch_web_page("https://example.org")

    print(web_page_text)

    assert web_page_text.startswith("Example Domain")
    assert web_page_text.endswith(
        "[More information...](https://www.iana.org/domains/example)"
    )
