from framework.browser_factory import BrowserFactory
from framework.login_page import LoginPage

def test_valid_login():
    browser = BrowserFactory().get_browser()
    page = browser.new_page()

    login = LoginPage(page)
    login.login("demoUser", "demoPass")

    assert page.url == "https://example.com/dashboard"
    browser.close()