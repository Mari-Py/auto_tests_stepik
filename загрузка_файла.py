from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #вводим данные в поля
    inp_1 = browser.find_element(By.NAME, "firstname")
    inp_1.send_keys("имя")
    inp_2 = browser.find_element(By.NAME, "lastname")
    inp_2.send_keys("фамилия")
    inp_2 = browser.find_element(By.NAME, "email")
    inp_2.send_keys("email")

    #загружаем файл txt, который лежит в той же директории, что и файл py

    # получаем путь к директории текущего исполняемого скрипта загрузка_файла.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "1.txt"
    # получаем путь к 1.txt
    file_path = os.path.join(current_dir, file_name)
    # ищем куда отправить (элемент) отправляем файл
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ждём 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()



