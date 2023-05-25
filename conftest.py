import pytest
from pytest import fixture, hookimpl
from playwright.sync_api import sync_playwright
from page_objects.login_page import LoginPage
import settings
import credentials
import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page

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
    # allure.attach(Page.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    login_page.close()


@fixture(scope="class")
def new_class():
    print("\nThis is a new class")
    yield


@fixture(scope="session")
def hi_bye():
    print("\nHello Tester~!!!")
    yield
    print("Good Bye YEllow Brick Road")

