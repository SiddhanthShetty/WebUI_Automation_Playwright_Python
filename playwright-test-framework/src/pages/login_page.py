from .base_page import BasePage

class LoginPage(BasePage):
    def goto(self, url):
        self.page.goto(url + "login")

    def login(self, username, password):
        self.page.fill('input[name="username"]', username)
        self.page.fill('input[name="password"]', password)
        self.page.click('button[type="submit"]')

    def get_flash_message(self):
        return self.page.inner_text("#flash")
