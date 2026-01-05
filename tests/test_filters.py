from playwright.sync_api import sync_playwright

def test_filters():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://saucedemo.com/")
        page.fill('input[id="user-name"]', 'standard_user')
        page.fill('input[id="password"]', 'secret_sauce')
        page.click('input[id="login-button"]')
        
        #Check that login was successful
        assert "Products" in page.text_content(".title")
        assert page.url == "https://www.saucedemo.com/inventory.html"

        # Apply a filter of Name (A to Z)
        page.select_option('select[class = product_sort_container]', 'az')

        # Verify that the filter was applied correctly
        assert page.locator('.inventory_item_name').first.text_content() == 'Sauce Labs Backpack'
        assert page.locator('.inventory_item_name').last.text_content() == 'Test.allTheThings() T-Shirt (Red)'


        # Apply a filter of Name (Z to A)
        page.select_option('select[class = product_sort_container]', 'za')

        # Verify that the filter was applied correctly
        assert page.locator('.inventory_item_name').first.text_content() == 'Test.allTheThings() T-Shirt (Red)'
        assert page.locator('.inventory_item_name').last.text_content() == 'Sauce Labs Backpack'


        # Apply a filter of low to high price
        page.select_option('select[class = product_sort_container]', 'lohi')

        # Verify that the filter was applied correctly
        assert page.locator('.inventory_item_price').first.text_content() == '$7.99'
        assert page.locator('.inventory_item_price').last.text_content() == '$49.99'


        # Apply a filter of high to low price
        page.select_option('select[class = product_sort_container]', 'hilo')

        # Verify that the filter was applied correctly
        assert page.locator('.inventory_item_price').first.text_content() == '$49.99'
        assert page.locator('.inventory_item_price').last.text_content() == '$7.99'

        browser.close()