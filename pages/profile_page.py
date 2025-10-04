import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Profile:
    """Класс предоставляет методы для работы со страницей Мой профиль приложения"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("После авторизации переходим на главную страницу"):
            self.driver.get("https://ru.yougile.com/team")

        with allure.step("Нажимаем на кнопку Мой профиль"):
            wait = WebDriverWait(self.driver, 60)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space(text())='Мой профиль']")))
            button.click()

    def check(self):
            with allure.step("Проверяем переход на страницу Мой профиль"):
                assert (self.driver.current_url == "https://ru.yougile.com/team/settings-account")
