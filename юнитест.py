from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Вводим данные в обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        input1.send_keys("Имя")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        input2.send_keys("Фамилия")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
        input3.send_keys("Имейл")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # проверяем ('что должно быть', 'что есть', 'что произошло')
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Не зарегистрирован")


    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Вводим данные в обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'input.first[required]')
        input1.send_keys("Имя")
        input2 = browser.find_element(By.CSS_SELECTOR, 'input.second[required]')
        input2.send_keys("Фамилия")
        input3 = browser.find_element(By.CSS_SELECTOR, 'input.third[required]')
        input3.send_keys("Имейл")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(2)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # проверяем ('что должно быть', 'что есть', 'что произошло')
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Не зарегистрирован")


if __name__ == "__main__":
    unittest.main()