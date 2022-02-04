# lesson link on Stepik: https://stepik.org/lesson/237240/step/3?unit=209628

import time
import math
import pytest
from selenium import webdriver


link_params = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', link_params)
def test_parametrization(browser, link):
    browser.implicitly_wait(30)
    browser.get(link)

    answer_field = browser.find_element_by_css_selector('[class="ember-text-area ember-view textarea string-quiz__textarea"]')
    answer = str(math.log(int(time.time())))
    answer_field.send_keys(answer)

    submit_button = browser.find_element_by_css_selector('[class="submit-submission"]')
    submit_button.click()

    test_value = browser.find_element_by_css_selector('[class="smart-hints__hint"]').text
    browser.quit()
    print(test_value)

    assert test_value == 'Correct!'
