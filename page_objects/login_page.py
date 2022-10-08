from playwright.sync_api import Playwright, expect
from playwright.sync_api import Page
import settings


class LoginPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        # self.base_url = base_url
        self.base_page = BasePage(self.page)

    def login(self, base_url, login, password):
        self.page.goto(base_url)
        self.page.locator("text=intelliflo office login east").click()
        self.page.locator("input[name=\"Username\"]").fill(login)
        self.page.locator("input[name=\"Password\"]").fill(password)
        self.page.locator("button[title = \"Login\"]").click()
        try:
            self.page.locator("text=Remind me in a week").click(timeout=300)
            self.page.wait_for_url(base_url + "nio/dashboard/userdashboard")
            return self
        finally:
            return self

    def verify_login_failed(self):
        self.validate_error()
        self.validate_user_name_field_is_contain_username()
        self.close()

    def validate_error(self):
        content = self.page.locator("strong").text_content()
        assert content == 'Error:', f"'\n'Expected: Error:, '\n'Actual: {content}"
        return self

    def validate_user_name_field_is_contain_username(self):
        content = self.page.locator("#username").input_value()
        expected = settings.USER_CREDENTIALS["fake"][0]
        assert content == expected, f"'\n'Expected: {expected}, '\n'Actual: {content}"
        self.page.wait_for_url("https://identity.sys-ie-07.intelliflo.systems/core/identity/account/login")
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

    def verify_page(self, url):
        assert self.page.url == url
        return self


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.client_search = ClientSearch(self.page)

    def click_adviser_workplace(self):
        self.page.locator("a[title = \"Adviser Workplace\"]").click()
        self.page.locator("text=Clients By Name").click()
        self.page.wait_for_timeout(3000)
        return self


class ClientSearch:
    def __init__(self, page: Page):
        self.page = page

    def verify_client_by_name_button_contains_valid_name(self):
        content = self.page.locator("text=Clients By Name").text_content()
        assert content == 'Clients By Name', 'No such element'
        return self

    def verify_client_by_name_button_is_present(self):
        element = self.page.locator("a[ui_test_id=\"nav-link10\"]").is_visible()
        if element:
            return self
        else:
            raise Exception('No such element')
