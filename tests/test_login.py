#tests/test_login.py

import json
from pages.login_page import LoginPage
from playwright.sync_api import expect

with open("utils/data.json") as f:
    users = json.load(f)

def test_valid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login(users["valid_user"]["username"], users["valid_user"]["password"])
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page):
    login = LoginPage(page)
    login.open() 
    login.login(users["invalid_user"]["username"], users["invalid_user"]["password"])
    error = page.locator("h3[data-test='error']")
    expect(error).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_logout(page):
    login = LoginPage(page)
    login.open() 
    login.login(users["valid_user"]["username"], users["valid_user"]["password"])
    login.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")