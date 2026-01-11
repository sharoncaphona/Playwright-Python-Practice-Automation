#pages/login_page.py

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.logout_button = "#logout_sidebar_link"
    
    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self,username, password):
        self.page.fill(self.username, username)
        self.page.fill(self.password, password)
        self.page.click(self.login_button)

    def logout(self):
        self.page.click("#react-burger-menu-btn")
        self.page.click(self.logout_button)
