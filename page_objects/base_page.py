from playwright.sync_api import Page
from page_objects.client_search import ClientSearch


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.client_search = ClientSearch(self.page)

    def click_adviser_workplace(self):
        self.page.locator(self.Locators.ADVISER_WORKPLACE).click()
        self.page.locator(self.Locators.BASE_SEARCH).click()
        return self

    class Locators:
        ADVISER_WORKPLACE = "a[title = \"Adviser Workplace\"]"
        BASE_SEARCH = "text=Clients By Name"
