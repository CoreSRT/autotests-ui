from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=500
    )
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    reg_button = page.get_by_test_id('registration-page-registration-button')

    expect(reg_button).to_be_disabled()
