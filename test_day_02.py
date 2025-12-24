def test_day_02(page):
        # Navigate to the example.com page
        page.goto("https://www.saucedemo.com/")

        #Use id for this
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()
        # page.locator("#login-btn").click()

        # #Use class for this
        # page.locator(".input_error").nth(0).fill("standard_user")
        # page.locator(".input_error").nth(1).fill("secret_sauce")
        # page.locator(".submit-button").click()

        # #Use Role for this
        # page.get_by_role("textbox", name="Username").fill("standard_user")
        # page.get_by_role("textbox", name="Password").fill("secret_sauce")
        # page.get_by_role("button", name="Login").click()