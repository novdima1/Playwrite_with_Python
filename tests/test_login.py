import pytest
from page_objects.login_page import LoginPage
import settings
import credentials


@pytest.mark.login
def test_io_login_pass(get_playwright):
    page = LoginPage(get_playwright).login(local_variables["url"],
                                           local_variables["login"],
                                           local_variables["password"]).\
        click_adviser_workplace().\
        verify_page(local_variables["url"]).\
        client_search.verify_client_by_name_button_contains_valid_name().\
        verify_client_by_name_button_is_present().\
        verify_client_by_name_button_contains_valid_name().\
        verify_client_by_name_button_is_present()


@pytest.mark.login
def test_io_login_fail(get_playwright):
    base_url = settings.ENVIRONMENTS["SYS_07"]
    login = credentials.USER_CREDENTIALS["fake"][0]
    password = credentials.USER_CREDENTIALS["fake"][1]
    page = LoginPage(get_playwright).login(local_variables["url"],
                                           local_variables["wrong_login"],
                                           local_variables["wrong_password"]).\
        verify_login_failed()


local_variables = {
    "url": settings.ENVIRONMENTS["SYS_07"],
    "login": credentials.USER_CREDENTIALS["SYS_07"][0],
    "password": credentials.USER_CREDENTIALS["SYS_07"][1],
    "wrong_login": credentials.USER_CREDENTIALS["fake"][0],
    "wrong_password": credentials.USER_CREDENTIALS["fake"][1]
}
