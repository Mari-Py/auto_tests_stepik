from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath("//input[ @required and contains (@class, 'form-control first')]")
    first_name.send_keys("req")
    second_name = browser.find_element_by_xpath("//input[ @required and contains (@class, 'form-control second')]")
    second_name.send_keys("req")
    email = browser.find_element_by_xpath("//input[ @required and contains (@class, 'form-control third')]")
    email.send_keys("req")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()