# pytest_ui_api_template1

# Дипломная работа на Python по YouGile

## Оглавление
- Описание
- Структура
- Инструкция по работе с тестами
- Стек технологий
- Установка библиотек

## Описание
Финальная работа по ручному тестированию

https://github.com/Lena-bit-lab/pytest_ui_api_template1

Автотесты для API и UI-тестов для сайта YouGile 
(Система управления проектами для больших команд)

[Сайт](https://ru.yougile.com/)


## Структура
_pages - классы_

- pages/AuthPage.py
- pages/main_page.py
- pages/profile_page.py
- pages/projects_page.py
- pages/sample_page.py

_tests - тесты_

- test/test_api.py
- test/test_ui.py

_pytest.ini - маркеры для запуска pytest_

_README.md - отчет-инструкция к работе_

_config.py - конфигурации_

_requirements.txt - зависимости_

## Инструкция по работе с тестами
### Запуск API тестов:

1. Команда pytest 
test/test_api.py --alluredir=./allure_result_api
2. После завершения тестирования вводим команду allure serve allure_result_api для просмотра отчета о тестировании

### Запуск UI тестов:

1. Команда pytest 
test/test_ui.py --alluredir=./allure_result_ui
2. После завершения тестирования вводим команду allure serve allure_result_ui для просмотра отчета о тестировании


## Стек технологий
- Python - основной язык программирования для написания тестов
- pytest - фреймворк для написания и запуска тестов
- selenium - библиотека для автоматизации взаимодействия с веб-браузером
- requests - библиотека для работы с HTTP-клиентом, используемая для API-тестирования
- allure - инструмент для генерации отчетов о выполнении тестов


