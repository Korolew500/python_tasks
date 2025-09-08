from typing import Callable
import functools


"""Служит базой данных для декоратора counter"""
data_dict = dict()


def counter(func: Callable) -> Callable:
    """Декоратор. Считает сколько раз была вызвана каждая функция,
    записывает в словарь data_dict и выводит его в консоль"""
    @functools.wraps(func)
    def operation(*args, **kwargs) -> Callable:
        if str(func.__name__) in data_dict:
            data_dict[str(func.__name__)] += 1
        else:
            data_dict[str(func.__name__)] = 1
        answer = func(*args, **kwargs)
        for i_func in sorted(data_dict.keys()):
            print(f'Функция {i_func} была вызвана уже {data_dict[i_func]} раз.')
        return answer
    return operation


@counter
def test_1() -> None:
    """Тестовая функция для проверки работы декоратора"""
    print('<Тут что-то происходит...>')


@counter
def test_2() -> None:
    """Тестовая функция для проверки работы декоратора"""
    print('<Тут что-то происходит...>')


@counter
def test_3() -> None:
    """Тестовая функция для проверки работы декоратора"""
    print('<Тут что-то происходит...>')


"""Каждую тестовую функцию вызовем разное количество раз"""
for iter_i in range(9):
    test_1()
    test_2()
    test_2()
    test_3()
    test_3()
    test_3()
