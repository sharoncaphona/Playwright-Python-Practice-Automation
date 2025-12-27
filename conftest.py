import pytest
from playwright.sync_api import sync_playwright

# @pytest.fixture
# def page():
#     with sync_playwright() as p:
#         #In which mode you want to run the browser & speed of execution
#         browser = p.chromium.launch(headless=False, slow_mo=500)
#         page= browser.new_page()
#         yield page
#         browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")