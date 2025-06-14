import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from pages.login_page import LoginPage
from config.config import BASE_URL

def test_login_success(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login.get_flash_message()

def test_login_failure(page):
    login = LoginPage(page)
    login.goto(BASE_URL)
    login.login("invalid", "invalid")
    assert "Your username is invalid!" in login.get_flash_message()
