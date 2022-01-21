# lesson link on Stepik: https://stepik.org/lesson/165493/step/7?unit=140087

import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    answer = calc(x)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(answer)

    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()

    robot_radio_button = browser.find_element_by_css_selector("#robotsRule")
    robot_radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
