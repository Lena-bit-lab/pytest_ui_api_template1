import allure
from selenium.webdriver.common.by import By


class Mytask:
    """Класс предоставляет методы для работы со страницей Мои задачи приложения"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("После авторизации переходим на главную страницу"):
            self.driver.get("https://ru.yougile.com/team")

        with allure.step("Нажимаем на кнопку Мои задачи"):
            elements = self.driver.find_element(By.CLASS_NAME,
                                          "text-panel-text-primary")
        button = elements[0]
        button.click()

    def check(self):
            with allure.step("Проверяем переход на страницу Мои задачи"):
                assert (self.driver.current_url == "https://ru.yougile.com/team/my-tasks")
