from selenium import webdriver
import time
import math
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_tag_name("[name='firstname']")
    first_name.send_keys("Max")

    last_name = browser.find_element_by_tag_name("[name='lastname']")
    last_name.send_keys("Max")

    email = browser.find_element_by_tag_name("[name='email']")
    email.send_keys("Max")

    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    submit = browser.find_element_by_css_selector('[type = "submit"]')
    submit.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
