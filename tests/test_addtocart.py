#tests/test_addtocart.py

from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_add_to_cart(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    cart_badge = page.locator(home.product_cart)
    page.click(home.add_to_cart_button.format("sauce-labs-backpack"))
    expect(cart_badge).to_have_text('1')
    page.click(home.add_to_cart_button.format("sauce-labs-bike-light"))
    expect(cart_badge).to_have_text('2')
    
    page.click(home.shopping_cart)
    # cart_items = page.locator('.cart_item')
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")