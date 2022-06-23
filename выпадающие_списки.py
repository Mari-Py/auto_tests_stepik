from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"
#http://suninjuly.github.io/selects1.html

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num1t = num1.text

    num2 = browser.find_element(By.ID, 'num2')
    num2t = num2.text

    x = int(num1t) + int(num2t)


    #ищем список, выбираем элемент по названию (по результату суммирования)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(x))

    #кликаем по сабмит
    sbmt = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    sbmt.click()


finally:
    time.sleep(15)
    browser.quit()

