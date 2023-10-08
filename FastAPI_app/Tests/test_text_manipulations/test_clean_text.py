"""Тесты для модуля очистки текста

Данный пакет содержит следующие тесты:
    * Unit-tests:
        ** Проверка удаления нечитабельных симовлов (-—.,:;_%©«»?*!@#№$^•·&()), цифр и []
        ** Проверка удаления символов табуляции
        ** Проверка замены символа переноса строки на пробел

Examples:
    $ pytest test_clean_text.py

Returns:
    > ==== 3 passed, 1 warning in 0.25s ====
"""

import pytest
from FastAPI_app.Tests import clean_text


@pytest.mark.parametrize(
    "text, expexted_result",
    [
        ("Проверка удаления нечитабельных симовлов (-—.,:;_%©«»?*!@#№$^•·&()), цифр и []",
         "проверка удаления нечитабельных симовлов цифр и")
    ]
)
def test_delete_unread_sym(text: str, expexted_result: str):
    """
    Проверить работоспособность функции на удаление (-—.,:;_%©«»?*!@#№$^•·&()), цифр и []
    Args:
        text (str): произвольный текст
        expexted_result (str): ожидаемый результат
    """
    cleaned_text = clean_text(text)
    assert cleaned_text == expexted_result


@pytest.mark.parametrize(
    "text, expexted_result",
    [
        ("Проверка       удаления    символов            табуляции",
         "проверка удаления символов табуляции")
    ]
)
def test_delete_tab_sym(text: str, expexted_result: str):
    """
    Проверить удаление символов табуляции
    Args:
        text (str): произвольный текст
        expexted_result (str): ожидаемый результат
    """
    cleaned_text = clean_text(text)
    assert cleaned_text == expexted_result


@pytest.mark.parametrize(
    "text, expexted_result",
    [
        ("Проверка замены символа\n переноса \n\nстроки на пробел\n",
         "проверка замены символа переноса строки на пробел")
    ]
)
def test_replace_enter(text: str, expexted_result: str):
    """
    Проверить работоспособность замены символа переноса строки на пробел
    Args:
        text (str): произвольный текст
        expexted_result (str): ожидаемый результат
    """
    cleaned_text = clean_text(text)
    assert cleaned_text == expexted_result