from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    context = browser.new_context()
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    # Находим элементы
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    # Заполняем формы и жмем кнопку регистрации:

    email_input.fill('some@mail.com')
    username_input.fill('someusername')
    password_input.fill('somepassword')
    registration_button.click()

    # Сохраняем состояние
    context.storage_state(path='state-for-courses.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False
    )
    context = browser.new_context(storage_state='state-for-courses.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # Теперь нам понадобятся:
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    no_result_text = page.get_by_test_id('courses-list-empty-view-title-text')
    empty_description_text = page.get_by_test_id('courses-list-empty-view-description-text')

    # Проводим операции с найденными элементами
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')
    print('Заголовок отображается верно')

    expect(no_result_text).to_be_visible()
    expect(no_result_text).to_have_text('There is no results')
    print('Уведомление об отсутствии результатов отображается верно')

    expect(folder_icon).to_be_visible() # Потому что если его нет в наличии, тест все равно упадет, я уточнял
    print('Иконка пустого блока отображается на странице')

    expect(empty_description_text).to_be_visible()
    expect(empty_description_text).to_have_text('Results from the load test pipeline will be displayed here')
    print('Текст об отображении результатов нагрузочного тестирования отображается верно')
