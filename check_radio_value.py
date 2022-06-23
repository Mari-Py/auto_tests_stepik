from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим картинку на странице, берём значение атрибута valuex и считаем его по формуле
    x_pict = browser.find_element(By.ID, "treasure")
    value1 = x_pict.get_attribute("valuex")
    y = calc(value1)

    #вводим ответ в текстовое поле
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    #находим и отмечаем checkbox
    check1 = browser.find_element(By.ID, 'robotCheckbox')
    check1.click()

    #находим и отмечам radiobutton
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()

    #кликаем по сабмит
    sbmt = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    sbmt.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()