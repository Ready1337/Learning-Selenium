# lesson link on Stepik: https://stepik.org/lesson/228249/step/3?unit=200781

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_css_selector('#num1').text)
    num2 = int(browser.find_element_by_css_selector('#num2').text)
    answer = num1 + num2

    answer_list = Select(browser.find_element_by_css_selector('#dropdown'))
    answer_list.select_by_value(f'{answer}')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
