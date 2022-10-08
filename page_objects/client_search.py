from playwright.sync_api import Page


class ClientSearch:
    def __init__(self, page: Page):
        self.page = page

    def verify_client_by_name_button_contains_valid_name(self):
        content = self.page.locator(self.Locators.BASE_SEARCH).text_content()
        assert content == 'Clients By Name', 'No such element'
        return self

    def verify_client_by_name_button_is_present(self):
        element = self.page.locator(self.Locators.BASE_SEARCH).is_visible()
        if element:
            return self
        else:
            raise Exception('No such element')

    class Locators:
        BASE_SEARCH = "text=Clients By Name"
