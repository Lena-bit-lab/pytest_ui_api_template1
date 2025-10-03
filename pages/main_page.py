import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


# # class AuthPage:
# #     """Класс предоставляет методы для работы со страницей авторизации приложения"""
# #
# #     # def __init__(self, driver: WebDriver) -> None:
# #     #     self.__url = ConfigProvider().get("ui", "ui_auth_url")
# #     #     self.__driver = driver
# #
# #     @allure.step("Перейти на страницу авторизации")
# #     def go(self):
# #         self.driver.get("https://ru.yougile.com")
#
# class AuthPage:
#     def __init__(self, driver):
#
#         def __init__(self, driver: WebDriver) -> None:
#             def open(self):
#                 self.driver.get("https://ru.yougile.com")
#                 self.username_field = self.driver.find_element(By.CLASS_NAME, "sign-in-button".click())
#                 self.username_field = self.driver.find_element(By.CLASS_NAME, "sign-in-button")
#                 self.password_field = self.driver.find_element(By.CLASS_NAME, "login-form-input_input")
#                 self.login_button = self.driver.find_element(By.CLASS_NAME, "login-button")
#
#                 self.username_field.send_keys("sulatomato@tiffincrane.com")
#                 self.password_field.send_keys("sulatomato")
#                 self.login_button.click()
#
# # class AuthPage:
# #     """Класс предоставляет методы для работы со страницей авторизации приложения"""
# #
# #     # def __init__(self, driver: WebDriver) -> None:
# #     #     self.__url = ConfigProvider().get("ui", "ui_auth_url")
# #     #     self.__driver = driver
# #
# #     @allure.step("Перейти на страницу авторизации")
# #     def go(self):
# #         self.__driver.get("https://ru.yougile.com")
# #
# #     # def open(self):
# #     #     self.driver.get("https://ru.yougile.com")
# #
# #
# #     @allure.step("Авторизоваться под {sulatomato@tiffincrane.com}:{sulatomato}")
# #     def login_as(self, email: str, password: str):
# #
# #             with allure.step("Заполнить поле 'E-mail:'sulatomato@tiffincrane.com"):
# #                 self.__driver.find_element(By.CSS_SELECTOR, '[type="email"]').send_keys(email)
# #             with allure.step("Заполнить поле 'Пароль:'sulatomato"):
# #                 self.__driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys(password)
# #             with allure.step("Нажать кнопку 'Войти'"):
# #                 self.__driver.find_element(By.CSS_SELECTOR, '[role="button"]').click()
# #
# #     @allure.step("Получить текущий URL")
# #     def get_current_url(self) -> str:
# #         # Вернем текущий url
# #         return self.__driver.current_url
#
#     # @allure.step("Получить название компании пользователя")
#     # def current_company(self) -> str:
#     #     element = self.__driver.find_element(By.CSS_SELECTOR, ".mr-6.whitespace-nowrap.h1-semibold").text
#     #     return element
#
#     @allure.step("Открыть страницу сайта с меню")
#     # def open_project(self, name: str):
#     #     locator = f"'div[title=\"{name}\"]'"
#     #     print(locator)
#     #     self.__driver.find_element(By.CSS_SELECTOR, 'div[title="Clark and Sons"]').click()
#     #
#     def check(self):
#         assert (self.driver.current_url == "https://ru.yougile.com/team")

class Mytask:
    def __init__(self, driver):
        self.driver = driver
       # self.wait = WebDriverWait(driver, 5)
    def open(self):
        self.driver.get("https://ru.yougile.com/team")
        elements = self.driver.find_element(By.CLASS_NAME,
                                          "text-panel-text-primary")
        button = elements[0]
        button.click()

    def check(self):
        assert (self.driver.current_url == "https://ru.yougile.com/team/my-tasks")





