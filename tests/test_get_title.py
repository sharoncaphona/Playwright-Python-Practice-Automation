from playwright.sync_api import sync_playwright


def test_get_title():
    with sync_playwright() as p:
        # Open the webkit browser in the headless mode
        browser = p.webkit.launch(headless=True)

        # Create a new browser context
        context = browser.new_context()

        # Create a new page in the browser context
        page = context.new_page()

        # Go the webpage
        page.goto("https://www.google.com")
        print(page.title())

        # Close the browser
        browser.close()
