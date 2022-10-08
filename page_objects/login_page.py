from playwright.sync_api import Playwright, expect
from page_objects.base_page import BasePage
import credentials


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
        expected = credentials.USER_CREDENTIALS["fake"][0]
        assert content == expected, f"'\n'Expected: {expected}, '\n'Actual: {content}"
        return self

    def verify_page(self, url):
        assert self.page.url == url
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
