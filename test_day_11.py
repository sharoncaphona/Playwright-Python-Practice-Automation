def test_login(page, context):
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    context.tracing.stop(path="trace.zip")
