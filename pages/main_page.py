import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class AuthPage:
    """Класс предоставляет методы для работы со страницей авторизации приложения"""

    # def __init__(self, driver: WebDriver) -> None:
    #     self.__url = ConfigProvider().get("ui", "ui_auth_url")
    #     self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self):
        self.__driver.get("https://ru.yougile.com")


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)


    def open(self):
        self.driver.get("https://ru.yougile.com/team")

        elements = self.driver.find_element(By.CLASS_NAME,
                                          "text-panel-text-primary")
        #button.click()
        print(elements)

    def check(self):
        assert (self.driver.current_url == "https://ru.yougile.com/team/my-tasks")



