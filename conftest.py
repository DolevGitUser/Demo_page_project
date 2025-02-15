import pytest
from playwright.sync_api import sync_playwright
from pages.demo_page import DemoMainPage


@pytest.fixture(scope="session")
def browser():
    """Fixture to launch and close the browser"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def demo_main_page(browser ):
    """Fixture to create a new DemoMainPage object with an open page"""
    context = browser.new_context()
    page = context.new_page()
    demo_page = DemoMainPage(page)
    yield demo_page
    context.close()