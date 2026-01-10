from playwright.sync_api import sync_playwright

def test_add_product():
    with sync_playwright() as p:
        #Open the browser in the headless mode
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()
        page.goto("https://saucedemo.com/")
        page.fill('input[id="user-name"]', 'standard_user')
        page.fill('input[id="password"]', 'secret_sauce')
        page.click('input[id="login-button"]')
        
        #Check that login was successful
        assert "Products" in page.text_content(".title")
        assert page.url == "https://www.saucedemo.com/inventory.html"

        #Add prodcts
        # Product 1: Sauce Labs Backpack
        page.click('button[id = "add-to-cart-sauce-labs-backpack"]')
        assert page.locator('a[class="shopping_cart_link"]').text_content() == '1'

        # Product 2: Sauce Labs Bike Light
        page.click('button[id = "add-to-cart-sauce-labs-bike-light"]')
        assert page.locator('a[class="shopping_cart_link"]').text_content() == '2'

        # Product 3: Sauce Labs Bolt T-Shirt
        page.click('button[id = "add-to-cart-sauce-labs-bolt-t-shirt"]')
        assert page.locator('a[class="shopping_cart_link"]').text_content() == '3'

        # Product 4: Sauce Labs Fleece Jacket
        page.click('button[id = "add-to-cart-sauce-labs-fleece-jacket"]')
        assert page.locator('a[class="shopping_cart_link"]').text_content() == '4'

        # Product 5: Sauce Labs Onesie
        page.click('button[id = "add-to-cart-sauce-labs-onesie"]')
        assert page.locator('a[class="shopping_cart_link"]').text_content() == '5'

        # Product 6: Test.allTheThings() T-Shirt (Red)
        page.click('button[id = "add-to-cart-test.allthethings()-t-shirt-(red)"]')
        assert page.locator('a[class="shopping_cart_link"]').text_content() == '6'

        browser.close()