# pytest_ui_api_template1

# Дипломная работа на Python по Yougile

## Оглавление
- Описание
- Структура
- Инструкция по работе с тестами
- Стек технологий
- Установка библиотек

## Описание
Финальная работа по ручному тестированию:
https://github.com/Lena-bit-lab/pytest_ui_api_template1/tree/main 
Автотесты для API и UI-тестов для сайта YouGile (Система управления проектами для больших команд).

Сайт: https://ru.yougile.com/

## Структура
pages - классы

- pages/api_page.py
- pages/main_page.py
- 
tests - тесты

tests/test_api.py
tests/test_ui.py

pytest.ini - маркеры для запуска pytest

README.md - отчет-инструкция к работе

config.py - конфигурации

requirements.txt - зависимости

## Инструкция по работе с тестами
### Запуск API тестов:

1. Команда pytest 
tests/test_api.py --alluredir=./allure_result_api
2. После завершения тестирования вводим команду allure serve allure_result_api для просмотра отчета о тестировании

### Запуск UI тестов:

1. Команда pytest 
tests/test_ui.py --alluredir=./allure_result_ui
2. После завершения тестирования вводим команду allure serve allure_result_ui для просмотра отчета о тестировании


## Стек технологий
- Python - основной язык программирования для написания тестов
- pytest - фреймворк для написания и запуска тестов
- selenium - библиотека для автоматизации взаимодействия с веб-браузером
- requests - библиотека для работы с HTTP-клиентом, используемая для API-тестирования
- allure - инструмент для генерации отчетов о выполнении тестов


## Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
