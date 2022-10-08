from pytest import fixture
from playwright.sync_api import sync_playwright


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright






