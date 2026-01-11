#tests/test_login.py

from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("invalid_user", "invalid_password")
    error_message = page.text_content("h3[data-test='error']")
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

def test_logout(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    login.logout()
    assert page.url == "https://www.saucedemo.com/"