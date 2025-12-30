from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://saucedemo.com/")
        page.fill('input[id="user-name"]', 'standard_user')
        page.fill('input[id="password"]', 'secret_sauce')
        page.click('input[id="login-button"]')
        
        #Check that login was successful
        assert "Products" in page.text_content(".title")
        assert page.url == "https://www.saucedemo.com/inventory.html"
        
        browser.close()