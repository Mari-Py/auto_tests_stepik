from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем на кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # соглашаемся со всплывающим окном
    confirm = browser.switch_to.alert
    confirm.accept()

    # ищем элемент, считаем по формуле
    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    z = calc(x)

    # ищем поле ввода, вводим результат расчета
    inp_num = browser.find_element(By.ID, "answer")
    inp_num.send_keys(z)

    #кликаем сабмит
    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()

finally:
    # ждём 15 секунд
    time.sleep(15)
    # закрываем браузер
    browser.quit()