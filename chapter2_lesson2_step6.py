from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input_field = browser.find_element(By.ID, "answer")


    #находим необходимые поля
    x_get = browser.find_element(By.ID, "input_value")
    x = int(x_get.text)

    #вычисляем значение
    result = calc(x)
    input_field.send_keys(result)


    button = browser.find_element(By.TAG_NAME, "button")
    radio_button_check = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    time.sleep(3)
    check_box_check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check_box_check.click()

    radio_button_check.click()
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()