from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input_value = browser.find_element(By.ID, "treasure")

    X = input_value.get_attribute('valuex')

    res = calc(int(X))

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(res)

    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()

    check = browser.find_element(By.ID, "robotsRule")
    check.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла