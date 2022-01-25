# lesson link on Stepik: https://stepik.org/lesson/184253/step/4?unit=158843

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    submit_button = browser.find_element_by_css_selector('[type="submit"]')
    submit_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_value = browser.find_element_by_css_selector('#input_value').text
    answer = calc(x_value)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(answer)

    submit_button = browser.find_element_by_css_selector('[class="btn btn-primary"]')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
