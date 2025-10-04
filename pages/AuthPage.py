import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class AuthPage:
    """Класс предоставляет методы для работы со страницей авторизации приложения"""

    def __init__(self, driver):
        self.driver = webdriver.Chrome()
    def open(self):
        with allure.step("Открываем страницу сайта с меню"):
            self.driver.get("https://ru.yougile.com")

        with allure.step("Начинаем авторизацию, нажимая кнопки и вводя запрашиваемые данные"):
            self.entrance_button = self.driver.find_element(By.CLASS_NAME, "btn-outline-primary")
            self.entrance_button.click()

        with allure.step("Ожидание 5 секунд для стабильной работы"):
            self.wait = WebDriverWait(self.driver, 5)

            self.email_field = self.driver.find_element(By.CSS_SELECTOR, '.login-form-field[type="email"]')
            self.password_field = self.driver.find_element(By.CSS_SELECTOR, '.login-form-field[type="password"]')
            self.login_button = self.driver.find_element(By.CLASS_NAME, "cursor-pointer")

            self.email_field.send_keys("sulatomato@tiffincrane.com")
            self.password_field.send_keys("sulatomato")
            self.login_button.click()

    def check(self):
        with allure.step("Проверям, что выполнен вход на сайт"):
            assert (self.driver.current_url == "https://ru.yougile.com/team")
