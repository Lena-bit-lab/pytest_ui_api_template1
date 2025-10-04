import allure
from selenium.webdriver.common.by import By


class Projects:
    """Класс предоставляет методы для работы со страницей Моя компания (проекты) приложения"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("После авторизации переходим на главную страницу"):
            self.driver.get("https://ru.yougile.com/team")

        with allure.step("Нажимаем на кнопку Моя компания"):
            elements = self.driver.find_element(By.CLASS_NAME,
                                          "light-darker")
        button = elements[0]
        button.click()

    def check(self):
        with allure.step("Проверяем переход на страницу Моя компания (проекты)"):
            assert (self.driver.current_url == "https://ru.yougile.com/team/projects")
