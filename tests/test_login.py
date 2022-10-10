import pytest
from page_objects.login_page import LoginPage
import settings
import credentials


local_variables = {
    "url": settings.ENVIRONMENTS["SYS_07"],
    "wrong_login": credentials.USER_CREDENTIALS["fake"][0],
    "wrong_password": credentials.USER_CREDENTIALS["fake"][1]
}


@pytest.mark.login
def test_io_login_pass(login):
    page = login.\
        click_adviser_workplace().\
        verify_page(local_variables["url"]).\
        client_search.verify_client_by_name_button_contains_valid_name().\
        verify_client_by_name_button_is_present().\
        verify_client_by_name_button_contains_valid_name().\
        verify_client_by_name_button_is_present()


@pytest.mark.login
def test_io_login_fail(get_playwright):
    page = LoginPage(get_playwright).login(local_variables["url"],
                                           local_variables["wrong_login"],
                                           local_variables["wrong_password"]).\
        verify_login_failed()

