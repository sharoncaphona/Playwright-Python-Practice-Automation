#tests/test_filters.py

from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_filter_a_to_z(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.a_to_z_option)
    items = page.locator('.inventory_item_name')
    expect(items.first).to_have_text('Sauce Labs Backpack')
    expect(items.last).to_have_text('Test.allTheThings() T-Shirt (Red)')

def test_filter_z_to_a(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.z_to_a_option)
    items = page.locator('.inventory_item_name')
    expect(items.first).to_have_text('Test.allTheThings() T-Shirt (Red)')
    expect(items.last).to_have_text('Sauce Labs Backpack')

def test_filter_low_to_high(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.low_to_high_option)
    items_price = page.locator('.inventory_item_price')
    expect(items_price.first).to_have_text('$7.99')
    expect(items_price.last).to_have_text('$49.99')

def test_filter_high_to_low(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.high_to_low_option)
    items_price = page.locator('.inventory_item_price')
    expect(items_price.first).to_have_text('$49.99')
    expect(items_price.last).to_have_text('$7.99')