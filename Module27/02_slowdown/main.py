from typing import Callable
import functools
import time


def slowly_dec(func: Callable) -> Callable:
    """Декоратор. Замедляет работу функции на 3 секунды"""

    @functools.wraps(func)
    def slowly(*args, **kwargs) -> Callable:
        print('Система замедлена на 3 секунды')
        time.sleep(3)
        print('Процесс замедления завершен')
        return func(*args, **kwargs)
    return slowly


@slowly_dec
def test() -> None:
    """Тестовая функция для проверки работы декоратора"""
    print('<Тут что-то происходит...>')


test()
