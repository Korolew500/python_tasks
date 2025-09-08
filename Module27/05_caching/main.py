from typing import Callable
import functools


def casher(func: Callable) -> Callable:
    """Декоратор. Служит для хеширования результатов вычислений чисел Фибоначчи"""
    chash_dict = dict()

    @functools.wraps(func)
    def casher_fib(number: int):
        if number not in chash_dict:
            answer = func(number)
            chash_dict[number] = answer
        return chash_dict[number]
    return casher_fib


@casher
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и кеширован
