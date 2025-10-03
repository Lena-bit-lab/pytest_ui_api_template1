import pytest
#import allure
from pages.main_page import Mytask
from pages.AuthPage import AuthPage
from selenium import webdriver


@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_mytask(driver):
    authpage = AuthPage(driver)
    authpage.open()
    page = Mytask(driver)
    page.open()
    page.check()


def test_auth_page(driver):
    page = AuthPage(driver)
    page.open()
    page.check()