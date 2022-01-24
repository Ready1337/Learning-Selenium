# lesson link on Stepik: https://stepik.org/lesson/228249/step/8?unit=200781

from selenium import webdriver
import time
import os


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector('[name="firstname"]')
    first_name.send_keys('Yegor')

    last_name = browser.find_element_by_css_selector('[name="lastname"]')
    last_name.send_keys('Zinovyev')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('e.z@yandex.ru')

    attachments = browser.find_element_by_css_selector('[type="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    attachments.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

