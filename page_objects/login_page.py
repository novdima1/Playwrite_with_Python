from playwright.sync_api import Playwright, expect
# from page_objects.base_page import BasePage
import credentials
from playwright.sync_api import Page
from page_objects.base_page import BasePage
from page_objects.client_search import ClientSearch


class LoginPage(BasePage):
    def __init__(self, playwright: Playwright):
        super().__init__(playwright)
        self.client_search = ClientSearch(self.page)

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
        actual = self.page.locator(self.Locators.USER_NAME).input_value()
        expected = credentials.USER_CREDENTIALS["fake"][0]
        assert actual == expected, f"'\n'Expected: {expected}, '\n'Actual: {actual}"
        return self

    def verify_page(self, url):
        actual = url
        expected = self.page.url
        assert expected[:len(url)] == actual, f"'\n'Expected: {expected}, '\n'Actual: {actual}"
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    class Locators:
        LOGIN = "button[title = \"Login\"]"
        LOGOUT = "text=Logout"
        USER_NAME = "#username"
        PASSWORD = "#password"
        TITLE = 'h1'
        REMIND = "text = Remind me in a week"
        REDIRECT = "text = intelliflo office login east"
        STRONG = "strong"
