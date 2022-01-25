# lesson link on Stepik: https://stepik.org/lesson/181384/step/8?unit=156009

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_css_selector('#book')
    button.click()

    x_value = browser.find_element_by_css_selector('#input_value').text
    answer = calc(x_value)

    answer_field = browser.find_element_by_css_selector('#answer')
    answer_field.send_keys(answer)

    submit_button = browser.find_element_by_css_selector('#solve')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
