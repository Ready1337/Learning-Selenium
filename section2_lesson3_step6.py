# lesson link on Stepik: https://stepik.org/lesson/184253/step/6?unit=158843

import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    trollface_button = browser.find_element_by_css_selector('[class="trollface btn btn-primary"]')
    trollface_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_value = browser.find_element_by_css_selector('#input_value').text
    answer = calc(x_value)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(answer)

    submit_button = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
