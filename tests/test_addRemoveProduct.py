from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_add_product(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    cart_badge = page.locator(home.product_cart)
    page.click(home.add_to_cart_button.format("sauce-labs-backpack"))
    expect(cart_badge).to_have_text('1')
    page.click(home.add_to_cart_button.format("sauce-labs-bike-light"))
    expect(cart_badge).to_have_text('2')
    page.click(home.add_to_cart_button.format("sauce-labs-bolt-t-shirt"))
    expect(cart_badge).to_have_text('3')
    page.click(home.add_to_cart_button.format("sauce-labs-fleece-jacket"))
    expect(cart_badge).to_have_text('4')
    page.click(home.add_to_cart_button.format("sauce-labs-onesie"))
    expect(cart_badge).to_have_text('5')
    page.click(home.add_to_cart_button.format("test.allthethings()-t-shirt-(red)"))
    expect(cart_badge).to_have_text('6')

def test_remove_product(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    
    #Call the add product test to ensure products are in the cart before removing
    test_add_product(page)

    cart_badge = page.locator(home.product_cart)
    page.click(home.remove_from_cart_button.format("sauce-labs-backpack"))
    expect(cart_badge).to_have_text('5')
    page.click(home.remove_from_cart_button.format("sauce-labs-bike-light"))
    expect(cart_badge).to_have_text('4')
    page.click(home.remove_from_cart_button.format("sauce-labs-bolt-t-shirt"))
    expect(cart_badge).to_have_text('3')
    page.click(home.remove_from_cart_button.format("sauce-labs-fleece-jacket"))
    expect(cart_badge).to_have_text('2')
    page.click(home.remove_from_cart_button.format("sauce-labs-onesie"))
    expect(cart_badge).to_have_text('1')
    page.click(home.remove_from_cart_button.format("test.allthethings()-t-shirt-(red)"))
    expect(cart_badge).to_have_text('')