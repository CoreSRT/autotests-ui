from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=2000 # 2 секунды между действиями, чтобы можно было уследить за всем, что происходит
    )
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим элементы, с которыми будем работать
    reg_button = page.get_by_test_id('registration-page-registration-button')
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')

    expect(reg_button).to_be_disabled()
    print('Кнопка в состоянии disabled')

    # Заполняем поля
    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    print('Данные введены')

    expect(reg_button).not_to_be_disabled()
    print('Кнопка перешла в состояние enabled')