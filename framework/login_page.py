from framework.base_page import BasePage

class LoginPage(BasePage):

    def login(self, username, password):
        self.page.goto("https://example.com/login")
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("#loginBtn")
