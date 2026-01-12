from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_add_product(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    page.click(home.add_to_cart_button.format("sauce-labs-backpack"))
    assert page.locator(home.product_cart).text_content() == '1'
    page.click(home.add_to_cart_button.format("sauce-labs-bike-light"))
    assert page.locator(home.product_cart).text_content() == '2'
    page.click(home.add_to_cart_button.format("sauce-labs-bolt-t-shirt"))
    assert page.locator(home.product_cart).text_content() == '3'
    page.click(home.add_to_cart_button.format("sauce-labs-fleece-jacket"))
    assert page.locator(home.product_cart).text_content() == '4'
    page.click(home.add_to_cart_button.format("sauce-labs-onesie"))
    assert page.locator(home.product_cart).text_content() == '5'
    page.click(home.add_to_cart_button.format("test.allthethings()-t-shirt-(red)"))
    assert page.locator(home.product_cart).text_content() == '6'

def test_remove_product(page):
    login = LoginPage(page)
    login.open() 
    login.login("standard_user", "secret_sauce")
    home = HomePage(page)
    #Call the add product test to ensure products are in the cart before removing
    test_add_product(page)

    page.click(home.remove_from_cart_button.format("sauce-labs-backpack"))
    assert page.locator(home.product_cart).text_content() == '5'
    page.click(home.remove_from_cart_button.format("sauce-labs-bike-light"))
    assert page.locator(home.product_cart).text_content() == '4'
    page.click(home.remove_from_cart_button.format("sauce-labs-bolt-t-shirt"))
    assert page.locator(home.product_cart).text_content() == '3'
    page.click(home.remove_from_cart_button.format("sauce-labs-fleece-jacket"))
    assert page.locator(home.product_cart).text_content() == '2'
    page.click(home.remove_from_cart_button.format("sauce-labs-onesie"))
    assert page.locator(home.product_cart).text_content() == '1'
    page.click(home.remove_from_cart_button.format("test.allthethings()-t-shirt-(red)"))
    assert page.locator(home.product_cart).text_content() == ''