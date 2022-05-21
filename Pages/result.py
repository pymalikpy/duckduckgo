from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    RESULT_LINKS = (By.TAG_NAME, 'a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # initializer
    def __init__(self, browser):
        self.browser = browser

    # interactions

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        for link in links:
            print(link.text)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
