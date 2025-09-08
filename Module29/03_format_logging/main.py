import functools
import time
from datetime import datetime
from typing import Callable


def time_string(time_conf: str) -> str:

    """Функция принимает формат даты и времени.
    Возвращает текущие дату и время заданного формата."""

    data_str = ''
    for i_symbol in time_conf:
        if i_symbol.isalpha():
            data_str += '%'
        data_str += i_symbol
    return datetime.now().strftime(data_str)


def log_method(time_str):
    def decor_all(func):
        @functools.wraps(func)
        def decor(*args, **kwargs):
            print(f'Запускается {func.__qualname__}'
                  f'. Дата и время запуска:', time_string(time_str))
            start_time = time.time()
            result = func(*args, **kwargs)
            all_time = time.time() - start_time
            print(f'Завершение {func.__qualname__}'
                  f', время работы = {round(all_time, 3)}s')
            return result
        return decor
    return decor_all


def log_methods(time_conf: str) -> Callable:
    def decor_all(cls):
        for name_method in dir(cls):
            if '__' not in name_method:
                cur_met = getattr(cls, name_method)
                decor_met = log_method(time_conf)
                decor_method = decor_met(cur_met)
                setattr(cls, name_method, decor_method)
        return cls
    return decor_all


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self) -> int:
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
