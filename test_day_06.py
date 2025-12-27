from playwright.sync_api import sync_playwright, expect

def test_day_06(page):        
        #Navigate to the example.com page
        page.goto("https://the-internet.herokuapp.com/")
        page.click("text=Multiple Windows")

        #Verify we are on the correct page
        expect(page.locator("h3")).to_have_text("Opening a new window")

        #Click the link that open a new window
        with page.expect_popup() as popup:
            page.click("text=Click Here")

        new_page = popup.value

        #Verify the new window content
        expect(new_page.locator("h3")).to_have_text("New Window")