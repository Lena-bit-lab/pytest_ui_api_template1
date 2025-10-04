import allure
from selenium.webdriver.common.by import By


class Profile:
    """Класс предоставляет методы для работы со страницей Мой профиль приложения"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("После авторизации переходим на главную страницу"):
            self.driver.get("https://ru.yougile.com/team")

        with allure.step("Нажимаем на кнопку Мой профиль"):
            elements = self.driver.find_element(By.CLASS_NAME,
                                          "leading-4")
        button = elements[0]
        button.click()

    def check(self):
            with allure.step("Проверяем переход на страницу Мой профиль"):
                assert (self.driver.current_url == "https://ru.yougile.com/team/settings-account")
