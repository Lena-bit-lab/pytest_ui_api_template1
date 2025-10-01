import pytest
import requests
import allure


BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "EEAEvYZenR9jWSOcBBZrTZl7B4YwMqjL4P+ePJC7bmjx1z8PIAe12vxI1ufWUcTa"
HEADERS = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}

@pytest.fixture
@allure.feature("Создать проект с методом post")
@allure.story("API")
@allure.title("create_project_post")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
def test_create_project_post():
    with allure.step("Создаем позитивный запрос на создание проекта с методом post"):
        payload = {
        "title": "autotest",
        "users": {},
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r.status_code == 201, r.text
        "Ожидается статус-код 201"
        body = r.json()
        assert isinstance(body.get("id"), str)
        assert body["id"]


@pytest.fixture
@allure.feature("Создать проект с методом post без заголовка")
@allure.story("API")
@allure.title("create_project_post__400_without_title")
@pytest.mark.negative
@pytest.mark.api
@pytest.mark.smoke
def test_create_project_post__400_without_title():
    with allure.step("Создаем негативный запрос на создание проекта с методом post"):
        payload = {"users": {}}
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r.status_code == 400, r.text
        "Ожидается статус-код 400"


@pytest.fixture
@allure.feature("Вызвать проект с методом get")
@allure.story("API")
@allure.title("get_project_get__200")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
def test_get_project_get__200():
    with allure.step("Создаем позитивный запрос на вызов проекта с методом get"):
        r_create = requests.post(
        f"{BASE_URL}/projects",
        json={"title": "autotest", "users": {}},
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r_create.status_code == 201, r_create.text
        "Ожидается статус-код 201"
        project_id = r_create.json()["id"]
    r_get = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r_get.status_code == 200, r_get.text
        "Ожидается статус-код 200"
        assert r_get.json().get("id") == project_id


@pytest.fixture
@allure.feature("Вызвать проект с методом get c неизвестным ID")
@allure.story("API")
@allure.title("get_project_get__404_unknown_id")
@pytest.mark.negative
@pytest.mark.api
@pytest.mark.smoke
def test_get_project_get__404_unknown_id():
    with allure.step("Создаем негативный запрос на вызов проекта с методом get"):
        bogus_id = "111111"
    r = requests.get(
        f"{BASE_URL}/projects/{bogus_id}",
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r.status_code == 404, r.text
        "Ожидается статус-код 404"


@pytest.fixture
@allure.feature("Обновить проект с методом put")
@allure.story("API")
@allure.title("update_project_put")
@pytest.mark.positive
@pytest.mark.api
@pytest.mark.smoke
def test_update_project_put():
    with allure.step("Обновляем запрос на вызов проекта с методом put"):
        create_payload = {
        "title": "autotest",
        "users": {},
    }
    r_create = requests.post(
        f"{BASE_URL}/projects",
        json=create_payload,
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r_create.status_code == 201, r_create.text
        "Ожидается статус-код 201"
        project_id = r_create.json()["id"]

    new_title = create_payload["title"] + "_upd"
    r_put = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": new_title},
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r_put.status_code == 200, r_put.text
        "Ожидается статус-код 200"
        assert r_put.json().get("id") == project_id


@pytest.fixture
@allure.feature("Обновить проект с методом put с неизвестным ID")
@allure.story("API")
@allure.title("update_project_put__404_unknown_id")
@pytest.mark.negative
@pytest.mark.api
@pytest.mark.smoke
def test_update_project_put__404_unknown_id():
    with allure.step("Создаем негативный запрос на обновление проекта с неизвестным ID"):
        bogus_id = "111111"
    r = requests.put(
        f"{BASE_URL}/projects/{bogus_id}",
        json={"title": "x"},
        headers=HEADERS,
    )
    with allure.step("Проверяем статус-код"):
        assert r.status_code == 404, r.text
        "Ожидается статус-код 404"
