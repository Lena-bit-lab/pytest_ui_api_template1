import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


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
