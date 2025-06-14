from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="module")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_example(page):
    page.goto("https://google.com")
    print("Page Title: "+page.title())
    page.screenshot(path="./screenshot/demo.png")
    assert "Google" in page.title()
