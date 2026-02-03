from playwright.sync_api import sync_playwright

class BrowserFactory:
    def get_browser(self):
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        return browser
