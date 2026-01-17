from playwright.sync_api import sync_playwright

def test_popup_alert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practice-automation.com/popups/")
        page.on("dialog", lambda dialog: dialog.accept())
        page.click("#alert")

def test_popup_confirm_ok():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practice-automation.com/popups/")
        page.on("dialog", lambda dialog: dialog.accept())
        page.click("#confirm")

def test_popup_confirm_cancel():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practice-automation.com/popups/")
        page.on("dialog", lambda dialog: dialog.dismiss())
        page.click("#confirm")

def test_popup_prompt():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://practice-automation.com/popups/")
        page.on("dialog", lambda dialog: dialog.accept("Hello World"))
        page.click("#prompt")