#pages/login_page.py

from pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.logout_button = "#logout_sidebar_link"
    
    def open(self):
        self.open_url("https://www.saucedemo.com/")

    def login(self,username, password):
        self.fill(self.username, username)
        self.fill(self.password, password)
        self.click(self.login_button)

    def logout(self):
        self.click("#react-burger-menu-btn")
        self.click(self.logout_button)
