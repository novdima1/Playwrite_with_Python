from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.login_page import LoginPage
import settings
import credentials

local_variables = {
    "url": settings.ENVIRONMENTS["SYS_07"],
    "login": credentials.USER_CREDENTIALS["SYS_07"][0],
    "password": credentials.USER_CREDENTIALS["SYS_07"][1]
}


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def login(get_playwright):
    login_page = LoginPage(get_playwright).login(local_variables["url"],
                                                 local_variables["login"],
                                                 local_variables["password"])
    yield login_page


