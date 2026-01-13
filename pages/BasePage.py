#pages/BasePage.py

class BasePage:
    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()
    
    def get_current_url(self):
        return self.page.url