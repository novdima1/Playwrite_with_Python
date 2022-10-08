from playwright.sync_api import Page, Playwright
from page_objects.client_search import ClientSearch


class BasePage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def click_adviser_workplace(self):
        self.page.locator(BasePage.Locators.ADVISER_WORKPLACE).click()
        self.page.locator(BasePage.Locators.BASE_SEARCH).click()
        return self

    class Locators:
        ADVISER_WORKPLACE = "a[title = \"Adviser Workplace\"]"
        BASE_SEARCH = "text=Clients By Name"
