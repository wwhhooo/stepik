from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input_value = browser.find_element(By.ID, "input_value").text
    res = calc(int(input_value))

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(res)

    browser.find_element(By.TAG_NAME, "button").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла