from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим необходимые поля
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    answer = browser.find_element(By.CLASS_NAME, "form-control:required")

    #вычисляем значение
    x = x_element.text
    y = calc(x)

    #заполняем поле для ввода полученным значением
    answer.send_keys(y)

    #Отметить checkbox "I'm the robot". Выбрать radiobutton "Robots rule!".
    cbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    cbox.click()
    rbutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    rbutton.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()