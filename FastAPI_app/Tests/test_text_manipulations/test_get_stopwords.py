"""Тесты для модуля загрузки стоп-слов из внешних источников

Данный пакет содержит следующие тесты:
    * Unit-tests:
        ** Проверка действительности URL-ссылки на ресурс
        ** Проверка заполненности скаченного файла stopwords.txt
        ** Проверка успешной конкатенации списков стоп-слов с разных источников

Examples:
    $ pytest test_get_stopwords.py

Returns:
    > ==== 3 passed in 1.13s ====
"""

import pytest
import requests

from FastAPI_app.Tests import get_stopwords


@pytest.mark.parametrize(
    "link, expected_result",
    [
        ("https://drive.google.com/uc?export=download&id=17wVn5YPpMjHToctGgff_KfSeWcIIlf7c", 200)
    ]
)
def test_check_valid_link(link: str, expected_result: int):
    """
    Проверяет действительность URL-ссылки на ресурс
    Args:
        link (str): ссылка на ресурс
        expected_result (int): статус возвращаемого ответа
    """
    response = requests.get(link)
    assert response.status_code == expected_result


@pytest.mark.parametrize(
    "path_file, expected_num_of_strings",
[
        ("FastAPI_app/app/text_manipulations/stopwords.txt", 625)
    ]
)
def test_check_num_stopwords(path_file: str, expected_num_of_strings: int):
    """
    Проверяет что файл со стоп-словами дошел в целостности
    Args:
        path_file: путь до скачанного файла со стоп-словами
        expected_num_of_strings: количество строк файла со стоп-словами
    """
    stopwords_path = "./stopwords.txt"
    get_stopwords(stopwords_path)
    with open(stopwords_path, "r") as file:
        num_strings = len(file.readlines())
    assert num_strings == expected_num_of_strings


@pytest.mark.parametrize(
    "stop_file, expected_general_num",
    [
        ("./stopwords.txt", 776)
    ]
)
def test_check_general_stopwords(stop_file: str, expected_general_num: int):
    """
    Проверить статус конкатенации списков стоп-слов из разных источников
    Args:
        stop_file (str): путь файла с добоавочными стоп-словами
        expected_general_num (int): общее количество стоп-слов
    """
    num_stop_words = len(get_stopwords(stop_file))
    assert num_stop_words == expected_general_num