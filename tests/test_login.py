#tests/test_login.py

from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
