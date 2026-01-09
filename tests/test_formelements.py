from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        #Input Test Fields
        page.fill("#name","Dhanush")
        page.fill("#email","d@gma.com")
        page.fill("#phone","1234567890")
        page.fill("#textarea","This is a test Address of Dhanush.")
        
        #Radio Buttons
        #Select the first radio button & check if it is selected
        page.check("#male")
        assert page.is_checked("#male") == True

        #Select the first radio button & check if it is selected
        page.check("#female")
        assert page.is_checked("#female") == True
        

        #Checkboxes
        #Select the first checkbox & check if it is selected
        page.check("#sunday")
        assert page.is_checked("#sunday") == True

        browser.close()