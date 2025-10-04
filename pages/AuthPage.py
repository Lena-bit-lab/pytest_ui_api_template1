import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:
    """Класс предоставляет методы для работы со страницей авторизации приложения"""

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        with allure.step("Открываем страницу сайта с меню"):
            self.driver.get("https://ru.yougile.com")

        with allure.step("Начинаем авторизацию, нажимая кнопки и вводя запрашиваемые данные"):
            self.entrance_button = self.driver.find_element(By.CLASS_NAME, "btn-outline-primary")
            self.entrance_button.click()

        with allure.step("Ожидание 60 секунд для стабильной работы"):
            wait = WebDriverWait(self.driver, 60)

            self.email_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
            self.password_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
            self.login_button = self.driver.find_element(By.CLASS_NAME, "cursor-pointer")

            self.email_field.send_keys("sulatomato@tiffincrane.com")
            self.password_field.send_keys("sulatomato")
            self.login_button.click()

        with allure.step("Ожидание загрузки главной страницы"):
            self.my_profile_btn = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Мой профиль']")))

    def check(self):
        with allure.step("Проверям, что выполнен вход на сайт"):
            assert self.my_profile_btn.is_displayed()
            assert "SkyPro" in self.driver.title
