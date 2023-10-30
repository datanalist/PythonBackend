import time
from math import gcd
from hashlib import md5
from .app import celery_app


@celery_app.task
def degree(num: int, deg: int) -> int:
    """
    Возвести число в степень
    Args:
        num(int): возводимое число
        deg(int): степень возводимого числа
    Returns:
        int: число в степени
    """
    return num**deg


@celery_app.task
def hcf(num: int, mum: int) -> int:
    """
    Найти НОД двух чисел
    Args:
        num: первое число
        mum: второе число
    Returns:
        int: НОД двух чисел
    """
    return gcd(num, mum)


@celery_app.task
def get_md5(string: str) -> str:
    """
    Возвращает md5-хэш от строки
    Args:
        string(str): входящая строка
    Returns:
        str: результат выполнения хэш-функции над строкой
    """
    hashh = md5(string.encode("UTF-8"))
    return hashh.hexdigest()