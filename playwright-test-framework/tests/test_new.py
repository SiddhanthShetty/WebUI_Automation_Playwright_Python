import pytest
from playwright.sync_api import sync_playwright

def test_new_example():
    print("Hello, World!")

def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        # Enter username and password
        page.fill('input[name="username"]', 'tomsmith')
        page.fill('input[name="password"]', 'SuperSecretPassword!')
        # Click the login button
        page.click('button[type="submit"]')
        # Assert a successful login message (more robust check)
        flash_text = page.locator('#flash').inner_text()
        assert 'You logged into a secure area!' in flash_text
        browser.close()
