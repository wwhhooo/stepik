from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Ivan")
    input_sname = browser.find_element(By.NAME, "lastname")
    input_sname.send_keys("Petrov")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("Ivan.Petrov@email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла