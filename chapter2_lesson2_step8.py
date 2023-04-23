from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name_field = browser.find_element(By.NAME, "firstname")
    name_field.send_keys("Ivan")
    lastName_field = browser.find_element(By.NAME, "lastname")
    lastName_field.send_keys("Petrov")
    email_field = browser.find_element(By.NAME, "email")
    email_field.send_keys("test@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.rtf')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()