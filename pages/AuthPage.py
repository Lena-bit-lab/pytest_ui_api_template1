import allure
from selenium import webdriver
#from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class AuthPage:
    """Класс предоставляет методы для работы со страницей авторизации приложения"""

    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get("https://ru.yougile.com")
        self.entrance_button = self.driver.find_element(By.CLASS_NAME, "btn-outline-primary")
        self.entrance_button.click()
        self.wait = WebDriverWait(self.driver, 5)
        self.username_field = self.driver.find_element(By.CSS_SELECTOR, "email")
        self.password_field = self.driver.find_element(By.CSS_SELECTOR, "password")
        self.login_button = self.driver.find_element(By.CLASS_NAME, "gap-4 cursor-pointer")

        self.username_field.send_keys("sulatomato@tiffincrane.com")
        self.password_field.send_keys("sulatomato")
        self.login_button.click()

    def check(self):
        assert (self.driver.current_url == "https://ru.yougile.com/team")

    #with allure.step("Открыть страницу сайта с меню"):