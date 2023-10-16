"""Тесты для модуля лемматизации текста

Данный пакет содержит следующие тесты:
    * Unit-tests:
        ** Проверка корректности лемматизации текста на 3-х примерах

Examples:
    $ pytest test_text_lemmatize.py

Returns:
    > ==== 1 failed, 2 passed, 37 warnings in 0.93s ====

Notes:
    Один тест будет провален, так как неверно определена первая форма слова: I-form('мыла') != 'мыло'
"""

import pytest

from FastAPI_app.Tests import text_lemmatize


@pytest.mark.parametrize(
    "arbitrary_text, expexted_lemmatize_text",
    [
        ("Мама мыла раму", "мама мыть рама"),
        ("На траве дрова, на дворе трава", "трава дрова двор трава"),
        ("Давай приколимся, пройдем по бардюр1234567у крыш.\nБудем говорить друг другу голосом потише...",
         "давать приколиться пройти бардюр крыша говорить друг друг голос тихий")
    ]
)
def test_text_lemmatize(arbitrary_text: str, expexted_lemmatize_text: str):
    """
    Проверить корректность процесса лемматизации текста
    Args:
        arbitrary_text (str): произвольный входной текст
        expexted_lemmatize_text (str): конечный лемматизированный и очищенный текст
    """
    lemm_list: list = text_lemmatize(arbitrary_text)
    resulted_lemmatize: str = " ".join(lemm_list)
    assert resulted_lemmatize == expexted_lemmatize_text