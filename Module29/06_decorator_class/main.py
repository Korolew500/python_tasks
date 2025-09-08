import time
import functools
from typing import Callable


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:

        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Callable:

        start = time.time()
        self.result = self.func(*args, **kwargs)
        all_time = time.time() - start

        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args}, {kwargs}')
        print(f'Результат: {self.result}')
        print(f'Время выполнения: {all_time} секунд')

        return self.result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result_1 = complex_algorithm(10, 50)
