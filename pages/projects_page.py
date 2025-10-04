import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Projects:
    """Класс предоставляет методы для работы со страницей Моя компания (проекты) приложения"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("После авторизации переходим на главную страницу"):
            self.driver.get("https://ru.yougile.com/team")

        with allure.step("Нажимаем на кнопку Моя компания"):
            wait = WebDriverWait(self.driver, 60)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space(text())='Моя компания']")))
            button.click()

    def check(self):
        with allure.step("Проверяем переход на страницу Моя компания (проекты)"):
            assert (self.driver.current_url == "https://ru.yougile.com/team/projects")
