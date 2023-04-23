from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(a, b, s):
  if s == '+':
    return str(a + b)
  elif s == '-':
    return str(abs(a - b))


try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим необходимые поля
    a_num = browser.find_element(By.ID, "num1")
    b_num = browser.find_element(By.ID, "num2")
    s_num = browser.find_element(By.CSS_SELECTOR, "h2 .nowrap:nth-child(3)")
    a = int(a_num.text)
    b = int(b_num.text)
    s = s_num.text

    #вычисляем значение
    result = calc(a, b , s)

    # работа со списком
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()