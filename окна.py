from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем элемент, считаем по формуле
    find_x = browser.find_element(By.ID, "input_value")
    x = find_x.text
    z = calc(x)

    #ищем форму ввода, скролим до неё и вводим результат расчета
    inp_num = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inp_num)
    inp_num.send_keys(z)

    #отмечаем чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    #отмечаем радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option1.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ждём 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()