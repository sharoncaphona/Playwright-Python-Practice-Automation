from playwright.sync_api import sync_playwright

def test_file_download():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Go to a webpage that allows file upload
        page.goto("https://practice-automation.com/file-download/")
        
        # Initiate the file download
        with page.expect_download() as download_info:
            page.click(".download-on-click")
        download = download_info.value
        assert download.suggested_filename == "test.pdf"

def test_single_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Go to a webpage that allows file upload
        page.goto("https://practice-automation.com/file-upload/")

        # Upload the sinle file
        page.set_input_files("input[type='file']", "utils/test.pdf")
        page.click("#upload-btn")

        assert "Thank you for your message. It has been sent" 

def test_multiple_file_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to a webpage that allows file upload
        page.goto("https://testautomationpractice.blogspot.com/")

        # Upload multiple files
        page.set_input_files("#multipleFilesInput",["utils/test.pdf", "utils/test2.pdf"])
        page.click("button:has-text('Upload Multiple Files')")

        assert "Multiple files selected:" in page.text_content("#multipleFilesStatus")