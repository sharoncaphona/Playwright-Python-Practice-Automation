#tests/test_filters.py

from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_filter_a_to_z(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.a_to_z_option)
    assert page.locator('.inventory_item_name').first.text_content() == 'Sauce Labs Backpack'
    assert page.locator('.inventory_item_name').last.text_content() == 'Test.allTheThings() T-Shirt (Red)'

def test_filter_z_to_a(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.z_to_a_option)
    assert page.locator('.inventory_item_name').first.text_content() == 'Test.allTheThings() T-Shirt (Red)'
    assert page.locator('.inventory_item_name').last.text_content() == 'Sauce Labs Backpack'

def test_filter_low_to_high(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.low_to_high_option)
    assert page.locator('.inventory_item_price').first.text_content() == '$7.99'
    assert page.locator('.inventory_item_price').last.text_content() == '$49.99'

def test_filter_high_to_low(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.select_option(home.filter, home.high_to_low_option)
    assert page.locator('.inventory_item_price').first.text_content() == '$49.99'
    assert page.locator('.inventory_item_price').last.text_content() == '$7.99'