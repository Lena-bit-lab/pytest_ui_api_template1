import allure
from selenium.webdriver.common.by import By


class Sample:
    """Класс предоставляет методы для работы со страницей Пример проекта приложения"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("После авторизации переходим на главную страницу"):
            self.driver.get("https://ru.yougile.com/team")

        with allure.step("Нажимаем на кнопку Пример проекта"):
            elements = self.driver.find_element(By.CLASS_NAME,
                                          "truncate")
        button = elements[0]
        button.click()

    def check(self):
            with allure.step("Проверяем переход на страницу Пример проекта"):
                assert (self.driver.current_url == "https://ru.yougile.com/team/f9826200841f/Пример-проекта")
