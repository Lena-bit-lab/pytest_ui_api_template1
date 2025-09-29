import pytest
import allure
from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    page = MainPage(driver)
    yield driver
    driver.quit()

def test_mytask(driver):
    page = MainPage(driver)
    page.open()
    page.check()

