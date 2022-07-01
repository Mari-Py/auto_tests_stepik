import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time

@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    # этот код выполнится после завершения теста (из-за yield)
    br.quit()

# в качестве аргументов передаётся изменяемая часть ссылок
@pytest.mark.parametrize('links', ['236895', '236896', '236897', '236898',
                                   '236899', '236903', '236904', '236905'])
def test_guest(browser, links):
    link = f'https://stepik.org/lesson/{links}/step/1'

    # ожидание прогрузки страницы
    browser.implicitly_wait(10)

    browser.get(link)

    # ищем поле ввода, вводим ответ
    browser.find_element(By.TAG_NAME, 'textarea').send_keys((str(math.log(int(time.time())))))

    # кликаем "отправить" когда появится кнопка
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()

    # находим элемент, содержащий текст, который надо проверить, берём из него текст
    check_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text

    assert check_text == "Correct!"
