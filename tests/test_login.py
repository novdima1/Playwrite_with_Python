import pytest

from page_objects.login_page import LoginPage
import settings


@pytest.mark.login
def test_io_login_pass(get_playwright):
    base_url = settings.ENVIRONMENTS["SYS_07"]
    login = settings.USER_CREDENTIALS["SYS_07"][0]
    password = settings.USER_CREDENTIALS["SYS_07"][1]
    page = LoginPage(get_playwright).login(base_url, login, password).\
        base_page.click_adviser_workplace().\
        client_search.verify_client_by_name_button_contains_valid_name(). \
        verify_client_by_name_button_is_present().\
        verify_client_by_name_button_contains_valid_name(). \
        verify_client_by_name_button_is_present()


@pytest.mark.login
def test_io_login_fail(get_playwright):
    base_url = settings.ENVIRONMENTS["fake"]
    login = settings.USER_CREDENTIALS["fake"][0]
    password = settings.USER_CREDENTIALS["fake"][1]
    page = LoginPage(get_playwright).login(base_url, login, password).\
        verify_login_failed()
