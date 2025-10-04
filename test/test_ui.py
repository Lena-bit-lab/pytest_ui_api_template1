import pytest
import allure
from selenium import webdriver
from pages.AuthPage import AuthPage
from pages.main_page import Mytask
from pages.profile_page import Profile
from pages.projects_page import Projects
from pages.sample_page import Sample


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.title("Тест на авторизацию на сайте")
def test_auth_page(driver):
    page = AuthPage(driver)
    page.open()
    page.check()

@allure.title("Тест на работу кнопки Мои задачи и переход на страницу с задачами (после предварительной авторизации")
def test_mytask(driver):
    authpage = AuthPage(driver)
    authpage.open()
    page = Mytask(driver)
    page.open()
    page.check()

@allure.title("Тест на работу кнопки Мой профиль и переход на страницу с настройками профиля (после предварительной авторизации")
def test_profile(driver):
    authpage = AuthPage(driver)
    authpage.open()
    page = Profile(driver)
    page.open()
    page.check()

@allure.title("Тест на работу кнопки Мои задачи и переход на страницу с проектами (после предварительной авторизации")
def test_projects(driver):
    authpage = AuthPage(driver)
    authpage.open()
    page = Projects(driver)
    page.open()
    page.check()

@allure.title("Тест на работу кнопки Пример проекта и переход на страницу с примерами проекта (после предварительной авторизации")
def test_sample(driver):
    authpage = AuthPage(driver)
    authpage.open()
    page = Sample(driver)
    page.open()
    page.check()
