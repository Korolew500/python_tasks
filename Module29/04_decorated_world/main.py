from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def decor_f(*args, **kwargs):
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        return decorator
    return decor_f


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    @functools.wraps(func)
    def decor_f(*args, **kwargs):
        return func(*args, **kwargs)
    return decor_f


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
