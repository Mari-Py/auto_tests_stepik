from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #в течение 12 секунд ждём, что в элементе с id "price" появится текст "$100"
    price_wait = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    # ищем элемент, считаем по формуле
    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    z = calc(x)

    # ищем поле ввода, вводим результат расчета
    inp_num = browser.find_element(By.ID, "answer")
    inp_num.send_keys(z)

    # кликаем сабмит
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ждём 15 секунд
    time.sleep(15)
    # закрываем браузер
    browser.quit()