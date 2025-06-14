import pytest
from playwright.sync_api import sync_playwright
from ..config.config import BROWSER, HEADLESS
from ..utils.logger import get_logger
from ..utils.helpers import take_screenshot

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = getattr(playwright_instance, BROWSER).launch(headless=HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

# Pytest hook to take screenshot on failure and attach to report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_name = f"{item.name}.png"
            take_screenshot(page, screenshot_name)
            if hasattr(item.config, '_html'):  # pytest-html
                extra = getattr(rep, 'extra', [])
                extra.append(item.config._html.extras.image(f"../reports/{screenshot_name}"))
                rep.extra = extra
