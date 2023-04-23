from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_input = browser.find_element(By.ID, "input_value")
    x = x_input.text

    result = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()