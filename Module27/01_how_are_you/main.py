from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:
    """Декоратор. Спрашивает "Как дела?",
    вне зависимости от ответа (ответ не сохраняется.)
    отвечает «А у меня не очень!»
    и только потом запускает саму функцию"""
    @functools.wraps(func)
    def operation(*args, **kwargs) -> Callable:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)
    return operation


@how_are_you
def test() -> None:
    """test - тестовая функция для проверки работы декоратора how_are_you"""
    print('<Тут что-то происходит...>')


test()
