from typing import Callable, Any
import functools
import datetime
import random


def log_dec(func: Callable) -> Callable:
    """Декоратор. Записывает в файл
    все вызванные ошибки и их время"""
    @functools.wraps(func)
    def logging(*args, **kwargs) -> Any:
        with open('error.log', 'a', encoding='utf-8') as file:
            try:
                answer = func(*args, **kwargs)
                return answer
            except Exception as ex:
                file.write(
                    f'Ошибка в функции "{func.__name__}" - '
                    f'{str(type(ex)).split('\'')[1]} - '
                    f'{datetime.datetime.now()}\n')
                return print(f'Ошибка в функции {func.__name__}\nДобавлена запись в error.log\n')
    return logging


@log_dec
def test() -> None:
    """Тестовая функция для проверки работы декоратора с вызовом ошибки"""
    print('<Тут что-то происходит...>')
    raise random.choice([TypeError, NameError, ZeroDivisionError, PermissionError, KeyError,
                         ArithmeticError, AssertionError, ConnectionAbortedError, OSError,
                         OverflowError, LookupError, ModuleNotFoundError, SyntaxError])


for iter_i in range(50):
    test()
