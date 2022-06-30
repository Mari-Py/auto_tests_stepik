import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import math
import time

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])
@pytest.mark.xfail(strict=True)
def test_guest(browser, links):
    answer = math.log(int(time.time()))

    link = f"{links}"

    browser = webdriver.Chrome()
    browser.get(link)

    # ищем поле ввода, вводим ответ
    inp_num = browser.find_element(By.ID, "ember91")
    inp_num.send_keys(answer)

    # кликаем "отправить"
    button2 = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button2.click()

    time.sleep(3)

    # находим элемент, содержащий текст, который надо проверить
    proverka = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")

    # записываем текст из элемента proverka
    pr_text = proverka.text

    assert pr_text == "Correct!", "Осознанное сообщение"