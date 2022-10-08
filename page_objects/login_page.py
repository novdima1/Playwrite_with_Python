from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page
import settings


class LoginPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_page = BasePage(self.page)

    def login(self, base_url, login, password):
        self.page.goto(base_url)
        self.page.locator(self.Locators.REDIRECT).click()
        self.page.locator(self.Locators.USER_NAME).fill(login)
        self.page.locator(self.Locators.PASSWORD).fill(password)
        self.page.locator(self.Locators.LOGIN).click()
        try:
            self.page.locator(self.Locators.REMIND).click(timeout=300)
            return self
        finally:
            return self

    def verify_login_failed(self):
        self.validate_error()
        self.validate_user_name_field_is_contain_username()
        self.close()

    def validate_error(self):
        content = self.page.locator(self.Locators.STRONG).text_content()
        assert content == 'Error:', f"'\n'Expected: Error:, '\n'Actual: {content}"
        return self

    def validate_user_name_field_is_contain_username(self):
        content = self.page.locator(self.Locators.USER_NAME).input_value()
        expected = settings.USER_CREDENTIALS["fake"][0]
        assert content == expected, f"'\n'Expected: {expected}, '\n'Actual: {content}"
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def verify_page(self, url):
        assert self.page.url == url
        return self

    class Locators:
        LOGIN = "button[title = \"Login\"]"
        LOGOUT = "text=Logout"
        USER_NAME = "#username"
        PASSWORD = "#password"
        TITLE = 'h1'
        REMIND = "text = Remind me in a week"
        REDIRECT = "text = intelliflo office login east"
        STRONG = "strong"


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
