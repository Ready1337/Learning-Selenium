# lesson link on Stepik: https://stepik.org/lesson/193188/step/3?unit=167629

from selenium import webdriver
import unittest
import time
import pytest


class RegistrationTest(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        first_name.send_keys("Мой ответ")

        last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        last_name.send_keys("Мой ответ")

        email = browser.find_element_by_css_selector('input[placeholder = "Input your email"]')
        email.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        first_name.send_keys("Мой ответ")

        last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        last_name.send_keys("Мой ответ")

        email = browser.find_element_by_css_selector('input[placeholder = "Input your email"]')
        email.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)

        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
