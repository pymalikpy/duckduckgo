from Pages.search import DuckDuckGoSearchPage
from Pages.result import DuckDuckGoResultPage


def test_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "TEST Automation With AI"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "TEST Automation With AI"
    search_page.search(PHRASE)

    # Then the search result title contains "TEST Automation With AI"
    assert PHRASE in result_page.title()

    # And the search result query is "TEST Automation With AI"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "TEST Automation With AI"
    # for title in result_page.result_link_titles():
    #     assert PHRASE.lower() in titles.lower()

    # # TODO: Remove this exception once the test is complete
    # raise Exception("Incomplete Test")
