#tests/test_login.py

from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_valid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login("invalid_user", "invalid_password")
    error = page.locator("h3[data-test='error']")
    expect(error).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_logout(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    login.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")